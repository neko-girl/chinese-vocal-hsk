/**
 * Audio Manager for Chinese Vocal HSK & Flashcard System.
 * Handles multi-voice playback with random voice selection across:
 *   1. Mature Woman (成熟女性)
 *   2. Soothing Host (温润女主播)
 *   3. Office Man (职场男音)
 *   4. Tender CEO (霸道/温润总裁)
 *
 * Falls back seamlessly to Web Speech API TTS when audio files are not present.
 */

const AudioManager = (function() {
  'use strict';

  let currentAudio = null;
  let activeSpeakingElements = [];
  let cachedChineseVoices = [];

  const VOICE_LABELS = {
    mature_woman: '👩 Mature Woman (成熟女性 / 晓晓)',
    soothing_host: '🎙️ Soothing Host (温润女主播 / 晓依)',
    office_man: '💼 Office Man (职场男音 / 云扬)',
    tender_ceo: '👔 Tender CEO (霸道总裁 / 云健)'
  };

  /**
   * Loads and caches all available Chinese voices in the browser.
   */
  function loadChineseVoices() {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) return [];
    try {
      const all = window.speechSynthesis.getVoices() || [];
      cachedChineseVoices = all.filter(v => {
        const lang = (v.lang || '').toLowerCase();
        const name = (v.name || '').toLowerCase();
        return lang.startsWith('zh') || lang.startsWith('cmn') ||
               name.includes('chinese') || name.includes('mandarin') || name.includes('putonghua');
      });
      return cachedChineseVoices;
    } catch (e) {
      return [];
    }
  }

  // Pre-load voices on startup & subscribe to async voicesready
  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    loadChineseVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.onvoiceschanged = () => loadChineseVoices();
    }
  }

  /**
   * Retrieves all Chinese voices installed or available in this browser.
   */
  function getAvailableChineseVoices() {
    if (!cachedChineseVoices.length) {
      loadChineseVoices();
    }
    return cachedChineseVoices;
  }

  /**
   * Picks the highest quality neural / natural Chinese voice.
   * Priority: Microsoft Online Natural (Xiaoxiao/Yunxi) > Google Neural > Apple Enhanced > Other.
   */
  function getBestChineseVoice(preferredVoiceURI = null) {
    const voices = getAvailableChineseVoices();
    if (!voices.length) return null;

    if (preferredVoiceURI) {
      const match = voices.find(v => v.voiceURI === preferredVoiceURI || v.name === preferredVoiceURI);
      if (match) return match;
    }

    // Heuristic neural ranking
    const scored = voices.map(v => {
      let score = 0;
      const n = (v.name || '').toLowerCase();
      const l = (v.lang || '').toLowerCase();

      // Microsoft Edge / Azure Online Natural voices (world's best)
      if (n.includes('natural') || n.includes('online')) score += 50;
      if (n.includes('xiaoxiao') || n.includes('yunxi') || n.includes('yunyang') || n.includes('xiaoyi') || n.includes('yunjian')) score += 40;
      // Google Chrome Neural
      if (n.includes('google') || n.includes('普通话') || n.includes('china')) score += 30;
      // Apple Siri / Enhanced
      if (n.includes('enhanced') || n.includes('premium') || n.includes('siri') || n.includes('ting-ting')) score += 25;
      // Remote cloud synthesis (higher fidelity than local robot)
      if (v.localService === false) score += 20;
      // Prefer Mainland Mandarin
      if (l === 'zh-cn' || l === 'zh_cn' || l.startsWith('zh-cn')) score += 10;
      // Demote robotic eSpeak if other options exist
      if (n.includes('espeak')) score -= 50;

      return { voice: v, score };
    });

    scored.sort((a, b) => b.score - a.score);
    return scored[0]?.voice || voices[0];
  }

  /**
   * Clears any active .speaking visual highlights on buttons/elements.
   */
  function clearVisualSpeaking() {
    activeSpeakingElements.forEach(el => {
      try {
        if (el && el.classList) el.classList.remove('speaking');
      } catch (e) {}
    });
    activeSpeakingElements = [];
    document.querySelectorAll('.speaking').forEach(el => el.classList.remove('speaking'));
  }

  /**
   * Adds .speaking class to the triggered element and global audio buttons.
   */
  function setVisualSpeaking(triggerEl) {
    clearVisualSpeaking();
    if (triggerEl && triggerEl.classList) {
      triggerEl.classList.add('speaking');
      activeSpeakingElements.push(triggerEl);
    }
    // Also highlight main hero audio buttons if playing headword
    const heroBtns = document.querySelectorAll('.hero-audio-btn, .audio-control-cluster button');
    heroBtns.forEach(b => {
      b.classList.add('speaking');
      activeSpeakingElements.push(b);
    });
  }

  /**
   * Web Speech API TTS Fallback.
   */
  function speakTTS(text, speed = 1.0, triggerEl = null) {
    if (!('speechSynthesis' in window)) {
      console.warn('Speech synthesis not supported in this browser.');
      return;
    }

    try {
      window.speechSynthesis.cancel();
      if (!text) return;

      const hanziOnly = (text.match(/[\u4e00-\u9fa5]+/g) || []).join('');
      const toSpeak = hanziOnly || text;

      const u = new SpeechSynthesisUtterance(toSpeak);
      u.lang = 'zh-CN';

      const settings = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings() : null;
      u.rate = (typeof speed === 'number') ? speed : (settings?.speechRate || 0.9);

      // Select highest quality neural voice
      const bestVoice = getBestChineseVoice(settings?.browserVoiceURI);
      if (bestVoice) {
        u.voice = bestVoice;
        u.lang = bestVoice.lang || 'zh-CN';
      }

      setVisualSpeaking(triggerEl);

      u.onend = () => clearVisualSpeaking();
      u.onerror = () => clearVisualSpeaking();

      window.speechSynthesis.speak(u);
    } catch (err) {
      console.warn('TTS playback error:', err);
      clearVisualSpeaking();
    }
  }

  /**
   * Selects an audio URL from an audio mapping object.
   * If voice preference in settings is 'random' (default), chooses randomly between all available voices.
   *
   * @param {Object|string} audioData - Map of { voice_key: url } or single url string
   * @returns {{ url: string|null, voice: string|null }}
   */
  function selectAudioUrl(audioData) {
    if (!audioData) return { url: null, voice: null };

    if (typeof audioData === 'string') {
      return { url: audioData, voice: 'default' };
    }

    if (typeof audioData !== 'object') return { url: null, voice: null };

    const settings = (typeof StorageManager !== 'undefined') ? StorageManager.getSettings() : {};
    const preferredVoice = settings.preferredVoice || 'random';

    // If user locked a specific voice preference and that audio file exists
    if (preferredVoice !== 'random' && audioData[preferredVoice]) {
      return { url: audioData[preferredVoice], voice: preferredVoice };
    }

    // Default: Pick randomly between all available voices
    const availableEntries = Object.entries(audioData).filter(([k, url]) => url && typeof url === 'string');
    if (availableEntries.length === 0) return { url: null, voice: null };

    const randomIndex = Math.floor(Math.random() * availableEntries.length);
    const [selectedVoice, selectedUrl] = availableEntries[randomIndex];

    return { url: selectedUrl, voice: selectedVoice };
  }

  /**
   * Plays audio with random voice selection across the 4 MiniMax personas.
   * Falls back to TTS if no audio file is found or on network error.
   *
   * @param {Object|string|null} audioData - { mature_woman: '...', soothing_host: '...', ... }
   * @param {string} fallbackText - Chinese text to speak via TTS if audio is missing
   * @param {number} speed - Playback speed (e.g. 0.75 or 1.0)
   * @param {HTMLElement|null} triggerEl - Optional button or element that triggered the playback
   */
  function play(audioData, fallbackText = '', speed = 1.0, triggerEl = null) {
    stop();

    const { url, voice } = selectAudioUrl(audioData);

    if (url) {
      try {
        const audio = new Audio(url);
        audio.playbackRate = (typeof speed === 'number' && speed > 0) ? speed : 1.0;
        currentAudio = audio;

        setVisualSpeaking(triggerEl);

        audio.onended = () => {
          clearVisualSpeaking();
          currentAudio = null;
        };

        audio.onerror = (e) => {
          console.warn(`Audio playback failed for ${url}, falling back to TTS:`, e);
          clearVisualSpeaking();
          currentAudio = null;
          speakTTS(fallbackText, speed, triggerEl);
        };

        const playPromise = audio.play();
        if (playPromise !== undefined) {
          playPromise.catch(err => {
            console.warn(`Audio autoplay blocked or failed (${url}):`, err);
            clearVisualSpeaking();
            currentAudio = null;
            speakTTS(fallbackText, speed, triggerEl);
          });
        }
        return;
      } catch (err) {
        console.warn('Audio construction error, falling back to TTS:', err);
      }
    }

    // Fallback: Web Speech API TTS
    speakTTS(fallbackText, speed, triggerEl);
  }

  /**
   * Stops any currently playing audio or speech synthesis.
   */
  function stop() {
    if (currentAudio) {
      try {
        currentAudio.pause();
        currentAudio.currentTime = 0;
      } catch (e) {}
      currentAudio = null;
    }
    if ('speechSynthesis' in window) {
      try {
        window.speechSynthesis.cancel();
      } catch (e) {}
    }
    clearVisualSpeaking();
  }

  return {
    play,
    stop,
    speakTTS,
    selectAudioUrl,
    getAvailableChineseVoices,
    getBestChineseVoice,
    VOICE_LABELS
  };
})();

// Export globally
window.AudioManager = AudioManager;

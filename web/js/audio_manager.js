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

  const VOICE_LABELS = {
    mature_woman: '👩 Mature Woman (成熟女性)',
    soothing_host: '🎙️ Soothing Host (温润女主播)',
    office_man: '💼 Office Man (职场男音)',
    tender_ceo: '👔 Tender CEO (霸道/温润总裁)'
  };

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
    VOICE_LABELS
  };
})();

// Export globally
window.AudioManager = AudioManager;

# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 播放
    {
        "id": "31",
        "hanzi": "播放",
        "pinyin": "bō fàng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to broadcast; to transmit; to play (video or audio)",
            "es": "reproducir; emitir; transmitir; difundir (audio o vídeo)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to transmit sound or images through radio, television, internet, or playback devices",
                "definition_es": "transmitir o emitir señales sonoras o visuales a través de medios de difusión o reproductores",
                "example_phrase": "播放背景音乐 (play background music)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "电影院的大银幕上正在播放最新上映的科幻大片，震撼的音效让观众仿佛身临其境。",
                "pinyin": "Diànyǐngyuàn de dàyínmù shàng zhèngzài bōfàng zuìxīn shàngyìng de kēhuàn dàpiān, zhènhàn de yīnxiào ràng guānzhòng fǎngfú shēnlín-qíjìng.",
                "en": "The cinema's big screen was playing the newly released sci-fi blockbuster, its stunning sound effects immersing the audience.",
                "es": "En la gran pantalla del cine se reproducía el último estreno de ciencia ficción, cuyos vibrantes efectos envolvían a los espectadores."
            },
            {
                "id": "#2",
                "hanzi": "国家广播电台每天清晨准时向全国各地的听众播放早间新闻与天气预报节目。",
                "pinyin": "Guójiā guǎngbō diàntái měitiān qīngchén zhǔnshí xiàng quánguó gèdì de tīngzhòng bōfàng zǎojiān xīnwén yǔ tiānqì yùbào jiémù.",
                "en": "The national radio station broadcasts morning news and weather forecast programs punctually to listeners nationwide.",
                "es": "La radio nacional emite puntualmente cada mañana el noticiario matutino y el pronóstico del tiempo para la audiencia de todo el país."
            }
        ],
        "collocations": [
            {"hanzi": "播放音乐", "en": "play music"},
            {"hanzi": "播放视频", "en": "play video"},
            {"hanzi": "循环播放", "en": "loop playback / play on repeat"},
            {"hanzi": "暂停播放", "en": "pause playback"},
            {"hanzi": "正在播放", "en": "currently playing / now showing"},
            {"hanzi": "播放列表", "en": "playlist"}
        ],
        "idioms": [
            {"hanzi": "绘声绘色", "pinyin": "huì shēng huì sè", "meaning_en": "vivid and lively description in sound and color"},
            {"hanzi": "口口相传", "pinyin": "kǒu kǒu xiāng chuán", "meaning_en": "passed on from mouth to mouth; oral tradition"},
            {"hanzi": "声情并茂", "pinyin": "shēng qíng bìng mào", "meaning_en": "rich in both voice and emotion; expressive recitation"},
            {"hanzi": "广为流传", "pinyin": "guǎng wéi liú chuán", "meaning_en": "widely circulated and propagated"}
        ],
        "character_decomposition": [
            {
                "character": "播",
                "pinyin": "bō",
                "meaning_en": "sow; spread; broadcast; scatter",
                "meaning_es": "sembrar; esparcir; difundir; emitir",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand casting seeds) + 番 (turning paws / spread)",
                "sound_component": "番 (fān/bō, turn over / phonetic)",
                "stroke_count": 15,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with 番; scattering seeds wide across fields, extended to scattering electromagnetic waves into the air.",
                "visual_mnemonic_story_en": "A hand (扌) scatters grain (番) across fields, just as a transmitter scatters broadcast signals (播).",
                "visual_mnemonic_story_es": "Una mano (扌) esparce simiente (番) en el sembrado, igual que una antena difunde ondas al aire (播).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QHDW",
                "traditional": ""
            },
            {
                "character": "放",
                "pinyin": "fàng",
                "meaning_en": "release; let go; place; bloom",
                "meaning_es": "soltar; liberar; colocar; florecer",
                "radical": "攵",
                "radical_meaning_en": "tap / action",
                "meaning_component": "方 (square / side) + 攵 (whip / tap)",
                "sound_component": "方 (fāng, square / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand driving cattle with a whip 攵 out into the four directions 方; signifies releasing, setting free, or letting out.",
                "visual_mnemonic_story_en": "Livestock are guided outward in all directions (方) by a herder (攵) to graze freely (放).",
                "visual_mnemonic_story_es": "El ganado es guiado hacia las cuatro direcciones (方) por el pastor (攵) para pastar libre (放).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YSK",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Scattering waves (播) and releasing them freely into the atmosphere (放) broadcasts programs (播放).",
            "composite_memory_hook_es": "Esparcir ondas (播) y liberarlas al éter (放) reproduce y emite las señales (播放).",
            "cultural_and_cognitive_roots": "Agricultural metaphor: ancient farmers broadcast seeds (播种), which modern telecommunications borrowed to mean radio diffusion (广播) and audiovisual playback.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'bō fàng' (55-51). Hold high pitch 55 on 'bō', then descend decisively on 'fàng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "插", "pinyin": "chā", "meaning_en": "insert; stick in", "distinction_note": "Has 臿 on right of 扌 instead of 番 in 播"},
                {"character": "潘", "pinyin": "pān", "meaning_en": "surname; river", "distinction_note": "Has water radical 氵 on left of 番"},
                {"character": "房", "pinyin": "fáng", "meaning_en": "house; room", "distinction_note": "Has door radical 户 atop 方 instead of 攵 in 放"},
                {"character": "防", "pinyin": "fáng", "meaning_en": "defend; prevent", "distinction_note": "Has hill radical 阝 on left of 方"}
            ],
            "etymological_cognates": [
                {"character": "传", "pinyin": "chuán", "gloss_en": "transmit; pass on"},
                {"character": "达", "pinyin": "dá", "gloss_en": "reach; communicate"},
                {"character": "扬", "pinyin": "yáng", "gloss_en": "hoist; make known"},
                {"character": "发", "pinyin": "fā", "gloss_en": "send out; emit"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "播放 designates the physical action of transmitting or playing audio and video recordings via electronic apparatus.",
            "contrasts": [
                {"id": "1", "compared_word": "播放 vs. 广播", "pinyin": "guǎngbō", "analysis": "广播 denotes the broader public mass media industry or institutional transmission station ('中央人民广播电台'), while 播放 is the concrete act of playing specific media clips."},
                {"id": "2", "compared_word": "播放 vs. 放映", "pinyin": "fàngyìng", "analysis": "放映 specifically denotes projecting cinematographic motion pictures onto big screens or theater walls, while 播放 applies to audio, TV, and digital apps."},
                {"id": "3", "compared_word": "播放 vs. 演播", "pinyin": "yǎnbō", "analysis": "演播 emphasizes live studio performance combined with broadcasting ('演播室'), while 播放 plays pre-recorded files."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "夜幕降临，宁静的咖啡馆里点亮了柔和温暖的橘黄色灯光。角落里的留声机缓缓旋转，播放着舒缓悠扬的古典爵士乐曲。伴随着醇厚诱人的咖啡香气，客人们在此洗去一身疲惫，静享安宁时光。",
                "pinyin": "Yèmù jiànglín, níngjìng de kāfēiguǎn lǐ diǎnliàng le róuhé wēnnuǎn de júhuángsè dēngguāng. Jiǎoluò lǐ de liúshēngjī huǎnhuǎn xuánzhuǎn, bōfàng zhe shūhuǎn yōuyáng de gǔdiǎn juéshì yuèqǔ. Bànsuí zhe chúnhòu yòurén de kāfēi xiāngqì, kèrénmen zàicǐ xǐqù yì shēn píbèi, jìngxiǎng ānníng shíguāng.",
                "en": "At dusk, the quiet cafe is lit by warm amber glow. A corner gramophone spins slowly, playing soothing jazz. Mingled with rich coffee aroma, guests wash away fatigue, savoring peaceful hours.",
                "es": "Al anochecer, el café se ilumina con tenue luz ambarina. En el rincón, un gramófono gira suave emitiendo jazz clásico. Entre aromas a café tostado, los clientes disipan el cansancio y gozan de la calma."
            },
            {
                "id": "#2",
                "hanzi": "在现代移动互联网时代，短视频平台凭借先进的智能推荐算法，实现了视频内容的个性化精准播放。无论是传统非遗手艺还是前沿科技科普，都能借助便捷的屏幕播放触达数以亿计的受众，激发出强大的文化传播力量。",
                "pinyin": "Zài xiàndài yídòng hùliánwǎng shídài, duǎnshìpín píngtái píngjiè xiānjìn de zhìnéng tuījiàn suànfǎ, shíxiàn le shìpín nèiróng de gèxìnghuà jīngzhǔn bōfàng. Wúlùn shì chuántǒng fēiyí shǒuyì háishì qiányán kējì kēpǔ, dōunéng jièzhù biànjié de píngmù bōfàng chùdá shùyǐyìjì de shòuzhòng, jīfā chū qiángdà de wénhuà chuánbō lìliàng.",
                "en": "In the mobile internet era, video platforms use algorithms for personalized playback. Whether intangible heritage or science popularization, swift video streaming reaches hundreds of millions, igniting cultural resonance.",
                "es": "En la era de internet móvil, las plataformas de vídeo usan algoritmos para una reproducción personalizada. Desde oficios tradicionales hasta ciencia punta, las pantallas difunden saberes a millones avivando la cultura."
            }
        ]
    },

    # 32 纪念
    {
        "id": "32",
        "hanzi": "纪念",
        "pinyin": "jì niàn",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to commemorate; to remember; souvenir; memorial; commemoration",
            "es": "conmemorar; recordar; recuerdo; memorial; conmemoración"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to honor the memory of a person, event, or past deed through ceremonies, tokens, or monuments",
                "definition_es": "honrar la memoria de una persona o efeméride histórica mediante actos, ofrendas o monumentos",
                "example_phrase": "纪念伟大的先驱 (commemorate great pioneers)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a keepsake, souvenir, memorial token, or commemorative artifact",
                "definition_es": "recuerdo, objeto conmemorativo o prenda testimonial que perpetúa una memoria",
                "example_phrase": "留作纪念 (keep as a souvenir)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每年清明时节，成千上万的少先队员都会来到烈士陵园敬献花圈，深切纪念为国捐躯的英雄。",
                "pinyin": "Měinián Qīngmíng shíjié, chéngqiān-shàngwàn de Shàoxiānduìyuán dōuhuì láidào lièshì língyuán jìngxiàn huāquān, shēnqiè jìniàn wèiguó juānqū de yīngxióng.",
                "en": "Every Qingming festival, thousands of Young Pioneers visit martyrs' cemeteries to lay wreaths and deeply commemorate fallen heroes.",
                "es": "Cada año por Qingming, millares de escolares acuden al cementerio de mártires a ofrendar coronas conmemorando a los héroes caídos por la patria."
            },
            {
                "id": "#2",
                "hanzi": "这块做工考究的机械怀表是爷爷离职退休时单位赠送的，他一直珍藏在书房抽屉里留作纪念。",
                "pinyin": "Zhè kuài zuògōng kǎojiu de jīxiè huáibiǎo shì yéye lízhí tuìxiū shí dānwèi zèngsòng de, tā yìzhí zhēncáng zài shūfáng chōuti lǐ liúzuò jìniàn.",
                "en": "This exquisite mechanical pocket watch was gifted by grandfather's work unit upon retirement; he keeps it in a study drawer as a souvenir.",
                "es": "Este fino reloj de bolsillo mecánico fue un obsequio que recibió el abuelo al jubilarse, conservándolo con cariño en su despacho como recuerdo."
            }
        ],
        "collocations": [
            {"hanzi": "纪念馆", "en": "memorial hall / museum"},
            {"hanzi": "纪念品", "en": "souvenir; keepsake"},
            {"hanzi": "纪念日", "en": "anniversary; memorial day"},
            {"hanzi": "深切纪念", "en": "deeply commemorate"},
            {"hanzi": "留作纪念", "en": "keep as a souvenir/memento"},
            {"hanzi": "纪念碑", "en": "monument; memorial stele"}
        ],
        "idioms": [
            {"hanzi": "永垂不朽", "pinyin": "yǒng chuí bù xiǔ", "meaning_en": "immortal; eternal glory enduring through ages"},
            {"hanzi": "流芳百世", "pinyin": "liú fāng bǎi shì", "meaning_en": "leave a good name for a hundred generations"},
            {"hanzi": "铭记在心", "pinyin": "míng jì zài xīn", "meaning_en": "engraved deeply on one's heart; never forget"},
            {"hanzi": "睹物思人", "pinyin": "dǔ wù sī rén", "meaning_en": "seeing familiar objects evokes memories of absent persons"}
        ],
        "character_decomposition": [
            {
                "character": "纪",
                "pinyin": "jì",
                "meaning_en": "record; chronicle; era; discipline",
                "meaning_es": "registrar; época; crónica; disciplina",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (sorting skeins of silk thread)",
                "sound_component": "己 (jǐ, self / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Unraveling and sorting tangled silk skeins 纟 into an orderly historical record; denotes chronicles or eras.",
                "visual_mnemonic_story_en": "Threads of silk (纟) are sorted into orderly historical records (纪).",
                "visual_mnemonic_story_es": "Hebras de seda (纟) hiladas en pulcro orden para tejer las crónicas de la historia (纪).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMSU",
                "traditional": "紀"
            },
            {
                "character": "念",
                "pinyin": "niàn",
                "meaning_en": "read aloud; think of; miss; thought",
                "meaning_es": "leer en voz alta; pensar en; recordar; idea",
                "radical": "心",
                "radical_meaning_en": "heart / mind",
                "meaning_component": "今 (present moment) + 心 (heart/mind)",
                "sound_component": "念 (niàn)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Holding thoughts of someone in one's heart 心 at the present moment 今; signifies remembering, yearning, or reciting.",
                "visual_mnemonic_story_en": "Present thoughts (今) reside deep in the loving heart (心), remembering (念) dear ones.",
                "visual_mnemonic_story_es": "Pensamientos del presente (今) habitan en el corazón (心) recordando con ternura a los seres queridos (念).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "ONP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Silk chronicles (纪) intertwined with heartfelt thoughts (念) commemorate historical legacies (纪念).",
            "composite_memory_hook_es": "Crónicas escritas (纪) atadas al recuerdo del corazón (念) conmemoran hechos insignes (纪念).",
            "cultural_and_cognitive_roots": "Derived from traditional ancestral remembrance rituals and historiography (纪传体); venerating precursors to link past, present, and future generations.",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'jì niàn' (51-51). Descend firmly on 'jì', then drop down sharply again on 'niàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "记", "pinyin": "jì", "meaning_en": "record; remember", "distinction_note": "Has speech radical 讠 on left instead of silk 纟 in 纪"},
                {"character": "红", "pinyin": "hóng", "meaning_en": "red", "distinction_note": "Has 工 on right of 纟"},
                {"character": "忿", "pinyin": "fèn", "meaning_en": "anger; indignation", "distinction_note": "Has 分 atop 心 instead of 今 in 念"},
                {"character": "急", "pinyin": "jí", "meaning_en": "urgent; anxious", "distinction_note": "Has 刍-like upper component atop 心"}
            ],
            "etymological_cognates": [
                {"character": "忆", "pinyin": "yì", "gloss_en": "recollect; recall memory"},
                {"character": "怀", "pinyin": "huái", "gloss_en": "bosom; cherish memory"},
                {"character": "思", "pinyin": "sī", "gloss_en": "ponder; yearn for"},
                {"character": "悼", "pinyin": "dào", "gloss_en": "grieve; mourn the dead"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "纪念 emphasizes public, ritual, or tangible remembrance of monumental deeds, heroes, or significant dates.",
            "contrasts": [
                {"id": "1", "compared_word": "纪念 vs. 怀念", "pinyin": "huáiniàn", "analysis": "怀念 is a soft, personal emotional feeling of longing for absent friends or bygone days, while 纪念 involves public ceremonies, medals, or monuments."},
                {"id": "2", "compared_word": "纪念 vs. 悼念", "pinyin": "dàoniàn", "analysis": "悼念 is strictly focused on grief and sorrow immediately following someone's death, while 纪念 celebrates lasting legacies over long eras."},
                {"id": "3", "compared_word": "纪念 vs. 留念", "pinyin": "liúniàn", "analysis": "留念 is specifically used when giving small gifts or posing for photos upon departure ('拍照留念'), while 纪念 has broader historic stature."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "庄严巍峨的人民英雄纪念碑耸立在天安门广场中央。碑身正面镌刻着金光闪闪的题词，四周汉白玉浮雕生动再现了百余年来中华儿女浴血奋斗的历史长卷。它不仅是对革命先烈的深切纪念，更是激励后人奋进的灯塔。",
                "pinyin": "Zhuāngyán-wēi'é de Rénmín Yīngxióng Jìniànbēi sǒnglì zài Tiān'ānmén Guǎngchǎng zhōngyāng. Bēishēn zhèngmiàn juānkè zhe jīnguāng-shǎnshǎn de tící, sìzhōu hànbáiyù fúdiāo shēngdòng zàixiàn le bǎiyú nián lái Zhōnghuá érnǚ yùxuè-fèndòu de lìshǐ chángjuǎn. Tā bùjǐn shì duì gémìng xiānliè de shēnqiè jìniàn, gèng shì jīlì hòurén fènjìn de dēngtǎ.",
                "en": "The Monument to the People's Heroes rises in Tiananmen Square. Gilded inscriptions and marble bas-reliefs depict historic struggles. It stands as a solemn commemoration of martyrs and a guiding beacon inspiring generations.",
                "es": "El Monumento a los Héroes del Pueblo se yergue en la plaza de Tiananmen. Inscripciones doradas y relieves de mármol retratan gestas históricas, conmemorando a los mártires e iluminando el porvenir.",
                "es": "El Monumento a los Héroes del Pueblo se yergue en la plaza de Tiananmen. Relieves de mármol retratan gestas históricas conmemorando a los mártires e iluminando el porvenir nacional."
            },
            {
                "id": "#2",
                "hanzi": "今年适逢该校建校一百周年，来自世界各地的数千名校友重返母校，共同出席隆重庄严的世纪纪念盛典。大家漫步在绿树成荫的林荫道上，重温当年的求学时光，并在标志性钟楼前合影留作难忘的青春纪念。",
                "pinyin": "Jīnnián shìféng gāixiào jiànxiào yìbǎi zhōunián, láizì shìjiè gèdì de shùqiān míng xiàoyǒu chóngfǎn mǔxiào, gòngtóng chūxí lóngzhòng zhuāngyán de shìjì jìniàn shèngdiǎn. Dàjiā mànbù zài lǜshù-chéngyīn de línyīndào shàng, chóngwēn dāngnián de qiúxué shíguāng, bìng zài biāozhìxìng zhōnglóu qián héyǐng liúzuò nánwàng de qīngchūn jìniàn.",
                "en": "Marking the school's centenary, thousands of alumni returned worldwide for commemorative celebrations. Strolling shady avenues, they reminisced about student days, snapping keepsake photos before the landmark clock tower.",
                "es": "Con ocasión del centenario escolar, miles de antiguos alumnos regresaron para los actos conmemorativos. Paseando bajo las arboledas evocaron sus años mozos, tomándose fotos inolvidables ante el reloj del campus."
            }
        ]
    },

    # 33 导演
    {
        "id": "33",
        "hanzi": "导演",
        "pinyin": "dǎo yǎn",
        "part_of_speech": "Noun / Verb",
        "meanings_summary": {
            "en": "director (of film/play); to direct (film/play)",
            "es": "director (de cine o teatro); dirigir (una película u obra)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person who directs the artistic performance and visual staging of a film, play, or television show",
                "definition_es": "persona que dirige la puesta en escena, actuación e interpretación artística de una película u obra teatral",
                "example_phrase": "著名电影导演 (famous movie director)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to guide, stage, or oversee the dramatic performance of a production",
                "definition_es": "guiar, orquestar o supervisar la realización artística de un montaje escénico o audiovisual",
                "example_phrase": "导演一部经典话剧 (direct a classic stage play)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这位才华横溢的年轻导演凭借对细节的敏锐把控，将一部低成本文艺片打磨成了震撼人心的艺术杰作。",
                "pinyin": "Zhè wèi cáihuá-héngyì de niánqīng dǎoyǎn píngjiè duì xìjié de mǐnruì bǎkòng, jiāng yí bù dīchéngběn wényìpiān dǎmó chéng le zhènhàn-rénxīn de yìshù jiézuò.",
                "en": "With sharp control over details, this talented young director polished a low-budget indie film into a moving artistic masterpiece.",
                "es": "Con un afinado dominio de los detalles, este talentoso director novel convirtió una modesta película de autor en una conmovedora obra maestra."
            },
            {
                "id": "#2",
                "hanzi": "在排练现场，导演耐心地为男女主演分析人物内心独白与情感转折，引导他们渐入佳境。",
                "pinyin": "Zài páiliàn xiànchǎng, dǎoyǎn nàixīn de wèi nán-nǚ zhǔyǎn fēnxī rénwù nèixīn dúbái yǔ qínggǎn zhuǎnzhé, yǐndǎo tāmen jiànrùjiājìng.",
                "en": "In rehearsals, the director patiently analyzed characters' inner monologues and emotional shifts, guiding leads into peak performance.",
                "es": "En los ensayos, el director analizaba con paciencia el monólogo interior de los protagonistas, guiándolos a una interpretación insuperable."
            }
        ],
        "collocations": [
            {"hanzi": "执行导演", "en": "executive director"},
            {"hanzi": "总导演", "en": "chief director / artistic director"},
            {"hanzi": "副导演", "en": "assistant director"},
            {"hanzi": "新锐导演", "en": "cutting-edge up-and-coming director"},
            {"hanzi": "导演风格", "en": "directorial style"},
            {"hanzi": "自编自导", "en": "write and direct oneself"}
        ],
        "idioms": [
            {"hanzi": "运筹帷幄", "pinyin": "yùn chóu wéi wò", "meaning_en": "devise strategies within a command tent; mastermind operations"},
            {"hanzi": "别出心裁", "pinyin": "bié chū xīn cái", "meaning_en": "adopt an original approach; show novelty"},
            {"hanzi": "绘声绘色", "pinyin": "huì shēng huì sè", "meaning_en": "vivid and expressive in sound and imagery"},
            {"hanzi": "独树一帜", "pinyin": "dú shù yì zhì", "meaning_en": "raise a unique banner; develop a distinctive style"}
        ],
        "character_decomposition": [
            {
                "character": "导",
                "pinyin": "dǎo",
                "meaning_en": "guide; lead; instruct; conduct",
                "meaning_es": "guiar; conducir; orientar; dirigir",
                "radical": "寸",
                "radical_meaning_en": "inch / hand measure",
                "meaning_component": "巳 (offspring / path) + 寸 (hand measuring / pointing way)",
                "sound_component": "道 (dào, the way / phonetic origin)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A hand 寸 pointing out the path 道; guiding people along the correct route.",
                "visual_mnemonic_story_en": "A hand (寸) points ahead, guiding (导) followers safely along the right course.",
                "visual_mnemonic_story_es": "Una mano orientadora (寸) señala la ruta correcta conduciendo (导) los pasos del grupo.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RDI",
                "traditional": "導"
            },
            {
                "character": "演",
                "pinyin": "yǎn",
                "meaning_en": "perform; act; play; deduce; develop",
                "meaning_es": "actuar; interpretar; representar; deducir",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water flowing smoothly)",
                "sound_component": "寅 (yín, bow / dawn / phonetic)",
                "stroke_count": 14,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 combined with 寅; streams flowing continuously, extended to continuous staged performances and deductions.",
                "visual_mnemonic_story_en": "Water (氵) flows rhythmically like drama unfolding smoothly across the stage (演).",
                "visual_mnemonic_story_es": "Las aguas (氵) fluyen cadenciosas como la trama que se desenvuelve en escena (演).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "EJMC",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Guiding the path (导) for actors performing on stage (演) is the duty of a director (导演).",
            "composite_memory_hook_es": "Guiar el rumbo escénico (导) para quienes actúan e interpretan (演) es labor del director (导演).",
            "cultural_and_cognitive_roots": "Compound created in early 20th-century Chinese spoken drama (话剧) movements; merges classical guidance (引导) with theatrical acting (表演).",
            "tone_sandhi_and_pitch_modulation": "Two third tones in succession triggering tone sandhi: 'dǎo yǎn' becomes [dáo yǎn] (35-214). Pronounce 'dǎo' with rising second tone pitch 35, then dip fully on 'yǎn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "寻", "pinyin": "xún", "meaning_en": "seek; search", "distinction_note": "Has 彐 on top of 寸 instead of 巳 in 导"},
                {"character": "异", "pinyin": "yì", "meaning_en": "different; strange", "distinction_note": "Has 廾 underneath 巳"},
                {"character": "滨", "pinyin": "bīn", "meaning_en": "shore; coast", "distinction_note": "Has 宾 on right of 氵 instead of 寅 in 演"},
                {"character": "漠", "pinyin": "mò", "meaning_en": "desert; indifferent", "distinction_note": "Has 莫 on right of 氵"}
            ],
            "etymological_cognates": [
                {"character": "编", "pinyin": "biān", "gloss_en": "weave bamboo; edit script"},
                {"character": "摄", "pinyin": "shè", "gloss_en": "capture image; shoot camera"},
                {"character": "戏", "pinyin": "xì", "gloss_en": "theatrical drama; play"},
                {"character": "领", "pinyin": "lǐng", "gloss_en": "lead forward; collar"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "导演 designates the artistic commander who shapes and coordinates acting, lighting, camera work, and narrative pacing.",
            "contrasts": [
                {"id": "1", "compared_word": "导演 vs. 编剧", "pinyin": "biānjù", "analysis": "编剧 writes the dialogue, plot, and script, while 导演 realizes the written text into visual cinematic or theatrical reality."},
                {"id": "2", "compared_word": "导演 vs. 制片人", "pinyin": "zhìpiànrén", "analysis": "制片人 (producer) manages financing, logistics, commercial scheduling, and marketing, while 导演 commands creative artistic decisions."},
                {"id": "3", "compared_word": "导演 vs. 摄影师", "pinyin": "shèyǐngshī", "analysis": "摄影师 executes lighting and lens framing under the conceptual artistic guidance of 导演."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在一部优秀的电影作品背后，导演就像是一艘巨轮的掌舵者。从最初推敲剧本角色、挑选演员阵容，到拍摄现场把控演员情绪与摄影机调度，导演的审美眼光与艺术构思决定了整部作品的精神内核与艺术高度。",
                "pinyin": "Zài yí bù yōuxiù de diànyǐng zuòpǐn bèihòu, dǎoyǎn jiù xiàng shì yì sōu jùlún de zhǎngduòzhě. Cóng zuìchū tuīqiāo jùběn juésè, tiāoxuǎn yǎnyuán zhènróng, dào pāishè xiànchǎng bǎkòng yǎnyuán qíngxù yǔ shèyǐngjī diàodù, dǎoyǎn de shěnměi yǎnguāng yǔ yìshù gòusī juédìng le zhěng bù zuòpǐn de jīngshén nèihé yǔ yìshù gāodù.",
                "en": "Behind every great film, the director is the helmsman of a colossal ship. From polishing scripts and casting leads to modulating performance on set, their aesthetic vision determines the film's artistic soul.",
                "es": "Tras toda película magistral, el director pilota una nave inmensa. Desde pulir el guion y elegir el reparto hasta modular la emoción ante la cámara, su criterio estético define el alma y la altura de la obra."
            },
            {
                "id": "#2",
                "hanzi": "中国第五代著名电影导演张艺谋，善于运用饱满浓烈的色彩美学与宏大的场面调度传达深厚的东方历史文化底蕴。无论是早期的经典文艺片，还是近年来震撼全球的奥运会开幕式，都充分展现了他卓越非凡的导演才华。",
                "pinyin": "Zhōngguó dìwǔdài zhùmíng diànyǐng dǎoyǎn Zhāng Yìmóu, shànyú yùnyòng bǎomǎn nóngliè de sècǎi měixué yǔ hóngdà de chǎngmiàn diàodù chuándá shēnhòu de dōngfāng lìshǐ wénhuà dǐyùn. Wúlùn shì zǎoqī de jīngdiǎn wényìpiān, háishì jìnniánlái zhènhàn quánqiú de Àoyùnhuì kāimùshì, dōu chōngfèn zhǎnxiàn le tā zhuóyuè-fēifán de dǎoyǎn cáihuá.",
                "en": "Renowned director Zhang Yimou uses intense color palettes and grand staging to convey deep Eastern culture. From early art films to stunning Olympic opening ceremonies, he exhibits extraordinary directorial talent.",
                "es": "El célebre cineasta Zhang Yimou emplea vivos contrastes cromáticos y composiciones grandiosas para plasmar la cultura oriental. Desde sus filmes de autor hasta ceremonias olímpicas, demuestra una maestría insigne."
            }
        ]
    },

    # 34 瞬间
    {
        "id": "34",
        "hanzi": "瞬间",
        "pinyin": "shùn jiān",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "moment; instant; split second; flash",
            "es": "instante; momento; abrir y cerrar de ojos; segundo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an extremely brief span of time; an instant; a blink of an eye",
                "definition_es": "espacio brevísimo de tiempo; un instante o pestañeo",
                "example_phrase": "一瞬间 (in a split second / in an instant)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "夜空中划过一道耀眼的金色流星，虽然仅仅闪耀了一瞬间，却在仰望星空的人们心中留下了永恒的美丽。",
                "pinyin": "Yèkōng zhōng huàguò yí dào yàoyǎn de jīnsè liúxīng, suīrán jǐnjǐn shǎnyào le yí shùnjiān, què zài yǎngwàng xīngkōng de rénmen xīnxzhōng liúxià le yǒnghéng de měilì.",
                "en": "A dazzling golden shooting star streaked across the night sky; though gleaming for merely an instant, it left eternal beauty in stargazers' hearts.",
                "es": "Un fulgurante meteoro dorado cruzó la noche; aunque solo brilló un instante, dejó una estela de belleza eterna en el corazón de quienes miraban."
            },
            {
                "id": "#2",
                "hanzi": "在裁判吹响终场哨声的瞬间，全场沸腾欢呼，队员们激动得紧紧拥抱在一起失声痛哭。",
                "pinyin": "Zài cáipàn chuīxiǎng zhōngchǎng shàoshēng de shùnjiān, quánchǎng fèiténg huānhū, duìyuánmen jīdòng de jǐnjǐn yōngbào zài yìqǐ shīshēng tòngkū.",
                "en": "The instant the referee blew the final whistle, the stadium erupted in cheers, players embracing each other and weeping tears of joy.",
                "es": "En el instante en que el árbitro pitó el final, la grada estalló en júbilo y los jugadores se fundieron en un abrazo llorando de emoción."
            }
        ],
        "collocations": [
            {"hanzi": "一瞬间", "en": "in a split second; in an instant"},
            {"hanzi": "瞬间爆发", "en": "instantaneous outburst"},
            {"hanzi": "精彩瞬间", "en": "wonderful highlight moments"},
            {"hanzi": "抓住瞬间", "en": "seize the fleeting moment"},
            {"hanzi": "瞬间消失", "en": "vanish in an instant"},
            {"hanzi": "永恒的瞬间", "en": "eternal instant"}
        ],
        "idioms": [
            {"hanzi": "转瞬即逝", "pinyin": "zhuǎn shùn jí shì", "meaning_en": "vanish in the blink of an eye; fleeting and transient"},
            {"hanzi": "白驹过隙", "pinyin": "bái jū guò xì", "meaning_en": "time passing like a white colt leaping across a gap; fleeting time"},
            {"hanzi": "电光石火", "pinyin": "diàn guāng shí huǒ", "meaning_en": "lightning flash and spark from flint; split second"},
            {"hanzi": "弹指之间", "pinyin": "tán zhǐ zhī jiān", "meaning_en": "in the flick of a finger; in a trice"}
        ],
        "character_decomposition": [
            {
                "character": "瞬",
                "pinyin": "shùn",
                "meaning_en": "wink; blink eye; flash; instant",
                "meaning_es": "parpadear; guiñar; pestañeo; instante",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye blinking) + 舜 (flowering hibiscus / ephemeral)",
                "sound_component": "舜 (shùn, wise emperor / phonetic)",
                "stroke_count": 17,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Eye radical 目 combined with 舜; the brief duration of an eye winking or blinking shut.",
                "visual_mnemonic_story_en": "An eyelid (目) winks shut like a flower blooming and closing in an instant (瞬).",
                "visual_mnemonic_story_es": "Un ojo (目) parpadea fugaz como corola que abre y cierra en un pestañeo (瞬).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HUBFQ",
                "traditional": ""
            },
            {
                "character": "间",
                "pinyin": "jiān",
                "meaning_en": "between; among; interval; room",
                "meaning_es": "entre; intervalo; espacio; habitación",
                "radical": "门",
                "radical_meaning_en": "gate / door",
                "meaning_component": "门 (double door) + 日 (sunlight peeking through crevice)",
                "sound_component": "间 (jiān)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Sunlight 日 shining through the chink of closed double doors 门; represents a spatial opening or temporal interval.",
                "visual_mnemonic_story_en": "Sunlight gleams through a crack in closed doors (门), defining a brief interval (间).",
                "visual_mnemonic_story_es": "Un rayo de sol asoma por la rendija del portón (门) marcando un lapso efímero (间).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "LSA",
                "traditional": "間"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The tiny time interval (间) of an eye blinking (瞬) defines a split second (瞬间).",
            "composite_memory_hook_es": "El mínimo intervalo (间) que tarda un ojo en parpadear (瞬) define un instante (瞬间).",
            "cultural_and_cognitive_roots": "Derived from Buddhist temporal units (ksana / 刹那): the human eye blinking constitutes the foundational metaphor for transience.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by level high tone: 'shùn jiān' (51-55). Strike down on 'shùn' then float high and clear on 'jiān'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "睛", "pinyin": "jīng", "meaning_en": "eyeball; pupil", "distinction_note": "Has 青 on right of 目 instead of 舜 in 瞬"},
                {"character": "睡", "pinyin": "shuì", "meaning_en": "sleep", "distinction_note": "Has 垂 on right of 目"},
                {"character": "问", "pinyin": "wèn", "meaning_en": "ask", "distinction_note": "Has mouth 口 inside 门 instead of 日 in 间"},
                {"character": "闭", "pinyin": "bì", "meaning_en": "close; shut", "distinction_note": "Has 才 inside 门"}
            ],
            "etymological_cognates": [
                {"character": "秒", "pinyin": "miǎo", "gloss_en": "second; awn of grain"},
                {"character": "刹", "pinyin": "chà", "gloss_en": "instant; ksana"},
                {"character": "顷", "pinyin": "qǐng", "gloss_en": "short while; inclined head"},
                {"character": "刻", "pinyin": "kè", "gloss_en": "quarter hour; carve notch"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "瞬间 emphasizes the extreme brevity of a fleeting flash of time, often capturing decisive kinetic actions.",
            "contrasts": [
                {"id": "1", "compared_word": "瞬间 vs. 刹那", "pinyin": "chànà", "analysis": "刹那 is a formal philosophical or poetic Buddhist term for a micro-instant, while 瞬间 is modern standard written and spoken Chinese."},
                {"id": "2", "compared_word": "瞬间 vs. 片刻", "pinyin": "piànkè", "analysis": "片刻 designates a short while or brief pause spanning several minutes ('休息片刻'), while 瞬间 is a fraction of a second."},
                {"id": "3", "compared_word": "瞬间 vs. 顿时", "pinyin": "dùnshí", "analysis": "顿时 is an adverb meaning 'immediately / at once' emphasizing cause-and-effect reaction, while 瞬间 is a noun designating the time instant itself."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "摄影的最高境界，在于用心灵捕捉那些稍纵即逝的感人瞬间。奔跑骏马四蹄凌空的一瞬，婴儿绽放天真笑容的刹那，亦或老夫妻街头相视而笑的温馨画面，都在快门按下的瞬间化作了永不褪色的永恒记忆。",
                "pinyin": "Shèyǐng de zuìgāo jìngjiè, zàiyú yòng xīnlíng bǔzhuō nàxiē shāozòng-jíshì de gǎnrén shùnjiān. Bēnpǎo jùnmǎ sì tí língkōng de yí shùn, yīng'ér zhànfàng tiānzhēn xiàoróng de chànà, yìhuò lǎofūqī jiētóu xiāngshì-érxiào de wēnxīn huàmiàn, dōu zài kuàimén ànxià de shùnjiān huàzuò le yǒngbútùisè de yǒnghéng jìyì.",
                "en": "Photography's peak lies in capturing fleeting moments. A steed's hooves airborne, an infant's pure smile, or an old couple's warm glance all become timeless memories the instant the shutter clicks.",
                "es": "La cumbre de la fotografía radica en capturar instantes fugitivos. Cascos suspendidos en el galope, la risa de un bebé o miradas cómplices de ancianos se tornan memoria eterna al disparar el obturador."
            },
            {
                "id": "#2",
                "hanzi": "面对突如其来的地震险情，生死往往只在短短的一两秒瞬间决定。危急关头，年轻的班主任毫不犹豫地张开双臂护住讲台下的幼小学生，将生的希望留给孩子们，用生命谱写出感天动地的人性赞歌。",
                "pinyin": "Miànduì tūrúqílái de dìzhèn xiǎnqíng, shēngsǐ wǎngwǎng zhǐ zài duǎnduǎn de yì-liǎng miǎo shùnjiān juédìng. Wēijí guāntóu, niánqīng de bānzhǔrèn háobùyóuyù de zhāngkāi shuāngbì hùzhù jiǎngtái xià de yòuxiǎo xuésheng, jiāng shēng de xīwàng liúgěi háizimen, yòng shēngmìng pǔxiě chū gǎntiān-dòngdì de rénxìng zàngē.",
                "en": "In earthquakes, survival is decided in a split second. At the critical moment, the young teacher shielded pupils beneath the desk with outstretched arms, offering hope of life in an unforgettable act.",
                "es": "Ante la sacudida de un terremoto, la vida y la muerte se zanjan en un instante. En el trance crítico, la maestra cubrió a sus pupilos con sus brazos, ofrendando su vida en un conmovedor himno de entrega."
            }
        ]
    },

    # 35 请求
    {
        "id": "35",
        "hanzi": "请求",
        "pinyin": "qǐng qiú",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to request; to ask; to appeal; request; petition",
            "es": "solicitar; pedir; rogar; petición; solicitud"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to ask politely or formally for assistance, permission, or a favor",
                "definition_es": "pedir con cortesía o formalidad ayuda, autorización o concesión de algo",
                "example_phrase": "请求上级批准 (request superior approval)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an act of asking politely; a formal petition or appeal",
                "definition_es": "petición, solicitud formal o ruego respetuoso",
                "example_phrase": "提出合理请求 (put forward a reasonable request)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "因家中突发紧急变故，他怀着歉意向部门主管诚恳地请求准予三天带薪事假。",
                "pinyin": "Yīn jiāzhōng tūfā jǐnjí biàngù, tā huáizhe qiànyì xiàng bùmén zhǔguǎn chéngkěn de qǐngqiú zhǔnyǔ sān tiān dàixīn shìjià.",
                "en": "Due to a family emergency, he apologetically and earnestly requested three days of paid personal leave from his manager.",
                "es": "Por una emergencia familiar imprevista, solicitó respetuoso y sincero a su superior tres días de permiso retribuido."
            },
            {
                "id": "#2",
                "hanzi": "面对受灾群众迫切的救援请求，应急救援抢险分队顶风冒雨连夜赶往滑坡现场。",
                "pinyin": "Miànduì shòuzāi qúnzhòng pòqiè de jiùyuán qǐngqiú, yīngjí jiùyuán qiǎngxiǎn fēnduì dǐngfēng-màoyǔ liányè gǎnwǎng huápō xiànchǎng.",
                "en": "Confronted with victims' urgent requests for rescue, emergency teams braved rainstorms overnight to rush to the landslide site.",
                "es": "Ante los apremiantes ruegos de auxilio de los damnificados, brigadas de rescate acudieron de noche bajo el temporal al lugar del desprendimiento."
            }
        ],
        "collocations": [
            {"hanzi": "提出请求", "en": "put forward a request"},
            {"hanzi": "答应请求", "en": "agree to a request"},
            {"hanzi": "拒绝请求", "en": "refuse a request"},
            {"hanzi": "请求支援", "en": "request reinforcements/support"},
            {"hanzi": "请求原谅", "en": "beg forgiveness / request pardon"},
            {"hanzi": "合理请求", "en": "reasonable request"}
        ],
        "idioms": [
            {"hanzi": "不情之请", "pinyin": "bù qíng zhī qǐng", "meaning_en": "my presumptuous request; an uncalled-for favor (polite formula)"},
            {"hanzi": "求之不得", "pinyin": "qiú zhī bù dé", "meaning_en": "seek but cannot get; all that one could wish for"},
            {"hanzi": "有求必应", "pinyin": "yǒu qiú bì yìng", "meaning_en": "grant every request; never say no to appeals"},
            {"hanzi": "恳切哀求", "pinyin": "kěn qiè āi qiú", "meaning_en": "beseech earnestly and piteously"}
        ],
        "character_decomposition": [
            {
                "character": "请",
                "pinyin": "qǐng",
                "meaning_en": "please; ask; invite; request",
                "meaning_es": "por favor; invitar; rogar; pedir",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (courteous spoken words)",
                "sound_component": "青 (qīng, pure green / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 delivered with sincere purity 青; denotes polite requests and hospitable invitations.",
                "visual_mnemonic_story_en": "Polite words (讠) spoken with sincerity (青) frame a courteous request (请).",
                "visual_mnemonic_story_es": "Palabras gentiles (讠) expresadas con pureza sincera (青) articulan un ruego cortés (请).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "IVQMB",
                "traditional": "請"
            },
            {
                "character": "求",
                "pinyin": "qiú",
                "meaning_en": "seek; beg; plead; demand",
                "meaning_es": "buscar; pedir; implorar; exigir",
                "radical": "水",
                "radical_meaning_en": "water",
                "meaning_component": "裘 (fur coat with tails) -> simplified to hand grasping",
                "sound_component": "求 (qiú)",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Originally a fur coat 裘 worn for warmth; borrowed phonetically to mean seeking, pleading, or praying for blessings.",
                "visual_mnemonic_story_en": "Hands reach out clasping together in earnest prayer to plead for help (求).",
                "visual_mnemonic_story_es": "Manos juntas que se extienden en ferviente súplica para rogar auxilio (求).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IJE",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Polite words (请) accompanied by earnest pleading (求) formulate a respectful request (请求).",
            "composite_memory_hook_es": "Palabras corteses (请) unidas a una súplica sentida (求) formalizan la petición (请求).",
            "cultural_and_cognitive_roots": "Politeness register in Chinese social hierarchy (礼貌用语); pairing deferential speech (请) with respectful appeal (求) maintains social harmony.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by rising second tone: 'qǐng qiú' (214-35). Dip low on 'qǐng' then rise smoothly on 'qiú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "清", "pinyin": "qīng", "meaning_en": "clear; pure", "distinction_note": "Has water radical 氵 on left of 青 instead of speech 讠 in 请"},
                {"character": "晴", "pinyin": "qíng", "meaning_en": "sunny; clear sky", "distinction_note": "Has sun radical 日 on left of 青"},
                {"character": "球", "pinyin": "qiú", "meaning_en": "ball; sphere", "distinction_note": "Has jade radical 王 on left of 求"},
                {"character": "救", "pinyin": "jiù", "meaning_en": "rescue; save", "distinction_note": "Has tap radical 攵 on right of 求"}
            ],
            "etymological_cognates": [
                {"character": "恳", "pinyin": "kěn", "gloss_en": "earnest; sincere heart"},
                {"character": "托", "pinyin": "tuō", "gloss_en": "entrust in hand; request"},
                {"character": "索", "pinyin": "suǒ", "gloss_en": "search rope; demand"},
                {"character": "要", "pinyin": "yào", "gloss_en": "want; demand with hands"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "请求 is a polite, formal appeal directed towards superiors, peers, or authorities for consent or aid.",
            "contrasts": [
                {"id": "1", "compared_word": "请求 vs. 要求", "pinyin": "yāoqiú", "analysis": "要求 expresses an authoritative demand or mandatory requirement from superiors or contracts, while 请求 is deferential and polite."},
                {"id": "2", "compared_word": "请求 vs. 祈求", "pinyin": "qíqiú", "analysis": "祈求 is religious prayer or desperate pleading to deities or fate ('祈求平安'), while 请求 operates in human social affairs."},
                {"id": "3", "compared_word": "请求 vs. 申请", "pinyin": "shēnqǐng", "analysis": "申请 is an official bureaucratic application requiring written paperwork and formal qualification vetting ('申请签证'), while 请求 can be oral."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "科研攻关过程中，年轻的博士生遇到了前所未见的实验数据异常。他虚心整理好全部观测记录与推导草稿，恭敬地向前辈院士提出请教请求。老科学家深受其求真精神感动，毫无保留地指点迷津。",
                "pinyin": "Kēyán gōngguān guòchéng zhōng, niánqīng de bóshìshēng yùdào le qiánsuǒwèijiàn de shíyàn shùjù yìcháng. Tā xūxīn zhěnglǐ hǎo quánbù guāncè jìlù yǔ tuīdǎo cǎogǎo, gōngjìng de xiàng qiánbèi yuànshì tíchū qǐngjiào qǐngqiú. Lǎo kēxuéjiā shēn shòu qí qiúzhēn jīngshén gǎndòng, háowú-bǎoliú de zhǐdiǎn míjīn.",
                "en": "Encountering unprecedented data anomalies, a young doctoral student organized notes and respectfully requested guidance from a senior academician. Moved by his sincerity, the veteran scientist offered guidance.",
                "es": "Ante anomalías insólitas en sus datos, un joven doctorando ordenó sus notas solicitando con respeto el consejo de un académico emérito. Conmovido por su afán, el veterano científico lo orientó con generosidad."
            },
            {
                "id": "#2",
                "hanzi": "在现代政务服务大厅里，“一网通办”便民改革切实落实了让数据多跑路、群众少跑腿的惠民承诺。市民只需在手机终端提交相关证明与业务审批请求，便能在短短几个工作日内足不出户办结各项民生手续。",
                "pinyin": "Zài xiàndài zhèngwù fúwù dàtīng lǐ, 'yìwǎngtōngbàn' biànmín gǎigé qièshí luòshí le ràng shùjù duō pǎolù, qúnzhòng shǎo pǎotuǐ de huìmín chéngnuò. Shìmín zhǐxū zài shǒujī duān tíjiāo xiāngguān zhèngmíng yǔ yèwù shěnpī qǐngqiú, biàn néng zài duǎnduǎn jǐ ge gōngzuòrì nèi zúbùchūhù bànjié gèxiàng mínshēng shǒuxù.",
                "en": "In government service halls, digital administration fulfills the promise of letting data travel instead of citizens. Submitting approvals and requests via smartphones, residents complete civil formalities seamlessly.",
                "es": "En la administración digitalizada, el ciudadano ahorra desplazamientos gracias a la tramitación telemática. Remitiendo solicitudes desde el teléfono móvil, se despachan trámites en pocos días sin salir de casa."
            }
        ]
    },

    # 36 或许
    {
        "id": "36",
        "hanzi": "或许",
        "pinyin": "huò xǔ",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "perhaps; maybe; probably",
            "es": "quizás; tal vez; acaso; a lo mejor"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "expressing uncertainty, possibility, speculation, or polite conjecture",
                "definition_es": "expresa conjetura, incertidumbre o posibilidad prudente sobre un hecho",
                "example_phrase": "或许他已经知道了 (perhaps he already knows)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "会议室的灯还亮着，或许项目攻关小组今晚又要通宵加班赶制测试版本了。",
                "pinyin": "Huìyìshì de dēng hái liàng zhe, huòxǔ xiàngmù gōngguān xiǎozǔ jīnwǎn yòuyào tōngxiāo jiābān gǎnzhì cèshì bǎnběn le.",
                "en": "The lights in the conference room are still on; perhaps the project team is working overnight again to rush out test versions.",
                "es": "Las luces de la sala de juntas siguen encendidas; tal vez el equipo del proyecto vuelva a trasnochar para apurar la versión beta."
            },
            {
                "id": "#2",
                "hanzi": "面对眼前看似无法逾越的困难，换一种全新的逆向思维，或许能迎来柳暗花明。",
                "pinyin": "Miànduì yǎnqián kànsì wúfǎ yúyuè de kùnnán, huàn yì zhǒng quánxīn de nìxiàng sīwéi, huòxǔ néng yínglái liǔ'àn-huāmíng.",
                "en": "Facing seemingly insurmountable difficulties, shifting to reverse thinking might perhaps lead to an unexpected breakthrough.",
                "es": "Ante dificultades en apariencia insuperables, adoptar un enfoque inverso tal vez depare una solución tan luminosa como inesperada."
            }
        ],
        "collocations": [
            {"hanzi": "或许会", "en": "perhaps will / might"},
            {"hanzi": "或许可以", "en": "perhaps could / maybe can"},
            {"hanzi": "或许正是", "en": "perhaps precisely is"},
            {"hanzi": "或许因为", "en": "perhaps because"},
            {"hanzi": "或许不是", "en": "perhaps not"},
            {"hanzi": "或许有人", "en": "perhaps someone"}
        ],
        "idioms": [
            {"hanzi": "柳暗花明", "pinyin": "liǔ àn huā míng", "meaning_en": "dark willows and bright flowers; light at the end of the tunnel"},
            {"hanzi": "未可厚非", "pinyin": "wèi kě hòu fēi", "meaning_en": "not entirely blameworthy; understandable"},
            {"hanzi": "若隐若现", "pinyin": "ruò yǐn ruò xiàn", "meaning_en": "partly visible and partly hidden; faint and elusive"},
            {"hanzi": "莫衷一是", "pinyin": "mò zhōng yī shì", "meaning_en": "unable to agree on which is right; opinions vary"}
        ],
        "character_decomposition": [
            {
                "character": "或",
                "pinyin": "huò",
                "meaning_en": "or; either; perhaps; someone",
                "meaning_es": "o; tal vez; quizás; alguien",
                "radical": "戈",
                "radical_meaning_en": "dagger-axe",
                "meaning_component": "戈 (weapon guarding border) + 囗/一 (walled city territory)",
                "sound_component": "或 (huò)",
                "stroke_count": 8,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Original form of 國 (state/city defended by spear 戈); later borrowed to mean hypothetical choices, someone, or perhaps.",
                "visual_mnemonic_story_en": "A spear (戈) defends a city border where choices between peace or battle hang in balance (或).",
                "visual_mnemonic_story_es": "Una lanza (戈) guarda el baluarte fronterizo donde la paz o la lid penden de un hilo (或).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IRM",
                "traditional": ""
            },
            {
                "character": "许",
                "pinyin": "xǔ",
                "meaning_en": "allow; permit; promise; praise; perhaps",
                "meaning_es": "permitir; prometer; tal vez; alabar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken commitment) + 午 (pestle / noon)",
                "sound_component": "午 (wǔ, noon / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 agreeing to allow an action; extended to approximate estimation (许多) and conditional possibility.",
                "visual_mnemonic_story_en": "Spoken words (讠) assent with a nod at high noon (午), permitting possibility (许).",
                "visual_mnemonic_story_es": "Palabras meditadas (讠) otorgan su venia al mediodía (午) admitiendo la posibilidad (许).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "IVO",
                "traditional": "許"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Balancing options on the border (或) and permitting conditional possibilities (许) suggests 'perhaps' (或许).",
            "composite_memory_hook_es": "Sopesar opciones (或) y admitir la posibilidad (许) da sentido a 'quizás' o 'tal vez' (或许).",
            "cultural_and_cognitive_roots": "Polite hedging in Chinese dialectics and literature; softening declarative assertions with 或许 demonstrates intellectual modesty and nuanced deliberation.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by dipping third tone: 'huò xǔ' (51-214). Drop decisively on 'huò' then dip down and rise gently on 'xǔ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "惑", "pinyin": "huò", "meaning_en": "delude; confused", "distinction_note": "Has heart radical 心 underneath 或"},
                {"character": "域", "pinyin": "yù", "meaning_en": "territory; realm", "distinction_note": "Has earth radical 土 on left of 或"},
                {"character": "计", "pinyin": "jì", "meaning_en": "calculate; plan", "distinction_note": "Has 十 on right of 讠 instead of 午 in 许"},
                {"character": "诈", "pinyin": "zhà", "meaning_en": "cheat; pretend", "distinction_note": "Has 乍 on right of 讠"}
            ],
            "etymological_cognates": [
                {"character": "可", "pinyin": "kě", "gloss_en": "can; permissible"},
                {"character": "能", "pinyin": "néng", "gloss_en": "able; potential power"},
                {"character": "若", "pinyin": "ruò", "gloss_en": "as if; supposing"},
                {"character": "殆", "pinyin": "dài", "gloss_en": "perilous; nearly probable"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "或许 introduces speculative, soft, and polite possibilities in literary or analytical prose.",
            "contrasts": [
                {"id": "1", "compared_word": "或许 vs. 也许", "pinyin": "yěxǔ", "analysis": "也许 is more frequent in everyday conversational oral speech, while 或许 possesses a more formal, reflective, and literary stylistic flavor."},
                {"id": "2", "compared_word": "或许 vs. 可能", "pinyin": "kěnéng", "analysis": "可能 can function as a noun ('有这种可能') or an adjective/auxiliary ('可能发生'), whereas 或许 functions solely as a sentence adverb."},
                {"id": "3", "compared_word": "或许 vs. 大概", "pinyin": "dàgài", "analysis": "大概 denotes high probability or rough numerical estimation ('大概八点钟'), whereas 或许 expresses open, speculative conjecture."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫漫人生旅途犹如攀登险峰，难免遭遇浓雾与陡坡。当我们感到迷茫疲惫时，不妨停下匆匆的脚步稍作歇息。或许在下一个蜿蜒的转角处，就会迎面撞见一片云蒸霞蔚、令人心醉神迷的绚丽壮景。",
                "pinyin": "Mànmàn rénshēng lǚtú yóurú pāndēng xiǎnfēng, nánmiǎn zāoyù nóngwù yǔ dǒupō. Dāng wǒmen gǎndào mímáng píbèi shí, bùfáng tíngxià cōngcōng de jiǎobù shāozuò xiēxī. Huòxǔ zài xià yí ge wānyán de zhuǎnjiǎochù, jiùhuì yíngmiàn zhuàngjiàn yí piàn yúnzhēng-xiáwèi, lìngrén-xīnduì-shénmí de xuànlì zhuàngjǐng.",
                "en": "Life's journey is like scaling peaks; fog and slopes are inevitable. When feeling weary and lost, pause your hurried steps. Perhaps at the next bend, breathtaking scenery bathed in golden clouds awaits you.",
                "es": "La senda vital asemeja la ascensión de cumbres, entre nieblas y pendientes. Ante la fatiga conviene detenerse y tomar aliento. Tal vez al doblar el próximo recodo se revele un deslumbrante mar de nubes doradas."
            },
            {
                "id": "#2",
                "hanzi": "在浩瀚无垠的宇宙深处，地球或许并不是唯一的生命摇篮。天文学家们借助先进的空间射电望远镜，日夜不停地巡视深邃星空、捕捉微弱无线电脉冲信号。或许在遥远的未来，人类终将揭开地外智慧文明的神秘面纱。",
                "pinyin": "Zài hàohàn-wúyín de yǔzhòu shēnchù, Dìqiú huòxǔ bìng bùshì wéiyī de shēngmìng yáolán. Tiānwénxuéjiāmen jièzhù xiānjìn de kōngjiān shèdiàn wàngyuǎnjìng, rìyè-bùtíng de xúnshì shēnsù xīngkōng, bǔzhuō wēiruò wúxiàndiàn màichōng xìnhào. Huòxǔ zài yáoyuǎn de wèilái, rénlèi zhōngjiāng jiēkāi dìwài zhìhuì wénmíng de shénmì miànshā.",
                "en": "In the boundless cosmos, Earth is perhaps not the sole cradle of life. Astronomers scan deep space with space telescopes, capturing radio pulses. Perhaps in the distant future, humanity will unveil extraterrestrial civilizations.",
                "es": "En la inmensidad del cosmos, la Tierra quizás no sea la única cuna viviente. Astrónomos rastrean señales de radio con radiotelescopios espaciales. Tal vez en un futuro remoto desvelaremos el enigma de inteligencias alienígenas."
            }
        ]
    },

    # 37 重大
    {
        "id": "37",
        "hanzi": "重大",
        "pinyin": "zhòng dà",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "great; momentous; significant; major; monumental",
            "es": "trascendental; de gran envergadura; crucial; capital"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "having great significance, consequence, scale, or far-reaching impact",
                "definition_es": "que reviste extraordinaria importancia, alcance, trascendencia o gravedad",
                "example_phrase": "取得重大突破 (achieve a major breakthrough)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "我国科学家在量子计算与量子通信领域取得了举世瞩目的重大突破，牢牢占据了国际科技制高点。",
                "pinyin": "Wǒguó kēxuéjiā zài liàngzǐ jìsuàn yǔ liàngzǐ tōngxìn lǐngyù qǔdé le jǔshì-zhǔmù de zhòngdà tūpò, láoláo zhànjù le guójì kējì zhìgāodiǎn.",
                "en": "Our country's scientists achieved world-renowned major breakthroughs in quantum computing, securing commanding heights in global tech.",
                "es": "Nuestros científicos lograron avances de trascendental envergadura en computación cuántica, conquistando un liderazgo mundial indiscutible."
            },
            {
                "id": "#2",
                "hanzi": "在涉及国家安全与人民群众根本利益的重大问题上，必须始终保持高度的政治敏锐性与原则性。",
                "pinyin": "Zài shèjí guójiā ānquán yǔ rénmín qúnzhòng gēnběn lìyì de zhòngdà wèntí shàng, bìxū shǐzhōng bǎochí gāodù de zhèngzhì mǐnruìxìng yǔ yuánzéxìng.",
                "en": "On momentous issues concerning national security and people's fundamental interests, one must maintain political sensitivity and principle.",
                "es": "En asuntos de capital trascendencia relativos a la seguridad nacional y el bienestar ciudadano, es imperativo mantener una sólida firmeza de principios."
            }
        ],
        "collocations": [
            {"hanzi": "重大突破", "en": "major breakthrough"},
            {"hanzi": "重大意义", "en": "monumental significance"},
            {"hanzi": "重大贡献", "en": "momentous contribution"},
            {"hanzi": "重大事故", "en": "major accident; severe incident"},
            {"hanzi": "重大决策", "en": "momentous strategic decision"},
            {"hanzi": "重大历史事件", "en": "major historical event"}
        ],
        "idioms": [
            {"hanzi": "举足轻重", "pinyin": "jǔ zú qīng zhòng", "meaning_en": "hold the balance of power; play a pivotal, decisive role"},
            {"hanzi": "至关重要", "pinyin": "zhì guān zhòng yào", "meaning_en": "of paramount importance; vital and crucial"},
            {"hanzi": "非同小可", "pinyin": "fēi tóng xiǎo kě", "meaning_en": "no trivial matter; of profound consequence"},
            {"hanzi": "重中之重", "pinyin": "zhòng zhōng zhī zhòng", "meaning_en": "the highest priority of all; priority among priorities"}
        ],
        "character_decomposition": [
            {
                "character": "重",
                "pinyin": "zhòng",
                "meaning_en": "heavy; weighty; serious; important",
                "meaning_es": "pesado; grave; importante; de peso",
                "radical": "里",
                "radical_meaning_en": "village / Chinese mile",
                "meaning_component": "人 (human standing) + 东 (heavy bundle strapped on back) + 土 (earth/burden)",
                "sound_component": "重 (zhòng)",
                "stroke_count": 9,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A person bending under a heavy baggage bundle 东 on their back; signifies weightiness, seriousness, and importance.",
                "visual_mnemonic_story_en": "A traveler carries a heavy loaded bundle (东) strapped tight, staggering under the weighty burden (重).",
                "visual_mnemonic_story_es": "Un caminante sostiene un fardo pesado (东) a sus espaldas, encorvándose bajo la enorme carga (重).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HJG",
                "traditional": ""
            },
            {
                "character": "大",
                "pinyin": "dà",
                "meaning_en": "big; large; great; grand",
                "meaning_es": "grande; grandioso; magno; mayor",
                "radical": "大",
                "radical_meaning_en": "big / great",
                "meaning_component": "人 (human stretching arms and legs out to maximum size)",
                "sound_component": "大 (dà)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of an adult person standing tall with arms stretched wide to represent greatness and scale.",
                "visual_mnemonic_story_en": "A person spreads arms wide to measure something huge and grand (大).",
                "visual_mnemonic_story_es": "Una persona extiende los brazos en cruz para abarcar algo inmenso y grandioso (大).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "K",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Both weighty in consequence (重) and vast in scale (大), a momentous event is created (重大).",
            "composite_memory_hook_es": "Pesado de consecuencias (重) e inmenso de escala (大) forjan lo trascendental y crucial (重大).",
            "cultural_and_cognitive_roots": "Synonym pairing of magnitude and consequence; applied in statecraft (国家大计) to demarcate cardinal political and civil landmarks.",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'zhòng dà' (51-51). Descend sharply and heavily on 'zhòng', then land firmly on 'dà'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "量", "pinyin": "liàng", "meaning_en": "measure; quantity", "distinction_note": "Has 日 atop 里 instead of 千 in 重"},
                {"character": "童", "pinyin": "tóng", "meaning_en": "child", "distinction_note": "Has 立 atop 里"},
                {"character": "太", "pinyin": "tài", "meaning_en": "too; extreme", "distinction_note": "Has a dot at bottom of 大"},
                {"character": "犬", "pinyin": "quǎn", "meaning_en": "dog", "distinction_note": "Has a dot at upper right of 大"}
            ],
            "etymological_cognates": [
                {"character": "巨", "pinyin": "jù", "gloss_en": "gigantic; immense size"},
                {"character": "要", "pinyin": "yào", "gloss_en": "crucial waist; essential"},
                {"character": "要", "pinyin": "zhòng", "gloss_en": "weight of bronze"},
                {"character": "伟", "pinyin": "wěi", "gloss_en": "extraordinary greatness"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "重大 modifies events, breakthroughs, policies, and consequences that carry profound institutional or historical impact.",
            "contrasts": [
                {"id": "1", "compared_word": "重大 vs. 重要", "pinyin": "zhòngyào", "analysis": "重要 is a widely applicable descriptor for anything essential or necessary in daily life ('重要的人', '重要的事情'), while 重大 is reserved for macroscopic, epochal events and breakthroughs ('重大转折', '重大胜利')."},
                {"id": "2", "compared_word": "重大 vs. 巨大", "pinyin": "jùdà", "analysis": "巨大 emphasizes immense physical volume, physical force, or quantitative scale ('巨大的石块', '巨大的反响'), whereas 重大 emphasizes profound consequence and significance."},
                {"id": "3", "compared_word": "重大 vs. 要紧", "pinyin": "yàojǐn", "analysis": "要紧 is an informal spoken adjective meaning urgent or critical ('不要紧 nothing serious'), lacking the institutional stature of 重大."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "港珠澳大桥作为连接粤港澳大湾区的三地跨海巨构，是国家重大工程建设史上的光辉里程碑。建设团队攻克了海底深埋沉管等一系列世界级技术难题，对促进区域经济深度融合发展具有深远重大的战略意义。",
                "pinyin": "Gǎng-Zhū-Ào Dàqiáo zuòwéi liánjiē Yuè-Gǎng-Ào Dàwānqū de sān dì kuàhǎi jùgòu, shì guójiā zhòngdà gōngchéng jiànshè shǐ shàng de guānghuī lǐchéngbēi. Jiànshè tuánduì gōngkè le hǎidǐ shēnmái chénguǎn děng yíxìliè shìjièjí jìshù nántí, duì cùjìn qūyù jīngjì shēndù rónghé fāzhǎn jùyǒu shēnyuǎn zhòngdà de zhànlüè yìyì.",
                "en": "The Hong Kong-Zhuhai-Macao Bridge, linking the Greater Bay Area, marks a milestone in national mega-engineering. Overcoming undersea tube engineering hurdles, it holds momentous strategic significance for regional integration.",
                "es": "El puente Hong Kong-Zhuhai-Macao constituye un hito glorioso en la megaingeniería nacional. Superando retos de túneles submarinos sumergidos, reviste una trascendencia estratégica capital para la integración comarcal."
            },
            {
                "id": "#2",
                "hanzi": "站在人类文明发展的历史十字路口，每一次科技革命都会引发生产力与社会结构的重大重塑。面对新一轮人工智能与绿色能源浪潮，各国唯有秉持开放包容与合作共赢的原则，才能有效防范重大全球性风险，携手开创美好未来。",
                "pinyin": "Zhàn zài rénlèi wénmíng fāzhǎn de lìshǐ shízìlùkǒu, měi yí cì kējì gémìng dōuhuì yǐnfā shēngchǎnlì yǔ shèhuì jiégòu de zhòngdà chóngsù. Miànduì xīn yì lún réngōng zhìnéng yǔ lǜsè néngyuán làngcháo, gèguó wéiyǒu bǐngchí kāifàng-bāoróng yǔ hézuò-gòngyíng de yuánzé, cáinéng yǒuxiào fángfàn zhòngdà quánqiúxìng fēngxiǎn, xiéshǒu kāichuàng měihǎo wèilái.",
                "en": "At history's crossroads, every scientific revolution triggers major reshaping of productivity and society. Facing AI and green energy waves, nations must uphold cooperation to guard against major global risks and forge a shared future.",
                "es": "En la encrucijada histórica de la civilización, toda revolución técnica suscita una transformación de gran calado. Ante la inteligencia artificial y la energía verde, la cooperación multilateral previene riesgos globales mayores."
            }
        ]
    }
]

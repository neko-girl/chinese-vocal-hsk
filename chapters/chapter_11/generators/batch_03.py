# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 慌张
    {
        "id": "21",
        "hanzi": "慌张",
        "pinyin": "huāng zhāng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "flustered; panic-stricken; confused; agitated",
            "es": "nervioso; atolondrado; desconcertado; presa del pánico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "flustered, hurried, agitated, and losing self-possession due to sudden panic or unexpected events",
                "definition_es": "inquieto, atolondrado y visiblemente turbado por una alarma o sorpresa repentina",
                "example_phrase": "神色慌张 (look flustered / panic-stricken in expression)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "看到巡逻民警迎面走来，小偷神色慌张地低下头，加快脚步试图溜走。",
                "pinyin": "Kàndào xúnluó mínjǐng yíngmiàn zǒulái, xiǎotōu shénsè huāngzhāng de dīxià tóu, jiākuài jiǎobù shìtú liūzǒu.",
                "en": "Seeing patrolling police officers approaching, the thief lowered his head with a flustered expression, quickening his steps to slip away.",
                "es": "Al ver aproximarse a la patrulla policial, el ratero bajó la cabeza con aire desconcertado apurando el paso para escaquearse."
            },
            {
                "id": "#2",
                "hanzi": "遭遇突发火灾警报时千万不要慌张，应当用湿毛巾捂住口鼻、弯腰有序撤离。",
                "pinyin": "Zāoyù tūfā huǒzāi jǐngbào shí qiānwàn búyào huāngzhāng, yīngdāng yòng shī máojīn wǔzhù kǒu-bí, wānyāo yǒuxù chèlí.",
                "en": "Never panic when facing a sudden fire alarm; cover mouth and nose with a damp towel, bend down, and evacuate in an orderly manner.",
                "es": "Jamás cunda el pánico ante una alarma de incendio repentina; cúbranse boca y nariz con un paño húmedo y desalojen agachados y en orden."
            }
        ],
        "collocations": [
            {"hanzi": "神色慌张", "en": "flustered expression; panicked look"},
            {"hanzi": "慌张失措", "en": "flustered and at a loss what to do"},
            {"hanzi": "不必慌张", "en": "no need to panic"},
            {"hanzi": "举止慌张", "en": "agitated/flustered manners"},
            {"hanzi": "十分慌张", "en": "extremely flustered"},
            {"hanzi": "显得慌张", "en": "appear panicked / look flurried"}
        ],
        "idioms": [
            {"hanzi": "惊慌失措", "pinyin": "jīng huāng shī cuò", "meaning_en": "panic-stricken and at a loss what to do; lose one's head"},
            {"hanzi": "手忙脚乱", "pinyin": "shǒu máng jiǎo luàn", "meaning_en": "hands and feet in a fluster; frantic disorder"},
            {"hanzi": "张皇失措", "pinyin": "zhāng huáng shī cuò", "meaning_en": "bewildered, terrified, and helpless in crisis"},
            {"hanzi": "镇定自若", "pinyin": "zhèn dìng zì ruò", "meaning_en": "calm, composed, and completely in control of oneself"}
        ],
        "character_decomposition": [
            {
                "character": "慌",
                "pinyin": "huāng",
                "meaning_en": "panicky; flurried; confused; nervous",
                "meaning_es": "inquieto; turbado; asustado; aturdido",
                "radical": "忄",
                "radical_meaning_en": "heart",
                "meaning_component": "忄 (distressed agitated heart) + 荒 (wasteland overgrown with weeds)",
                "sound_component": "荒 (huāng, wasteland / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Heart radical 忄 combined with 荒 (wild desolate weed fields); feelings thrown into disarray like a wild overgrown wasteland.",
                "visual_mnemonic_story_en": "Emotions in the heart (忄) run wild like weeds in an unkempt wasteland (荒), sparking panic (慌).",
                "visual_mnemonic_story_es": "Las emociones del corazón (忄) se desbordan como maleza en páramo yermo (荒) desatando el pavor (慌).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "PTYU",
                "traditional": ""
            },
            {
                "character": "张",
                "pinyin": "zhāng",
                "meaning_en": "draw bow; stretch; spread; display",
                "meaning_es": "tensar arco; abrir; extender; desplegar",
                "radical": "弓",
                "radical_meaning_en": "bow",
                "meaning_component": "弓 (archery bow) + 长 (long / extended tension)",
                "sound_component": "长 (cháng/zhǎng, long / phonetic carrier)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An archer drawing a bow 弓 to full length 长; represents stretching, tension, spreading out, or looking wide-eyed.",
                "visual_mnemonic_story_en": "Pulling an archer's bow (弓) taut to its longest stretch (长) strains tension (张).",
                "visual_mnemonic_story_es": "Tensar la cuerda del arco (弓) a su máxima longitud (长) refleja tirantez y agitación (张).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "NPO",
                "traditional": "張"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A heart thrown into wasteland panic (慌) stretched taut like a drawn bow (张) acts flustered (慌张).",
            "composite_memory_hook_es": "El corazón en páramo de pánico (慌) tenso como cuerda de arco (张) actúa atolondrado (慌张).",
            "cultural_and_cognitive_roots": "Folk psychological portrait: 慌 (internal mental confusion) paired with 张 (visible outward bodily agitation and frantic pacing).",
            "tone_sandhi_and_pitch_modulation": "Double level high first tones: 'huāng zhāng' (55-55). Hold level high pitch 55 across both syllables smoothly."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "谎", "pinyin": "huǎng", "meaning_en": "lie; falsehood", "distinction_note": "Has speech radical 讠 on left instead of heart 忄 in 慌"},
                {"character": "荒", "pinyin": "huāng", "meaning_en": "wasteland; famine", "distinction_note": "Has grass radical 艹 on top, lacking 忄"},
                {"character": "涨", "pinyin": "zhǎng", "meaning_en": "rise; swell", "distinction_note": "Has water radical 氵 on left instead of bow 弓 in 张"},
                {"character": "帐", "pinyin": "zhàng", "meaning_en": "tent; curtain", "distinction_note": "Has cloth radical 巾 on left of 长"}
            ],
            "etymological_cognates": [
                {"character": "恐", "pinyin": "kǒng", "gloss_en": "fear in heart"},
                {"character": "乱", "pinyin": "luàn", "gloss_en": "tangled silk disorder"},
                {"character": "忙", "pinyin": "máng", "gloss_en": "busy heart; rushed"},
                {"character": "躁", "pinyin": "zào", "gloss_en": "restless feet stamping"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "慌张 emphasizes visible behavioral disarray, hurried clumsiness, and loss of composure under sudden fright.",
            "contrasts": [
                {"id": "1", "compared_word": "慌张 vs. 紧张", "pinyin": "jǐnzhāng", "analysis": "紧张 describes normal physiological nervousness before exams or performances without losing control ('考试前紧张'), while 慌张 is visible flustered disarray."},
                {"id": "2", "compared_word": "慌张 vs. 害怕", "pinyin": "hàipà", "analysis": "害怕 emphasizes subjective cowardice or dread of pain/danger ('害怕黑暗'), whereas 慌张 describes chaotic outward behavioral manner."},
                {"id": "3", "compared_word": "慌张 vs. 匆忙", "pinyin": "cōngmáng", "analysis": "匆忙 focuses simply on being rushed for time ('匆忙赶路'), without the panic or flustered fright of 慌张."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代空难与火灾逃生演练中，安全专家反复强调“遇险不慌张”的核心生存法则。当灾难降临时，盲目慌张奔逃只会导致致命的踩踏事故，唯有沉着冷静、服从指挥引导，才能在黄金时间内安全疏散。",
                "pinyin": "Zài xiàndài kōngnàn yǔ huǒzāi táoshēng yǎnliàn zhōng, ānquán zhuānjiā fǎnfù qiángdiào 'yùxiǎn bù huāngzhāng' de héxīn shēngcún fǎzé. Dāng zāinàn jiànglín shí, mángmù huāngzhāng bēntáo zhǐhuì dǎozhì zhìmìng de cǎità shìgù, wéiyǒu chénzhuó-lěngjìng, fúcóng zhǐhuī yǐndǎo, cáinéng zài huángjīn shíjiān nèi ānquán shūsàn.",
                "en": "In fire and emergency drills, experts stress the rule of avoiding panic. When disaster strikes, blind panic leads to fatal stampedes; remaining calm and following guidance ensures safe evacuation within golden minutes.",
                "es": "En simulacros de evacuación, expertos recalcan la regla de oro: mantener la calma ante el peligro. Huir despavoridos provoca avalanchas letales; solo la serenidad y la disciplina salvan vidas en minutos clave."
            },
            {
                "id": "#2",
                "hanzi": "当清晨闹钟骤然大作时，深度睡眠中的人体交感神经被强行激活，常常伴随一阵莫名的心慌意乱与神色慌张。这种突发性惊醒破坏了大脑从浅睡眠自然唤醒的平稳节律，长期以往会使人形成神经质的早起焦虑症。",
                "pinyin": "Dāng qīngchén nàozhōng zhòurán dàzuò shí, shēndù shuìmián zhōng de réntǐ jiāogǎn shénjīng bèi qiángxíng jīhuó, chángcháng bànsuí yí zhèn mòmíng de xīnhuāng-yìluàn yǔ shénsè huāngzhāng. Zhè zhǒng tūfāxìng jīngxǐng pòhuài le dànǎo cóng qiǎn shuìmián zìrán huànxǐng de píngwěn jiélǜ, chángqī yǐwǎng huì shǐ rén xíngchéng shénjīngzhì de zǎoqǐ jiāolǜzhèng.",
                "en": "When alarms blare, sympathetic nerves in deep sleepers activate abruptly, accompanied by heart palpitations and flustered panic. This sudden jolt disrupts smooth natural awakening, inducing chronic morning anxiety.",
                "es": "Al rugir el despertador, el sistema simpático se activa de golpe provocando palpitaciones y agitación ansiosa. Esta sacudida quiebra el despertar apacible desde el sueño ligero, induciendo una neurosis matinal crónica."
            }
        ]
    },

    # 22 情绪
    {
        "id": "22",
        "hanzi": "情绪",
        "pinyin": "qíng xù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "emotion; mood; sentiment; morale",
            "es": "emoción; estado de ánimo; humor; temple"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a conscious mental reaction (anger, joy, grief, fear) subjectively experienced and accompanied by physiological changes",
                "definition_es": "reacción psicofisiológica que refleja el estado de ánimo (alegría, cólera, pena, desánimo)",
                "example_phrase": "控制情绪 (control one's emotions)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "成年人最重要的一项修养，就是在遇到挑衅或不顺心的事情时能够理智地管理好自己的负面情绪。",
                "pinyin": "Chéngniánrén zuì zhòngyào de yí xiàng xiūyǎng, jiùshì zài yùdào tiǎoxìn huò búshùnxīn de shìqing shí nénggòu lǐzhì de guǎnlǐ hǎo zìjǐ de fùmiàn qíngxù.",
                "en": "An adult's most important cultivation is managing negative emotions rationally when facing provocation or setbacks.",
                "es": "El rasgo primordial de madurez es saber gobernar las emociones negativas con raciocinio ante afrentas o contrariedades."
            },
            {
                "id": "#2",
                "hanzi": "连日阴雨绵绵、不见天日，灰暗低沉的天气容易导致部分敏感体质的人产生烦躁压抑的消极情绪。",
                "pinyin": "Liánrì yīnyǔ miánmián, bú jiàn tiānrì, huī'àn dīchén de tiānqì róngyì dǎozhì bùfen mǐngǎn tǐzhì de rén chǎnshēng fánzào yāyì de xiāojí qíngxù.",
                "en": "Successive days of continuous overcast rain and lack of sunshine easily cause sensitive people to develop irritable, depressed moods.",
                "es": "Días seguidos de llovizna plomiza y falta de sol inducen fácilmente desánimo, fastidio y melancolía en personas sensibles."
            }
        ],
        "collocations": [
            {"hanzi": "稳定情绪", "en": "stabilize emotions / calm down"},
            {"hanzi": "负面情绪", "en": "negative emotions"},
            {"hanzi": "情绪低落", "en": "depressed mood / low spirits"},
            {"hanzi": "情绪激动", "en": "emotionally agitated / excited"},
            {"hanzi": "控制情绪", "en": "control one's temper/emotions"},
            {"hanzi": "情绪波动", "en": "mood swings / emotional fluctuations"}
        ],
        "idioms": [
            {"hanzi": "喜怒无常", "pinyin": "xǐ nù wú cháng", "meaning_en": "capricious and temperamental; unpredictable mood swings"},
            {"hanzi": "喜形于色", "pinyin": "xǐ xíng yú sè", "meaning_en": "joy beaming on one's face; visibly joyful"},
            {"hanzi": "心平气和", "pinyin": "xīn píng qì hé", "meaning_en": "calm and even-tempered; placid in mind and breath"},
            {"hanzi": "意气风发", "pinyin": "yì qì fēng fā", "meaning_en": "in high and enthusiastic spirits; daring vigor"}
        ],
        "character_decomposition": [
            {
                "character": "情",
                "pinyin": "qíng",
                "meaning_en": "feeling; emotion; sentiment; passion; situation",
                "meaning_es": "sentimiento; afecto; emoción; situación",
                "radical": "忄",
                "radical_meaning_en": "heart",
                "meaning_component": "忄 (inner heart feelings) + 青 (pure green / budding life)",
                "sound_component": "青 (qīng, green/pure / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Heart radical 忄 combined with 青 (pure youthful vigor); feelings and emotional affections welling up from within the human soul.",
                "visual_mnemonic_story_en": "Feelings in the human heart (忄) bloom fresh and genuine like spring greenery (青), creating emotion (情).",
                "visual_mnemonic_story_es": "Los afectos del corazón (忄) brotan con la lozanía de la primavera verde (青) expresando la emoción (情).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "PQMB",
                "traditional": ""
            },
            {
                "character": "绪",
                "pinyin": "xù",
                "meaning_en": "thread end; beginning; mental state; clue",
                "meaning_es": "cabo de hilo; principio; hilo mental; pista",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (skein of silk thread) + 者 (person sorting fibers)",
                "sound_component": "者 (zhě, person / phonetic origin)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk radical 纟 paired with 者; pulling the initial lead thread end out of a tangled cocoon to unravel order, extended to mental strands of mood.",
                "visual_mnemonic_story_en": "A hand pulls the lead thread (纟) from a silk cocoon (者), sorting tangled emotional strands (绪).",
                "visual_mnemonic_story_es": "Una mano desentraña el cabo (纟) de un capullo de seda (者) ordenando la maraña de afectos (绪).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMJKA",
                "traditional": "緒"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Heartfelt affections (情) tangled like unraveled silk threads (绪) make up human emotions and moods (情绪).",
            "composite_memory_hook_es": "Afectos del corazón (情) deshilvanados como hebras de seda (绪) componen el estado anímico (情绪).",
            "cultural_and_cognitive_roots": "Literary psychological metaphor (千头万绪: thousands of tangled emotional thread-ends); silk reeling mirrors the delicate sorting of complex psychological states.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'qíng xù' (35-51). Rise smoothly on 'qíng', then descend decisively on 'xù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "晴", "pinyin": "qíng", "meaning_en": "sunny; clear", "distinction_note": "Has sun radical 日 on left of 青 instead of heart 忄 in 情"},
                {"character": "请", "pinyin": "qǐng", "meaning_en": "please; invite", "distinction_note": "Has speech radical 讠 on left of 青"},
                {"character": "绩", "pinyin": "jì", "meaning_en": "merit; achievement", "distinction_note": "Has 责 on right of 纟 instead of 者 in 绪"},
                {"character": "续", "pinyin": "xù", "meaning_en": "continue", "distinction_note": "Has 卖 on right of 纟"}
            ],
            "etymological_cognates": [
                {"character": "感", "pinyin": "gǎn", "gloss_en": "feel; moved by emotion"},
                {"character": "意", "pinyin": "yì", "gloss_en": "inner voice of heart; intent"},
                {"character": "心", "pinyin": "xīn", "gloss_en": "seat of feelings; heart"},
                {"character": "志", "pinyin": "zhì", "gloss_en": "willpower of mind"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "情绪 refers to dynamic, subjective psychological moods and emotional reactions.",
            "contrasts": [
                {"id": "1", "compared_word": "情绪 vs. 情感", "pinyin": "qínggǎn", "analysis": "情感 refers to deep, enduring, and stable moral or interpersonal sentiments (patriotic affection, love of family), while 情绪 refers to transient moods (anger, sadness, joy)."},
                {"id": "2", "compared_word": "情绪 vs. 心情", "pinyin": "xīnqíng", "analysis": "心情 is colloquial and refers to personal daily good/bad moods ('心情愉快'), while 情绪 can describe collective morale of crowds ('群众情绪稳定')."},
                {"id": "3", "compared_word": "情绪 vs. 脾气", "pinyin": "píqi", "analysis": "脾气 refers to innate human temperament or anger tantrums ('发脾气'), distinct from scientific emotional states."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "现代心理学研究发现，情绪并非理性思考的对立面，而是人类漫长演化历程中形成的高效生存预警机制。接纳自身情绪的存在，学会识别恐惧、愤怒或悲伤背后的心理诉求，是建立强大心理复原力不可或缺的第一步。",
                "pinyin": "Xiàndài xīnlǐxué yánjiū fāxiàn, qíngxù bìngfēi lǐxìng sīkǎo de duìlìmiàn, érshì rénlèi màncháng yǎnhuà lìchéng zhōng xíngchéng de gāoxiào shēngcún yùjǐng jīzhì. Jiēnà zìshēn qíngxù de cúnzài, xuéhuì shíbié kǒngjù, fènnù huò bēishāng bèihòu de xīnlǐ sùqiú, shì jiànlì qiángdà xīnlǐ fùyuánlì bùkě-huòquē de dì-yī bù.",
                "en": "Psychology shows emotions are not foes of reason, but efficient survival alert mechanisms evolved over eons. Accepting emotions and decoding the needs behind fear or anger is the first step toward building resilience.",
                "es": "La psicología moderna demuestra que la emoción no riñe con la razón, sino que es una alerta evolutiva de supervivencia. Asumir los afectos y descifrar el temor o la ira es clave para forjar resiliencia."
            },
            {
                "id": "#2",
                "hanzi": "在团队管理与团队协作中，领导者的情绪稳定度直接决定了整个团队的凝聚力与战斗力。面对突如其来的危机考验，主心骨若能从容镇定、临危不乱，便能有效抚平下属的恐慌情绪，带领大家迎难而上化解险情。",
                "pinyin": "Zài tuánduì guǎnlǐ yǔ tuánduì xiézuò zhōng, lǐngdǎozhě de qíngxù wěndìngdù zhíjiē juédìng le zhěng gè tuánduì de níngjùlì yǔ zhàndòulì. Miànduì tūrúqílái de wēijī kǎoyàn, zhǔxīngǔ ruò néng cóngróng-zhèndìng, línwēi-búluàn, biàn néng yǒuxiào fǔpíng xiàshǔ de kǒnghuāng qíngxù, dàilǐng dàjiā yíngnán'érshàng huàjiě xiǎnqíng.",
                "en": "In leadership, emotional stability determines team cohesion and fighting power. When facing crises, an unshakeable leader calms subordinates' panic, guiding everyone to confront difficulties and defuse peril.",
                "es": "En la dirección de equipos, el temple anímico del líder apuntala la cohesión colectiva. Ante las tempestades, un guía sereno sosiega el pánico general liderando con firmeza la superación del trance."
            }
        ]
    },

    # 23 低落
    {
        "id": "23",
        "hanzi": "低落",
        "pinyin": "dī luò",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "downcast; depressed; low (spirits/morale); slumped",
            "es": "decaído; abatido; deprimido; bajo (ánimo, moral)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "low, depressed, slumped, or sinking (of mood, morale, spirits, or tide)",
                "definition_es": "decaído, abatido o en declive (dicho del ánimo, moral o nivel de las aguas)",
                "example_phrase": "情绪低落 (downcast in mood)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这次全国选拔赛痛失冠军后，他连续好几天情绪低落，一个人躲在房间里闭门不出。",
                "pinyin": "Zhè cì quánguó xuǎnbásài tòngshī guànjūn hòu, tā liánxù hǎojǐ tiān qíngxù dīluò, yí ge rén duǒ zài fángjiān lǐ bìmén-bùchū.",
                "en": "After painfully missing the championship in this national trial, he remained in low spirits for days, hiding alone behind closed doors.",
                "es": "Tras perder el campeonato nacional por la mínima, anduvo abatido varios días encerrado a solas en su cuarto sin ver a nadie."
            },
            {
                "id": "#2",
                "hanzi": "部队遭遇强敌阻击受挫，指挥官发表了慷慨激昂的动员讲话，彻底扭转了士气低落的被动局面。",
                "pinyin": "Bùduì zāoyù qiángdí zǔjī shòucuò, zhǐhuīguān fābiǎo le kāngkǎi-jī'áng de dòngyuán jiǎnghuà, chèdǐ niǔzhuǎn le shìqì dīluò de bèidòng júmiàn.",
                "en": "Suffering setbacks against strong enemy ambushes, the commander delivered an impassioned rousing speech, reversing the low morale.",
                "es": "Ante el repliegue por el fuego enemigo, la vibrante arenga del comandante levantó la alicaída moral de la tropa trocando el rumbo del combate."
            }
        ],
        "collocations": [
            {"hanzi": "情绪低落", "en": "depressed mood / low spirits"},
            {"hanzi": "士气低落", "en": "low morale"},
            {"hanzi": "神情低落", "en": "downcast expression"},
            {"hanzi": "情绪非常低落", "en": "extremely despondent"},
            {"hanzi": "走出低落", "en": "step out of depression/slump"},
            {"hanzi": "潮水低落", "en": "ebb tide / low water level"}
        ],
        "idioms": [
            {"hanzi": "垂头丧气", "pinyin": "chuí tóu sàng qì", "meaning_en": "hang one's head in dejection; crestfallen"},
            {"hanzi": "闷闷不乐", "pinyin": "mèn mèn bú lè", "meaning_en": "gloomy and sullen; out of sorts"},
            {"hanzi": "灰心丧气", "pinyin": "huī xīn sàng qì", "meaning_en": "lose heart and despondent; disheartened"},
            {"hanzi": "振作精神", "pinyin": "zhèn zuò jīng shén", "meaning_en": "pull oneself together; summon up one's spirits"}
        ],
        "character_decomposition": [
            {
                "character": "低",
                "pinyin": "dī",
                "meaning_en": "low; beneath; hang down; inferior",
                "meaning_es": "bajo; inferior; agachar; descender",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person bowing) + 氐 (bottom / foundation)",
                "sound_component": "氐 (dǐ, base / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 bowing low down to the ground or foundation 氐; signifies low height, drooping head, or modest depth.",
                "visual_mnemonic_story_en": "A standing person (亻) bows down low to the soil baseline (氐), hanging the head (低).",
                "visual_mnemonic_story_es": "Una persona (亻) agacha la cabeza humilde hacia la base del suelo (氐) inclinándose baja (低).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OHYPM",
                "traditional": ""
            },
            {
                "character": "落",
                "pinyin": "luò",
                "meaning_en": "fall; drop; descend; decline; settlement",
                "meaning_es": "caer; descender; declinar; aldea",
                "radical": "艹",
                "radical_meaning_en": "grass / plant",
                "meaning_component": "艹 (leaves/foliage) + 洛 (water swirling down)",
                "sound_component": "洛 (luò, water river / phonetic)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Autumn leaves 艹 falling drifting down upon swirling waters 洛; signifies descending, falling, or dropping low.",
                "visual_mnemonic_story_en": "Withered autumn leaves (艹) swirl downward on flowing river water (洛), falling low (落).",
                "visual_mnemonic_story_es": "Hojas marchitas de otoño (艹) flotan descendiendo por el agua del río (洛), cayendo al suelo (落).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TEHR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Bowing low (低) like withered autumn leaves falling to earth (落) portrays downcast spirits (低落).",
            "composite_memory_hook_es": "Inclinarse bajo (低) como hojas de otoño cayendo a tierra (落) retrata el abatimiento (低落).",
            "cultural_and_cognitive_roots": "Spatial elevation metaphor (Lakoff & Johnson: happy is up, sad is down); dropping down from high vitality into a despondent trough.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling fourth tone: 'dī luò' (55-51). Hold high pitch 55 on 'dī', then plunge down sharply on 'luò'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "底", "pinyin": "dǐ", "meaning_en": "bottom; foundation", "distinction_note": "Has shelter radical 广 enclosing 氐 instead of person 亻 in 低"},
                {"character": "抵", "pinyin": "dǐ", "meaning_en": "resist;抵押 mortgage", "distinction_note": "Has hand radical 扌 on left of 氐"},
                {"character": "满", "pinyin": "mǎn", "meaning_en": "full", "distinction_note": "Has water radical 氵 on left of 艹 and 两"},
                {"character": "暮", "pinyin": "mù", "meaning_en": "dusk", "distinction_note": "Has 日 underneath 艹 and 大"}
            ],
            "etymological_cognates": [
                {"character": "沉", "pinyin": "chén", "gloss_en": "sink into water deep"},
                {"character": "降", "pinyin": "jiàng", "gloss_en": "descend from steep hill"},
                {"character": "下", "pinyin": "xià", "gloss_en": "below; downwards"},
                {"character": "垂", "pinyin": "chuí", "gloss_en": "droop down heavy"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "低落 specifically modifies psychological moods or collective morale sinking into a disheartened trough.",
            "contrasts": [
                {"id": "1", "compared_word": "低落 vs. 沮丧", "pinyin": "jǔsàng", "analysis": "沮丧 emphasizes acute disappointment, frustration, and wounded self-esteem following a setback, while 低落 is quiet, passive emotional flatness."},
                {"id": "2", "compared_word": "低落 vs. 低沉", "pinyin": "dīchén", "analysis": "低沉 modifies acoustic voice pitch (deep, muffled voice: '声音低沉') or dark gloomy weather, while 低落 modifies mood and morale."},
                {"id": "3", "compared_word": "低落 vs. 悲伤", "pinyin": "bēishāng", "analysis": "悲伤 refers to sharp sorrow, weeping, and grief over loss, while 低落 is low energy and apathy."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "人生的旅途中总会经历潮起潮落，遭遇挫折时情绪低落是极其正常的生理应激反应。关键在于不要长期沉溺于自我怀疑的消极泥潭中，应当多与良师益友交流倾诉，在温暖关爱中重燃对美好生活的信心与热爱。",
                "pinyin": "Rénshēng de lǚtú zhōng zǒng huì jīnglì cháoqǐ-cháoluò, zāoyù cuòzhé shí qíngxù dīluò shì jíqí zhèngcháng de shēnglǐ yìngjī fǎnyìng. Guānjiàn zàiyú búyào chángqī chénnì yú zìwǒ huáiyí de xiāojí nítán zhōng, yīngdāng duō yǔ liángshī-yìyǒu jiāoliú qīngsù, zài wēnnuǎn guān'ài zhōng chóngrán duì měihǎo shēnghuó de xìnxīn yǔ rè'ài.",
                "en": "In life's journey, tides ebb and flow; low moods after setbacks are normal stress reactions. The key is avoiding prolonged self-doubt, confiding in mentors and friends to rekindle confidence and love for life.",
                "es": "La vida conoce pleamares y bajamares; decaerse ante reveses es una respuesta humana natural. Lo crucial es no encallarse en la apatía, desahogándose con leales amigos para avivar la confianza en el porvenir."
            },
            {
                "id": "#2",
                "hanzi": "医学临床调查显示，慢性失眠患者由于夜间缺乏深度脑部休息，白天更容易陷入情绪低落与注意力涣散的恶性循环。保证规律作息、适当接受日光照射，能够有效促进大脑分泌多巴胺与血清素，驱散心灵阴霾。",
                "pinyin": "Yīxué línchuáng diàochá xiǎnshì, mànxìng shīmián huànzhě yóuyú yèjiān quēfá shēndù nǎobù xiūxi, báitiān gèng róngyì xiànrù qíngxù dīluò yǔ zhùyìlì huànsàn de èxìng xúnhuán. Bǎozhèng guīlǜ zuòxī, shìdàng jiēshòu rìguāng zhàoshè, nénggòu yǒuxiào cùjìn dànǎo fēnmì duōbā'àn yǔ xuèqīngsù, qūsàn xīnlíng yīnmái.",
                "en": "Clinical surveys show chronic insomniacs, lacking deep brain rest at night, easily fall into cycles of low spirits and distraction. Maintaining regular routines and soaking in sunlight stimulates dopamine to dispel gloom.",
                "es": "Estudios clínicos revelan que el insomnio crónico aboca de día a un círculo vicioso de desánimo y dispersión. Guardar horarios regulares y tomar el sol estimula la serotonina, disipando la bruma anímica."
            }
        ]
    },

    # 24 记忆
    {
        "id": "24",
        "hanzi": "记忆",
        "pinyin": "jì yì",
        "part_of_speech": "Noun / Verb",
        "meanings_summary": {
            "en": "memory; recollection; to memorize; to remember",
            "es": "memoria; recuerdo; acordarse; memorizar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the cognitive faculty of encoding, retaining, and recalling past experiences, information, or skills",
                "definition_es": "facultad cognitiva de retener y recordar vivencias o nociones pasadas; recuerdo",
                "example_phrase": "记忆力很强 (have a strong memory)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to commit to memory, memorize, or keep consciously in mind",
                "definition_es": "memorizar, retener o fijar conocimientos en la mente",
                "example_phrase": "记忆生词 (memorize new vocabulary)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "童年在外婆家门前那条清澈溪流边捉螃蟹的快乐时光，是他脑海中永不褪色的美好记忆。",
                "pinyin": "Tóngnián zài wàipó jiā ménqián nà tiáo qīngchè xīliú biān zhuō pángxiè de kuàilè shíguāng, shì tā nǎohǎi zhōng yǒngbútùisè de měihǎo jìyì.",
                "en": "Childhood happy hours catching crabs beside the clear brook before maternal grandmother's house are timeless memories that never fade in his mind.",
                "es": "Las risas de infancia atrapando cangrejos en el arroyo límpido frente a casa de la abuela son recuerdos imborrables en su memoria."
            },
            {
                "id": "#2",
                "hanzi": "神经科学研究表明，高质量的深度睡眠对于大脑巩固日间所学知识与形成长期记忆至关重要。",
                "pinyin": "Shénjīng kēxué yánjiū biǎomíng, gāozhìliàng de shēndù shuìmián duìyú dànǎo gǒnggù rìjiān suǒ xué zhīshi yǔ xíngchéng chángqī jìyì zhìguān-zhòngyào.",
                "en": "Neuroscience indicates that high-quality deep sleep is crucial for the brain to consolidate daytime knowledge and form long-term memories.",
                "es": "La neurociencia constata que el sueño profundo de calidad es crucial para que el cerebro fije lo aprendido y consolide la memoria duradera."
            }
        ],
        "collocations": [
            {"hanzi": "记忆力", "en": "memory capacity; power of recollection"},
            {"hanzi": "童年记忆", "en": "childhood memories"},
            {"hanzi": "恢复记忆", "en": "recover memory"},
            {"hanzi": "长期记忆", "en": "long-term memory"},
            {"hanzi": "失去记忆", "en": "lose memory / amnesia"},
            {"hanzi": "唤醒记忆", "en": "awaken/evoke memories"}
        ],
        "idioms": [
            {"hanzi": "记忆犹新", "pinyin": "jì yì yóu xīn", "meaning_en": "remain fresh in one's memory; remember as if yesterday"},
            {"hanzi": "难以忘怀", "pinyin": "nán yǐ wàng huái", "meaning_en": "hard to forget; cherished unforgettable memory"},
            {"hanzi": "过目不忘", "pinyin": "guò mù bù wàng", "meaning_en": "photographic memory; never forget what has once been seen"},
            {"hanzi": "铭肌镂骨", "pinyin": "míng jī lòu gǔ", "meaning_en": "engraved on flesh and bone; indelible deep gratitude"}
        ],
        "character_decomposition": [
            {
                "character": "记",
                "pinyin": "jì",
                "meaning_en": "record; remember; chronicle; mark",
                "meaning_es": "anotar; recordar; crónica; marca",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken words recorded) + 己 (self / boundary marker)",
                "sound_component": "己 (jǐ / phonetic)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 committed to personal awareness 己 on bamboo slips; signifies recording, noting down, or remembering.",
                "visual_mnemonic_story_en": "Words (讠) are noted down carefully for oneself (己) so as to remember (记).",
                "visual_mnemonic_story_es": "Las palabras (讠) se anotan para uno mismo (己) a fin de recordarlas bien (记).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVSU",
                "traditional": "記"
            },
            {
                "character": "忆",
                "pinyin": "yì",
                "meaning_en": "remember; recall; memory",
                "meaning_es": "recordar; evocar; memoria",
                "radical": "忄",
                "radical_meaning_en": "heart",
                "meaning_component": "忄 (inner heart sentiment) + 乙 (twisted sprouting sprout)",
                "sound_component": "乙 (yǐ / phonetic origin)",
                "stroke_count": 4,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Heart radical 忄 storing uncurling thoughts and recollections 乙; represents reflecting back upon past events in the heart.",
                "visual_mnemonic_story_en": "The heart (忄) traces back through winding past experiences (乙) to recall memories (忆).",
                "visual_mnemonic_story_es": "El corazón (忄) desanda meandros del pasado (乙) evocando tiernos recuerdos (忆).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "PN",
                "traditional": "憶"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Notes recorded in words (记) that uncurl feelings in the heart (忆) form our memories (记忆).",
            "composite_memory_hook_es": "Apuntes transcritos en palabras (记) que despiertan el eco del corazón (忆) forman la memoria (记忆).",
            "cultural_and_cognitive_roots": "Epistemological pairing: 记 (external recorded inscription) + 忆 (internal affective recall in the heart); cognitive retaining and retrieving.",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'jì yì' (51-51). Descend sharply on 'jì', then land firmly with equal force on 'yì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "纪", "pinyin": "jì", "meaning_en": "era; record", "distinction_note": "Has silk radical 纟 on left of 己 instead of speech 讠 in 记"},
                {"character": "订", "pinyin": "dìng", "meaning_en": "book; subscribe", "distinction_note": "Has 丁 on right of 讠"},
                {"character": "乞", "pinyin": "qǐ", "meaning_en": "beg", "distinction_note": "Has upper horizontal stroke, unlike 乙"},
                {"character": "忙", "pinyin": "máng", "meaning_en": "busy", "distinction_note": "Has 亡 on right of 忄 instead of 乙 in 忆"}
            ],
            "etymological_cognates": [
                {"character": "念", "pinyin": "niàn", "gloss_en": "think of; mindful thought"},
                {"character": "怀", "pinyin": "huái", "gloss_en": "bosom; cherish memory"},
                {"character": "思", "pinyin": "sī", "gloss_en": "ponder deeply; yearn"},
                {"character": "想", "pinyin": "xiǎng", "gloss_en": "imagine; remember tree"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "记忆 encompasses both the biological cognitive storage faculty (memory capacity) and individual recollections of past events.",
            "contrasts": [
                {"id": "1", "compared_word": "记忆 vs. 回忆", "pinyin": "huíyì", "analysis": "回忆 is an active dynamic verb meaning 'to recall / reminisce about past events' ('回忆童年往事'), while 记忆 is the noun faculty ('记忆力') or content of memory."},
                {"id": "2", "compared_word": "记忆 vs. 纪念", "pinyin": "jìniàn", "analysis": "纪念 involves public honoring or keeping souvenirs of historical legacies ('人民英雄纪念碑'), while 记忆 is psychological storage."},
                {"id": "3", "compared_word": "记忆 vs. 记录", "pinyin": "jìlù", "analysis": "记录 refers to written notes, recorded logs, or athletic sports scores ('打破世界纪录'), not neural cognitive storage."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫步在故乡斑驳青石板铺成的小巷深处，古老民居院落里飘散出熟悉的饭菜香气，总能瞬间激活沉睡在脑海深处的童年记忆。时光虽已匆匆流逝数十载，但那份浸润着亲情与乡愁的温馨回忆，却历久弥新、清晰如昨。",
                "pinyin": "Mànbù zài gùxiāng bānbó qīngshíbǎn pūchéng de xiǎoxiàng shēnchù, gǔlǎo mínjū yuànluò lǐ piāosàn chū shúxī de fàncài xiāngqì, zǒng néng shùnjiān jīhuó chénsù zài nǎohǎi shēnchù de tóngnián jìyì. Shíguāng suī yǐ cōngcōng liúshì shùshí zǎi, dàn nà fèn jìnrùn zhe qīnqíng yǔ xiāngchóu de wēnxīn huíyì, què lìjiǔ-míxīn, qīngxī rú zuó.",
                "en": "Strolling deep in old paved alleyways of home, aromas from ancient courtyards instantly awaken dormant childhood memories. Though decades passed, warm recollections soaked in family love remain fresh as yesterday.",
                "es": "Pasear por callejuelas empedradas de la aldea natal oliendo guisos caseros revive recuerdos de infancia adormecidos. Aunque pasen decenios, esa memoria teñida de cariño y nostalgia sigue viva como ayer."
            },
            {
                "id": "#2",
                "hanzi": "数字化时代，海量外部智能设备在极大拓展人类信息储存边界的同时，也在不知不觉中削弱了人们的本能记忆能力。面对电话号码与日常行程安排，现代人越来越依赖手机备忘录，自主大脑记忆训练显得愈发重要。",
                "pinyin": "Shùzìhuà shídài, hǎiliàng wàibù zhìnéng shèbèi zài jídà tuòzhǎn rénlèi xìnxī chǔcún biānjiè de tóngshí, yě zài bùzhī-bùjué zhōng xuēruò le rénmen de běnnéng jìyì nénglì. Miànduì diànhuà hàomǎ yǔ rìcháng xíngchéng ānpái, xiàndàirén yuèláiyuè yīlài shǒujī bèiwànglù, zìzhǔ dànǎo jìyì xùnliàn xiǎnde yùfā zhòngyào.",
                "en": "In the digital age, smart devices expand information storage boundaries yet subtly weaken innate memory. Relying on phone memos for contacts and agendas, autonomous brain memory exercise is ever more vital.",
                "es": "En la era digital, la memoria externa de los dispositivos móviles expande datos pero merma la retentiva natural. Confiando teléfonos y citas a blocs digitales, ejercitar la propia memoria cerebral se torna indispensable."
            }
        ]
    },

    # 25 计算
    {
        "id": "25",
        "hanzi": "计算",
        "pinyin": "jì suàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to calculate; to compute; to reckon; calculation",
            "es": "calcular; computar; contar; cálculo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to determine mathematically through numerical operations, formulas, or algorithms",
                "definition_es": "determinar matemáticamente mediante operaciones numéricas, fórmulas o algoritmos",
                "example_phrase": "计算成本 / 计算机 (calculate costs / computer)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "航天测控中心的超级计算机仅用数秒时间，便精确计算出了飞船重返大气层的最佳轨道参数。",
                "pinyin": "Hángtiān cèkòng zhōngxīn de chāojí jìsuànjī jǐn yòng shù miǎo shíjiān, biàn jīngquè jìsuàn chū le fēichuán chóngfǎn dàqìcéng de zuìjiā guǐdào cānshù.",
                "en": "In mere seconds, the aerospace control center's supercomputer precisely calculated optimal orbital parameters for the spacecraft's reentry.",
                "es": "En escasos segundos, el superordenador del centro aeroespacial calculó con exactitud los parámetros orbitales para la reentrada de la nave."
            },
            {
                "id": "#2",
                "hanzi": "在做出这项重大商业投资决定之前，财务分析师必须严谨计算潜在的投资回报率与市场风险。",
                "pinyin": "Zài zuòchū zhè xiàng zhòngdà shāngyè tóuzī juédìng zhīqián, cáiwù fēnxīshī bìxū yánjǐn jìsuàn qiánzài de tóuzī huíbàolǜ yǔ shìchǎng fēngxiǎn.",
                "en": "Before making this major commercial investment decision, financial analysts must rigorously calculate potential return rates and market risks.",
                "es": "Antes de acometer esta inversión mercantil de calado, los analistas financieros deben calcular con rigor la rentabilidad y el riesgo de mercado."
            }
        ],
        "collocations": [
            {"hanzi": "计算机", "en": "computer"},
            {"hanzi": "精确计算", "en": "calculate precisely / exact computation"},
            {"hanzi": "计算成本", "en": "calculate costs"},
            {"hanzi": "云计算", "en": "cloud computing"},
            {"hanzi": "计算能力", "en": "computing power / computational capability"},
            {"hanzi": "计算结果", "en": "calculation result"}
        ],
        "idioms": [
            {"hanzi": "精打细算", "pinyin": "jīng dǎ xì suàn", "meaning_en": "careful calculation and strict budgeting; meticulous planning"},
            {"hanzi": "神机妙算", "pinyin": "shén jī miào suàn", "meaning_en": "miraculous calculation and ingenious reckoning; prescient planning"},
            {"hanzi": "算无遗策", "pinyin": "suàn wú yí cè", "meaning_en": "never fail in one's calculations; plans foolproof"},
            {"hanzi": "失算", "pinyin": "shī suàn", "meaning_en": "miscalculate; misjudge"}
        ],
        "character_decomposition": [
            {
                "character": "计",
                "pinyin": "jì",
                "meaning_en": "count; calculate; plan; meter",
                "meaning_es": "contar; calcular; plan; medidor",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken numbers counted) + 十 (ten / base-10 completeness)",
                "sound_component": "计 (jì)",
                "stroke_count": 4,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 counting numbers up to ten 十 in the decimal system; signifies counting, tallying, calculating, and planning.",
                "visual_mnemonic_story_en": "A clerk speaks numbers (讠) counting neatly up to ten (十) to reckon accounts (计).",
                "visual_mnemonic_story_es": "Un contable recita números (讠) sumando hasta diez (十) para cuadrar cuentas (计).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVJ",
                "traditional": "計"
            },
            {
                "character": "算",
                "pinyin": "suàn",
                "meaning_en": "calculate; reckon; count; plan; consider",
                "meaning_es": "calcular; contar; planear; considerar",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo counting rods) + 具/廾 (hands holding rods)",
                "sound_component": "算 (suàn)",
                "stroke_count": 14,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two hands 廾 manipulating bamboo counting rods 竹 atop an abacus frame; denotes arithmetic calculation and mathematical reckoning.",
                "visual_mnemonic_story_en": "Two hands (廾) manipulate bamboo counting sticks (竹) across an abacus frame to calculate (算).",
                "visual_mnemonic_story_es": "Dos manos (廾) mueven varillas de bambú (竹) sobre el tablero del ábaco para calcular (算).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HBUD",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Tallying numbers to ten (计) with bamboo counting rods (算) executes mathematical calculation (计算).",
            "composite_memory_hook_es": "Sumar cifras de diez en diez (计) con varillas de bambú en el ábaco (算) ejecuta el cálculo (计算).",
            "cultural_and_cognitive_roots": "Ancient Chinese mathematics: counting rods (算筹) and the suanpan abacus (算盘); formed the computational basis for the Nine Chapters on Mathematical Art (九章算术).",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'jì suàn' (51-51). Descend sharply on 'jì', then land with a firm snap on 'suàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "订", "pinyin": "dìng", "meaning_en": "book; agree", "distinction_note": "Has 丁 on right of 讠 instead of 十 in 计"},
                {"character": "讨", "pinyin": "tǎo", "meaning_en": "discuss; demand", "distinction_note": "Has 寸 on right of 讠"},
                {"character": "鼻", "pinyin": "bí", "meaning_en": "nose", "distinction_note": "Has 自 on top of 畀 instead of bamboo 竹 in 算"},
                {"character": "笨", "pinyin": "bèn", "meaning_en": "clumsy", "distinction_note": "Has 本 underneath 竹"}
            ],
            "etymological_cognates": [
                {"character": "数", "pinyin": "shǔ", "gloss_en": "count; tally grain"},
                {"character": "核", "pinyin": "hé", "gloss_en": "audit core numbers; verify"},
                {"character": "量", "pinyin": "liàng", "gloss_en": "measure grain bucket"},
                {"character": "估", "pinyin": "gū", "gloss_en": "estimate; appraise ancient value"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "计算 focuses on rigorous mathematical, algorithmic, or numerical computation of figures.",
            "contrasts": [
                {"id": "1", "compared_word": "计算 vs. 估算", "pinyin": "gūsuàn", "analysis": "估算 refers to rough approximation or guesswork without precise formulas, while 计算 requires exact arithmetic or algorithmic deduction."},
                {"id": "2", "compared_word": "计算 vs. 运算", "pinyin": "yùnsuàn", "analysis": "运算 specifically designates the mathematical operational process (+, -, ×, ÷ or boolean logic), while 计算 is the broader determination of quantities."},
                {"id": "3", "compared_word": "计算 vs. 打算", "pinyin": "dǎsuàn", "analysis": "打算 is a common colloquial verb meaning 'to plan / intend to do something' ('我打算去旅游'), not mathematical calculation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代数学家祖冲之凭借惊人的坚韧毅力，利用数千根简陋的竹制算筹在地上日夜演算，在世界上首次将圆周率精细计算到小数点后第七位。这项领先世界近千年的卓越数学计算成就，在人类科技史上铸就了永恒丰碑。",
                "pinyin": "Zhōngguó gǔdài shùxuéjiā Zǔ Chōngzhī píngjiè jīngrén de jiānrèn yìlì, lìyòng shùqiān gēn jiǎnlòu de zhúzhì suànchóu zài dìshang rìyè yǎnsuàn, zài shìjiè shàng shǒucì jiāng yuánzhōulǜ jīngxì jìsuàn dào xiǎoshùdiǎn hòu dì-qī wèi. Zhè xiàng lǐngxiān shìjiè jìn qiān nián de zhuóyuè shùxué jìsuàn chéngjiù, zài rénlèi kējì shǐ shàng zhùjiù le yǒnghéng fēngbēi.",
                "en": "Ancient mathematician Zu Chongzhi, calculating with thousands of bamboo rods, first determined Pi to seven decimal places. Leading the world for nearly a millennium, this outstanding calculation remains a monument in science.",
                "es": "El matemático antiguo Zu Chongzhi, con miles de varillas de bambú, calculó por primera vez el número Pi hasta siete decimales. Su proeza computacional, adelantada casi un milenio al mundo, es un hito de la ciencia."
            },
            {
                "id": "#2",
                "hanzi": "在人工智能与量子计算浪潮席卷全球的今天，强大的算力已成为衡量国家综合科研实力的战略支柱。量子计算机凭借颠覆性的量子叠加与纠缠特性，展现出指数级飞跃的计算速度，将彻底重塑药物研发与气象预测格局。",
                "pinyin": "Zài réngōng zhìnéng yǔ liàngzǐ jìsuàn làngcháo xíjuǎn quánqiú de jīntiān, qiángdà de suànlì yǐ chéngwéi héngliáng guójiā zōnghé kēyán shílì de zhànlüè zhīzhù. Liàngzǐ jìsuànjī píngjiè diānfùxìng de liàngzǐ diéjiā yǔ jiūchán tèxìng, zhǎnxiàn chū zhǐshùjí fēiyuè de jìsuàn sùdù, jiāng chèdǐ chóngsù yàowù yánfā yǔ qìxiàng yùcè géjú.",
                "en": "In the era of AI and quantum computing, computational power is a strategic pillar of national science strength. Harnessing quantum superposition, quantum computers show exponential leap in speeds, reshaping drug discovery.",
                "es": "En la era de la inteligencia artificial y la computación cuántica, la potencia de cálculo es pilar estratégico nacional. Con el entrelazamiento cuántico, los nuevos ordenadores multiplican su velocidad transformando la ciencia médica."
            }
        ]
    },

    # 26 相当
    {
        "id": "26",
        "hanzi": "相当",
        "pinyin": "xiāng dāng",
        "part_of_speech": "Adverb / Verb",
        "meanings_summary": {
            "en": "quite; considerably; equivalent to; to match; to balance",
            "es": "bastante; considerablemente; equivalente a; equiparable; equivaler"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "to a considerable degree; quite; fairly; pretty",
                "definition_es": "en grado notable; bastante; considerablemente",
                "example_phrase": "相当不错 (pretty good / quite impressive)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to be equal to, equivalent to, or balanced with in proportion or value",
                "definition_es": "equivaler, corresponder o igualarse en valor o proporción con otra cosa",
                "example_phrase": "与去年持平或相当 (be equivalent to last year)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过长达一年的严格系统训练，这位年轻选手的专业竞技水平已经相当出色了。",
                "pinyin": "Jīngguò chángdá yì nián de yángé xìtǒng xùnliàn, zhè wèi niánqīng xuǎnshǒu de zhuānyè jìngjì shuǐpíng yǐjīng xiāngdāng chūsè le.",
                "en": "After a year of rigorous systematic training, this young athlete's professional competitive level is already quite remarkable.",
                "es": "Tras un año de riguroso entrenamiento sistemático, el nivel competitivo de este joven deportista es ya bastante sobresaliente."
            },
            {
                "id": "#2",
                "hanzi": "这处新发现的特大型盐湖锂矿储量极其丰富，其总经济价值相当于一座大型金矿。",
                "pinyin": "Zhè chù xīnfāxiàn de tàdàxíng yánhú lǐkuàng chǔliàng jíqí fēngfù, qí zǒng jīngjì jiàzhí xiāngdāng yú yí zuò dàxíng jīnkuàng.",
                "en": "This newly discovered mega salt-lake lithium reserve is rich, its economic value equivalent to that of a major gold mine.",
                "es": "Las reservas de este megayacimiento de litio en salar son riquísimas, equivaliendo su valor total al de una gran mina de oro."
            }
        ],
        "collocations": [
            {"hanzi": "相当不错", "en": "pretty good; quite nice"},
            {"hanzi": "相当于", "en": "equivalent to; equal to"},
            {"hanzi": "势均力敌相当", "en": "evenly matched in balance"},
            {"hanzi": "相当严重", "en": "quite serious; considerably severe"},
            {"hanzi": "旗鼓相当", "en": "well-matched; equal in strength"},
            {"hanzi": "水平相当", "en": "on an equal level"}
        ],
        "idioms": [
            {"hanzi": "旗鼓相当", "pinyin": "qí gǔ xiāng dāng", "meaning_en": "banners and drums well-matched; equal in force and prowess"},
            {"hanzi": "势均力敌", "pinyin": "shì jūn lì dí", "meaning_en": "evenly matched in power and influence"},
            {"hanzi": "半斤八两", "pinyin": "bàn jīn bā liǎng", "meaning_en": "six of one and half a dozen of the other; much of a muchness"},
            {"hanzi": "相差无几", "pinyin": "xiāng chà wú jǐ", "meaning_en": "almost identical; differing by very little"}
        ],
        "character_decomposition": [
            {
                "character": "相",
                "pinyin": "xiāng",
                "meaning_en": "each other; mutually; reciprocal",
                "meaning_es": "mutuamente; el uno al otro; recíproco",
                "radical": "木",
                "radical_meaning_en": "wood / tree",
                "meaning_component": "木 (tree) + 目 (observing eye gazing at tree)",
                "sound_component": "相 (xiāng)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An eye 目 scrutinizing timber 木 up close; denotes inspecting, mutual gazing, and reciprocal relations.",
                "visual_mnemonic_story_en": "An eye (目) inspects a tree (木) face to face, engaging in mutual appraisal (相).",
                "visual_mnemonic_story_es": "Un ojo atento (目) contempla un árbol (木) frente a frente en mutuo examen recíproco (相).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DOU",
                "traditional": ""
            },
            {
                "character": "当",
                "pinyin": "dāng",
                "meaning_en": "bear; serve as; equal; match; when",
                "meaning_es": "asumir; ejercer de; igualar; corresponder",
                "radical": "⺌",
                "radical_meaning_en": "small / top",
                "meaning_component": "尚 (high / value) + 田 (fertile land value)",
                "sound_component": "当 (dāng)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Equal value of agricultural land 田 matched in valuation 尚; signifies balancing, matching, serving as, or corresponding to.",
                "visual_mnemonic_story_en": "Fields (田) balanced evenly on scales correspond in equal value (当).",
                "visual_mnemonic_story_es": "Campos de cultivo (田) pesados en la balanza igualan su valor recíproco (当).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "FSM",
                "traditional": "當"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Mutual inspection (相) reveals equal balanced value (当), meaning 'equivalent to' or 'quite' (相当).",
            "composite_memory_hook_es": "La mirada mutua (相) comprueba un peso equilibrado (当) significando equivalente o bastante (相当).",
            "cultural_and_cognitive_roots": "Metrology and barter trade: balancing equal goods on scale pans (相当: counterpart equivalence), which generalized adverbially to indicate considerable degree.",
            "tone_sandhi_and_pitch_modulation": "Double level high first tones: 'xiāng dāng' (55-55). Hold level high pitch 55 steadily across both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "想", "pinyin": "xiǎng", "meaning_en": "think", "distinction_note": "Has heart radical 心 underneath 相"},
                {"character": "箱", "pinyin": "xiāng", "meaning_en": "chest; trunk", "distinction_note": "Has bamboo radical 竹 atop 相"},
                {"character": "党", "pinyin": "dǎng", "meaning_en": "party; clan", "distinction_note": "Has 儿 at bottom instead of 彐 in 当"},
                {"character": "光", "pinyin": "guāng", "meaning_en": "light", "distinction_note": "Has 儿 underneath ⺌"}
            ],
            "etymological_cognates": [
                {"character": "等", "pinyin": "děng", "gloss_en": "equal bamboo slips"},
                {"character": "均", "pinyin": "jūn", "gloss_en": "potter wheel balance; equal"},
                {"character": "齐", "pinyin": "qí", "gloss_en": "ears of grain level"},
                {"character": "匹", "pinyin": "pǐ", "gloss_en": "equal match; bolt of cloth"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "相当 functions adverbially expressing a notable degree ('quite / rather') or verbally expressing equivalence ('equal to').",
            "contrasts": [
                {"id": "1", "compared_word": "相当 vs. 挺", "pinyin": "tǐng", "analysis": "挺 is colloquial spoken Chinese ('挺好的'), while 相当 has higher formality suitable for written reports and analytical essays ('相当成功')."},
                {"id": "2", "compared_word": "相当 vs. 非常", "pinyin": "fēicháng", "analysis": "非常 expresses an absolute superlative degree ('极度 / very'), while 相当 expresses a moderate to high degree ('quite / considerably')."},
                {"id": "3", "compared_word": "相当 vs. 等于", "pinyin": "děngyú", "analysis": "等于 is an exact mathematical equals sign (1+1=2), whereas 相当于 means equivalent in weight, value, or metaphoric significance."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在古代丝绸之路的黄金贸易时代，一匹做工极为精细奢华的中国蜀锦，在罗马帝国市场上能换取等重的纯金，其昂贵程度相当于普通贵族一整座豪华庄园的价值，见证了东西方文明交融的繁荣传奇。",
                "pinyin": "Zài gǔdài Sīchóuzhīlù de huángjīn màoyì shídài, yì pǐ zuògōng jíwéi jīngxì shēhuá de Zhōngguó shǔjǐn, zài Luómǎ Dìguó shìchǎng shàng néng huànqǔ děngzhòng de chúnjīn, qí ángguì chéngdù xiāngdāng yú pǔtōng guìzú yì zhěng zuò háohuá zhuāngyuán de jiàzhí, jiànzhèng le dōng-xīfāng wénmíng jiāoróng de fánróng chuánqí.",
                "en": "In the golden age of the Silk Road, a bolt of exquisite Chinese Shu brocade could trade for its weight in pure gold in Rome, its value equivalent to an entire noble estate, witnessing East-West exchange.",
                "es": "En la era dorada de la Ruta de la Seda, una pieza de fino brocado de Shu se trocaba en Roma por su peso en oro puro, equivaliendo a una villa aristocrática entera en el floreciente comercio euroasiático."
            },
            {
                "id": "#2",
                "hanzi": "科研人员在南极冰川钻取的这根深海冰芯样品具有相当高的学术研究价值。通过分析封存在微小冰层气泡中的古大气成分，科学家能够精确还原距今数十万年前地球气候冷暖交替的历史全貌，为预测全球变暖提供依据。",
                "pinyin": "Kēyán rényuán zài Nánjí bīngchuān zuānqǔ de zhè gēn shēnhǎi bīngxīn yàngpǐn jùyǒu xiāngdāng gāo de xuéshù yánjiū jiàzhí. Tōngguò fēnxī fēngcún zài wēixiǎo bīngcéng qìpào zhōng de gǔdàqì chéngfèn, kēxuéjiā nénggòu jīngquè huányuán jùjīn shùshíwàn nián qián Dìqiú qìhòu lěngnuǎn jiāotì de lìshǐ quánmào, wèi yùcè quánqiú biànnuǎn tígōng yījù.",
                "en": "The ice core drilled in Antarctica holds considerably high research value. By analyzing ancient atmospheric bubbles sealed in ice layers, scientists reconstruct climate cycles from millennia ago to model global warming.",
                "es": "El testigo de hielo extraído en la Antártida reviste un valor científico considerable. Analizando burbujas de aire fósil, los climatólogos reconstruyen épocas glaciares milenarias para pronosticar el calentamiento global."
            }
        ]
    },

    # 27 持续
    {
        "id": "27",
        "hanzi": "持续",
        "pinyin": "chí xù",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to continue; to persist; to last; continuous; sustained",
            "es": "continuar; durar; prolongarse; persistir; sostenido"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to extend without interruption or cessation over a period of time; to sustain",
                "definition_es": "mantenerse, prolongarse o proseguir sin interrupción en el tiempo; perdurar",
                "example_phrase": "持续发展 (sustainable development)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "连日来南方地区持续出现高温酷暑天气，多地最高气温突破了历史观测极值。",
                "pinyin": "Liánrì lái nánfāng dìqū chíxù chūxiàn gāowēn kùshǔ tiānqì, duō dì zuìgāo qìwēn tūpò le lìshǐ guāncè jízhí.",
                "en": "Over recent days, southern regions have experienced continuous scorching heat, with record temperatures shattered in multiple locations.",
                "es": "En los últimos días el sur del país ha padecido una persistente ola de calor tórrido, batiéndose récords históricos de temperatura en varias provincias."
            },
            {
                "id": "#2",
                "hanzi": "只有坚持走绿色低碳的可持续发展道路，才能为子孙后代留下天蓝地绿水清的美丽家园。",
                "pinyin": "Zhǐyào jiānchí zǒu lǜsè dītàn de kěchíxù fāzhǎn dàolù, cáinéng wèi zǐsūn-hòudài liúxià tiānlán-dìlǜ-shuǐqīng de měilì jiāyuán.",
                "en": "Only by adhering to green, low-carbon sustainable development can we bequeath a homeland with blue skies, green earth, and clear waters to posterity.",
                "es": "Solo perseverando en una senda ecológica de desarrollo sostenible legaremos a las generaciones venideras un hogar de cielos limpios y aguas diáfanas."
            }
        ],
        "collocations": [
            {"hanzi": "持续发展", "en": "sustainable development"},
            {"hanzi": "可持续", "en": "sustainable"},
            {"hanzi": "持续增长", "en": "sustained growth"},
            {"hanzi": "持续时间", "en": "duration; duration time"},
            {"hanzi": "持续进行", "en": "continue ongoing"},
            {"hanzi": "持续高温", "en": "persistent high temperatures"}
        ],
        "idioms": [
            {"hanzi": "持之以恒", "pinyin": "chí zhī yǐ héng", "meaning_en": "persevere relentlessly; persist constantly with constancy"},
            {"hanzi": "连绵不断", "pinyin": "lián mián bú duàn", "meaning_en": "continuous without break; unbroken stretch"},
            {"hanzi": "经久不衰", "pinyin": "jīng jiǔ bù shuāi", "meaning_en": "endure long without declining; unfailing vigor"},
            {"hanzi": "源源不断", "pinyin": "yuán yuán bú duàn", "meaning_en": "steady and continuous flow like a spring"}
        ],
        "character_decomposition": [
            {
                "character": "持",
                "pinyin": "chí",
                "meaning_en": "hold; grasp; support; maintain; persist",
                "meaning_es": "sostener; agarrar; mantener; perseverar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand holding firmly) + 寺 (temple court / measure rule)",
                "sound_component": "寺 (sì, temple / phonetic origin)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand 扌 upholding temple law and justice 寺; signifies firmly grasping, holding, maintaining, and supporting.",
                "visual_mnemonic_story_en": "A steady hand (扌) holds firm to temple principles (寺), upholding constancy (持).",
                "visual_mnemonic_story_es": "Una mano firme (扌) sostiene las leyes del templo (寺) perseverando sin desmayo (持).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "QGDI",
                "traditional": ""
            },
            {
                "character": "续",
                "pinyin": "xù",
                "meaning_en": "continue; join; extend; succession",
                "meaning_es": "continuar; empalmar; enlazar; suceder",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (silk thread) + 卖 (sell / continuous exchange)",
                "sound_component": "卖 (mài / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tying new silk thread ends 纟 onto depleted skeins to keep weaving continuously; represents joining, continuing, and prolonging.",
                "visual_mnemonic_story_en": "A weaver splices new silk strands (纟) into the loom (卖) to continue uninterrupted (续).",
                "visual_mnemonic_story_es": "El tejedor empalma nuevas hebras de seda (纟) en el telar (卖) para hilar sin corte (续).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMJDC",
                "traditional": "續"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Holding firmly in hand (持) and splicing continuous threads (续) maintains sustained duration (持续).",
            "composite_memory_hook_es": "Sostener firme en la mano (持) y empalmar hebras sin fin (续) mantiene la continuidad (持续).",
            "cultural_and_cognitive_roots": "Textile weaving metaphor: splicing silk filament ends (续丝) to maintain ceaseless cloth production; applied modernly to ecological sustainability (可持续发展).",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'chí xù' (35-51). Rise smoothly on 'chí', then descend firmly on 'xù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "特", "pinyin": "tè", "meaning_en": "special", "distinction_note": "Has cow radical 牜 on left of 寺 instead of hand 扌 in 持"},
                {"character": "待", "pinyin": "dài", "meaning_en": "wait; treat", "distinction_note": "Has step radical 彳 on left of 寺"},
                {"character": "读", "pinyin": "dú", "meaning_en": "read", "distinction_note": "Has speech radical 讠 on left of 卖 instead of silk 纟 in 续"},
                {"character": "渎", "pinyin": "dú", "meaning_en": "ditch; blaspheme", "distinction_note": "Has water radical 氵 on left"}
            ],
            "etymological_cognates": [
                {"character": "继", "pinyin": "jì", "gloss_en": "inherit; join silk fibers"},
                {"character": "连", "pinyin": "lián", "gloss_en": "chariots connected in line"},
                {"character": "久", "pinyin": "jiǔ", "gloss_en": "long duration of time"},
                {"character": "恒", "pinyin": "héng", "gloss_en": "constant moon; persistent"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "持续 emphasizes unbroken, sustained temporal progression or economic stability across an uninterrupted duration.",
            "contrasts": [
                {"id": "1", "compared_word": "持续 vs. 继续", "pinyin": "jìxù", "analysis": "继续 focuses on resuming an action after an interruption or progressing to the next step ('休息后继续干'), while 持续 means uninterrupted sustaining over a time span ('持续高温三周')."},
                {"id": "2", "compared_word": "持续 vs. 连续", "pinyin": "liánxù", "analysis": "连续 emphasizes discrete instances repeated one after another without gap ('连续打了五个电话'), while 持续 modifies continuous ongoing states."},
                {"id": "3", "compared_word": "持续 vs. 保持", "pinyin": "bǎochí", "analysis": "保持 is a transitive verb meaning to maintain a state or record ('保持整洁'), while 持续 emphasizes the natural duration itself."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国作为全球第二大经济体，近年来坚定不移践行新发展理念，大力推动经济社会绿色低碳转型。通过持续加大风电、光伏等清洁能源投资布局，不仅实现了能源结构的优化升级，更为全球应对气候变化注入了强大的可持续动能。",
                "pinyin": "Zhōngguó zuòwéi quánqiú dì-èr dà jīngjìtǐ, jìnniánlái jiāndìng-bùyí jiànxíng xīn fāzhǎn lǐniàn, dàlì tuīdòng jīngjì shèhuì lǜsè dītàn zhuǎnxíng. Tōngguò chíxù jiàdà fēngdiàn, guāngfú děng qīngjié néngyuán tóuzī bùjú, bùjǐn shíxiàn le néngyuán jiégòu de yōuhuà shēngjí, gèng wèi quánqiú yìngduì qìhòu biànhuà zhùrù le qiángdà de kěchíxù dòngnéng.",
                "en": "As the world's second-largest economy, China embraces green low-carbon transformation. Through sustained investment in wind and solar power, it upgrades its energy mix, injecting sustainable momentum into global climate efforts.",
                "es": "Como segunda economía mundial, China impulsa la transición verde descarbonizada. Invirtiendo de forma continuada en eólica y fotovoltaica, optimiza su matriz energética aportando un dinamismo sostenible a la lucha climática."
            },
            {
                "id": "#2",
                "hanzi": "求知钻研的道路漫长曲折，没有任何捷径可走。要想在学术研究中有所建树，不仅需要敏锐的学术眼光，更依赖于十年如一日持续深耕的专注毅力。唯有耐得住寂寞、持之以恒攻关，才能在厚积薄发中迎来璀璨突破。",
                "pinyin": "Qiúzhī zuānyán de dàolù màncháng qūzhé, méiyǒu rènhé jiéjìng kě zǒu. Yàoxiǎng zài xuéshù yánjiū zhōng yǒu suǒ jiànshù, bùjǐn xūyào mǐnruì de xuéshù yǎnguāng, gèng yīlài yú shí nián rú yí rì chíxù shēngēng de zhuānzhù yìlì. Wéiyǒu nàidézhu jìmò, chízhīyǐhéng gōngguān, cáinéng zài hòujī-bófā zhōng yínglái cuǐcàn tūpò.",
                "en": "The path of scholarship is winding with no shortcuts. Success demands academic insight and sustained dedication over decades. Enduring solitude and persevering brings breakthroughs through deep accumulated wisdom.",
                "es": "La senda del saber no admite atajos. Triunfar en la investigación exige sagacidad y un esfuerzo sostenido año tras año. Quien persevera con paciencia y rigor corona hallazgos fecundos."
            }
        ]
    },

    # 28 数
    {
        "id": "28",
        "hanzi": "数",
        "pinyin": "shù",
        "part_of_speech": "Numeral",
        "meanings_summary": {
            "en": "several; a few; number; figure",
            "es": "varios; unos cuantos; número; cifra"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Numeral",
                "register": "Standard",
                "definition_en": "several; a few (indicating an unspecified small quantity, usually greater than two)",
                "definition_es": "varios; unos cuantos (indica cantidad reducida indeterminada superior a dos)",
                "example_phrase": "数天 / 数年 (several days / several years)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这位老科学家在偏僻的大西北戈壁滩默默坚守数十载，为国家核工业发展奉献了青春。",
                "pinyin": "Zhè wèi lǎo kēxuéjiā zài piānpì de dàxīběi Gēbìtān mòmò jiānshǒu shùshí zǎi, wèi guójiā hégōngyè fāzhǎn fèngxiàn le qīngchūn.",
                "en": "This veteran scientist quietly persevered for several decades on the remote Gobi desert, dedicating his youth to the nation's nuclear industry.",
                "es": "Este veterano científico perseveró silencioso durante varias décadas en el remoto desierto de Gobi, consagrando su juventud a la energía nuclear patricia."
            },
            {
                "id": "#2",
                "hanzi": "长途跋涉了数天之后，科考队终于穿过茫茫原始密林，抵达了神秘的高原冰川源头。",
                "pinyin": "Chángtú báshè le shù tiān zhīhòu, kěkǎoduì zhōngyú chuānguò mángmáng yuánshǐ mìlín, dǐdá le shénmì de gāoyuán bīngchuān yuántóu.",
                "en": "After trekking for several days, the scientific expedition finally traversed dense virgin forests, arriving at the mysterious glacier source.",
                "es": "Tras varios días de penosa marcha, la expedición cruzó la espesura virgen arribando al misterioso nacimiento del glaciar de alta meseta."
            }
        ],
        "collocations": [
            {"hanzi": "数天", "en": "several days"},
            {"hanzi": "数年", "en": "several years"},
            {"hanzi": "数十个", "en": "several dozen"},
            {"hanzi": "数以万计", "en": "tens of thousands; numbered in tens of thousands"},
            {"hanzi": "数月", "en": "several months"},
            {"hanzi": "数倍", "en": "several times / several-fold"}
        ],
        "idioms": [
            {"hanzi": "数以万计", "pinyin": "shù yǐ wàn jì", "meaning_en": "numbered in the tens of thousands; myriad"},
            {"hanzi": "寥寥无几", "pinyin": "liáo liáo wú jǐ", "meaning_en": "very few; sparse and countable on fingers"},
            {"hanzi": "不可胜数", "pinyin": "bù kě shèng shǔ", "meaning_en": "too numerous to count; countless"},
            {"hanzi": "屈指可数", "pinyin": "qū zhǐ kě shǔ", "meaning_en": "can be counted on the fingers; very few in number"}
        ],
        "character_decomposition": [
            {
                "character": "数",
                "pinyin": "shù",
                "meaning_en": "number; several; count; fate",
                "meaning_es": "número; varios; contar; destino",
                "radical": "攵",
                "radical_meaning_en": "tap / action",
                "meaning_component": "娄 (woman with hair tied / tallying grain) + 攵 (tapping rod counting)",
                "sound_component": "娄 (lóu / phonetic origin)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A woman 娄 holding a counting rod 攵 tapping and reckoning grain tallies; signifies counting (shǔ) or mathematical quantity and indefinite numbers (shù).",
                "visual_mnemonic_story_en": "A hand taps a counting rod (攵) across organized sacks of grain (娄) to reckon several numbers (数).",
                "visual_mnemonic_story_es": "Una mano maneja la vara de conteo (攵) sobre sacos de grano (娄) para contar varios números (数).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FDOK",
                "traditional": "數"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Tapping a rod (攵) across grain tallies (娄) reckons several quantities (shù, 数).",
            "composite_memory_hook_es": "Contar grano con una vara (攵) sobre montones (娄) suma varios días o números (shù, 数).",
            "cultural_and_cognitive_roots": "Polyphonic root: verbal shǔ (action of counting: 数数), nominal shù (number: 数字), and indefinite numeral shù (several/a few: 数天, 数载).",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone when functioning as numeral or noun: 'shù' (51). Drop sharply from pitch 5 to 1."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "楼", "pinyin": "lóu", "meaning_en": "building; floor", "distinction_note": "Has wood radical 木 on left instead of 娄 and 攵"},
                {"character": "搂", "pinyin": "lǒu", "meaning_en": "hug; embrace", "distinction_note": "Has hand radical 扌 on left of 娄"},
                {"character": "救", "pinyin": "jiù", "meaning_en": "rescue; save", "distinction_note": "Has 求 on left of 攵 instead of 娄 in 数"},
                {"character": "敏", "pinyin": "mǐn", "meaning_en": "agile; sensitive", "distinction_note": "Has 每 on left of 攵"}
            ],
            "etymological_cognates": [
                {"character": "几", "pinyin": "jǐ", "gloss_en": "how many; a few"},
                {"character": "各", "pinyin": "gè", "gloss_en": "each; various"},
                {"character": "量", "pinyin": "liàng", "gloss_en": "measure; quantity"},
                {"character": "度", "pinyin": "dù", "gloss_en": "degree; rule measure"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "数 (shù) is a literary and formal indefinite numeral prefix meaning 'several / a few' (数天, 数载).",
            "contrasts": [
                {"id": "1", "compared_word": "数 vs. 几", "pinyin": "jǐ", "analysis": "几 is the standard colloquial spoken word for 'a few / several' ('几天', '几个人'), while 数 is literary, written, and dignified ('数日', '数载')."},
                {"id": "2", "compared_word": "数 vs. 许多", "pinyin": "xǔduō", "analysis": "许多 indicates an abundant large quantity ('many / a lot of'), while 数 indicates an indefinite modest quantity ('several')."},
                {"id": "3", "compared_word": "数 vs. 若干", "pinyin": "ruògān", "analysis": "若干 is an official bureaucratic administrative pronoun meaning 'a certain number of' ('若干规定'), while 数 directly quantifies time and items."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫长数载的光阴弹指一挥间，当年偏僻荒凉的南海小渔村，在改革开放的浩荡春风中化作了高楼林立、充满创新活力的现代化国际大都市。数以万计怀揣梦想的奋斗者汇聚于此，谱写出震撼人心的时代奇迹。",
                "pinyin": "Màncháng shù zǎi de guāngyīn tánzhǐ-yīhuī jiān, dāngnián piānpì huāngliáng de Nánhǎi xiǎoyúcūn, zài gǎigé-kāifàng de hàodàng chūnfēng zhōng huàzuò le gāolóu-línlì, chōngmǎn chuàngxīn huólì de xiàndàihuà guójì dàdūshì. Shùyǐwànjì huáichuāi mèngxiǎng de fèndǒuzhě huìjù yúcǐ, pǔxiě chū zhènhàn-rénxīn de shídài qíjì.",
                "en": "In several years, a once-barren fishing hamlet transformed into a towering modern metropolis under reform winds. Tens of thousands of dreamers gathered here, composing a moving miracle of the era.",
                "es": "En unos cuantos decenios, una modesta aldea pesquera se convirtió en una deslumbrante metrópoli cosmopolita. Decenas de miles de soñadores forjaron aquí un milagro contemporáneo sin parangón."
            },
            {
                "id": "#2",
                "hanzi": "面对突如其来的全球供应链断裂危机，企业研发团队在数月时间内夜以继日连续攻关。他们试验了数百种替代原材料与数十套算法架构，终于彻底突破卡脖子技术瓶颈，确保了关键设备生产线的平稳运转。",
                "pinyin": "Miànduì tūrúqílái de quánqiú gōngyìngliàn duànliè wēijī, qǐyè yánfā tuánduì zài shù yuè shíjiān nèi yèyǐjìrì liánxù gōngjiān. Tāmen shìyàn le shùbǎi zhǒng tìdài yuáncáiliào yǔ shùshí tào suànfǎ jiàgòu, zhōngyú chèdǐ tūpò qiǎbózi jìshù píngjǐng, quèbǎo le guānjiàn shèbèi shēngchǎnxiàn de píngwěn yùnzhuǎn.",
                "en": "Facing global supply chain disruptions, the R&D team worked day and night over several months. Testing hundreds of materials and dozens of algorithms, they broke technological bottlenecks to secure production.",
                "es": "Ante la rotura de suministros mundiales, ingenieros investigaron día y noche durante varios meses. Ensayando cientos de materiales y decenas de algoritmos, vencieron el cuello de botella garantizando la producción."
            }
        ]
    },

    # 29 导致
    {
        "id": "29",
        "hanzi": "导致",
        "pinyin": "dǎo zhì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to lead to; to cause; to bring about; to result in",
            "es": "conducir a; provocar; causar; desembocar en; originar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to cause, bring about, or result in (almost exclusively introducing negative, undesirable, or adverse outcomes)",
                "definition_es": "provocar, acarrear o desembocar en (casi siempre introduciendo consecuencias adversas o desfavorables)",
                "example_phrase": "导致严重后果 (lead to serious consequences)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "由于施工人员严重违反安全操作规程，最终导致了这起性质恶劣的特大火灾事故。",
                "pinyin": "Yóuyú shīgōng rényuán yánzhòng wéifǎn ānquán cāozuò guīchéng, zuìzhōng dǎozhì le zhè qǐ xìngzhì èliè de tàdà huǒzāi shìgù.",
                "en": "Because construction workers seriously violated safety regulations, it ultimately led to this egregious major fire disaster.",
                "es": "Por infringir gravemente los protocolos de seguridad los operarios, se produjo este terrible siniestro con consecuencias devastadoras."
            },
            {
                "id": "#2",
                "hanzi": "长期处于严重睡眠不足与高压紧绷状态，容易导致人体自主神经功能紊乱与记忆力衰退。",
                "pinyin": "Chángqī chǔyú yánzhòng shuìmián bùzú yǔ gāoyā jǐnbēng zhuàngtài, róngyì dǎozhì réntǐ zìzhǔ shénjīng gōngnéng wěnluàn yǔ jìyìlì shuāituì.",
                "en": "Prolonged severe sleep deprivation and high-stress tension easily lead to autonomic nervous system dysfunction and memory decline.",
                "es": "La falta crónica de descanso y el estrés continuo conducen al desajuste del sistema nervioso autónomo y al deterioro de la memoria."
            }
        ],
        "collocations": [
            {"hanzi": "导致失败", "en": "lead to failure"},
            {"hanzi": "导致严重后果", "en": "result in serious consequences"},
            {"hanzi": "导致事故", "en": "cause an accident"},
            {"hanzi": "直接导致", "en": "directly lead to"},
            {"hanzi": "可能导致", "en": "may lead to; potentially cause"},
            {"hanzi": "导致疾病", "en": "cause illness/disease"}
        ],
        "idioms": [
            {"hanzi": "自食其果", "pinyin": "zì shí qí guǒ", "meaning_en": "reap what one has sown; eat the bitter fruit of one's own making"},
            {"hanzi": "玩火自焚", "pinyin": "wán huǒ zì fén", "meaning_en": "play with fire and burn oneself; court disaster"},
            {"hanzi": "前因后果", "pinyin": "qián yīn hòu guǒ", "meaning_en": "antecedents and consequences; causes and effects"},
            {"hanzi": "因小失大", "pinyin": "yīn xiǎo shī dà", "meaning_en": "lose big because of petty greed; penny wise pound foolish"}
        ],
        "character_decomposition": [
            {
                "character": "导",
                "pinyin": "dǎo",
                "meaning_en": "lead; guide; conduct; direct",
                "meaning_es": "guiar; conducir; canalizar; dirigir",
                "radical": "寸",
                "radical_meaning_en": "inch / hand measure",
                "meaning_component": "巳 (offspring / river channel) + 寸 (hand guiding way)",
                "sound_component": "道 (dào, path / phonetic origin)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A hand 寸 pointing out the path 道; guiding movement along a channel, leading to a consequence.",
                "visual_mnemonic_story_en": "A hand (寸) points the channel ahead, leading (导) events toward their result.",
                "visual_mnemonic_story_es": "Una mano (寸) canaliza la ruta orientando (导) los hechos hacia su desenlace.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RDI",
                "traditional": "導"
            },
            {
                "character": "致",
                "pinyin": "zhì",
                "meaning_en": "send; deliver; arrive; cause; delicate",
                "meaning_es": "entregar; llegar; provocar; delicado; causar",
                "radical": "至",
                "radical_meaning_en": "arrive",
                "meaning_component": "至 (arrow hitting ground / arrival) + 攵 (gentle tapping hand)",
                "sound_component": "至 (zhì, arrive / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An arrow arriving at its final ground target 至 guided by a hand 攵; represents bringing about, sending, or arriving at a terminus.",
                "visual_mnemonic_story_en": "An arrow reaches its final mark (至) propelled by hand (攵), causing completion (致).",
                "visual_mnemonic_story_es": "Una flecha hace diana al llegar (至) impulsada por la mano (攵), consumando el efecto (致).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MGOIK",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Guiding a course (导) until it hits the final destination (致) leads to an adverse outcome (导致).",
            "composite_memory_hook_es": "Canalizar los hechos (导) hasta que dan en el blanco final (致) provoca o acarrea un resultado (导致).",
            "cultural_and_cognitive_roots": "Causal grammar constraint: 导 (channeling trajectory) + 致 (final arrival); in modern syntax, strictly polarizes toward adverse or undesirable results.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by falling fourth tone: 'dǎo zhì' (214-51). Dip down on 'dǎo', then strike down firmly on 'zhì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "寻", "pinyin": "xún", "meaning_en": "seek", "distinction_note": "Has 彐 on top of 寸 instead of 巳 in 导"},
                {"character": "异", "pinyin": "yì", "meaning_en": "different", "distinction_note": "Has 廾 underneath 巳"},
                {"character": "到", "pinyin": "dào", "meaning_en": "arrive", "distinction_note": "Has knife radical 刂 on right of 至 instead of 攵 in 致"},
                {"character": "敌", "pinyin": "dí", "meaning_en": "enemy", "distinction_note": "Has 舌 on left of 攵 instead of 至"}
            ],
            "etymological_cognates": [
                {"character": "引", "pinyin": "yǐn", "gloss_en": "draw bow; trigger"},
                {"character": "起", "pinyin": "qǐ", "gloss_en": "rise; originate"},
                {"character": "成", "pinyin": "chéng", "gloss_en": "become; result in"},
                {"character": "致", "pinyin": "zhì", "gloss_en": "reach terminal result"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "导致 strictly introduces negative, unwanted, or harmful consequences (diseases, accidents, failures, losses).",
            "contrasts": [
                {"id": "1", "compared_word": "导致 vs. 引起", "pinyin": "yǐnqǐ", "analysis": "引起 can introduce positive, neutral, or negative reactions ('引起关注', '引起共鸣'), while 导致 is almost exclusively negative ('导致破产')."},
                {"id": "2", "compared_word": "导致 vs. 造成", "pinyin": "zàochéng", "analysis": "造成 emphasizes creating a tangible adverse state or loss ('造成经济损失', '造成人员伤亡'), largely interchangeable with 导致."},
                {"id": "3", "compared_word": "导致 vs. 致使", "pinyin": "zhìshǐ", "analysis": "致使 is more literary and formal, common in legal verdicts and forensic police accident reports, while 导致 is standard in all prose."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "全球气候变暖引发的极端天气频发，直接导致了部分沿海低洼岛国面临被上升海平面淹没的严峻生存威胁。极端干旱与洪涝灾害更导致大面积粮食作物减产，进一步加剧了全球范围内的饥饿与地缘动荡危机。",
                "pinyin": "Quánqiú qìhòu biànnuǎn yǐnfā de jíduān tiānqì pínfā, zhíjiē dǎozhì le bùfen yánhǎi dīwā dǎoguó miànlín bèi shàngshēng hǎipíngmiàn yānmò de yánjùn shēngcún wēixié. Jíduān gānhàn yǔ hónglào zāihài gèng dǎozhì dàmiànjī liángshi zuòwù jiǎnchǎn, jìnyíbù jiājù le quánqiú fànwéi nèi de jī'è yǔ dìyuán dòngdàng wēijī.",
                "en": "Climate change triggers extreme weather, leading low-lying island states to face threats of rising seas. Droughts and floods also lead to major crop reductions, exacerbating hunger and geopolitical unrest.",
                "es": "El cambio climático provoca anomalías meteorológicas que conducen a la sumersión de atolones por el mar. Sequías y riadas acarrean la ruina de cosechas agravando el hambre y la inestabilidad internacional."
            },
            {
                "id": "#2",
                "hanzi": "盲目贪大求全、盲目举债扩张，是许多昔日辉煌的大型企业最终走向资金链断裂、轰然倒闭的核心主因。缺乏敬畏市场规律的盲目决策，必然导致资产负债率居高不下，最终在金融风暴来临时难逃破产厄运。",
                "pinyin": "Mángmù tāndà-qiúquán, mángmù jǔzhài kuòzhāng, shì xǔduō xīrì huīhuáng de dàxíng qǐyè zuìzhōng zǒuxiàng zījīnliàn duànliè, hōngrán dǎobì de héxīn zhǔyīn. Quēfá jìngwèi shìchǎng guīlǜ de mángmù juécè, bìrán dǎozhì zīchǎn-fùzhàilǜ jūgāobùxià, zuìzhōng zài jīnróng fēngbào láilín shí nántáo pòchǎn èyùn.",
                "en": "Reckless borrowing and overexpansion are key factors leading once-glorious firms into liquidity defaults and collapse. Disregarding market rules inevitably leads to sky-high debt ratios, courting bankruptcy during storms.",
                "es": "Endeudarse a ciegas para expandirse condujo a la quiebra a consorcios antes boyantes. Desoír las leyes del mercado acarrea un endeudamiento insostenible que naufraga en la bancarrota al estallar crisis financieras."
            }
        ]
    },

    # 30 失眠
    {
        "id": "30",
        "hanzi": "失眠",
        "pinyin": "shī mián",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to suffer from insomnia; sleeplessness; insomnia",
            "es": "padecer insomnio; no poder dormir; insomnio"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to be unable to fall asleep or remain asleep throughout the night; to suffer insomnia",
                "definition_es": "ser incapaz de conciliar o mantener el sueño durante la noche; desvelarse",
                "example_phrase": "彻夜失眠 (suffer sleeplessness all night long)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "明天就要迎来期待已久的博士论文答辩，他躺在床上辗转反侧，竟然失眠了整整大半夜。",
                "pinyin": "Míngtiān jiùyào yínglái qīdài yǐ jiǔ de bóshì lùnwén dábiàn, tā tǎng zài chuáng shàng zhǎnzhuǎn-fǎncè, jìngrán shīmián le zhěngzhěng dàbànyè.",
                "en": "With tomorrow's long-awaited doctoral defense approaching, he tossed and turned in bed, suffering insomnia for half the night.",
                "es": "Ante la inminente defensa de su tesis doctoral, dio vueltas en la cama desvelado durante más de media noche."
            },
            {
                "id": "#2",
                "hanzi": "长期慢性失眠不仅会加速容颜衰老，更会导致人体免疫细胞活性大幅下降，诱发多种慢性疾病。",
                "pinyin": "Chángqī mànxìng shīmián bùjǐn huì jiāsù róngyán shuāilǎo, gèng huì dǎozhì réntǐ miǎnyì xìbāo huóxìng dàfú xiàjiàng, yòufā duō zhǒng mànxìng jíbìng.",
                "en": "Chronic long-term insomnia not only accelerates skin aging, but also causes significant drops in immune cell activity, inducing chronic diseases.",
                "es": "El insomnio crónico no solo envejece el semblante, sino que deprime las defensas inmunitarias propiciando dolencias crónicas."
            }
        ],
        "collocations": [
            {"hanzi": "慢性失眠", "en": "chronic insomnia"},
            {"hanzi": "经常失眠", "en": "frequently suffer from insomnia"},
            {"hanzi": "严重失眠", "en": "severe insomnia"},
            {"hanzi": "彻夜失眠", "en": "sleepless all night"},
            {"hanzi": "引起失眠", "en": "cause insomnia"},
            {"hanzi": "治疗失眠", "en": "treat insomnia"}
        ],
        "idioms": [
            {"hanzi": "辗转反侧", "pinyin": "zhǎn zhuǎn fǎn cè", "meaning_en": "toss and turn restlessly in bed unable to sleep"},
            {"hanzi": "彻夜难眠", "pinyin": "chè yè nán mián", "meaning_en": "unable to fall asleep all night through"},
            {"hanzi": "夜不能寐", "pinyin": "yè bù néng mèi", "meaning_en": "unable to sleep at night due to worries"},
            {"hanzi": "高枕无忧", "pinyin": "gāo zhěn wú yōu", "meaning_en": "sleep soundly on a high pillow; free from all worries"}
        ],
        "character_decomposition": [
            {
                "character": "失",
                "pinyin": "shī",
                "meaning_en": "lose; miss; fail; mistake",
                "meaning_es": "perder; dejar escapar; fallar; error",
                "radical": "大",
                "radical_meaning_en": "big",
                "meaning_component": "手 (hand) + 一 (object slipping away from grasp)",
                "sound_component": "失 (shī)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A hand 手 dropping an object that slips through fingers 一; signifies losing, slipping away, or missing.",
                "visual_mnemonic_story_en": "A hand opens and an object slips away through the fingers, lost (失).",
                "visual_mnemonic_story_es": "Una mano se abre y un objeto resbala de entre los dedos perdiéndose (失).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "HQO",
                "traditional": ""
            },
            {
                "character": "眠",
                "pinyin": "mián",
                "meaning_en": "sleep; close eyes; dormant",
                "meaning_es": "dormir; cerrar ojos; letargo",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye closing shut) + 民 (blinded eye / sleep)",
                "sound_component": "民 (mín, people / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Eye radical 目 paired with 民 (eyes closed in blindness/slumber); closing one's eyelids in peaceful sleep or hibernation.",
                "visual_mnemonic_story_en": "Eyelids (目) close softly shut as a person falls peacefully into deep sleep (眠).",
                "visual_mnemonic_story_es": "Los párpados (目) se cierran mansos cuando el durmiente concilia el sueño (眠).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BURVP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Losing (失) the ability to close eyes in peaceful sleep (眠) results in insomnia (失眠).",
            "composite_memory_hook_es": "Perder (失) la facultad de cerrar los ojos al plácido sueño (眠) es el insomnio (失眠).",
            "cultural_and_cognitive_roots": "Traditional Chinese medicine (中医神志学: 阳不入阴 / yang failing to enter yin); sleep represents restoring vital spirit (安神定志).",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by rising second tone: 'shī mián' (55-35). Hold high pitch 55 on 'shī', then climb upward smoothly on 'mián'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "矢", "pinyin": "shǐ", "meaning_en": "arrow; vow", "distinction_note": "Top stroke does not cross the horizontal stroke, unlike 失"},
                {"character": "夫", "pinyin": "fū", "meaning_en": "man; husband", "distinction_note": "Has straight horizontal top stroke"},
                {"character": "眼", "pinyin": "yǎn", "meaning_en": "eye", "distinction_note": "Has 艮 on right of 目 instead of 民 in 眠"},
                {"character": "睛", "pinyin": "jīng", "meaning_en": "eyeball", "distinction_note": "Has 青 on right of 目"}
            ],
            "etymological_cognates": [
                {"character": "睡", "pinyin": "shuì", "gloss_en": "drooping eyes in sleep"},
                {"character": "寐", "pinyin": "mèi", "gloss_en": "sleep soundly under roof"},
                {"character": "醒", "pinyin": "xǐng", "gloss_en": "wake from slumber/wine"},
                {"character": "梦", "pinyin": "mèng", "gloss_en": "dream while asleep"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "失眠 specifically designates the clinical condition or sleepless experience of inability to sleep.",
            "contrasts": [
                {"id": "1", "compared_word": "失眠 vs. 熬夜", "pinyin": "áoyè", "analysis": "熬夜 is voluntary staying up late to study, party, or work overtime, while 失眠 is the involuntary, painful inability to fall asleep in bed."},
                {"id": "2", "compared_word": "失眠 vs. 睡不着", "pinyin": "shuìbùzháo", "analysis": "睡不着 is an everyday colloquial spoken phrase ('我今晚睡不着'), whereas 失眠 is a formal medical noun and verb."},
                {"id": "3", "compared_word": "失眠 vs. 困倦", "pinyin": "kùnjuàn", "analysis": "困倦 describes feeling drowsy and weary with heavy eyelids, while 失眠 is inability to obtain sleep."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫漫长夜里，许多失眠者越是强迫自己尽快入睡，大脑皮层反而愈发兴奋清醒。心理医生建议，遇到辗转反侧失眠时，不必强赖在床上苦苦熬煎，不妨起身坐在柔和灯光下翻阅几页晦涩书卷，困意往往会在不经意间悄然降临。",
                "pinyin": "Mànmàn chángyè lǐ, xǔduō shīmiánzhě yuèshì qiǎngpò zìjǐ jǐnkuài rùshuì, dànǎo pícéng fǎn'ér yùfā xīngfèn qīngxǐng. Xīnlǐ yīshēng jiànyì, yùdào zhǎnzhuǎn-fǎncè shīmián shí, búbì qiáng lài zài chuáng shàng kǔkǔ áojiān, bùfáng qǐshēn zuò zài róuhé dēngguāng xià fānyuè jǐ yè huìsè shūjuǎn, kùnyì wǎngwǎng huì zài bùjīngyì jiān qiǎorán jiànglín.",
                "en": "In the dead of night, the more insomniacs force sleep, the more alert the brain becomes. Therapists suggest leaving bed to read under dim light rather than tossing restlessly; drowsiness soon arrives unbidden.",
                "es": "En la noche en vela, cuanto más se empeña el insomne en dormir, más se excita la corteza cerebral. Psiquiatras aconsejan levantarse a hojear un libro bajo luz tenue; el sueño vendrá por sí solo sin forzarlo."
            },
            {
                "id": "#2",
                "hanzi": "现代都市人失眠的主要诱因之一，是睡前长时间近距离刷短视频或打电子游戏。手机屏幕发射的强烈高频蓝光会抑制松果体分泌褪黑素，从而扰乱正常的昼夜生理节律，导致入睡困难与睡眠浅碎易醒。",
                "pinyin": "Xiàndài dūshìrén shīmián de zhǔyào yòuyīn zhīyī, shì shuìqián cháng shíjiān jìn jùlí shuā duǎnshìpín huò dǎ diànzǐ yóuxì. Shǒujī píngmù fāshè de qiángliè gāopín lánguāng huì yìzhì sōngguǒtǐ fēnmì tuìhēisù, cóng'ér rǎoluàn zhèngcháng de zhòuyè shēnglǐ jiélǜ, dǎozhì rùshuì kùnnán yǔ shuìmián qiǎnsuì yìxǐng.",
                "en": "A major trigger of modern urban insomnia is scrolling videos or gaming before bed. High-frequency blue light emitted by phone screens inhibits pineal melatonin, disrupting circadian rhythms and causing light, fragmented sleep.",
                "es": "Un detonante del insomnio actual es mirar pantallas antes de acostarse. La luz azulada de los móviles inhibe la melatonina en la glándula pineal, quebrando el ritmo circadiano y provocando un descanso superficial y entrecortado."
            }
        ]
    }
]

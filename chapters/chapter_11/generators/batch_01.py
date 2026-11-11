# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 闹钟
    {
        "id": "1",
        "hanzi": "闹钟",
        "pinyin": "nào zhōng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "alarm clock; alarm",
            "es": "despertador; reloj despertador"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a clock equipped with an acoustic mechanism to awaken sleeper or alert at a preset hour",
                "definition_es": "reloj provisto de mecanismo sonoro para despertar al durmiente o avisar a una hora fijada",
                "example_phrase": "调好闹钟 (set the alarm clock)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了赶上清晨首班高铁，他在睡觉前特意把手机闹钟设置在清晨五点整。",
                "pinyin": "Wèile gǎnshàng qīngchén shǒubān gāotiě, tā zài shuìjiào qián tèyì bǎ shǒujī nàozhōng shèzhì zài qīngchén wǔ diǎn zhěng.",
                "en": "In order to catch the morning's first high-speed train, he deliberately set his phone alarm clock to five o'clock sharp before sleeping.",
                "es": "Para no perder el primer tren de alta velocidad de la mañana, programó el despertador del móvil a las cinco en punto antes de acostarse."
            },
            {
                "id": "#2",
                "hanzi": "医学研究表明，长期被刺耳的机械闹钟突然惊醒容易引起心跳加速与情绪焦虑。",
                "pinyin": "Yīxué yánjiū biǎomíng, chángqī bèi cì'ěr de jīxiè nàozhōng tūrán jīngxǐng róngyì yǐnqǐ xīntiào jiāsù yǔ qíngxù jiāolǜ.",
                "en": "Medical research indicates that being startled awake for long periods by piercing mechanical alarms easily triggers rapid heartbeat and anxiety.",
                "es": "Estudios médicos señalan que ser despertado bruscamente por alarmas estridentes provoca taquicardia y desasosiego emocional prolongado."
            }
        ],
        "collocations": [
            {"hanzi": "定闹钟", "en": "set an alarm clock"},
            {"hanzi": "闹钟响了", "en": "alarm clock rings"},
            {"hanzi": "机械闹钟", "en": "mechanical alarm clock"},
            {"hanzi": "电子闹钟", "en": "electronic/digital alarm clock"},
            {"hanzi": "关掉闹钟", "en": "turn off / silence alarm"},
            {"hanzi": "静音闹钟", "en": "silent / vibration alarm"}
        ],
        "idioms": [
            {"hanzi": "晨钟暮鼓", "pinyin": "chén zhōng mù gǔ", "meaning_en": "morning bell and evening drum; timely reminders of time's passing"},
            {"hanzi": "警钟长鸣", "pinyin": "jǐng zhōng cháng míng", "meaning_en": "alarm bell ringing continuously; remain vigilant"},
            {"hanzi": "鸡鸣戒旦", "pinyin": "jī míng jiè dàn", "meaning_en": "rooster crowing at dawn; diligent early rising"},
            {"hanzi": "闻鸡起舞", "pinyin": "wén jī qǐ wǔ", "meaning_en": "rise upon hearing rooster crow to practice swords; hardworking vigor"}
        ],
        "character_decomposition": [
            {
                "character": "闹",
                "pinyin": "nào",
                "meaning_en": "noisy; make noise; stir up; suffer from",
                "meaning_es": "ruidoso; alborotar; bullir; padecer",
                "radical": "门",
                "radical_meaning_en": "door / gate",
                "meaning_component": "门 (city marketplace gates) + 市 (bustling market)",
                "sound_component": "闹 (nào)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Market crowds 市 shouting inside market gates 门; represents loud clamor, racket, and bustling commotion.",
                "visual_mnemonic_story_en": "A bustling market (市) clamors noisily inside open city gates (门), making a lively commotion (闹).",
                "visual_mnemonic_story_es": "El mercado bullicioso (市) vocifera tras las puertas (门) armando un alboroto sonoro (闹).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LSYB",
                "traditional": "鬧"
            },
            {
                "character": "钟",
                "pinyin": "zhōng",
                "meaning_en": "clock; bell; cup; time unit",
                "meaning_es": "reloj; campana; copa; minuto",
                "radical": "钅",
                "radical_meaning_en": "metal / gold",
                "meaning_component": "钅 (cast bronze metal) + 中 (straight upright spindle)",
                "sound_component": "重 (chóng/zhòng / phonetic origin)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Metal radical 钅 paired with a hanging vessel; originally an ancient musical bronze bell, later timepiece clocks.",
                "visual_mnemonic_story_en": "A bronze bell cast of metal (钅) rings at centered intervals (中) to mark the hour (钟).",
                "visual_mnemonic_story_es": "Una campana forjada en metal (钅) tañe con compás equilibrado (中) midiendo la hora (钟).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "CLP",
                "traditional": "鐘"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A metallic bell (钟) that makes a loud, clamorous noise (闹) to awaken you is an alarm clock (闹钟).",
            "composite_memory_hook_es": "Una campana metálica (钟) que arma ruido estridente (闹) para despertarte es el despertador (闹钟).",
            "cultural_and_cognitive_roots": "Traditional Chinese temple bell and drum towers (钟鼓楼) announced dawn and curfew; Western mechanical clocks replaced them in the late Qing.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by level high tone: 'nào zhōng' (51-55). Strike down on 'nào', then sustain a clear high ring on 'zhōng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "闲", "pinyin": "xián", "meaning_en": "idle; leisure", "distinction_note": "Has wood 木 inside 门 instead of 市 in 闹"},
                {"character": "阔", "pinyin": "kuò", "meaning_en": "broad; vast", "distinction_note": "Has 活 inside 门"},
                {"character": "针", "pinyin": "zhēn", "meaning_en": "needle; pin", "distinction_note": "Has 十 on right of 钅 instead of 中 in 钟"},
                {"character": "钢", "pinyin": "gāng", "meaning_en": "steel", "distinction_note": "Has 冈 on right of 钅"}
            ],
            "etymological_cognates": [
                {"character": "表", "pinyin": "biǎo", "gloss_en": "watch; external surface"},
                {"character": "铃", "pinyin": "líng", "gloss_en": "little bell; tinkling chime"},
                {"character": "钲", "pinyin": "zhēng", "gloss_en": "ancient metallic gong"},
                {"character": "铎", "pinyin": "duó", "gloss_en": "large ancient handbell"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "闹钟 specifically denotes a timepiece designed to ring aloud at a pre-set alert time, distinguished from passive wall clocks.",
            "contrasts": [
                {"id": "1", "compared_word": "闹钟 vs. 时钟", "pinyin": "shízhōng", "analysis": "时钟 refers generically to any large clock or clock tower, while 闹钟 specifically features an audible alarm mechanism."},
                {"id": "2", "compared_word": "闹钟 vs. 手表", "pinyin": "shǒubiǎo", "analysis": "手表 designates a personal wrist watch worn on the wrist, whereas 闹钟 typically rests on a bedside nightstand or phone app."},
                {"id": "3", "compared_word": "闹钟 vs. 门铃", "pinyin": "ménlíng", "analysis": "门铃 is an entrance doorbell triggered by arriving visitors, not a wake-up scheduling alarm."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "很多上班族为了防止早晨赖床迟到，往往习惯在床头设置多个间隔五分钟的响亮闹钟。然而生理学家指出，反复被吵醒又迷糊入睡会打乱大脑正常的睡眠节律，反而让人整天昏昏沉沉、精力不济。",
                "pinyin": "Hěnduō shàngbānzú wèile fángzhǐ zǎochen làichuáng chídào, wǎngwǎng xíguàn zài chuángtóu shèzhì duō ge jiàngé wǔ fēnzhōng de xiǎngliàng nàozhōng. Rán'ér shēnglǐxuéjiā zhǐchū, fǎnfù bèi chǎoxǐng yòu míhu rùshuì huì dǎluàn dànǎo zhèngcháng de shuìmián jiélǜ, fǎn'ér ràng rén zhěng tiān hūnhūn-chénchén, jīnglì bújì.",
                "en": "Many office workers set multiple alarms five minutes apart to prevent oversleeping. Yet physiologists warn that repeatedly being jolted awake disrupts brain sleep cycles, causing lethargy all day long.",
                "es": "Muchos empleados programan varias alarmas cada cinco minutos para no dormirse. Empero, fisiólogos advierten que despertar y adormilarse en bucle rompe el ciclo circadiano, causando sopor y fatiga todo el día."
            },
            {
                "id": "#2",
                "hanzi": "与刺耳突兀的传统机械铃声相比，新型智能光照闹钟能够模拟清晨自然日出的柔和光线。它在设定起床时间前半小时缓慢渐亮，温和地唤醒人体内部沉睡的生物钟，有效避免心血管系统骤然承受惊吓与血压波动。",
                "pinyin": "Yǔ cì'ěr tūwù de chuántǒng jīxiè língshēng xiāngbǐ, xīnxíng zhìnéng guāngzhào nàozhōng nénggòu mónǐ qīngchén zìrán rìchū de róuhé guāngxiàn. Tā zài shèdìng qǐchuáng shíjiān qián bàn xiǎoshí huǎnmàn jiànliàng, wēnhé de huànxǐng réntǐ nèibù chénsù de shēngwùzhōng, yǒuxiào bìmiǎn xīnxuèguǎn xìtǒng zhòurán chéngshòu jīngxià yǔ xuèyā bōdòng.",
                "en": "Compared with jarring mechanical rings, new smart sunrise alarms simulate morning dawn. Gradually brightening 30 minutes before waking, they gently awaken the internal biological clock without cardiovascular shocks.",
                "es": "Frente al estridente zumbador tradicional, los despertadores solares simulan el alba. Iluminando la estancia media hora antes, activan suavemente el reloj biológico sin sacudidas cardiovasculares ni alzas de presión."
            }
        ]
    },

    # 02 危害
    {
        "id": "2",
        "hanzi": "危害",
        "pinyin": "wēi hài",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to harm; to jeopardize; to damage; harm; peril",
            "es": "dañar; perjudicar; atentar contra; peligro; daño"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to cause severe injury, damage, jeopardy, or impairment to health, safety, or society",
                "definition_es": "causar daño grave, perjuicio o menoscabo a la salud, seguridad o bienestar social",
                "example_phrase": "危害身体健康 (harm bodily health)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "harm, danger, detriment, or hazardous damage",
                "definition_es": "perjuicio, daño, peligro o estrago",
                "example_phrase": "认识吸烟的危害 (recognize harms of smoking)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "长期吸烟与吸二手烟会对人体肺部和心脑血管系统造成极大的不可逆危害。",
                "pinyin": "Chángqī xīyān yǔ xī èrshǒuyān huì duì réntǐ fèibù hé xīn-nǎoxiěguǎn xìtǒng zàochéng jí dà de bùkěnì wēihài.",
                "en": "Long-term smoking and second-hand smoke cause immense and irreversible harm to lungs and cardiovascular systems.",
                "es": "Fumar de forma prolongada e inhalar humo ajeno causa daños de enorme gravedad e irreversibles a los pulmones y vasos sanguíneos."
            },
            {
                "id": "#2",
                "hanzi": "任何危害国家主权、安全与公共利益的违法犯罪行为，都必将受到法律的严惩。",
                "pinyin": "Rènhé wēihài guójiā zhǔquán, ānquán yǔ gōnggòng lìyì de wéifǎ fànzuì xíngwéi, dōu bìjiāng shòudào fǎlǜ de yánchéng.",
                "en": "Any illegal criminal conduct that jeopardizes national sovereignty, security, or public interests will be punished severely by law.",
                "es": "Toda conducta delictiva que atente contra la soberanía, la seguridad y el bien público será castigada con el rigor de la ley."
            }
        ],
        "collocations": [
            {"hanzi": "严重危害", "en": "serious harm / severely jeopardize"},
            {"hanzi": "危害健康", "en": "harm health"},
            {"hanzi": "危害安全", "en": "jeopardize safety/security"},
            {"hanzi": "环境危害", "en": "environmental hazard/harm"},
            {"hanzi": "造成危害", "en": "cause harm / inflict damage"},
            {"hanzi": "危害社会", "en": "harm society"}
        ],
        "idioms": [
            {"hanzi": "后患无穷", "pinyin": "hòu huàn wú qióng", "meaning_en": "no end of future troubles; endless disastrous aftermath"},
            {"hanzi": "贻害无穷", "pinyin": "yí hài wú qióng", "meaning_en": "leave boundless harm for future generations"},
            {"hanzi": "防患未然", "pinyin": "fáng huàn wèi rán", "meaning_en": "prevent troubles before they happen; take precautions"},
            {"hanzi": "除暴安良", "pinyin": "chú bào ān liáng", "meaning_en": "eliminate the violent and protect the peaceful"}
        ],
        "character_decomposition": [
            {
                "character": "危",
                "pinyin": "wēi",
                "meaning_en": "danger; perilous; precarious; high",
                "meaning_es": "peligro; arriesgado; precario; alto",
                "radical": "厄",
                "radical_meaning_en": "distress / cliff",
                "meaning_component": "𠂆 (precipitous cliff) + 卩 (kneeling person on edge)",
                "sound_component": "危 (wēi)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A person 卩 kneeling trembling atop a high, dizzying cliff 𠂆; signifies peril, danger, and precariousness.",
                "visual_mnemonic_story_en": "A figure crouches cautiously on the edge of a sheer cliff (𠂆), facing extreme danger (危).",
                "visual_mnemonic_story_es": "Una figura se agacha aterrada al borde de un risco escarpado (𠂆) ante el abismo peligroso (危).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "NMSU",
                "traditional": ""
            },
            {
                "character": "害",
                "pinyin": "hài",
                "meaning_en": "harm; damage; injure; evil",
                "meaning_es": "dañar; perjudicar; matar; mal",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (house roof) + 丰 (thorn weapon) + 口 (malevolent words)",
                "sound_component": "害 (hài)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Spiteful words 口 and sharp thorns entering a home 宀 to hurt inhabitants; signifies injury and damage.",
                "visual_mnemonic_story_en": "Harmful weapons and words pierce into a peaceful house (宀), causing painful injury (害).",
                "visual_mnemonic_story_es": "Espinas punzantes y rencores entran bajo el techo del hogar (宀) infligiendo daño (害).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "JQMR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Perched on a perilous cliff (危) while suffering painful damage (害) captures severe jeopardy (危害).",
            "composite_memory_hook_es": "Al borde del abismo peligroso (危) sufriendo un daño lesivo (害) se configura el perjuicio grave (危害).",
            "cultural_and_cognitive_roots": "Classical moral pairing: 危 (instability/hazard) compounded with 害 (malevolent harm/destruction); frequently used in legal statutes.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'wēi hài' (55-51). Hold high pitch 55 on 'wēi', then descend sharply and heavily on 'hài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "免", "pinyin": "miǎn", "meaning_en": "exempt; avoid", "distinction_note": "Lacks the upper cliff lid 𠂆 of 危"},
                {"character": "角", "pinyin": "jiǎo", "meaning_en": "horn; corner", "distinction_note": "Has central vertical stroke penetrating down"},
                {"character": "割", "pinyin": "gē", "meaning_en": "cut; sever", "distinction_note": "Has knife radical 刂 on right of 害"},
                {"character": "豁", "pinyin": "huò", "meaning_en": "open; exempt", "distinction_note": "Has 谷 on right of 害"}
            ],
            "etymological_cognates": [
                {"character": "损", "pinyin": "sǔn", "gloss_en": "damage; decrease loss"},
                {"character": "伤", "pinyin": "shāng", "gloss_en": "wound; injure flesh"},
                {"character": "祸", "pinyin": "huò", "gloss_en": "calamity; disaster"},
                {"character": "殃", "pinyin": "yāng", "gloss_en": "misfortune; disaster"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "危害 highlights active, systemic jeopardy or severe societal/physiological harm.",
            "contrasts": [
                {"id": "1", "compared_word": "危害 vs. 损害", "pinyin": "sǔnhài", "analysis": "损害 emphasizes concrete financial loss or physical damage to interests and rights ('损害名誉', '损害利益'), while 危害 emphasizes perilous threats to safety and existence."},
                {"id": "2", "compared_word": "危害 vs. 破坏", "pinyin": "pòhuài", "analysis": "破坏 emphasizes physical smashing or disrupting orders and treaties ('破坏公物', '破坏协议'), while 危害 can be invisible and chronic."},
                {"id": "3", "compared_word": "危害 vs. 伤害", "pinyin": "shānghài", "analysis": "伤害 focuses primarily on biological injury to living bodies or wounded emotions ('伤害感情'), while 危害 applies broadly to public security, health, and ecosystems."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着现代工业文明飞速发展，未经妥善处理的塑料微粒和有毒工业废水正严重危害着海洋生态系统。有毒重金属在海洋鱼类体内持续富集，最终通过食物链回流至人类餐桌，对人体健康构成了潜在的长期危害。",
                "pinyin": "Suízhe xiàndài gōngyè wénmíng fēisù fāzhǎn, wèijīng tuǒshàn chǔlǐ de sùliào wēilì hé yǒudú gōngyè fèishuǐ zhèng yánzhòng wēihài zhe hǎiyáng shēngtài xìtǒng. Yǒudú zhòngjīnshǔ zài hǎiyáng yúlèi tǐnèi chíxù fùjí, zuìzhōng tōngguò shíwùliàn huíliú zhì rénlèi cānzhuō, duì réntǐ jiànkāng gòuchéng le qiánzài de chángqī wēihài.",
                "en": "With rapid industrialization, untreated microplastics and chemical effluents severely jeopardize marine ecosystems. Toxic heavy metals accumulate up food chains to dinner tables, posing long-term hazards to human health.",
                "es": "Con el auge industrial, microplásticos y aguas residuales tóxicas dañan gravemente la ecología marina. Metales pesados se bioacumulan en la fauna llegando a la mesa y amenazando la salud humana a largo plazo."
            },
            {
                "id": "#2",
                "hanzi": "在数字化信息时代，网络谣言与虚假信息的广泛传播对正常社会秩序造成了不可忽视的重大危害。不法分子利用公众的焦虑情绪恶意炮制耸人听闻的谎言，挑拨社会矛盾，执法机关必须依法坚决打击、严厉惩治。",
                "pinyin": "Zài shùzìhuà xìnxī shídài, wǎngluò yáoyán yǔ xūjiǎ xìnxī de guǎngfàn chuánbō duì zhèngcháng shèhuì zhìxù zàochéng le bùkě hūshì de zhòngdà wēihài. Bùfǎ fènzǐ lìyòng gōngzhòng de jiāolǜ qíngxù èyì páozhì sǒngrén-tīngwén de huǎngyán, tiǎobō shèhuì máodùn, zhífǎ jīguān bìxū yīfǎ jiānjué dǎjī, yánlì chéngzhì.",
                "en": "In the digital era, proliferation of online rumors inflicts unignorable harm on social order. Criminals exploit anxiety to fabricate sensational lies and sow discord, demanding resolute crackdowns by law enforcement.",
                "es": "En la era digital, la proliferación de bulos causa estragos innegables en la paz social. Maleantes explotan la zozobra pública urdiendo patrañas para sembrar discordia, exigiendo una respuesta implacable de la justicia."
            }
        ]
    },

    # 03 人类
    {
        "id": "3",
        "hanzi": "人类",
        "pinyin": "rén lèi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "humankind; humanity; mankind; human race",
            "es": "humanidad; género humano; especie humana; seres humanos"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the human race or species collectively, distinct from animals and divine beings",
                "definition_es": "el conjunto de seres humanos o la especie Homo sapiens en su totalidad",
                "example_phrase": "人类文明 (human civilization)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "探索未知浩瀚宇宙、寻找地外宜居星球，是整个人类自古以来共同怀揣的浪漫梦想。",
                "pinyin": "Tànsuǒ wèizhī hàohàn yǔzhòu, xúnzhǎo dìwài yíjū xīngqiú, shì zhěng gè rénlèi zìgǔ yǐlái gòngtóng huáichuāi de làngmàn mèngxiǎng.",
                "en": "Exploring the vast unknown cosmos and searching for habitable exoplanets is a romantic dream shared by all humanity since ancient times.",
                "es": "Explorar el cosmos ignoto y buscar planetas habitables es un sueño poético que comparte la humanidad entera desde tiempos remotos."
            },
            {
                "id": "#2",
                "hanzi": "文字的发明与普及是人类进化史上的一座丰碑，它让人类的智慧与思想得以世代相传。",
                "pinyin": "Wénzì de fāmíng yǔ pǔjí shì rénlèi jìnhuà shǐ shàng de yí zuò fēngbēi, tā ràng rénlèi de zhìhuì yǔ sīxiǎng déyǐ shìdài xiāngchuán.",
                "en": "The invention and spread of writing marks a milestone in human evolution, enabling human wisdom and ideas to be passed across generations.",
                "es": "La invención y difusión de la escritura marca un hito en la evolución humana, permitiendo transmitir la sabiduría de generación en generación."
            }
        ],
        "collocations": [
            {"hanzi": "人类社会", "en": "human society"},
            {"hanzi": "人类文明", "en": "human civilization"},
            {"hanzi": "全人类", "en": "all humankind; entire humanity"},
            {"hanzi": "人类历史", "en": "human history"},
            {"hanzi": "人类基因", "en": "human genome/genes"},
            {"hanzi": "人类命运共同体", "en": "community with a shared future for mankind"}
        ],
        "idioms": [
            {"hanzi": "生生不息", "pinyin": "shēng shēng bù xī", "meaning_en": "perpetuate endlessly; continuous reproduction and renewal"},
            {"hanzi": "源远流长", "pinyin": "yuán yuǎn liú cháng", "meaning_en": "have a long history and deep roots; date back to remote antiquity"},
            {"hanzi": "改天换地", "pinyin": "gǎi tiān huàn dì", "meaning_en": "transform heaven and earth; reshape the physical world"},
            {"hanzi": "薪火相传", "pinyin": "xīn huǒ xiāng chuán", "meaning_en": "pass the torch from generation to generation"}
        ],
        "character_decomposition": [
            {
                "character": "人",
                "pinyin": "rén",
                "meaning_en": "person; human; mankind",
                "meaning_es": "persona; ser humano; hombre",
                "radical": "人",
                "radical_meaning_en": "human",
                "meaning_component": "人 (side profile of walking bipedal human)",
                "sound_component": "人 (rén)",
                "stroke_count": 2,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph depicting a person standing upright on two feet with arms extended forward.",
                "visual_mnemonic_story_en": "Two sturdy legs stride forward upright, embodying the noble human being (人).",
                "visual_mnemonic_story_es": "Dos piernas firmes avanzan erguidas dibujando la silueta del ser humano (人).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "O",
                "traditional": ""
            },
            {
                "character": "类",
                "pinyin": "lèi",
                "meaning_en": "kind; type; category; class; species",
                "meaning_es": "clase; especie; categoría; tipo",
                "radical": "米",
                "radical_meaning_en": "rice",
                "meaning_component": "米 (grains of rice of same variety) + 犬 (hound sorting species)",
                "sound_component": "类 (lèi)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Sorting grains of harvested rice 米 by variety and breed; signifies category, species, and kinds.",
                "visual_mnemonic_story_en": "Grains of rice (米) sorted into distinct types (大) define a biological class or species (类).",
                "visual_mnemonic_story_es": "Granos de arroz (米) seleccionados por variedades (大) tipifican una clase o especie (类).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FDK",
                "traditional": "類"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The species (类) of upright thinking beings (人) makes up humankind (人类).",
            "composite_memory_hook_es": "La especie (类) que camina erguida pensando (人) conforma la humanidad (人类).",
            "cultural_and_cognitive_roots": "Universal collective biological noun: combines 人 (bipedal moral human) with 类 (taxonomic genus/kind), reflecting both natural history and humanism.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'rén lèi' (35-51). Rise smoothly on 'rén', then land firmly on 'lèi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "入", "pinyin": "rù", "meaning_en": "enter", "distinction_note": "Right stroke overlaps left stroke, opposite of 人"},
                {"character": "八", "pinyin": "bā", "meaning_en": "eight", "distinction_note": "Two strokes do not touch at the top"},
                {"character": "粪", "pinyin": "fèn", "meaning_en": "manure; dung", "distinction_note": "Has 共 underneath 米 instead of 大 in 类"},
                {"character": "迷", "pinyin": "mí", "meaning_en": "bewilder; lost", "distinction_note": "Has movement radical 辶 enclosing 米"}
            ],
            "etymological_cognates": [
                {"character": "群", "pinyin": "qún", "gloss_en": "crowd; flock of sheep"},
                {"character": "生", "pinyin": "shēng", "gloss_en": "life; birth of plant"},
                {"character": "属", "pinyin": "shǔ", "gloss_en": "belong to; taxonomic genus"},
                {"character": "民", "pinyin": "mín", "gloss_en": "people; populace"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "人类 refers to the entire human species on a macroscopic, evolutionary, or global civilizational scale.",
            "contrasts": [
                {"id": "1", "compared_word": "人类 vs. 人们", "pinyin": "rénmen", "analysis": "人们 refers casually to ordinary people or a crowd of individuals present ('人们议论纷纷'), while 人类 is the biological species or civilization as a whole."},
                {"id": "2", "compared_word": "人类 vs. 人口", "pinyin": "rénkǒu", "analysis": "人口 is a demographic statistical term counting numbers of inhabitants in a country or city, while 人类 is anthropological."},
                {"id": "3", "compared_word": "人类 vs. 人员", "pinyin": "rényuán", "analysis": "人员 denotes staff or personnel belonging to an organization ('医务人员'), completely distinct from species-wide 人类."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "从原始狩猎采集时代学会使用火与石器，到现代掌握人工智能与核能，人类在漫长的数万年漫漫岁月中创造了璀璨辉煌的物质与精神文明。然而伴随科技进步，如何与自然万物和谐相处，已成为全人类必须正视的课题。",
                "pinyin": "Cóng yuánshǐ shòuliè-cǎijí shídài xuéhuì shǐyòng huǒ yǔ shíqì, dào xiàndài zhǎngwò réngōng zhìnéng yǔ hénéng, rénlèi zài màncháng de shùwàn nián mànmàn suìyuè zhōng chuàngzào le cuǐcàn huīhuáng de wùzhì yǔ jīngshén wénmíng. Rán'ér bànsuí kējì jìnbù, rúhé yǔ zìrán wànwù héxié xiāngchǔ, yǐ chéngwéi quán rénlèi bìxū zhèngshì de kètí.",
                "en": "From mastering fire and flint tools to modern AI and nuclear energy, humankind created brilliant civilizations over millennia. Yet as science advances, living in harmony with nature is an imperative for all humanity.",
                "es": "Desde dominar el fuego y la piedra hasta la inteligencia artificial y la energía atómica, el ser humano forjó civilizaciones brillantes. Ahora, convivir en armonía con la biosfera es el gran dilema de la humanidad."
            },
            {
                "id": "#2",
                "hanzi": "面对气候恶化、生态失衡与跨国流行疾病等重大全球性危机，没有哪一个国家或民族能够独善其身。各国应当超越意识形态偏见与地缘政治争端，秉持人类命运共同体理念，携手筑牢守护地球家园的安全屏障。",
                "pinyin": "Miànduì qìhòu èhuà, shēngtài shīhéng yǔ kuàguó liúxíng jíbìng děng zhòngdà quánqiúxìng wēijī, méiyǒu nǎ yí ge guójiā huò mínzú nénggòu dúshàn-qíshēn. Gèguó yīngdāng chāoyuè yìshí-xíngtài piānjiàn yǔ dìyuán zhèngzhì zhēngduān, bǐngchí rénlèi mìngyùn gòngtóngtǐ lǐniàn, xiéshǒu zhùláo shǒuhù Dìqiú jiāyuán de ānquán píngzhàng.",
                "en": "Confronting climate crises and pandemics, no country can stand in isolation. Transcending ideological biases, nations must uphold a shared community for mankind, building barriers to protect our planet.",
                "es": "Ante la crisis climática y las pandemias globales, ningún país se salva en solitario. Superando rivalidades geopolíticas, las naciones deben cobijar un destino compartido para blindar el hogar terrenal común."
            }
        ]
    },

    # 04 机制
    {
        "id": "4",
        "hanzi": "机制",
        "pinyin": "jī zhì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "mechanism; internal workings; operating structure",
            "es": "mecanismo; engranaje interno; funcionamiento orgánico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the structural parts and interworking processes of a biological organism, machine, or social institution",
                "definition_es": "estructura, funcionamiento o conjunto de procesos coordinados de un organismo, máquina o sistema social",
                "example_phrase": "工作机制 / 防御机制 (working mechanism / defense mechanism)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "诺贝尔生理学或医学奖得主成功阐明了控制人体生物钟昼夜节律的分子运转机制。",
                "pinyin": "Nuòbèi'ěr shēnglǐxué huò yīxuéjiǎng dézhǔ chénggōng chǎnmíng le kòngzhì réntǐ shēngwùzhōng zhòuyè jiélǜ de fēnzǐ yùnzhuǎn jīzhì.",
                "en": "Nobel laureates in Physiology or Medicine successfully elucidated the molecular operating mechanism controlling the human circadian clock.",
                "es": "Los laureados con el Nobel de Medicina desentrañaron el mecanismo molecular que regula el ritmo circadiano del reloj biológico humano."
            },
            {
                "id": "#2",
                "hanzi": "为了有效遏制市场垄断行为，监管部门迅速建立起了跨部门联合执法的常态化工作机制。",
                "pinyin": "Wèile yǒuxiào èzhì shìchǎng lǒngduàn xíngwéi, jiānguǎn bùmén xùnsù jiànlì qǐ le kuà-bùmén liánhé zhífǎ de chángtàihuà gōngzuò jīzhì.",
                "en": "To curb market monopolistic behavior, regulators rapidly instituted a normalized inter-departmental joint enforcement mechanism.",
                "es": "Para frenar prácticas monopolísticas, las autoridades supervisoras establecieron un mecanismo interdepartamental permanente de inspección conjunta."
            }
        ],
        "collocations": [
            {"hanzi": "长效机制", "en": "long-term mechanism"},
            {"hanzi": "运行机制", "en": "operating/functioning mechanism"},
            {"hanzi": "激励机制", "en": "incentive mechanism"},
            {"hanzi": "防御机制", "en": "defense mechanism"},
            {"hanzi": "形成机制", "en": "formation mechanism"},
            {"hanzi": "调解机制", "en": "mediation mechanism"}
        ],
        "idioms": [
            {"hanzi": "环环相扣", "pinyin": "huán huán xiāng kòu", "meaning_en": "interlinked closely like rings of a chain; tightly linked"},
            {"hanzi": "相辅相成", "pinyin": "xiāng fǔ xiāng chéng", "meaning_en": "complement and reinforce each other"},
            {"hanzi": "自圆其说", "pinyin": "zì yuán qí shuō", "meaning_en": "make one's statement consistent and plausible"},
            {"hanzi": "因势利导", "pinyin": "yīn shì lì dǎo", "meaning_en": "guide action according to circumstances"}
        ],
        "character_decomposition": [
            {
                "character": "机",
                "pinyin": "jī",
                "meaning_en": "machine; mechanism; trigger; opportunity",
                "meaning_es": "máquina; mecanismo; disparador; ocasión",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden loom/crossbow mechanism) + 几 (small table / trigger)",
                "sound_component": "几 (jī, small table / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A wooden loom or the trigger mechanism 几 of a wooden crossbow 木; represents triggers and machinery.",
                "visual_mnemonic_story_en": "Wooden components (木) and sensitive triggers (几) spring into coordinated machine motion (机).",
                "visual_mnemonic_story_es": "Piezas de madera (木) y un gatillo sensible (几) se ensamblan en un mecanismo coordinado (机).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DHN",
                "traditional": "機"
            },
            {
                "character": "制",
                "pinyin": "zhì",
                "meaning_en": "system; make; formulate; control; restrict",
                "meaning_es": "sistema; elaborar; formular; controlar",
                "radical": "刂",
                "radical_meaning_en": "knife",
                "meaning_component": "刂 (knife cutting to pattern) + 未/制 (tree branches shaped)",
                "sound_component": "制 (zhì)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A knife 刂 pruning overgrown tree branches to follow regular form; signifies rules, systems, and manufacturing.",
                "visual_mnemonic_story_en": "A sharp knife (刂) trims wild branches into orderly, regulated shape (制).",
                "visual_mnemonic_story_es": "Un cuchillo afilado (刂) poda ramas desordenadas imponiendo un patrón regulado (制).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HBLN",
                "traditional": "製"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A machine trigger (机) functioning under regulated rules (制) constitutes a mechanism (机制).",
            "composite_memory_hook_es": "Un disparador mecánico (机) que actúa bajo una pauta regulada (制) integra un mecanismo (机制).",
            "cultural_and_cognitive_roots": "Scientific calque translating 'mechanism' (mechanics of machinery) into biological physiology (生理机制) and administrative governance.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'jī zhì' (55-51). Hold high pitch 55 on 'jī', then descend firmly on 'zhì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "饥", "pinyin": "jī", "meaning_en": "hungry; famine", "distinction_note": "Has food radical 饣 on left instead of wood 木 in 机"},
                {"character": "肌", "pinyin": "jī", "meaning_en": "muscle; flesh", "distinction_note": "Has flesh radical 月 on left"},
                {"character": "到", "pinyin": "dào", "meaning_en": "arrive; reach", "distinction_note": "Has 至 on left of 刂 instead of 制's left side"},
                {"character": "刷", "pinyin": "shuā", "meaning_en": "brush; swipe", "distinction_note": "Has 尸 on left of 刂"}
            ],
            "etymological_cognates": [
                {"character": "体", "pinyin": "tǐ", "gloss_en": "body; structural system"},
                {"character": "理", "pinyin": "lǐ", "gloss_en": "jade veins; principle"},
                {"character": "度", "pinyin": "dù", "gloss_en": "measure; degree; system"},
                {"character": "构", "pinyin": "gòu", "gloss_en": "construct; frame of timbers"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "机制 designates the dynamic internal processes and interrelationships causing an organism, engine, or policy to function.",
            "contrasts": [
                {"id": "1", "compared_word": "机制 vs. 体制", "pinyin": "tǐzhì", "analysis": "体制 refers to macroscopic static state structures and political/economic governance frameworks ('政治体制'), while 机制 refers to active operational processes."},
                {"id": "2", "compared_word": "机制 vs. 制度", "pinyin": "zhìdù", "analysis": "制度 refers to written statutory rules, codes of conduct, or laws ('规章制度'), while 机制 is how components interact in practice."},
                {"id": "3", "compared_word": "机制 vs. 器官", "pinyin": "qìguān", "analysis": "器官 is an anatomical bodily organ (heart, lungs), while 机制 is the physiological process coordinating those organs."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "人体免疫机制是一道精密神奇的生理防线。当外界病毒侵入机体时，免疫细胞会迅速启动识别机制，分工协作产生抗体将病原体围剿消灭，同时建立免疫记忆机制，为下一次抵御同类病菌打下坚实屏障。",
                "pinyin": "Réntǐ miǎnyì jīzhì shì yí dào jīngmì shénqí de shēnglǐ fángxiàn. Dāng wàijiè bìngdú qīnrù jītǐ shí, miǎnyì xìbāo huì xùnsù qǐdòng shíbié jīzhì, fēngōng-xiézuò chǎnshēng kàngtǐ jiāng bìngyuántǐ wéijiǎo xiāomiè, tóngshí jiànlì miǎnyì jìyì jīzhì, wèi xià yí cì dǐyù tónglèi bìngjūn dǎxià jiānshí píngzhàng.",
                "en": "The human immune mechanism is an intricate biological defense line. Upon viral invasion, immune cells trigger recognition mechanisms, cooperating to generate antibodies and establish memory.",
                "es": "El sistema inmunológico humano es un portentoso mecanismo de defensa. Ante virus invasores activa sensores celulares coordinando anticuerpos y fijando memorias que blindan futuras infecciones."
            },
            {
                "id": "#2",
                "hanzi": "推进现代高新技术成果转化，亟须打破科研院所与企业之间的壁垒，构建起产学研深度融合的利益共享机制。唯有完善科技成果评估体系与收益分配激励机制，才能充分调动科研人员创新创业的内生动力与澎湃活力。",
                "pinyin": "Tuījìn xiàndài gāoxīnjìshù chéngguǒ zhuǎnhuà, jíxū dǎpò kēyán yuànsuǒ yǔ qǐyè zhījiān de bìlěi, gòujiàn qǐ chǎn-xué-yán shēndù rónghé de lìyì gòngxiǎng jīzhì. Wéiyǒu wánshàn kējì chéngguǒ pínggū tǐxì yǔ shòuyì fēnpèi jīlì jīzhì, cáinéng chōngfèn diàodòng kēyán rényuán chuàngxīn-chuàngyè de nèishēng dònglì yǔ péngpài huólì.",
                "en": "Translating high-tech achievements demands breaking barriers between institutes and enterprises to build profit-sharing mechanisms. Reforming incentives stimulates researchers' innovation vitality.",
                "es": "Para transferir tecnología punta urge tender puentes entre academias y empresas creando mecanismos de beneficio mutuo. Recompensar el mérito investigador desata el dinamismo emprendedor."
            }
        ]
    },

    # 05 生物
    {
        "id": "5",
        "hanzi": "生物",
        "pinyin": "shēng wù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "living organism; living creature; biology",
            "es": "ser vivo; organismo vivo; criatura; biología"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "living beings having vitality, growth, metabolism, and reproduction (animals, plants, microbes)",
                "definition_es": "ser que posee vida, capaz de nutrirse, crecer y reproducirse (animales, plantas, microorganismos)",
                "example_phrase": "海洋生物 (marine organisms)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the academic subject or science of biology",
                "definition_es": "la asignatura académica o ciencia de la biología",
                "example_phrase": "生物课 (biology class)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "热带雨林是地球上生物多样性最为丰富的宝库，栖息着数百万种未被人类发现的奇异生物。",
                "pinyin": "Rèdài yǔlín shì Dìqiú shàng shēngwù duōyàngxìng zuìwéi fēngfù de bǎokù, qīxī zhe shùbǎiwàn zhǒng wèibèi rénlèi fāxiàn de qíyì shēngwù.",
                "en": "Tropical rainforests are Earth's richest treasure troves of biodiversity, harboring millions of exotic living species undiscovered by humans.",
                "es": "La selva tropical es el tesoro de mayor biodiversidad del planeta, albergando millones de singulares seres vivos aún ignotos para la ciencia."
            },
            {
                "id": "#2",
                "hanzi": "高三年级的生物老师通过生动形象的三维模型动画，深入浅出地讲解了细胞分裂过程。",
                "pinyin": "Gāosān niánjí de shēngwù lǎoshī tōngguò shēngdòng-xíngxiàng de sānwéi móxíng dònghuà, shēnrù-qiǎnchū de jiǎngjiě le xìbāo fēnliè guòchéng.",
                "en": "The high school senior biology teacher used vivid 3D animation models to explain the cell division process with remarkable clarity.",
                "es": "El profesor de biología de bachillerato explicó el proceso de mitosis celular con diáfana sencillez mediante animaciones 3D."
            }
        ],
        "collocations": [
            {"hanzi": "生物多样性", "en": "biodiversity"},
            {"hanzi": "生物钟", "en": "biological clock; circadian rhythm"},
            {"hanzi": "海洋生物", "en": "marine life / organisms"},
            {"hanzi": "微生物", "en": "microorganism; microbe"},
            {"hanzi": "生物工程", "en": "bioengineering; biotechnology"},
            {"hanzi": "水生生物", "en": "aquatic organisms"}
        ],
        "idioms": [
            {"hanzi": "万物复苏", "pinyin": "wàn wù fù sū", "meaning_en": "all living things revive and return to life in spring"},
            {"hanzi": "生机勃勃", "pinyin": "shēng jī bó bó", "meaning_en": "brimming with vitality; flourishing and vigorous"},
            {"hanzi": "生生不息", "pinyin": "shēng shēng bù xī", "meaning_en": "endless generation and ceaseless cycle of life"},
            {"hanzi": "芸芸众生", "pinyin": "yún yún zhòng shēng", "meaning_en": "all living mortals; the teeming masses of beings"}
        ],
        "character_decomposition": [
            {
                "character": "生",
                "pinyin": "shēng",
                "meaning_en": "life; give birth; grow; raw; fresh",
                "meaning_es": "vida; nacer; brotar; crudo; vivo",
                "radical": "生",
                "radical_meaning_en": "life / birth",
                "meaning_component": "土 (fertile soil) + 屮 (young sprout budding upward)",
                "sound_component": "生 (shēng)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of a green seedling 屮 sprouting out from the fertile earth 土; represents life, growth, and birth.",
                "visual_mnemonic_story_en": "A tender shoot sprouts up from fertile soil, bursting with fresh life (生).",
                "visual_mnemonic_story_es": "Un brote verde brota pujante de la tierra fértil rebosando nueva vida (生).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "HQM",
                "traditional": ""
            },
            {
                "character": "物",
                "pinyin": "wù",
                "meaning_en": "thing; object; matter; creature",
                "meaning_es": "cosa; objeto; materia; criatura",
                "radical": "牜",
                "radical_meaning_en": "cow / ox",
                "meaning_component": "牜 (spotted cattle) + 勿 (multicolored flags / diverse things)",
                "sound_component": "勿 (wù, do not / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Cattle radical 牜 paired with multicolored banners 勿; sorting speckled domestic cattle, generalizing to all worldly objects and creatures.",
                "visual_mnemonic_story_en": "An ox (牜) plows fields amidst diverse colored banners (勿), classifying things (物).",
                "visual_mnemonic_story_es": "Un buey (牜) pasta entre banderas multicolores (勿) que clasifican los seres y cosas (物).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HQPHI",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Living, growing entities (生) among the physical things of the world (物) constitute organisms (生物).",
            "composite_memory_hook_es": "Entidades que gozan de vida y crecimiento (生) entre las materias del orbe (物) son los seres vivos (生物).",
            "cultural_and_cognitive_roots": "Classical philosophy (万物: myriad entities); in modern science, 生物 translates both biological organisms and academic biology.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'shēng wù' (55-51). Hold high pitch 55 on 'shēng', then drop decisively on 'wù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "牛", "pinyin": "niú", "meaning_en": "cow; bull", "distinction_note": "Vertical stroke crosses top stroke, unlike 生"},
                {"character": "午", "pinyin": "wǔ", "meaning_en": "noon; 7th earthly branch", "distinction_note": "Has two horizontal strokes"},
                {"character": "特", "pinyin": "tè", "meaning_en": "special", "distinction_note": "Has 寺 on right of 牜 instead of 勿 in 物"},
                {"character": "牧", "pinyin": "mù", "meaning_en": "herd; pasture", "distinction_note": "Has tap radical 攵 on right of 牜"}
            ],
            "etymological_cognates": [
                {"character": "植", "pinyin": "zhí", "gloss_en": "plant; upright tree"},
                {"character": "兽", "pinyin": "shòu", "gloss_en": "beast; four-footed mammal"},
                {"character": "命", "pinyin": "mìng", "gloss_en": "life span; command"},
                {"character": "禽", "pinyin": "qín", "gloss_en": "birds; feathered fowl"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "生物 is the comprehensive biological term for all living organisms possessing cellular metabolism.",
            "contrasts": [
                {"id": "1", "compared_word": "生物 vs. 动物", "pinyin": "dòngwù", "analysis": "动物 is a subset of 生物 specifically designating motile animals, whereas 生物 includes plants, fungi, and bacteria."},
                {"id": "2", "compared_word": "生物 vs. 植物", "pinyin": "zhíwù", "analysis": "植物 specifically designates photosynthesizing flora, which is only one branch of 生物."},
                {"id": "3", "compared_word": "生物 vs. 活物", "pinyin": "huówù", "analysis": "活物 is a folksy colloquial term for live animals ('笼子里有活物'), while 生物 is rigorous and academic."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在漆黑冰冷的万米深海马里亚纳海沟底部，承受着常人难以想象的超高水压。然而科学家们惊喜地发现，这里并非生命的荒漠，许多特化的深海发光生物依靠地热喷口附近的化学能量生生不息，展现了生命极致的适应力。",
                "pinyin": "Zài qīhēi bīnglěng de wànmǐ shēnhǎi Mǎlǐyànà Hǎigōu dǐbù, chéngshòu zhe chángrén nányǐ xiǎngxiàng de chāogāo shuǐyā. Rán'ér kēxuéjiāmen jīngxǐ de fāxiàn, zhèlǐ bìngfēi shēngmìng de huāngmò, xǔduō tèhuà de shēnhǎi fāguāng shēngwù yīkào dìrè pēnkǒu fùjìn de huàxué néngliàng shēngshēng-bùxī, zhǎnxiàn le shēngmìng jízhì de shìyìnglì.",
                "en": "At the freezing bottom of the Mariana Trench, high hydrostatic pressures reign. Yet scientists discovered it is no desert; bioluminescent organisms thrive near hydrothermal vents, proving life's resilience.",
                "es": "En la sima de las Marianas reina una presión titánica. Empero, los oceanógrafos hallaron que no es un erial; seres bioluminiscentes prosperan junto a fumarolas térmicas revelando la tenacidad de la vida."
            },
            {
                "id": "#2",
                "hanzi": "保护生物多样性就是保护人类自身的未来。每一种生物都是漫长演化历史中不可复制的宝贵基因库，一旦灭绝便永远无法挽回。建立国家公园体制、严格划定生态保护红线，正是为了给野生动植物留下充足繁衍生息的乐土。",
                "pinyin": "Bǎohù shēngwù duōyàngxìng jiùshì bǎohù rénlèi zìshēn de wèilái. Měi yì zhǒng shēngwù dōu shì màncháng yǎnhuà lìshǐ zhōng bùkě fùzhì de bǎoguì jīyīnkù, yídàn mièjué biàn yǒngyuǎn wúfǎ wǎnhuí. Jiànlì guójiā gōngyuán tǐzhì, yángé huàdìng shēngtài bǎohù hóngxiàn, zhèngshì wèile gěi yěshēng dòng-zhíwù liúxià chōngzú fányǎn-shēngxī de lètǔ.",
                "en": "Protecting biodiversity is safeguarding humanity's future. Every species is an irreplaceable genetic library; once extinct, it is lost forever. National park systems preserve habitats for wildlife to multiply.",
                "es": "Preservar la biodiversidad es blindar el porvenir humano. Cada organismo es un banco genético irrepetible cuya extinción es irreparable. La red de parques nacionales brinda a la fauna y flora un edén seguro."
            }
        ]
    },

    # 06 规律
    {
        "id": "6",
        "hanzi": "规律",
        "pinyin": "guī lǜ",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "law; regular pattern; rule; regular; disciplined",
            "es": "ley natural; pauta regular; norma; ordenado; regular"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "objective inner connections and necessary laws governing the development of things",
                "definition_es": "ley intrínseca objetiva o pauta constante que rige el desarrollo de los fenómenos",
                "example_phrase": "自然规律 (laws of nature)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "regular, disciplined, and recurring at orderly predictable intervals",
                "definition_es": "ordenado, pautado o regular en horarios y hábitos",
                "example_phrase": "生活很有规律 (lead a regular/disciplined life)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "遵循大自然春生夏长、秋收冬藏的客观规律，农业生产才能获得丰厚的回报。",
                "pinyin": "Zūnxún dànzìrán chūnshēng-xiàzhǎng, qiūshōu-dōngcáng de kèguān guīlǜ, nóngyè shēngchǎn cáinéng huòdé fēnghòu de huíbào.",
                "en": "Only by following nature's objective laws of seasonal growth and harvest can agricultural production reap abundant yields.",
                "es": "Acatando las leyes objetivas de la naturaleza según las estaciones, el cultivo agrícola rinde cosechas ubérrimas."
            },
            {
                "id": "#2",
                "hanzi": "坚持健康科学的作息规律，保证充足睡眠和合理饮食，是增强身体免疫力的基石。",
                "pinyin": "Jiānchí jiànkāng kēxué de zuòxī guīlǜ, bǎozhèng chōngzú shuìmián hé hélǐ yǐnshí, shì zēngqiáng shēntǐ miǎnyìlì de jīshí.",
                "en": "Maintaining regular, scientific daily routines with ample sleep and balanced diet forms the foundation of immune vitality.",
                "es": "Mantener hábitos diarios regulares y saludables con sueño reparador y dieta equilibrada es la base del vigor inmunológico."
            }
        ],
        "collocations": [
            {"hanzi": "自然规律", "en": "laws of nature"},
            {"hanzi": "客观规律", "en": "objective law/pattern"},
            {"hanzi": "生活规律", "en": "regular lifestyle habits"},
            {"hanzi": "作息规律", "en": "regular daily routine"},
            {"hanzi": "寻找规律", "en": "search for patterns/laws"},
            {"hanzi": "发展规律", "en": "developmental laws"}
        ],
        "idioms": [
            {"hanzi": "按图索骥", "pinyin": "àn tú suǒ jì", "meaning_en": "look for a noble steed according to a picture; act by rules"},
            {"hanzi": "墨守成规", "pinyin": "mò shǒu chéng guī", "meaning_en": "stick stubbornly to obsolete rules"},
            {"hanzi": "循规蹈矩", "pinyin": "xún guī dǎo jǔ", "meaning_en": "follow rules strictly; abide by convention"},
            {"hanzi": "铁证如山", "pinyin": "tiě zhèng rú shān", "meaning_en": "irrefutable evidence as solid as a mountain"}
        ],
        "character_decomposition": [
            {
                "character": "规",
                "pinyin": "guī",
                "meaning_en": "compass; rule; regulate; plan",
                "meaning_es": "compás; regla; pauta; planificar",
                "radical": "见",
                "radical_meaning_en": "see",
                "meaning_component": "夫 (measuring master) + 见 (observing eye)",
                "sound_component": "规 (guī)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person observing with eye 见 holding a drawing compass 夫 to draw a perfect circle; represents rules and standards.",
                "visual_mnemonic_story_en": "A watchful eye (见) guides a compass (夫) to draw a perfect circle according to rule (规).",
                "visual_mnemonic_story_es": "Un ojo atento (见) guía el compás de dibujo (夫) trazando círculos según la regla (规).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QOUU",
                "traditional": "規"
            },
            {
                "character": "律",
                "pinyin": "lǜ",
                "meaning_en": "law; pitch; regulate; rhythm",
                "meaning_es": "ley; tono; ritmo; precepto",
                "radical": "彳",
                "radical_meaning_en": "step / walk",
                "meaning_component": "彳 (step / walking on path) + 聿 (hand holding scribe brush)",
                "sound_component": "律 (lǜ)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A scribe brush 聿 recording laws for travelers walking the public street 彳; represents laws, codes, and musical pitches.",
                "visual_mnemonic_story_en": "A hand writes laws with a brush (聿) to govern footsteps along public highways (彳).",
                "visual_mnemonic_story_es": "Una mano escribe decretos con pincel (聿) para ordenar los pasos por el camino real (彳).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HOLQ",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A compass establishing standards (规) combined with recorded legal and pitch codes (律) reveals regular laws (规律).",
            "composite_memory_hook_es": "El compás de trazar normas (规) y el código de leyes escritas (律) revelan las pautas regulares (规律).",
            "cultural_and_cognitive_roots": "Derived from classical standardizing tools (规 compass + 矩 square) paired with acoustic pitch pipes (十二律: twelve musical pitches); laws of the cosmos.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'guī lǜ' (55-51). Hold high pitch 55 on 'guī', then drop down sharply on 'lǜ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "视", "pinyin": "shì", "meaning_en": "look; inspect", "distinction_note": "Has altar radical 礻 on left instead of 夫 in 规"},
                {"character": "现", "pinyin": "xiàn", "meaning_en": "appear; present", "distinction_note": "Has jade radical 王 on left of 见"},
                {"character": "津", "pinyin": "jīn", "meaning_en": "ferry; saliva", "distinction_note": "Has water radical 氵 on left of 聿 instead of 彳 in 律"},
                {"character": "建", "pinyin": "jiàn", "meaning_en": "build; construct", "distinction_note": "Has long stride 廴 enclosing 聿"}
            ],
            "etymological_cognates": [
                {"character": "法", "pinyin": "fǎ", "gloss_en": "law; water level fairness"},
                {"character": "矩", "pinyin": "jǔ", "gloss_en": "carpenter square rule"},
                {"character": "则", "pinyin": "zé", "gloss_en": "knife carving standard rule"},
                {"character": "常", "pinyin": "cháng", "gloss_en": "constant invariant cloth"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "规律 denotes the invariant, inherent objective laws of science/nature, or disciplined regularity of habits.",
            "contrasts": [
                {"id": "1", "compared_word": "规律 vs. 规则", "pinyin": "guīzé", "analysis": "规则 refers to artificial, human-made regulations and game rules ('交通规则', '比赛规则'), while 规律 refers to inviolable objective natural laws ('自然规律')."},
                {"id": "2", "compared_word": "规律 vs. 法律", "pinyin": "fǎlǜ", "analysis": "法律 refers specifically to the penal and civil statutes enacted by the state legislature, whereas 规律 is universal and scientific."},
                {"id": "3", "compared_word": "规律 vs. 惯例", "pinyin": "guànlì", "analysis": "惯例 denotes customary conventions established through precedent, not necessary underlying scientific patterns."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "日月星辰运行不息，春夏秋冬寒来暑往，大自然以其严整深邃的规律维系着生态系统的动态平衡。人类若狂妄自大企图凌驾于自然之上盲目索取，必将遭受客观自然规律的严厉惩罚与无回报应。",
                "pinyin": "Rì-yuè-xīngchén yùnxíng bùxī, chūn-xià-qiū-dōng hánlái-shǔwǎng, dànzìrán yǐ qí yánzhěng shēnsù de guīlǜ wéixì zhe shēngtài xìtǒng de dòngtài pínghéng. Rénlèi ruò kuángwàng-zìdà qǐtú língjià yú zìrán zhīshàng mángmù suǒqǔ, bìjiāng zāoshòu kèguān zìrán guīlǜ de yánlì chéngfá yǔ wúqíng bàoyìng.",
                "en": "Stars turn endlessly and seasons cycle; nature maintains ecological balance through deep laws. If humans arrogantly exploit resources blind to these laws, nature will punish us severely.",
                "es": "Los astros giran y las estaciones se suceden; la naturaleza preserva su equilibrio dinámico mediante leyes inexorables. Si el hombre depreda con soberbia, la ley cósmica impondrá su castigo."
            },
            {
                "id": "#2",
                "hanzi": "在现代金融投资领域，优秀的基金经理从不轻信虚幻的市场传言，而是潜心通过历史大数据挖掘资本市场运转的内在规律。只有顺应宏观经济周期规律、坚守理性价值投资，才能在惊涛骇浪的市场波动中行稳致远。",
                "pinyin": "Zài xiàndài jīnróng tóuzī lǐngyù, yōuxiù de jījīn jīnglǐ cóng bù qīngxìn xūhuàn de shìchǎng chuányán, érshì qiánxīn tōngguò lìshǐ dàshùjù wājué zīběn shìchǎng yùnzhuǎn de nèizài guīlǜ. Zhǐyào shùnyìng hóngguān jīngjì zhōuqī guīlǜ, jiānshǒu lǐxìng jiàzhí tóuzī, cáinéng zài jīngtāo-hàilàng de shìchǎng bōdòng zhōng xíngwěn-zhìyuǎn.",
                "en": "In finance, astute fund managers rely on big data to uncover intrinsic patterns of capital markets rather than rumors. Following economic cycles and disciplined value investing yields steady returns amidst volatility.",
                "es": "En finanzas, los gestores expertos desdeñan rumores para rastrear las leyes del mercado mediante datos masivos. Acatar los ciclos macroeconómicos con sensatez garantiza navegar la volatilidad con éxito."
            }
        ]
    },

    # 07 光线
    {
        "id": "7",
        "hanzi": "光线",
        "pinyin": "guāng xiàn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "light; light ray; beam of light",
            "es": "luz; rayo de luz; haz luminoso; iluminación"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a ray, beam, or ambient condition of visible illumination emitted from a light source",
                "definition_es": "haz o rayo luminoso proyectado por una fuente de luz, o iluminación ambiental",
                "example_phrase": "光线充足 (plenty of light / well-lit)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清晨拉开厚厚的窗帘，温暖明媚的金色光线洒满了整间宽敞的书房。",
                "pinyin": "Qīngchén lākāi hòuhòu de chuānglián, wēnnuǎn míngmèi de jīnsè guāngxiàn sǎmǎn le zhěng jiān kuānchǎng de shūfáng.",
                "en": "Drawing open thick curtains in the morning, warm golden rays of light spilled across the spacious study.",
                "es": "Al descorrer las tupidas cortinas por la mañana, los cálidos rayos dorados de luz inundaron el amplio despacho."
            },
            {
                "id": "#2",
                "hanzi": "在光线昏暗的环境下长时间阅读电子屏幕，极易导致眼睛睫状肌疲劳与近视度数加深。",
                "pinyin": "Zài guāngxiàn hūn'àn de huánjìng xià cháng shíjiān yuèdú diànzǐ píngmù, jíyì dǎozhì yǎnjing jiézhuàngjī píbèi yǔ jìnshì dùshù jiāshēn.",
                "en": "Reading electronic screens for extended hours in dimly lit environments easily causes eye strain and worsening myopia.",
                "es": "Leer pantallas electrónicas en un entorno de luz tenue fatiga los músculos oculares y acelera la miopía."
            }
        ],
        "collocations": [
            {"hanzi": "光线柔和", "en": "soft/gentle light"},
            {"hanzi": "光线充足", "en": "well-lit; sufficient lighting"},
            {"hanzi": "光线昏暗", "en": "dimly lit; poor lighting"},
            {"hanzi": "强烈的阳光光线", "en": "intense sunlight rays"},
            {"hanzi": "阻挡光线", "en": "block light"},
            {"hanzi": "调整光线", "en": "adjust the lighting"}
        ],
        "idioms": [
            {"hanzi": "浮光掠影", "pinyin": "fú guāng lüè yǐng", "meaning_en": "skimming over light and shadow; superficial impression"},
            {"hanzi": "光彩夺目", "pinyin": "guāng cǎi duó mù", "meaning_en": "dazzlingly brilliant; radiant and colorful"},
            {"hanzi": "日月生辉", "pinyin": "rì yuè shēng huī", "meaning_en": "sun and moon shining with radiant splendor"},
            {"hanzi": "流光溢彩", "pinyin": "liú guāng yì cǎi", "meaning_en": "flowing with radiance and overflowing with color"}
        ],
        "character_decomposition": [
            {
                "character": "光",
                "pinyin": "guāng",
                "meaning_en": "light; ray; glory; bare; only",
                "meaning_es": "luz; rayo; brillo; descalzo; solo",
                "radical": "儿",
                "radical_meaning_en": "human / legs",
                "meaning_component": "火 (fire torch) + 儿 (kneeling person carrying fire above head)",
                "sound_component": "光 (guāng)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of a human 儿 carrying a blazing torch 火 atop their head to illuminate the dark; represents light and radiance.",
                "visual_mnemonic_story_en": "A runner holds a blazing fire torch high overhead (火), illuminating the dark with radiant light (光).",
                "visual_mnemonic_story_es": "Una figura alza una antorcha de fuego (火) sobre su cabeza disipando las sombras con viva luz (光).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "FMU",
                "traditional": ""
            },
            {
                "character": "线",
                "pinyin": "xiàn",
                "meaning_en": "thread; string; wire; line; ray",
                "meaning_es": "hilo; hebra; línea; alambre; rayo",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (spun silk thread) + 戋 (small slender / phonetic)",
                "sound_component": "戋 (jiān, slender / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spun silk threads 纟 stretching out in a thin linear fiber 戋; extended to geometric lines and straight optical rays.",
                "visual_mnemonic_story_en": "A delicate strand of silk (纟) pulls straight and thin like a linear beam (线).",
                "visual_mnemonic_story_es": "Una fina hebra de seda (纟) se estira recta y delgada dibujando una línea luminosa (线).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMII",
                "traditional": "線"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Torches shedding radiant illumination (光) extending in linear threads (线) make beams of light (光线).",
            "composite_memory_hook_es": "La antorcha que alumbra (光) trazando hebras rectas en la penumbra (线) forma el haz de luz (光线).",
            "cultural_and_cognitive_roots": "Optical geometric physics; traditional Chinese shadow puppetry (皮影戏) mastered the projection of luminous lines through translucent parchment.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling fourth tone: 'guāng xiàn' (55-51). Hold high pitch 55 on 'guāng', then drop down sharply on 'xiàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "先", "pinyin": "xiān", "meaning_en": "first; ancestor", "distinction_note": "Has 丿 on top instead of central dot and stroke of 光"},
                {"character": "充", "pinyin": "chōng", "meaning_en": "fill; charge", "distinction_note": "Has 亠 atop 厶 and 儿"},
                {"character": "钱", "pinyin": "qián", "meaning_en": "money; coin", "distinction_note": "Has metal radical 钅 on left instead of silk 纟 in 线"},
                {"character": "浅", "pinyin": "qiǎn", "meaning_en": "shallow; light", "distinction_note": "Has water radical 氵 on left of 戋"}
            ],
            "etymological_cognates": [
                {"character": "芒", "pinyin": "máng", "gloss_en": "ray of light; awn of grass"},
                {"character": "束", "pinyin": "shù", "gloss_en": "bundle; beam of rays"},
                {"character": "缕", "pinyin": "lǚ", "gloss_en": "strand; wisp of smoke/light"},
                {"character": "照", "pinyin": "zhào", "gloss_en": "shine; illuminate path"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "光线 designates linear rays of optical illumination or environmental ambient lighting conditions.",
            "contrasts": [
                {"id": "1", "compared_word": "光线 vs. 光芒", "pinyin": "guāngmáng", "analysis": "光芒 emphasizes brilliant, dazzling radiating halos ('太阳的光芒', '放射光芒'), while 光线 is neutral physical illumination ('光线太暗')."},
                {"id": "2", "compared_word": "光线 vs. 阳光", "pinyin": "yángguāng", "analysis": "阳光 is specifically natural sunlight from the solar orb, while 光线 includes artificial bulbs, laser beams, and candles."},
                {"id": "3", "compared_word": "光线 vs. 灯光", "pinyin": "dēngguāng", "analysis": "灯光 specifically denotes the glow produced by manufactured electric lamps, whereas 光线 covers all rays."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在绘画与摄影艺术中，光线被称为塑造形象的“第二支画笔”。大师们熟练运用侧光展现人物面部坚毅深邃的轮廓，用逆光勾勒秀发的金色光晕，恰到好处的光线明暗反差赋予画面无限的生命力与艺术感染力。",
                "pinyin": "Zài huìhuà yǔ shèyǐng yìshù zhōng, guāngxiàn bèi chēngwéi sùzào xíngxiàng de 'dì-èr zhī huàbǐ'. Dàshīmen shúliàn yùnyòng cèguāng zhǎnxiàn rénwù miànbù jiānyì-shēnsù de lúnkuò, yòng nìguāng gōulè xiùfà de jīnsè guāngyùn, qiàdàohǎochù de guāngxiàn míng'àn fǎnchà fùyǔ huàmiàn wúxiàn de shēngmìnglì yǔ yìshù gǎnrǎnlì.",
                "en": "In painting and photography, light is called the second paintbrush. Masters skillfully use sidelight to sculpt facial profiles and backlighting to outline hair halos, infusing imagery with vital contrast.",
                "es": "En pintura y fotografía, la luz se considera el segundo pincel. Los maestros emplean luces laterales para cincelar perfiles y contraluces dorados, infundiendo un vivo contraste y plasticidad al lienzo."
            },
            {
                "id": "#2",
                "hanzi": "盛夏午后烈日当空，茂密幽静的原始森林中，缕缕金色光线穿透重重叠叠的树冠枝叶倾泻而下，在布满松针的湿润地面上投下斑驳陆离的光影。这奇幻宁静的自然丁达尔效应景观，令人叹为观止、流连忘返。",
                "pinyin": "Shèngxià wǔhòu lièrì dāngkōng, màomì yōujìng de yuánshǐ sēnlín zhōng, lǚlǚ jīnsè guāngxiàn chuāntòu chóngchóng-diédié de shùguān zhīyè qīngxiè ér xià, zài bùmǎn sōngzhēn de shīrùn dīmiàn shàng tóuxià bānbó-lùlí de guāngyǐng. Zhè qíhuàn níngjìng de zìrán Dīngdá'ěr xiàoyìng jǐngguān, lìngrén tànwéiguānzhǐ, liúlián-wàngfǎn.",
                "en": "Under scorching midsummer sun, rays of golden light pierce dense forest canopies, casting dappled shadows over pine needles. This Tyndall effect phenomenon captivates visitors with quiet natural beauty.",
                "es": "Bajo el sol estival, hebras de luz dorada perforan el follaje del bosque virgen proyectando sombras sobre agujas de pino. El efecto Tyndall crea una estampa mágica y sosegada que embelesa al paseante."
            }
        ]
    },

    # 08 必要
    {
        "id": "8",
        "hanzi": "必要",
        "pinyin": "bì yào",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "necessary; essential; indispensable",
            "es": "necesario; indispensable; esencial; imperativo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "indispensable, essential, or strictly required for achieving an objective",
                "definition_es": "indispensable, imperioso o preceptivo para lograr un fin o garantizar un resultado",
                "example_phrase": "有必要这样做 (it is necessary to do so)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在野外进行高风险探险之前，做好充足的体能储备并携带必要的应急药品是绝对不可忽视的。",
                "pinyin": "Zài yěwài jìnxíng gāofēngxiǎn tànxiǎn zhīqián, zuòhǎo chōngzú de tǐnéng chǔbèi bìng xiédài bìyào de yīngjí yàopǐn shì juéduì bùkě hūshì de.",
                "en": "Before engaging in high-risk outdoor expeditions, preparing physical stamina and carrying necessary emergency medicines must never be neglected.",
                "es": "Antes de emprender una expedición arriesgada al aire libre, contar con buena preparación física y botiquines necesarios resulta imperativo."
            },
            {
                "id": "#2",
                "hanzi": "为了确保工程项目保质保量如期交付，项目部认为有必要召开一次全员安全质量交底大会。",
                "pinyin": "Wèile quèbǎo gōngchéng xiàngmù bǎozhì-bǎoliàng rúqī jiāofù, xiàngmùbù rènwéi yǒu bìyào zhàokāi yí cì quányuán ānquán zhìliàng jiāodǐ dàhuì.",
                "en": "To ensure the engineering project is delivered on schedule with quality, the team considered it necessary to convene a safety briefing.",
                "es": "Para garantizar la entrega puntual y con calidad de la obra, la dirección estimó necesario convocar una junta general de seguridad."
            }
        ],
        "collocations": [
            {"hanzi": "非常有必要", "en": "highly necessary; very essential"},
            {"hanzi": "必要条件", "en": "necessary condition / prerequisite"},
            {"hanzi": "必要措施", "en": "necessary measures"},
            {"hanzi": "必要的准备", "en": "necessary preparations"},
            {"hanzi": "毫无必要", "en": "completely unnecessary"},
            {"hanzi": "视为必要", "en": "deemed necessary"}
        ],
        "idioms": [
            {"hanzi": "不可或缺", "pinyin": "bù kě huò quē", "meaning_en": "indispensable; cannot do without"},
            {"hanzi": "必不可少", "pinyin": "bì bù kě shǎo", "meaning_en": "absolutely essential; indispensable"},
            {"hanzi": "刻不容缓", "pinyin": "kè bù róng huǎn", "meaning_en": "brook no delay; demand immediate action"},
            {"hanzi": "迫在眉睫", "pinyin": "pò zài méi jié", "meaning_en": "imminent and urgent; pressing close to eyelashes"}
        ],
        "character_decomposition": [
            {
                "character": "必",
                "pinyin": "bì",
                "meaning_en": "certainly; must; surely; necessary",
                "meaning_es": "sin falta; deber; forzoso; necesario",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "弋 (stake / split) + 八 (slash through / decisive resolve)",
                "sound_component": "必 (bì)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Originally a measuring weapon or divider stroke slashing decisively through; signifies certainty, necessity, and firmness.",
                "visual_mnemonic_story_en": "A firm slash cuts decisively across, making an unavoidable, necessary mark (必).",
                "visual_mnemonic_story_es": "Un trazo firme cruza con rotunda certeza fijando un imperativo ineludible (必).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "PHX",
                "traditional": ""
            },
            {
                "character": "要",
                "pinyin": "yào",
                "meaning_en": "want; need; must; vital; important",
                "meaning_es": "querer; necesitar; esencial; vital",
                "radical": "覀",
                "radical_meaning_en": "west / cover",
                "meaning_component": "覀 (two hands on human waist) + 女 (woman)",
                "sound_component": "要 (yào)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Original pictograph of hands resting on a woman's waist 女; waist being the vital pivot of the body, extended to vital necessity.",
                "visual_mnemonic_story_en": "Hands embrace the waist (覀) of a figure (女), holding the vital core of need (要).",
                "visual_mnemonic_story_es": "Manos que sujetan la cintura (覀) femenina (女) destacando el eje vital indispensable (要).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MWV",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Decisive absolute certainty (必) paired with the vital waist pivot (要) makes something indispensable (必要).",
            "composite_memory_hook_es": "Certeza ineludible (必) y eje vital indispensable (要) conforman lo necesario (必要).",
            "cultural_and_cognitive_roots": "Philosophical logic pairing: 必 (categorical imperative) + 要 (vital pivot), widely used in logic (必要条件 vs. 充分条件).",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'bì yào' (51-51). Descend sharply on 'bì', then strike down firmly on 'yào'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "心", "pinyin": "xīn", "meaning_en": "heart; mind", "distinction_note": "Lacks the long slash crossing stroke of 必"},
                {"character": "毖", "pinyin": "bì", "meaning_en": "careful; caution", "distinction_note": "Consists of two 必 side by side"},
                {"character": "耍", "pinyin": "shuǎ", "meaning_en": "play; juggle", "distinction_note": "Has 而 atop 女 instead of 覀 in 要"},
                {"character": "妥", "pinyin": "tuǒ", "meaning_en": "proper; settled", "distinction_note": "Has 爪 atop 女"}
            ],
            "etymological_cognates": [
                {"character": "需", "pinyin": "xū", "gloss_en": "rain on beard; need"},
                {"character": "须", "pinyin": "xū", "gloss_en": "must; beard hairs"},
                {"character": "重", "pinyin": "zhòng", "gloss_en": "heavy burden; important"},
                {"character": "切", "pinyin": "qiè", "gloss_en": "cut close; urgent"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "必要 emphasizes that a condition, action, or tool is indispensable and cannot be dispensed with.",
            "contrasts": [
                {"id": "1", "compared_word": "必要 vs. 重要", "pinyin": "zhòngyào", "analysis": "重要 describes high value, significance, or weight ('重要会议'), while 必要 emphasizes that an action is strictly mandatory or prerequisite ('有必要进行核实')."},
                {"id": "2", "compared_word": "必要 vs. 必须", "pinyin": "bìxū", "analysis": "必须 is an adverb/auxiliary verb meaning 'must / have to' modifying verbs ('必须按时到达'), while 必要 is an adjective ('必要的步骤')."},
                {"id": "3", "compared_word": "必要 vs. 需要", "pinyin": "xūyào", "analysis": "需要 functions as a common verb meaning 'to need / demand' ('需要帮助'), while 必要 is descriptive."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代企业治理中，定期的财务审计是防范经营风险的必要手段。独立审计机构通过核查账目流水、盘点资产负债，能够及时发现管理漏洞与合规隐患，为企业稳健长远发展筑牢不可或缺的制度屏障。",
                "pinyin": "Zài xiàndài qǐyè zhìlǐ zhōng, dìngqī de cáiwù shěnjì shì fángfàn jīngyíng fēngxiǎn de bìyào shǒuduàn. Dúlì shěnjì jīgòu tōngguò héchá zhàngmù liúshuǐ, pándiǎn zīchǎn-fùzhài, nénggòu jíshí fāxiàn guǎnlǐ lòudòng yǔ hégūi yǐnhuàn, wèi qǐyè wěnjiàn chángyuǎn fāzhǎn zhùláo bùkě-huòquē de zhìdù píngzhàng.",
                "en": "In corporate governance, periodic financial audits are necessary tools to avert operational risks. Independent auditors verify balances to plug compliance loopholes, fortifying institutional barriers.",
                "es": "En la gestión corporativa, las auditorías financieras periódicas son un resorte necesario contra riesgos. Auditores independientes cotejan balances subsanando lagunas y afianzando la solvencia empresarial."
            },
            {
                "id": "#2",
                "hanzi": "人际交往中，保持适当的心理边界是维护健康友谊的必要前提。即使再要好的知己朋友，也应当相互尊重彼此的私人空间与独立选择，不横加干涉。唯有保持这种有分寸的默契，友谊之花才能长盛不衰。",
                "pinyin": "Rénjì jiāowǎng zhōng, bǎochí shìdàng de xīnlǐ biānjiè shì wéihù jiànkāng yǒuyì de bìyào qiántí. Jíshǐ zài yàohǎo de zhījǐ péngyou, yě yīngdāng xiānghù zūnzhòng bǐcǐ de sīrén kōngjiān yǔ dúlì xuǎnzé, bù héngjiā gānshè. Wéiyǒu bǎochí zhè zhǒng yǒu fēncùn de mòqì, yǒuyì zhī huā cáinéng chángshèng-bùshuāi.",
                "en": "In interpersonal relations, healthy boundaries are a necessary prerequisite. Even the closest friends should respect private space and choices without meddling, allowing true friendship to flourish.",
                "es": "En el trato humano, delimitar el espacio personal es premisa necesaria para una amistad sana. Incluso íntimos camaradas deben respetar la intimidad ajena sin entrometerse para que florezca el aprecio mutuo."
            }
        ]
    },

    # 09 过渡
    {
        "id": "9",
        "hanzi": "过渡",
        "pinyin": "guò dù",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to transition; to transit; transition; interim phase",
            "es": "hacer la transición; transitar; transición; fase intermedia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to pass, shift, or transit smoothly from one stage, state, or era to another",
                "definition_es": "pasar, evolucionar o mudar paulatinamente de un estado o etapa a otra",
                "example_phrase": "平稳过渡 (smooth transition)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a transitional period, interim stage, or passage connecting two phases",
                "definition_es": "período de transición, fase intermedia o puente entre dos épocas",
                "example_phrase": "过渡时期 (transitional period)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "从深度睡眠到完全清醒，人体的中枢神经系统需要经历一段温和的生理过渡阶段。",
                "pinyin": "Cóng shēndù shuìmián dào wánquán qīngxǐng, réntǐ de zhōngshū shénjīng xìtǒng xūyào jīnglì yí duàn wēnhé de shēnglǐ guòdù jiēduàn.",
                "en": "From deep sleep to full alertness, the human central nervous system requires a gentle physiological transitional phase.",
                "es": "Del sueño profundo a la vigilia plena, el sistema nervioso central precisa un sosegado período de transición fisiológica."
            },
            {
                "id": "#2",
                "hanzi": "在老厂长退休之际，新老管理团队密切配合，实现了企业经营管理权的平稳过渡。",
                "pinyin": "Zài lǎo chǎngzhǎng tuìxiū zhī jì, xīn-lǎo guǎnlǐ tuánduì mìqiè pèihé, shíxiàn le qǐyè jīngyíng guǎnlǐquán de píngwěn guòdù.",
                "en": "Upon the veteran director's retirement, new and old management teams collaborated closely, achieving a smooth handover of managerial power.",
                "es": "Con la jubilación del veterano director, la directiva saliente y entrante cooperaron estrechamente logrando un traspaso de poderes impecable."
            }
        ],
        "collocations": [
            {"hanzi": "平稳过渡", "en": "smooth transition"},
            {"hanzi": "过渡时期", "en": "transitional period"},
            {"hanzi": "过渡阶段", "en": "interim/transition stage"},
            {"hanzi": "自然过渡", "en": "natural transition"},
            {"hanzi": "过渡性措施", "en": "transitional/interim measures"},
            {"hanzi": "顺利过渡", "en": "successful/smooth transition"}
        ],
        "idioms": [
            {"hanzi": "承前启后", "pinyin": "chéng qián qǐ hòu", "meaning_en": "carry forward the past and open up the future; link past and future"},
            {"hanzi": "继往开来", "pinyin": "jì wǎng kāi lái", "meaning_en": "build on past achievements and open up path forward"},
            {"hanzi": "渐入佳境", "pinyin": "jiàn rù jiā jìng", "meaning_en": "gradually enter a pleasant phase; steadily improve"},
            {"hanzi": "水到渠成", "pinyin": "shuǐ dào qú chéng", "meaning_en": "water flows and a channel is formed; succeed naturally when ripe"}
        ],
        "character_decomposition": [
            {
                "character": "过",
                "pinyin": "guò",
                "meaning_en": "pass; cross; go beyond; mistake",
                "meaning_es": "pasar; cruzar; sobrepasar; error",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walk/movement) + 寸 (inch / hand measure)",
                "sound_component": "呙 (guō, twisted mouth / phonetic origin)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Footsteps 辶 pacing across a threshold or measured mark 寸; signifies crossing over, passing through, or exceeding boundaries.",
                "visual_mnemonic_story_en": "Footsteps (辶) measure out distance (寸) to cross over the boundary line (过).",
                "visual_mnemonic_story_es": "Pasos firmes (辶) miden el espacio (寸) para cruzar la frontera hacia el otro lado (过).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YDI",
                "traditional": "過"
            },
            {
                "character": "渡",
                "pinyin": "dù",
                "meaning_en": "ferry; cross river; transit; tide over",
                "meaning_es": "cruzar río; vadear; transitar; superar",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water/river) + 度 (measure/ferry pace)",
                "sound_component": "度 (dù, degree/measure / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 paired with 度 (measure/capacity); crossing across rivers by ferryboat, extended to traversing transitions.",
                "visual_mnemonic_story_en": "A ferry carries passengers across deep waters (氵) to the opposite shore (度), crossing over safely (渡).",
                "visual_mnemonic_story_es": "Una barcaza surca las aguas (氵) arribando a la orilla opuesta (度) para vadear el río (渡).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EITO",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Crossing a boundary (过) like ferrying across a wide river (渡) achieves a smooth transition (过渡).",
            "composite_memory_hook_es": "Cruzar el linde (过) como quien cruza en barca el río (渡) describe la transición (过渡).",
            "cultural_and_cognitive_roots": "Ferry river crossing metaphor: ancient travelers took ferries (渡口) to cross treacherous currents; applied conceptually to shifts in politics and physiology.",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'guò dù' (51-51). Descend sharply on 'guò', then drop down decisively again on 'dù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "这", "pinyin": "zhè", "meaning_en": "this", "distinction_note": "Has 文 inside 辶 instead of 寸 in 过"},
                {"character": "进", "pinyin": "jìn", "meaning_en": "enter; advance", "distinction_note": "Has 井 inside 辶"},
                {"character": "度", "pinyin": "dù", "meaning_en": "degree; measure", "distinction_note": "Lacks the water radical 氵 of 渡"},
                {"character": "镀", "pinyin": "dù", "meaning_en": "plate; coat with metal", "distinction_note": "Has metal radical 钅 on left"}
            ],
            "etymological_cognates": [
                {"character": "迁", "pinyin": "qiān", "gloss_en": "migrate; move house"},
                {"character": "移", "pinyin": "yí", "gloss_en": "shift; transplant rice"},
                {"character": "变", "pinyin": "biàn", "gloss_en": "change; alter form"},
                {"character": "化", "pinyin": "huà", "gloss_en": "transform; melt"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "过渡 emphasizes the progressive, intermediate bridging process between two distinct historical, physical, or physiological stages.",
            "contrasts": [
                {"id": "1", "compared_word": "过渡 vs. 转变", "pinyin": "zhuǎnbiàn", "analysis": "转变 emphasizes changing the direction, nature, or attitude of something ('转变观念'), while 过渡 emphasizes the temporal interim bridging phase."},
                {"id": "2", "compared_word": "过渡 vs. 转换", "pinyin": "zhuǎnhuàn", "analysis": "转换 emphasizes switching between discrete modes or formats ('转换频道', '转换格式'), while 过渡 is a gradual smooth shift."},
                {"id": "3", "compared_word": "过渡 vs. 过度", "pinyin": "guòdù", "analysis": "过度 (homophone with 度) means excessive or going beyond healthy limits ('过度疲劳', '过度饮酒'), while 过渡 means transition."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "四季更迭时节，秋天是大自然从夏日的繁盛喧嚣向冬日的沉静萧瑟平稳过渡的金色桥梁。树叶在阵阵微风中缓缓由绿变黄，候鸟成群结队整齐南飞，一切生物都在从容不迫地做好迎接寒冬的过渡准备。",
                "pinyin": "Sìjì gèngdié shíjié, qiūtiān shì dànzìrán cóng xiàrì de fánshèng xuānxiāo xiàng dōngrì de chénjìng xiāosè píngwěn guòdù de jīnsè qiáoliáng. Shùyè zài zhènzhèn wēifēng zhōng huǎnhuǎn yóu lǜ biàn huáng, hòuniǎo chéngqún-jiéduì zhěngqí nánfēi, yíqiè shēngwù dōu zài cóngróng-bùpò de zuòhǎo yíngjiē hándōng de guòdù zhǔnbèi.",
                "en": "During seasonal change, autumn is nature's golden bridge transitioning smoothly from summer lushness to winter dormancy. Leaves turn yellow and migratory birds fly south, readying for winter.",
                "es": "En la rueda del año, el otoño es puente áureo que transita con sosiego de la fronda estival al letargo invernal. Hojas amarillas y aves rumbo al sur preparan a la biosfera para el invierno."
            },
            {
                "id": "#2",
                "hanzi": "从传统化石能源向绿色清洁能源转型，是一个涉及千行百业的宏大系统工程。在这个历史过渡时期，必须统筹兼顾能源安全保供与节能减排目标，合理发展天然气等过渡清洁替代能源，确保国民经济平稳运行。",
                "pinyin": "Cóng chuántǒng huàshí néngyuán xiàng lǜsè qīngjié néngyuán zhuǎnxíng, shì yí ge shèjí qiānháng-bǎiyè de hóngdà xìtǒng gōngchéng. Zài zhè ge lìshǐ guòdù shíqī, bìxū tǒngchóu jiāngù néngyuán ānquán bǎogōng yǔ jiénéng jiǎnpái mùbiāo, hélǐ fāzhǎn tiānránqì děng guòdù qīngjié tìdài néngyuán, quèbǎo guómín jīngjì píngwěn yùnxíng.",
                "en": "Transitioning from fossil fuels to clean energy is a vast systemic undertaking. In this transitional era, balancing energy security with emissions reduction via bridge fuels like natural gas ensures economic stability.",
                "es": "Migrar del combustible fósil a la energía limpia es un cambio estructural. En este período de transición, compaginar el suministro con la descarbonización mediante energías puente asegura la estabilidad económica."
            }
        ]
    },

    # 10 浅
    {
        "id": "10",
        "hanzi": "浅",
        "pinyin": "qiǎn",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "shallow; light (color/sleep); superficial; simple",
            "es": "poco profundo; superficial; claro (color); ligero (sueño)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "shallow in depth from surface to bottom (opposite of deep/深)",
                "definition_es": "de poca profundidad o fondo; somero (opuesto a profundo/深)",
                "example_phrase": "水很浅 (the water is shallow)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "light, superficial, or brief (of color, sleep, knowledge, or emotional bonds)",
                "definition_es": "claro (de color), superficial (de saber) o ligero y fácil de interrumpir (de sueño)",
                "example_phrase": "浅睡眠 / 浅蓝色 (light sleep / light blue)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清澈见底的溪水很浅，刚没过脚踝，成群的银色小鱼在光滑的鹅卵石间欢快游动。",
                "pinyin": "Qīngchè jiàndǐ de xīshuǐ hěn qiǎn, gāng mòguò jiǎohuái, chéngqún de yínsè xiǎoyú zài guānghuá de éluǎnshí jiān huānkuài yóudòng.",
                "en": "The crystal-clear stream water is very shallow, barely covering ankles, as schools of silver minnows dart among smooth pebbles.",
                "es": "El arroyo cristalino es tan somero que apenas cubre los tobillos, con pececillos plateados nadando alegres entre cantos rodados."
            },
            {
                "id": "#2",
                "hanzi": "在半夜处于浅睡眠阶段时，哪怕是远处传来极其微弱的关门声也容易让人警醒过来。",
                "pinyin": "Zài bànyè chǔyú qiǎn shuìmián jiēduàn shí, nǎpà shì yuǎnchù chuánlái jíqí wēiruò de guānmén shēng yě róngyì ràng rén jǐngxǐng guòlai.",
                "en": "When in the light sleep stage in the middle of the night, even a faint distant door-closing sound easily jolts one awake.",
                "es": "En la fase de sueño ligero a medianoche, el más leve chasquido de una puerta lejana despierta de inmediato al durmiente."
            }
        ],
        "collocations": [
            {"hanzi": "浅睡眠", "en": "light sleep"},
            {"hanzi": "浅色", "en": "light color"},
            {"hanzi": "浅蓝色", "en": "light blue"},
            {"hanzi": "由浅入深", "en": "from shallow to deep; step by step"},
            {"hanzi": "水浅", "en": "shallow water"},
            {"hanzi": "学识浅薄", "en": "shallow learning / superficial knowledge"}
        ],
        "idioms": [
            {"hanzi": "浅尝辄止", "pinyin": "qiǎn cháng zhé zhǐ", "meaning_en": "stop after tasting a little; skim the surface without deep study"},
            {"hanzi": "深浅莫测", "pinyin": "shēn qiǎn mò cè", "meaning_en": "depth unpredictable; unfathomable and hard to gauge"},
            {"hanzi": "深入浅出", "pinyin": "shēn rù qiǎn chū", "meaning_en": "explain profound truths in simple, accessible language"},
            {"hanzi": "浅见寡闻", "pinyin": "qiǎn jiàn guǎ wén", "meaning_en": "have superficial views and limited experience"}
        ],
        "character_decomposition": [
            {
                "character": "浅",
                "pinyin": "qiǎn",
                "meaning_en": "shallow; light; superficial",
                "meaning_es": "poco profundo; claro; superficial",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water flow) + 戋 (small / narrow / shallow)",
                "sound_component": "戋 (jiān, small / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 combined with 戋 (two small halberds / petty); little depth of water, meaning shallow or light.",
                "visual_mnemonic_story_en": "Water drops (氵) pool only in tiny, narrow amounts (戋), revealing a shallow stream (浅).",
                "visual_mnemonic_story_es": "Un hilillo de agua (氵) apenas llena un cuenco menguado (戋) formando un charco somero (浅).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "EII",
                "traditional": "淺"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Water (氵) that is scanty and narrow (戋) is shallow and light (浅).",
            "composite_memory_hook_es": "El agua (氵) escasa y menguada (戋) denota lo somero y claro (浅).",
            "cultural_and_cognitive_roots": "Spatial depth paired with cognitive depth: paired universally as an antonym with 深 (deep); symbolizes introductory knowledge (深入浅出).",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'qiǎn' (214). Dip down low into pitch 2 and curve gently back up to 4."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "钱", "pinyin": "qián", "meaning_en": "money; coin", "distinction_note": "Has metal radical 钅 on left instead of water 氵 in 浅"},
                {"character": "线", "pinyin": "xiàn", "meaning_en": "thread; line", "distinction_note": "Has silk radical 纟 on left of 戋"},
                {"character": "残", "pinyin": "cán", "meaning_en": "cruel; disabled; remnant", "distinction_note": "Has bone radical 歹 on left of 戋"},
                {"character": "践", "pinyin": "jiàn", "meaning_en": "trample; fulfill", "distinction_note": "Has foot radical 足 on left of 戋"}
            ],
            "etymological_cognates": [
                {"character": "薄", "pinyin": "báo", "gloss_en": "thin; slight layer"},
                {"character": "浮", "pinyin": "fú", "gloss_en": "float on surface"},
                {"character": "轻", "pinyin": "qīng", "gloss_en": "light weight; gentle"},
                {"character": "淡", "pinyin": "dàn", "gloss_en": "mild; insipid; pale"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "浅 strictly denotes lack of depth (physical water, cognitive learning, sleep, or color saturation).",
            "contrasts": [
                {"id": "1", "compared_word": "浅 vs. 薄", "pinyin": "báo", "analysis": "薄 refers to physical planar thickness or insubstantiality ('薄纸', '感情淡薄'), while 浅 refers to water depth, sleep lightness, or colors."},
                {"id": "2", "compared_word": "浅 vs. 淡", "pinyin": "dàn", "analysis": "淡 focuses on flavor (mild/bland), scent, or weak concentration of liquids ('淡水', '味道淡'), while 浅 describes visual color hue or water level."},
                {"id": "3", "compared_word": "浅 vs. 短", "pinyin": "duǎn", "analysis": "短 refers to linear physical length or chronological duration ('时间短'), while 浅 refers to vertical depth."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "初学者研读晦涩深奥的古代哲学经典，最忌讳浅尝辄止与浮躁求快。唯有循序渐进、由浅入深，耐下心来一字一句细细推敲字里行间的微言大义，方能真正领会圣贤先哲博大精深的治世智慧与处世哲学。",
                "pinyin": "Chūxuézhě yándú huìsè shēn'ào de gǔdài zhéxué jīngdiǎn, zuì jìhuì qiǎncháng-zhézhǐ yǔ fúzào qiúkuài. Wéiyǒu xúnxù-jiànjìn, yóuqiǎn-rùshēn, nàixià xīnlái yízì-yíjù xìxì tuīqiāo zìlǐ-hángjiān de wēiyán-dàyì, fāngnéng zhēnzhèng lǐnghuì shèngxián-xiānzhé bódà-jīngshēn de zhìshì zhìhuì yǔ chǔshì zhéxué.",
                "en": "When novices study ancient philosophy, superficial skimming and impatient haste are worst. Only progressing step by step from shallow to deep and pondering sentences carefully can one grasp profound wisdom.",
                "es": "Al abordar la filosofía clásica, el peor vicio es el desdén superficial. Solo avanzando con sosiego de lo elemental a lo hondo y saboreando cada renglón se asimila la magna sabiduría de los sabios."
            },
            {
                "id": "#2",
                "hanzi": "盛夏时节，年轻女孩换上一袭优雅的浅绿色亚麻连衣裙，微风吹拂裙摆如荷叶摇曳，给人一种清爽宜人的清凉之感。浅色系服饰不仅在视觉上令人赏心悦目，更能在炎炎夏日有效反射刺目的阳光热量。",
                "pinyin": "Shèngxià shíjié, niánqīng nǚhái huànshàng yì xí yōuyǎ de qiǎnlǜsè yàmá liányīqún, wēifēng chuīfú qúnbǎi rú héyè yáoyè, jǐrén yì zhǒng qīngshuǎng yírén de qīngliángzhīgǎn. Qiǎnsèxì fúshì bùjǐn zài shìjué shàng lìngrén shǎnxīn-yuèmù, gèng néng zài yányán xiàrì yǒuxiào fǎnshè cìmù de yángguāng rèliàng.",
                "en": "In midsummer, a girl wears a light green linen dress, swaying like lotus leaves in the breeze with refreshing coolness. Light-colored clothing pleases the eye and reflects scorching sunlight heat effectively.",
                "es": "En canícula, un vestido de lino verde claro ondea como hoja de loto brindando una grata frescura. La gama de tonos claros deleita la vista y refleja el calor del sol abrasador con eficacia."
            }
        ]
    }
]

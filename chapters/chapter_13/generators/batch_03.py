# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 何况
    {
        "id": "21",
        "hanzi": "何况",
        "pinyin": "hé kuàng",
        "part_of_speech": "Conjunction",
        "meanings_summary": {
            "en": "let alone; much less; not to mention",
            "es": "mucho menos; con mayor razón; cuánto más"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Conjunction",
                "register": "Standard",
                "definition_en": "used to introduce a further more obvious point or reason, often equivalent to 'much less' or 'all the more so'",
                "definition_es": "introduce una razón o consideración adicional aún más evidente; mucho más, con más motivo",
                "example_phrase": "大人尚且吃不消，何况小孩呢 (adults can hardly endure it, let alone a child)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "连经验丰富的老船长在如此恶劣的风暴中都感到吃力，何况是初次出海的新水手呢。",
                "pinyin": "Lián jīngyàn fēngfù de lǎo chuánzhǎng zài rúcǐ èliè de fēngbào zhōng dōu gǎndào chīlì, hékuàng shì chūcì chūhǎi de xīn shuǐshǒu ne.",
                "en": "Even seasoned captains find it arduous in such severe storms, let alone novice sailors putting to sea for the first time.",
                "es": "Incluso un viejo capitán curtido se las ve difíciles en semejante temporal, cuánto más los marineros novatos en su primera travesía."
            },
            {
                "id": "#2",
                "hanzi": "目前公司核心产品的销量在本土市场尚且停滞不前，何况盲目进军竞争惨烈的海外新兴市场。",
                "pinyin": "Mùqián gōngsī héxīn chǎnpǐn de xiàoliàng zài běntǔ shìchǎng shàngqiě tíngzhì-bùqián, hékuàng mángmù jìnjūn jìngzhēng cǎnliè de hǎiwài xīnxīng shìchǎng.",
                "en": "Presently, core product sales remain stagnant even domestically, let alone blindly charging into cutthroat emerging overseas markets.",
                "es": "Las ventas de la empresa están estancadas en el mercado nacional, cuánto más si se aventura a ciegas en el feroz mercado exterior."
            }
        ],
        "collocations": [
            {"hanzi": "更何况", "en": "even more so; not to mention"},
            {"hanzi": "尚且……何况……", "en": "even... let alone..."},
            {"hanzi": "何况是", "en": "much less; let alone being"},
            {"hanzi": "又何况", "en": "and what is more; let alone"},
            {"hanzi": "何况还要", "en": "not to mention having to"},
            {"hanzi": "何况如今", "en": "let alone nowadays"}
        ],
        "idioms": [
            {"hanzi": "顾此失彼", "pinyin": "gù cǐ shī bǐ", "meaning_en": "attend to one and lose the other; unable to juggle both"},
            {"hanzi": "雪上加霜", "pinyin": "xuě shàng jiā shuāng", "meaning_en": "add frost to snow; one disaster after another"},
            {"hanzi": "举步维艰", "pinyin": "jǔ bù wéi jiān", "meaning_en": "hard to take a single step; struggling with difficulty"},
            {"hanzi": "力不从心", "pinyin": "lì bù cóng xīn", "meaning_en": "ability falls short of one's desires; powerless to help"}
        ],
        "character_decomposition": [
            {
                "character": "何",
                "pinyin": "hé",
                "meaning_en": "what; how; why",
                "meaning_es": "qué; cómo; por qué",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person carrying burden) + 可 (exclamation)",
                "sound_component": "可 (kě / phonetic link)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 carrying a shoulder pole 可; originally bearing a load, borrowed as an interrogative pronoun (what/why).",
                "visual_mnemonic_story_en": "A standing person (亻) carrying a heavy shoulder pole asking what burden lies ahead (何).",
                "visual_mnemonic_story_es": "Una persona (亻) cargando una pértiga al hombro preguntando qué peso le aguarda (何).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "ONR",
                "traditional": "何"
            },
            {
                "character": "况",
                "pinyin": "kuàng",
                "meaning_en": "condition; situation; furthermore",
                "meaning_es": "situación; además; estado",
                "radical": "冫",
                "radical_meaning_en": "ice",
                "meaning_component": "冫 (ice cold water) + 兄 (elder brother speaking)",
                "sound_component": "兄 (xiōng / phonetic connection)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water/ice radical 冫 beside elder brother 兄; originally cold river conditions, extended to state of affairs and rhetorical comparison.",
                "visual_mnemonic_story_en": "An elder brother (兄) assessing freezing ice conditions (冫) to explain a further situation (况).",
                "visual_mnemonic_story_es": "El hermano mayor (兄) comprobando la escarcha helada (冫) para valorar la situación (况).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EMRU",
                "traditional": "況"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Asking why (何) about an already obvious condition (况) introduces a further reason: let alone (何况).",
            "composite_memory_hook_es": "Preguntar el porqué (何) sobre una evidencia obvia (况) sirve para recalcar con mayor motivo (何况).",
            "cultural_and_cognitive_roots": "A cornerstone logical conjunction in classical Chinese argumentation (况且/何况) used to reinforce a conclusion a fortiori.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'hé kuàng' (35-51). Smooth upward glide on 'hé' followed by crisp fall on 'kuàng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "何", "pinyin": "hé", "meaning_en": "what; how", "distinction_note": "Person radical 亻 on left with 可"},
                {"character": "河", "pinyin": "hé", "meaning_en": "river", "distinction_note": "Water radical 氵 on left"},
                {"character": "况", "pinyin": "kuàng", "meaning_en": "situation; moreover", "distinction_note": "Ice radical 冫 on left with 兄"},
                {"character": "祝", "pinyin": "zhù", "meaning_en": "wish; pray", "distinction_note": "Altard radical 礻 on left with 兄"}
            ],
            "etymological_cognates": [
                {"character": "且", "pinyin": "qiě", "gloss_en": "furthermore; moreover"},
                {"character": "兼", "pinyin": "jiān", "gloss_en": "simultaneously; combine"},
                {"character": "更", "pinyin": "gèng", "gloss_en": "even more; further"},
                {"character": "况", "pinyin": "kuàng", "gloss_en": "circumstance; moreover"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "何况 introduces an a fortiori argument highlighting an even stronger, more obvious factor.",
            "contrasts": [
                {"id": 1, "compared_word": "何况 vs. 况且", "pinyin": "kuàngqiě", "analysis": "况且 adds a supplementary parallel reason (今天很冷，况且下雨), while 何况 is primarily used in rhetorical '尚且……何况……' contrastive logic."},
                {"id": 2, "compared_word": "何况 vs. 甚至", "pinyin": "shènzhì", "analysis": "甚至 emphasizes an extreme surprising example (连老人甚至婴儿), whereas 何况 introduces an obvious deduced truth."},
                {"id": 3, "compared_word": "何况 vs. 反而", "pinyin": "fǎn'ér", "analysis": "反而 indicates an outcome contrary to expectations, whereas 何况 deepens the expected gradient."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古人讲‘穷则独善其身，达则兼济天下’。普通百姓在困窘之时尚且恪守廉洁良知，不为非分之财所动，何况身为执掌公共权柄的官员，更当常思民生疾苦，以如履薄冰之心坚守清正廉明的政德底线。",
                "pinyin": "Gǔrén jiǎng 'qióng zé dú shàn qí shēn, dá zé jiān jì tiānxià'. Pǔtōng bǎixìng zài kùnjiǒng zhī shí shàngqiě kèshǒu liánjié liángzhī, bù wéi fēifèn zhī cái suǒ dòng, hékuàng shēnwéi zhízhǎng gōnggòng quánbǐng de guānyuán, gèng dāng cháng sī mínshēng jíkǔ, yǐ rúlǚ-bóbīng zhī xīn jiānshǒu qīngzhèng-liánmíng de zhèngdé dǐxiàn.",
                "en": "The ancients noted that when poor, one should perfect oneself; when prosperous, help all under heaven. If ordinary folks preserve integrity in hardship, all the more should officials holding public power guard incorruptibility.",
                "es": "Decían los antiguos: en la estrechez, cultiva la virtud; en la holgura, ampara al mundo. Si el pueblo humilde guarda su honradez, cuánto más los gobernantes deben velar con probidad por el bienestar común."
            },
            {
                "id": "#2",
                "hanzi": "在早期篮球比赛中，让两队队员干等着取球已经令人难以忍受，何况看台上还坐着满怀期待的热情球迷。这种漫长的停顿不仅打断了比赛的顺畅节奏，更让场馆里原本激烈的对抗气氛彻底降至冰点。正是这种多方共有的困扰，推动了规则的大胆革新。",
                "pinyin": "Zài zǎoqī lánqiú bǐsài zhōng, ràng liǎng duì duìyuán gān děng zhe qǔ qiú yǐjīng lìngrén nányǐ rěnshòu, hékuàng kàntái shang hái zuò zhe mǎnhuái qīdài de rèqíng qiúmí. Zhè zhǒng màncháng de tíngdùn bùjǐn dǎduàn le bǐsài de shùnchàng jiézòu, gèng ràng chǎngguǎn lǐ yuánběn jīliè de duìkàng qìfēn chèdǐ jiàng zhì bīngdiǎn. Zhèng shì zhè zhǒng duōfāng gòngyǒu de kùnrǎo, tuīdòng le guīzé de dàdǎn géxīn.",
                "en": "In early basketball, forcing both teams to stand waiting for the ball was already unbearable, let alone having passionate fans sitting in the stands. The long delay broke game rhythm and froze court excitement, impelling a bold rule revolution.",
                "es": "Hacer esperar a los jugadores tras cada canasta era insufrible, cuánto más con la grada llena de entusiastas aficionados. Esa demora rompía la fluidez congelando el fervor, propiciando una audaz reforma reglamentaria."
            }
        ]
    },

    # 22 球迷
    {
        "id": "22",
        "hanzi": "球迷",
        "pinyin": "qiú mí",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "ball game fan; soccer/basketball enthusiast",
            "es": "aficionado al fútbol/baloncesto; fanático de la pelota"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a passionate enthusiast and supporter of ball sports such as football, basketball, or tennis",
                "definition_es": "persona apasionada seguidora de deportes de pelota como fútbol o baloncesto",
                "example_phrase": "狂热的足球迷 (a fanatical soccer fan)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "当主队在补时阶段攻入绝杀进球时，看台上数万名狂热的球迷激动得热泪盈眶并高声欢呼。",
                "pinyin": "Dāng zhǔduì zài bǔshí jiēduàn gōngrù juéshā jìnqiú shí, kàntái shang shùwàn míng kuángrè de qiúmí jīdòng de rèlèi-yíngkuàng bìng gāoshēng huānhū.",
                "en": "When the home team netted the buzzer-beating winning goal in stoppage time, tens of thousands of fervent fans on the stands cheered with tears in their eyes.",
                "es": "Al anotar el equipo local el gol del triunfo en el descuento, decenas de miles de hinchas en las gradas rompieron a llorar de emoción y a vitorear."
            },
            {
                "id": "#2",
                "hanzi": "虽然今晚下着滂沱大雨，但依然有许多忠实球迷早早守候在体育馆外等待与球星签名合影。",
                "pinyin": "Suīrán jīnwǎn xià zhe pángtuó dàyǔ, dàn yīrán yǒu xǔduō zhōngshí qiúmí zǎozǎo shǒuhòu zài tǐyùguǎn wài děngdài yǔ qiúxīng qiānmíng héyǐng.",
                "en": "Despite pouring rain tonight, many devoted fans waited outside the arena early for autographs and photos with sports stars.",
                "es": "Pese al diluvio de esta noche, numerosos aficionados leales aguardaron ante el pabellón para conseguir autógrafos de sus ídolos."
            }
        ],
        "collocations": [
            {"hanzi": "忠实球迷", "en": "loyal ball fan"},
            {"hanzi": "狂热球迷", "en": "fanatical enthusiast"},
            {"hanzi": "资深球迷", "en": "veteran sports fan"},
            {"hanzi": "篮球迷", "en": "basketball fan"},
            {"hanzi": "足球迷", "en": "soccer fan"},
            {"hanzi": "球迷见面会", "en": "fan meet-and-greet event"}
        ],
        "idioms": [
            {"hanzi": "如醉如痴", "pinyin": "rú zuì rú chī", "meaning_en": "entranced and infatuated; utterly spellbound"},
            {"hanzi": "万人空巷", "pinyin": "wàn rén kōng xiàng", "meaning_en": "the whole town empties out to celebrate an event"},
            {"hanzi": "助威呐喊", "pinyin": "zhù wēi nà hǎn", "meaning_en": "shout encouragement and cheer loudly"},
            {"hanzi": "热火朝天", "pinyin": "rè huǒ cháo tiān", "meaning_en": "seething with fiery enthusiasm; buzzing activity"}
        ],
        "character_decomposition": [
            {
                "character": "球",
                "pinyin": "qiú",
                "meaning_en": "ball; sphere; globe; orb",
                "meaning_es": "pelota; balón; esfera; globo",
                "radical": "王",
                "radical_meaning_en": "jade / king",
                "meaning_component": "王 (jade stone / precious gem) + 求 (fur coat / curling)",
                "sound_component": "求 (qiú / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Jade radical 王 beside 求; originally a fine round jade sphere, extended to modern sports spheres and balls.",
                "visual_mnemonic_story_en": "A precious polished jade sphere (王) bouncing smoothly like a ball (球).",
                "visual_mnemonic_story_es": "Una preciosa piedra de jade pulida en esfera redonda (王) que bota como una pelota (球).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MGIJE",
                "traditional": "球"
            },
            {
                "character": "迷",
                "pinyin": "mí",
                "meaning_en": "fan; enthusiast; enchant; lost",
                "meaning_es": "aficionado; cautivado; perderse",
                "radical": "辶",
                "radical_meaning_en": "movement",
                "meaning_component": "辶 (wandering movement) + 米 (dispersed grains)",
                "sound_component": "米 (mǐ / phonetic association)",
                "stroke_count": 9,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Movement radical 辶 with scattered grain 米; wandering captivated in confusing paths, extended to passionate obsession.",
                "visual_mnemonic_story_en": "Following scattered trails of rice grains (米) along winding paths (辶) in passionate fascination (迷).",
                "visual_mnemonic_story_es": "Seguir senderos de granos de arroz (米) absorto en el camino (辶) entregado a la pasión (迷).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YFD",
                "traditional": "迷"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "One who is utterly fascinated (迷) by the bouncing ball (球) is a true sports fan (球迷).",
            "composite_memory_hook_es": "Quien se siente cautivado (迷) por el movimiento del balón (球) es un verdadero aficionado (球迷).",
            "cultural_and_cognitive_roots": "The suffix '迷' denotes avid passion or enthusiasts (歌迷 fan of singing, 影迷 movie buff, 球迷 sports fan).",
            "tone_sandhi_and_pitch_modulation": "Two rising second tones: 'qiú mí' (35-35). Both rise in pitch with smooth vocal energy."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "球", "pinyin": "qiú", "meaning_en": "ball; globe", "distinction_note": "Jade radical 王 on left with 求"},
                {"character": "救", "pinyin": "jiù", "meaning_en": "rescue; save", "distinction_note": "Has 求 on left with 攵 (tap) on right"},
                {"character": "迷", "pinyin": "mí", "meaning_en": "fan; lost", "distinction_note": "Movement radical 辶 at bottom of 米"},
                {"character": "谜", "pinyin": "mí", "meaning_en": "riddle; puzzle", "distinction_note": "Speech radical 讠 on left of 迷"}
            ],
            "etymological_cognates": [
                {"character": "粉", "pinyin": "fěn", "gloss_en": "powder; fan (slang)"},
                {"character": "友", "pinyin": "yǒu", "gloss_en": "friend; companion"},
                {"character": "众", "pinyin": "zhòng", "gloss_en": "crowd; spectators"},
                {"character": "徒", "pinyin": "tú", "gloss_en": "disciple; follower"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "球迷 specifically designates dedicated fans or followers of ball-related athletic sports.",
            "contrasts": [
                {"id": 1, "compared_word": "球迷 vs. 观众", "pinyin": "guānzhòng", "analysis": "观众 refers broadly to any passive audience member watching a show, whereas 球迷 implies emotional attachment to a ball club."},
                {"id": 2, "compared_word": "球迷 vs. 粉丝", "pinyin": "fěnsī", "analysis": "粉丝 is a generic modern umbrella term for celebrity/pop fans, while 球迷 is specialized for sporting ball events."},
                {"id": 3, "compared_word": "球迷 vs. 队员", "pinyin": "duìyuán", "analysis": "队员 is an active roster athlete playing on the court, while 球迷 supports from the bleachers."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "看台上的球迷是球场上无可争议的第十二人。无论是在球队遭遇连败的至暗低谷，还是在问鼎冠军的荣耀时刻，那面迎风飘扬的俱乐部巨幅旗帜下，始终汇聚着最执着真诚的掌声与最滚烫炽热的呐喊。",
                "pinyin": "Kàntái shang de qiúmí shì qiúchǎng shang wúkě-zhēngyì de dì-shí'èr rén. Wúlùn shì zài qiúduì zāoyù liánbài de zhì'àn dīgǔ, háishì zài wèndǐng guànjūn de róngyào shíkè, nà miàn yíngfēng piāoyáng de jùlébù jùfú qízhì xià, shǐzhōng huìjù zhe zuì zhízhuó zhēnchéng de zhǎngshēng yǔ zuì gǔntàng chìrè de nàhǎn.",
                "en": "Fans in the stands are indisputably the team's twelfth player. Whether during dark losing streaks or crowning championship glory, under the massive fluttering club banner gathers the most devoted applause and fiery roar.",
                "es": "La hinchada en la grada es el jugador número doce. Tanto en las derrotas más dolorosas como al alzar el trofeo, bajo la ondeante pancarta del club resuenan siempre los aplausos más leales y los cánticos más fervorosos."
            },
            {
                "id": "#2",
                "hanzi": "早年在春田学院，看台上坐满了年轻球迷。每当有人投篮入筐，大家刚想喝彩，比赛却因慢吞吞搬梯取球而叫停。为了不辜负球迷的观赛热情，工匠毅然用锯子开掉筐底，赋予了篮球运动极其流畅的竞技节奏。",
                "pinyin": "Zǎonián zài Chūntián xuéyuàn, kàntái shang zuòmǎn le niánqīng qiúmí. Měidāng yǒurén tóulán rù kuāng, dàjiā gāng xiǎng hècǎi, bǐsài què yīn màntūntūn bān tī qǔ qiú ér jiàotíng. Wèile bù gūfù qiúmí de guānsài rèqíng, gōngjiàng yìrán yòng jùzi kāi diào kuāngdǐ, fùyǔ le lánqiú yùndòng jíqí liúchàng de jìngjì jiézòu.",
                "en": "At Springfield College, stands were filled with young fans. Whenever a basket was scored, play was halted while ladders were dragged out. To satisfy fan passion, craftsmen sawed off the bottoms, gifting basketball a delightfully fluid rhythm.",
                "es": "En Springfield, las gradas rebosaban de jóvenes hinchas. Al encestar, el juego paraba para traer la escalera. Para no defraudar a la afición, los conserjes serraron el fondo, dotando al baloncesto de un ritmo trepidante."
            }
        ]
    },

    # 23 工程师
    {
        "id": "23",
        "hanzi": "工程师",
        "pinyin": "gōng chéng shī",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "engineer (professional technical designer)",
            "es": "ingeniero; técnica/o superior"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person trained in the design, construction, and use of engines, machines, software, or structures",
                "definition_es": "profesional cualificado que aplica principios científicos para diseñar, construir y operar obras, máquinas o programas",
                "example_phrase": "资深软件架构工程师 (senior software architect engineer)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "桥梁工程师和施工人员在悬崖深谷间连续奋战了数月，终于成功合龙了这座特大悬索桥。",
                "pinyin": "Qiáoliáng gōngchéngshī hé shīgōng rényuán zài xuányá shēngǔ jiān liánxù fènzhàn le shù yuè, zhōngyú chénggōng hélóng le zhè zuò tìdà xuánsuǒqiáo.",
                "en": "Bridge engineers and construction workers fought for months across the deep cliffside chasm, finally joining the spans of this mega suspension bridge.",
                "es": "Los ingenieros de puentes y operarios bregaron durante meses en el desfiladero hasta completar el ensamblaje final del monumental puente colgante."
            },
            {
                "id": "#2",
                "hanzi": "优秀的航空工程师在设计客机外壳时，对每一个部件的气动阻力都进行了极为精密严苛的模拟风洞计算。",
                "pinyin": "Yōuxiù de hángkōng gōngchéngshī zài shèjì kèjī wàiké shí, duì měi yí ge bùjiàn de qìdòng zǔlì dōu jìnxíng le jíwéi jīngmì yánkē de mónǐ fēngdòng jìsuàn.",
                "en": "Distinguished aeronautical engineers perform rigorous wind-tunnel simulations on the aerodynamic drag of every component when designing passenger planes.",
                "es": "Los ingenieros aeronáuticos realizan rigurosos cálculos aerodinámicos en túneles de viento para optimizar cada pieza del fuselaje."
            }
        ],
        "collocations": [
            {"hanzi": "总工程师", "en": "chief engineer"},
            {"hanzi": "软件工程师", "en": "software engineer"},
            {"hanzi": "建筑工程师", "en": "civil / structural engineer"},
            {"hanzi": "机械工程师", "en": "mechanical engineer"},
            {"hanzi": "助理工程师", "en": "assistant engineer"},
            {"hanzi": "高级工程师", "en": "senior engineer"}
        ],
        "idioms": [
            {"hanzi": "匠心独运", "pinyin": "jiàng xīn dú yùn", "meaning_en": "displaying wonderful ingenuity; singular craftsmanship"},
            {"hanzi": "精雕细刻", "pinyin": "jīng diāo xì kè", "meaning_en": "carve with fine precision; meticulous craftsmanship"},
            {"hanzi": "开山架桥", "pinyin": "kāi shān jià qiáo", "meaning_en": "level mountains and build bridges; clear obstacles boldly"},
            {"hanzi": "革故鼎新", "pinyin": "gé gù dǐng xīn", "meaning_en": "overthrow the old and usher in the new; innovate boldly"}
        ],
        "character_decomposition": [
            {
                "character": "工",
                "pinyin": "gōng",
                "meaning_en": "work; craft; engineering",
                "meaning_es": "obra; técnica; ingeniería",
                "radical": "工",
                "radical_meaning_en": "work / craft",
                "meaning_component": "carpenter's plumb square",
                "sound_component": "工 (gōng)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A carpenter's square tool; represents engineering, craftsmanship, and structured construction.",
                "visual_mnemonic_story_en": "A carpenter's level square (工) measuring structural angles for precision craft.",
                "visual_mnemonic_story_es": "Una escuadra de carpintero (工) guiando trazos precisos en la construcción.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "M",
                "traditional": "工"
            },
            {
                "character": "程",
                "pinyin": "chéng",
                "meaning_en": "order; rule; measure; journey",
                "meaning_es": "proceso; medida; trayecto",
                "radical": "禾",
                "radical_meaning_en": "grain",
                "meaning_component": "禾 (grain measurement) + 呈 (display / present)",
                "sound_component": "呈 (chéng / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Grain radical 禾 beside 呈; weighing grain standards to establish official measurement rules and systematic workflows.",
                "visual_mnemonic_story_en": "Weighing stalks of golden grain (禾) on an official presentation tray (呈) to establish orderly standards (程).",
                "visual_mnemonic_story_es": "Pesar espigas de cereal (禾) en una balanza oficial (呈) fijando normas metódicas (程).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HDRHG",
                "traditional": "程"
            },
            {
                "character": "师",
                "pinyin": "shī",
                "meaning_en": "master; teacher; expert; army",
                "meaning_es": "maestro; perito; experto",
                "radical": "巾",
                "radical_meaning_en": "cloth / towel",
                "meaning_component": "帀 (circling troops banner) + 巾 (standard cloth)",
                "sound_component": "师 (shī)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A commander holding military banners before troops; evolved into revered masters, mentors, and certified professionals.",
                "visual_mnemonic_story_en": "A revered master raising the banner of knowledge (巾) to instruct apprentices (师).",
                "visual_mnemonic_story_es": "Un maestro que alza el estandarte de la pericia (巾) guiando a sus discípulos (师).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "HLMLB",
                "traditional": "師"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A master (师) who applies technical standards (程) to construction works (工) is a qualified engineer (工程师).",
            "composite_memory_hook_es": "Un perito acreditado (师) que aplica procesos metódicos (程) a las obras (工) es un ingeniero (工程师).",
            "cultural_and_cognitive_roots": "Title combining modern technical methodology with historical reverence for masters of craft (师徒制).",
            "tone_sandhi_and_pitch_modulation": "Three syllables: 'gōng chéng shī' (55-35-55). High level tone on 'gōng', rising on 'chéng', and sustaining high on 'shī'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "程", "pinyin": "chéng", "meaning_en": "order; journey", "distinction_note": "Grain radical 禾 on left with 呈"},
                {"character": "呈", "pinyin": "chéng", "meaning_en": "present; display", "distinction_note": "Without the grain radical on left"},
                {"character": "师", "pinyin": "shī", "meaning_en": "master; teacher", "distinction_note": "Has 刂-like vertical and 巾"},
                {"character": "帅", "pinyin": "shuài", "meaning_en": "commander; handsome", "distinction_note": "Has a top stroke  丿 on left"}
            ],
            "etymological_cognates": [
                {"character": "工", "pinyin": "gōng", "gloss_en": "worker; artisan"},
                {"character": "匠", "pinyin": "jiàng", "gloss_en": "craftsman; artisan"},
                {"character": "家", "pinyin": "jiā", "gloss_en": "specialist; expert"},
                {"character": "员", "pinyin": "yuán", "gloss_en": "member; personnel"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "工程师 denotes an educated professional applying science and mathematics to practical design and systems.",
            "contrasts": [
                {"id": 1, "compared_word": "工程师 vs. 工人", "pinyin": "gōngrén", "analysis": "工人 denotes manual labor execution on the production line, while 工程师 formulates blueprints, software architectures, and mathematical designs."},
                {"id": 2, "compared_word": "工程师 vs. 科学家", "pinyin": "kēxuéjiā", "analysis": "科学家 pursues pure theoretical truth and discovery, whereas 工程师 translates those scientific discoveries into functional commercial products."},
                {"id": 3, "compared_word": "工程师 vs. 技师", "pinyin": "jìshī", "analysis": "技师 focuses on practical operational maintenance and machine adjustment, while 工程师 oversees systemic system design."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "航天工程师团队在深空探测领域攻坚克难。他们凭借务实的科学作风与精益求精的工匠情怀，将探测器精准送达预定轨道，让飞天梦想在浩瀚星空中璀璨绽放。",
                "pinyin": "Hángtiān gōngchéngshī tuánduì zài shēnkōng tàncè lǐngyù gōngjiān-kènán. Tāmen píngjiè wùshí de kēxué zuòfēng yǔ jīngyìqiújīng de gōngjiàng qínghuái, jiāng tàncèqì jīngzhǔn sòngdá yùdìng guǐdào, ràng fēitiān mèngxiǎng zài hàohàn xīngkōng zhōng cuǐcàn zhànfàng.",
                "en": "Aerospace engineers have overcome challenges in deep space exploration. With scientific pragmatism and meticulous craftsmanship, they delivered orbiters onto precision paths, realizing ancient dreams.",
                "es": "Los ingenieros aeroespaciales superaron grandes hitos espaciales. Con rigor pragmático y esmero artesanal, situaron las sondas en órbita con precisión, materializando el sueño de surcar el cosmos."
            },
            {
                "id": "#2",
                "hanzi": "面对取球难题，工程师起初设计了复杂的滑轮装置试图倾倒皮球。然而实践证明，精密图纸反倒不如一把普通锯子直截了当。顶尖的工程智慧，恰恰体现在大道至简之中。",
                "pinyin": "Miànduì qǔ qiú nántí, gōngchéngshī qǐchū shèjì le fùzá de huálún zhuāngzhì shìtú qīngdào píqiú. Rán'ér shíjiàn zhèngmíng, jīngmì túzhǐ fǎndào bùrú yì bǎ pǔtōng jùzi zhíjié-liǎodàng. Dǐngjiān de gōngchéng zhìhuì, qiàqià tǐxiàn zài dàdào-zhìjiǎn zhīzhōng.",
                "en": "Faced with extracting balls, engineers initially devised complex pulleys to tilt baskets. Yet practice proved intricate designs inferior to an ordinary saw. Supreme engineering brilliance lies in radical simplicity.",
                "es": "Para vaciar las canastas, los ingenieros idearon poleas complejas. Mas la práctica demostró que una modesta sierra superaba a planos sofisticados. La verdadera maestría técnica reside en la sencillez."
            }
        ]
    },

    # 24 机器
    {
        "id": "24",
        "hanzi": "机器",
        "pinyin": "jī qì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "machine; apparatus; mechanical device",
            "es": "máquina; aparato; ingenio mecánico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an apparatus using mechanical power and having several parts, each with a definite function and together performing a particular task",
                "definition_es": "conjunto de piezas acopladas que transforma energía para realizar un trabajo mecánico o productivo",
                "example_phrase": "运转正常的生产机器 (smoothly operating production machines)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "全自动数控车间里的数十台精密机器高速运转，有条不紊地加工着微型芯片组件。",
                "pinyin": "Quán zìdòng shùkòng chējiān lǐ de shùshí tái jīngmì jīqì gāosù yùnzhuǎn, yǒutiáo-bùwěn de jiāgōng zhe wēixíng xīnpìan zǔjiàn.",
                "en": "Dozens of high-precision machines in the automated CNC workshop ran at high speed, processing miniature microchip components with meticulous order.",
                "es": "En la nave de mecanizado automatizado, decenas de máquinas de precisión giraban a gran velocidad procesando microcomponentes con orden perfecto."
            },
            {
                "id": "#2",
                "hanzi": "人类发明机器的初衷是为了把双手从繁重危险的体力劳动中解放出来，从而追求更有创造力的精神生活。",
                "pinyin": "Rénlèi fāmíng jīqì de chūzhōng shì wèile bǎ shuāngshǒu cóng fánzhòng wēixiǎn de tǐlì láodòng zhōng jiěfàng chūlái, cóng'ér zhuīqiú gèng yǒu chuàngzàolì de jīngshén shēnghuó.",
                "en": "Humanity's initial purpose in inventing machines was to liberate hands from grueling, hazardous physical toil, thus enabling more creative pursuits.",
                "es": "La humanidad inventó las máquinas para liberar sus manos del trabajo físico penoso y peligroso, abriendo cauce a una vida intelectual más fecunda."
            }
        ],
        "collocations": [
            {"hanzi": "运转机器", "en": "operate / run a machine"},
            {"hanzi": "机器故障", "en": "machine breakdown / malfunction"},
            {"hanzi": "维修机器", "en": "repair machinery"},
            {"hanzi": "精密机器", "en": "precision machine"},
            {"hanzi": "机器人", "en": "robot"},
            {"hanzi": "机器制造", "en": "machine manufacturing"}
        ],
        "idioms": [
            {"hanzi": "神工鬼斧", "pinyin": "shén gōng guǐ fǔ", "meaning_en": "superhuman craft and divine axes; miraculous craftsmanship"},
            {"hanzi": "脱胎换骨", "pinyin": "tuō tāi huàn gǔ", "meaning_en": "shed old body and bone; thorough transformation"},
            {"hanzi": "一日千里", "pinyin": "yī rì qiān lǐ", "meaning_en": "advance a thousand miles a day; meteoric progress"},
            {"hanzi": "生机勃勃", "pinyin": "shēng jī bó bó", "meaning_en": "full of vibrant vigor and surging vitality"}
        ],
        "character_decomposition": [
            {
                "character": "机",
                "pinyin": "jī",
                "meaning_en": "machine; mechanism; opportunity",
                "meaning_es": "máquina; mecanismo; ocasión",
                "radical": "木",
                "radical_meaning_en": "tree / wood",
                "meaning_component": "木 (wooden loom / frame) + 几 (small stool; phonetic)",
                "sound_component": "几 (jī / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tree radical 木 beside 几; originally the wooden trigger mechanism of a crossbow or a weaving loom.",
                "visual_mnemonic_story_en": "A wooden loom frame (木) resting by a small stool (几), forming a weaving mechanism (机).",
                "visual_mnemonic_story_es": "El bastidor de madera de un telar (木) junto a un banquito (几), formando un mecanismo tejedor (机).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DHN",
                "traditional": "機"
            },
            {
                "character": "器",
                "pinyin": "qì",
                "meaning_en": "vessel; utensil; organ; instrument",
                "meaning_es": "recipiente; utensilio; aparato",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "four 口 (four vessels/dishes) surrounding 犬 (watchdog)",
                "sound_component": "器 (qì)",
                "stroke_count": 16,
                "composition_type": "上中下结构",
                "etymology_and_mnemonic": "Four mouth radicals 口 representing diverse vessels guarded by a dog 犬; broad category of utensils, gear, and manufactured devices.",
                "visual_mnemonic_story_en": "Four valuable bronze vessels (口) guarded vigilantly by a faithful dog (犬) in the treasure hall (器).",
                "visual_mnemonic_story_es": "Cuatro valiosas vasijas ceremoniales (口) guardadas con celo por un perro (犬) en la sala (器).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "RROIK",
                "traditional": "器"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Mechanical moving mechanisms (机) combined with manufactured instruments (器) constitute a machine (机器).",
            "composite_memory_hook_es": "Los mecanismos móviles (机) ensamblados en un aparato funcional (器) componen una máquina (机器).",
            "cultural_and_cognitive_roots": "Crossbow triggers (弩机) and silk weaving looms (织机) served as ancient China's prototypical automated machines.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling fourth tone: 'jī qì' (55-51). Hold 'jī' at a clear high register, then drop sharply on 'qì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "机", "pinyin": "jī", "meaning_en": "machine; engine", "distinction_note": "Wood radical 木 on left with 几"},
                {"character": "几", "pinyin": "jǐ/jī", "meaning_en": "how many; small table", "distinction_note": "Without the wood radical"},
                {"character": "器", "pinyin": "qì", "meaning_en": "utensil; machine", "distinction_note": "Has four 口 around 犬 in center"},
                {"character": "哭", "pinyin": "kū", "meaning_en": "weep; cry", "distinction_note": "Has only two 口 on top over 犬"}
            ],
            "etymological_cognates": [
                {"character": "械", "pinyin": "xiè", "gloss_en": "machinery; implement"},
                {"character": "具", "pinyin": "jù", "gloss_en": "tool; equipment"},
                {"character": "设", "pinyin": "shè", "gloss_en": "install; devise"},
                {"character": "备", "pinyin": "bèi", "gloss_en": "prepare; equipment"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "机器 denotes power-driven mechanisms with coordinated moving parts executing work.",
            "contrasts": [
                {"id": 1, "compared_word": "机器 vs. 工具", "pinyin": "gōngjù", "analysis": "工具 denotes simple handheld manual implements (hammer, saw), while 机器 involves powered kinetic mechanisms."},
                {"id": 2, "compared_word": "机器 vs. 设备", "pinyin": "shèbèi", "analysis": "设备 encompasses installations, factory plant rooms, and complete setups, whereas 机器 is a specific motorized apparatus."},
                {"id": 3, "compared_word": "机器 vs. 仪器", "pinyin": "yíqì", "analysis": "仪器 is calibrated for analytical scientific testing and measurement, while 机器 performs mechanical power work."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "工业革命以蒸汽机器的应用为标志，重塑了社会生产形态。手工纺织被现代化工厂取代，轰鸣的机器不仅释放了生产力，更开启了波澜壮阔的城市化历史进程。",
                "pinyin": "Gōngyè gémìng yǐ zhēngqì jīqì de yìngyòng wéi biāozhì, chóngsù le shèhuì shēngchǎn xíngtài. Shǒugōng fǎngzhī bèi xiàndàihuà gōngchǎng qǔdài, hōngmíng de jīqì bùjǐn shìfàng le shēngchǎnlì, gèng kāiqǐ le bōlán-zhuàngkuò de chéngshìhuà lìshǐ jìnchéng.",
                "en": "The Industrial Revolution, marked by steam machines, reshaped production. Modern factories replaced manual mills; roaring machinery unchained productivity and launched rapid urbanization.",
                "es": "La Revolución Industrial, impulsada por la máquina de vapor, transformó la producción. Fábricas mecanizadas relevaron a telares; las máquinas desataron la productividad e impulsaron la urbanización."
            },
            {
                "id": "#2",
                "hanzi": "当年发明篮球时，学校没有任何现代化制造机器。面对每次投球后的繁琐取球障碍，人们没有耗费巨资研制复杂的取球机器，而是用一把普通锯子就轻而易举化解了难题。",
                "pinyin": "Dāngnián fāmíng lánqiú shí, xuéxiào méiyǒu rènhé xiàndàihuà zhìzào jīqì. Miànduì měicì tóu qiú hòu de fánsuǒ qǔ qiú zhàng'ài, rénmen méiyǒu hàofèi jùzī yánzhì fùzá de qǔ qiú jīqì, érshì yòng yì bǎ pǔtōng jùzi jiù qīng'éryǐjǔ huàjiě le nántí.",
                "en": "When basketball was invented, the school had no modern machinery. Faced with tedious ball extraction, rather than building complex automated machines, they solved it effortlessly with an ordinary saw.",
                "es": "Al crearse el baloncesto, la escuela no poseía maquinaria avanzada. Ante el tedio de recuperar balones, en vez de costosas máquinas automáticas, bastó una sencilla sierra para solventar el dilema."
            }
        ]
    },

    # 25 顺畅
    {
        "id": "25",
        "hanzi": "顺畅",
        "pinyin": "shùn chàng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "smooth; unhindered; fluent; unimpeded",
            "es": "fluido; despejado; expedito; sin trabas"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "flowing smoothly and continuously without obstruction or friction",
                "definition_es": "que fluye con facilidad y continuidad sin tropiezos, trabas ni interrupciones",
                "example_phrase": "道路交通十分顺畅 (road traffic is completely unimpeded and smooth)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过城市交管部门对早高峰路段的科学分流与信号灯智能优化，主干道交通变得非常顺畅。",
                "pinyin": "Jīngguò chéngshì jiāoguǎn bùmén duì zǎogāofēng lùduàn de kēxué fēnliú yǔ xìnhàodēng zhìnéng yōuhuà, zhǔgàndào jiāotōng biàn de fēicháng shùnchàng.",
                "en": "Through traffic authorities' diversion planning and intelligent light tuning during the morning rush hour, main thoroughfare traffic became exceedingly smooth.",
                "es": "Tras el desvío coordinado del tráfico y la sincronización semafórica en la hora punta, la circulación en la avenida principal discurrió con total fluidez."
            },
            {
                "id": "#2",
                "hanzi": "只有建立高效顺畅的跨部门沟通机制，企业才能在瞬息万变的市场竞争中快速响应客户需求。",
                "pinyin": "Zhǐyǒu jiànlì gāoxiào shùnchàng de kuà-bùmén gōutōng jīzhì, qǐyè cái néng zài shùnxī-wànbiàn de shìchǎng jìngzhēng zhōng kuàisù xiǎngyìng kèhù xūqiú.",
                "en": "Only by establishing an efficient and unhindered cross-departmental communication channel can an enterprise rapidly respond to clients amid volatile market competition.",
                "es": "Sólo forjando una comunicación interdepartamental ágil y fluida podrá la corporación responder con celeridad a las demandas del cambiante mercado."
            }
        ],
        "collocations": [
            {"hanzi": "交通顺畅", "en": "smooth, unhindered traffic"},
            {"hanzi": "呼吸顺畅", "en": "unobstructed, smooth breathing"},
            {"hanzi": "沟通顺畅", "en": "unimpeded communication"},
            {"hanzi": "流程顺畅", "en": "smooth workflow"},
            {"hanzi": "表达顺畅", "en": "fluent, smooth expression"},
            {"hanzi": "心情顺畅", "en": "cheerful, buoyant mood"}
        ],
        "idioms": [
            {"hanzi": "畅通无阻", "pinyin": "chàng tōng wú zǔ", "meaning_en": "unimpeded and clear; completely unblocked"},
            {"hanzi": "一帆风顺", "pinyin": "yī fān fēng shùn", "meaning_en": "smooth sailing all the way; plain sailing"},
            {"hanzi": "通达明辨", "pinyin": "tōng dá míng biàn", "meaning_en": "perceptive and articulate; clear-minded"},
            {"hanzi": "水到渠成", "pinyin": "shuǐ dào qú chéng", "meaning_en": "when water arrives the canal forms; natural spontaneous success"}
        ],
        "character_decomposition": [
            {
                "character": "顺",
                "pinyin": "shùn",
                "meaning_en": "along with; obedient; smooth",
                "meaning_es": "seguir; propicio; favorable",
                "radical": "川",
                "radical_meaning_en": "river",
                "meaning_component": "川 (smooth flowing river current) + 页 (head/face)",
                "sound_component": "川 (chuān / phonetic association)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Flowing river streams 川 beside head 页; tilting the head to align with natural river currents, symbolizing going with the flow.",
                "visual_mnemonic_story_en": "Turning one's head (页) to drift along the smooth river current (川) without fighting upstream (顺).",
                "visual_mnemonic_story_es": "Alinear la mirada (页) a favor de la corriente del río (川) dejándose llevar con fluidez (顺).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LLMBO",
                "traditional": "順"
            },
            {
                "character": "畅",
                "pinyin": "chàng",
                "meaning_en": "smooth; unimpeded; free; joyful",
                "meaning_es": "expedito; desahogado; contento",
                "radical": "申",
                "radical_meaning_en": "extend",
                "meaning_component": "申 (stretch / extend freely) + 𠮛 (sunshine / vital energy)",
                "sound_component": "𠮛 (yáng / bright expansion)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Expanding 申 under open sky; an unhindered opening through which life energy, fluids, or thoughts flow completely free.",
                "visual_mnemonic_story_en": "Life energy extending outward (申) under the sun without meeting any roadblocks (畅).",
                "visual_mnemonic_story_es": "La energía vital expandiéndose (申) libremente a cielo abierto sin ningún obstáculo (畅).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LNSH",
                "traditional": "暢"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Following smooth river currents (顺) to unhindered outward expansion (畅) describes an unblocked flow (顺畅).",
            "composite_memory_hook_es": "Navegar con la corriente favorable (顺) hacia una expansión libre de trabas (畅) es discurrir con fluidez (顺畅).",
            "cultural_and_cognitive_roots": "Derived from Daoist natural river metaphors where non-resistance (顺水推舟) yields maximum unobstructed grace.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'shùn chàng' (51-51). Deliver both syllables with clear downward momentum and confidence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "顺", "pinyin": "shùn", "meaning_en": "smooth; along", "distinction_note": "River 川 on left with 页 on right"},
                {"character": "须", "pinyin": "xū", "meaning_en": "must; beard", "distinction_note": "Has 彡 (three strokes) on left with 页"},
                {"character": "畅", "pinyin": "chàng", "meaning_en": "fluent; unimpeded", "distinction_note": "Has 申 on left with 𠮛 on right"},
                {"character": "扬", "pinyin": "yáng", "meaning_en": "raise; scatter", "distinction_note": "Hand radical 扌 on left of 𠮛"}
            ],
            "etymological_cognates": [
                {"character": "通", "pinyin": "tōng", "gloss_en": "pass through; clear"},
                {"character": "流", "pinyin": "liú", "gloss_en": "flow; drift"},
                {"character": "利", "pinyin": "lì", "gloss_en": "sharp; advantageous"},
                {"character": "滑", "pinyin": "huá", "gloss_en": "slippery; smooth"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "顺畅 emphasizes the unimpeded, friction-free movement of fluids, traffic, air, or processes.",
            "contrasts": [
                {"id": 1, "compared_word": "顺畅 vs. 流畅", "pinyin": "liúchàng", "analysis": "流畅 focuses on graceful stylistic elegance in speech, prose, or dance (文笔流畅), while 顺畅 focuses on lack of physical blockages (交通顺畅, 呼吸顺畅)."},
                {"id": 2, "compared_word": "顺畅 vs. 顺利", "pinyin": "shùnlì", "analysis": "顺利 denotes the favorable outcome of undertakings without mishap (工作顺利), whereas 顺畅 depicts kinetic passage."},
                {"id": 3, "compared_word": "顺畅 vs. 舒畅", "pinyin": "shūchàng", "analysis": "舒畅 exclusively describes internal subjective emotional ease and relief (心情舒畅), not physical traffic."},
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "晨雾散去后的滨海大道上，微咸的海风拂面而来。极目远眺，宽阔整洁的八车道路面上车流平稳有序、行进顺畅，两侧葱茏挺拔的椰子树在阳光下舒展枝叶，勾勒出一幅舒缓惬意的现代海滨都市生态画卷。",
                "pinyin": "Chénwù sànqù hòu de bīnhǎi dàdào shang, wēixián de hǎifēng fúmiàn ér lái. Jímù yuǎntiào, kuānkuò zhěngjié de bā chēdào lùmiàn shang chēliú píngwěn yǒuxù, xíngjìn shùnchàng, liǎngcè cōnglóng tǐngbá de yēzǐshù zài yángguāng xià shūzhǎn zhīyè, gōulè chū yì fú shūhuǎn qièyì de xiàndài hǎibīn dūshì shēngtài huàjuàn.",
                "en": "On the coastal boulevard after morning mists lifted, salty sea breezes caressed travelers. Eight lanes of traffic moved with smooth order while verdant coconut palms stretched in the sun, forming a restful coastal city panorama.",
                "es": "Disipada la niebla matinal en el paseo marítimo, la brisa marina rozaba el rostro. En la ancha calzada de ocho carriles, el tráfico fluía con suave compás mientras los cocoteros mecían sus palmas bajo el sol."
            },
            {
                "id": "#2",
                "hanzi": "当年篮球比赛之所以常常被球迷抱怨节奏拖沓，根源就在于缺乏顺畅的进球反馈机制。每次投篮得分都意味着一次人为的强制暂停，直到有人把竹筐底锯掉后，篮球才能在穿筐而过的刹那直接坠落回地面，比赛流程自此变得无比顺畅欢快。",
                "pinyin": "Dāngnián lánqiú bǐsài zhī suǒyǐ chángcháng bèi qiúmí bàoyuàn jiézòu tuōtà, gēnyuán jiù zàiyú quēfá shùnchàng de jìnqiú fǎnhuì jīzhì. Měicì tóulán défēn dōu yìwèizhe yí cì rénwéi de qiángzhì zàntíng, zhídào yǒurén bǎ zhúkuāng dǐ jù diào hòu, lánqiú cái néng zài chuān kuāng ér guò de chànà zhíjiē zhuìluò huí dìmbiàn, bǐsài liúchéng zìcǐ biàn de wúbǐ shùnchàng huānkuài.",
                "en": "Fans complained early basketball was sluggish because it lacked an unimpeded scoring cycle. Every basket forced a manual pause. Only when someone sawed open the bottom could the ball plunge directly to the court, transforming the entire game into an exhilarating, flowing delight.",
                "es": "Los hinchas criticaban la lentitud del baloncesto pionero por carecer de un ciclo fluido tras el enceste. Cada punto obligaba a parar el juego. Al serrar el fondo de la cesta, el balón cayó libremente al suelo, tornando el deporte en una fiesta ágil y continua."
            }
        ]
    },

    # 26 幼儿园
    {
        "id": "26",
        "hanzi": "幼儿园",
        "pinyin": "yòu 'ér yuán",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "kindergarten; preschool; nursery school",
            "es": "jardín de infancia; guardería; parvulario"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an educational establishment or day-care facility for children below the age of compulsory schooling (typically ages 3 to 6)",
                "definition_es": "institución educativa para niños de tres a seis años previa a la enseñanza primaria",
                "example_phrase": "把孩子送到附近的公立幼儿园 (send the child to a nearby public kindergarten)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每天清晨，这所国际双语幼儿园的塑胶操场上都会响起欢快活泼的儿歌和孩子们银铃般的笑声。",
                "pinyin": "Měitiān qīngchén, zhè suǒ guójì shuāngyǔ yòu'éryuán de sùjiāo cāochǎng shang dōu huì xiǎngqǐ huānkuài huópō de érgē hé háizimen yínlíng bān de xiàoshēng.",
                "en": "Every dawn, cheerful nursery rhymes and silvery children's laughter resonate across the synthetic playground of this international bilingual kindergarten.",
                "es": "Cada mañana, alegres rondas infantiles y risas cantadinas resuenan en el patio de juegos acolchado del jardín de infancia bilingüe."
            },
            {
                "id": "#2",
                "hanzi": "学前教育专家强调，幼儿园课程应当以启发好奇心和培养基本生活习惯为主，切不可过早超纲灌输应试知识。",
                "pinyin": "Xuéqián jiàoyù zhuānjiā qiángdiào, yòu'éryuán kèchéng yīngdāng yǐ qǐfā hàoqíxīn hé péiyǎng jīběn shēnghuó xíguàn wéi zhǔ, qiè bùkě guòzǎo chāogāng guànshū yìngshì zhīshi.",
                "en": "Early childhood education experts emphasize that kindergarten curricula should focus on inspiring curiosity and nurturing life habits, avoiding cramming academic tests.",
                "es": "Expertos en educación preescolar subrayan que el parvulario debe priorizar la curiosidad e higiene personal, evitando sobrecargar al niño con lecciones académicas."
            }
        ],
        "collocations": [
            {"hanzi": "上幼儿园", "en": "attend kindergarten"},
            {"hanzi": "公立幼儿园", "en": "public kindergarten"},
            {"hanzi": "私立幼儿园", "en": "private preschool / kindergarten"},
            {"hanzi": "幼儿园老师", "en": "kindergarten teacher"},
            {"hanzi": "幼儿园小朋友", "en": "kindergarten pupils"},
            {"hanzi": "双语幼儿园", "en": "bilingual nursery school"}
        ],
        "idioms": [
            {"hanzi": "欢声笑语", "pinyin": "huān shēng xiào yǔ", "meaning_en": "cheers and laughter; joyful atmosphere"},
            {"hanzi": "天真烂漫", "pinyin": "tiān zhēn làn màn", "meaning_en": "innocent, artless, and delightful like children"},
            {"hanzi": "童心未泯", "pinyin": "tóng xīn wèi mǐn", "meaning_en": "retaining child-like innocence into adulthood"},
            {"hanzi": "循循善诱", "pinyin": "xún xún shàn yòu", "meaning_en": "guide systematically and patiently with gentle teaching"}
        ],
        "character_decomposition": [
            {
                "character": "幼",
                "pinyin": "yòu",
                "meaning_en": "young; tender; infant",
                "meaning_es": "joven; tierno; párvulo",
                "radical": "幺",
                "radical_meaning_en": "tiny / small",
                "meaning_component": "幺 (tiny filament) + 力 (infant physical strength)",
                "sound_component": "幼 (yòu)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tiny 幺 beside strength 力; having only minute infant physical power, denoting tender young age.",
                "visual_mnemonic_story_en": "A tiny infant (幺) attempting to exert its little arm strength (力) as it learns to walk (幼).",
                "visual_mnemonic_story_es": "Un tierno bebé (幺) tratando de usar su escasa fuerza (力) al dar sus primeros pasos (幼).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VIKS",
                "traditional": "幼"
            },
            {
                "character": "儿",
                "pinyin": "ér",
                "meaning_en": "child; son; young person",
                "meaning_es": "niño; hijo; joven",
                "radical": "儿",
                "radical_meaning_en": "legs / person",
                "meaning_component": "pictograph of an infant with soft unclosed skull fontanelle and little legs",
                "sound_component": "儿 (ér)",
                "stroke_count": 2,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of an infant walking on two little legs, head fontanelle still soft.",
                "visual_mnemonic_story_en": "Two small legs (儿) toddling happily forward, the sweet sign of a growing child.",
                "visual_mnemonic_story_es": "Dos piernecitas (儿) correteando contentas, la viva imagen de un párvulo.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HU",
                "traditional": "兒"
            },
            {
                "character": "园",
                "pinyin": "yuán",
                "meaning_en": "garden; park; enclosed ground",
                "meaning_es": "jardín; huerto; parque",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (surrounding walled perimeter) + 元 (spacious first origin)",
                "sound_component": "元 (yuán / phonetic)",
                "stroke_count": 7,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "Enclosure 囗 surrounding 元; an enclosed garden plot for cultivating flowers, crops, or nurturing youngsters.",
                "visual_mnemonic_story_en": "A fenced protective courtyard (囗) where fruitful seeds take root and grow (元): a peaceful garden (园).",
                "visual_mnemonic_story_es": "Un recinto cerrado protector (囗) donde florecen brotes jóvenes (元): un bello jardín (园).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "WMMU",
                "traditional": "園"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A protective garden enclosure (园) nurturing tender young (幼) children (儿) is a kindergarten (幼儿园).",
            "composite_memory_hook_es": "Un jardín acogedor (园) que cobija y educa a niños (儿) de tierna edad (幼) es un parvulario (幼儿园).",
            "cultural_and_cognitive_roots": "Direct conceptual loan from Froebel's German 'Kindergarten' (children's garden), entered Chinese via late Qing reforms.",
            "tone_sandhi_and_pitch_modulation": "Three syllables: 'yòu 'ér yuán' (51-35-35). Falling fourth tone on 'yòu', followed by two rising second tones on ''ér' and 'yuán'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "幼", "pinyin": "yòu", "meaning_en": "young; tender", "distinction_note": "Has 幺 on left and 力 on right"},
                {"character": "幻", "pinyin": "huàn", "meaning_en": "fantasy; illusion", "distinction_note": "Has 幺 on left and 弓-like stroke on right"},
                {"character": "园", "pinyin": "yuán", "meaning_en": "garden", "distinction_note": "Enclosed 囗 with 元 inside"},
                {"character": "圆", "pinyin": "yuán", "meaning_en": "round; circle", "distinction_note": "Enclosed 囗 with 员 inside"}
            ],
            "etymological_cognates": [
                {"character": "托", "pinyin": "tuō", "gloss_en": "nursery; trust; support"},
                {"character": "童", "pinyin": "tóng", "gloss_en": "child; youthful"},
                {"character": "雏", "pinyin": "chú", "gloss_en": "chick; fledgling"},
                {"character": "苑", "pinyin": "yuàn", "gloss_en": "park; academic enclave"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "幼儿园 specifically denotes the pre-primary educational institution for children ages 3 to 6.",
            "contrasts": [
                {"id": 1, "compared_word": "幼儿园 vs. 托儿所", "pinyin": "tuō'érsuǒ", "analysis": "托儿所 (daycare / creche) accommodates infants and toddlers from birth to 3 years old primarily for care, while 幼儿园 provides structured pre-K education."},
                {"id": 2, "compared_word": "幼儿园 vs. 小学", "pinyin": "xiǎoxué", "analysis": "小学 (elementary school) enters compulsory grade curricula for ages 6 to 12, unlike playtime-based 幼儿园."},
                {"id": 3, "compared_word": "幼儿园 vs. 早教中心", "pinyin": "zǎojiào zhōngxīn", "analysis": "早教中心 provides specialized hourly parent-child developmental sessions, whereas 幼儿园 offers full-day pre-schooling."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "温暖的午后阳光透过树梢洒落在幼儿园的花园草坪上。老师正带着一群扎着羊角辫的孩子们围坐成圆圈做趣味游戏。孩子们清脆纯真的笑声在微风中飘荡，那一双双澄澈无暇的大眼睛里，闪烁着对整个世界最初的奇妙向往。",
                "pinyin": "Wēnnuǎn de wǔhòu yángguāng tòuguò shùshāo sǎluò zài yòu'éryuán de huāyuán cǎopíng shang. Lǎoshī zhèng dài zhe yì qún zā zhe yángjiǎobiàn de háizimen wéizuò chéng yuánquān zuò qùwèi yóuxì. Háizimen qīngcuì chúnzhēn de xiàoshēng zài wēifēng zhōng piāodàng, nà yì shuāngshuāng chéngchè-wúxiá de dà yǎnjing lǐ, shǎnshuò zhe duì zhěnggè shìjiè zuìchū de qímiào xiàngwǎng.",
                "en": "Warm afternoon sunlight filtered through leaves onto the kindergarten lawn. The teacher gathered children in a circle for playful games. Pure laughter floated on the breeze; within their clear innocent eyes sparkled their very first wonders about the world.",
                "es": "El sol de la tarde bañaba el césped del jardín de infancia. La maestra jugaba en corro con los pequeños, cuyas risas cristalinas mecía la brisa. En sus ojos límpidos resplandecía el asombro inaugural ante la belleza del mundo."
            },
            {
                "id": "#2",
                "hanzi": "面对大人被繁琐规则困扰却束手无策的僵局，有时候恰恰是幼儿园里天真无邪的孩子，能以最直白的童眼看穿问题的本质。当年启发大家剪开竹筐底部的，正是一个路过球场的小朋友。孩子未经世俗教条规训的心智，往往蕴含着化繁为简的非凡创造力。",
                "pinyin": "Miànduì dàren bèi fánsuǒ guīzé kùnrǎo què shùshǒu-wúcè de jiāngjú, yǒushíhou qiàqià shì yòu'éryuán lǐ tiānzhēn-wúxié de háizi, néng yǐ zuì zhíbái de tóngyǎn kànchuān wèntí de běnzhì. Dāngnián qǐfā dàjiā jiǎn kāi zhúkuāng dǐbù de, zhèng shì yí ge lùguò qiúchǎng de xiǎopéngyou. Háizi wèijīng shìsú jiàotiáo guīxùn de xīnjiào, wǎngwǎng yùnhán zhe huà fán wéi jiǎn de fēifán chuàngzàolì.",
                "en": "When adults are bogged down by rules and paralyzed by overthinking, it is often an innocent kindergarten child who cuts straight to the core. The person who prompted everyone to cut open the basket bottoms was a passing kid. Unfettered minds harbor sublime creative breakthroughs.",
                "es": "Cuando los adultos se enredan en trabas burocráticas, a menudo es un parvulito inocente quien vislumbra la solución de raíz. Quien inspiró recortar el fondo de la canasta fue un niño que pasaba. La mente infantil sin prejuicios atesora una sublime creatividad."
            }
        ]
    },

    # 27 好奇
    {
        "id": "27",
        "hanzi": "好奇",
        "pinyin": "hào qí",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "curious; inquisitive; inquisitive interest",
            "es": "curioso; inquisitivo; afán de saber"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "eager to know or learn something new, unusual, or unexplained",
                "definition_es": "inclinado a conocer o averiguar cosas nuevas, raras o misteriosas",
                "example_phrase": "对大自然抱有强烈的好奇心 (possess intense curiosity about nature)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "那个年幼的孩子趴在草地旁，好奇地观察着成群结队的黑蚂蚁如何分工搬运沉重的面包屑。",
                "pinyin": "Nà ge niányòu de háizi pā zài cǎodì páng, hàoqí de guānchá zhe chéngqún-jiéduì de hēi mǎyǐ rúhé fēngōng bānyùn chénzhòng de miànbāoxiè.",
                "en": "Lying upon the grass, the young child curiously observed how marching black ants divided labor to transport heavy breadcrumbs.",
                "es": "Tumbado en la hierba, el niño observaba con viva curiosidad cómo las laboriosas hormigas se repartían el acarreo de las migajas de pan."
            },
            {
                "id": "#2",
                "hanzi": "保持对未知世界永不衰退的好奇与敬畏，是每一个真正科学家在漫长探索征途上最宝贵的动力源泉。",
                "pinyin": "Bǎochí duì wèizhī shìjiè yǒng bù shuāituì de hàoqí yǔ jìngwèi, shì měi yí ge zhēnzhèng kēxuéjiā zài màncháng tànsuǒ zhēngtú shang zuì bǎoguì de dònglì yuánquán.",
                "en": "Maintaining unfading curiosity and reverence toward the unknown is the most precious wellspring of motivation for any true scientist on the quest of discovery.",
                "es": "Preservar una curiosidad infatigable y reverencia ante lo ignoto constituye el motor más valioso de cualquier científico en su afán de saber."
            }
        ],
        "collocations": [
            {"hanzi": "好奇心", "en": "curiosity; inquisitive mind"},
            {"hanzi": "充满好奇", "en": "filled with curiosity"},
            {"hanzi": "感到好奇", "en": "feel curious about"},
            {"hanzi": "强烈的好奇", "en": "intense curiosity"},
            {"hanzi": "满足好奇心", "en": "satisfy one's curiosity"},
            {"hanzi": "好奇地打量", "en": "scrutinize curiously"}
        ],
        "idioms": [
            {"hanzi": "求知若渴", "pinyin": "qiú zhī ruò kě", "meaning_en": "thirsting for knowledge; eager intellectual yearning"},
            {"hanzi": "探幽索微", "pinyin": "tàn yōu suǒ wēi", "meaning_en": "probe deep mysteries and investigate subtleties"},
            {"hanzi": "别开生面", "pinyin": "bié kāi shēng miàn", "meaning_en": "break new ground; open up refreshing perspectives"},
            {"hanzi": "追本溯源", "pinyin": "zhuī běn sù yuán", "meaning_en": "trace back to the fountainhead; seek underlying origins"}
        ],
        "character_decomposition": [
            {
                "character": "好",
                "pinyin": "hào",
                "meaning_en": "fond of; like; love; eager for",
                "meaning_es": "aficionado a; amar; gustar",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (mother) + 子 (child embracing)",
                "sound_component": "好 (hào/hǎo)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Mother 女 holding her child 子 with deep affection; fourth-tone reading (hào) denotes being fond of or inclined toward.",
                "visual_mnemonic_story_en": "A loving mother (女) embracing her beloved child (子), fond of nurturing all that is good (好).",
                "visual_mnemonic_story_es": "Una madre abnegada (女) abrazando a su tierno hijo (子), inclinada a amar y aprender (好).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VND",
                "traditional": "好"
            },
            {
                "character": "奇",
                "pinyin": "qí",
                "meaning_en": "strange; rare; wonderful; novel",
                "meaning_es": "raro; asombroso; singular",
                "radical": "大",
                "radical_meaning_en": "big",
                "meaning_component": "大 (big / remarkable) + 可 (exclamation of approval)",
                "sound_component": "奇 (qí)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Remarkable person 大 above approved speech 可; something extraordinarily striking, rare, and novel.",
                "visual_mnemonic_story_en": "A person standing tall (大) exclaiming in astonishment (可) at a wondrous spectacle (奇).",
                "visual_mnemonic_story_es": "Un hombre con brazos abiertos (大) exclamando con asombro (可) ante un prodigio singular (奇).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "KMNR",
                "traditional": "奇"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Being intensely fond of (好) exploring the strange and wonderful (奇) makes you curious (好奇).",
            "composite_memory_hook_es": "Ser aficionado a (好) descubrir lo insólito y asombroso (奇) define a una persona curiosa (好奇).",
            "cultural_and_cognitive_roots": "Considered the prime catalyst of philosophical inquiry and scientific invention across Chinese intellectual traditions.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by rising second tone: 'hào qí' (51-35). Note fourth tone 'hào' (not third tone 'hǎo'), soaring upward on 'qí'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "奇", "pinyin": "qí", "meaning_en": "strange; wonderful", "distinction_note": "Big 大 on top over 可"},
                {"character": "夺", "pinyin": "duó", "meaning_en": "seize; snatch", "distinction_note": "Big 大 over 寸"},
                {"character": "寄", "pinyin": "jì", "meaning_en": "send; mail; lodge", "distinction_note": "Roof radical 宀 on top of 奇"},
                {"character": "椅", "pinyin": "yǐ", "meaning_en": "chair", "distinction_note": "Tree radical 木 on left of 奇"}
            ],
            "etymological_cognates": [
                {"character": "探", "pinyin": "tàn", "gloss_en": "explore; probe; spy"},
                {"character": "疑", "pinyin": "yí", "gloss_en": "doubt; suspect"},
                {"character": "问", "pinyin": "wèn", "gloss_en": "ask; inquire"},
                {"character": "异", "pinyin": "yì", "gloss_en": "different; extraordinary"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "好奇 denotes the psychological craving to investigate or understand novel and unfamiliar phenomena.",
            "contrasts": [
                {"id": 1, "compared_word": "好奇 vs. 奇怪", "pinyin": "qíguài", "analysis": "奇怪 is an objective descriptor meaning strange or bizarre (这件事很奇怪), while 好奇 describes a subjective mental state of inquiring eagerness (好奇心)."},
                {"id": 2, "compared_word": "好奇 vs. 关注", "pinyin": "guānzhù", "analysis": "关注 means paying close, serious ongoing attention to developments, whereas 好奇 can be whimsical and triggered by novelty."},
                {"id": 3, "compared_word": "好奇 vs. 猎奇", "pinyin": "lièqí", "analysis": "猎奇 carries derogatory connotations of sensationalist novelty-seeking, while 好奇 is healthy intellectual inquisitiveness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "爱因斯坦曾谦逊地写道：‘我并没有什么特殊的才能，我只是保持了无比强烈的好奇心。’正是对光线传播与时空奥秘那份孩童般纯粹的好奇，指引他在常人习以为常的自然规律深处，开创出颠覆近代物理学常识的相对论宏伟体系。",
                "pinyin": "Àiyīnsītǎn céng qiānxùn de xiědào: 'Wǒ bìng méiyǒu shénme tèshū de cáinéng, wǒ zhǐshì bǎochí le wúbǐ qiángliè de hàoqíxīn.' Zhèng shì duì guāngxiàn chuánbō yǔ shíkōng àomì nà fèn háitóng bān chúncuì de hàoqí, zhǐyǐn tā zài chángrén xíyǐwéicháng de zìrán guīlǜ shēnchù, kāichuàng chū diānfù jìndài wùlǐxué chángshí de xiāngduìlùn hóngwěi tǐxì.",
                "en": "Einstein humbly wrote: 'I have no special talent; I am only passionately curious.' It was pure curiosity about light and spacetime that guided him to unearth the revolutionary theory of relativity from ordinary natural laws.",
                "es": "Einstein admitió con humildad: 'No tengo talentos especiales, sólo una apasionada curiosidad'. Ese asombro infantil ante la luz y el cosmos le guió a formular la teoría de la relatividad revolucionando la física moderna."
            },
            {
                "id": "#2",
                "hanzi": "当年在篮球场边看比赛的孩子，之所以能打破工人们苦思冥想的僵局，恰恰在于他怀揣着一颗未受条框束缚的好奇心。他好奇人们为什么每次都要多此一举地搬梯子取球，正是这份敢于质疑常规的好奇与质朴发问，推开了现代体育创新的一扇大门。",
                "pinyin": "Dāngnián zài lánqiú chǎngbiān kàn bǐsài de háizi, zhī suǒyǐ néng dǎpò gōngrénmen kǔsī-míngxiǎng de jiāngjú, qiàqià zàiyú tā huáichuāi zhe yì kē wèishòu tiáokuāng shùfù de hàoqíxīn. Tā hàoqí rénmen wèishénme měicì dōu yào duōcǐyìjǔ de bān tīzi qǔ qiú, zhèng shì zhè fèn gǎnyú zhìyí chángguī de hàoqí yǔ zhípǔ fāwèn, tuīkāi le xiàndài tǐyù chuàngxīn de yí shàn dàmén.",
                "en": "The child by the court broke the adults' deadlock because he held uninhibited curiosity. He wondered why adults needlessly lugged ladders after every score. That candid curiosity questioning routine swung wide the doors to modern sports innovation.",
                "es": "El niño de la grada desbloqueó el dilema de los adultos gracias a su curiosidad sin ataduras. Le intrigaba por qué acarreaban escaleras en vano tras cada canasta; esa ingenua pregunta abrió las puertas a la innovación deportiva."
            }
        ]
    },

    # 28 何必
    {
        "id": "28",
        "hanzi": "何必",
        "pinyin": "hé bì",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "why should; there is no need; what is the point of",
            "es": "¿para qué?; ¿qué necesidad hay de...?; no es menester"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "used in rhetorical questions to emphasize that something is completely unnecessary or superfluous",
                "definition_es": "empleado en oraciones retóricas para indicar que algo resulta totalmente innecesario o redundante",
                "example_phrase": "何必为此大惊小怪呢 (why make such a fuss over this?)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "既然双方在主要商业合作条款上已经达成高度共识，又何必为了几个微不足道的细枝末节争执不休呢。",
                "pinyin": "Jìrán shuāngfāng zài zhǔyào shāngyè hézuò tiáokuǎn shang yǐjīng dáchéng gāodù gòngshí, yòu hébì wèile jǐ ge wēibùzúdào de xìzhī-mòjié zhēngzhí-bùxiū ne.",
                "en": "Since both sides have reached strong consensus on main business terms, why bother arguing endlessly over trifling trivialities?",
                "es": "Si ambas partes concuerdan en los términos sustanciales, ¿qué necesidad hay de disputar interminablemente por nimiedades secundarias?"
            },
            {
                "id": "#2",
                "hanzi": "人生苦短且岁月匆匆，我们何必整日为了过去的微小挫折耿耿于怀、自我消耗呢。",
                "pinyin": "Rénshēng kǔduǎn qiě suìyuè cōngcōng, wǒmen hébì zhěngrì wèile guòqù de wēixiǎo cuòzhé gěnggěng-yùhuái, zìwǒ xiāohào ne.",
                "en": "Life is brief and years slip swiftly by; why should we brood incessantly over past minor setbacks and consume ourselves in grief?",
                "es": "La vida es breve y los años fugaces; ¿para qué atormentarse y desgastarse a diario rumiando pequeños tropiezos del pasado?"
            }
        ],
        "collocations": [
            {"hanzi": "何必如此", "en": "why go so far; no need for this"},
            {"hanzi": "又何必", "en": "why should; there's even less need to"},
            {"hanzi": "何必介意", "en": "why take it to heart; don't mind"},
            {"hanzi": "何必当初", "en": "why act thus in the first place"},
            {"hanzi": "何必多此一举", "en": "why make an unnecessary move"},
            {"hanzi": "何必计较", "en": "why haggle or bother over"}
        ],
        "idioms": [
            {"hanzi": "何必当初", "pinyin": "hé bì dāng chū", "meaning_en": "why did one act so initially; hindsight regret (早知今日何必当初)"},
            {"hanzi": "画蛇添足", "pinyin": "huà shé tiān zú", "meaning_en": "draw snake and add feet; superfluous over-elaboration"},
            {"hanzi": "多此一举", "pinyin": "duō cǐ yī jǔ", "meaning_en": "make a totally unnecessary gesture; redundant act"},
            {"hanzi": "庸人自扰", "pinyin": "yōng rén zì rǎo", "meaning_en": "worry about imaginary troubles; create problems out of nothing"}
        ],
        "character_decomposition": [
            {
                "character": "何",
                "pinyin": "hé",
                "meaning_en": "why; what; how",
                "meaning_es": "por qué; qué; cómo",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person carrying burden) + 可 (exclamation)",
                "sound_component": "可 (kě)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 carrying a pole 可, serving as an interrogative asking why or for what reason.",
                "visual_mnemonic_story_en": "A traveler (亻) setting down his shoulder pole (可) questioning why to go further (何).",
                "visual_mnemonic_story_es": "Un viajero (亻) posando su pesada pértiga (可) preguntándose el motivo de tanto afán (何).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "ONR",
                "traditional": "何"
            },
            {
                "character": "必",
                "pinyin": "bì",
                "meaning_en": "must; surely; necessity",
                "meaning_es": "necesario; deber; ciertamente",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "八 (divide) + line piercing heart 心",
                "sound_component": "必 (bì)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A decisive line dividing or staking certainty through 心; absolute necessity and certainty.",
                "visual_mnemonic_story_en": "A firm stake driven into the center of resolve, signaling absolute necessity (必).",
                "visual_mnemonic_story_es": "Una estaca clavada con aplomo en el centro de la decisión, denotando necesidad imperiosa (必).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "PHT",
                "traditional": "必"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Asking why (何) something should be an absolute necessity (必) rhetorical declares: there is no need (何必).",
            "composite_memory_hook_es": "Cuestionar el porqué (何) de una pretendida necesidad forzosa (必) afirma que no es menester (何必).",
            "cultural_and_cognitive_roots": "A classic rhetorical rhetorical adverb (反问副词) common in philosophical persuasion and Daoist simplicity.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'hé bì' (35-51). Lift upwards on 'hé' and drop emphatically on 'bì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "何", "pinyin": "hé", "meaning_en": "what; why", "distinction_note": "Person radical 亻 with 可"},
                {"character": "荷", "pinyin": "hé", "meaning_en": "lotus; carry", "distinction_note": "Grass radical 艹 on top of 何"},
                {"character": "必", "pinyin": "bì", "meaning_en": "must; necessity", "distinction_note": "Heart 心 pierced with a diagonal slash"},
                {"character": "心", "pinyin": "xīn", "meaning_en": "heart; mind", "distinction_note": "Without the piercing diagonal slash"}
            ],
            "etymological_cognates": [
                {"character": "需", "pinyin": "xū", "gloss_en": "require; need"},
                {"character": "用", "pinyin": "yòng", "gloss_en": "use; need (不用)"},
                {"character": "须", "pinyin": "xū", "gloss_en": "must; beard"},
                {"character": "宜", "pinyin": "yí", "gloss_en": "fitting; suitable"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "何必 explicitly poses a rhetorical question rejecting the necessity of an action or worry.",
            "contrasts": [
                {"id": 1, "compared_word": "何必 vs. 不必", "pinyin": "búbì", "analysis": "不必 is a direct declarative statement stating lack of need (你明天不必来), while 何必 is an emotive rhetorical counter-question (你何必亲自去呢)."},
                {"id": 2, "compared_word": "何必 vs. 何苦", "pinyin": "hékǔ", "analysis": "何苦 emphasizes that the action brings unnecessary suffering or pain (何苦自讨苦吃), while 何必 merely focuses on superfluity."},
                {"id": 3, "compared_word": "何必 vs. 为何", "pinyin": "wèihé", "analysis": "为何 is a genuine inquiry asking 'why' (你为何迟到), whereas 何必 implies 'there is no reason to'."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "苏轼在《前赤壁赋》中豁达地写道：‘天地之间，物各有主，苟非吾之所有，虽一毫而莫取。’人生在世不过数十寒暑，清风明月皆可取用不竭，我们又何必贪恋身外虚名浮利，徒增无谓的心灵枷锁与身心疲惫呢。",
                "pinyin": "Sū Shì zài Qián Chìbì Fù zhōng huòdá de xiědào: 'Tiāndì zhījiān, wù gè yǒu zhǔ, gǒu fēi wú zhī suǒyǒu, suī yìháo ér mò qǔ.' Rénshēng zài shì bùguò shùshí hánshǔ, qīngfēng míngyuè jiē kě qǔyòng-bùjié, wǒmen yòu hébì tānliàn shēnwài xūmíng fúlì, tú zēng wúwèi de xīnlíng jiāsuǒ yǔ shēnxīn píbèi ne.",
                "en": "Su Shi magnanimously noted: in heaven and earth each thing has its master; if not mine, take not a hair. Life is a brief flash; cool breezes and bright moons are inexhaustible. Why covet transient vanities and shackle one's soul?",
                "es": "Su Shi proclamó con serenidad: cada bien tiene su dueño; no tomes ni una brizna ajena. La brisa y la luna son dádivas inagotables. ¿Para qué codiciar vanidades efímeras que sólo encadenan y fatigan el espíritu?"
            },
            {
                "id": "#2",
                "hanzi": "小男孩好奇的质问如雷贯耳：‘大家每次投篮后何必大费周章搬梯子爬上去取球呢？’这句反问瞬间点醒了被条条框框束缚的大人们。是啊，既然目的是投球计分，何必死守着一个带底的完整果筐？锯掉多余的底子，问题便迎刃而解。",
                "pinyin": "Xiǎo nánhái hàoqí de zhìwèn rúléi-guàn'ěr: 'Dàjiā měicì tóulán hòu hébì dàfèi-zhōuzhāng bān tīzi pá shàngqu qǔ qiú ne?' Zhè jù fǎnwèn shùnjiān diǎnxǐng le bèi tiáotiáo-kuàngkuàng shùfù de dàrenmen. Shì a, jìrán mùdì shì tóu qiú jìfēn, hébì sǐshǒu zhe yí ge dàidǐ de wánzhěng guǒkuāng? Jù diào duōyú de dǐzi, wèntí biàn yíngrèn'érjiě.",
                "en": "The boy's question rang out: 'Why go to all the trouble of hauling ladders after each score?' This rhetorical query woke adults chained by convention. If the goal is scoring, why cling to a closed basket? Saw off the superfluous bottom, and the knot unties.",
                "es": "La pregunta del niño resonó con fuerza: '¿Para qué complicarse subiendo a una escalera tras cada tiro?' Aquella duda abrió los ojos a los adultos. Si el fin es encestar, ¿qué necesidad hay de conservar el fondo? Serrarlo disipó el problema."
            }
        ]
    },

    # 29 多亏
    {
        "id": "29",
        "hanzi": "多亏",
        "pinyin": "duō kuī",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "thanks to; luckily; fortunate that",
            "es": "gracias a; por fortuna; menos mal que"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to express gratitude that an intervention, help, or lucky circumstance averted disaster or achieved success",
                "definition_es": "expresa que gracias a determinada ayuda o circunstancia propicia se evitó un mal o se logró un bien",
                "example_phrase": "多亏了邻居的热心相助 (thanks to the enthusiastic help of our neighbors)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "昨晚突降狂风暴雨，多亏巡查网格员在半夜及时排查隐患，老旧小区的低洼地带才没有发生严重内涝。",
                "pinyin": "Zuówǎn tūjiàng kuángfēng-bàoyǔ, duōkuī xúnchá wǎnggéyuán zài bànyè jíshí páichá yǐnhuàn, lǎojiù xiǎoqū de dīwā dìdài cái méiyǒu fāshēng yánzhòng nèilào.",
                "en": "A violent storm struck last night; thanks to the neighborhood inspectors identifying hazards at midnight, the low-lying old community avoided flooding.",
                "es": "Anoche arreció un temporal; gracias a que los vigilantes revisaron los sumideros a medianoche, la barriada vieja no sufrió inundaciones."
            },
            {
                "id": "#2",
                "hanzi": "这次复杂的跨境并购谈判能够圆满成功，多亏了法务专家团队在关键时刻化解了重大合规风险。",
                "pinyin": "Zhè cì fùzá de kuàjìng bìnggòu tánpàn nénggòu yuánmǎn chénggōng, duōkuī le fǎwù zhuānjiā tuánduì zài guānjiàn shíkè huàjiě le zhòngdà hégūi fēngxiǎn.",
                "en": "This intricate cross-border merger negotiation succeeded smoothly, thanks to the legal team defusing major compliance risks at critical junctures.",
                "es": "La compleja negociación de fusión internacional culminó con éxito gracias a que el equipo legal resolvió a tiempo graves escollos normativos."
            }
        ],
        "collocations": [
            {"hanzi": "多亏了", "en": "thanks to; fortunately"},
            {"hanzi": "这次多亏你", "en": "I'm indebted to you this time"},
            {"hanzi": "多亏及时", "en": "luckily in the nick of time"},
            {"hanzi": "多亏有准备", "en": "fortunate that we prepared"},
            {"hanzi": "多亏医生抢救", "en": "thanks to doctors' emergency rescue"},
            {"hanzi": "多亏提醒", "en": "thanks for the timely reminder"}
        ],
        "idioms": [
            {"hanzi": "化险为夷", "pinyin": "huà xiǎn wéi yí", "meaning_en": "turn danger into safety; avert mortal peril"},
            {"hanzi": "绝处逢生", "pinyin": "jué chù féng shēng", "meaning_en": "find life in a dead end; rescue from desperate straits"},
            {"hanzi": "吉人天相", "pinyin": "jí rén tiān xiàng", "meaning_en": "heaven assists the good; blessed by good fortune"},
            {"hanzi": "感激不尽", "pinyin": "gǎn jī bú jìn", "meaning_en": "boundless gratitude; cannot thank enough"}
        ],
        "character_decomposition": [
            {
                "character": "多",
                "pinyin": "duō",
                "meaning_en": "many; much; abundant",
                "meaning_es": "mucho; abundante",
                "radical": "夕",
                "radical_meaning_en": "evening",
                "meaning_component": "two 夕 (crescent moons / pieces of meat) stacked",
                "sound_component": "多 (duō)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two portions of sacrificial meat 夕 stacked together in ancient script, denoting abundance and multiplicity.",
                "visual_mnemonic_story_en": "Two cuts of choice meat (夕) piled generously one over another: great abundance (多).",
                "visual_mnemonic_story_es": "Dos piezas de carne (夕) apiladas generosamente en el festín: gran abundancia (多).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "NINI",
                "traditional": "多"
            },
            {
                "character": "亏",
                "pinyin": "kuī",
                "meaning_en": "loss; deficit; deficient; luckily",
                "meaning_es": "déficit; pérdida; menguar; gracia",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "breath 丂 failing to rise under the sky 一",
                "sound_component": "亏 (kuī)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Breath striving upward but hindered by a bar; deficit or losing out; used conversely in '多亏' as indebtedness for spared loss.",
                "visual_mnemonic_story_en": "A debt or deficit averted in time through fortunate assistance (亏).",
                "visual_mnemonic_story_es": "Un quebranto o déficit esquivado a tiempo gracias a un providencial auxilio (亏).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MMVS",
                "traditional": "虧"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Having great abundance (多) spared from painful deficit (亏) means expressing heartfelt thanks (多亏).",
            "composite_memory_hook_es": "Contar con abundancia (多) sin sufrir mengua ni pérdida (亏) es motivo para dar gracias (多亏).",
            "cultural_and_cognitive_roots": "Grammaticalized colloquial construction expressing appreciative relief when a negative outcome is narrowly averted.",
            "tone_sandhi_and_pitch_modulation": "Two level high tones: 'duō kuī' (55-55). Maintain sustained high, warm vocal pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "多", "pinyin": "duō", "meaning_en": "many; much", "distinction_note": "Two 夕 stacked vertically"},
                {"character": "夕", "pinyin": "xī", "meaning_en": "evening; sunset", "distinction_note": "Single character with 3 strokes"},
                {"character": "亏", "pinyin": "kuī", "meaning_en": "loss; luckily", "distinction_note": "3 strokes: horizontal, horizontal, vertical hook with slant"},
                {"character": "于", "pinyin": "yú", "meaning_en": "at; in; to", "distinction_note": "Has two horizontal bars and a vertical hook without the curving tail"}
            ],
            "etymological_cognates": [
                {"character": "幸", "pinyin": "xìng", "gloss_en": "fortunate; lucky"},
                {"character": "赖", "pinyin": "lài", "gloss_en": "rely on; thanks to"},
                {"character": "蒙", "pinyin": "méng", "gloss_en": "receive favor; indebted"},
                {"character": "谢", "pinyin": "xiè", "gloss_en": "thank; decline"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "多亏 expresses grateful relief that an external person or circumstance averted a looming setback.",
            "contrasts": [
                {"id": 1, "compared_word": "多亏 vs. 幸亏", "pinyin": "xìngkuī", "analysis": "幸亏 focuses on impersonal luck or chance (幸亏没下雨), while 多亏 can take direct human grammatical objects of gratitude (多亏了你, 多亏老师指点)."},
                {"id": 2, "compared_word": "多亏 vs. 感谢", "pinyin": "gǎnxiè", "analysis": "感谢 is an explicit verb expressing appreciation, while 多亏 functions as a clause connective explaining causality."},
                {"id": 3, "compared_word": "多亏 vs. 由于", "pinyin": "yóuyú", "analysis": "由于 is a neutral preposition of cause (can lead to bad or good outcomes), while 多亏 strictly leads to happy relief."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "回首艰辛的创业岁月，创始人感慨万千：‘当年在最资金链濒临断裂的至暗时刻，多亏了老同学毅然抵押房产为我们注资，多亏了团队骨干通宵达旦拼死攻坚，我们这支年轻的企业才能浴火重生、行稳致远。’",
                "pinyin": "Huíshǒu jiānxīn de chuàngyè suìyuè, chuàngshǐrén gǎnkǎi-wànqiān: 'Dāngnián zài zuì zījīnliàn bīnlín duànliè de zhì'àn shíkè, duōkuī le lǎo tóngxué yìrán dǐyā fángchǎn wèi wǒmen zhùzī, duōkuī le tuánduì gǔgàn tōngxiāo-dádàn pīnsǐ gōngjiān, wǒmen zhè zhī niánqīng de qǐyè cái néng yùhuǒ-chóngshēng, xíngwěn-zhìyuǎn.'",
                "en": "Reflecting on arduous startup days, the founder remarked with emotion: 'When funding ran dry, thanks to an old classmate mortgaging his home and our team working day and night, our venture rose from the ashes and prospered.'",
                "es": "Evocando los duros inicios, el fundador confesó conmovido: 'Al agotarse los fondos, gracias a un viejo amigo que hipotecó su casa y al equipo que bregó sin descanso, esta empresa renació de sus cenizas y prosperó'."
            },
            {
                "id": "#2",
                "hanzi": "篮球运动今天能够演变成风靡全球的第一大室内球类项目，多亏了当年那位大胆发问的小男孩。多亏了他一句天真无邪的提醒，工匠们才从僵化死板的思维定势中猛然醒悟，拿起锯子锯开筐底，彻底赋予了比赛畅快淋漓的全新生命力。",
                "pinyin": "Lánqiú yùndòng jīntiān nénggòu yǎnbiàn wéi fēngmí quánqiú de dì-yī dà shìnèi qiúlèi xiàngmù, duōkuī le dāngnián nà wèi dàdǎn fāwèn de xiǎo nánhái. Duōkuī le tā yí jù tiānzhēn-wúxié de tíxǐng, gōngjiàngmen cái cóng jiānghuà sǐbǎn de sīwéi dìngshì zhōng měngrán xǐngwù, ná qǐ jùzi jù kāi kuāngdǐ, chèdǐ fùyǔ le bǐsài chàngkuài-línlí de quánxīn shēngmìnglì.",
                "en": "That basketball evolved into the world's premier indoor sport is thanks to that daring little boy. Thanks to his innocent reminder, craftsmen snapped out of rigid assumptions, took up saws to cut the basket bottoms, and breathed vibrant life into the game.",
                "es": "Si el baloncesto es hoy el rey de los deportes bajo techo, es gracias al niño de la grada. Gracias a su ingeniosa observación, los conserjes quebraron su ceguera mental y abrieron el fondo con la sierra, dotando al juego de vitalidad."
            }
        ]
    },

    # 30 连忙
    {
        "id": "30",
        "hanzi": "连忙",
        "pinyin": "lián máng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "promptly; at once; hurriedly; hastily",
            "es": "en seguida; apresuradamente; con presteza; al punto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "acting immediately and hurriedly in prompt response to a situation or request",
                "definition_es": "actuar con prontitud y rapidez en respuesta inmediata a un estímulo o llamada",
                "example_phrase": "听到敲门声连忙起身开门 (hurriedly get up to answer the knock on the door)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "看到白发苍苍的老奶奶提着沉重的蔬菜上车，坐在前排的年轻小伙子连忙微笑着起身让座。",
                "pinyin": "Kàndào báifà-cāngcāng de lǎonǎinai tí zhe chénzhòng de shūcài shàngchē, zuò zài qiánpái de niánqīng xiǎohuǒzi liánmáng wēixiào zhe qǐshēn ràngzuò.",
                "en": "Seeing an elderly gray-haired grandmother board carrying heavy vegetables, the young man in the front row promptly stood up with a smile to offer his seat.",
                "es": "Al ver subir al autobús a una anciana con pesadas bolsas de verduras, el joven de la primera fila se levantó de inmediato sonriente para cederle el asiento."
            },
            {
                "id": "#2",
                "hanzi": "发现实验室管道接头处有微量气体泄漏，值班技术员连忙按下了紧急切断阀并拉响警报。",
                "pinyin": "Fāxiàn shíyànshì guǎndào jiētóuchù yǒu wēiliàng qìtǐ xièlòu, zhíbān jìshùyuán liánmáng ànxià le jǐnjí qiēduànfá bìng lāxiǎng jǐngbào.",
                "en": "Spotting a trace gas leak at the laboratory pipe junction, the technician on duty promptly pressed the emergency shut-off valve and sounded the alarm.",
                "es": "Al percatarse de una leve fuga en la junta de la tubería, el técnico de guardia accionó al punto la válvula de corte y activó la alarma."
            }
        ],
        "collocations": [
            {"hanzi": "连忙站起来", "en": "promptly stand up"},
            {"hanzi": "连忙解释", "en": "hastily explain"},
            {"hanzi": "连忙道歉", "en": "hastily apologize"},
            {"hanzi": "连忙答应", "en": "promptly agree / consent"},
            {"hanzi": "连忙跑过去", "en": "hurriedly run over"},
            {"hanzi": "连忙挥手", "en": "hurriedly wave one's hand"}
        ],
        "idioms": [
            {"hanzi": "迫不及待", "pinyin": "pò bù jí dài", "meaning_en": "too impatient to wait; eager beyond endurance"},
            {"hanzi": "疾足先得", "pinyin": "jí zú xiān dé", "meaning_en": "the swift-footed arrives first; first come first served"},
            {"hanzi": "闻风而动", "pinyin": "wén fēng ér dòng", "meaning_en": "act immediately upon hearing news; spring into action"},
            {"hanzi": "雷厉风行", "pinyin": "léi lì fēng xíng", "meaning_en": "vigorous and speedy as thunder and wind"}
        ],
        "character_decomposition": [
            {
                "character": "连",
                "pinyin": "lián",
                "meaning_en": "connect; join; continuous; even",
                "meaning_es": "unir; conectar; continuo",
                "radical": "辶",
                "radical_meaning_en": "movement",
                "meaning_component": "辶 (movement / road) + 车 (wheeled chariot)",
                "sound_component": "车 (chē / connection)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Chariots 车 advancing in unbroken convoy along the road 辶; continuous link without break.",
                "visual_mnemonic_story_en": "War chariots (车) linked one behind another on a rapid march (辶).",
                "visual_mnemonic_story_es": "Carros de combate (车) enlazados en marcha continua por el camino (辶).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YKQ",
                "traditional": "連"
            },
            {
                "character": "忙",
                "pinyin": "máng",
                "meaning_en": "busy; hurried; rushed",
                "meaning_es": "ocupado; apresurado; ajetreado",
                "radical": "忄",
                "radical_meaning_en": "heart",
                "meaning_component": "忄 (flustered heart) + 亡 (perish / lose)",
                "sound_component": "亡 (wáng / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Heart radical 忄 beside 亡; heart overwhelmed by urgent tasks, losing calm in a state of bustling flurry.",
                "visual_mnemonic_story_en": "A flustered heart (忄) racing frantically as if time were slipping away (亡): being busy (忙).",
                "visual_mnemonic_story_es": "Un corazón agitado (忄) que late apresurado como si el tiempo se agotara (亡): andar atareado (忙).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "PYN",
                "traditional": "忙"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Continuously advancing without delay (连) with a brisk busy pace (忙) means doing something promptly (连忙).",
            "composite_memory_hook_es": "Avanzar sin pausa (连) con paso diligente y presto (忙) expresa actuar apresuradamente (连忙).",
            "cultural_and_cognitive_roots": "Captures the instinctive, prompt physical reaction to unexpected events, polite hospitality, or urgent emergencies.",
            "tone_sandhi_and_pitch_modulation": "Two rising second tones: 'lián máng' (35-35). Both rise in tone with lively, agile rhythm."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "连", "pinyin": "lián", "meaning_en": "connect; even", "distinction_note": "Movement radical 辶 with 车"},
                {"character": "运", "pinyin": "yùn", "meaning_en": "transport; fortune", "distinction_note": "Movement radical 辶 with 云"},
                {"character": "忙", "pinyin": "máng", "meaning_en": "busy; hurried", "distinction_note": "Heart radical 忄 on left of 亡"},
                {"character": "芒", "pinyin": "máng", "meaning_en": "awn; miscanthus", "distinction_note": "Grass radical 艹 on top of 亡"}
            ],
            "etymological_cognates": [
                {"character": "急", "pinyin": "jí", "gloss_en": "urgent; hurried"},
                {"character": "赶", "pinyin": "gǎn", "gloss_en": "rush; catch up"},
                {"character": "速", "pinyin": "sù", "gloss_en": "fast; rapid"},
                {"character": "骤", "pinyin": "zhòu", "gloss_en": "sudden; abrupt"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "连忙 emphasizes prompt, immediate physical reaction in response to external circumstances.",
            "contrasts": [
                {"id": 1, "compared_word": "连忙 vs. 急忙", "pinyin": "jímáng", "analysis": "连忙 emphasizes instant promptness in reaction (听到敲门连忙开门), whereas 急忙 highlights anxious internal haste and agitation (急忙赶路)."},
                {"id": 2, "compared_word": "连忙 vs. 赶快", "pinyin": "gǎnkuài", "analysis": "赶快 is often used in imperatives urging someone else to hurry (你赶快去吧), while 连忙 describes completed past actions in narration."},
                {"id": 3, "compared_word": "连忙 vs. 马上", "pinyin": "mǎshàng", "analysis": "马上 specifies temporal immediacy (I will do it right now), whereas 连忙 denotes brisk responsive physical action."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "暮春时节山间气候多变，刚才还是晴空万里，转眼间天际便乌云翻滚。正在山坡上晾晒新茶的农户们见状，连忙抓起竹箩竹匾快步收拾。大家齐心协力赶在大雨倾盆前，将嫩绿芬芳的春茶悉数抢运进了干燥的库房。",
                "pinyin": "Mùchūn shíjié shānjiān qìhòu duōbiàn, gāngcái háishì qíngkōng-wànlǐ, zhuǎnyǎn jiān tiānjì biàn wūyún fāngǔn. Zhèng zài shānpō shang liàngshài xīnchá de nónghùmen jiànzhuàng, liánmáng zhuā qǐ zhúluó zhúbiǎn kuàibù shōushi. Dàjiā qíxīn-xiélì gǎn zài dàyǔ qīngpén qián, jiāng nènlǜ fēnfāng de chūnchá xīshù qiǎngyùn jìn le gānzào de kùfáng.",
                "en": "Spring mountain weather is capricious; sunny skies swiftly filled with rolling dark clouds. Tea farmers drying leaves on slopes immediately grabbed wicker trays. Working together, they hustled the fragrant green tea into dry storehouses before downpours struck.",
                "es": "En primavera el clima serrano es veleidoso; el cielo azul se encapotó al punto de nubarrones. Los campesinos que secaban té recogieron las bateas apresuradamente. En equipo, resguardaron la cosecha fragante en el almacén antes del aguacero."
            },
            {
                "id": "#2",
                "hanzi": "当听到围观小男孩那句‘为什么不把筐底剪掉’的天真建议时，在场被死板规则困扰的大人们面面相觑，工匠连忙找来锋利的锯子爬上梯恩子。伴随着一阵清脆的拉锯声，桃筐底部应声脱落，困扰所有人多时的繁琐取球障碍瞬间烟消云散。",
                "pinyin": "Dāng tīngdào wéiguān xiǎo nánhái nà jù 'wèishénme bù bǎ kuāngdǐ jiǎn diào' de tiānzhēn jiànyì shí, zàichǎng bèi sǐbǎn guīzé kùnrǎo de dàrenmen miànmiàn-xiāngqù, gōngjiàng liánmáng zhǎolái fēnglì de jùzi pá shàng tīzi. Bànsuí zhe yí zhèn qīngcuì de lājù shēng, táokuāng dǐbù yìngshēng tuōluò, kùnrǎo suǒyǒurén duōshí de fánsuǒ qǔ qiú zhàng'ài shùnjiān yānxiāo-yúnsàn.",
                "en": "Hearing the boy's suggestion: 'Why not cut off the basket bottom?', dumbfounded adults looked at each other. A worker promptly grabbed a sharp saw and climbed the ladder. With rhythmic rasping strokes, the bottom fell away, dissolving the nuisance in an instant.",
                "es": "Ante la ocurrencia del niño: '¿Por qué no le quitan el fondo?', los adultos se miraron perplejos. El conserje buscó al punto una sierra afilada y subió a la escalera. Al serrar la base, el obstáculo que tanto les agobiaba se esfumó en un abrir y cerrar de ojos."
            }
        ]
    }
]

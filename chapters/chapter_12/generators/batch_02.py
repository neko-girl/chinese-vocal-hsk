# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 召开
    {
        "id": "11",
        "hanzi": "召开",
        "pinyin": "zhào kāi",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to convene; convoke; hold (a formal meeting or conference)",
            "es": "convocar; celebrar; inaugurar (una reunión, asamblea o cumbre formal)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Formal",
                "definition_en": "to formally summon participants together to open and hold an assembly, press conference, or council",
                "definition_es": "convocar a los participantes y abrir formalmente una asamblea, rueda de prensa o congreso",
                "example_phrase": "召开新闻发布会 (hold a press conference)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "腾讯公司在海外多个国家首都同步召开大型媒体沟通会，隆重推介微信国际版全新升级功能。",
                "pinyin": "Téngxùn gōngsī zài hǎiwài duō gè guójiā shǒudū tóngbù zhàokāi dàxíng méitǐ gōutōnghuì, lóngzhòng tuījiè Wēixìn guójìbǎn quánxīn shēngjí gōngnéng.",
                "en": "Tencent held large media briefings simultaneously across several foreign capitals to grandly introduce the newly upgraded features of WeChat's international edition.",
                "es": "Tencent celebró ruedas de prensa simultáneas en varias capitales extranjeras para presentar por todo lo alto las novedades de la versión internacional de WeChat."
            },
            {
                "id": "#2",
                "hanzi": "联合国气候变化大会每年定期召开，汇聚全球数百个国家的元首与专家共同商讨减排方案。",
                "pinyin": "Liánhéguó qìhòu biànhuà dàhuì měinián dìngqī zhàokāi, huìjù quánqiú shùbǎi gè guójiā de yuánshǒu yǔ zhuānjiā gòngtóng shāngtǎo jiǎnpái fāng'àn.",
                "en": "The United Nations Climate Change Conference is convened annually, gathering leaders and specialists from hundreds of nations to negotiate emission cuts.",
                "es": "La Cumbre del Clima de la ONU se convoca cada año reuniendo a jefes de Estado y expertos de cientos de países para consensuar recortes de emisiones."
            }
        ],
        "collocations": [
            {"hanzi": "召开会议", "en": "convene a meeting / conference"},
            {"hanzi": "召开发布会", "en": "hold a press conference"},
            {"hanzi": "召开股东大会", "en": "convene a shareholders' meeting"},
            {"hanzi": "定期召开", "en": "convene regularly"},
            {"hanzi": "紧急召开", "en": "convene urgently"},
            {"hanzi": "决定召开", "en": "decide to convene"}
        ],
        "idioms": [
            {"hanzi": "广开言路", "pinyin": "guǎng kāi yán lù", "meaning_en": "open wide all channels of speech and counsel"},
            {"hanzi": "群英荟萃", "pinyin": "qún yīng huì cuì", "meaning_en": "distinguished assembly of heroes and talents"},
            {"hanzi": "集思广益", "pinyin": "jí sī guǎng yì", "meaning_en": "pool collective wisdom for fruitful benefit"},
            {"hanzi": "盛况空前", "pinyin": "shèng kuàng kōng qián", "meaning_en": "unprecedented grandeur and spectacular turnout"}
        ],
        "character_decomposition": [
            {
                "character": "召",
                "pinyin": "zhào",
                "meaning_en": "summon; call together; invoke",
                "meaning_es": "convocar; llamar; citar; invocar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "刀 (knife/authority command) + 口 (mouth speaking imperial order)",
                "sound_component": "Self-phonetic zhào",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A mouth 口 issuing an authoritative command backed by legal power 刀; summons to assemble.",
                "visual_mnemonic_story_en": "An authoritative mouth (口) issuing decisive sharp orders (刀) summons everyone to assemble (召).",
                "visual_mnemonic_story_es": "Una boca autoritaria (口) profiere órdenes tajantes (刀) para convocar a la reunión (召).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "SHR",
                "traditional": ""
            },
            {
                "character": "开",
                "pinyin": "kāi",
                "meaning_en": "open; unfold; start; hold",
                "meaning_es": "abrir; desplegar; iniciar; celebrar",
                "radical": "廾",
                "radical_meaning_en": "two hands",
                "meaning_component": "Two hands 廾 lifting off the crossbar 一 of a heavy gate",
                "sound_component": "Historical phonetic nuance in 開",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Two hands lifting away a wooden bolt to unbar double doors; extended to opening, initiating, and commencing meetings.",
                "visual_mnemonic_story_en": "Two hands lifting the heavy door bolt open wide the palace gates (开).",
                "visual_mnemonic_story_es": "Dos manos apartan el cerrojo de madera para abrir de par en par la sesión (开).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MT",
                "traditional": "開"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Summoning participants together with authority (召) and opening the proceedings (开) is convening a conference (召开).",
            "composite_memory_hook_es": "Convocar con autoridad (召) y dar inicio a la sesión (开) es inaugurar o celebrar una reunión (召开).",
            "cultural_and_cognitive_roots": "Derived from ancient sovereign edicts: emperors issued royal summons (召令) to open court councils (开朝会) across the provinces.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by first tone: 'zhào kāi' (51-55). Sharp drop from 51 followed by sustained high level 55."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "绍", "pinyin": "shào", "meaning_en": "introduce; carry on", "distinction_note": "Has silk radical 纟 on left of 召"},
                {"character": "招", "pinyin": "zhāo", "meaning_en": "beckon; recruit", "distinction_note": "Has hand radical 扌 on left of 召"},
                {"character": "升", "pinyin": "shēng", "meaning_en": "rise; liter", "distinction_note": "Has a slanted drop on top left, unlike 开"},
                {"character": "井", "pinyin": "jǐng", "meaning_en": "water well", "distinction_note": "Has two vertical parallel strokes crossing two horizontals"}
            ],
            "etymological_cognates": [
                {"character": "举", "pinyin": "jǔ", "gloss_en": "hold; elevate"},
                {"character": "行", "pinyin": "xíng", "gloss_en": "conduct; execute"},
                {"character": "办", "pinyin": "bàn", "gloss_en": "manage; organize"},
                {"character": "聚", "pinyin": "jù", "gloss_en": "gather; assemble"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "召开 is a formal transitive verb used exclusively for assembling participants to hold large, organized conferences or meetings.",
            "contrasts": [
                {"id": "1", "compared_word": "召开 vs. 举行", "pinyin": "jǔxíng", "analysis": "举行 applies broadly to ceremonies, sports games, banquets, and contests ('举行婚礼', '举行比赛'), while 召开 applies almost exclusively to meetings and conferences."},
                {"id": "2", "compared_word": "召开 vs. 开会", "pinyin": "kāihuì", "analysis": "开会 is colloquial and general for attending or holding any routine workplace or school meeting, whereas 召开 is solemn and formal."},
                {"id": "3", "compared_word": "召开 vs. 召集", "pinyin": "zhàojí", "analysis": "召集 focuses on the preliminary act of rounding up or summoning people together, whereas 召开 focuses on formally holding the proceedings."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "为进一步深化多边科技创新合作，国际电信联盟在日内瓦召开全球数字通信发展研讨会。来自数十个国家的行业代表围绕下一代移动网络安全标准展开深入探讨，为弥合全球数字鸿沟凝聚了广泛的国际共识。",
                "pinyin": "Wèi jìnyíbù shēnhuà duōbiān kējì chuàngxīn hézuò, Guójì Diànxìn Liánméng zài Rìnèiwǎ zhàokāi quánqiú shùzì tōngxìn fāzhǎn yántǎohuì. Láizì shùshí gè guójiā de hángyè dàibiǎo wéirào xià yí dài yídòng wǎngluò ānquán biāozhǔn zhǎnkāi shēnrù tàntǎo, wèi míhé quánqiú shùzì hónggōu níngjùle guǎngfàn de guójì gòngshí.",
                "en": "To deepen multilateral tech cooperation, the ITU convened a global symposium in Geneva. Industry delegates from dozens of countries debated next-gen network standards, forging broad international consensus to bridge digital divides.",
                "es": "Para estrechar lazos técnicos, la UIT convocó en Ginebra un simposio sobre telecomunicaciones digitales. Delegados de decenas de países debatieron estándares de seguridad de red consensuando vías para acortar la brecha digital."
            },
            {
                "id": "#2",
                "hanzi": "在企业面临产业转型的关键历史节点，董事会紧急召开临时特别会议，细致审议关于全面进军海外智能软件市场的战略方案。与会高管经过长达数小时的热烈论证，最终全票通过了重组海外营销事业群的重大决议。",
                "pinyin": "Zài qǐyè miànlín chǎnyè zhuǎnxíng de guānjiàn lìshǐ jiédiǎn, dǒngshìhuì jǐnjí zhàokāi línshí tèbié huìyì, xìzhì shěnyì guānyú quánmiàn jìnjūn hǎiwài zhìnéng ruǎnjiàn shìchǎng de zhànlüè fāng'àn. Yùhuì gāoguǎn jīngguò chángdá shù xiǎoshí de rèliè lùnzhèng, zuìzhōng quánpiào tōngguòle chóngzǔ hǎiwài yíngxiāo shìyèqún de zhòngdà juéyì.",
                "en": "At a critical juncture of industrial transformation, the board urgently convened an extraordinary meeting to review strategic plans for expanding overseas. After hours of debate, executives unanimously approved restructuring the overseas division.",
                "es": "En plena reconversión, el consejo convocó una junta extraordinaria para examinar la expansión de software inteligente en el exterior. Tras horas de deliberación, la directiva aprobó por unanimidad la reestructuración internacional."
            }
        ]
    },

    # 12 合作
    {
        "id": "12",
        "hanzi": "合作",
        "pinyin": "hé zuò",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to cooperate; collaborate; work together; cooperation; partnership",
            "es": "cooperar; colaborar; trabajar conjuntamente; cooperación; colaboración"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to work jointly with others toward a common goal or mutual benefit",
                "definition_es": "obrar juntamente con otro u otros para la consecución de un fin común",
                "example_phrase": "真诚合作 (cooperate sincerely)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "joint operation, collaborative alliance, or mutual association",
                "definition_es": "asociación, alianza colaborativa o acción conjunta",
                "example_phrase": "经贸合作 (economic and trade cooperation)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "微信通过与各国本地电信企业展开多维度合作，成功降低了跨国数据漫游资费，方便了全球用户。",
                "pinyin": "Wēixìn tōngguò yǔ gè guó běndì diànxìn qǐyè zhǎnkāi duōwéidù hézuò, chénggōng jiàngdīle kuàguó shùjù mànyóu zīfèi, fāngbiànle quánqiú yònghù.",
                "en": "Through multidimensional cooperation with local telecom companies, WeChat successfully cut cross-border data roaming fees, benefiting global users.",
                "es": "Mediante una estrecha colaboración con operadoras locales, WeChat redujo las tarifas de itinerancia de datos beneficiando a usuarios del mundo entero."
            },
            {
                "id": "#2",
                "hanzi": "两家高科技企业决定在云计算和大数据算法领域开展全面战略合作，共同拓展海外新兴市场。",
                "pinyin": "Liǎng jiā gāokējì qǐyè juédìng zài yúnjìsuàn hé dàshùjù suànfǎ lǐngyù kāizhǎn quánmiàn zhànlüè hézuò, gòngtóng tuòzhǎn hǎiwài xīnxīng shìchǎng.",
                "en": "The two high-tech enterprises decided to launch comprehensive strategic cooperation in cloud computing and big data, jointly expanding into emerging markets.",
                "es": "Las dos firmas tecnológicas acordaron una cooperación estratégica en computación en la nube y macrodatos para expandirse en mercados emergentes."
            }
        ],
        "collocations": [
            {"hanzi": "战略合作", "en": "strategic cooperation / partnership"},
            {"hanzi": "开展合作", "en": "launch / carry out cooperation"},
            {"hanzi": "深化合作", "en": "deepen collaboration"},
            {"hanzi": "合作伙伴", "en": "cooperative partner / associate"},
            {"hanzi": "国际合作", "en": "international cooperation"},
            {"hanzi": "合作共赢", "en": "win-win cooperation"}
        ],
        "idioms": [
            {"hanzi": "精诚合作", "pinyin": "jīng chéng hé zuò", "meaning_en": "cooperate with utmost sincerity and dedication"},
            {"hanzi": "分工合作", "pinyin": "fēn gōng hé zuò", "meaning_en": "divide the labor and collaborate smoothly"},
            {"hanzi": "同心协力", "pinyin": "tóng xīn xié lì", "meaning_en": "unite in one heart and pool collaborative efforts"},
            {"hanzi": "风雨同舟", "pinyin": "fēng yǔ tóng zhōu", "meaning_en": "stand together through storm and tempest in the same boat"}
        ],
        "character_decomposition": [
            {
                "character": "合",
                "pinyin": "hé",
                "meaning_en": "combine; join; gather; fit; harmonious",
                "meaning_es": "unir; juntar; encajar; armonizar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "亼 (three lines coming together at top / lid) + 口 (mouth / container)",
                "sound_component": "Self-phonetic hé",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A container with its lid fitted tightly on top; symbolizes meeting together, closing gaps, and harmonious joining.",
                "visual_mnemonic_story_en": "A snug lid (亼) fitting over a round bowl container (口) unites two halves seamlessly (合).",
                "visual_mnemonic_story_es": "Una tapa (亼) que encaja exacta sobre el cuenco (口) uniendo las partes en perfecta armonía (合).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OMR",
                "traditional": ""
            },
            {
                "character": "作",
                "pinyin": "zuò",
                "meaning_en": "do; make; write; act; work",
                "meaning_es": "hacer; actuar; crear; obrar; trabajar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / human laborer) + 乍 (sudden sprouting / initial start)",
                "sound_component": "乍 (zhà, sudden / phonetic zuò)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 stepping forward to begin crafting, working, or manufacturing something new.",
                "visual_mnemonic_story_en": "A diligent person (亻) rising promptly at daybreak (乍) to perform creative work (作).",
                "visual_mnemonic_story_es": "Un hombre trabajador (亻) que inicia con presteza (乍) su faena creadora (作).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OHS",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Joining hearts harmoniously together (合) to execute work and creations (作) is cooperation (合作).",
            "composite_memory_hook_es": "Unirse en sintonía (合) para llevar a cabo obras conjuntas (作) es cooperar (合作).",
            "cultural_and_cognitive_roots": "Derived from ancient guild agricultural traditions: neighboring villages pooling draft oxen and sickles to complete harvest under the banner of '分工合作'.",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by fourth tone: 'hé zuò' (35-51). Smooth rising tone followed by sharp decisive fall."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "盒", "pinyin": "hé", "meaning_en": "box; case", "distinction_note": "Has dish radical 皿 under 合"},
                {"character": "答", "pinyin": "dá", "meaning_en": "answer; reply", "distinction_note": "Has bamboo radical 竹 on top of 合"},
                {"character": "昨", "pinyin": "zuó", "meaning_en": "yesterday", "distinction_note": "Has sun radical 日 on left of 乍 instead of person 亻 in 作"},
                {"character": "诈", "pinyin": "zhà", "meaning_en": "deceive; cheat", "distinction_note": "Has speech radical 讠 on left of 乍"}
            ],
            "etymological_cognates": [
                {"character": "协", "pinyin": "xié", "gloss_en": "joint; harmonize"},
                {"character": "同", "pinyin": "tóng", "gloss_en": "together; same"},
                {"character": "联", "pinyin": "lián", "gloss_en": "ally; connect"},
                {"character": "帮", "pinyin": "bāng", "gloss_en": "help; assist"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "合作 emphasizes mutual coordination and complementary pooling of resources between parties toward shared benefit.",
            "contrasts": [
                {"id": "1", "compared_word": "合作 vs. 协作", "pinyin": "xiézuò", "analysis": "协作 emphasizes technical operational coordination between different units or departments on a joint production line ('分工协作'), while 合作 is broader covering business, diplomacy, and trade."},
                {"id": "2", "compared_word": "合作 vs. 配合", "pinyin": "pèihé", "analysis": "配合 indicates playing a subordinate or supporting role to assist a main actor's lead ('积极配合警方工作'), whereas 合作 implies equal partnership."},
                {"id": "3", "compared_word": "合作 vs. 联合", "pinyin": "liánhé", "analysis": "联合 denotes merging distinct groups into a unified coalition or formal federation ('联合声明', '联合国'), while 合作 refers to ongoing joint actions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在经济全球化日益深入的今天，任何国家都无法在封闭隔绝中谋求长久繁荣。深化国际经贸合作与人文交流，坚持多边主义与互利共赢原则，不仅能够促进生产要素在全球范围内高效流动，更是维护世界和平稳定的共同基石。",
                "pinyin": "Zài jīngjì quánqiúhuà rìyì shēnrù de jīntiān, rènhé guójiā dōu wúfǎ zài fēngbì géjué zhōng móuqiú chángjiǔ fánróng. Shēnhuà guójì jīngmào hézuò yǔ rénwén jiāoliú, jiānchí duōbiān zhǔyì yǔ hùlì gòngyíng yuánzé, bùjǐn nénggòu cùjìn shēngchǎn yàosù zài quánqiú fànwéi nèi gāoxiào liúdòng, gèng shì wéihù shìjiè hépíng wěndìng de gòngtóng jīshí.",
                "en": "In today's interconnected global economy, no nation can seek enduring prosperity in isolation. Deepening trade cooperation and upholding win-win multilateralism optimizes resource flows and lays a cornerstone for world peace.",
                "es": "En la economía global actual, ninguna nación puede prosperar aislada. Profundizar la cooperación comercial y defender el multilateralismo agiliza el flujo de recursos mundiales y afianza la paz y estabilidad compartidas."
            },
            {
                "id": "#2",
                "hanzi": "现代医学攻关早已跨越了单一学科的狭隘界限，呈现出多学科深度交叉合作的鲜明特征。临床医生、生物化学家与计算机算法专家紧密携手，通过海量临床数据建模与药物分子筛选，成功研制出针对罕见疾病的高效靶向新药。",
                "pinyin": "Xiàndài yīxué gōngguān zǎoyǐ kuàyuèle dānyī xuékē de xiá'ài jièxiàn, chéngxiàn chū duōxuékē shēndù jiāochā hézuò de xiānmíng tèzhēng. Línchuáng yīshēng, shēngwù-huàxuéjiā yǔ jìsuànjī suànfǎ zhuānjiā jǐnmì xiéshǒu, tōngguò hǎiliàng línchuáng shùjù jiànmó yǔ yàowù fēnzǐ shāixuǎn, chénggōng yánzhì chū zhēnduì hǎnjiàn jíbìng de gāoxiào bǎxiàng xīnyào.",
                "en": "Modern medical breakthroughs have broken disciplinary boundaries, showcasing deep cross-field collaboration. Physicians, biochemists, and AI experts join hands, modeling clinical data to formulate targeted medicines for rare diseases.",
                "es": "Los avances biomédicos trascienden barreras académicas reflejando una estrecha colaboración interdisciplinar. Médicos, bioquímicos y expertos en computación aunaron esfuerzos creando fármacos dirigidos contra patologías raras."
            }
        ]
    },

    # 13 伙伴
    {
        "id": "13",
        "hanzi": "伙伴",
        "pinyin": "huǒ bàn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "partner; companion; associate; pal; ally",
            "es": "compañero; socio; aliado; partícipe; colega"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person, entity, or nation closely associated with another in a joint activity, business endeavor, or friendship",
                "definition_es": "persona, empresa o país que comparte una actividad, negocio, causa o estrecha amistad con otro",
                "example_phrase": "合作伙伴 (cooperative business partner)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "中国互联网企业在拓展海外市场时，积极寻找当地实力雄厚的电信运营商作为战略合作伙伴。",
                "pinyin": "Zhōngguó hùliánwǎng qǐyè zài tuòzhǎn hǎiwài shìchǎng shí, jījí xúnzhǎo dāngdì shílì xiónghòu de diànxìn yùnyíngshāng zuòwéi zhànlüè hézuò huǒbàn.",
                "en": "When expanding into overseas markets, Chinese Internet firms actively seek powerful local telecom carriers as strategic partners.",
                "es": "Al expandirse en ultramar, las tecnológicas chinas buscan operadoras locales consolidadas como socios estratégicos de confianza."
            },
            {
                "id": "#2",
                "hanzi": "每当回忆起童年时代在村头小河边与小伙伴们嬉水抓鱼的情景，他心中总会泛起阵阵暖意。",
                "pinyin": "Měidāng huíyì qǐ tóngnián shídài zài cūntóu xiǎohé biān yǔ xiǎohuǒbànmen xīshuǐ zhuāyú de qíngjǐng, tā xīnzhōng zǒng huì fànqǐ zhènzhèn nuǎnyì.",
                "en": "Whenever he reminisces about splashing and catching fish by the village stream with childhood pals, warmth wells up in his heart.",
                "es": "Al evocar cómo chapoteaba pescando en el arroyo con sus compañeros de infancia, una oleada de entrañable calidez inunda su corazón."
            }
        ],
        "collocations": [
            {"hanzi": "合作伙伴", "en": "cooperative partner / associate"},
            {"hanzi": "战略伙伴", "en": "strategic partner"},
            {"hanzi": "小伙伴", "en": "little companion / childhood pal"},
            {"hanzi": "忠实伙伴", "en": "faithful companion"},
            {"hanzi": "贸易伙伴", "en": "trading partner"},
            {"hanzi": "寻找伙伴", "en": "seek a partner"}
        ],
        "idioms": [
            {"hanzi": "同甘共苦", "pinyin": "tóng gān gòng kǔ", "meaning_en": "share joys and sorrows through thick and thin"},
            {"hanzi": "休戚与共", "pinyin": "xiū qī yǔ gòng", "meaning_en": "share common weal and woe in close solidarity"},
            {"hanzi": "莫逆之交", "pinyin": "mò nì zhī jiāo", "meaning_en": "bosom friends with complete mutual understanding"},
            {"hanzi": "金石为开", "pinyin": "jīn shí wéi kāi", "meaning_en": "sincerity splits even gold and stone"}
        ],
        "character_decomposition": [
            {
                "character": "伙",
                "pinyin": "huǒ",
                "meaning_en": "companion; partner; group; mess food",
                "meaning_es": "compañero; socio; cuadrilla; rancho de comida",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / comrade) + 火 (campfire / hearth flame)",
                "sound_component": "火 (huǒ, fire / phonetic companion)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Soldiers or comrades 亻 sharing meals cooked over the same campfire flame 火; fellow messmates.",
                "visual_mnemonic_story_en": "Comrades (亻) gathered around a warm camp cooking fire (火) share food as brothers (伙).",
                "visual_mnemonic_story_es": "Soldados (亻) reunidos al calor de la hoguera (火) compartiendo el rancho como camaradas (伙).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "OF",
                "traditional": ""
            },
            {
                "character": "伴",
                "pinyin": "bàn",
                "meaning_en": "accompany; partner; associate; attend",
                "meaning_es": "acompañar; compañero; pareja; escoltar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person walking beside) + 半 (half / equal counterpart)",
                "sound_component": "半 (bàn, half / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 who serves as the other matching half 半 of a pair; a walking companion or partner.",
                "visual_mnemonic_story_en": "A loving person (亻) standing as your missing half (半) walks beside you as a companion (伴).",
                "visual_mnemonic_story_es": "Una persona (亻) que encarna tu otra mitad (半) y camina a tu lado como fiel compañera (伴).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OFQ",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Comrades sharing the mess fire (伙) who stand as your other matching half (伴) are true partners (伙伴).",
            "composite_memory_hook_es": "Los camaradas que comparten el fogón (伙) y caminan a tu lado como tu otra mitad (伴) son compañeros (伙伴).",
            "cultural_and_cognitive_roots": "Originates from the military logistics system of ancient China (火伴): ten soldiers forming a single mess squad sharing one cooking pot.",
            "tone_sandhi_and_pitch_modulation": "Third tone followed by fourth tone: 'huǒ bàn' (214-51). Dip low with 214, then drop sharply with 51."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "秋", "pinyin": "qiū", "meaning_en": "autumn", "distinction_note": "Has grain radical 禾 on left of 火 instead of person 亻 in 伙"},
                {"character": "狄", "pinyin": "dí", "meaning_en": "northern tribes", "distinction_note": "Has dog radical 犭 on left of 火"},
                {"character": "判", "pinyin": "pàn", "meaning_en": "judge; distinguish", "distinction_note": "Has knife radical 刂 on right of 半"},
                {"character": "胖", "pinyin": "pàng", "meaning_en": "fat; stout", "distinction_note": "Has flesh radical 月 on left of 半"}
            ],
            "etymological_cognates": [
                {"character": "友", "pinyin": "yǒu", "gloss_en": "friend; friendship"},
                {"character": "朋", "pinyin": "péng", "gloss_en": "friend; peer"},
                {"character": "侣", "pinyin": "lǚ", "gloss_en": "companion; mate"},
                {"character": "俦", "pinyin": "chóu", "gloss_en": "comrade; fellow"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "伙伴 highlights mutual accompaniment, joint participation in ventures, or informal camaraderie.",
            "contrasts": [
                {"id": "1", "compared_word": "伙伴 vs. 朋友", "pinyin": "péngyou", "analysis": "朋友 emphasizes emotional personal friendship and social closeness, whereas 伙伴 often includes shared commercial tasks or business alliances ('商业伙伴')."},
                {"id": "2", "compared_word": "伙伴 vs. 同事", "pinyin": "tóngshì", "analysis": "同事 specifically denotes coworkers employed at the same firm or institution, while 伙伴 can cross corporate and national boundaries."},
                {"id": "3", "compared_word": "伙伴 vs. 同伴", "pinyin": "tóngbàn", "analysis": "同伴 usually refers to people traveling or carrying out a specific transient trip together ('旅行同伴'), while 伙伴 can denote lasting strategic partners."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在携手推进共建“一带一路”高质量发展的征程中，各参与国秉持共商共建共享原则，结成了休戚与共的紧密合作伙伴。通过加强港口、铁路与新能源电站等重大基础设施联通，为沿线各国人民带来了沉甸甸的发展福祉。",
                "pinyin": "Zài xiéshǒu tuījìn gòngjiàn 'Yīdài Yīlù' gāozhìliàng fāzhǎn de zhēngchéng zhōng, gè cānyùguó bǐngchí gòngshāng-gòngjiàn-gòngxiǎng yuánzé, jiéchéngle xiūqī-yǔgòng de jǐnmì hézuò huǒbàn. Tōngguò jiāqiáng gǎngkǒu, tiělù yǔ xīnnéngyuán diànzhàn děng zhòngdà jīchǔ shèshī liántōng, wèi yánxiàn gè guó rénmín dàiláile chéndiāndiān de fāzhǎn fúzhǐ.",
                "en": "In promoting high-quality Belt and Road development, participating nations adhere to consultation and joint building, forging close partnerships. Upgrading ports, railways, and power grids brings tangible well-being to all peoples.",
                "es": "En la Franja y la Ruta, los países asociados cooperan bajo el principio de consulta y beneficio compartido forjando alianzas sólidas. La interconexión de puertos, vías férreas y centrales de energía genera prosperidad palpable."
            },
            {
                "id": "#2",
                "hanzi": "科研团队的带头人常说，在探索未知真理的漫长而孤独的道路上，志同道合的实验室伙伴是给予自己最大精神力量的源泉。大家在无数次试验失败时不离不弃、互相打气，正是这种肝胆相照的伙伴情谊铸就了最后的突破奇迹。",
                "pinyin": "Kēyán tuánduì de dàitóurén cháng shuō, zài tànsuǒ wèizhī zhēnlǐ de màncháng ér gūdú de dàolù shàng, zhìtóng-dàohé de shíyànshì huǒbàn shì jǐyǔ zìjǐ zuìdà jīngshén lìliang de yuánquán. Dàjiā zài wúshù cì shìyàn shībài shí bùlí-búqì, hùxiāng dǎqì, zhèngshì zhèzhǒng gāndǎn-xiāngzhào de huǒbàn qíngyì zhùjiùle zuìhòu de tūpò qíjī.",
                "en": "The research lead often said that on the lonely road of seeking scientific truth, like-minded lab partners are the greatest source of strength. Standing by each other through repeated failures, this deep camaraderie forged ultimate breakthroughs.",
                "es": "El jefe de investigación afirma que en el arduo camino de la ciencia, los colegas de laboratorio son el mayor sostén anímico. Apoyándose en cada tropiezo con lealtad inquebrantable, ese compañerismo obró el milagro del éxito final."
            }
        ]
    },

    # 14 总裁
    {
        "id": "14",
        "hanzi": "总裁",
        "pinyin": "zǒng cái",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "president (of a corporation); CEO; director-general",
            "es": "presidente ejecutivo; director general; CEO de empresa corporativa"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the highest executive officer or president managing the operations of a large corporation, conglomerate, or international financial institution",
                "definition_es": "máximo responsable ejecutivo o presidente con mando supremo en una corporación, consorcio o banco",
                "example_phrase": "执行总裁 (chief executive officer / CEO)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在微信国际化战略研讨会上，腾讯公司总裁发表了关于打造全球移动互联生态圈的主题演讲。",
                "pinyin": "Zài Wēixìn guójìhuà zhànlüè yántǎohuì shàng, Téngxùn gōngsī zǒngcái fābiǎole guānyú dǎzào quánqiú yídòng hùlián shēngtàiquān de zhǔtí yǎnjiǎng.",
                "en": "At the WeChat globalization seminar, the president of Tencent delivered a keynote address on building a worldwide mobile internet ecosystem.",
                "es": "En las jornadas de internacionalización de WeChat, el presidente de Tencent pronunció un discurso magistral sobre el ecosistema móvil global."
            },
            {
                "id": "#2",
                "hanzi": "跨国银行新任总裁雷厉风行地启动了组织架构改革，旨在全面提升数字化金融服务的响应速度。",
                "pinyin": "Kuàguó yínháng xīnrèn zǒngcái léilì-fēngxíng de qǐdòngle zǔzhī jiàgòu gǎigé, zhǐzài quánmiàn tíshēng shùzìhuà jīnróng fúwù de xiǎngyìng sùdù.",
                "en": "The multinational bank's new president swiftly initiated an organizational restructure aiming to elevate the responsiveness of digital financial services.",
                "es": "El nuevo presidente ejecutivo del banco internacional acometió con pulso firme una reforma organizativa para agilizar la banca digital."
            }
        ],
        "collocations": [
            {"hanzi": "执行总裁", "en": "Chief Executive Officer (CEO)"},
            {"hanzi": "副总裁", "en": "Vice President (VP)"},
            {"hanzi": "公司总裁", "en": "company president"},
            {"hanzi": "出任总裁", "en": "assume the post of president"},
            {"hanzi": "集团总裁", "en": "group president / conglomerate CEO"},
            {"hanzi": "高级副总裁", "en": "Senior Vice President (SVP)"}
        ],
        "idioms": [
            {"hanzi": "运筹帷幄", "pinyin": "yùn chóu wéi wò", "meaning_en": "devise strategies within a command tent; mastermind decisions"},
            {"hanzi": "独当一面", "pinyin": "dú dāng yī miàn", "meaning_en": "take charge of a major area independently with mastery"},
            {"hanzi": "总揽大局", "pinyin": "zǒng lǎn dà jú", "meaning_en": "oversee the entire situation and steer overall direction"},
            {"hanzi": "断事如神", "pinyin": "duàn shì rú shén", "meaning_en": "judge and resolve affairs with godlike insight"}
        ],
        "character_decomposition": [
            {
                "character": "总",
                "pinyin": "zǒng",
                "meaning_en": "general; overall; assemble; always; chief",
                "meaning_es": "general; total; reunir; supremo; siempre",
                "radical": "丷",
                "radical_meaning_en": "eight / disperse",
                "meaning_component": "Silk thread bundle gathered together at center over heart 心",
                "sound_component": "Archaic phonetic nuance in 總",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Gathering separate strands of raw silk into a central unified thread over one's heart 心; overarching general control.",
                "visual_mnemonic_story_en": "Gathering diverse silk threads under the head of heart-centered control unifies the whole (总).",
                "visual_mnemonic_story_es": "Reunir los hilos dispersos bajo un corazón directivo (心) centraliza el mando supremo (总).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "CRP",
                "traditional": "總"
            },
            {
                "character": "裁",
                "pinyin": "cái",
                "meaning_en": "cut out; trim; judge; decide; arbitrate",
                "meaning_es": "cortar tela; recortar; juzgar; decidir; arbitrar",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (fabric garment) + 𢦏/戈 (halberd cutting tool / weapon)",
                "sound_component": "𢦏 (zāi, phonosemantic cut)",
                "stroke_count": 12,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Cutting patterned fabric 衣 with a sharp blade 戈 to tailor fine garments; extended to judging, ruling, and deciding corporate policy.",
                "visual_mnemonic_story_en": "Using a sharp blade to cut out silk cloth (衣) to measure tailor garments; ruling with decisive judgment (裁).",
                "visual_mnemonic_story_es": "Empuñar la cuchilla afilada sobre la tela (衣) para cortar con precisión y dictar sentencia (裁).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JIYHV",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "One who holds overall central authority (总) and makes decisive executive rulings (裁) is the corporate president (总裁).",
            "composite_memory_hook_es": "Quien ostenta el mando general unificado (总) y toma decisiones ejecutivas de peso (裁) es el presidente (总裁).",
            "cultural_and_cognitive_roots": "Historically, 总裁 denoted high imperial court editors or examiners overseeing major compilations (like the Siku Quanshu 四库全书总裁官). Modern usage adopted it for corporate CEOs.",
            "tone_sandhi_and_pitch_modulation": "Third tone followed by second tone: 'zǒng cái' (214-35). Low dipping third tone rising smoothly into second tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "忽", "pinyin": "hū", "meaning_en": "suddenly; neglect", "distinction_note": "Has 勿 over 心 instead of 丷 and 口 in 总"},
                {"character": "思", "pinyin": "sī", "meaning_en": "think; thought", "distinction_note": "Has field 田 over 心"},
                {"character": "栽", "pinyin": "zāi", "meaning_en": "plant; cultivate", "distinction_note": "Has tree radical 木 inside instead of cloth 衣 in 裁"},
                {"character": "载", "pinyin": "zài", "meaning_en": "carry; load", "distinction_note": "Has vehicle radical 车 inside"}
            ],
            "etymological_cognates": [
                {"character": "董", "pinyin": "dǒng", "gloss_en": "direct; board director"},
                {"character": "长", "pinyin": "zhǎng", "gloss_en": "senior; chief"},
                {"character": "领", "pinyin": "lǐng", "gloss_en": "lead; collar"},
                {"character": "首", "pinyin": "shǒu", "gloss_en": "head; leader"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "总裁 designates the highest operating executive or corporate president responsible for overall company management.",
            "contrasts": [
                {"id": "1", "compared_word": "总裁 vs. 董事长", "pinyin": "dǒngshìzhǎng", "analysis": "董事长 is the Chairman of the Board representing shareholders with supreme governance authority, while 总裁 is the CEO executing daily operational management."},
                {"id": "2", "compared_word": "总裁 vs. 总经理", "pinyin": "zǒngjīnglǐ", "analysis": "总经理 is the general manager of a company branch or standard firm, whereas 总裁 is typically used in large conglomerates, multinationals, or international groups."},
                {"id": "3", "compared_word": "总裁 vs. 首席执行官", "pinyin": "shǒuxí zhíxíngguān", "analysis": "首席执行官 is the direct translation of CEO; in many Chinese corporate structures, 总裁 and CEO are identical or overlapping roles."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "跨国企业的总裁不仅需要具备敏锐的商业洞察力和卓越的决断力，更应当具有跨越多元文化背景的包容心。在面对复杂多变的全球地缘政治与国际贸易挑战时，一位优秀的总裁总能审时度势，带领企业破浪前行。",
                "pinyin": "Kuàguó qǐyè de zǒngcái bùjǐn xūyào jùbèi mǐnruì de shāngyè dòngchàlì yǔ zhuóyuè de juéduànlì, gèng yīngdāng jùyǒu kuàyuè duōyuán wénhuà bèijǐng de bāoróngxīn. Zài miànduì fùzá-duōbiàn de quánqiú dìyuán zhèngzhì yǔ guójì màoyì tiǎozhàn shí, yī wèi yōuxiù de zǒngcái zǒng néng shěnshí-duóshì, dàilǐng qǐyè pòlàng-qiánxíng.",
                "en": "The president of a multinational must possess sharp commercial insight, decisiveness, and intercultural tolerance. Facing volatile geopolitical and trade challenges, an exceptional CEO gauges trends to steer the firm forward.",
                "es": "El presidente de una multinacional aúna visión comercial, pulso firme e integración intercultural. Ante la volatilidad geopolítica y arancelaria, un directivo ejemplar calibra los tiempos guiando la corporación hacia buen puerto."
            },
            {
                "id": "#2",
                "hanzi": "在年度全球商业创新峰会上，多家世界五百强企业的执行总裁齐聚一堂，围绕人工智能与绿色低碳转型的战略交汇点展开高端对话。总裁们一致指出，未来十年科技企业必须主动拥抱可持续发展，将社会责任融入核心经营逻辑。",
                "pinyin": "Zài niándù quánqiú shāngyè chuàngxīn fēnghuì shàng, duō jiā shìjiè wǔbǎiqiáng qǐyè de zhíxíng zǒngcái qíjù-yītáng, wéirào réngōng zhìnéng yǔ lǜsè dītàn zhuǎnxíng de zhànlüè jiāohuìdiǎn zhǎnkāi gāoduān duìhuà. Zǒngcáimen yīzhì zhǐchū, wèilái shí nián kējì qǐyè bìxū zhǔdòng yōngbào kěchíxù fāzhǎn, jiāng shèhuì zérèn róngrù héxīn jīngyíng luójí.",
                "en": "At the annual business innovation summit, Fortune 500 CEOs gathered for dialogue on AI and green low-carbon transitions. The presidents agreed that tech firms must embrace sustainability over the coming decade, embedding ethics into core strategies.",
                "es": "En la cumbre anual de innovación empresarial, los presidentes de gigantes de Fortune 500 dialogaron sobre inteligencia artificial y sostenibilidad verde, coincidiendo en arraigar la responsabilidad social en la estrategia corporativa."
            }
        ]
    },

    # 15 实现
    {
        "id": "15",
        "hanzi": "实现",
        "pinyin": "shí xiàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to realize; achieve; fulfill; bring about; materialize",
            "es": "realizar; cumplir; materializar; hacer realidad; alcanzar (metas, sueños)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to make a wish, goal, ideal, plan, or potential reality through concrete action",
                "definition_es": "llevar a efecto una aspiración, plan, ideal o meta convirtiéndolos en realidad palpable",
                "example_phrase": "实现梦想 (realize one's dream)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "通过技术创新与全球化布局，微信成功实现了让全球海外用户随时随地免费跨国语音互联的愿景。",
                "pinyin": "Tōngguò jìshù chuàngxīn yǔ quánqiúhuà bùjú, Wēixìn chénggōng shíxiànle ràng quánqiú hǎiwài yònghù suíshí-suídì miǎnfèi kuàguó yǔyīn hùlián de yuànjǐng.",
                "en": "Through technological innovation and global layout, WeChat successfully realized its vision of enabling overseas users worldwide to connect freely via voice anytime.",
                "es": "Mediante la innovación y su despliegue mundial, WeChat logró hacer realidad el sueño de que los usuarios se comuniquen gratis por voz en cualquier rincón."
            },
            {
                "id": "#2",
                "hanzi": "经过研发团队历经数百次反复调试，这款高精度医疗检测设备终于实现了核心部件的完全自主可控。",
                "pinyin": "Jīngguò yánfā tuánduì lìjīng shùbǎi cì fǎnfù tiáoshì, zhè kuǎn gāojīngdù yīliáo jiǎncè shèbèi zhōngyú shíxiànle héxīn bùjiàn de wánquán zìzhǔ kěkòng.",
                "en": "After hundreds of rounds of tuning by the R&D team, this precision medical detection device finally achieved full independence for its core components.",
                "es": "Tras cientos de ensayos del equipo de desarrollo, este equipo médico de precisión logró por fin la total autonomía tecnológica en sus piezas clave."
            }
        ],
        "collocations": [
            {"hanzi": "实现目标", "en": "achieve / realize an objective"},
            {"hanzi": "实现梦想", "en": "fulfill / realize a dream"},
            {"hanzi": "实现价值", "en": "realize one's value"},
            {"hanzi": "逐步实现", "en": "gradually achieve"},
            {"hanzi": "难以实现", "en": "hard to achieve / realize"},
            {"hanzi": "全面实现", "en": "fully realize / achieve in full"}
        ],
        "idioms": [
            {"hanzi": "如愿以偿", "pinyin": "rú yuàn yǐ cháng", "meaning_en": "have one's wish completely fulfilled"},
            {"hanzi": "梦想成真", "pinyin": "mèng xiǎng chéng zhēn", "meaning_en": "dreams come true; aspirations turn into reality"},
            {"hanzi": "水到渠成", "pinyin": "shuǐ dào qú chéng", "meaning_en": "when water flows, a channel is formed; success comes naturally"},
            {"hanzi": "大功告成", "pinyin": "dà gōng gào chéng", "meaning_en": "grand task successfully accomplished"}
        ],
        "character_decomposition": [
            {
                "character": "实",
                "pinyin": "shí",
                "meaning_en": "solid; real; true; fruit; reality",
                "meaning_es": "sólido; real; verdadero; fruto; realidad",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (safe domestic house) + 头/贯 (abundance of wealth and grain filling house)",
                "sound_component": "Historical phonetic nuance in 實",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A house 宀 packed full of solid tangible treasures and grains; signifies substance, truth, and solid reality.",
                "visual_mnemonic_story_en": "A house (宀) filled to the brim with real solid grains and wealth embodies substance (实).",
                "visual_mnemonic_story_es": "El hogar (宀) colmado de grano y bienes tangibles encarna la solidez y la realidad (实).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JYK",
                "traditional": "實"
            },
            {
                "character": "现",
                "pinyin": "xiàn",
                "meaning_en": "appear; present; current; manifest",
                "meaning_es": "aparecer; presente; actual; manifestarse",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王/玉 (shining jade jewel) + 见 (see / visible to eyes)",
                "sound_component": "见 (jiàn, see / phonetic nuance xiàn)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Polishing a rough stone until the brilliant luster of jade 王 is clearly visible 见 to all eyes; becoming manifest and present.",
                "visual_mnemonic_story_en": "A precious jade gem (王) uncovered and held up for all to see (见) manifests into reality (现).",
                "visual_mnemonic_story_es": "Una gema de jade (王) pulida que se expone a la vista de todos (见) se manifiesta en el presente (现).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MGBU",
                "traditional": "現"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Taking solid substance (实) and bringing it into visible manifestation (现) is realizing and fulfilling a goal (实现).",
            "composite_memory_hook_es": "Dar solidez tangible (实) a algo haciéndolo visible y presente (现) es hacer realidad o materializar (实现).",
            "cultural_and_cognitive_roots": "Philosophical concept originating from Song Dynasty Neo-Confucianism: transforming abstract principle (理) into living experiential actuality (实体展现).",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by fourth tone: 'shí xiàn' (35-51). Rising contour gliding into sharp falling drop."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "头", "pinyin": "tóu", "meaning_en": "head", "distinction_note": "Lacks the roof radical 宀 on top of 实"},
                {"character": "买", "pinyin": "mǎi", "meaning_en": "buy", "distinction_note": "Has 乛 on top instead of 宀"},
                {"character": "观", "pinyin": "guān", "meaning_en": "view; watch", "distinction_note": "Has 又 on left of 见 instead of jade 王 in 现"},
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; compass", "distinction_note": "Has husband 夫 on left of 见"}
            ],
            "etymological_cognates": [
                {"character": "达", "pinyin": "dá", "gloss_en": "reach; attain"},
                {"character": "成", "pinyin": "chéng", "gloss_en": "complete; succeed"},
                {"character": "践", "pinyin": "jiàn", "gloss_en": "tread; practice"},
                {"character": "行", "pinyin": "xíng", "gloss_en": "execute; conduct"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "实现 emphasizes translating an abstract blueprint, dream, ideal, or capability into actual tangible existence.",
            "contrasts": [
                {"id": "1", "compared_word": "实现 vs. 实行", "pinyin": "shíxíng", "analysis": "实行 means putting a policy, law, or management system into administrative practice ('实行新法规'), while 实现 is achieving an end result or goal ('实现理想')."},
                {"id": "2", "compared_word": "实现 vs. 完成", "pinyin": "wánchéng", "analysis": "完成 means finishing a concrete task, assignment, or construction project ('完成作业', '完成工程'), whereas 实现 applies to dreams, targets, and ambitions."},
                {"id": "3", "compared_word": "实现 vs. 达到", "pinyin": "dádào", "analysis": "达到 refers to hitting a measurable numerical metric, temperature, or physical standard ('达到国际标准'), while 实现 encompasses comprehensive fulfillment."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "实现中华民族伟大复兴是近代以来全体中国人民最深沉的共同梦想。一代代奋斗者前赴后继、自强不息，在艰难险阻中开拓创新，使国家经济实力、科技实力和综合国力跃上崭新台阶，让千年梦想步步化为宏伟壮丽的现实。",
                "pinyin": "Shíxiàn Zhōnghuá mínzú wěidà fùxīng shì jìndài yǐlái quántǐ Zhōngguó rénmín zuì shēnchén de gòngtóng mèngxiǎng. Yīdàidài fèndòuzhě qiánfù-hòujì, zìqiáng-bùxī, zài jiānnán xiǎnzǔ zhōng kāituò chuàngxīn, shǐ guójiā jīngjì shílì, kējì shílì hé zōnghé guólì yuèshàng zhǎnxīn táijiē, ràng qiān nián mèngxiǎng bùbù huà wéi hóngwěi zhuànglì de xiànshí.",
                "en": "Realizing the rejuvenation of the Chinese nation has been the deepest shared dream of its people in modern times. Generations of strivers persevered through hardships, lifting national strength and turning millennial dreams into grand reality.",
                "es": "Hacer realidad la gran revitalización nacional ha sido el mayor anhelo del pueblo chino. Generaciones de luchadores perseveraron superando escollos y elevando el poderío científico y económico, transformando un sueño milenario en realidad tangible."
            },
            {
                "id": "#2",
                "hanzi": "青年科研工作者要敢于有梦、勇于追梦。科学研究是一场漫长而艰苦的马拉松，只有把个人的人生理想紧密融入国家重大发展战略之中，耐得住寂寞、扛得住挫折，才能在一次次攻坚克难中最终实现自己的人生科学价值。",
                "pinyin": "Qīngnián kēyán gōngzuòzhě yào gǎnyú yǒumèng, yǒngyú zhuīmèng. Kēxué yánjiū shì yī cháng màncháng ér jiānkǔ de mǎlāsōng, zhǐyǒu bǎ gèrén de rénshēng lǐxiǎng jǐnmì róngrù guójiā zhòngdà fāzhǎn zhànlüè zhīzhōng, nàidezhù jìmò, kángdezhù cuòzhé, cáinéng zài yīcìcì gōngjiān-kènán zhōng zuìzhōng shíxiàn zìjǐ de rénshēng kēxué jiàzhí.",
                "en": "Young scientists must dare to dream and pursue them. Research is a grueling marathon; only by weaving personal aspirations into national strategic goals and withstanding setbacks can one ultimately realize one's scientific value in life.",
                "es": "Los jóvenes científicos deben soñar con valentía. La investigación es un maratón exigente; solo aunando la vocación personal con las prioridades nacionales y superando la soledad de la probeta se materializa el valor científico propio."
            }
        ]
    },

    # 16 覆盖
    {
        "id": "16",
        "hanzi": "覆盖",
        "pinyin": "fù gài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to cover; blanket; overlay; encompass; reach",
            "es": "cubrir; tapar; arropar; abarcar; extender la cobertura sobre"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to spread over the surface of something; or to extend telecommunications, media, or service reach across a geographical territory or population",
                "definition_es": "extenderse sobre una superficie cubriéndola; o abarcar una red de telecomunicaciones o servicio un territorio o población",
                "example_phrase": "网络全面覆盖 (network full coverage)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "得益于全球云服务器节点的广泛铺设，微信国际版的高速数据通信网络已经覆盖了一百多个国家和地区。",
                "pinyin": "Déyì yú quánqiú yún fúwùqì jiédiǎn de guǎngfàn pūshè, Wēixìn guójìbǎn de gāosù shùjù tōngxìn wǎngluò yǐjīng fùgàile yībǎi duō gè guójiā hé dìqū.",
                "en": "Thanks to the extensive deployment of global cloud server nodes, WeChat International's high-speed network has covered over one hundred countries and regions.",
                "es": "Gracias al despliegue mundial de servidores en la nube, la red de alta velocidad de WeChat cubre ya más de un centenar de países y territorios."
            },
            {
                "id": "#2",
                "hanzi": "一场罕见的漫天大雪在一夜之间覆盖了整座北方古城，城墙与古寺屋顶银装素裹、宛若仙境。",
                "pinyin": "Yī chǎng hǎnjiàn de màntiān dàxuě zài yíyè zhījiān fùgàile zhěng zuò běifāng gǔchéng, chéngqiáng yǔ gǔsì wūdǐng yínzhuāng-sùguǒ, wǎnrù xiānjìng.",
                "en": "A rare heavy snowfall blanketed the ancient northern city overnight, cloaking city walls and temple roofs in pristine silver like a wonderland.",
                "es": "Una gran nevada cubrió por completo la urbe histórica norteña en una noche, arropando murallas y templos con un manto blanco de cuento de hadas."
            }
        ],
        "collocations": [
            {"hanzi": "全面覆盖", "en": "full / comprehensive coverage"},
            {"hanzi": "网络覆盖", "en": "network coverage"},
            {"hanzi": "覆盖范围", "en": "coverage area / scope"},
            {"hanzi": "森林覆盖率", "en": "forest coverage rate"},
            {"hanzi": "信号覆盖", "en": "signal coverage"},
            {"hanzi": "覆盖面积", "en": "coverage area"}
        ],
        "idioms": [
            {"hanzi": "翻云覆雨", "pinyin": "fān yún fù yǔ", "meaning_en": "capriciously manipulate situations; play fast and loose"},
            {"hanzi": "天翻地覆", "pinyin": "tiān fān dì fù", "meaning_en": "heaven and earth overturned; earth-shattering changes"},
            {"hanzi": "席卷天下", "pinyin": "xí juǎn tiān xià", "meaning_en": "sweep across the entire world like a rolling mat"},
            {"hanzi": "铺天盖地", "pinyin": "pū tiān gài dì", "meaning_en": "blot out sky and earth; engulfing everywhere"}
        ],
        "character_decomposition": [
            {
                "character": "覆",
                "pinyin": "fù",
                "meaning_en": "cover; capsize; overturn; repeat",
                "meaning_es": "cubrir; tapar; volcar; zozobrar; repetir",
                "radical": "覀",
                "radical_meaning_en": "cover / west",
                "meaning_component": "覀/襾 (lid/cover placed from above) + 復 (return / repeat over surface)",
                "sound_component": "復 (fù, repeat / phonetic)",
                "stroke_count": 18,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A cover 覀 placed over an object repeatedly 復 until its entire surface is blanketed or overturned.",
                "visual_mnemonic_story_en": "Spreading a wide woven sheet (覀) repeatedly (復) until it completely blankets the land (覆).",
                "visual_mnemonic_story_es": "Extender un amplio toldo (覀) que vuelve a tapar (復) hasta cubrir la superficie por entero (覆).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MTMOE",
                "traditional": ""
            },
            {
                "character": "盖",
                "pinyin": "gài",
                "meaning_en": "lid; cap; cover; build; surpass",
                "meaning_es": "tapa; cubierta; techar; edificar; sobrepasar",
                "radical": "皿",
                "radical_meaning_en": "dish / vessel",
                "meaning_component": "羊/𦍌 (auspicious wool/meat) + 皿 (shallow dish container covered from above)",
                "sound_component": "Historical phonetic nuance in 蓋",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A thatch roof or lid covering a vessel 皿 to protect precious contents; placing a lid or building over something.",
                "visual_mnemonic_story_en": "Placing an ornate lid over a broad dish container (皿) to seal and cover it (盖).",
                "visual_mnemonic_story_es": "Poner una cubierta protectora sobre la vasija (皿) para taparla y techarla (盖).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TOTBT",
                "traditional": "蓋"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Spreading a blanket from above (覆) and securing a protective lid over all (盖) constitutes complete coverage (覆盖).",
            "composite_memory_hook_es": "Arropar desde arriba (覆) y poner una cubierta total (盖) es cubrir o dar cobertura completa (覆盖).",
            "cultural_and_cognitive_roots": "Used in traditional cosmology: Heaven blankets all things (天覆地载), which transitioned in modern technological parlance to wireless signal grids (信号覆盖).",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'fù gài' (51-51). Pronounce both syllables with firm, crisp falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "复", "pinyin": "fù", "meaning_en": "repeat; complex", "distinction_note": "Lacks the top lid radical 覀 of 覆"},
                {"character": "履", "pinyin": "lǚ", "meaning_en": "shoe; fulfill", "distinction_note": "Has corpse radical 尸 enclosing 復"},
                {"character": "益", "pinyin": "yì", "meaning_en": "benefit; profit", "distinction_note": "Has 丷 and 一 over 皿 instead of 羊 in 盖"},
                {"character": "盂", "pinyin": "yú", "meaning_en": "basin; cup", "distinction_note": "Has 于 over 皿"}
            ],
            "etymological_cognates": [
                {"character": "罩", "pinyin": "zhào", "gloss_en": "cover; shade; hood"},
                {"character": "遮", "pinyin": "zhē", "gloss_en": "block; screen"},
                {"character": "掩", "pinyin": "yǎn", "gloss_en": "cover; conceal"},
                {"character": "蒙", "pinyin": "méng", "gloss_en": "drape; blindfold"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "覆盖 denotes spreading over a surface physically, or extending operational telecom/policy reach over a population or geographic territory.",
            "contrasts": [
                {"id": "1", "compared_word": "覆盖 vs. 笼罩", "pinyin": "lǒngzhào", "analysis": "笼罩 is poetic/descriptive for atmospheric mist, fog, darkness, or mood enveloping a place ('夜幕笼罩', '大雾笼罩'), while 覆盖 is factual and measurable ('5G覆盖')."},
                {"id": "2", "compared_word": "覆盖 vs. 包括", "pinyin": "bāokuò", "analysis": "包括 indicates structural membership or logical containment of elements ('费用包括税金'), while 覆盖 emphasizes geographical span or reach."},
                {"id": "3", "compared_word": "覆盖 vs. 淹没", "pinyin": "yānmò", "analysis": "淹没 means being physically submerged underwater or drowned out by loud noise ('洪水淹没农田'), whereas 覆盖 simply blankets the top."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着第五代移动通信技术的深入推进，中国已经建成了全球规模最大的高速宽带网络。即使在崇山峻岭环抱的偏远高原村落，高速无线网络信号也实现了无缝覆盖，让大山深处的孩子们能够与一线城市学生同上一堂名师网课。",
                "pinyin": "Suízhe dì-wǔ dài yídòng tōngxìn jìshù de shēnrù tuījìn, Zhōngguó yǐjīng jiànchéngle quánqiú guīmó zuìdà de gāosù kuāndài wǎngluò. Jíshǐ zài chóngshān-jùnlǐng huánbào de piānyuǎn gāoyuán cūnluò, gāosù wúxiàn wǎngluò xìnhào yě shíxiànle wúfèng fùgài, ràng dàshān shēnchù de háizimen nénggòu yǔ yīxiàn chéngshì xuésheng tóng shàng yī táng míngshī wǎngkè.",
                "en": "With the deep rollout of 5G, China has built the world's largest broadband network. Even in remote plateau villages, high-speed wireless signals achieve seamless coverage, allowing mountain children to share live classes with urban peers.",
                "es": "Con el despliegue del 5G, China ha erigido la mayor red de banda ancha del planeta. Incluso en aldeas remotas de montaña, la señal inalámbrica ofrece cobertura total permitiendo a los niños compartir clases en línea con alumnos de las metrópolis."
            },
            {
                "id": "#2",
                "hanzi": "经过持续数十年的植树造林与退耕还林工程，三北防护林体系有效遏制了北方沙尘暴的肆虐侵袭。郁郁葱葱的防护林带像绿色巨龙般覆盖在辽阔荒漠边缘，区域森林覆盖率显著攀升，构筑起抵御风沙生态退化的坚实屏障。",
                "pinyin": "Jīngguò chíxù shùshí nián de zhíshù zàolín yǔ tuìgēng huánlín gōngchéng, Sānběi Fánghùlín tǐxì yǒuxiào èzhìle běifāng shāchénbào de sìnüè qīnxí. Yùyù-cōngcōng de fánghùlíndài xiàng lǜsè jùlóng bān fùgài zài liáokuò huāngmò biānyuán, qūyù sēnlín fùgàilǜ xiǎnzhù pānshēng, gòuzhù qǐ dǐyù fēngshā shēngtài tuìhuà de jiānshí píngzhàng.",
                "en": "Decades of afforestation have checked sandstorms via the Three-North Shelter Forest. Verdant forest belts blanket the edges of vast deserts like a green dragon, lifting regional forest coverage and erecting an ecological shield against erosion.",
                "es": "Décadas de reforestación frenaron las tormentas de arena gracias a la Gran Muralla Verde. Exuberantes franjas boscosas cubren el linde de los desiertos elevando la cobertura forestal y levantando un baluarte contra la desertificación."
            }
        ]
    },

    # 17 移动
    {
        "id": "17",
        "hanzi": "移动",
        "pinyin": "yí dòng",
        "part_of_speech": "Verb / Adjective",
        "meanings_summary": {
            "en": "to move; shift; mobile; portable (telecom, internet)",
            "es": "mover; desplazarse; trasladar; móvil; portátil; telecomunicaciones móviles"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to change physical position or location; to shift or dislodge",
                "definition_es": "cambiar de lugar o posición; trasladarse de un punto a otro",
                "example_phrase": "缓慢移动 (move slowly)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "capable of moving, functioning while moving, or relating to cellular wireless communications",
                "definition_es": "que puede moverse o relativo a la tecnología inalámbrica y teléfonos celulares",
                "example_phrase": "移动互联网 (mobile internet)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "智能手机的飞速普及与移动通信网络的全面升级，深刻重塑了二十一世纪人类社会的日常生活方式。",
                "pinyin": "Zhìnéng shǒujī de fēisù pǔjí yǔ yídòng tōngxìn wǎngluò de quánmiàn shēngjí, shēnkè zhòngsùle èrshíyī shìjì rénlèi shèhuì de rìcháng shēnghuó fāngshì.",
                "en": "The rapid spread of smartphones and comprehensive upgrading of mobile networks have profoundly reshaped the daily lifestyle of 21st-century human society.",
                "es": "La popularización del teléfono inteligente y las redes móviles han reconfigurado profundamente el estilo de vida cotidiano del siglo XXI."
            },
            {
                "id": "#2",
                "hanzi": "护士小心翼翼地移动病床，将刚刚完成心脏手术的老人平稳推入安静舒适的重症监护室。",
                "pinyin": "Hùshi xiǎoxīn-yìyì de yídòng bìngchuáng, jiāng gānggāng wánchéng xīnzàng shǒushù de lǎorén píngwěn tuīrù ānjìng shūshì de zhòngzhèng jiānhùshì.",
                "en": "The nurse moved the hospital bed cautiously, smoothly wheeling the elderly patient who just completed heart surgery into the quiet ICU.",
                "es": "La enfermera movió la camilla con sumo cuidado trasladando al anciano recién operado del corazón hacia la sala de cuidados intensivos."
            }
        ],
        "collocations": [
            {"hanzi": "移动互联网", "en": "mobile Internet"},
            {"hanzi": "移动通信", "en": "mobile communications"},
            {"hanzi": "移动支付", "en": "mobile payment"},
            {"hanzi": "移动电话", "en": "mobile phone / cellular phone"},
            {"hanzi": "缓慢移动", "en": "move slowly"},
            {"hanzi": "禁止移动", "en": "prohibited from moving"}
        ],
        "idioms": [
            {"hanzi": "坚定不移", "pinyin": "jiān dìng bù yí", "meaning_en": "firm and unswerving; steadfast without moving"},
            {"hanzi": "潜移默化", "pinyin": "qián yí mò huà", "meaning_en": "influence subtly and imperceptibly over time"},
            {"hanzi": "移山填海", "pinyin": "yí shān tián hǎi", "meaning_en": "move mountains and fill seas; gigantic resolve"},
            {"hanzi": "轻举妄动", "pinyin": "qīng jǔ wàng dòng", "meaning_en": "act rashly and blindly without thought"}
        ],
        "character_decomposition": [
            {
                "character": "移",
                "pinyin": "yí",
                "meaning_en": "shift; move; alter; transplant",
                "meaning_es": "mover; trasladar; cambiar; trasplantar",
                "radical": "禾",
                "radical_meaning_en": "grain",
                "meaning_component": "禾 (grain seedlings) + 多 (many / sequential steps)",
                "sound_component": "多 (duō, many / phonetic yí)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Transplanting multiple green rice seedlings 禾 from nursery beds to wide water paddies; moving position.",
                "visual_mnemonic_story_en": "A farmer transplanting many rice shoots (禾) from bed to paddy shifts positions (移).",
                "visual_mnemonic_story_es": "Un campesino que trasplanta brotes de arroz (禾) a lo largo del campo desplaza su posición (移).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HDNIN",
                "traditional": ""
            },
            {
                "character": "动",
                "pinyin": "dòng",
                "meaning_en": "move; stir; act; mobilize; action",
                "meaning_es": "mover; actuar; movilizar; acción; dinámico",
                "radical": "力",
                "radical_meaning_en": "power / strength",
                "meaning_component": "云 (vapor clouds churning in heaven) + 力 (physical strength/force)",
                "sound_component": "重 (zhòng / phonetic in traditional 動)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Clouds churning 云 with dynamic physical power 力; exertion of muscular kinetic energy creating movement.",
                "visual_mnemonic_story_en": "Churning sky clouds (云) driven by muscular strength (力) set everything in motion (动).",
                "visual_mnemonic_story_es": "Las nubes que se arremolinan (云) impulsadas por la fuerza (力) se ponen en movimiento (动).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MMKS",
                "traditional": "動"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Shifting location like transplanted seedlings (移) propelled by kinetic power (动) is moving or mobile (移动).",
            "composite_memory_hook_es": "Trasladar de sitio (移) aplicando energía y dinamismo (动) es mover o desplazarse (移动).",
            "cultural_and_cognitive_roots": "From the agrarian custom of transplanting young rice shoots (移秧), transferred in modern times to cellular untethered mobility (移动网络).",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by fourth tone: 'yí dòng' (35-51). Rising second tone followed by brisk decisive drop."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "私", "pinyin": "sī", "meaning_en": "private; selfish", "distinction_note": "Has 厶 on right of 禾 instead of 多 in 移"},
                {"character": "税", "pinyin": "shuì", "meaning_en": "tax; duty", "distinction_note": "Has 兑 on right of 禾"},
                {"character": "劝", "pinyin": "quàn", "meaning_en": "advise; urge", "distinction_note": "Has 又 on left of 力 instead of 云 in 动"},
                {"character": "劫", "pinyin": "jié", "meaning_en": "rob; disaster", "distinction_note": "Has 去 on left of 力"}
            ],
            "etymological_cognates": [
                {"character": "挪", "pinyin": "nuó", "gloss_en": "shift; nudge"},
                {"character": "徙", "pinyin": "xǐ", "gloss_en": "migrate; relocate"},
                {"character": "迁", "pinyin": "qiān", "gloss_en": "move; transfer"},
                {"character": "转", "pinyin": "zhuǎn", "gloss_en": "turn; shift"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "移动 refers to changing spatial coordinates, or functions as a prefix for untethered wireless cellular technology.",
            "contrasts": [
                {"id": "1", "compared_word": "移动 vs. 运动", "pinyin": "yùndòng", "analysis": "运动 refers to physical exercise/athletics or sociopolitical campaigns ('体育运动', '群众运动'), while 移动 is changing physical position or mobile telecom."},
                {"id": "2", "compared_word": "移动 vs. 挪动", "pinyin": "nuódòng", "analysis": "挪动 specifically stresses minor, slow, or painstaking shifting over very small distances ('吃力地挪动脚步'), while 移动 is neutral and broad."},
                {"id": "3", "compared_word": "移动 vs. 迁移", "pinyin": "qiānyí", "analysis": "迁移 refers to large-scale relocation of populations, habitats, or plants ('人口迁移', '鸟类迁移'), while 移动 covers ordinary object movement."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "移动支付的全面普及深刻改变了现代人的消费习惯。如今出门只需携带一部智能手机，无论是乘坐公共交通工具还是在便利店购物，轻轻一扫便能瞬间完成结算，展现出无处不在的高效与便捷。",
                "pinyin": "Yídòng zhīfù de quánmiàn pǔjí shēnkè gǎibiànle xiàndàirén de xiāofèi xíguàn. Rújīn chūmén zhǐxū xiàidài yī bù zhìnéng shǒujī, wúlùn shì chéngzuò gōnggòng jiāotōng gōngjù háishì zài biànlìdiàn gòuwù, qīngqīng yī sǎo biàn néng shùnjiān wánchéng jiésuàn, zhǎnxiàn chū wúchù-bùzài de gāoxiào yǔ biànjié.",
                "en": "The ubiquity of mobile payment has profoundly reshaped modern consumer habits. Leaving home requires only a smartphone; riding transit or shopping at convenience stores settles instantly with a scan, demonstrating omnipresent convenience.",
                "es": "El pago móvil ha transformado los hábitos de compra modernos. Hoy basta salir con el móvil para abonar el transporte o comprar en tiendas escaneando un código, haciendo gala de una comodidad y rapidez asombrosas."
            },
            {
                "id": "#2",
                "hanzi": "在现代智能化仓储物流中心内部，数百台橙色自主移动搬运机器人穿梭往来于高耸的货架之间。机器人依托地面二维码与激光雷达导航精准移动，不仅彻底免去了人工繁重搬运的疲劳，更将货品分拣出库的准确率提升至惊人的极限水平。",
                "pinyin": "Zài xiàndài zhìnénghuà cāngchǔ wùliú zhōngxīn nèibù, shùbǎi tái chéngsè zìzhǔ yídòng bānyùn jīqìrén chuānsuō wǎnglái yú gāosǒng de huòjià zhījiān. Jīqìrén yītuō dīmiàn èrwéimǎ yǔ jīguāng léidá dǎoháng jīngzhǔn yídòng, bùjǐn chèdǐ miǎnqùle réngōng fánzhòng bānyùn de píláo, gèng jiāng huòpǐn fēnjiǎn chūkù de zhǔnquèlǜ tíshēng zhì jīngrén de jíxiàn shuǐpíng.",
                "en": "Inside smart logistics centers, hundreds of orange autonomous mobile robots weave through towering shelves. Navigating precisely via QR codes and LiDAR, they eliminate exhausting manual lifting and elevate sorting accuracy to astonishing heights.",
                "es": "En los centros logísticos inteligentes, robots móviles autónomos de color naranja circulan entre altas estanterías. Guiados por códigos y sensores láser, eliminan el esfuerzo manual y elevan la precisión de empaquetado a cotas asombrosas."
            }
        ]
    },

    # 18 通信
    {
        "id": "18",
        "hanzi": "通信",
        "pinyin": "tōng xìn",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to communicate; correspond by mail/signals; telecommunications; message transmission",
            "es": "comunicarse; cartearse; telecomunicaciones; transmisión de señales o mensajes"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to exchange letters, messages, or electronic signals between distant parties",
                "definition_es": "mantener correspondencia por carta, mensajes o intercambiar señales electrónicas a distancia",
                "example_phrase": "保持通信 (keep up correspondence)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the science, technology, industry, or system of transmitting information over distance via cable, radio, or satellite",
                "definition_es": "tecnología, sector o sistema de transmisión de información a distancia mediante cables, ondas o satélites",
                "example_phrase": "卫星通信 (satellite telecommunications)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "微信以其极致清晰的语音与视频通信功能，彻底颠覆了海外华人与国内亲朋好友跨洋联络的传统方式。",
                "pinyin": "Wēixìn yǐ qí jízhì qīngxī de yǔyīn yǔ shìpín tōngxìn gōngnéng, chèdǐ diānfùle hǎiwài Huárén yǔ guónèi qīnpéng hǎoyǒu kuàyáng liánluò de chuántǒng fāngshì.",
                "en": "With its exceptionally clear voice and video telecommunications features, WeChat completely overturned traditional overseas communication between Chinese diaspora and domestic families.",
                "es": "Con llamadas de voz y vídeo nítidas, WeChat transformó la forma en que los chinos en el extranjero contactan con sus allegados en la patria."
            },
            {
                "id": "#2",
                "hanzi": "即便远隔重洋数万公里，两位老学者几十年间始终坚持通过书信保持密切通信，探讨学术前沿问题。",
                "pinyin": "Jíbiàn yuǎngé chóngyáng shùwàn gōnglǐ, liǎng wèi lǎo xuézhě jǐshí nián jiān shǐzhōng jiānchí tōngguò shūxìn bǎochí mìqiè tōngxìn, tàntǎo xuéshù qiányán wèntí.",
                "en": "Even separated by oceans over tens of thousands of kilometers, the two senior scholars maintained close correspondence by letter for decades, discussing frontiers of learning.",
                "es": "Pese a vivir separados por océanos a miles de kilómetros, los dos veteranos eruditos mantuvieron correspondencia epistolar debatiendo dilemas académicos."
            }
        ],
        "collocations": [
            {"hanzi": "通信网络", "en": "telecommunications network"},
            {"hanzi": "卫星通信", "en": "satellite communications"},
            {"hanzi": "移动通信", "en": "mobile communications"},
            {"hanzi": "通信技术", "en": "communications technology"},
            {"hanzi": "保持通信", "en": "maintain correspondence / keep in touch"},
            {"hanzi": "通信卫星", "en": "communications satellite"}
        ],
        "idioms": [
            {"hanzi": "音信杳然", "pinyin": "yīn xìn yǎo rán", "meaning_en": "no news whatsoever; completely out of communication"},
            {"hanzi": "四通八达", "pinyin": "sì tōng bā dá", "meaning_en": "accessible from all directions; extending far and wide"},
            {"hanzi": "通风报信", "pinyin": "tōng fēng bào xìn", "meaning_en": "tip off; secretly pass information to someone"},
            {"hanzi": "鸿雁传书", "pinyin": "hóng yàn chuán shū", "meaning_en": "wild geese delivering letters; postal correspondence"}
        ],
        "character_decomposition": [
            {
                "character": "通",
                "pinyin": "tōng",
                "meaning_en": "pass through; connect; open; unblocked; thorough",
                "meaning_es": "pasar; conectar; abierto; despejado; expedito",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (movement along path) + 甬 (flourishing bell stalk / unblocked channel)",
                "sound_component": "甬 (yǒng, canal / phonetic nuance)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Moving along footsteps 辶 down an unblocked tunnel or channel 甬; unobstructed, clear, through-and-through communication.",
                "visual_mnemonic_story_en": "Steps traveling along a pathway (辶) through an open clear tunnel (甬) connect unobstructed (通).",
                "visual_mnemonic_story_es": "Los pasos que avanzan por el sendero (辶) a través de un canal expedito (甬) conectan sin trabas (通).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YNIB",
                "traditional": ""
            },
            {
                "character": "信",
                "pinyin": "xìn",
                "meaning_en": "letter; message; trust; faith; believe",
                "meaning_es": "carta; mensaje; fe; confianza; creer",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / speaker) + 言 (speech / words)",
                "sound_component": "Self-phonetic xìn",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 standing faithfully behind their spoken words 言; trustworthiness, sincerity, and by extension messages and letters sent in good faith.",
                "visual_mnemonic_story_en": "A righteous person (亻) whose spoken words (言) are genuine sends a faithful letter (信).",
                "visual_mnemonic_story_es": "Una persona honrada (亻) cuyas palabras (言) son sinceras envía una misiva de confianza (信).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OYMR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Connecting unobstructed pathways (通) to deliver faithful messages and letters (信) is telecommunications (通信).",
            "composite_memory_hook_es": "Abrir vías expeditas (通) para hacer llegar mensajes y misivas de confianza (信) es la telecomunicación (通信).",
            "cultural_and_cognitive_roots": "Derived from classical frontier relay postal posts (驿传): sending reliable runners to pass letters (信) through connecting roads (通达).",
            "tone_sandhi_and_pitch_modulation": "First tone followed by fourth tone: 'tōng xìn' (55-51). Hold level high tone 55, then fall sharply to 51."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "痛", "pinyin": "tòng", "meaning_en": "pain; ache", "distinction_note": "Has illness radical 疒 on outside instead of walk 辶 in 通"},
                {"character": "桶", "pinyin": "tǒng", "meaning_en": "bucket; barrel", "distinction_note": "Has wood radical 木 on left of 甬"},
                {"character": "伸", "pinyin": "shēn", "meaning_en": "stretch; extend", "distinction_note": "Has 申 on right of 亻 instead of 言 in 信"},
                {"character": "件", "pinyin": "jiàn", "meaning_en": "piece; document", "distinction_note": "Has ox 牛 on right of 亻"}
            ],
            "etymological_cognates": [
                {"character": "达", "pinyin": "dá", "gloss_en": "reach; communicate"},
                {"character": "讯", "pinyin": "xùn", "gloss_en": "inquire; dispatch message"},
                {"character": "讯", "pinyin": "xùn", "gloss_en": "telecom signal"},
                {"character": "电", "pinyin": "diàn", "gloss_en": "electricity; electronic telegraph"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "通信 encompasses technical telecommunications transmission networks, as well as postal/epistolary correspondence.",
            "contrasts": [
                {"id": "1", "compared_word": "通信 vs. 通讯", "pinyin": "tōngxùn", "analysis": "通信 highlights technical point-to-point electronic transmission of signals and mutual letter-writing, while 通讯 can also mean a journalistic news dispatch or feature report ('通讯报道')."},
                {"id": "2", "compared_word": "通信 vs. 联络", "pinyin": "liánluò", "analysis": "联络 focuses on maintaining human social touch or building networking bridges ('联络感情'), whereas 通信 refers to functional data or postal transmission."},
                {"id": "3", "compared_word": "通信 vs. 交流", "pinyin": "jiāoliú", "analysis": "交流 emphasizes reciprocal exchange of ideas, feelings, or culture ('文化交流'), whereas 通信 is the transmission medium itself."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "量子通信技术是保障未来信息安全的战略制高点。利用量子纠缠效应传输加密密钥，能够在物理层面上实现绝不被窃听与破译的安全通信，为国防军工、国家金融网络与关键基础设施构筑起牢不可破的量子防护盾牌。",
                "pinyin": "Liàngzǐ tōngxìn jìshù shì bǎozhàng wèilái xìnxī ānquán de zhànlüè zhìgāodiǎn. Lìyòng liàngzǐ jiūchán xiàoyìng chuánshū jiāmì mìyuè, nénggòu zài wùlǐ céngmiàn shàng shíxiàn juébù bèi qiètīng yǔ pòyì de ānquán tōngxìn, wèi guófáng jūngōng, guójiā jīnróng wǎngluò yǔ guānjiàn jīchǔ shèshī gòuzhù qǐ láobùkěpò de liàngzǐ fánghù dùnpái.",
                "en": "Quantum communication represents the strategic high ground of information security. Using entanglement to transmit encryption keys, it enables unhackable transmissions physically, creating an impenetrable shield for defense and finance.",
                "es": "La comunicación cuántica es la cúspide de la ciberseguridad. Al emplear el entrelazamiento cuántico para transmitir claves cifradas, garantiza una transmisión invulnerable a escuchas, blindando redes de defensa y finanzas."
            },
            {
                "id": "#2",
                "hanzi": "在人迹罕至的远洋航行与极地科考探险中，可靠的卫星通信系统是科考队员维系外界联系的唯一生命线。科考队员不仅能够依靠海事卫星实时上传海洋生态监测数据，还能在佳节之夜与远隔万里的家人进行高清视频通话互道平安。",
                "pinyin": "Zài rénjì-hǎnji de yuǎnyáng hángxíng yǔ jídì kěkǎo tànxiǎn zhōng, kěkào de wèixīng tōngxìn xìtǒng shì kěkǎo duìyuán wéixì wàijiè liánxì de wéiyī shēngmìngxiàn. Kěkǎo duìyuán bùjǐn nénggòu yīkào hǎishì wèixīng shíshí shàngchuán hǎiyáng shēngtài jiāncè shùjù, hái néng zài jiājié zhī yè yǔ yuǎngé wànlǐ de jiārén jìnxíng gāoqīng shìpín tōnghuà hùdào píng'ān.",
                "en": "In uninhabited ocean expeditions and polar surveys, satellite communication is the sole lifeline connecting teams with the world. Scientists upload marine ecological data via satellite while making HD video calls home during holidays.",
                "es": "En expediciones oceánicas y polares, la comunicación por satélite es el único cordón umbilical con el mundo. Los científicos transmiten datos oceanográficos y mantienen videoconferencias con sus familias en noches festivas."
            }
        ]
    },

    # 19 应用
    {
        "id": "19",
        "hanzi": "应用",
        "pinyin": "yìng yòng",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to apply; put to practical use; application; app; software application",
            "es": "aplicar; poner en práctica; aplicación; app informática; uso práctico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to put theoretical knowledge, principles, techniques, or scientific findings into practical implementation",
                "definition_es": "poner en práctica conocimientos teóricos, fórmulas o principios técnicos en situaciones reales",
                "example_phrase": "应用新技术 (apply new technologies)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a computer software program or mobile phone app designed to perform specific user functions",
                "definition_es": "programa informático o aplicación móvil (app) diseñada para tareas concretas del usuario",
                "example_phrase": "下载手机应用 (download mobile app)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "作为一款集即时通讯、移动支付与社交分享于一体的超级应用，微信极大简化了现代人的数字生活。",
                "pinyin": "Zuòwéi yī kuǎn jí jíshí tōngxùn, yídòng zhīfù yǔ shèjiāo fēnxiǎng yú yītǐ de chāojí yìngyòng, Wēixìn jídà jiǎnhuàle xiàndàirén de shùzì shēnghuó.",
                "en": "As a super-app integrating instant messaging, mobile payment, and social sharing, WeChat has drastically simplified modern digital life.",
                "es": "Como súper-aplicación que integra mensajería, pagos móviles y redes sociales, WeChat ha simplificado enormemente la vida digital moderna."
            },
            {
                "id": "#2",
                "hanzi": "科研人员致力于将人工智能算法深入应用到医学影像智能识别领域，显著提高了早期癌症的诊断准确率。",
                "pinyin": "Kēyán rényuán zhìlì yú jiāng réngōng zhìnéng suànfǎ shēnrù yìngyòng dào yīxué yǐngxiàng zhìnéng shíbié lǐngyù, xiǎnzhù tígāole zǎoqī áizhèng de zhěnduàn zhǔnquèlǜ.",
                "en": "Researchers are devoted to deeply applying AI algorithms to medical image recognition, significantly improving early cancer diagnostic accuracy.",
                "es": "Los investigadores aplican algoritmos de inteligencia artificial al diagnóstico por imagen, elevando la precisión en la detección precoz de tumores."
            }
        ],
        "collocations": [
            {"hanzi": "应用软件", "en": "application software / app"},
            {"hanzi": "手机应用", "en": "mobile application / app"},
            {"hanzi": "广泛应用", "en": "widely applied / extensive application"},
            {"hanzi": "实际应用", "en": "practical application"},
            {"hanzi": "应用科学", "en": "applied sciences"},
            {"hanzi": "开发应用", "en": "develop applications"}
        ],
        "idioms": [
            {"hanzi": "洋为中用", "pinyin": "yáng wéi zhōng yòng", "meaning_en": "make foreign things serve China's needs"},
            {"hanzi": "古为今用", "pinyin": "gǔ wéi jīn yòng", "meaning_en": "make the past serve the present"},
            {"hanzi": "学以致用", "pinyin": "xué yǐ zhì yòng", "meaning_en": "learn in order to practice and apply"},
            {"hanzi": "物尽其用", "pinyin": "wù jìn qí yòng", "meaning_en": "make the best and fullest use of all materials"}
        ],
        "character_decomposition": [
            {
                "character": "应",
                "pinyin": "yìng",
                "meaning_en": "respond; echo; correspond; should; cope with",
                "meaning_es": "responder; corresponder; deber; reaccionar",
                "radical": "广",
                "radical_meaning_en": "shelter / hall",
                "meaning_component": "广 (hall / room acoustic) + 隹/心 (bird answering call from heart)",
                "sound_component": "Historical phonetic nuance in 應",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A voice calling into a wide hall 广 and receiving an immediate matching acoustic echo; responding appropriately to practical conditions.",
                "visual_mnemonic_story_en": "A shout echoed under a wide hall roof (广) answers promptly to match reality (应).",
                "visual_mnemonic_story_es": "Un eco que resuena bajo el pabellón (广) dando respuesta precisa a la llamada (应).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IF",
                "traditional": "應"
            },
            {
                "character": "用",
                "pinyin": "yòng",
                "meaning_en": "use; employ; apply; utility",
                "meaning_es": "usar; emplear; aplicar; utilizar; utilidad",
                "radical": "用",
                "radical_meaning_en": "use",
                "meaning_component": "A framed implement ready in hand for ritual or functional work",
                "sound_component": "Self-phonetic yòng",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A tool or container put into active operation; represents functional utility, deployment, and practical use.",
                "visual_mnemonic_story_en": "A wooden tool bucket held in hand put to active functional use (用).",
                "visual_mnemonic_story_es": "El armazón de una herramienta listo para prestar utilidad práctica inmediata (用).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BQI",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Responding appropriately to practical needs (应) by deploying useful functional tools (用) is application (应用).",
            "composite_memory_hook_es": "Dar respuesta a necesidades reales (应) haciendo uso de herramientas útiles (用) es aplicar o una aplicación (应用).",
            "cultural_and_cognitive_roots": "Derived from traditional Confucian practical learning (经世致用): scholarship must not remain in abstract clouds, but must be actively applied (应用) to social benefit.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'yìng yòng' (51-51). Pronounce both syllables with firm, crisp falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "庄", "pinyin": "zhuāng", "meaning_en": "village; solemn", "distinction_note": "Has 土 under 广 instead of dots and strokes in 应"},
                {"character": "床", "pinyin": "chuáng", "meaning_en": "bed", "distinction_note": "Has wood 木 under 广"},
                {"character": "甩", "pinyin": "shuǎi", "meaning_en": "fling; swing", "distinction_note": "Bottom stroke hooks out sideways like a tail, unlike 用"},
                {"character": "角", "pinyin": "jiǎo", "meaning_en": "horn; corner", "distinction_note": "Has slanted peak on top"}
            ],
            "etymological_cognates": [
                {"character": "使", "pinyin": "shǐ", "gloss_en": "employ; use"},
                {"character": "行", "pinyin": "xíng", "gloss_en": "put into action"},
                {"character": "操", "pinyin": "cāo", "gloss_en": "operate; grasp"},
                {"character": "效", "pinyin": "xiào", "gloss_en": "render effect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "应用 means translating theories or tools into practical use, or refers specifically to software applications (apps).",
            "contrasts": [
                {"id": "1", "compared_word": "应用 vs. 运用", "pinyin": "yùnyòng", "analysis": "运用 emphasizes skillful, agile, and flexible mastery of rules, tactics, or language ('熟练运用语言'), while 应用 emphasizes the direct practical implementation of technology or an app."},
                {"id": "2", "compared_word": "应用 vs. 使用", "pinyin": "shǐyòng", "analysis": "使用 is the everyday generic term for operating any physical tool, money, or vehicle ('使用电脑'), while 应用 is broader for applied sciences and software systems."},
                {"id": "3", "compared_word": "应用 vs. 适用", "pinyin": "shìyòng", "analysis": "适用 is an adjective meaning suitable, applicable, or fitting under specific laws or parameters ('该条款不适用'), while 应用 is active."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在智能移动终端深度融入日常生活的当下，手机应用生态正展现出前所未有的繁荣景象。从在线政务办理到跨境电商购物，各式各样的应用程序不仅极大地节约了人们的办事成本，更重构了现代城市的公共服务体系。",
                "pinyin": "Zài zhìnéng yídòng zhòngduān shēndù róngrù rìcháng shēnghuó de dāngxià, shǒujī yìngyòng shēngtài zhèng zhǎnxiàn chū qiánsuǒwèiyǒu de fánróng jǐngxiàng. Cóng zàixiàn zhèngwù bànlǐ dào kuàjìng diànshāng gòumǎi, gèshì-gèyàng de yìngyòng chéngxù bùjǐn jídà de jiéyuēle rénmen de bànshì chéngběn, gèng chónggòule xiàndài chéngshì de gōnggòng fúwù tǐxì.",
                "en": "With smart terminals woven into daily life, mobile app ecosystems are booming. From online public services to cross-border e-commerce, diverse applications cut errands costs and reconfigure municipal public service systems.",
                "es": "Con el móvil integrado en la rutina, el ecosistema de apps vive un florecimiento sin precedentes. De trámites administrativos al comercio transfronterizo, las aplicaciones agilizan gestiones redefiniendo los servicios públicos urbanos."
            },
            {
                "id": "#2",
                "hanzi": "基础科学研究向工业实际应用的转化周期正在全球范围内大幅缩短。各大研究型高校纷纷成立产业孵化基地，推动前沿实验室里的尖端技术成果尽快应用到先进制造与新能源生产一线，将科技论文转化为驱动经济高质量发展的实际生产力。",
                "pinyin": "Jīchǔ kēxué yánjiū xiàng gōngyè shíjì yìngyòng de zhuǎnhuà zhōuqī zhèng zài quánqiú fànwéi nèi dàfú suōduǎn. Gè dà yánjiūxíng gāoxiào fēnfēn chénglì chǎnyè fūhuà jīdì, tuīdòng qiányán shíyànshì lǐ de jiānduān jìshù chéngguǒ jǐnkuài yìngyòng dào xiānjìn zhìzào yǔ xīnnéngyuán shēngchǎn yīxiàn, jiāng kējì lùnwén zhuǎnhuà wéi qūdòng jīngjì gāozhìliàng fāzhǎn de shíjì shēngchǎnlì.",
                "en": "The cycle from basic science research to industrial application is shrinking globally. Research universities establish incubators, pushing lab innovations to manufacturing and green energy lines, turning papers into economic productivity.",
                "es": "El ciclo que media entre la ciencia básica y su aplicación industrial se acorta en el mundo. Las universidades fundan incubadoras para llevar avances de laboratorio a la industria y la energía limpia, transformando estudios en motor económico."
            }
        ]
    },

    # 20 企业
    {
        "id": "20",
        "hanzi": "企业",
        "pinyin": "qǐ yè",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "enterprise; business; company; corporation",
            "es": "empresa; compañía; corporación mercantil; firma comercial"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an economic organization engaged in manufacturing, trading, or providing commercial services for profit and social value",
                "definition_es": "organización económica dedicada a actividades industriales, mercantiles o de servicios con fines productivos",
                "example_phrase": "跨国企业 (multinational enterprise)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "面对日趋激烈的海外市场竞争，中国高科技企业唯有持续加大自主研发投入，才能在全球产业链中赢得尊重。",
                "pinyin": "Miànduì rìqū jīliè de hǎiwài shìchǎng jìngzhēng, Zhōngguó gāokējì qǐyè wéiyǒu chíxù jiādà zìzhǔ yánfā tóurù, cáinéng zài quánqiú chǎnyèliàn zhōng yíngdé zūnzhòng.",
                "en": "Facing increasingly fierce competition in overseas markets, Chinese high-tech enterprises can win respect in global industrial chains only by steadily increasing R&D.",
                "es": "Ante la competencia en ultramar, las tecnológicas chinas solo ganarán respeto en la cadena de valor global redoblando su inversión en I+D."
            },
            {
                "id": "#2",
                "hanzi": "政府出台了多项减税降费扶持政策，旨在有效减轻中小微企业的经营成本与融资负担。",
                "pinyin": "Zhèngfǔ chūtáile duō xiàng jiǎnshuì jiàngfèi fúchí zhèngcè, zhǐzài yǒuxiào jiǎnqīng zhōng-xiǎo-wēi qǐyè de jīngyíng chéngběn yǔ róngzī fùdān.",
                "en": "The government introduced multiple tax and fee cut policies aimed at effectively reducing operating costs and financing burdens for micro, small, and medium enterprises.",
                "es": "Las autoridades promulgaron exenciones fiscales para aliviar los costes operativos y cargas de financiación de las pequeñas y medianas empresas."
            }
        ],
        "collocations": [
            {"hanzi": "国有企业", "en": "state-owned enterprise (SOE)"},
            {"hanzi": "跨国企业", "en": "multinational corporation (MNC)"},
            {"hanzi": "民营企业", "en": "private enterprise"},
            {"hanzi": "企业文化", "en": "corporate culture"},
            {"hanzi": "企业形象", "en": "corporate image"},
            {"hanzi": "中小企业", "en": "small and medium-sized enterprises (SMEs)"}
        ],
        "idioms": [
            {"hanzi": "万象更新", "pinyin": "wàn xiàng gēng xīn", "meaning_en": "everything takes on a completely fresh new look"},
            {"hanzi": "百折不挠", "pinyin": "bǎi zhé bù náo", "meaning_en": "indomitable and unyielding despite repeated setbacks"},
            {"hanzi": "蒸蒸日上", "pinyin": "zhēng zhēng rì shàng", "meaning_en": "thriving, prosperous, and flourishing day by day"},
            {"hanzi": "基业长青", "pinyin": "jī yè cháng qīng", "meaning_en": "evergreen foundation; enduring business longevity"}
        ],
        "character_decomposition": [
            {
                "character": "企",
                "pinyin": "qǐ",
                "meaning_en": "stand on tiptoe; look forward to; scheme; business",
                "meaning_es": "ponerse de puntillas; anhelar; planear; empresa",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "人 (person) + 止 (foot standing on tiptoe to gaze into distance)",
                "sound_component": "Historical phonetic nuance",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A person 人 standing on tiptoe on their feet 止 to gaze far into the future; represents vision, anticipation, ambition, and enterprise.",
                "visual_mnemonic_story_en": "A visionary person (人) standing on tiptoes on their feet (止) gazes far into future markets (企).",
                "visual_mnemonic_story_es": "Una persona visionaria (人) que se alza de puntillas sobre sus pies (止) oteando el porvenir (企).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "OYM",
                "traditional": ""
            },
            {
                "character": "业",
                "pinyin": "yè",
                "meaning_en": "business; profession; trade; karma; estate",
                "meaning_es": "negocio; profesión; oficio; industria; patrimonio",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "Originally a wooden stand with notched boards used to hang large ceremonial bronze bells and drums",
                "sound_component": "Archaic phonetic yè",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Carved notched stand for grand ritual musical instruments; extended to grand accomplishments, industries, professions, and corporate undertakings.",
                "visual_mnemonic_story_en": "A majestic framed stand supporting ceremonial instruments symbolizes lifelong business endeavors (业).",
                "visual_mnemonic_story_es": "Un sólido atril labrado para campanas ceremoniales que simboliza las grandes empresas y oficios (业).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TC",
                "traditional": "業"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Looking forward with strategic vision on tiptoe (企) to build an enduring industrial foundation (业) creates an enterprise (企业).",
            "composite_memory_hook_es": "Mirar con visión de futuro (企) para erigir un próspero patrimonio productivo (业) forja una empresa (企业).",
            "cultural_and_cognitive_roots": "Coined during modernization to translate 'enterprise': 企 expresses visionary planning and entrepreneurial ambition, while 业 grounds it in durable trade.",
            "tone_sandhi_and_pitch_modulation": "Third tone followed by fourth tone: 'qǐ yè' (214-51). Low dip followed by strong, decisive drop."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "乞", "pinyin": "qǐ", "meaning_en": "beg; plead", "distinction_note": "Lacks the bottom horizontal base stroke of 止 in 企"},
                {"character": "止", "pinyin": "zhǐ", "meaning_en": "stop; halt", "distinction_note": "Lacks the top person 人 radical of 企"},
                {"character": "亚", "pinyin": "yà", "meaning_en": "Asia; second", "distinction_note": "Has two horizontal bars enclosing center, unlike vertical strokes of 业"},
                {"character": "严", "pinyin": "yán", "meaning_en": "strict; severe", "distinction_note": "Has top bars and slanted bottom stroke"}
            ],
            "etymological_cognates": [
                {"character": "商", "pinyin": "shāng", "gloss_en": "commerce; business"},
                {"character": "司", "pinyin": "sī", "gloss_en": "manage; company division"},
                {"character": "行", "pinyin": "háng", "gloss_en": "trade; firm"},
                {"character": "店", "pinyin": "diàn", "gloss_en": "shop; store"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "企业 refers to a formal economic, commercial, industrial, or corporate entity engaged in production, services, or trade.",
            "contrasts": [
                {"id": "1", "compared_word": "企业 vs. 公司", "pinyin": "gōngsī", "analysis": "公司 is the specific legal structural form (corporation, LLC, etc.), whereas 企业 is broader and economic in nature encompassing state factories, farms, and conglomerates."},
                {"id": "2", "compared_word": "企业 vs. 事业", "pinyin": "shìyè", "analysis": "事业单位 refers to non-profit public sector institutions (schools, public hospitals, museums), whereas 企业 operates for economic sustainability and profit."},
                {"id": "3", "compared_word": "企业 vs. 行业", "pinyin": "hángyè", "analysis": "行业 designates an entire economic industry or branch of business (e.g. IT industry, steel industry), while 企业 is an individual firm within an industry."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "企业是推动国家经济高质量发展和技术创新的关键市场微观主体。面对全球绿色低碳转型的历史趋势，广大制造企业主动加大环保设备改造投入，以精益求精的工匠精神提升产品附加值，为实现可持续发展目标贡献了澎湃动能。",
                "pinyin": "Qǐyè shì tuīdòng guójiā jīngjì gāozhìliàng fāzhǎn yǔ jìshù chuàngxīn de guānjiàn shìchǎng wēiguān zhǔtǐ. Miànduì quánqiú lǜsè dītàn zhuǎnxíng de lìshǐ qūshì, guǎngdà zhìzào qǐyè zhǔdòng jiādà huánbǎo shèbèi gǎizào tóurù, yǐ jīngyìqiújīng de gōngjiàng jīngshén tíshēng chǎnpǐn fùjiāzhí, wèi shíxiàn kěchíxù fāzhǎn mùbiāo gòngxiànle péngbài dòngnéng.",
                "en": "Enterprises are the key market micro-entities driving economic growth and tech innovation. Confronting green low-carbon trends, manufacturers invest in eco-friendly upgrades, elevating product value with craftsmanship to boost sustainable development.",
                "es": "Las empresas son el motor microeconómico que impulsa el crecimiento y la innovación técnica. Ante la transición ecológica, las fábricas renuevan su maquinaria elevando el valor añadido del producto con rigor artesano."
            },
            {
                "id": "#2",
                "hanzi": "一家卓越的企业不仅能在商业竞争中创造优异的经济效益，更应当在社会公益、员工福祉与生态保护方面勇于承担责任。将崇高的企业社会责任深深融入企业文化之中，才能赢得全社会的长久赞誉，在风云变幻的商海中基业长青。",
                "pinyin": "Yī jiā zhuóyuè de qǐyè bùjǐn néng zài shāngyè jìngzhēng zhōng chuàngzào yōuyì de jīngjì xiàoyì, gèng yīngdāng zài shèhuì gōngyì, yuángōng fúzhǐ yǔ shēngtài bǎohù fāngmiàn yǒngyú chéngdān zérèn. Jiāng chónggāo de qǐyè shèhuì zérèn shēndēn róngrù qǐyè wénhuà zhīzhōng, cáinéng yíngdé quán shèhuì de chángjiǔ zànyù, zài fēngyún-biànhuàn de shānghǎi zhōng jīyè-chángqīng.",
                "en": "An outstanding enterprise not only generates stellar economic returns in business competition, but also shoulders duties in charity, employee welfare, and ecology. Embedding corporate social responsibility into culture ensures lasting success.",
                "es": "Una empresa sobresaliente no solo genera beneficios económicos, sino que asume compromisos en filantropía, bienestar laboral y ecología. Arraigar la responsabilidad social corporativa en su cultura garantiza un prestigio duradero."
            }
        ]
    }
]

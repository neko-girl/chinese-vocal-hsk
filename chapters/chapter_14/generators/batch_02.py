# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 通常
    {
        "id": "11",
        "hanzi": "通常",
        "pinyin": "tōng cháng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "usually; generally; normally; ordinary",
            "es": "generalmente; por lo general; normalmente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "under normal or customary conditions; as a general rule",
                "definition_es": "en condiciones habituales o normales; por regla general",
                "example_phrase": "通常情况下 (under normal circumstances)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在老北京四合院中，北面的正房通常留给家中辈分最高的老人居住，以示敬重。",
                "pinyin": "Zài lǎo Běijīng sìhéyuàn zhōng, běimiàn de zhèngfáng tōngcháng liú gěi jiāzhōng bèifèn zuìgāo de lǎorén jūzhù, yǐ shì jìngzhòng.",
                "en": "In old Beijing courtyards, the north main room is usually reserved for the family's senior elders as a mark of respect.",
                "es": "En los patios tradicionales de Pekín, la sala principal del norte suele reservarse a los ancianos de mayor jerarquía familiar en señal de respeto."
            },
            {
                "id": "#2",
                "hanzi": "若没有突发状况，国际客运航班通常会按照既定时刻表准点起飞与降落。",
                "pinyin": "Ruò méiyǒu tūfā zhuàngkuàng, guójì kèyùn hángbān tōngcháng huì ànzhào jìdìng shíkèbiǎo zhǔndiǎn qǐfēi yǔ jiàngluò.",
                "en": "Barring unexpected emergencies, international passenger flights usually take off and land punctually per the schedule.",
                "es": "Salvo imprevistos de última hora, los vuelos comerciales internacionales suelen despegar y aterrizar con puntualidad según el horario fijado."
            }
        ],
        "collocations": [
            {"hanzi": "通常情况下", "en": "under normal circumstances"},
            {"hanzi": "通常认为", "en": "generally considered"},
            {"hanzi": "通常做法", "en": "usual practice"},
            {"hanzi": "按照通常", "en": "according to the usual norm"},
            {"hanzi": "通常规律", "en": "general rule / normal pattern"},
            {"hanzi": "超越通常", "en": "exceed what is normal"}
        ],
        "idioms": [
            {"hanzi": "习以为常", "pinyin": "xí yǐ wéi cháng", "meaning_en": "accustomed to through long habit"},
            {"hanzi": "屡见不鲜", "pinyin": "lǚ jiàn bù xiān", "meaning_en": "common sight; not at all novel"},
            {"hanzi": "司空见惯", "pinyin": "sī kōng jiàn guàn", "meaning_en": "familiar sight; common daily occurrence"},
            {"hanzi": "通情达理", "pinyin": "tōng qíng dá lǐ", "meaning_en": "fair-minded, sensible, and reasonable"}
        ],
        "character_decomposition": [
            {
                "character": "通",
                "pinyin": "tōng",
                "meaning_en": "pass through; common; general",
                "meaning_es": "pasar a través; común; general",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (motion) + 甬 (flowing corridor/path)",
                "sound_component": "甬 (yǒng)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Motion 辶 moving unobstructed along a paved thoroughfare 甬; implies uninterrupted flow and broad currency.",
                "visual_mnemonic_story_en": "Moving smoothly along an open road (辶) with nothing blocking the passage (通).",
                "visual_mnemonic_story_es": "Avanzar con fluidez por un camino expedito (辶) sin obstáculos que cierren el paso (通).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YNIB",
                "traditional": "通"
            },
            {
                "character": "常",
                "pinyin": "cháng",
                "meaning_en": "frequent; regular; constant",
                "meaning_es": "frecuente; regular; constante",
                "radical": "巾",
                "radical_meaning_en": "cloth / towel",
                "meaning_component": "尚 (elevated roof/spire) + 巾 (standard hanging banner)",
                "sound_component": "尚 (shàng)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A standard skirt or banner 巾 hung prominently; represents constancy, enduring routines, and norms.",
                "visual_mnemonic_story_en": "A distinctive banner (巾) hung permanently aloft that serves as an enduring everyday standard (常).",
                "visual_mnemonic_story_es": "Un estandarte ceremonial (巾) suspendido de modo permanente como norma constante de la vida diaria (常).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "FBRB",
                "traditional": "常"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Moving openly through (通) enduring daily customs (常) reflects what usually (通常) happens.",
            "composite_memory_hook_es": "Transitar abiertamente (通) por costumbres constantes (常) define lo que ocurre habitualmente (通常).",
            "cultural_and_cognitive_roots": "Blends 'thoroughfare connectivity' (通) with 'temporal constancy' (常) to signify everyday default patterns.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'tōng cháng' (55-35). Start on a level high pitch and rise steadily."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "痛", "pinyin": "tòng", "meaning_en": "pain; ache", "distinction_note": "Sickness radical 疒 instead of 辶"},
                {"character": "勇", "pinyin": "yǒng", "meaning_en": "brave; courageous", "distinction_note": "Strength radical 力 below 甬"},
                {"character": "裳", "pinyin": "shang", "meaning_en": "clothes; garments", "distinction_note": "Clothing radical 衣 at the base instead of 巾"},
                {"character": "堂", "pinyin": "táng", "meaning_en": "hall; spacious room", "distinction_note": "Earth radical 土 at the base instead of 巾"}
            ],
            "etymological_cognates": [
                {"character": "平常", "pinyin": "píngcháng", "gloss_en": "ordinary; common"},
                {"character": "经常", "pinyin": "jīngcháng", "gloss_en": "often; regularly"},
                {"character": "普及", "pinyin": "pǔjí", "gloss_en": "popularize; widespread"},
                {"character": "普遍", "pinyin": "pǔbiàn", "gloss_en": "universal; general"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "通常 expresses standard, prevailing probability under general everyday conditions.",
            "contrasts": [
                {"id": 1, "compared_word": "通常 vs. 经常", "pinyin": "jīngcháng", "analysis": "经常 focuses on high temporal frequency (often/repeatedly), whereas 通常 denotes standard regular practice or probability."},
                {"id": 2, "compared_word": "通常 vs. 平常", "pinyin": "píngcháng", "analysis": "平常 functions as an adjective meaning ordinary or unexceptional, while 通常 acts adverbially for prevailing customs."},
                {"id": 3, "compared_word": "通常 vs. 一向", "pinyin": "yīxiàng", "analysis": "一向 denotes unbroken persistence from the past up to now ('all along'), whereas 通常 expresses the customary norm."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在老北京的合院建筑规制中，建筑用料通常由房主的社会身份决定。王府公馆通常使用考究的青白石台基与琉璃瓦件，而普通平民住宅则通常采用素雅质朴的灰色砖瓦。这种习惯体现了古代严密的礼制等级。",
                "pinyin": "Zài lǎo Běijīng de héyuàn jiànzhù guīzhì zhōng, jiànzhù yòngliào tōngcháng yóu fángzhǔ de shèhuì shēnfèn juédìng. Wángfǔ gōngguǎn tōngcháng shǐyòng kǎojiu de qīngbáishí táijī yǔ liúliwǎ jiàn, ér pǔtōng píngmín zhùzhái zé tōngcháng cǎiyòng sùyǎ zhìpǔ de huīsè zhuānwǎ. Zhè zhǒng xíguàn tǐxiàn le gǔdài yánmì de lǐzhì děngjí.",
                "en": "In the architectural codes of old Beijing quadrangles, building materials were usually determined by the homeowner's social status. Princely mansions usually featured fine white stone pedestals and glazed tiles, whereas common residences usually utilized modest grey bricks.",
                "es": "En los códigos constructivos de los patios de Pekín, los materiales solían definirse por el rango social del propietario. Los palacios nobiliarios solían emplear zócalos de piedra blanca y tejas esmaltadas, mientras que los hogares plebeyos recurrían al ladrillo gris."
            },
            {
                "id": "#2",
                "hanzi": "民间日常邻里交往也通常恪守传统的谦让礼俗。逢年过节，街坊之间通常会互赠亲手制作的应节糕点。若有外来客人登门拜访，主人通常会以最高礼节奉上盖碗茉莉花茶。这些看似平常的举动，深藏着古都街巷独特的淳朴民风与人情滋味。",
                "pinyin": "Mínjiān rìcháng línlǐ jiāowǎng yě tōngcháng kèshǒu chuántǒng de qiānràng lǐsú. Féng nián guò jié, jiēfang zhījiān tōngcháng huì hù zèng qīnshǒu zhìzuò de yìngjié gāodiǎn. Ruò yǒu wàilái kèrén dēngmén bàifǎng, zhǔrén tōngcháng huì yǐ zuìgāo lǐjié fèngshang gàiwǎn mòlihuā chá. Zhèxiē kànsì píngcháng de jǔdòng, shēncáng zhe gǔdū jiēxiàng dútè de chúnpǔ mínfēng yǔ rénqíng zīwèi.",
                "en": "Daily neighborhood interactions among civilians also usually strictly observed traditional polite customs. During festivals, neighbors usually exchanged homemade seasonal cakes. When outside guests arrived, hosts usually offered covered-bowl jasmine tea with highest etiquette.",
                "es": "Las relaciones vecinales cotidianas solían observar con esmero la cortesía tradicional. En festividades, los vecinos solían regalarse dulces típicos caseros. Ante la llegada de visitas, el anfitrión servía té de jazmín en cuenco con reverencia, reflejando la entrañable hospitalidad pekinesa."
            }
        ]
    },

    # 12 并列
    {
        "id": "12",
        "hanzi": "并列",
        "pinyin": "bìng liè",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to stand side by side; juxtapose; tie (in a contest)",
            "es": "yuxtaponer; alinearse; empatar; estar en el mismo plano"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to be placed side by side; to rank equally without distinction of superior and inferior",
                "definition_es": "colocarse uno al lado del otro; alinearse en el mismo rango o igualdad de condiciones",
                "example_phrase": "并列第一名 (tie for first place)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在老北京四合院的规整格局中，东厢房与西厢房分立在庭院两侧，形成了整齐并列的对称之美。",
                "pinyin": "Zài lǎo Běijīng sìhéyuàn de guīzhěng géjú zhōng, dōngxiāngfáng yǔ xīxiāngfáng fēnlì zài tíngyuàn liǎngcè, xíngchéng le zhěngqí bìngliè de duìchèn zhī měi.",
                "en": "In the orderly layout of old Beijing quadrangles, east and west wing-rooms stand on either side of the courtyard, forming a neatly juxtaposed symmetrical aesthetic.",
                "es": "En la ordenada traza del siheyuan pekinés, las alas este y oeste se alzan a ambos flancos del patio, creando una equilibrada belleza simétrica yuxtapuesta."
            },
            {
                "id": "#2",
                "hanzi": "两位青年学者凭借开创性的理论研究成果，在今年的学术年会上并列荣获一等奖。",
                "pinyin": "Liǎng wèi qīngnián xuézhě píngjiè kāichuàngxìng de lǐlùn yánjiū chéngguǒ, zài jīntiān de xuéshù niánhuì shang bìngliè rónghuò yīděngjiǎng.",
                "en": "Two young scholars jointly won the first prize in a tie at this year's academic symposium for their groundbreaking theoretical findings.",
                "es": "Dos jóvenes investigadores obtuvieron conjuntamente el primer premio en pie de igualdad en el congreso científico gracias a sus innovadoras teorías."
            }
        ],
        "collocations": [
            {"hanzi": "并列第一", "en": "tie for first place"},
            {"hanzi": "并列关系", "en": "coordinate relationship (grammar)"},
            {"hanzi": "并列排布", "en": "arrayed side by side"},
            {"hanzi": "不分先后", "en": "in no specific precedence"},
            {"hanzi": "并列句子", "en": "coordinate clauses"},
            {"hanzi": "地位并列", "en": "equal status / parallel standing"}
        ],
        "idioms": [
            {"hanzi": "并驾齐驱", "pinyin": "bìng jià qí qū", "meaning_en": "run neck and neck; keep pace side by side"},
            {"hanzi": "平起平坐", "pinyin": "píng qǐ píng zuò", "meaning_en": "sit on equal footing; enjoy parity"},
            {"hanzi": "相提并论", "pinyin": "xiāng tí bìng lùn", "meaning_en": "mention in the same breath; treat as equivalent"},
            {"hanzi": "并肩作战", "pinyin": "bìng jiān zuòzhàn", "meaning_en": "fight shoulder to shoulder"}
        ],
        "character_decomposition": [
            {
                "character": "并",
                "pinyin": "bìng",
                "meaning_en": "combine; together; side by side",
                "meaning_es": "combinar; juntos; a la vez",
                "radical": "干",
                "radical_meaning_en": "shield / dry",
                "meaning_component": "two standing figures joined together at the base",
                "sound_component": "并 (bìng)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of two people standing side by side shoulder-to-shoulder in tandem.",
                "visual_mnemonic_story_en": "Two figures standing shoulder to shoulder (并) walking together in lockstep.",
                "visual_mnemonic_story_es": "Dos siluetas erguidas hombro con hombro (并) marchando al unísono.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TT",
                "traditional": "並"
            },
            {
                "character": "列",
                "pinyin": "liè",
                "meaning_en": "row; line; arrange; list",
                "meaning_es": "fila; hilera; alinear; clasificar",
                "radical": "刂",
                "radical_meaning_en": "knife / blade",
                "meaning_component": "歹 (broken bone / clean division) + 刂 (cutting knife)",
                "sound_component": "列 (liè)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A sharp knife 刂 segmenting bone fragments into an orderly row or sequence; line up.",
                "visual_mnemonic_story_en": "Using a knife blade (刂) to trim components neatly into an organized column or line (列).",
                "visual_mnemonic_story_es": "Emplear una hoja afilada (刂) para separar elementos en una hilera ordenada (列).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MNLN",
                "traditional": "列"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Standing side by side (并) aligned in an orderly rank (列) signifies parallel juxtaposition (并列).",
            "composite_memory_hook_es": "Estar hombro con hombro (并) alineados en rigurosa hilera (列) define la yuxtaposición paritaria (并列).",
            "cultural_and_cognitive_roots": "Derived from classical military formations and grammatical coordinates where neither term subordinates the other.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'bìng liè' (51-51). Deliver both syllables with crisp, sharp downward inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "井", "pinyin": "jǐng", "meaning_en": "water well", "distinction_note": "Grid lines without top horizontal dot strokes"},
                {"character": "开", "pinyin": "kāi", "meaning_en": "open; start", "distinction_note": "Horizontal bar across two vertical supports"},
                {"character": "例", "pinyin": "lì", "meaning_en": "example; instance", "distinction_note": "Person radical 亻 to the left of 列"},
                {"character": "烈", "pinyin": "liè", "meaning_en": "intense; fiery", "distinction_note": "Four fire dots 灬 below 列"}
            ],
            "etymological_cognates": [
                {"character": "排列", "pinyin": "páiliè", "gloss_en": "arrange; line up"},
                {"character": "队列", "pinyin": "duìliè", "gloss_en": "formation; queue"},
                {"character": "合并", "pinyin": "hébìng", "gloss_en": "merge; coalesce"},
                {"character": "兼并", "pinyin": "jiānbìng", "gloss_en": "annex; swallow up"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "并列 emphasizes equal rank, simultaneous presence, or horizontal non-hierarchical juxtaposition.",
            "contrasts": [
                {"id": 1, "compared_word": "并列 vs. 从属", "pinyin": "cóngshǔ", "analysis": "从属 denotes hierarchical subordination where one relies on the master, while 并列 denotes equal status."},
                {"id": 2, "compared_word": "并列 vs. 递进", "pinyin": "dìjìn", "analysis": "递进 marks step-by-step sequential escalation in intensity, whereas 并列 treats all items on the same plane."},
                {"id": 3, "compared_word": "并列 vs. 交叉", "pinyin": "jiāochā", "analysis": "交叉 involves intersecting or overlapping paths, whereas 并列 features parallel non-intersecting lines."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统院落的规划非常讲究对称并列。在四合院内部，东西两侧的厢房无论在进深、开间还是屋顶造型上，都保持着高度的并列对应。这种左右对称的建筑格局，营造出一种端正庄重的居住秩序。",
                "pinyin": "Zhōngguó chuántǒng yuànluò de guīhuà fēicháng jiǎngjiu duìchèn bìngliè. Zài sìhéyuàn nèibù, dōngxī liǎngcè de xiāngfáng wúlùn zài jìnshēn, kāijiān háishì wūdǐng zàoxíng shang, dōu bǎochí zhe gāodù de bìngliè duìyìng. Zhè zhǒng zuǒyòu duìchèn de jiànzhù géjú, yíngzào chū yī zhǒng duānzhèng zhuāngzhòng de jūzhù zhìxù.",
                "en": "The planning of traditional Chinese courtyards emphasized symmetry and parallel layout. Inside a quadrangle, the east and west wings maintained high coordinate correspondence in depth, span, and roof styling, forging an orderly dignity.",
                "es": "La traza del patio tradicional chino concede enorme importancia a la simetría y alineación. Las alas este y oeste guardaban estricta concordancia en profundidad, crujías y techumbres, forjando un orden residencial solemne."
            },
            {
                "id": "#2",
                "hanzi": "在汉语语法构造中，并列短语是由两个或两个以上地位平等的词汇共同组合而成的。它们之间没有修饰与被修饰的依附关系，表达的意思互为补充。学会准确识别并列关系，有助于深入理解古代诗词与现代美文的精妙对仗。",
                "pinyin": "Zài Hànyǔ yǔfǎ gòuzào zhōng, bìngliè duǎnyǔ shì yóu liǎng gè huò liǎng gè yǐshàng dìwèi píngděng de cíhuì gòngtóng zǔhé ér chéng de. Tāmen zhījiān méiyǒu xiūshì yǔ bèi xiūshì de yīfù guānxi, biǎodá de yìsi hù wéi bǔchōng. Xuéhuì zhǔnquè shíbié bìngliè guānxi, yǒuzhùyú shēnrù lǐjiě gǔdài shīcí yǔ xiàndài měiwén de jīngmiào duìzhàng.",
                "en": "In Chinese grammatical syntax, coordinate phrases are composed of two or more words of equal standing. They share no subordinate modifying relationship and complement each other, enabling learners to appreciate poetic parallelism.",
                "es": "En la sintaxis gramatical china, los sintagmas coordinados se componen de términos de idéntica jerarquía. No guardan dependencia de subordinación sino que se complementan, permitiendo apreciar el pulcro paralelismo poético."
            }
        ]
    },

    # 13 组成
    {
        "id": "13",
        "hanzi": "组成",
        "pinyin": "zǔ chéng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to compose; form; constitute; component",
            "es": "componer; formar; constituir; conformar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to combine individual elements or members together into a coherent whole or organization",
                "definition_es": "combinar elementos o integrantes individuales para formar un todo u organización",
                "example_phrase": "由……组成 (be composed of ...)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经典的北京四合院由正房、倒座房以及东西两座对称的厢房组合围成，形式浑然一体。",
                "pinyin": "Jīngdiǎn de Běijīng sìhéyuàn yóu zhèngfáng, dàozuòfáng yǐjí dōngxī liǎng zuò duìchèn de xiāngfáng zǔhé wéichéng, xíngshì húnrányītǐ.",
                "en": "The classic Beijing courtyard is formed by the main room, reverse front room, and two symmetrical side wings, creating an integrated whole.",
                "es": "El clásico patio pekinés está constituido por la sala principal, la habitación frontal y dos alas laterales simétricas, formando una unidad armónica."
            },
            {
                "id": "#2",
                "hanzi": "本次联合考察队由地质勘探专家、生物学者以及数位资深摄影师共同组成。",
                "pinyin": "Běncì liánhé kǎocháduì yóu dìzhì kāntàn zhuānjiā, shēngwù xuézhě yǐjí shù wèi zīshēn shèyǐngshī gòngtóng zǔchéng.",
                "en": "This joint expedition team is composed of geological survey specialists, biologists, and several veteran photographers.",
                "es": "La expedición conjunta está integrada por especialistas en exploración geológica, biólogos y varios fotógrafos experimentados."
            }
        ],
        "collocations": [
            {"hanzi": "组成部分", "en": "constituent part; integral component"},
            {"hanzi": "由……组成", "en": "be composed / formed of"},
            {"hanzi": "组成小组", "en": "form a working team"},
            {"hanzi": "基本组成", "en": "basic makeup / structural makeup"},
            {"hanzi": "人员组成", "en": "personnel composition"},
            {"hanzi": "组成联盟", "en": "form an alliance"}
        ],
        "idioms": [
            {"hanzi": "聚沙成塔", "pinyin": "jù shā chéng tǎ", "meaning_en": "grains of sand build a pagoda; small efforts accumulate to big feats"},
            {"hanzi": "众志成城", "pinyin": "zhòng zhì chéng chéng", "meaning_en": "unity of will forms an impregnable fortress"},
            {"hanzi": "融为一体", "pinyin": "róng wéi yī tǐ", "meaning_en": "fuse into an indivisible whole"},
            {"hanzi": "相辅相成", "pinyin": "xiāng fǔ xiāng chéng", "meaning_en": "complement and reinforce each other"}
        ],
        "character_decomposition": [
            {
                "character": "组",
                "pinyin": "zǔ",
                "meaning_en": "braid; organize; form; group",
                "meaning_es": "trenzar; organizar; agrupar; serie",
                "radical": "纟",
                "radical_meaning_en": "silk / thread",
                "meaning_component": "纟 (threads/cords) + 且 (ancestral altar/heaping stones)",
                "sound_component": "且 (qiě / phonetic root)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silken cords 纟 woven and tied together around ceremonial markers 且; to organize into a firm group.",
                "visual_mnemonic_story_en": "Weaving silk strings (纟) into neat patterned bands to unite members into a group (组).",
                "visual_mnemonic_story_es": "Trenzar cordones de seda (纟) en bandas uniformes para congregar miembros en un grupo (组).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "VMBM",
                "traditional": "組"
            },
            {
                "character": "成",
                "pinyin": "chéng",
                "meaning_en": "become; complete; achieve; succeed",
                "meaning_es": "convertirse en; completar; lograr; éxito",
                "radical": "戈",
                "radical_meaning_en": "dagger-axe / weapon",
                "meaning_component": "戊 (weapon / axe) + 丁 (striking pin / nail)",
                "sound_component": "成 (chéng)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A warrior completing a task through decisive action with a halberd 戈; signifies completion.",
                "visual_mnemonic_story_en": "Using a weapon tool (戈) decisively to accomplish and finish a great work (成).",
                "visual_mnemonic_story_es": "Blandir la alabarda (戈) con determinación para culminar y completar una gran obra (成).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IHS",
                "traditional": "成"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Weaving threads together (组) to accomplish a completed structure (成) means to compose or form (组成).",
            "composite_memory_hook_es": "Entrelazar hebras (组) hasta culminar una estructura completa (成) conforma el acto de componer (组成).",
            "cultural_and_cognitive_roots": "Originates from weaving terminology where separate strands unite into strong textiles, applied to systems and groups.",
            "tone_sandhi_and_pitch_modulation": "Third tone to second tone: 'zǔ chéng' (214-35). Dip the voice deeply on 'zǔ' and soar smoothly on 'chéng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "阻", "pinyin": "zǔ", "meaning_en": "block; hinder", "distinction_note": "Mound radical 阝 on the left instead of 纟"},
                {"character": "租", "pinyin": "zū", "meaning_en": "rent; lease", "distinction_note": "Grain radical 禾 on the left instead of 纟"},
                {"character": "城", "pinyin": "chéng", "meaning_en": "city; wall", "distinction_note": "Earth radical 土 to the left of 成"},
                {"character": "诚", "pinyin": "chéng", "meaning_en": "honest; sincere", "distinction_note": "Speech radical 讠 to the left of 成"}
            ],
            "etymological_cognates": [
                {"character": "构成", "pinyin": "gòuchéng", "gloss_en": "constitute; construct"},
                {"character": "组织", "pinyin": "zǔzhī", "gloss_en": "organization; to organize"},
                {"character": "合成", "pinyin": "héchéng", "gloss_en": "synthesize; compound"},
                {"character": "成立", "pinyin": "chénglì", "gloss_en": "establish; found"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "组成 stresses the dynamic assembly or structural parts comprising an integrated whole.",
            "contrasts": [
                {"id": 1, "compared_word": "组成 vs. 构成", "pinyin": "gòuchéng", "analysis": "构成 focuses more on abstract structural formation or legal elements, whereas 组成 often deals with tangible components or teams."},
                {"id": 2, "compared_word": "组成 vs. 组织", "pinyin": "zǔzhī", "analysis": "组织 denotes the managerial act of coordinating people or an enterprise, while 组成 states the compositional ingredients."},
                {"id": 3, "compared_word": "组成 vs. 拆散", "pinyin": "chāisàn", "analysis": "拆散 is the complete direct antonym meaning to dismantle or break up an assembled entity."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统四合院建筑的奇妙之处，在于它由几个独立单体建筑巧妙组成。正房、厢房与门楼通过抄手游廊相互勾连，共同组成一个围合的天井庭院。各个部分各司其职，在空间上形成紧密呼应的和谐整体。",
                "pinyin": "Zhōngguó chuántǒng sìhéyuàn jiànzhù de qímiào zhīchù, zàiyú tā yóu jǐ gè dúlì dāntǐ jiànzhù qiǎomiào zǔchéng. Zhèngfáng, xiāngfáng yǔ ménlóu tōngguò chāoshǒu yóuláng xiānghù gōulián, gòngtóng zǔchéng yī gè wéihé de tiānjǐng tíngyuàn. Gègè bùfen gè sī qí zhí, zài kōngjiān shang xíngchéng jǐnmì hūyìng de héxié zhěngtǐ.",
                "en": "The wonder of traditional Chinese courtyards lies in being cleverly composed of several independent individual buildings. The main room, wings, and gatehouse connect via covered verandas, together forming an enclosed courtyard.",
                "es": "La maravilla del siheyuan estriba en componerse ingeniosamente de varios edificios independientes. La sala principal, las alas y el pórtico se enlazan mediante galerías, conformando un patio cerrado que armoniza en un todo solidario."
            },
            {
                "id": "#2",
                "hanzi": "在现代科学视角下，任何繁复的物质系统都是由微小基础单元组成的。比如细胞由生物分子组成，大厦由砖石钢筋组成，精密的计算机程序由一行行逻辑代码组成。理解了基础组成的规律，就能在复杂现象中把握本质。",
                "pinyin": "Zài xiàndài kēxué shìjiǎo xià, rènhé fánfù de wùzhì xìtǒng dōu shì yóu wēixiǎo jīchǔ dānyuán zǔchéng de. Bǐrú xìbāo yóu shēngwù fēnzǐ zǔchéng, dàshà yóu zhuānshí gāngjīn zǔchéng, jīngmì de jìsuànjī chéngxù yóu yī háng háng luóji dàimǎ zǔchéng. Lǐjiě le jīchǔ zǔchéng de guīlǜ, jiù néng zài fùzá xiànxiàng zhōng bǎwò běnzhì.",
                "en": "From the perspective of modern science, any complex physical system is composed of tiny fundamental units. Cells are made of molecules, towers composed of bricks and steel, and programs composed of code. Grasping these basic components clarifies the essence.",
                "es": "Bajo la mirada científica moderna, todo sistema complejo se compone de diminutas unidades básicas: las células se componen de biomoléculas, los edificios de acero y piedra, y el software de líneas de código lógico."
            }
        ]
    },

    # 14 长辈
    {
        "id": "14",
        "hanzi": "长辈",
        "pinyin": "zhǎng bèi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "elder generation; senior relatives; elders",
            "es": "generación mayor; parientes mayores; mayores de la familia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "family members or relatives belonging to an older generation than oneself",
                "definition_es": "miembros de la familia o parientes pertenecientes a una generación superior a la propia",
                "example_phrase": "尊敬长辈 (respect one's elders)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院的建筑规制处处体现孝道，最好的正房总是安排给家中的长辈安居颐养。",
                "pinyin": "Sìhéyuàn de jiànzhù guīzhì chùchù tǐxiàn xiàodào, zuì hǎo de zhèngfáng zǒngshì ānpái gěi jiāzhōng de zhǎngbèi ānjū yíyǎng.",
                "en": "The architectural layout of courtyards embodies filial piety everywhere, with the finest main room always allocated to family elders for rest.",
                "es": "La disposición espacial del siheyuan refleja la piedad filial en cada detalle, asignando siempre la mejor estancia a los mayores de la familia."
            },
            {
                "id": "#2",
                "hanzi": "逢年过节阖家团聚时，晚辈们都会毕恭毕敬地向长辈敬茶拜年，互道安康祝福。",
                "pinyin": "Féng nián guò jié héjiā tuánjù shí, wǎnbèi men dōu huì bìgōngbìjìng de xiàng zhǎngbèi jìng chá bàinián, hù dào ānkāng zhùfú.",
                "en": "During festival family reunions, younger generations respectfully serve tea to elders and offer New Year greetings wishing them good health.",
                "es": "En las reuniones familiares festivas, los jóvenes sirven té con sumo respeto a los mayores y les desean prosperidad y salud para el nuevo año."
            }
        ],
        "collocations": [
            {"hanzi": "孝敬长辈", "en": "show filial devotion to elders"},
            {"hanzi": "尊敬长辈", "en": "respect senior generation"},
            {"hanzi": "家族长辈", "en": "family clan elders"},
            {"hanzi": "听从长辈", "en": "heed the advice of elders"},
            {"hanzi": "长辈嘱托", "en": "earnest exhortations of elders"},
            {"hanzi": "长辈关怀", "en": "loving care from elders"}
        ],
        "idioms": [
            {"hanzi": "尊老爱幼", "pinyin": "zūn lǎo ài yòu", "meaning_en": "respect the elderly and care for the young"},
            {"hanzi": "老当益壮", "pinyin": "lǎo dāng yì zhuàng", "meaning_en": "old in years but stout at heart"},
            {"hanzi": "安享晚年", "pinyin": "ān xiǎng wǎn nián", "meaning_en": "enjoy twilight years in peace and serenity"},
            {"hanzi": "孝子贤孙", "pinyin": "xiào zǐ xián sūn", "meaning_en": "filial sons and virtuous grandchildren"}
        ],
        "character_decomposition": [
            {
                "character": "长",
                "pinyin": "zhǎng",
                "meaning_en": "senior; elder; to grow; chief",
                "meaning_es": "mayor; superior; crecer; jefe",
                "radical": "长",
                "radical_meaning_en": "long / elder",
                "meaning_component": "flowing long hair of a wise walking village elder",
                "sound_component": "长 (zhǎng / cháng)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of an elder with long flowing hair leaning on a walking staff.",
                "visual_mnemonic_story_en": "An elder with long silver locks (长) guiding the household with gentle wisdom.",
                "visual_mnemonic_story_es": "Un anciano de larga melena blanca (长) que guía a su familia con serena sabiduría.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "PO",
                "traditional": "長"
            },
            {
                "character": "辈",
                "pinyin": "bèi",
                "meaning_en": "generation; rank; cohort",
                "meaning_es": "generación; rango; camada",
                "radical": "车",
                "radical_meaning_en": "cart / vehicle",
                "meaning_component": "非 (opposing ranks/wings) + 车 (carriages)",
                "sound_component": "非 (fēi / phonetic root)",
                "stroke_count": 15,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A procession of military carriages 车 traveling in orderly ranks 非; indicates cohorts and generations.",
                "visual_mnemonic_story_en": "Carriages (车) arranged in successive historical ranks representing family generations (辈).",
                "visual_mnemonic_story_es": "Carruajes (车) alineados en riguroso orden ceremonial que representan las generaciones familiares (辈).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LYKJJ",
                "traditional": "輩"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A wise senior elder (长) seated in the honored carriage rank of the generation (辈) is a clan elder (长辈).",
            "composite_memory_hook_es": "Un anciano venerable (长) en el carruaje de honor de su generación (辈) encarna a los mayores de la familia (长辈).",
            "cultural_and_cognitive_roots": "Deeply anchored in Confucian filial culture where generational seniority dictates domestic protocol and housing arrangements.",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'zhǎng bèi' (214-51). Lower the pitch on 'zhǎng', then drop with resolute emphasis on 'bèi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "非", "pinyin": "fēi", "meaning_en": "wrong; not", "distinction_note": "Lacks the carriage 车 radical at the bottom"},
                {"character": "悲", "pinyin": "bēi", "meaning_en": "sad; sorrow", "distinction_note": "Heart radical 心 at bottom instead of 车"},
                {"character": "斐", "pinyin": "fěi", "meaning_en": "graceful; elegant", "distinction_note": "Pattern radical 文 at bottom instead of 车"},
                {"character": "翡", "pinyin": "fěi", "meaning_en": "red jadeite; kingfisher", "distinction_note": "Feather radical 羽 at bottom instead of 车"}
            ],
            "etymological_cognates": [
                {"character": "晚辈", "pinyin": "wǎnbèi", "gloss_en": "younger generation; juniors"},
                {"character": "同辈", "pinyin": "tóngbèi", "gloss_en": "peers of same generation"},
                {"character": "前辈", "pinyin": "qiánbèi", "gloss_en": "senior; predecessor"},
                {"character": "辈分", "pinyin": "bèifen", "gloss_en": "generational seniority"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "长辈 specifically designates relatives of older generations within the domestic family tree.",
            "contrasts": [
                {"id": 1, "compared_word": "长辈 vs. 前辈", "pinyin": "qiánbèi", "analysis": "长辈 is strictly restricted to family genealogical lineages, whereas 前辈 refers to career mentors or professional seniors."},
                {"id": 2, "compared_word": "长辈 vs. 晚辈", "pinyin": "wǎnbèi", "analysis": "晚辈 is the direct genealogical antonym meaning descendants or family members of junior generations."},
                {"id": 3, "compared_word": "长辈 vs. 老人", "pinyin": "lǎorén", "analysis": "老人 denotes any elderly person based on chronological age, whereas 长辈 is strictly a relational genealogical rank."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在老北京的四合院里，长辈享有崇高的家庭地位。坐北朝南的正房冬暖夏凉、宽敞明亮，理所当然由长辈居住。清晨晚辈们都要先到正房向长辈请安，这种严谨的起居秩序构成了传统家族亲情的核心纽带。",
                "pinyin": "Zài lǎo Běijīng de sìhéyuàn lǐ, zhǎngbèi xiǎngyǒu chónggāo de jiātíng dìwèi. Zuòběi cháonán de zhèngfáng dōngnuǎn xiàliáng, kuānchǎng míngliàng, lǐsuǒdāngrán yóu zhǎngbèi jūzhù. Qīngchén wǎnbèi men dōu yào xiān dào zhèngfáng xiàng zhǎngbèi qǐng'ān, zhè zhǒng yánjǐn de qǐjū zhìxù gòuchéng le chuántǒng jiāzú qīnqíng de héxīn niǔdài.",
                "en": "In old Beijing courtyards, elders held lofty status within the clan. The spacious, sunlit main room facing south was naturally reserved for them. Juniors greeted elders every morning, forming the core bond of traditional familial affection.",
                "es": "En el siheyuan pekinés, los mayores gozaban de veneración familiar. La sala principal, cálida en invierno y luminosa, les correspondía por derecho. El saludo matutino de los jóvenes afianzaba los lazos del linaje tradicional."
            },
            {
                "id": "#2",
                "hanzi": "中国传统家训十分强调对长辈的理解与体贴。随着年岁渐长，长辈的体力和精力大不如前，晚辈不仅要在物质生活上悉心照料长辈的起居，更要在精神上多陪伴倾听。尊重长辈的人生沉淀，是文明薪火相传的重要基石。",
                "pinyin": "Zhōngguó chuántǒng jiāxùn shífēn qiángdiào duì zhǎngbèi de lǐjiě yǔ tǐtiē. Suízhe niánsuì jiàn zhǎng, zhǎngbèi de tǐlì yǔ jīnglì dà bù rú qián, wǎnbèi bùjǐn yào zài wùzhì shēnghuó shang xīxīn zhàoliào zhǎngbèi de qǐjū, gèng yào zài jīngshén shang duō péibàn qīngtīng. Zūnzhòng zhǎngbèi de rénshēng chéndiàn, shì wénmíng xīnhuǒ xiāngchuán de zhòngyào jīshí.",
                "en": "Chinese familial precepts emphasize empathy and attentiveness toward elders. As age advances, juniors must not only provide physical care for elders' daily routine, but also offer patient companionship and listening to preserve generational wisdom.",
                "es": "Los preceptos familiares chinos inculcan ternura hacia los mayores. Con el paso de los años, los jóvenes no solo deben velar por su bienestar cotidiano, sino brindarles afecto y escucha para perpetuar la sabiduría del linaje."
            }
        ]
    },

    # 15 具备
    {
        "id": "15",
        "hanzi": "具备",
        "pinyin": "jù bèi",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to possess; have; be equipped with (qualifications/conditions)",
            "es": "poseer; contar con; reunir; estar provisto de"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to possess or be provided with necessary conditions, qualities, capabilities, or equipment",
                "definition_es": "poseer o estar provisto de las condiciones, cualidades o medios indispensables",
                "example_phrase": "具备条件 (possess the necessary conditions)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "现代化改造后的传统四合院，既保留了古典建筑风貌，又具备了先进完备的生活设施。",
                "pinyin": "Xiàndàihuà gǎizào hòu de chuántǒng sìhéyuàn, jì bǎoliú le gǔdiǎn jiànzhù fēngmào, yòu jùbèi le xiānjìn wánbèi de shēnghuó shèshī.",
                "en": "The modernly renovated traditional courtyard retains classical architecture while possessing advanced, complete living amenities.",
                "es": "Tras su remodelación, el patio tradicional preserva su porte clásico a la par que cuenta con avanzadas y completas instalaciones modernas."
            },
            {
                "id": "#2",
                "hanzi": "申请海外高水平科研基金的候选人，必须具备扎实的专业理论功底与突出的外语交流能力。",
                "pinyin": "Shēnqǐng hǎiwài gāoshuǐpíng kēyán jījīn de hòuxuǎnrén, bìxū jùbèi zhāshi de zhuānyè lǐlùn gōngdǐ yǔ tūchū de wàiyǔ jiāoliú nénglì.",
                "en": "Candidates applying for advanced overseas research funds must possess solid professional theoretical foundation and outstanding foreign language skills.",
                "es": "Los postulantes a fondos científicos internacionales deben poseer una sólida base teórica y sobresaliente solvencia en idiomas extranjeros."
            }
        ],
        "collocations": [
            {"hanzi": "具备条件", "en": "possess the qualifications / conditions"},
            {"hanzi": "具备能力", "en": "possess competence / capability"},
            {"hanzi": "具备素质", "en": "possess qualities / caliber"},
            {"hanzi": "具备资格", "en": "possess eligibility / credentials"},
            {"hanzi": "具备功能", "en": "be equipped with functions"},
            {"hanzi": "基本具备", "en": "basically possess / initially equipped"}
        ],
        "idioms": [
            {"hanzi": "万事俱备", "pinyin": "wàn shì jù bèi", "meaning_en": "all is ready except for one final element"},
            {"hanzi": "德才兼备", "pinyin": "dé cái jiān bèi", "meaning_en": "possessing both integrity and professional brilliance"},
            {"hanzi": "文武双全", "pinyin": "wén wǔ shuāng quán", "meaning_en": "accomplished in both civil arts and military prowess"},
            {"hanzi": "面面俱到", "pinyin": "miàn miàn jù dào", "meaning_en": "meticulously attentive to every single angle"}
        ],
        "character_decomposition": [
            {
                "character": "具",
                "pinyin": "jù",
                "meaning_en": "tool; possess; furnish; provide",
                "meaning_es": "herramienta; poseer; proveer; suministrar",
                "radical": "八",
                "radical_meaning_en": "eight / separate",
                "meaning_component": "鼎 (ritual cauldron) held up by hands 廾",
                "sound_component": "具 (jù)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two hands 廾 lifting up a bronze ritual vessel with food prepared for a feast; to furnish and provide completely.",
                "visual_mnemonic_story_en": "Hands presenting an ornate vessel equipped (具) with every utensil needed for a banquet.",
                "visual_mnemonic_story_es": "Manos que ofrecen una bandeja repleta con cada cubierto e instrumento necesario (具).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BMC",
                "traditional": "具"
            },
            {
                "character": "备",
                "pinyin": "bèi",
                "meaning_en": "prepare; ready; equip; equipment",
                "meaning_es": "preparar; dispuesto; equipar; provisto",
                "radical": "夂",
                "radical_meaning_en": "go / step",
                "meaning_component": "夂 (trailing feet) + 田 (quiver carrying arrows / storage)",
                "sound_component": "备 (bèi)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A quiver stocked with arrows ready for deployment on the march 夂; to be thoroughly prepared.",
                "visual_mnemonic_story_en": "Carrying a quiver packed with spare arrows so a hunter is fully equipped and ready (备).",
                "visual_mnemonic_story_es": "Llevar un carcaj colmado de flechas para marchar totalmente equipado y prevenido (备).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HEW",
                "traditional": "備"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Holding all necessary tools (具) and being fully prepared (备) means one possesses (具备) all requisites.",
            "composite_memory_hook_es": "Disponer de las herramientas (具) y hallarse enteramente preparado (备) implica poseer lo indispensable (具备).",
            "cultural_and_cognitive_roots": "Derived from classical statecraft where a city or army must possess both implements (具) and provisions (备) before setting out.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'jù bèi' (51-51). Articulate both syllables with decisive firmness."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "真", "pinyin": "zhēn", "meaning_en": "real; true", "distinction_note": "Ten radical 十 at top instead of 目/目-like frame"},
                {"character": "直", "pinyin": "zhí", "meaning_en": "straight; direct", "distinction_note": "No horizontal bar under the vertical eye box"},
                {"character": "奋", "pinyin": "fèn", "meaning_en": "strive; exert", "distinction_note": "Big radical 大 at the top instead of 夂"},
                {"character": "条", "pinyin": "tiáo", "meaning_en": "strip; clause", "distinction_note": "Wood radical 木 at the bottom instead of 田"}
            ],
            "etymological_cognates": [
                {"character": "具有", "pinyin": "jùyǒu", "gloss_en": "possess; have"},
                {"character": "设备", "pinyin": "shèbèi", "gloss_en": "equipment; facilities"},
                {"character": "准备", "pinyin": "zhǔnbèi", "gloss_en": "prepare; get ready"},
                {"character": "具体", "pinyin": "jùtǐ", "gloss_en": "concrete; specific"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "具备 signifies possessing non-material qualifications, capabilities, prerequisites, or essential traits.",
            "contrasts": [
                {"id": 1, "compared_word": "具备 vs. 具有", "pinyin": "jùyǒu", "analysis": "具有 is broader and can describe intrinsic natural features or qualities, while 具备 specifically implies meeting required conditions or criteria."},
                {"id": 2, "compared_word": "具备 vs. 拥有", "pinyin": "yōngyǒu", "analysis": "拥有 often applies to material wealth, vast assets, or large populations, whereas 具备 targets qualifying standards."},
                {"id": 3, "compared_word": "具备 vs. 缺乏", "pinyin": "quēfá", "analysis": "缺乏 is the direct antonym meaning to fall short of or lack necessary components."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "一座理想的中国古典民居，往往具备冬暖夏凉的微气候调节能力。四合院高耸的青砖实心外墙具备优良的保温隔热性能，院内的绿植与水池则具备增加湿度与调节气温的作用，使居民享受到舒适的生活环境。",
                "pinyin": "Yī zuò lǐxiǎng de Zhōngguó gǔdiǎn mínjū, wǎngwǎng jùbèi dōngnuǎn xiàliáng de wēi qìhòu tiáojié nénglì. Sìhéyuàn gāosǒng de qīngzhuān shíxīn wàiqiáng jùbèi yōuliáng de bǎowēn gérè xìngnéng, yuànnèi de lǜzhí yǔ shuǐchí zé jùbèi zēngjiā shīdù yǔ tiáojié qìwēn de zuòyòng, shǐ jūmín xiǎngshòu dào shūshì de shēnghuó huánjìng.",
                "en": "An ideal classical dwelling possesses microclimate regulation capabilities keeping it warm in winter and cool in summer. Its brick perimeter walls possess insulation performance, while greenery balances humidity and temperature.",
                "es": "Una vivienda clásica ideal reúne facultades para regular su microclima térmico. Los gruesos muros de ladrillo del siheyuan poseen aislamiento superior, y su vegetación y estanques modulan la humedad para el bienestar vecinal."
            },
            {
                "id": "#2",
                "hanzi": "在当今瞬息万变的全球化时代，优秀的复合型人才必须具备多维度的跨文化综合素质。他们不仅需要具备扎实深厚的本学科专业功底，更要具备宽广包容的国际视野与敏锐的批判性思维。具备这些卓越素质，方能引领前沿创新。",
                "pinyin": "Zài dāngjīn shùnxī-wànbiàn de quánqiúhuà shídài, yōuxiù de fùhéxíng réncái bìxū jùbèi duōwéidù de kuà wénhuà zōnghé sùzhì. Tāmen bùjǐn xūyào jùbèi zhāshi shēnhòu de běn xuékē zhuānyè gōngdǐ, gèng yào jùbèi kuānguǎng bāoróng de guójì shìyě yǔ mǐnruì de pīpànxìng sīwéi. Jùbèi zhèxiē zhuóyuè sùzhì, fāng néng yǐnlǐng qiányán chuàngxīn.",
                "en": "In today's fast-changing globalized era, multifaceted talents must possess comprehensive cross-cultural qualities. They must possess solid grounding in their field, an inclusive international vision, and sharp critical thinking to drive innovation.",
                "es": "En la cambiante era global, los talentos multidisciplinares deben reunir aptitudes interculturales complejas. Requieren contar con hondos saberes profesionales, visión integradora y pensamiento crítico para liderar la innovación."
            }
        ]
    },

    # 16 日常
    {
        "id": "16",
        "hanzi": "日常",
        "pinyin": "rì cháng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "daily; everyday; day-to-day; routine",
            "es": "diario; cotidiano; del día a día; ordinario"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "relating to ordinary everyday activities, life, or routine necessities",
                "definition_es": "perteneciente o relativo a las actividades, rutinas o necesidades de la vida diaria",
                "example_phrase": "日常生活 (daily life)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "居住在胡同四合院里的居民，在葡萄架下喝茶下棋，享受着平静而惬意的日常时光。",
                "pinyin": "Jūzhù zài hútòng sìhéyuàn lǐ de jūmín, zài pútáojià xià hē chá xià qí, xiǎngshòu zhe píngjìng ér qièyì de rìcháng shíguāng.",
                "en": "Residents living in alley quadrangles sip tea and play chess beneath grape trellises, savoring peaceful everyday moments.",
                "es": "Los vecinos de los patios beben té y juegan al ajedrez bajo emparrados de vid, saboreando el sosiego de la vida cotidiana."
            },
            {
                "id": "#2",
                "hanzi": "掌握基本的地道汉语日常口语，是外国留学生快速融入中国大学校园生活的关键。",
                "pinyin": "Zhǎngwò jīběn de dìdao Hànyǔ rìcháng kǒuyǔ, shì wàiguó liúxuéshēng kuàisù róngrù Zhōngguó dàxué xiàoyuán shēnghuó de guānjiàn.",
                "en": "Mastering authentic daily spoken Chinese is key for foreign students to integrate smoothly into campus life in China.",
                "es": "Dominar expresiones chinas coloquiales de uso diario resulta clave para que los estudiantes extranjeros se integren en la vida universitaria."
            }
        ],
        "collocations": [
            {"hanzi": "日常生活", "en": "daily life / everyday routine"},
            {"hanzi": "日常用品", "en": "daily necessities / toiletries"},
            {"hanzi": "日常工作", "en": "routine day-to-day work"},
            {"hanzi": "日常开支", "en": "everyday living expenses"},
            {"hanzi": "日常维护", "en": "routine maintenance"},
            {"hanzi": "日常交往", "en": "daily social interactions"}
        ],
        "idioms": [
            {"hanzi": "家常便饭", "pinyin": "jiā cháng biàn fàn", "meaning_en": "homestyle meal; routine matter of course"},
            {"hanzi": "柴米油盐", "pinyin": "chái mǐ yóu yán", "meaning_en": "firewood, rice, oil, and salt; basic necessities of life"},
            {"hanzi": "日复一日", "pinyin": "rì fù yī rì", "meaning_en": "day in and day out; continuously without break"},
            {"hanzi": "习以为常", "pinyin": "xí yǐ wéi cháng", "meaning_en": "become accustomed to as a matter of habit"}
        ],
        "character_decomposition": [
            {
                "character": "日",
                "pinyin": "rì",
                "meaning_en": "sun; day; daily",
                "meaning_es": "sol; día; diario",
                "radical": "日",
                "radical_meaning_en": "sun / day",
                "meaning_component": "pictograph of sun with a solar spot in the center",
                "sound_component": "日 (rì)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone glyph depicting the radiant round sun traversing the sky day after day.",
                "visual_mnemonic_story_en": "The shining sun (日) rising every dawn to mark each passing day.",
                "visual_mnemonic_story_es": "El sol radiante (日) que asciende al alba para seccionar el transcurso de cada día.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "A",
                "traditional": "日"
            },
            {
                "character": "常",
                "pinyin": "cháng",
                "meaning_en": "constant; regular; frequent; normal",
                "meaning_es": "constante; regular; frecuente; normal",
                "radical": "巾",
                "radical_meaning_en": "cloth / towel",
                "meaning_component": "尚 (elevated) + 巾 (standard ceremonial cloth)",
                "sound_component": "尚 (shàng)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A banner 巾 raised prominently overhead 尚 as an unchanging standard and perpetual constant.",
                "visual_mnemonic_story_en": "An enduring hanging cloth banner (巾) that stands firm across the passage of time (常).",
                "visual_mnemonic_story_es": "Un estandarte textil (巾) fijado permanentemente como testimonio de lo habitual (常).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "FBRB",
                "traditional": "常"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "What repeats with each rising sun (日) as a constant custom (常) is everyday daily life (日常).",
            "composite_memory_hook_es": "Aquello que retorna con cada nuevo sol (日) como pauta constante (常) conforma lo cotidiano (日常).",
            "cultural_and_cognitive_roots": "Captures the rhythmic cadence of agricultural society revolving around the solar cycle and routine chores.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone to second tone: 'rì cháng' (51-35). Drop abruptly on 'rì' and glide smoothly up on 'cháng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "目", "pinyin": "mù", "meaning_en": "eye; item", "distinction_note": "Contains two internal horizontal lines instead of one"},
                {"character": "白", "pinyin": "bái", "meaning_en": "white; clear", "distinction_note": "Has an upper slanting tick stroke on top"},
                {"character": "党", "pinyin": "dǎng", "meaning_en": "party; faction", "distinction_note": "Legs radical 儿 at bottom instead of 巾"},
                {"character": "尝", "pinyin": "cháng", "meaning_en": "taste; try", "distinction_note": "Small radical 小 inside 𡉚 or 云 variant"}
            ],
            "etymological_cognates": [
                {"character": "日记", "pinyin": "rìjì", "gloss_en": "diary; daily log"},
                {"character": "经常", "pinyin": "jīngcháng", "gloss_en": "often; regularly"},
                {"character": "日程", "pinyin": "rìchéng", "gloss_en": "itinerary; schedule"},
                {"character": "常见", "pinyin": "chángjiàn", "gloss_en": "common; often seen"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "日常 characterizes mundane, regular day-to-day matters as opposed to formal, rare, or festive occasions.",
            "contrasts": [
                {"id": 1, "compared_word": "日常 vs. 节日", "pinyin": "jiérì", "analysis": "节日 marks extraordinary celebratory holidays, contrasting with normal uninterrupted 日常 routines."},
                {"id": 2, "compared_word": "日常 vs. 特殊", "pinyin": "tèshū", "analysis": "特殊 designates rare or exceptional deviations, while 日常 describes habitual default states."},
                {"id": 3, "compared_word": "日常 vs. 偶尔", "pinyin": "ǒu'ěr", "analysis": "偶尔 refers to sporadic occurrences, whereas 日常 represents constant diurnal rhythm."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "四合院内部的空间格局巧妙兼顾了家庭成员的日常隐私与集体交往。封闭的高墙将外界的喧嚣隔绝开来，让一家人能够在庭院中自在地处理日常琐事，晾晒衣物、养花逗鸟，享受充满人间烟火气的惬意生活。",
                "pinyin": "Sìhéyuàn nèibù de kōngjiān géjú qiǎomiào jiāngù le jiātíng chéngyuán de rìcháng yǐnsī yǔ jítǐ jiāowǎng. Fēngbì de gāoqiáng jiāng wàijiè de xuānxīao géjué kāi lái, ràng yī jiā rén nénggòu zài tíngyuàn zhōng zìzài de chǔlǐ rìcháng suǒshì, liàngshài yīwù, yǎng huā dòu niǎo, xiǎngshòu chōngmǎn rénjiān yānhuǒqì de qièyì shēnghuó.",
                "en": "The spatial layout of courtyards skillfully balances everyday family privacy and collective interaction. Enclosing high walls block outside noise, allowing families to attend to daily domestic chores, air laundry, and tend flowers in comfort.",
                "es": "El diseño espacial del siheyuan armoniza la intimidad cotidiana familiar y la convivencia colectiva. Altos muros aíslan el bullicio exterior, permitiendo atender faenas domésticas, secar ropa y cuidar aves en agradable sosiego."
            },
            {
                "id": "#2",
                "hanzi": "现代人的生活节奏飞快，常常在忙碌的奔波中忽略了平凡日常的美好。其实，清晨的一缕暖阳、午后的一杯清茶、傍晚与家人共进的一顿热饭，都是日常中最真实动人的幸福。用心体验日常点滴，才能收获内心的宁静与从容。",
                "pinyin": "Xiàndài rén de shēnghuó jiézòu fēikuài, chángcháng zài mánglù de bēnbō zhōng hūlüè le píngfán rìcháng de měihǎo. Qíshí, qīngchén de yī lǚ nuǎnyáng, wǔhòu de yī bēi qīngchá, bàngwǎn yǔ jiārén gòng jìn de yī dùn rè fàn, dōu shì rìcháng zhōng zuì zhēnshí dòngrén de xìngfú. Yòngxīn tǐyàn rìcháng diǎndī, cái néng shōuhuò nèixīn de níngjìng yǔ cóngróng.",
                "en": "Modern life moves briskly, often causing people to overlook the quiet beauty of ordinary everyday living. The morning warmth, an afternoon cup of tea, and an evening dinner with family are the most authentic joys in daily existence.",
                "es": "El vertiginoso ritmo actual suele hacer olvidar la belleza de lo cotidiano. El sol matinal, una taza de té y una cena compartida en familia constituyen las dichas más genuinas del día a día, colmando el alma de paz."
            }
        ]
    },

    # 17 起居
    {
        "id": "17",
        "hanzi": "起居",
        "pinyin": "qǐ jū",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "daily life; daily routine; rise and rest",
            "es": "vida cotidiana; rutina diaria; descanso y actividad diaria"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "one's daily regimen of waking, resting, eating, and living; routine schedule of domestic existence",
                "definition_es": "régimen diario de vigilia, descanso, alimentación y quehaceres habituales",
                "example_phrase": "照顾起居 (take care of someone's daily routine)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "北京四合院的各栋房舍分工极具智慧，科学周全地照顾到了全家老小的日常起居生活。",
                "pinyin": "Běijīng sìhéyuàn de gè dòng fángshè fēngōng jí jù zhìhuì, kēxué zhōuquán de zhàogù dào le quánjiā lǎoxiǎo de rìcháng qǐjū shēnghuó.",
                "en": "The various wings of Beijing quadrangles were wisely planned, accommodating the daily routine and living needs of the whole family comprehensively.",
                "es": "Las estancias del siheyuan pekinés reflejan gran prudencia distributiva, atendiendo de forma metódica la vida y descanso cotidiano de la familia."
            },
            {
                "id": "#2",
                "hanzi": "医生建议术后康复期的患者务必保持规律的起居作息，切忌熬夜劳累或饮食失调。",
                "pinyin": "Yīshēng jiànyì shùhòu kāngfùqī de huànzhě wùbì bǎochí guīlǜ de qǐjū zuòxī, qièjì áoyè láolèi huò yǐnshí shītiáo.",
                "en": "The physician recommended that post-operative patients maintain a regular daily schedule, avoiding late nights, fatigue, or irregular diet.",
                "es": "El médico aconsejó a los pacientes en convalecencia mantener una rutina regular de descanso y vigilia, evitando trasnochar o desórdenes alimentarios."
            }
        ],
        "collocations": [
            {"hanzi": "起居饮食", "en": "daily living and eating habits"},
            {"hanzi": "起居有常", "en": "keep regular daily hours in rest and work"},
            {"hanzi": "照顾起居", "en": "attend to someone's daily routine"},
            {"hanzi": "日常起居", "en": "everyday routine of living"},
            {"hanzi": "起居室", "en": "living room / family sitting room"},
            {"hanzi": "起居作息", "en": "daily schedule of sleeping and rising"}
        ],
        "idioms": [
            {"hanzi": "起居有常", "pinyin": "qǐ jū yǒu cháng", "meaning_en": "keep regular hours in work and rest"},
            {"hanzi": "起早贪黑", "pinyin": "qǐ zǎo tān hēi", "meaning_en": "work from dawn till dusk; toil early and late"},
            {"hanzi": "安居乐业", "pinyin": "ān jū lè yè", "meaning_en": "live in peace and work with contentment"},
            {"hanzi": "四海为家", "pinyin": "sì hǎi wéi jiā", "meaning_en": "make the world one's home; wander anywhere"}
        ],
        "character_decomposition": [
            {
                "character": "起",
                "pinyin": "qǐ",
                "meaning_en": "rise; wake up; begin; start",
                "meaning_es": "levantarse; despertar; iniciar; comenzar",
                "radical": "走",
                "radical_meaning_en": "run / walk",
                "meaning_component": "走 (walking forward) + 己 (one's own body rising)",
                "sound_component": "己 (jǐ / phonetic association)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A person setting their body 己 into forward walking motion 走; to rise from bed and stand up.",
                "visual_mnemonic_story_en": "Springing onto one's feet to walk (走) at the start of a fresh day (起).",
                "visual_mnemonic_story_es": "Ponerse en pie sobre las propias piernas para caminar (走) al clarear el día (起).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "GOSU",
                "traditional": "起"
            },
            {
                "character": "居",
                "pinyin": "jū",
                "meaning_en": "reside; dwell; live; stay",
                "meaning_es": "residir; habitar; morar; aposento",
                "radical": "尸",
                "radical_meaning_en": "corpse / seated body frame",
                "meaning_component": "尸 (body seated in resting posture) + 古 (old ancestral hearth)",
                "sound_component": "古 (gǔ / phonetic link)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A human body 尸 reposing peacefully inside a time-honored shelter 古; to dwell and repose.",
                "visual_mnemonic_story_en": "A person sheltered under an ancestral roof (尸) resting peacefully at home (居).",
                "visual_mnemonic_story_es": "Una persona cobijada bajo el alero familiar (尸) descansando en su morada (居).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "SJR",
                "traditional": "居"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Rising at dawn (起) and returning home to rest (居) forms one's whole daily routine of living (起居).",
            "composite_memory_hook_es": "Levantarse al alba (起) y reposar en el hogar (居) sintetiza el ciclo vital de la rutina cotidiana (起居).",
            "cultural_and_cognitive_roots": "Derives from ancient medical and imperial records ('起居注') documenting emperors' and scholars' daily movements and rest.",
            "tone_sandhi_and_pitch_modulation": "Third tone to first tone: 'qǐ jū' (214-55). Dip deeply on 'qǐ' and finish with an elevated steady tone on 'jū'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "赶", "pinyin": "gǎn", "meaning_en": "catch up; hurry", "distinction_note": "Shield radical 干 instead of 己"},
                {"character": "越", "pinyin": "yuè", "meaning_en": "surpass; cross over", "distinction_note": "Halberd radical 戉 inside instead of 己"},
                {"character": "剧", "pinyin": "jù", "meaning_en": "drama; play", "distinction_note": "Knife radical 刂 on the right of 居"},
                {"character": "据", "pinyin": "jù", "meaning_en": "according to; seize", "distinction_note": "Hand radical 扌 on the left of 居"}
            ],
            "etymological_cognates": [
                {"character": "起床", "pinyin": "qǐchuáng", "gloss_en": "get up from bed"},
                {"character": "居住", "pinyin": "jūzhù", "gloss_en": "reside; dwell"},
                {"character": "邻居", "pinyin": "línjū", "gloss_en": "neighbor"},
                {"character": "居所", "pinyin": "jūsuǒ", "gloss_en": "dwelling place; abode"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "起居 highlights the biological and domestic rhythm of waking, retiring, and maintaining bodily habits.",
            "contrasts": [
                {"id": 1, "compared_word": "起居 vs. 饮食", "pinyin": "yǐnshí", "analysis": "饮食 covers drinking and dining nutrition, whereas 起居 emphasizes sleep, rest, and mobility."},
                {"id": 2, "compared_word": "起居 vs. 作息", "pinyin": "zuòxī", "analysis": "作息 focuses narrowly on timetable schedules between work and breaks, while 起居 encompasses full domestic comfort."},
                {"id": 3, "compared_word": "起居 vs. 劳碌", "pinyin": "láolù", "analysis": "劳碌 expresses relentless draining toil, contrasting with peaceful, orderly 起居."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代四合院建筑充分体现了天人合一的居住智慧。四面合围的庭院把自然的光照与四季的新鲜空气引入起居空间，让居住者在起居饮食之间时刻感受到节气的变换，营造出安详悠闲的传统生活节奏。",
                "pinyin": "Zhōngguó gǔdiǎn sìhéyuàn jiànzhù chōngfèn tǐxiàn le tiānrén-héyī de jūzhù zhìhuì. Sìmiàn héwéi de tíngyuàn bǎ zìrán de guāngzhào yǔ sìjì de xīnxiān kōngqì yǐnrù qǐjū kōngjiān, ràng jūzhùzhě zài qǐjū yǐnshí zhījiān shíkè gǎnshòudào jiéqì de biànhuàn, yíngzào chū ānxiáng yōuxián de chuántǒng shēnghuó jiézòu.",
                "en": "Classical courtyards embodied ancient wisdom of harmony between humanity and nature. The courtyard channeled sunlight and fresh air into daily living quarters, allowing inhabitants to perceive changing seasons throughout their daily routines.",
                "es": "La arquitectura del siheyuan clásico refleja la armonía entre el hombre y el cosmos. Su patio canaliza luz natural y brisas hacia las estancias, permitiendo a los habitantes percibir las estaciones en su descanso y rutina diaria."
            },
            {
                "id": "#2",
                "hanzi": "传统养生学认为，起居有常是延年益寿的首要法则。顺应自然日月的更迭，日出而作、日落而息，保持良好的起居节律，不仅能够保养体内的气血精神，更能让心灵在宁静的作息中得到充分的滋养与放松。",
                "pinyin": "Chuántǒng yǎngshēngxué rènwéi, qǐjū yǒucháng shì yánnián-yìshòu de shǒuyào fǎzé. Shùnyìng zìrán rìyuè de gēngdié, rì chū ér zuò, rì luò ér xī, bǎochí liánghǎo de qǐjū jiélǜ, bùjǐn nénggòu bǎoyǎng tǐnèi de qìxuè jīngshén, gèng néng ràng xīnlíng zài níngjìng de zuòxī zhōng dédào chōngfèn de zīyǎng yǔ fàngsōng.",
                "en": "Traditional wellness asserts that regular daily rising and resting hours are the foremost principle of longevity. Rising with the dawn and resting at dusk preserves vitality and nurtures peace of mind through balanced living.",
                "es": "Las artes milenarias de la salud consideran que la regularidad en el descanso es ley primordial de longevidad. Despertar con el sol y reposar al anochecer templa la energía vital y serena el espíritu mediante un ritmo armónico."
            }
        ]
    },

    # 18 接待
    {
        "id": "18",
        "hanzi": "接待",
        "pinyin": "jiē dài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to receive; host; entertain (guests/visitors)",
            "es": "recibir; acoger; atender; hospedar (a huéspedes o visitantes)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to meet, receive, and accommodate guests, clients, or visiting delegations with hospitality",
                "definition_es": "recibir, dar la bienvenida y atender con cortesía a invitados, clientes o delegaciones",
                "example_phrase": "热情接待 (receive warmly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在老北京四合院中，正房正厅通常作为接待重要宾朋的客厅，以展现主人的热情与礼仪。",
                "pinyin": "Zài lǎo Běijīng sìhéyuàn zhōng, zhèngfáng zhèngtīng tōngcháng zuòwéi jiēdài zhòngyào bīnpéng de kètīng, yǐ zhǎnxiàn zhǔrén de rèqíng yǔ lǐyí.",
                "en": "In old Beijing courtyards, the central hall of the main building served as a parlor to receive important guests with warmth and etiquette.",
                "es": "En el siheyuan pekinés, la sala central del pabellón principal servía de salón para recibir a visitantes ilustres con calidez y cortesía."
            },
            {
                "id": "#2",
                "hanzi": "本届博览会的主办方设立了专业的多语种接待中心，全天候为各国展商提供周到细致的服务。",
                "pinyin": "Běnjiè bólǎnhuì de zhǔbànfāng shèlì le zhuānyè de duōyǔzhǒng jiēdài zhōngxīn, quántiānhòu wèi gèguó zhǎnshāng tígōng zhōudào xìzhì de fúwù.",
                "en": "The organizers of the expo established a professional multilingual reception center to provide attentive service to international exhibitors round the clock.",
                "es": "Los organizadores de la exposición inauguraron un centro de recepción multilingüe para brindar atención solícita a expositores internacionales."
            }
        ],
        "collocations": [
            {"hanzi": "热情接待", "en": "warm reception"},
            {"hanzi": "接待客人", "en": "receive guests / visitors"},
            {"hanzi": "接待中心", "en": "reception center"},
            {"hanzi": "接待人员", "en": "reception staff"},
            {"hanzi": "接待标准", "en": "protocol standard for reception"},
            {"hanzi": "隆重接待", "en": "grand ceremonial reception"}
        ],
        "idioms": [
            {"hanzi": "彬彬有礼", "pinyin": "bīn bīn yǒu lǐ", "meaning_en": "refined and courteous in manners"},
            {"hanzi": "客客气气", "pinyin": "kè kè qì qì", "meaning_en": "extremely polite and cordial"},
            {"hanzi": "虚左以待", "pinyin": "xū zuǒ yǐ dài", "meaning_en": "leave the seat of honor vacant to welcome worthy guests"},
            {"hanzi": "扫榻以待", "pinyin": "sǎo tà yǐ dài", "meaning_en": "sweep the couch clean to receive esteemed guests"}
        ],
        "character_decomposition": [
            {
                "character": "接",
                "pinyin": "jiē",
                "meaning_en": "receive; connect; take over; meet",
                "meaning_es": "recibir; conectar; tomar el relevo; encontrarse",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand reaching out) + 妾 (woman bowing in reception)",
                "sound_component": "妾 (qiè / phonetic association)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Extending a welcoming hand 扌 forward to meet and connect with another person; to receive.",
                "visual_mnemonic_story_en": "Reaching out open hands (扌) warmly to welcome a visitor across the threshold (接).",
                "visual_mnemonic_story_es": "Extender las manos abiertas (扌) con afecto para recibir a un viajero en el umbral (接).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QYT",
                "traditional": "接"
            },
            {
                "character": "待",
                "pinyin": "dài",
                "meaning_en": "treat; entertain; wait for; attend",
                "meaning_es": "tratar; acoger; aguardar; atender",
                "radical": "彳",
                "radical_meaning_en": "step / walk slowly",
                "meaning_component": "彳 (step along walkway) + 寺 (monastery/court hall with hand hold)",
                "sound_component": "寺 (sì / phonetic root)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Waiting along a ceremonial hall path 彳 to attend upon arriving guests 寺 with dignified hospitality.",
                "visual_mnemonic_story_en": "Stepping out onto the porch (彳) to attend to and treat a waited guest with care (待).",
                "visual_mnemonic_story_es": "Avanzar unos pasos por el porche (彳) para acoger y agasajar al huésped esperado (待).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HOGDI",
                "traditional": "待"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Welcoming with open hands (接) and treating hospitably (待) equals receiving guests (接待).",
            "composite_memory_hook_es": "Dar la bienvenida con las manos (接) y agasajar con esmero (待) conforma el acto de acoger (接待).",
            "cultural_and_cognitive_roots": "Essential concept of traditional Chinese hospitality where hosts go out to the courtyard gate to receive visitors.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'jiē dài' (55-51). High steady pitch on 'jiē', followed by a crisp downward drop on 'dài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "按", "pinyin": "àn", "meaning_en": "press; according to", "distinction_note": "Safe radical 安 on the right instead of 妾"},
                {"character": "搂", "pinyin": "lǒu", "meaning_en": "hug; embrace", "distinction_note": "Lou radical 娄 on the right instead of 妾"},
                {"character": "持", "pinyin": "chí", "meaning_en": "hold; maintain", "distinction_note": "Hand radical 扌 on left instead of step 彳"},
                {"character": "侍", "pinyin": "shì", "meaning_en": "serve; attend upon", "distinction_note": "Person radical 亻 on left instead of 彳"}
            ],
            "etymological_cognates": [
                {"character": "接见", "pinyin": "jiējiàn", "gloss_en": "grant interview; receive officially"},
                {"character": "招待", "pinyin": "zhāodài", "gloss_en": "entertain; hospitality"},
                {"character": "迎接", "pinyin": "yíngjiē", "gloss_en": "greet; welcome"},
                {"character": "待遇", "pinyin": "dàiyù", "gloss_en": "treatment; compensation"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "接待 implies formal or courteous hospitality shown to visitors, clients, or travelers.",
            "contrasts": [
                {"id": 1, "compared_word": "接待 vs. 招待", "pinyin": "zhāodài", "analysis": "招待 leans heavily toward serving food and drinks (banquets/feasts), while 接待 focuses on overall reception protocol."},
                {"id": 2, "compared_word": "接待 vs. 迎接", "pinyin": "yíngjiē", "analysis": "迎接 is the physical action of going out to meet arriving guests, while 接待 encompasses the entire hosting process."},
                {"id": 3, "compared_word": "接待 vs. 怠慢", "pinyin": "dàimàn", "analysis": "怠慢 is the direct antonym meaning to cold-shoulder or neglect visiting guests."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的建筑格局对接待客人有着极为明确的礼仪界限。普通访客通常在外院倒座房接待，而尊贵挚友才会被请入内院正房品茗叙旧。这种层次分明的接待规制，体现了中国古人内外有别的待客智慧。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de jiànzhù géjú duì jiēdài kèrén yǒu zhe jíwéi míngquè de lǐyí jièxiàn. Pǔtōng fǎngkè tōngcháng zài wàiyuàn dàozuòfáng jiēdài, ér zūnguì zhìyǒu cái huì bèi qǐng rù nèiyuàn zhèngfáng pǐnmíng xùjiù. Zhè zhǒng céngcì fēnmíng de jiēdài guīzhì, tǐxiàn le Zhōngguó gǔrén nèiwài-yǒubié de dàikè zhìhuì.",
                "en": "The architectural layout of old Beijing quadrangles had clear etiquette boundaries for receiving guests. Ordinary visitors were received in outer gate rooms, while honored friends entered the inner courtyard parlor, showing refined hospitality codes.",
                "es": "La distribución del siheyuan pekinés establecía límites ceremoniales para recibir visitas. Los visitantes corrientes eran atendidos en el patio exterior, mientras los allegados pasaban al salón interior, reflejando códigos de cortesía."
            },
            {
                "id": "#2",
                "hanzi": "在现代涉外商务交流中，专业热情的接待往往能够为合作奠定坚实的信任基石。从机场迎接的真诚微笑，到会谈室中妥帖的茶水准备，每一个接待细节都在无声地传递着企业的文化素养。体贴入微的接待让远道而来的客户宾至如归。",
                "pinyin": "Zài xiàndài shèwài shāngwù jiāoliú zhōng, zhuānyè rèqíng de jiēdài wǎngwǎng nénggòu wèi hézuò diàndìng jiānshí de xìnrèn jīshí. Cóng jīchǎng yíngjiē de zhēnchéng wēixiào, dào huìtánshì zhōng tuǒtiē de cháshuǐ zhǔnbèi, měi yī gè jiēdài xìjié dōu zài wúshēng de chuándì zhe qǐyè de wénhuà sùyǎng. Tǐtiē-rùwēi de jiēdài ràng yuǎndào-érlái de kèhù bīnzhìrúguī.",
                "en": "In modern foreign business relations, professional and warm reception lays a solid foundation of trust. From welcoming smiles at the airport to thoughtful amenities in the conference room, hospitable details make visiting clients feel truly at home.",
                "es": "En las relaciones comerciales internacionales modernas, una acogida solícita sienta las bases de la confianza. Desde la sonrisa cordial en el aeropuerto hasta los pormenores en la sala de juntas, cada atención hace sentir al huésped en casa."
            }
        ]
    },

    # 19 功能
    {
        "id": "19",
        "hanzi": "功能",
        "pinyin": "gōng néng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "function; capability; feature",
            "es": "función; capacidad; funcionalidad"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the specific purpose, natural capacity, or operational duty of an object, organ, or system",
                "definition_es": "propósito específico, capacidad operativa o función determinada de un objeto, órgano o sistema",
                "example_phrase": "发挥功能 (bring one's function into play)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在四合院的四面建筑中，各个房屋具备明确而互补的起居功能，共同满足大家庭的生活需要。",
                "pinyin": "Zài sìhéyuàn de sìmiàn jiànzhù zhōng, gègè fángwū jùbèi míngquè ér hùbǔ de qǐjū gōngnéng, gòngtóng mǎnzú dàjiātíng de shēnghuó xūyào.",
                "en": "Among the four-sided buildings of a courtyard, each room possessed clear, complementary living functions fulfilling the extended family's needs.",
                "es": "Entre las cuatro alas del patio, cada edificio reunía funciones residenciales precisas y complementarias para satisfacer a la familia extendida."
            },
            {
                "id": "#2",
                "hanzi": "长期坚持适度的有氧运动，能够显著增强人体心肺系统的机能与免疫调节功能。",
                "pinyin": "Chángqī jiānchí shìdù de yǒuyǎng yùndòng, nénggòu xiǎnzhù zēngqiáng réntǐ xīnfèi xìtǒng de jīnéng yǔ miǎnyì tiáojié gōngnéng.",
                "en": "Consistently practicing moderate aerobic exercise over the long term can notably strengthen the cardiopulmonary capacity and immune regulatory functions.",
                "es": "La práctica continua de ejercicio aeróbico moderado fortalece notablemente el rendimiento cardiopulmonar y las funciones de regulación inmunológica."
            }
        ],
        "collocations": [
            {"hanzi": "主要功能", "en": "primary function / key feature"},
            {"hanzi": "发挥功能", "en": "bring function into full play"},
            {"hanzi": "功能齐全", "en": "fully equipped with all features"},
            {"hanzi": "实用功能", "en": "practical function / utility"},
            {"hanzi": "生理功能", "en": "physiological function"},
            {"hanzi": "特殊功能", "en": "special feature / unique function"}
        ],
        "idioms": [
            {"hanzi": "各尽其能", "pinyin": "gè jìn qí néng", "meaning_en": "each does one's utmost according to abilities"},
            {"hanzi": "无所不能", "pinyin": "wú suǒ bù néng", "meaning_en": "omnipotent; capable of doing anything"},
            {"hanzi": "用武之地", "pinyin": "yòng wǔ zhī dì", "meaning_en": "scope or battlefield to exercise one's talents"},
            {"hanzi": "实至名归", "pinyin": "shí zhì míng guī", "meaning_en": "reputation deserved by actual merit"}
        ],
        "character_decomposition": [
            {
                "character": "功",
                "pinyin": "gōng",
                "meaning_en": "merit; achievement; skill; work",
                "meaning_es": "mérito; logro; destreza; trabajo",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "工 (work/carpenter's square) + 力 (physical strength)",
                "sound_component": "工 (gōng)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Applying physical effort 力 to complete constructive craft work 工; signifies fruitful results.",
                "visual_mnemonic_story_en": "Exerting strength (力) through skilled artisan craft (工) to produce fruitful work (功).",
                "visual_mnemonic_story_es": "Aplicar la fuerza física (力) mediante el hábil trabajo artesanal (工) para lograr frutos útiles (功).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MKS",
                "traditional": "功"
            },
            {
                "character": "能",
                "pinyin": "néng",
                "meaning_en": "ability; capable; can; energy",
                "meaning_es": "capacidad; poder; apto; energía",
                "radical": "月",
                "radical_meaning_en": "flesh / meat",
                "meaning_component": "pictograph of a powerful muscular bear with strong claws and jaw",
                "sound_component": "能 (néng)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient pictograph of a bear with immense muscular endurance and prowess; signifies capability.",
                "visual_mnemonic_story_en": "A vigorous bear possessing the raw strength and boundless ability (能) to climb high peaks.",
                "visual_mnemonic_story_es": "Un oso robusto provisto de gran fortaleza muscular y facultad para dominar cumbres (能).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IBPP",
                "traditional": "能"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Work-merit (功) combined with inherent capability (能) creates an effective function (功能).",
            "composite_memory_hook_es": "El fruto del trabajo (功) sumado a la facultad inherente (能) da lugar a la funcionalidad práctica (功能).",
            "cultural_and_cognitive_roots": "Blends Confucian practical efficacy (功用) with systemic capabilities, ubiquitous in modern engineering and biology.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'gōng néng' (55-35). Begin high and level, then lift dynamically upward."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "攻", "pinyin": "gōng", "meaning_en": "attack; assault", "distinction_note": "Rap radical 攵 on the right instead of 力"},
                {"character": "巧", "pinyin": "qiǎo", "meaning_en": "skillful; clever", "distinction_note": "Beg radical 丂 on the right instead of 力"},
                {"character": "熊", "pinyin": "xióng", "meaning_en": "bear", "distinction_note": "Four fire dots 灬 under the 能 glyph"},
                {"character": "态", "pinyin": "tài", "meaning_en": "manner; state", "distinction_note": "Heart radical 心 at bottom instead of full bear form"}
            ],
            "etymological_cognates": [
                {"character": "功效", "pinyin": "gōngxiào", "gloss_en": "efficacy; curative effect"},
                {"character": "能力", "pinyin": "nénglì", "gloss_en": "ability; capability"},
                {"character": "技能", "pinyin": "jìnéng", "gloss_en": "skill; craftsmanship"},
                {"character": "功能性", "pinyin": "gōngnéngxìng", "gloss_en": "functionality"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "功能 points to the objective operating utility, purpose, or capacity designed into an entity.",
            "contrasts": [
                {"id": 1, "compared_word": "功能 vs. 作用", "pinyin": "zuòyòng", "analysis": "作用 focuses on external consequences or effects exerted on something else, while 功能 is the intrinsic capability itself."},
                {"id": 2, "compared_word": "功能 vs. 性能", "pinyin": "xìngnéng", "analysis": "性能 measures the quality or benchmark of performance (e.g. engine speed), while 功能 lists the features."},
                {"id": 3, "compared_word": "功能 vs. 缺陷", "pinyin": "quēxiàn", "analysis": "缺陷 denotes structural bugs or flaws impairing an object's intended functionality."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "北京四合院的各处构件不仅造型优美，更蕴含着实用的物理功能。例如房顶上层层交错的筒瓦具备迅速排水与隔热遮阳的功能，庭院中央栽植的绿树则具备夏季遮阳、秋冬防风落叶的自然生态调节功能。",
                "pinyin": "Běijīng sìhéyuàn de gèchù gòujiàn bùjǐn zàoxíng yōuměi, gèng yùnhán zhe shíyòng de wùlǐ gōngnéng. Lìrú fángdǐng shang céngcéng jiāocuò de tǒngwǎ jùbèi xùnsù páishuǐ yǔ gérè zhēyáng de gōngnéng, tíngyuàn zhōngyāng zāizhí de lǜshù zé jùbèi xiàjì zhēyáng, qiūdōng fángfēng luòyè de zìrán shēngtài tiáojié gōngnéng.",
                "en": "Every element of Beijing quadrangles not only boasts graceful form, but also harbors practical physical functions. The overlapping roof tiles channel rapid drainage and insulation, while trees provide ecological shade and wind protection.",
                "es": "Cada componente del siheyuan pekinés encierra una valiosa función física. Las tejas curvas del tejado canalizan el desagüe y aíslan del calor, mientras la arboleda del patio aporta sombra en estío y cortavientos en otoño."
            },
            {
                "id": "#2",
                "hanzi": "智能手机的发展史，正是设备功能不断高度集成的演进史。如今的移动通信设备早已超越了单纯的通话功能，兼备了专业摄影、移动办公以及实时健康监测等多重功能。强大的综合功能，深刻重塑了当代人类的生活图景。",
                "pinyin": "Zhìnéng shǒujī de fāzhǎnshǐ, zhèngshì shèbèi gōngnéng bùduàn gāodù jíchéng de yǎnjìnshǐ. Rújīn de yídòng tōngxìn shèbèi zǎoyǐ chāoyuè le dānchún de tōnghuà gōngnéng, jiānbèi le zhuānyè shèyǐng, yídòng bàngōng yǐjí shíshí jiànkāng jiāncè děng duōchóng gōngnéng. Qiángdà de zōnghé gōngnéng, shēnkè zhòngsù le dāngdài rénlèi de shēnghuó tújǐng.",
                "en": "The history of smartphones is an evolution of heightened functional integration. Modern mobile devices have surpassed mere voice calls to incorporate photography, remote office suites, and health metrics, reshaping modern living.",
                "es": "La evolución del teléfono inteligente refleja una creciente convergencia de funcionalidades. Los terminales modernos van más allá de la telefonía para incorporar fotografía, trabajo en remoto y control de la salud, transformando la vida."
            }
        ]
    },

    # 20 厢房
    {
        "id": "20",
        "hanzi": "厢房",
        "pinyin": "xiāng fáng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "wing-room; side building (in a courtyard)",
            "es": "ala lateral; habitación lateral del patio (en un siheyuan)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "rooms built along the east and west flanks of a traditional Chinese quadrangle courtyard compound",
                "definition_es": "estancias o pabellones dispuestos en los flancos este y oeste de un patio cuadrangular chino",
                "example_phrase": "东厢房与西厢房 (east wing-room and west wing-room)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在老北京四合院中，东厢房与西厢房面对面并列排布，通常分配给家中的儿女居住或作为书房。",
                "pinyin": "Zài lǎo Běijīng sìhéyuàn zhōng, dōngxiāngfáng yǔ xīxiāngfáng miànduìmiàn bìngliè páibù, tōngcháng fēnpèi gěi jiāzhōng de érnǚ jūzhù huò zuòwéi shūfáng.",
                "en": "In old Beijing courtyards, the east and west wings stand face to face, traditionally assigned as residences for sons and daughters or as studies.",
                "es": "En el siheyuan pekinés, las alas este y oeste se disponen frente a frente, reservadas habitualmente para los hijos o como estudios familiares."
            },
            {
                "id": "#2",
                "hanzi": "主人经过精心修缮，把原本堆放旧物的西厢房改造成了一间窗明几净、古色古香的客人茶室。",
                "pinyin": "Zhǔrén jīngguò jīngxīn xiūshàn, bǎ yuánběn duīfàng jiùwù de xīxiāngfáng gǎizào chéng le yī jiān chuāngmíng-jǐjìng, gǔsè-gǔxiāng de kèrén cháshì.",
                "en": "After meticulous restoration, the owner renovated the west wing—once used for storage—into a spotless, classically styled tea room for guests.",
                "es": "Tras una esmerada rehabilitación, el dueño convirtió el ala oeste, otrora trastero, en un salón de té para invitados diáfano y de aire clásico."
            }
        ],
        "collocations": [
            {"hanzi": "东厢房", "en": "east wing-room"},
            {"hanzi": "西厢房", "en": "west wing-room"},
            {"hanzi": "修缮厢房", "en": "renovate / restore wing-rooms"},
            {"hanzi": "两侧厢房", "en": "wing-rooms on both flanks"},
            {"hanzi": "厢房格局", "en": "spatial layout of wing-rooms"},
            {"hanzi": "改建厢房", "en": "remodel wing-rooms"}
        ],
        "idioms": [
            {"hanzi": "西厢待月", "pinyin": "xī xiāng dài yuè", "meaning_en": "waiting for one's beloved in the west wing under moonlight"},
            {"hanzi": "雕梁画栋", "pinyin": "diāo liáng huà dòng", "meaning_en": "carved beams and painted rafters; ornate building"},
            {"hanzi": "门当户对", "pinyin": "mén dāng hù duì", "meaning_en": "matched well in social standing and lineage"},
            {"hanzi": "画栋飞甍", "pinyin": "huà dòng fēi méng", "meaning_en": "splendid and picturesque architectural cornices"}
        ],
        "character_decomposition": [
            {
                "character": "厢",
                "pinyin": "xiāng",
                "meaning_en": "wing-room; side building; compartment",
                "meaning_es": "ala lateral; habitación contigua; compartimento",
                "radical": "广",
                "radical_meaning_en": "shelter / wide house",
                "meaning_component": "广 (broad rooftop shelter) + 相 (mutual inspection/flanking trees)",
                "sound_component": "相 (xiāng)",
                "stroke_count": 12,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A shelter 广 built alongside flanking rows 相 of trees and courtyards; represents flanking wing-rooms.",
                "visual_mnemonic_story_en": "A roofed side wing (广) positioned face to face (相) across the garden courtyard (厢).",
                "visual_mnemonic_story_es": "Un ala techada (广) situada cara a cara (相) al otro lado del patio solariego (厢).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "IDBU",
                "traditional": "廂"
            },
            {
                "character": "房",
                "pinyin": "fáng",
                "meaning_en": "house; room; building; dwelling",
                "meaning_es": "casa; estancia; habitación; morada",
                "radical": "户",
                "radical_meaning_en": "single-leaf door",
                "meaning_component": "户 (single door of a dwelling) + 方 (square foundation plot)",
                "sound_component": "方 (fāng)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A domestic room accessed via a single front door 户 built atop a square lot 方; a room or chamber.",
                "visual_mnemonic_story_en": "Pushing open a wooden single door (户) to enter an inviting square bedroom chamber (房).",
                "visual_mnemonic_story_es": "Empujar una puerta de madera (户) para acceder a una acogedora estancia cuadrangular (房).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HYSH",
                "traditional": "房"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A flanking side shelter (厢) built as a domestic room (房) forms a courtyard wing-room (厢房).",
            "composite_memory_hook_es": "Un pabellón lateral (厢) construido como estancia habitable (房) conforma el ala del patio (厢房).",
            "cultural_and_cognitive_roots": "A cornerstone of classical courtyard layout embodying axial symmetry and Confucian generational housing rank.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'xiāng fáng' (55-35). Begin high and level, then glide smoothly up."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "箱", "pinyin": "xiāng", "meaning_en": "box; chest; suitcase", "distinction_note": "Bamboo radical 竹 on top instead of shelter 广"},
                {"character": "相", "pinyin": "xiāng", "meaning_en": "mutual; appearance", "distinction_note": "Lacks the enclosing shelter radical 广"},
                {"character": "防", "pinyin": "fáng", "meaning_en": "defend; guard against", "distinction_note": "Mound radical 阝 on left instead of single door 户"},
                {"character": "坊", "pinyin": "fāng", "meaning_en": "lane; workshop; neighborhood", "distinction_note": "Earth radical 土 on left instead of single door 户"}
            ],
            "etymological_cognates": [
                {"character": "车厢", "pinyin": "chēxiāng", "gloss_en": "railway carriage; train car"},
                {"character": "包厢", "pinyin": "bāoxiāng", "gloss_en": "private box (theater/dining)"},
                {"character": "房屋", "pinyin": "fángwū", "gloss_en": "houses; premises"},
                {"character": "房间", "pinyin": "fángjiān", "gloss_en": "room; chamber"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "厢房 refers specifically to the east and west flanking lateral wings of a courtyard compound.",
            "contrasts": [
                {"id": 1, "compared_word": "厢房 vs. 正房", "pinyin": "zhèngfáng", "analysis": "正房 is the principal north-facing building reserved for elders, while 厢房 are secondary lateral flank buildings."},
                {"id": 2, "compared_word": "厢房 vs. 倒座房", "pinyin": "dàozuòfáng", "analysis": "倒座房 sits along the southern perimeter facing north toward the courtyard, distinct from east-west 厢房."},
                {"id": 3, "compared_word": "厢房 vs. 耳房", "pinyin": "ěrfáng", "analysis": "耳房 are small ear-like adjoining annexes attached to the sides of the main room, not standalone lateral wings."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "四合院东西两侧的厢房，是维系传统家族生活的重要场所。按照长幼次序的旧礼，东厢房采光更加充足，地位略高于西厢房，多安排给长子居住。两座厢房隔院相对，既保持了各房的独立，又方便彼此照料走动。",
                "pinyin": "Sìhéyuàn dōngxī liǎngcè de xiāngfáng, shì wéixì chuántǒng jiāzú shēnghuó de zhòngyào chǎngsuǒ. Ànzhào zhǎngyòu cìxù de jiùlǐ, dōngxiāngfáng cǎiguāng gèngjiā chōngzú, dìwèi lüègāo yú xīxiāngfáng, duō ānpái gěi zhǎngzǐ jūzhù. Liǎng zuò xiāngfáng gé yuàn xiāngduì, jì bǎochí le gè fáng de dúlì, yòu fāngbiàn bǐcǐ zhàoliào zǒudòng.",
                "en": "The side wings on the east and west of a courtyard were crucial spaces sustaining traditional family life. By old customs, the east wing enjoyed better daylight and slightly higher rank, housing the eldest son. Facing across the yard, they maintained privacy while facilitating mutual care.",
                "es": "Las alas este y oeste del siheyuan eran vitales para la convivencia familiar. Según la tradición, el ala este recibía mejor luz y rango, habitada por el primogénito. Enfrentadas a través del patio, aseguraban independencia y cercanía."
            },
            {
                "id": "#2",
                "hanzi": "中国古代著名的杂剧名作《西厢记》，正是发生在一座幽静寺院西厢房里的爱情传奇。崔莺莺与张生冲破封建礼教的重重禁锢，在月色映照下的西厢房里互诉衷肠。这出优美的经典戏剧，赋予了传统厢房无尽的诗意浪漫与文学底蕴。",
                "pinyin": "Zhōngguó gǔdài zhùmíng de zájù míngzuò Xīxiāngjì, zhèngshì fāshēng zài yī zuò yōujìng sìyuàn xīxiāngfáng lǐ de àiqíng chuánqí. Cuī Yīngyīng yǔ Zhāng Shēng chōngpò fēngjiàn lǐjiào de chóngchóng jìngù, zài yuèshè yìngzhào xià de xīxiāngfáng lǐ hù sù zhōngcháng. Zhè chū yōuměi de jīngdiǎn xìjù, fùyǔ le chuántǒng xiāngfáng wújìn de shīyì làngmàn yǔ wénxué dǐyùn.",
                "en": "The famous ancient drama 'Romance of the Western Chamber' tells an enduring love legend unfolding in the west wing of a quiet temple. Cui Yingying and Zhang Sheng broke through feudal constraints under moonlight, infusing the term with timeless literary romance.",
                "es": "El célebre drama clásico chino 'Romance del Pabellón Occidental' narra un romance en el ala oeste de un monasterio. Cui Yingying y Zhang Sheng desafiaron las ataduras feudales bajo la luna, impregnando este espacio de eterna poesía y romance literario."
            }
        ]
    }
]

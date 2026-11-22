# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 胜利
    {
        "id": "21",
        "hanzi": "胜利",
        "pinyin": "shèng lì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to win victory; triumph; victory; successfully",
            "es": "vencer; triunfar; victoria; triunfo; con éxito"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to vanquish an opponent, win a contest or battle, or achieve success in an undertaking",
                "definition_es": "derrotar al adversario, coronar con éxito una batalla o alcanzar el triunfo en un empeño",
                "example_phrase": "取得辉煌胜利 (achieve a glorious victory)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军凭借高超的诱敌战术与严密的包围圈，在惨烈的长平之战中取得了决定性的战略胜利。",
                "pinyin": "Qínjūn píngjiè gāochāo de yòudí zhànshù yǔ yánmì de bāowéiquān, zài cǎnliè de Chángpíng zhī zhàn zhōng qǔdé le juédìngxìng de zhànlüè shènglì.",
                "en": "Relying on tactics of luring the enemy and tight encirclement, Qin secured a decisive strategic victory at the Battle of Changping.",
                "es": "Valiéndose de astutas celadas y un cerco impenetrable, el ejército de Qin obtuvo una decisiva victoria estratégica en Changping."
            },
            {
                "id": "#2",
                "hanzi": "经过长达数年的艰苦攻关，该科研项目终于胜利完成了全部核心技术指标的验证工作。",
                "pinyin": "Jīngguò cháng dá shù nián de jiānkǔ gōngguān, gāi kēyán xiàngmù zhōngyú shènglì wánchéng le quánbù héxīn jìshù zhǐbiāo de yànzhèng gōngzuò.",
                "en": "After years of arduous research breakthroughs, the scientific project finally concluded the verification of all core technical benchmarks with success.",
                "es": "Tras años de abnegada investigación, el proyecto culminó con éxito la verificación de todos sus parámetros técnicos primordiales."
            }
        ],
        "collocations": [
            {"hanzi": "取得胜利", "en": "achieve / win victory"},
            {"hanzi": "胜利闭幕", "en": "successfully conclude (a congress/meeting)"},
            {"hanzi": "胜利成果", "en": "fruits of victory"},
            {"hanzi": "走向胜利", "en": "march toward triumph"},
            {"hanzi": "重大胜利", "en": "major / momentous victory"},
            {"hanzi": "胜利在望", "en": "victory in sight"}
        ],
        "idioms": [
            {"hanzi": "旗开得胜", "pinyin": "qí kāi dé shèng", "meaning_en": "win victory at the first unfurling of the flag"},
            {"hanzi": "克敌制胜", "pinyin": "kè dí zhì shèng", "meaning_en": "vanquish the foe and secure victory"},
            {"hanzi": "战无不胜", "pinyin": "zhàn wú bù shèng", "meaning_en": "invincible in every battle; triumph in all campaigns"},
            {"hanzi": "反败为胜", "pinyin": "fǎn bài wéi shèng", "meaning_en": "turn defeat into victory at the critical juncture"}
        ],
        "character_decomposition": [
            {
                "character": "胜",
                "pinyin": "shèng",
                "meaning_en": "win; victory; surpass; bear; superb",
                "meaning_es": "vencer; triunfar; superar; magnífico",
                "radical": "月",
                "radical_meaning_en": "flesh / organ",
                "meaning_component": "月/肉 (flesh / inner sinew strength) + 𢎘/生 (bursting upward growth)",
                "sound_component": "𢎘 (shèng)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Robust muscular endurance 月 overcoming obstacles to rise above all rivals 生; to vanquish.",
                "visual_mnemonic_story_en": "Muscular vitality (月) surging forth with explosive power to conquer challenges (胜).",
                "visual_mnemonic_story_es": "La pujanza física (月) emergiendo con vigor invicto para superar al oponente (胜).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BFQ",
                "traditional": "勝"
            },
            {
                "character": "利",
                "pinyin": "lì",
                "meaning_en": "sharp; benefit; profit; favorable",
                "meaning_es": "afilado; beneficio; provecho; favorable",
                "radical": "刂",
                "radical_meaning_en": "knife / blade",
                "meaning_component": "禾 (ripe grain crop) + 刂 (reaping sickle blade)",
                "sound_component": "利 (lì)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A sharp sickle 刂 harvesting golden ripe grain stalks 禾 with swift ease; signifies reaping benefits and success.",
                "visual_mnemonic_story_en": "A sharp blade (刂) smoothly cutting golden grain stalks (禾) to reap a bountiful harvest (利).",
                "visual_mnemonic_story_es": "Una hoz afilada (刂) segando espigas doradas (禾) para recoger una cosecha provechosa (利).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HDN",
                "traditional": "利"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Vanquishing an adversary through strength (胜) and reaping the fruitful spoils (利) defines victory (胜利).",
            "composite_memory_hook_es": "Superar al adversario en la contienda (胜) y recoger los frutos laureados (利) constituye la victoria (胜利).",
            "cultural_and_cognitive_roots": "Blends martial triumph over rivals with the auspicious harvest of benefits and peace.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'shèng lì' (51-51). Pronounce both syllables with energetic, triumphant downward inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "脸", "pinyin": "liǎn", "meaning_en": "face", "distinction_note": "Lian 佥 on right of 月 instead of 𢎘"},
                {"character": "服", "pinyin": "fú", "meaning_en": "clothes; obey", "distinction_note": "Fu 𠬝 on right of 月 instead of 𢎘"},
                {"character": "科", "pinyin": "kē", "meaning_en": "science", "distinction_note": "Dipper 斗 on right of 禾 instead of 刂"},
                {"character": "和", "pinyin": "hé", "meaning_en": "harmony; with", "distinction_note": "Mouth 口 on right of 禾 instead of 刂"}
            ],
            "etymological_cognates": [
                {"character": "胜利者", "pinyin": "shènglìzhě", "gloss_en": "victor; winner"},
                {"character": "获胜", "pinyin": "huòshèng", "gloss_en": "win victory; triumph"},
                {"character": "利益", "pinyin": "lìyì", "gloss_en": "benefit; interest"},
                {"character": "利用", "pinyin": "lìyòng", "gloss_en": "utilize; exploit"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "胜利 indicates triumphant conquest of an opponent, challenge, or military campaign.",
            "contrasts": [
                {"id": 1, "compared_word": "胜利 vs. 失败", "pinyin": "shībài", "analysis": "失败 is the direct antonym meaning defeat, failure, or collapse."},
                {"id": 2, "compared_word": "胜利 vs. 成功", "pinyin": "chénggōng", "analysis": "成功 is broader and applies to fulfilling personal plans or tasks, while 胜利 strongly implies defeating a rival in a contest or battle."},
                {"id": 3, "compared_word": "胜利 vs. 平局", "pinyin": "píngjú", "analysis": "平局 means a tie or draw, where neither side secures 胜利."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平之战的胜利，使秦国彻底摧毁了东方六国中军事实力最强的赵国主力。秦军主帅白起以高超的诱敌与穿插包围战术载入史册。这场巨大的军事胜利，为后来秦始皇吞并六国、一统华夏奠定了坚实的战略基础。",
                "pinyin": "Chángpíng zhī zhàn de shènglì, shǐ Qínguó chèdǐ cuīhuǐ le dōngfāng liùguó zhōng jūnshì shílì zuì qiáng de Zhàoguó zhǔlì. Qínjūn zhǔshuài Bái Qǐ yǐ gāochāo de yòudí yǔ chuānchā-bāowéi zhànshù zǎirù shǐcè. Zhè chǎng jùdà de jūnshì shènglì, wèi hòulái Qín Shǐhuáng tūnbìng liùguó, yītǒng Huáxià diàndìng le jiānshí de zhànlüè jīchǔ.",
                "en": "Victory at Changping allowed Qin to crush the elite army of Zhao, the strongest among the six states. General Bai Qi's brilliant tactics entered history. This monumental victory laid the strategic foundation for Qin Shihuang's unification of China.",
                "es": "La victoria en Changping permitió a Qin aniquilar al ejército de Zhao, el rival más formidable de los reinos orientales. Las maniobras de Bai Qi pasaron a la historia, sentando las bases estratégicas para la unificación de China."
            },
            {
                "id": "#2",
                "hanzi": "在漫长曲折的人生征程中，真正的胜利从来不是唾手可得的偶然幸运，而是无数个日夜默默耕耘、百折不挠的必然奖赏。在挫折面前永不放弃、在逆境中越战越勇的人，最终必将迎来属于自己的辉煌胜利。",
                "pinyin": "Zài màncháng-qūzhé de rénshēng zhēngchéng zhōng, zhēnzhèng de shènglì cónglái bùshì tuòshǒu-kědé de ǒurán xìngyùn, ér shì wúshù gè rìyè mòmò gēngyún, bǎizhé-bùnáo de bìrán jiǎngshǎng. Zài cuòzhé miànqián yǒng bù fàngqì, zài nìjìng zhōng yuè zhàn yuè yǒng de rén, zuìzhōng bìjiāng yínglái shǔyú zìjǐ de huīhuáng shènglì.",
                "en": "On life's winding journey, authentic victory is never a windfall of luck, but the inevitable reward for quiet dedication and unyielding resilience. Those who refuse to surrender before adversity will embrace their glorious triumph in the end.",
                "es": "En la travesía de la vida, el triunfo auténtico no es fruto del azar, sino el premio al tesón callado y a la entereza indomable. Quien no ceja ante los reveses y se crece en el infortunio alcanza tarde o temprano su propia victoria."
            }
        ]
    },

    # 22 调动
    {
        "id": "22",
        "hanzi": "调动",
        "pinyin": "diào dòng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to mobilize; transfer; reassign; maneuver; arouse",
            "es": "movilizar; trasladar; reasignar; maniobrar; incentivar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to redeploy or transfer military forces, personnel, or material resources; to arouse enthusiasm",
                "definition_es": "trasladar o reasignar tropas, personal o recursos; activar la motivación o iniciativa",
                "example_phrase": "调动工作岗位 (transfer to a new job post)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军统帅白起精通兵法，善于调动敌军，通过假装溃败巧妙诱使赵括脱离险要阵地。",
                "pinyin": "Qínjūn tǒngshuài Bái Qǐ jīngtōng bīngfǎ, shànyú diàodòng dírén, tōngguò jiǎzhuāng kuìbài qiǎomiào yòushǐ Zhào Kuò tuōlí xiǎnyào zhèndì.",
                "en": "Qin General Bai Qi mastered strategy and excelled at maneuvering enemy forces, faking a rout to lure Zhao Kuo out of his bastions.",
                "es": "El general Bai Qi dominaba el arte bélico y sabía mover al enemigo, simulando una desbandada para sacar a Zhao Kuo de sus posiciones."
            },
            {
                "id": "#2",
                "hanzi": "优秀的领导者善于建立科学合理的激励机制，充分调动全体员工的工作积极性与创造潜能。",
                "pinyin": "Yōuxiù de lǐngdǎozhě shànyú jiànlì kēxué hélǐ de jīlì jīzhì, chōngfèn diàodòng quántǐ yuángōng de gōngzuò jījíxìng yǔ chuàngzào qiánnéng.",
                "en": "Outstanding leaders excel at instituting incentive systems to fully mobilize staff enthusiasm and creative potential.",
                "es": "Los líderes sobresalientes saben articular incentivos justos para movilizar la motivación y el potencial creador del personal."
            }
        ],
        "collocations": [
            {"hanzi": "调动兵力", "en": "redeploy / maneuver troops"},
            {"hanzi": "调动积极性", "en": "arouse / mobilize enthusiasm"},
            {"hanzi": "工作调动", "en": "job transfer / reassignment"},
            {"hanzi": "调动资源", "en": "mobilize resources"},
            {"hanzi": "紧急调动", "en": "emergency redeployment"},
            {"hanzi": "调动作战部队", "en": "maneuver combat units"}
        ],
        "idioms": [
            {"hanzi": "兵贵神速", "pinyin": "bīng guì shén sù", "meaning_en": "speed is precious in warfare; lightning troop movements"},
            {"hanzi": "调兵遣将", "pinyin": "diào bīng qiǎn jiàng", "meaning_en": "deploy troops and dispatch generals; marshal forces"},
            {"hanzi": "指东打西", "pinyin": "zhǐ dōng dǎ xī", "meaning_en": "point to the east while attacking the west; feint maneuver"},
            {"hanzi": "声东击西", "pinyin": "shēng dōng jī xī", "meaning_en": "make a sound in the east and strike in the west"}
        ],
        "character_decomposition": [
            {
                "character": "调",
                "pinyin": "diào",
                "meaning_en": "transfer; shift; tune; tone; investigate",
                "meaning_es": "trasladar; cambiar; tono; melodía; investigar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken command) + 周 (complete cycle / universal circulation)",
                "sound_component": "周 (zhōu)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken administrative directives 讠 circulating troops and personnel around 周 the realm; to transfer.",
                "visual_mnemonic_story_en": "Words of administrative command (讠) circulating personnel across districts in a smooth cycle (周) to reassign them (调).",
                "visual_mnemonic_story_es": "Órdenes oficiales orales (讠) que trasladan tropas a través de las comarcas en un circuito ordenado (周) para reasignarlas (调).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVBGR",
                "traditional": "調"
            },
            {
                "character": "动",
                "pinyin": "dòng",
                "meaning_en": "move; act; stir; motion",
                "meaning_es": "mover; actuar; movimiento; impulso",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "云 (clouds swirling across sky) + 力 (physical strength)",
                "sound_component": "云 (yún)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Applying physical force 力 to induce dynamic motion like drifting clouds 云.",
                "visual_mnemonic_story_en": "Applying strength (力) to shift heavy objects like dynamic clouds (动).",
                "visual_mnemonic_story_es": "Aplicar la fuerza (力) para mover objetos pesados con soltura de nubes (动).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MIS",
                "traditional": "動"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Issuing verbal directives (调) to set resources and troops into motion (动) means to mobilize and redeploy (调动).",
            "composite_memory_hook_es": "Impartir mandatos administrativos (调) para poner recursos en movimiento (动) define la movilización y traslado (调动).",
            "cultural_and_cognitive_roots": "Derived from imperial tally systems (虎符) where generals redeployed garrisons with royal bronze seals.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'diào dòng' (51-51). Pronounce both syllables with brisk, administrative firmness."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "词", "pinyin": "cí", "meaning_en": "word; lyrics", "distinction_note": "Department 司 on right of 讠 instead of 周"},
                {"character": "诵", "pinyin": "sòng", "meaning_en": "recite; chant", "distinction_note": "Yong 甬 on right of 讠 instead of 周"},
                {"character": "功", "pinyin": "gōng", "meaning_en": "merit; skill", "distinction_note": "Work 工 on left of 力 instead of 云"},
                {"character": "劫", "pinyin": "jié", "meaning_en": "plunder", "distinction_note": "Go 去 on left of 力 instead of 云"}
            ],
            "etymological_cognates": [
                {"character": "调度", "pinyin": "diàodù", "gloss_en": "dispatch; control traffic"},
                {"character": "调换", "pinyin": "diàohuàn", "gloss_en": "exchange; swap"},
                {"character": "动向", "pinyin": "dòngxiàng", "gloss_en": "trend; movement"},
                {"character": "发动", "pinyin": "fādòng", "gloss_en": "launch; mobilize"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "调动 highlights deliberate reallocation of personnel, troops, or psychological motivation.",
            "contrasts": [
                {"id": 1, "compared_word": "调动 vs. 移动", "pinyin": "yídòng", "analysis": "移动 refers to physical shifting in spatial location (move chairs/furniture), while 调动 is administrative reassignment or strategic maneuvering."},
                {"id": 2, "compared_word": "调动 vs. 派遣", "pinyin": "pàiqiǎn", "analysis": "派遣 means sending someone out on an assignment, while 调动 implies shifting or reassigning posts."},
                {"id": 3, "compared_word": "调动 vs. 固定", "pinyin": "gùdìng", "analysis": "固定 is the direct antonym meaning firmly fixed and unchanging."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "善于用兵的统帅，精髓在于“能调动敌人而不被敌人调动”。长平之战中，秦军统帅白起指挥若定，通过诈败后撤与穿插突袭，把四十万赵军一步步调动进预先设好的包围圈，将调动敌军的战术艺术演绎到了极致。",
                "pinyin": "Shànyú yòngbīng de tǒngshuài, jīngsuǐ zàiyú 'néng diàodòng dírén ér bù bèi dírén diàodòng'. Chángpíng zhī zhàn zhōng, Qínjūn tǒngshuài Bái Qǐ zhǐhuī-ruòdìng, tōngguò zhàbài hòuchè yǔ chuānchā tūxí, bǎ sìshí wàn Zhàojūn yībù-yībù diàodòng jìn yùxiān shè hǎo de bāowéiquān, jiāng diàodòng díjūn de zhànshù yìshù yǎnyì dào le jízhì.",
                "en": "The essence of generalship is moving the enemy without being moved. At Changping, General Bai Qi feigned retreat, maneuvering 400,000 Zhao troops step by step into a prearranged trap, demonstrating the supreme art of tactical redeployment.",
                "es": "La cumbre del arte militar reside en mover al enemigo sin dejarse mover por él. En Changping, Bai Qi fingió retiradas tácticas, atrayendo a 400.000 soldados de Zhao hacia la celada y elevando la maniobra militar a la maestría suprema."
            },
            {
                "id": "#2",
                "hanzi": "在现代社会治理与危机应对中，高效调动各方资源是战胜突发灾害的重要保证。无论是调动精锐医疗专家奔赴抗疫一线，还是跨区域调动应急救灾物资，强大的综合调度与动员能力，生动展现了国家治理体系的高效运作。",
                "pinyin": "Zài xiàndài shèhuì zhìlǐ yǔ wēijī yìngduì zhōng, gāoxiào diàodòng gèfāng zīyuán shì zhànshèng tūfā zāihài de zhòngyào bǎozhèng. Wúlùn shì diàodòng jīngruì yīliáo zhuānjiā bēnfù kàngyì yīxiàn, háishì kuà qūyù diàodòng yìngjí jiùzāi wùzī, qiángdà de zōnghé diàodù yǔ dòngyuán nénglì, shēngdòng zhǎnxiàn le guójiā zhìlǐ tǐxì de gāoxiào yùnzuò.",
                "en": "In modern crisis management, efficiently mobilizing resources guarantees victory over disaster. Whether redeploying medical experts to the frontline or coordinating disaster relief across provinces, mobilization capacity reflects good governance.",
                "es": "En la gestión moderna de catástrofes, movilizar recursos con presteza es la garantía del éxito. Ya sea trasladando médicos a la vanguardia o canalizando suministros de auxilio, la capacidad logística refleja la solidez del Estado."
            }
        ]
    },

    # 23 散布
    {
        "id": "23",
        "hanzi": "散布",
        "pinyin": "sàn bù",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to spread; disseminate; diffuse; scatter",
            "es": "difundir; esparcir; diseminar; propagar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to spread rumors, information, or opinions widely; to scatter objects across a surface",
                "definition_es": "propagar o difundir rumores, noticias o doctrinas en diversas direcciones; diseminar",
                "example_phrase": "散布谣言 (spread rumors)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦相范雎派间谍潜入邯郸，四处散布“秦军只怕赵奢之子赵括”的谣言，企图实施反间计。",
                "pinyin": "Qínxiàng Fàn Jū pài jiàndié qiánrù Hándān, sìchù sànbù 'Qínjūn zhǐ pà Zhào Shē zhī zǐ Zhào Kuò' de yáoyán, qǐtú shíshī fǎnjiànjì.",
                "en": "Qin's minister sent spies into Handan to spread rumors that 'Qin feared only Zhao Kuo,' aiming to carry out counter-espionage.",
                "es": "El canciller de Qin infiltró espías en Handan para propagar rumores de que Qin solo temía a Zhao Kuo, urdiendo un ardid de contraespionaje."
            },
            {
                "id": "#2",
                "hanzi": "在现代互联网公共空间中，任何网民都应当自觉抵制并拒绝散布未经证实的虚假消息。",
                "pinyin": "Zài xiàndài hùliánwǎng gōnggòng kōngjiān zhōng, rènhé wǎngmín dōu yīngdāng zìjué dǐzhì bìng jùjué sànbù wèijīng zhèngshí de xūjiǎ xiāoxi.",
                "en": "In modern internet cyberspace, every netizen should consciously resist and refuse to disseminate unverified false information.",
                "es": "En el ciberespacio actual, los internautas deben abstenerse conscientemente de difundir informaciones falsas no corroboradas."
            }
        ],
        "collocations": [
            {"hanzi": "散布谣言", "en": "spread rumors / hearsay"},
            {"hanzi": "散布虚假信息", "en": "disseminate false information"},
            {"hanzi": "四处散布", "en": "disseminate everywhere"},
            {"hanzi": "散布言论", "en": "spread statements / opinions"},
            {"hanzi": "散布种子", "en": "scatter seeds (literal)"},
            {"hanzi": "散布恐惧", "en": "spread fear and panic"}
        ],
        "idioms": [
            {"hanzi": "造谣生事", "pinyin": "zào yáo shēng shì", "meaning_en": "concoct rumors and stir up trouble"},
            {"hanzi": "风言风语", "pinyin": "fēng yán fēng yǔ", "meaning_en": "groundless talk and malicious slander in the wind"},
            {"hanzi": "满城风雨", "pinyin": "mǎn chéng fēng yǔ", "meaning_en": "the whole town is rife with gossip and rumors"},
            {"hanzi": "防民之口，甚于防川", "pinyin": "fáng mín zhī kǒu, shèn yú fáng chuān", "meaning_en": "stopping people's mouths is more dangerous than stopping a river"}
        ],
        "character_decomposition": [
            {
                "character": "散",
                "pinyin": "sàn",
                "meaning_en": "scatter; disperse; spread; break up",
                "meaning_es": "dispersar; esparcir; desbandar; difundir",
                "radical": "攵",
                "radical_meaning_en": "tap / strike",
                "meaning_component": "𢽳/𣏟 (hemp fibers beaten out) + 攵 (striking stick)",
                "sound_component": "散 (sàn)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Beating bundles of hemp with a stick 攵 so the fibers separate and scatter widely 散.",
                "visual_mnemonic_story_en": "Beating flax fibers with a rod (攵) so they disperse and scatter in all directions (散).",
                "visual_mnemonic_story_es": "Golpear gavillas con una vara (攵) para que las fibras se dispersen en todas direcciones (散).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TBOK",
                "traditional": "散"
            },
            {
                "character": "布",
                "pinyin": "bù",
                "meaning_en": "cloth; spread; declare; deploy",
                "meaning_es": "tela; paño; difundir; desplegar; proclamar",
                "radical": "巾",
                "radical_meaning_en": "cloth / fabric",
                "meaning_component": "巾 (woven cloth) + 𠂇 (hand spreading it out)",
                "sound_component": "布 (bù)",
                "stroke_count": 5,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A hand spreading out a woven bolt of cloth 巾 across the counter; signifies diffusing and publishing.",
                "visual_mnemonic_story_en": "Unrolling and spreading a long bolt of cloth (巾) across a broad table (布).",
                "visual_mnemonic_story_es": "Desenrollar y extender un lienzo de tela (巾) con la mano sobre la mesa (布).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "KLB",
                "traditional": "布"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Scattering outward in fragments (散) and spreading wide like a roll of cloth (布) means to disseminate (散布).",
            "composite_memory_hook_es": "Dispersar en fragmentos (散) y extender a lo ancho como un paño de tela (布) conforma la difusión (散布).",
            "cultural_and_cognitive_roots": "Associated with psychological warfare (反间计) in classical statecraft where false rumors were circulated into rival courts.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'sàn bù' (51-51). Articulate both syllables with decisive downward force."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "敦", "pinyin": "dūn", "meaning_en": "honest; sincere", "distinction_note": "Xiang 享 on left instead of 𣏟"},
                {"character": "敬", "pinyin": "jìng", "meaning_en": "respect", "distinction_note": "Gou 苟 on left of 攵 instead of 𣏟"},
                {"character": "希", "pinyin": "xī", "meaning_en": "hope; rare", "distinction_note": "Contains 爻/乂-like strokes on top of 巾"},
                {"character": "市", "pinyin": "shì", "meaning_en": "city; market", "distinction_note": "Dot and horizontal bar over 巾 instead of 𠂇"}
            ],
            "etymological_cognates": [
                {"character": "散发", "pinyin": "sànfā", "gloss_en": "distribute; emit"},
                {"character": "分散", "pinyin": "fēnsàn", "gloss_en": "disperse; scatter"},
                {"character": "公布", "pinyin": "gōngbù", "gloss_en": "promulgate; announce"},
                {"character": "分布", "pinyin": "fēnbù", "gloss_en": "distribute; spread over"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "散布 carries a negative or covert connotation when applied to rumors, panic, or false stories.",
            "contrasts": [
                {"id": 1, "compared_word": "散布 vs. 传播", "pinyin": "chuánbō", "analysis": "传播 is a neutral or positive term for spreading knowledge or culture, while 散布 often targets rumors or toxic ideas."},
                {"id": 2, "compared_word": "散布 vs. 辟谣", "pinyin": "pìyáo", "analysis": "辟谣 is the direct antonym meaning to debunk and refute false rumors."},
                {"id": 3, "compared_word": "散布 vs. 搜集", "pinyin": "sōují", "analysis": "搜集 means gathering and collecting materials in one place, opposite to scattering outward 散布."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "秦国名臣范雎深知正面强攻赵国壁垒难以奏效，便以千金巨资派细作潜入赵国都城邯郸，秘密散布流言，称“秦国独畏赵奢之子赵括为将，廉颇老矣不堪一击”。赵王听信了这番散布的谣言，果然中计换将。",
                "pinyin": "Qínguó míngchén Fàn Jū shēnzhī zhèngmiàn qiánggōng Zhàoguó bìlěi nányǐ zòuxiào, biàn yǐ qiānjīn jùzī pài xìzuò qiánrù Zhàoguó dūchéng Hándān, mìmì sànbù liúyán, chēng 'Qínguó dú wèi Zhào Shē zhī zǐ Zhào Kuò wéi jiàng, Lián Pō lǎo yǐ bùkān-yījī'. Zhàowáng tīngxìn le zhè fān sànbù de yáoyán, guǒrán zhòngjì huànjiàng.",
                "en": "Knowing storming Zhao's bastions would fail, Qin's minister Fan Ju sent spies into Handan with bribes to spread rumors: 'Qin fears only Zhao Kuo; Lian Po is old and weak.' Duped by the rumors, King Zhao replaced his general.",
                "es": "Sabiendo que asaltar las murallas de Zhao costaría caro, Fan Ju infiltró espías en Handan para difundir bulos: 'Qin solo teme a Zhao Kuo; Lian Po está viejo y acabado.' Engañado por los rumores, el rey de Zhao relevó al general."
            },
            {
                "id": "#2",
                "hanzi": "在当今信息爆炸的网络时代，虚假信息与恶意谣言的散布速度之快、影响之广前所未有。广大公众应当提高自身的信息鉴别能力，不盲从、不偏信，做到“谣言止于智者”，共同维护清朗健康的网络舆论生态环境。",
                "pinyin": "Zài dāngjīn xìnxī-bàozhà de wǎngluò shídài, xūjiǎ xìnxī yǔ èyì yáoyán de sànbù sùdù zhī kuài, yǐngxiǎng zhī guǎng qiánsuǒwèiyǒu. Guǎngdà gōngzhòng yīngdāng tígāo zìshēn de xìnxī jiànbié nénglì, bù mángcóng, bù piānxìn, zuòdào 'yáoyán zhǐ yú zhìzhě', gòngtóng wéihù qīnglǎng jiànkāng de wǎngluò yúlùn shēngtài huánjìng.",
                "en": "In today's digital era, false information and malicious rumors spread at unprecedented speeds. The public must sharpen critical thinking to avoid gullibility; as the proverb goes, 'rumors stop with the wise,' safeguarding a healthy cyberspace.",
                "es": "En la era digital, la difusión de bulos y noticias falsas se propaga con rapidez insólita. La ciudadanía debe aguzar su juicio crítico para no caer en patrañas; como reza el refrán, 'el rumor cesa ante el sabio', protegiendo el entorno público."
            }
        ]
    },

    # 24 谣言
    {
        "id": "24",
        "hanzi": "谣言",
        "pinyin": "yáo yán",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "rumor; unfounded story; gossip; falsehood",
            "es": "rumor; bulo; patraña; falsedad infundada"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a fabricated, unverified, or groundless statement or report circulating among people without factual basis",
                "definition_es": "noticia falsa, invención o testimonio carente de base real que se propaga entre el público",
                "example_phrase": "制造谣言 (fabricate rumors)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵王缺乏政治鉴别力，轻信了秦国散布的虚假谣言，错误地罢免了前线坚守的老将廉颇。",
                "pinyin": "Zhàowáng quēfá zhèngzhì jiànbiélì, qīngxìn le Qínguó sànbù de xūjiǎ yáoyán, cuòwù de bàmǐan le qiánxiàn jiānshǒu de lǎojiàng Lián Pō.",
                "en": "Lacking political discernment, King Zhao gullibly believed the false rumors spread by Qin, mistakenly dismissing General Lian Po from the front.",
                "es": "Carente de lucidez política, el rey de Zhao creyó los falsos bulos difundidos por Qin y destituyó erróneamente al veterano Lian Po del frente."
            },
            {
                "id": "#2",
                "hanzi": "公安网监部门及时发布权威通报澄清事实，迅速平息了在社交网络上引发恐慌的网络谣言。",
                "pinyin": "Gōng'ān wǎngjiān bùmén jíshí fābù quánwēi tōngbào chéngqīng shìshí, xùnsù píngxī le zài shèjiāo wǎngluò shang yǐnfā kǒnghuāng de wǎngluò yáoyán.",
                "en": "Cyber police promptly issued an authoritative bulletin clarifying the facts, swiftly quelling online rumors that had triggered public panic.",
                "es": "La policía cibernética emitió una nota oficial aclarando los hechos y disipando el pánico causado por bulos en redes sociales."
            }
        ],
        "collocations": [
            {"hanzi": "制造谣言", "en": "fabricate / concoct rumors"},
            {"hanzi": "散布谣言", "en": "spread rumors"},
            {"hanzi": "谣言止于智者", "en": "rumors stop with the wise"},
            {"hanzi": "辟谣澄清", "en": "refute rumors and clarify"},
            {"hanzi": "网络谣言", "en": "internet rumors / disinformation"},
            {"hanzi": "恶毒谣言", "en": "malicious / venomous rumors"}
        ],
        "idioms": [
            {"hanzi": "造谣生事", "pinyin": "zào yáo shēng shì", "meaning_en": "concoct rumors to stir up trouble"},
            {"hanzi": "满城风雨", "pinyin": "mǎn chéng fēng yǔ", "meaning_en": "the whole town is rife with gossip and talk"},
            {"hanzi": "三人成虎", "pinyin": "sān rén chéng hǔ", "meaning_en": "three people repeating a lie make a tiger; falsehood repeated sounds true"},
            {"hanzi": "杯弓蛇影", "pinyin": "bēi gōng shé yǐng", "meaning_en": "mistake the reflection of a bow for a snake; illusory panic"}
        ],
        "character_decomposition": [
            {
                "character": "谣",
                "pinyin": "yáo",
                "meaning_en": "ballad; folk rhyme; rumor; fabricate",
                "meaning_es": "balada; copla popular; rumor; bulo",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken speech) + 䍃 (earthenware jar / floating ballad)",
                "sound_component": "䍃 (yáo)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken street verses 讠 sung without instrumental accompaniment like jars 䍃; evolved into circulating hearsay.",
                "visual_mnemonic_story_en": "Words of speech (讠) drifting through streets like singing ballads, mutating into unverified hearsay (谣).",
                "visual_mnemonic_story_es": "Palabras orales (讠) que vuelan por las calles como coplas anónimas mutando en habladurías (谣).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IVBOU",
                "traditional": "謠"
            },
            {
                "character": "言",
                "pinyin": "yán",
                "meaning_en": "words; speech; talk; say",
                "meaning_es": "palabra; lenguaje; hablar; discurso",
                "radical": "言",
                "radical_meaning_en": "speech",
                "meaning_component": "tongue emitting breath strokes 口 from mouth",
                "sound_component": "言 (yán)",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of sound strokes radiating upward from an open human mouth 口; signifies speech.",
                "visual_mnemonic_story_en": "Articulate sound waves radiating upward from an open mouth (口) as spoken words (言).",
                "visual_mnemonic_story_es": "Ondas sonoras que brotan de la boca abierta (口) articulando palabras humanas (言).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YMR",
                "traditional": "言"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Fabricated street ballads (谣) uttered as spoken words (言) constitute unfounded rumors (谣言).",
            "composite_memory_hook_es": "Coplas anónimas de callejuela (谣) formuladas en lenguaje hablado (言) conforman el bulo o rumor (谣言).",
            "cultural_and_cognitive_roots": "Derived from classical street ballads (童谣) that carried political prophecies or weaponized counter-intelligence.",
            "tone_sandhi_and_pitch_modulation": "Double second tone: 'yáo yán' (35-35). Rise cleanly on both syllables with steady cadence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "摇", "pinyin": "yáo", "meaning_en": "shake; rock", "distinction_note": "Hand radical 扌 on left instead of 讠"},
                {"character": "遥", "pinyin": "yáo", "meaning_en": "distant; remote", "distinction_note": "Movement 辶 around 䍃 instead of 讠"},
                {"character": "信", "pinyin": "xìn", "meaning_en": "letter; believe", "distinction_note": "Person 亻 on left of 言"},
                {"character": "誓", "pinyin": "shì", "meaning_en": "swear; vow", "distinction_note": "Fold 折 on top of 言"}
            ],
            "etymological_cognates": [
                {"character": "歌谣", "pinyin": "gēyáo", "gloss_en": "ballad; folk song"},
                {"character": "民谣", "pinyin": "mínyáo", "gloss_en": "folk ballad"},
                {"character": "言语", "pinyin": "yányǔ", "gloss_en": "speech; spoken words"},
                {"character": "言论", "pinyin": "yánlùn", "gloss_en": "discourse; speech"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "谣言 specifically designates unfounded, fabricated, and maliciously circulated falsehoods.",
            "contrasts": [
                {"id": 1, "compared_word": "谣言 vs. 真相", "pinyin": "zhēnxiàng", "analysis": "真相 is the direct antonym meaning objective facts and verified truth."},
                {"id": 2, "compared_word": "谣言 vs. 谎言", "pinyin": "huǎngyán", "analysis": "谎言 is a deliberate lie told by an individual, while 谣言 is an unverified story circulating across an entire community."},
                {"id": 3, "compared_word": "谣言 vs. 传言", "pinyin": "chuányán", "analysis": "传言 is a neutral term for circulating hearsay, whereas 谣言 strongly implies malicious fabrication."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "“三人成虎，积羽沉舟。”春秋战国时期的谋士们最擅长利用谣言实施心理战。秦国仅用数千金在邯郸散布谣言，便让多疑的赵王自毁长城，换下身经百战的廉颇。这表明心智不坚者面对谣言极易丧失理智判断。",
                "pinyin": "'Sān rén chéng hǔ, jī yǔ chén zhōu.' Chūnqiū-Zhànguó shíqī de móushì men zuì shàncháng lìyòng yáoyán shíshī xīnlǐzhàn. Qínguó jǐn yòng shù qiān jīn zài Hándān sànbù yáoyán, biàn ràng duōyí de Zhàowáng zìhuǐ-chángchéng, huàn xià shēnjīng-bǎizhàn de Lián Pō. Zhè biǎomíng xīnji bù jiān zhě miànduì yáoyán jí yì sàngshī lǐzhì pànduàn.",
                "en": "'Three men make a tiger; piled feathers sink a ship.' Sages excelled at weaponizing rumors in psychological warfare. A few thousand pieces of gold spreading rumors in Handan tricked King Zhao into firing Lian Po, destroying his realm.",
                "es": "'Tres voces inventan un tigre; plumas amontonadas hunden un bajel.' Los estrategas antiguos dominaban la guerra psicológica con bulos. Con poco oro esparcido en Handan, Qin empujó al monarca de Zhao a relevar al curtido Lian Po."
            },
            {
                "id": "#2",
                "hanzi": "古人云：“谣言止于智者。”在信息传播极为迅捷的今天，面对网络上真伪难辨的各种传言，保持清醒的理性头脑尤为珍贵。不信谣、不传谣，主动探寻权威证据，才是每一个具有独立思考能力的公民应当具备的素养。",
                "pinyin": "Gǔrén yún: 'Yáoyán zhǐ yú zhìzhě.' Zài xìnxī chuánbō jíwéi xùnjié de jīntiān, miànduì wǎngluò shang zhēnwěi-nánbiàn de gè zhǒng chuányán, bǎochí qīngxǐng de lǐxìng tóunǎo yóuwéi zhēnguì. Bù xìnyáo, bù chuányáo, zhǔdòng tànxún quánwēi zhèngjù, cái shì měi yī gè jùyǒu dúlì sīkǎo nénglì de gōngmín yīngdāng jùbèi de sùyǎng.",
                "en": "As ancients said: 'Rumors stop with the wise.' Today, facing hard-to-verify gossip on networks, maintaining a cool, rational mind is precious. Refusing to believe or spread rumors and seeking authority reflects critical citizenship.",
                "es": "Como sentenciaron los clásicos: 'El rumor cesa ante el sabio.' En la sociedad digital, preservar la cabeza fría ante noticias confusas es virtud suprema. Rechazar bulos y buscar fuentes fidedignas es el sello del ciudadano libre."
            }
        ]
    },

    # 25 上当
    {
        "id": "25",
        "hanzi": "上当",
        "pinyin": "shàng dàng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to be fooled; be taken in; fall into a trap; be duped",
            "es": "dejarse engañar; caer en la trampa; ser estafado; ser burlado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to be deceived, tricked, or taken in by deceptive words, fraudulent schemes, or ambushes",
                "definition_es": "ser víctima de engaño, trampa o fraude; dejarse embaucar por argucias",
                "example_phrase": "上当受骗 (be fooled and swindled)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵王轻信了秦国间谍散布的谣言，果然中计上当，执意派缺乏实战经验的赵括前去替换廉颇。",
                "pinyin": "Zhàowáng qīngxìn le Qínguó jiàndié sànbù de yáoyán, guǒrán zhòngjì shàngdàng, zhíyì pài quēfá shízhàn jīngyàn de Zhào Kuò qiánqù tìhuàn Lián Pō.",
                "en": "King Zhao believed rumors spread by Qin spies and was taken in by the trap, sending inexperienced Zhao Kuo to replace Lian Po.",
                "es": "El rey de Zhao creyó los infundios de los espías de Qin y cayó en la trampa, relevando a Lian Po por el inexperto Zhao Kuo."
            },
            {
                "id": "#2",
                "hanzi": "社区民警深入居民小区开展反诈宣传，提醒老年人提高警惕，切莫轻信高额回报而上当受骗。",
                "pinyin": "Shèqū mínjǐng shēnrù jūmín xiǎoqū kāizhǎn fǎnzà xuānchuán, tíxǐng lǎoniánrén tígāo jǐngtì, qiè mò qīngxìn gāo'é huíbào ér shàngdàng-shòupiàn.",
                "en": "Community police conducted anti-fraud campaigns in neighborhoods, reminding seniors to stay vigilant and avoid being duped by high-yield scams.",
                "es": "La policía de barrio impartió charlas antifraude, advirtiendo a los ancianos que no caigan en timos que prometen ganancias fáciles."
            }
        ],
        "collocations": [
            {"hanzi": "上当受骗", "en": "be duped and swindled"},
            {"hanzi": "容易上当", "en": "easily taken in / gullible"},
            {"hanzi": "谨防上当", "en": "guard against being deceived"},
            {"hanzi": "绝不上当", "en": "never be fooled"},
            {"hanzi": "上了一次当", "en": "got fooled once"},
            {"hanzi": "上当的滋味", "en": "the bitter taste of being tricked"}
        ],
        "idioms": [
            {"hanzi": "受骗上当", "pinyin": "shòu piàn shàng dàng", "meaning_en": "be deceived and taken in by trickery"},
            {"hanzi": "吃一堑，长一智", "pinyin": "chī yī qiàn, zhǎng yī zhì", "meaning_en": "a fall into the pit, a gain in your wit; learn from blunders"},
            {"hanzi": "自投罗网", "pinyin": "zì tóu luó wǎng", "meaning_en": "hurl oneself into the net; walk blindly into traps"},
            {"hanzi": "引颈受戮", "pinyin": "yǐn jǐng shòu lù", "meaning_en": "stick out one's neck to receive the axe; submit passively to slaughter"}
        ],
        "character_decomposition": [
            {
                "character": "上",
                "pinyin": "shàng",
                "meaning_en": "ascend; go up; enter; on",
                "meaning_es": "subir; entrar; sobre; arriba",
                "radical": "一",
                "radical_meaning_en": "one / baseline",
                "meaning_component": "horizontal baseline 一 with an indicator stroke pointing above",
                "sound_component": "上 (shàng)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Indicator glyph showing an element standing above a baseline; here meaning stepping into a trap.",
                "visual_mnemonic_story_en": "Stepping upward (上) blindly into a snare.",
                "visual_mnemonic_story_es": "Dar un paso hacia arriba (上) cayendo inadvertidamente en el lazo.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YMY",
                "traditional": "上"
            },
            {
                "character": "当",
                "pinyin": "dàng",
                "meaning_en": "pawnshop; pawn ticket; match; fitting",
                "meaning_es": "casa de empeño; boleta; encajar; adecuado",
                "radical": "⺌",
                "radical_meaning_en": "small",
                "meaning_component": "尚/⺌ (value / worth) + 彐/田 (pawn collateral ledger)",
                "sound_component": "尚 (shàng / dàng)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Entering a pawnshop 当 to pledge property; customers often fell victim to sharp valuation swindles (上当).",
                "visual_mnemonic_story_en": "Pawning heirlooms at a pawnshop (当) only to realize one has been shortchanged.",
                "visual_mnemonic_story_es": "Empeñar un objeto en el monte de piedad (当) dándose cuenta de la tasación engañosa.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FNS",
                "traditional": "當"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Walking into (上) the sharp valuation trap of a greedy pawnshop (当) gave rise to being fooled (上当).",
            "composite_memory_hook_es": "Entrar (上) en el engaño de tasación de una casa de empeño (当) dio origen al modismo caer en la trampa (上当).",
            "cultural_and_cognitive_roots": "Originates from late imperial Beijing pawnshops ('当铺') where appraisers systematically undervalued valuables, leaving patrons swindled ('上当').",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'shàng dàng' (51-51). Pronounce both syllables with firm, emphatic downward cadence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "下", "pinyin": "xià", "meaning_en": "down; below", "distinction_note": "Indicator stroke points downward"},
                {"character": "肖", "pinyin": "xiào", "meaning_en": "resemble; small", "distinction_note": "Flesh radical 月 at bottom instead of 彐"},
                {"character": "党", "pinyin": "dǎng", "meaning_en": "party; faction", "distinction_note": "Legs radical 儿 at bottom instead of 彐"},
                {"character": "常", "pinyin": "cháng", "meaning_en": "constant; normal", "distinction_note": "Towel radical 巾 at bottom instead of 彐"}
            ],
            "etymological_cognates": [
                {"character": "当铺", "pinyin": "dàngpù", "gloss_en": "pawnshop"},
                {"character": "受骗", "pinyin": "shòupiàn", "gloss_en": "be swindled / cheated"},
                {"character": "中计", "pinyin": "zhòngjì", "gloss_en": "fall into a trap / stratagem"},
                {"character": "不上当", "pinyin": "bù shàngdàng", "gloss_en": "not fall for it"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "上当 is an informal, widely used verb describing falling prey to someone else's deceptive scheme or trap.",
            "contrasts": [
                {"id": 1, "compared_word": "上当 vs. 识破", "pinyin": "shípò", "analysis": "识破 is the direct antonym meaning to see through a trick or unmask a deception."},
                {"id": 2, "compared_word": "上当 vs. 认输", "pinyin": "rènshū", "analysis": "认输 means conceding defeat voluntarily, while 上当 means being tricked into loss."},
                {"id": 3, "compared_word": "上当 vs. 迷失", "pinyin": "míshī", "analysis": "迷失 means losing one's way physically or morally, unlike being actively conned (上当)."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "战国历史上赵王因上当而导致长平惨败的教训极其深刻。秦国运用反间计散布谣言，赵王不仅未能明察秋毫，反而屡次上当，将百战老将廉颇撤换。这一致命决策使四十万将士身首异处，警示后人兼听则明、偏信则暗。",
                "pinyin": "Zhànguó lìshǐ shang Zhàowáng yīn shàngdàng ér dǎozhì Chángpíng cǎibài de jiàoxun jíqí shēnkè. Qínguó yùnyòng fǎnjiànjì sànbù yáoyán, Zhàowáng bùjǐn wèinéng míngchá-qiūháo, fǎn'ér lǚcì shàngdàng, jiāng bǎizhàn lǎojiàng Lián Pō chèhuàn. Zhè yī zhìmìng juécè shǐ sìshí wàn jiàngshì shēnshǒu-yìchù, jǐngshì hòurén jiāntīng-zémíng, piānxìn-zè'àn.",
                "en": "King Zhao's gullibility leading to Changping disaster is a grave historical lesson. Duped by Qin's counter-espionage rumors, he fell into the trap, replacing Lian Po. Forty thousand soldiers died, warning that credulity breeds ruin.",
                "es": "La caída en la trampa del rey de Zhao en Changping fue una tragedia histórica. Embaucado por bulos de Qin, cesó a Lian Po; 400.000 soldados perecieron, alertando a la posteridad de que la credulidad ciega engendra catástrofes."
            },
            {
                "id": "#2",
                "hanzi": "“天下没有免费的午餐。”在日常经济生活与投资理财中，形形色色的诈骗陷阱层出不穷。面对各种天花乱坠的暴利诱惑，我们必须保持高度清醒的理性防线，不贪小便宜，多方核实真伪，才能避免落入骗局上当受骗。",
                "pinyin": "'Tiānxià méiyǒu miǎnfèi de wǔcān.' Zài rìcháng jīngjì shēnghuó yǔ tóuzī lǐcái zhōng, xíngxíng-sèsè de zhàpiàn xiànjǐng céngchū-bùqióng. Miànduì gè zhǒng tiānhuā-luànzhuì de bàolì yòuhuò, wǒmen bìxū bǎochí gāodù qīngxǐng de lǐxìng fángxiàn, bù tān xiǎo piányi, duōfāng héshí zhēnwěi, cái néng bìmiǎn luòrù piànjú shàngdàng-shòupiàn.",
                "en": "'There is no free lunch in this world.' In modern financial investments, scams abound. Facing temptations of overnight riches, maintaining a cool, rational defense and refusing petty greed protects us from being taken in by fraudsters.",
                "es": "'Nadie da duros a cuatro pesetas.' En las finanzas diarias menudean timos y engaños. Ante promesas de ganancias desmedidas, mantener la guardia racional y desconfiar de gangas fáciles evita caer en la trampa de los estafadores."
            }
        ]
    },

    # 26 再三
    {
        "id": "26",
        "hanzi": "再三",
        "pinyin": "zài sān",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "repeatedly; again and again; over and over",
            "es": "repetidamente; una y otra vez; reiteradamente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "doing something repeatedly, more than once or twice; over and over again with insistence",
                "definition_es": "hacer algo de forma reiterada, más de una o dos veces; insistente y repetidamente",
                "example_phrase": "再三考虑 (consider over and over again)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "名相蔺相如拖着重病之躯进宫，再三劝阻赵王切不可派纸上谈兵的赵括统领大军，但赵王执迷不悟。",
                "pinyin": "Míngxiàng Lìn Xiàngrú tuō zhe zhòngbìng zhī qū jìn gōng, zàisān quànzǔ Zhàowáng qiè bùkě pài zhǐshàng-tánbīng de Zhào Kuò tǒnglǐng dàjūn, dàn Zhàowáng zhímí-bùwù.",
                "en": "Prime Minister Lin Xiangru, despite heavy illness, entered court and repeatedly pleaded with King Zhao not to dispatch Zhao Kuo, but the king refused to listen.",
                "es": "El canciller Lin Xiangru, aun postrado por la enfermedad, acudió a palacio a disuadir una y otra vez al rey de nombrar a Zhao Kuo, mas fue en vano."
            },
            {
                "id": "#2",
                "hanzi": "在正式签署国际贸易合同之前，法务顾问对各项免责条款再三推敲，确保公司权益万无一失。",
                "pinyin": "Zài zhèngshì qiānshǔ guójì màoyì hétong zhīqián, fǎwù gùwèn duì gè xiàng miǎnzé tiáokuǎn zàisān tuīqiāo, quèbǎo gōngsī quányì wànwúyīshī.",
                "en": "Before formally signing the international trade contract, legal counsel weighed every disclaimer clause over and over to ensure the company's rights.",
                "es": "Antes de suscribir el contrato mercantil, los asesores jurídicos sopesaron reiteradamente cada cláusula de exención para salvaguardar la empresa."
            }
        ],
        "collocations": [
            {"hanzi": "再三考虑", "en": "consider over and over again"},
            {"hanzi": "再三叮嘱", "en": "exhort / urge repeatedly"},
            {"hanzi": "再三推辞", "en": "decline repeatedly"},
            {"hanzi": "再三强调", "en": "stress / emphasize again and again"},
            {"hanzi": "再三挽留", "en": "urge to stay over and over"},
            {"hanzi": "再三申明", "en": "reiterate repeatedly"}
        ],
        "idioms": [
            {"hanzi": "三思而后行", "pinyin": "sān sī ér hòu xíng", "meaning_en": "think thrice before taking action; prudent deliberation"},
            {"hanzi": "再三再四", "pinyin": "zài sān zài sì", "meaning_en": "repeatedly time and time again; over and over"},
            {"hanzi": "语重心长", "pinyin": "yǔ zhòng xīn cháng", "meaning_en": "sincere words and earnest wishes; well-meaning exhortation"},
            {"hanzi": "千叮万嘱", "pinyin": "qiān dīng wàn zhǔ", "meaning_en": "give repeated instructions and earnest exhortations"}
        ],
        "character_decomposition": [
            {
                "character": "再",
                "pinyin": "zài",
                "meaning_en": "again; once more; re-; repeatedly",
                "meaning_es": "otra vez; de nuevo; reiterar; además",
                "radical": "冂",
                "radical_meaning_en": "down box / upside down",
                "meaning_component": "one horizontal bar 一 crossed by another 冉; signifies doing again",
                "sound_component": "再 (zài)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideograph showing a balance scale weighing once and then balancing a second time; signifies repetition.",
                "visual_mnemonic_story_en": "Placing a second weight upon the balance scale to weigh once again (再).",
                "visual_mnemonic_story_es": "Añadir una segunda pesa sobre el platillo para contrastar la tara otra vez (再).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GMB",
                "traditional": "再"
            },
            {
                "character": "三",
                "pinyin": "sān",
                "meaning_en": "three; several; repeated",
                "meaning_es": "tres; múltiple; reiterado",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "three parallel horizontal tally strokes",
                "sound_component": "三 (sān)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Three horizontal strokes representing heaven, earth, and mankind, frequently used idiomatically for multiple times.",
                "visual_mnemonic_story_en": "Three horizontal tally bars (三) signifying repeated, multiple instances.",
                "visual_mnemonic_story_es": "Tres líneas horizontales paralelas (三) que simbolizan la reiteración múltiple.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MMM",
                "traditional": "三"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Doing something once again (再) and repeating it for three times (三) means repeatedly (再三).",
            "composite_memory_hook_es": "Hacer algo de nuevo (再) y multiplicarlo hasta tres veces (三) sintetiza la insistencia reiterada (再三).",
            "cultural_and_cognitive_roots": "In Chinese numerology, 'three' represents completeness and multiplicity; '再三' denotes exhaustive repetitive effort.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone to first tone: 'zài sān' (51-55). Drop firmly on 'zài', transitioning into a sustained high pitch on 'sān'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "在", "pinyin": "zài", "meaning_en": "at; in; exist", "distinction_note": "Soil 土 on bottom instead of 冂 and horizontal bar"},
                {"character": "冉", "pinyin": "rǎn", "meaning_en": "tender; gradual", "distinction_note": "Lacks the top horizontal cap stroke 一"},
                {"character": "二", "pinyin": "èr", "meaning_en": "two", "distinction_note": "Two horizontal strokes instead of three"},
                {"character": "丰", "pinyin": "fēng", "meaning_en": "abundant", "distinction_note": "Vertical stroke piercing three horizontal lines"}
            ],
            "etymological_cognates": [
                {"character": "再次", "pinyin": "zàicì", "gloss_en": "once again; a second time"},
                {"character": "再见", "pinyin": "zàijiàn", "gloss_en": "goodbye; see you again"},
                {"character": "屡次", "pinyin": "lǚcì", "gloss_en": "repeatedly; time and again"},
                {"character": "频繁", "pinyin": "pínfán", "gloss_en": "frequent; constantly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "再三 modifies deliberate actions (thinking, pleading, checking) performed multiple times with deep earnestness.",
            "contrasts": [
                {"id": 1, "compared_word": "再三 vs. 屡次", "pinyin": "lǚcì", "analysis": "屡次 emphasizes objective high frequency of occurrences (e.g. repeated warnings/failures), while 再三 stresses subjective earnest insistence."},
                {"id": 2, "compared_word": "再三 vs. 偶尔", "pinyin": "ǒu'ěr", "analysis": "偶尔 is the direct antonym meaning occasionally or once in a blue moon."},
                {"id": 3, "compared_word": "再三 vs. 频繁", "pinyin": "pínfán", "analysis": "频繁 indicates short intervals between rapid repetitions, while 再三 emphasizes earnest gravity."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平之战换将关头，赵国重臣蔺相如在病榻上得知消息，心急如焚。他挣扎着入宫面圣，对赵王再三进言：“赵括徒能读其父书传，不知合变也。大王因其名而用之，危亡必矣！”可惜昏庸的赵王再三拒绝忠言，终成大祸。",
                "pinyin": "Chángpíng zhī zhàn huànjiàng guāntóu, Zhàoguó zhòngchén Lìn Xiàngrú zài bìngtā shang dézhī xiāoxi, xīnjí-rúfén. Tā zhēngzhá zhe rù gōng miàn shèng, duì Zhàowáng zàisān jìnyán: 'Zhào Kuò tú néng dú qí fù shūzhuàn, bùzhī hébiàn yě. Dàwáng yīn qí míng ér yòng zhī, wēiwáng bì yǐ!' Kěxī hūnyōng de Zhàowáng zàisān jùjué zhōngyán, zhōng chéng dàhuò.",
                "en": "At the threshold of Changping, Lin Xiangru learned of the replacement on his sickbed. Staggering to court, he repeatedly warned King Zhao: 'Zhao Kuo merely recites his father's books without knowing how to adapt. Disaster is certain!' The king rejected him.",
                "es": "Al tramarse el relevo en Changping, Lin Xiangru supo la nueva en su lecho de dolor. Acudió al trono suplicando una y otra vez: '¡Zhao Kuo solo repite libros sin saber adaptarse; nombrarlo es la ruina!' El rey desoyó sus advertencias."
            },
            {
                "id": "#2",
                "hanzi": "古人讲求“三思而后行”。在做出关乎人生转折或企业前途的重大抉择时，多花时间深入调研、再三权衡利弊得失，决不是优柔寡断，而是对未来高度负责的深谋远虑。慎始敬终、再三斟酌，才能行稳致远。",
                "pinyin": "Gǔrén jiǎngqiú 'sān sī ér hòu xíng'. Zài zuòchū guānhū rénshēng zhuǎnzhé huò qǐyè qiántú de zhòngdà juézé shí, duō huā shíjiān shēnrù diàoyán, zàisān quánhéng lìbì-déshī, jué bùshì yōuróu-guǎduàn, ér shì duì wèilái gāodù fùzé de shēnmóu-yuǎnlǜ. Shènshǐ-jìngzhōng, zàisān zhēnzhuó, cái néng xíngwěn-zhìyuǎn.",
                "en": "The ancients taught to 'think thrice before acting.' When making life-turning decisions, weighing pros and cons repeatedly is not indecisiveness, but responsible prudence for the future. Deliberating over and over ensures safe passage.",
                "es": "Los antiguos aconsejaron pensar tres veces antes de obrar. Ante encrucijadas vitales, sopesar los pros y contras una y otra vez no es indecisión, sino madura cautela; meditar con calma conduce al acierto."
            }
        ]
    },

    # 27 阻止
    {
        "id": "27",
        "hanzi": "阻止",
        "pinyin": "zǔ zhǐ",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to prevent; stop; block; hinder; obstruct",
            "es": "impedir; frenar; detener; obstaculizar; atajar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to stop, obstruct, or prevent an action, person, or development from proceeding forward",
                "definition_es": "detener, obstaculizar o impedir que progrese una acción, persona o acontecimiento perjudicial",
                "example_phrase": "及时阻止事故发生 (prevent accidents promptly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括的母亲深知儿子底细，亲自面见赵王，极力阻止赵王任命毫无实战韬略的赵括为大将。",
                "pinyin": "Zhào Kuò de mǔqīn shēnzhī érzi dǐxì, qīnzì miànjiàn Zhàowáng, jílì zǔzhǐ Zhàowáng rènmìng háowú shízhàn tāolüè de Zhào Kuò wéi dàjiàng.",
                "en": "Zhao Kuo's mother knew her son's shallow depth and personally saw the king, striving mightily to prevent him from appointing Zhao Kuo as general.",
                "es": "La madre de Zhao Kuo, conocedora de la incapacidad de su hijo, acudió ante el rey para impedir con vehemencia que lo nombrara general."
            },
            {
                "id": "#2",
                "hanzi": "巡警在夜间巡逻时敏锐发现了两名可疑分子，果断采取措施，成功阻止了一起严重入室盗窃案。",
                "pinyin": "Xúnjǐng zài yèjiān xúnluó shí mǐnruì fāxiàn le liǎng míng kěyí fènzǐ, guǒduàn cǎiqǔ cuòshī, chénggōng zǔzhǐ le yī qǐ yánzhòng rùshì dàoqiè'àn.",
                "en": "During night patrol, police spotted two suspicious individuals and took decisive measures, successfully preventing a serious burglary.",
                "es": "Durante la ronda nocturna, los agentes detectaron a dos sospechosos y actuaron con rapidez, impidiendo un grave robo con allanamiento."
            }
        ],
        "collocations": [
            {"hanzi": "极力阻止", "en": "strive mightily to prevent"},
            {"hanzi": "无法阻止", "en": "impossible to stop / prevent"},
            {"hanzi": "阻止事态恶化", "en": "prevent the situation from worsening"},
            {"hanzi": "及时阻止", "en": "prevent in a timely manner"},
            {"hanzi": "设法阻止", "en": "find ways to stop"},
            {"hanzi": "阻止悲剧发生", "en": "prevent tragedy from happening"}
        ],
        "idioms": [
            {"hanzi": "防患未然", "pinyin": "fáng huàn wèi rán", "meaning_en": "prevent troubles before they happen"},
            {"hanzi": "力挽狂澜", "pinyin": "lì wǎn kuáng lán", "meaning_en": "pull back raging billows; save a desperate situation"},
            {"hanzi": "截长补短", "pinyin": "jié cháng bǔ duǎn", "meaning_en": "trim excess to make up for deficiency"},
            {"hanzi": "势不可挡", "pinyin": "shì bù kě dǎng", "meaning_en": "overwhelming momentum that cannot be stopped"}
        ],
        "character_decomposition": [
            {
                "character": "阻",
                "pinyin": "zǔ",
                "meaning_en": "block; impede; hinder; obstacle",
                "meaning_es": "bloquear; impedir; obstáculo; traba",
                "radical": "阝",
                "radical_meaning_en": "mound / hill",
                "meaning_component": "阝 (steep earthen cliff) + 且 (standing ancestral stone marker)",
                "sound_component": "且 (qiě / zǔ)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A steep earthen cliff 阝 blocking the road ahead like an immovable stone slab 且; signifies obstruction.",
                "visual_mnemonic_story_en": "A towering rocky precipice (阝) barring travelers' passage like an immovable stone wall (阻).",
                "visual_mnemonic_story_es": "Un risco escarpado (阝) que corta el camino al viajero como un muro de piedra infranqueable (阻).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "NLBM",
                "traditional": "阻"
            },
            {
                "character": "止",
                "pinyin": "zhǐ",
                "meaning_en": "stop; halt; cease; only",
                "meaning_es": "parar; detener; cesar; límite; solo",
                "radical": "止",
                "radical_meaning_en": "stop / foot",
                "meaning_component": "pictograph of human footprint planted firmly on earth",
                "sound_component": "止 (zhǐ)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictograph of a human foot resting stationary upon the ground; to stop moving.",
                "visual_mnemonic_story_en": "Planting a firm foot (止) on the ground to halt forward motion.",
                "visual_mnemonic_story_es": "Plantar el pie con firmeza en el suelo (止) para detener la marcha en seco.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "YLM",
                "traditional": "止"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Placing a steep barrier obstacle (阻) that forces forward footsteps to halt (止) means to prevent or stop (阻止).",
            "composite_memory_hook_es": "Alzar una barrera escarpada (阻) que clava los pies al suelo (止) conforma el acto de impedir (阻止).",
            "cultural_and_cognitive_roots": "Derived from ancient tactical gate defense where spiked barricades were erected across mountain passes to halt enemy cavalry.",
            "tone_sandhi_and_pitch_modulation": "Third tone sandhi chain: 'zǔ zhǐ' -> pronounced 'zú zhǐ' (35-214). The first syllable shifts smoothly to second tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "组", "pinyin": "zǔ", "meaning_en": "group; organize", "distinction_note": "Silk radical 纟 on left instead of 阝"},
                {"character": "租", "pinyin": "zū", "meaning_en": "rent; lease", "distinction_note": "Grain radical 禾 on left instead of 阝"},
                {"character": "正", "pinyin": "zhèng", "meaning_en": "straight; correct", "distinction_note": "Has a top horizontal stroke 一 over 止"},
                {"character": "步", "pinyin": "bù", "meaning_en": "step; stride", "distinction_note": "Contains lower foot 少 below 止"}
            ],
            "etymological_cognates": [
                {"character": "阻拦", "pinyin": "zǔlán", "gloss_en": "block; hold back"},
                {"character": "障碍", "pinyin": "zhàng'ài", "gloss_en": "obstacle; hindrance"},
                {"character": "制止", "pinyin": "zhìzhǐ", "gloss_en": "curb; put an end to"},
                {"character": "停止", "pinyin": "tíngzhǐ", "gloss_en": "cease; come to a halt"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "阻止 emphasizes proactive intervention to abort an ongoing or impending harmful action.",
            "contrasts": [
                {"id": 1, "compared_word": "阻止 vs. 促进", "pinyin": "cùjìn", "analysis": "促进 is the direct antonym meaning to advance, promote, and accelerate forward."},
                {"id": 2, "compared_word": "阻止 vs. 阻碍", "pinyin": "zǔ'ài", "analysis": "阻碍 means creating friction or slow progress, while 阻止 means halting the event altogether."},
                {"id": 3, "compared_word": "阻止 vs. 纵容", "pinyin": "zòngróng", "analysis": "纵容 is the antonym meaning to indulge or turn a blind eye to harmful misdeeds."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在赵国面临换将危机的关头，不仅蔺相如拼死苦谏，赵括的母亲更是亲自上书赵王，直言儿子与丈夫截然不同，极力阻止这一致命任命。然而赵王利令智昏，完全听不进任何劝谏，最终导致四十万赵军魂断长平。",
                "pinyin": "Zài Zhàoguó miànlín huànjiàng wēijī de guāntóu, bùjǐn Lìn Xiàngrú pīnsǐ kǔjiàn, Zhào Kuò de mǔqīn gèng shì qīnzì shàngshū Zhàowáng, zhíyán érzi yǔ zhàngfu jiérán-bùtóng, jílì zǔzhǐ zhè yī zhìmìng rènmìng. Rán'ér Zhàowáng lìlìngzhìhūn, wánquán tīng bù jìn rènhé quànjiàn, zuìzhōng dǎozhì sìshí wàn Zhàojūn hún duàn Chángpíng.",
                "en": "At the crisis of command, not only did Lin Xiangru plead, but Zhao Kuo's mother petitioned the king, stating her son was nothing like her late husband and striving to stop the appointment. Blinded, the king refused, sealing the tragedy.",
                "es": "Ante el relevo en el mando, Lin Xiangru y la madre de Zhao Kuo rogaron al monarca, señalando que el hijo no se parecía en nada al padre e intentando atajar el nombramiento. El soberbio rey desoyó el ruego, consumando la hecatombe."
            },
            {
                "id": "#2",
                "hanzi": "在现代法治社会中，任何违法犯罪行为都必须受到法律的严正阻止与制裁。公安干警与各界群众紧密协作，不仅要依法惩处已经发生的犯罪，更要通过精密监控与社区调解，防微杜渐，将各类潜在危害隐患及时阻止在萌芽状态。",
                "pinyin": "Zài xiàndài fǎzhì shèhuì zhōng, rènhé wéifǎ-fànzuì xíngwéi dōu bìxū shòudào fǎlǜ de yánzhèng zǔzhǐ yǔ zhìcái. Gōng'ān gànjǐng yǔ gèjiè qúnzhòng jǐnmì xiézuò, bùjǐn yào yīfǎ chéngchǔ yǐjīng fāshēng de fànzuì, gèng yào tōngguò jīngmì jiānkòng yǔ shèqū tiáojiě, fángwēi-dùjiàn, jiāng gèlèi qiánzài wēihài yǐnhuàn jíshí zǔzhǐ zài méngyá zhuàngtài.",
                "en": "In modern societies under the rule of law, crimes must be sternly halted by law. Through surveillance and community mediation, police and citizens work together to stop latent hazards in their nascent stages before harm occurs.",
                "es": "En un Estado de derecho, la delincuencia debe ser frenada y sancionada con rigor. La policía y la ciudadanía cooperan para disuadir delitos y atajar peligros en su raíz antes de que causen daños irreparables."
            }
        ]
    },

    # 28 任命
    {
        "id": "28",
        "hanzi": "任命",
        "pinyin": "rèn mìng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to appoint; nominate; commission; designation",
            "es": "nombrar; designar; conferir cargo; nombramiento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to officially assign someone to a position of leadership, government post, or military command",
                "definition_es": "designar o conferir formalmente a una persona un cargo oficial de gobierno, mando militar o jefatura",
                "example_phrase": "正式任命为院长 (formally appointed as dean)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "昏庸自大的赵王不顾重臣与赵母的极力反对，执意正式任命毫无实战经验的赵括统领长平大军。",
                "pinyin": "Hūnyōng-zìdà de Zhàowáng bùgù zhòngchén yǔ Zhàomǔ de jílì fǎnduì, zhíyì zhèngshì rènmìng háowú shízhàn jīngyàn de Zhào Kuò tǒnglǐng Chángpíng dàjūn.",
                "en": "The arrogant King Zhao disregarded ministers' and Zhao Kuo's mother's fierce objections, insisting on appointing inexperienced Zhao Kuo to command.",
                "es": "El soberbio rey de Zhao, desoyendo al consejo y a la propia madre de Zhao Kuo, nombró formalmente a este al frente del ejército en Changping."
            },
            {
                "id": "#2",
                "hanzi": "经联合国教科文组织理事会审议表决，张教授被正式任命为新一届国际文化遗产保护委员会主席。",
                "pinyin": "Jīng Liánhéguó Jiàokēwén Zǔzhī lǐshìhuì shěnyì biàojué, Zhāng jiàoshòu bèi zhèngshì rènmìng wéi xīn yī jiè guójì wénhuà yíchǎn bǎohù wěiyuánhuì zhǔxí.",
                "en": "Following deliberation by the UNESCO council, Professor Zhang was formally appointed as president of the World Heritage Protection Committee.",
                "es": "Tras la votación del consejo de la UNESCO, el profesor Zhang fue nombrado presidente del Comité de Protección del Patrimonio Mundial."
            }
        ],
        "collocations": [
            {"hanzi": "正式任命", "en": "formally appoint / nominate"},
            {"hanzi": "任命为代表", "en": "appointed as representative"},
            {"hanzi": "接受任命", "en": "accept the appointment"},
            {"hanzi": "任命书", "en": "letter / certificate of appointment"},
            {"hanzi": "撤销任命", "en": "rescind / revoke an appointment"},
            {"hanzi": "行政任命", "en": "administrative appointment"}
        ],
        "idioms": [
            {"hanzi": "任人唯贤", "pinyin": "rèn rén wéi xián", "meaning_en": "appoint people according to their political integrity and competence"},
            {"hanzi": "任人唯亲", "pinyin": "rèn rén wéi qīn", "meaning_en": "appoint people by favoritism and nepotism (antonym)"},
            {"hanzi": "知人善任", "pinyin": "zhī rén shàn rèn", "meaning_en": "know people well and assign them to posts suited to abilities"},
            {"hanzi": "委以重任", "pinyin": "wěi yǐ zhòng rèn", "meaning_en": "entrust someone with heavy responsibilities"}
        ],
        "character_decomposition": [
            {
                "character": "任",
                "pinyin": "rèn",
                "meaning_en": "appoint; task; duty; office; assume",
                "meaning_es": "nombrar; cargo; deber; encomendar; asumir",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person standing) + 壬 (loom carrier holding heavy warp threads)",
                "sound_component": "壬 (rén)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 shouldering a heavy burden on a carrying pole 壬; signifies bearing official responsibility.",
                "visual_mnemonic_story_en": "A capable person (亻) shouldering a heavy burden on a balance pole (壬) with steady duty (任).",
                "visual_mnemonic_story_es": "Una persona íntegra (亻) cargando sobre los hombros una balanza de peso (壬) con entereza (任).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OHG",
                "traditional": "任"
            },
            {
                "character": "命",
                "pinyin": "mìng",
                "meaning_en": "command; decree; mandate; life",
                "meaning_es": "orden; mandato; decreto; vida",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (authoritative mouth decree) + 令 (binding command)",
                "sound_component": "令 (lìng)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A mouth 口 delivering a binding state command 令 to commission an officer.",
                "visual_mnemonic_story_en": "A sovereign's mouth (口) pronouncing a royal mandate (令) conferring public rank (命).",
                "visual_mnemonic_story_es": "La boca del monarca (口) proclamando el mandato regio (令) que confiere dignidad (命).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "ROMB",
                "traditional": "命"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Bestowing a public duty burden (任) through an official sovereign mandate (命) is to appoint (任命).",
            "composite_memory_hook_es": "Encomendar una responsabilidad pública (任) mediante mandato oficial (命) constituye el nombramiento (任命).",
            "cultural_and_cognitive_roots": "Derived from ancient investiture ceremonies where emperors conferred bronze seals and tallies to magistrates upon appointment.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'rèn mìng' (51-51). Articulate both syllables with decisive authoritative weight."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "住", "pinyin": "zhù", "meaning_en": "live; reside", "distinction_note": "Master 主 on right of 亻 instead of 壬"},
                {"character": "仕", "pinyin": "shì", "meaning_en": "official; serve", "distinction_note": "Scholar 士 on right of 亻 instead of 壬"},
                {"character": "伞", "pinyin": "sǎn", "meaning_en": "umbrella", "distinction_note": "Has multiple horizontal lines under 人"},
                {"character": "令", "pinyin": "lìng", "meaning_en": "order; season", "distinction_note": "Lacks the mouth 口 component at the bottom"}
            ],
            "etymological_cognates": [
                {"character": "责任", "pinyin": "zérèn", "gloss_en": "responsibility; duty"},
                {"character": "任期", "pinyin": "rènqī", "gloss_en": "term of office"},
                {"character": "使命", "pinyin": "shǐmìng", "gloss_en": "mission; calling"},
                {"character": "聘任", "pinyin": "pìnrèn", "gloss_en": "hire; appoint by contract"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "任命 specifically denotes the top-down official conferral of leadership authority or public office.",
            "contrasts": [
                {"id": 1, "compared_word": "任命 vs. 免职", "pinyin": "miǎnzhí", "analysis": "免职 is the direct antonym meaning to relieve someone of their official duties or remove them from office."},
                {"id": 2, "compared_word": "任命 vs. 选举", "pinyin": "xuǎnjǔ", "analysis": "选举 is bottom-up democratic voting by a constituency, whereas 任命 is top-down designation by superiors."},
                {"id": 3, "compared_word": "任命 vs. 聘请", "pinyin": "pìnqǐng", "analysis": "聘请 implies hiring professional consultants or professors on contractual terms, while 任命 carries administrative sovereign power."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代选贤任能讲究“知人善任”。长平之战前夕，赵王未能辨明虚实，在关乎国家生死存亡的决战时刻，错误地任命只擅长空谈兵法的赵括取代廉颇。这一轻率的任命打破了战略平衡，最终成为导致赵国亡国的转折点。",
                "pinyin": "Zhōngguó gǔdài xuǎnxián-rènnéng jiǎngjiu 'zhīrén-shànrèn'. Chángpíng zhī zhàn qiánxī, Zhàowáng wèinéng biànmíng xūshí, zài guānhū guójiā shēngsǐ-cúnwáng de juézhàn shíkè, cuòwù de rènmìng zhǐ shàncháng kōngtán bīngfǎ de Zhào Kuò qǔdài Lián Pō. Zhè yī qīngshuài de rènmìng dǎpò le zhànlüè pínghéng, zuìzhōng chéngwéi dǎozhì Zhàoguó wángguó de zhuǎnzhédiǎn.",
                "en": "Ancient statecraft emphasized appointing people suited to their talents. Before Changping, King Zhao failed to discern true capability, appointing Zhao Kuo to replace Lian Po. This reckless appointment tipped the balance, marking the collapse of Zhao.",
                "es": "La gobernanza clásica valoraba el nombramiento de los hombres según su talento. Antes de Changping, el rey de Zhao erró nombrando al bisoño Zhao Kuo en vez de a Lian Po. Aquel nombramiento temerario rompió el equilibrio y precipitó la ruina del reino."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业治理与组织管理中，核心管理层的任命直接关乎整个机构的战略航向与运营成效。唯有坚持“任人唯贤、德才兼备”的考核标准，把真正具备实战经验与卓越领导力的骨干任命到关键岗位，组织才能在激烈的市场竞争中乘风破浪。",
                "pinyin": "Zài xiàndài qǐyè zhìlǐ yǔ zǔzhī guǎnlǐ zhōng, héxīn guǎnlǐcéng de rènmìng zhíjiē guānhū zhěnggè jīgòu de zhànlüè hángxiàng yǔ yùnyíng chéngxiào. Wéiyǒu jiānchí 'rènrén-wéixián, décái-jiānbèi' de kǎohé biāozhǔn, bǎ zhēnzhèng jùbèi shízhàn jīngyàn yǔ zhuóyuè lǐngdǎolì de gǔgàn rènmìng dào guānjiàn gǎngwèi, zǔzhī cái néng zài jīliè de shìchǎng jìngzhēng zhōng chéngfēng-pòlàng.",
                "en": "In corporate governance, appointing executive leadership directly decides strategic direction and efficiency. Only by adhering to meritocratic standards—appointing talents of proven integrity and tested capability—can an enterprise conquer market tides.",
                "es": "En la gestión corporativa moderna, nombrar a los directivos decide el rumbo estratégico. Guiándose por el mérito y la solvencia ética para designar a los cuadros más aptos, las empresas logran triunfar en mercados competitivos."
            }
        ]
    },

    # 29 独立
    {
        "id": "29",
        "hanzi": "独立",
        "pinyin": "dú lì",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "independent; stand alone; self-reliant; sovereignty",
            "es": "independiente; autónomo; erguirse en solitario; soberanía"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "free from outside control or reliance; able to act, think, or stand alone without depending on others",
                "definition_es": "libre de dependencia o tutela ajena; capaz de obrar, pensar o sostenerse por sí mismo",
                "example_phrase": "独立思考 (think independently)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括自幼缺乏独立带兵作战的经验，一旦真正面临数十万大军的生死决战，便显得束手无策。",
                "pinyin": "Zhào Kuò zìyòu quēfá dúlì dài bīng zuòzhàn de jīngyàn, yīdàn zhēnzhèng miànlín shùshí wàn dàjūn de shēngsǐ juézhàn, biàn xiǎnde shùshǒu-wúcè.",
                "en": "Zhao Kuo had lacked independent experience in leading troops; when suddenly faced with a life-and-death campaign of thousands, he proved helpless.",
                "es": "Zhao Kuo carecía de experiencia de mando autónomo; al encarar una batalla de cientos de miles de hombres, se halló atado de pies y manos."
            },
            {
                "id": "#2",
                "hanzi": "青年人在成长过程中不仅要在经济上逐步自立，更应当在学术和思想上培养独立思考的能力。",
                "pinyin": "Qīngniánrén zài chéngzhǎng guòchéng zhōng bùjǐn yào zài jīngjì shang zhúbù zìlì, gèng yīngdāng zài xuéshù hé sīxiǎng shang péiyǎng dúlì sīkǎo de nénglì.",
                "en": "In growing up, youth must not only achieve economic self-reliance, but also cultivate the capability for independent thought in academics and ideas.",
                "es": "En su maduración, los jóvenes no solo deben alcanzar la solvencia material, sino cultivar el juicio crítico y el pensamiento autónomo."
            }
        ],
        "collocations": [
            {"hanzi": "独立思考", "en": "think independently"},
            {"hanzi": "国家独立", "en": "national independence"},
            {"hanzi": "独立自主", "en": "independent and self-reliant"},
            {"hanzi": "独立作战", "en": "fight independently"},
            {"hanzi": "经济独立", "en": "financial independence"},
            {"hanzi": "独立人格", "en": "independent personality / integrity"}
        ],
        "idioms": [
            {"hanzi": "特立独行", "pinyin": "tè lì dú xíng", "meaning_en": "act independently and stay true to principles despite crowds"},
            {"hanzi": "自立更生", "pinyin": "zì lì gēng shēng", "meaning_en": "regenerate through one's own efforts; self-reliance"},
            {"hanzi": "自食其力", "pinyin": "zì shí qí lì", "meaning_en": "support oneself by one's own labor"},
            {"hanzi": "卓尔不群", "pinyin": "zhuó ěr bù qún", "meaning_en": "stand out prominently from the crowd in excellence"}
        ],
        "character_decomposition": [
            {
                "character": "独",
                "pinyin": "dú",
                "meaning_en": "alone; single; solitary; only",
                "meaning_es": "solo; único; solitario; exclusivo",
                "radical": "犭",
                "radical_meaning_en": "dog / beast",
                "meaning_component": "犭 (solitary wild beast) + 虫 (crawling insect standing alone)",
                "sound_component": "蜀 (shǔ / dú)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A wild predatory animal 犭 that hunts in solitude rather than in a herd; signifies standing alone.",
                "visual_mnemonic_story_en": "A proud solitary wolf (犭) roaming the snowfields alone without relying on the pack (独).",
                "visual_mnemonic_story_es": "Un lobo solitario (犭) que campea por el páramo con dignidad sin depender de la manada (独).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "KHLI",
                "traditional": "獨"
            },
            {
                "character": "立",
                "pinyin": "lì",
                "meaning_en": "stand; erect; establish; set up",
                "meaning_es": "erguirse; estar de pie; fundar; erigir",
                "radical": "立",
                "radical_meaning_en": "stand",
                "meaning_component": "pictograph of a person standing upright firmly on the ground 一",
                "sound_component": "立 (lì)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A human figure standing firmly upright with feet planted upon the solid earth 一.",
                "visual_mnemonic_story_en": "A human standing tall and erect on the ground with unshakable balance (立).",
                "visual_mnemonic_story_es": "Una silueta humana que se yergue con aplomo sobre el suelo firme (立).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YT",
                "traditional": "立"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Standing alone in solitude (独) firmly upright on one's own feet (立) means to be independent (独立).",
            "composite_memory_hook_es": "Hallarse solo (独) erguido sobre los propios pies con entereza (立) conforma la independencia (独立).",
            "cultural_and_cognitive_roots": "From classical ethics ('独立而不改') celebrating the noble scholar who preserves moral autonomy against peer pressure.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'dú lì' (35-51). Rise smoothly on 'dú', then drop firmly on 'lì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "触", "pinyin": "chù", "meaning_en": "touch", "distinction_note": "Horn 角 on left instead of 犭"},
                {"character": "浊", "pinyin": "zhuó", "meaning_en": "turbid; muddy", "distinction_note": "Water 氵 on left instead of 犭"},
                {"character": "位", "pinyin": "wèi", "meaning_en": "position; seat", "distinction_note": "Person 亻 on left of 立"},
                {"character": "拉", "pinyin": "lā", "meaning_en": "pull", "distinction_note": "Hand 扌 on left of 立"}
            ],
            "etymological_cognates": [
                {"character": "独自", "pinyin": "dúzì", "gloss_en": "alone; by oneself"},
                {"character": "自立", "pinyin": "zìlì", "gloss_en": "self-reliant; stand on own"},
                {"character": "成立", "pinyin": "chénglì", "gloss_en": "establish; found"},
                {"character": "孤立", "pinyin": "gūlì", "gloss_en": "isolated; helpless"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "独立 denotes self-reliant autonomy free from external control, subordination, or dependence.",
            "contrasts": [
                {"id": 1, "compared_word": "独立 vs. 依赖", "pinyin": "yīlài", "analysis": "依赖 is the direct antonym meaning to lean on, depend on, or cling to others."},
                {"id": 2, "compared_word": "独立 vs. 孤立", "pinyin": "gūlì", "analysis": "孤立 carries a negative sense of being cut off from support, while 独立 represents positive sovereign self-reliance."},
                {"id": 3, "compared_word": "独立 vs. 附属", "pinyin": "fùshǔ", "analysis": "附属 means subordinate or attached as an auxiliary annex, opposite to autonomous 独立."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "真正的军事指挥才能绝不能仅凭书本背诵获得，而必须在尸山血海的实战中磨炼出独立判断的胆略。赵括平生从未独立指挥过哪怕一次真正的大战，在长平前线一旦遭遇白起的诡谲奇袭，其缺乏独立统帅经验的弊端便暴露无遗。",
                "pinyin": "Zhēnzhèng de jūnshì zhǐhuī cáinéng juébùnéng jǐn píng shūběn bèisòng huòdé, ér bìxū zài shīshān-xuèhǎi de shízhàn zhōng móliàn chū dúlì pànduàn de dǎnlüè. Zhào Kuò píngshēng cóngwèi dúlì zhǐhuī guò nǎpà yī cì zhēnzhèng de dàzhàn, zài Chángpíng qiánxiàn yīdàn zāoyù Bái Qǐ de guǐjué qíxí, qí quēfá dúlì tǒngshuài jīngyàn de bìduān biàn bàolù-wúyí.",
                "en": "True military command can never be memorized from books; it must be forged in combat to temper independent judgment. Zhao Kuo had never independently led an army in a real campaign; facing Bai Qi's ambush, his lack of command experience doomed him.",
                "es": "La maestría bélica no se adquiere memorizando tratados; se forja en el fuego para templar el juicio autónomo. Zhao Kuo jamás había comandado en solitario una gran campaña; ante las celadas de Bai Qi, su inexperiencia quedó al desnudo."
            },
            {
                "id": "#2",
                "hanzi": "“独立之精神，自由之思想。”在学术探索与人生追求的漫长道路上，保持独立思考的能力是抵御盲从与偏见的最强盾牌。敢于坚持真理、不人云亦云，唯有具备独立人格的人，才能在时代的洪流中站稳脚跟，书写有意义的壮丽篇章。",
                "pinyin": "'Dúlì zhī jīngshén, zìyóu zhī sīxiǎng.' Zài xuéshù tànsuǒ yǔ rénshēng zhuīqiú de màncháng dàolù shang, bǎochí dúlì sīkǎo de nénglì shì dǐyù mángcóng yǔ piānjiàn de zuì qiáng dùnpái. Gǎnyú jiānchí zhēnlǐ, bù rényún-yìyún, wéiyǒu jùbèi dúlì réngé de rén, cái néng zài shídài de hóngliú zhōng zhànwěn jiǎogēn, shūxiě yǒuyìyì de zhuànglì piānzhāng.",
                "en": "'Independence of spirit, freedom of thought.' In academic pursuits, independent thinking is the shield against dogma. Daring to uphold truth without parroting crowds, those with independent character plant firm feet to write meaningful life chapters.",
                "es": "'Espíritu independiente, pensamiento libre.' En la ciencia y en la vida, el criterio autónomo es el baluarte contra el dogmatismo. Sostener la verdad sin repetir consignas ajenas permite labrarse un destino noble en la historia."
            }
        ]
    },

    # 30 资格
    {
        "id": "30",
        "hanzi": "资格",
        "pinyin": "zī gé",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "qualifications; competence; credentials; seniority",
            "es": "cualificación; titulación; competencia; credencial; méritos"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "requisite conditions, credentials, experience, or status enabling one to assume a post or enjoy rights",
                "definition_es": "requisitos, méritos, títulos o condición indispensable para ejercer un cargo o disfrutar de un derecho",
                "example_phrase": "具备任职资格 (possess the qualifications to hold office)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括虽然能熟练背诵各家兵书，但在瞬息万变的实战战场上，他根本不具备统帅数十万大军的资格。",
                "pinyin": "Zhào Kuò suīrán néng shúliàn bèisòng gè jiā bīngshū, dàn zài shùnxī-wànbiàn de shízhàn zhànchǎng shang, tā gēnběn bù jùbèi tǒnglǐng shùshí wàn dàjūn de zīgé.",
                "en": "Although Zhao Kuo could recite military books, on the fast-changing battlefield he lacked the qualifications to command hundreds of thousands of troops.",
                "es": "Aunque Zhao Kuo recitaba tratados de memoria, en la crudeza del combate real carecía por entero de las cualificaciones para mandar a un ejército."
            },
            {
                "id": "#2",
                "hanzi": "通过了全国统一的高级翻译专业资格考试，她顺利获得了联合国同声传译员的执业资格。",
                "pinyin": "Tōngguò le quánguó tǒngyī de gāojí fānyì zhuānyè zīgé kǎoshì, tā shùnlì huòdé le Liánhéguó tóngshēng chuányìyuán de zhíyè zīgé.",
                "en": "Passing the national advanced translation qualification exam, she obtained the professional credential to practice as a UN interpreter.",
                "es": "Tras aprobar el examen nacional de traducción superior, obtuvo la titulación profesional para ejercer como intérprete simultánea en la ONU."
            }
        ],
        "collocations": [
            {"hanzi": "具备资格", "en": "possess qualifications / credentials"},
            {"hanzi": "取消资格", "en": "disqualify / revoke qualifications"},
            {"hanzi": "审查资格", "en": "examine / verify qualifications"},
            {"hanzi": "获得资格", "en": "obtain qualification"},
            {"hanzi": "老资格", "en": "veteran / senior standing"},
            {"hanzi": "从业资格", "en": "professional certification / practice license"}
        ],
        "idioms": [
            {"hanzi": "名正言顺", "pinyin": "míng zhèng yán shùn", "meaning_en": "in accordance with proper title and reasons; fully justified"},
            {"hanzi": "德才兼备", "pinyin": "dé cái jiān bèi", "meaning_en": "possessing both integrity and talent; highly qualified"},
            {"hanzi": "论资排辈", "pinyin": "lùn zī pái bèi", "meaning_en": "assign ranks strictly according to seniority and tenure"},
            {"hanzi": "实至名归", "pinyin": "shí zhì míng guī", "meaning_en": "reputation deserved by actual merit"}
        ],
        "character_decomposition": [
            {
                "character": "资",
                "pinyin": "zī",
                "meaning_en": "money; wealth; resources; capital; qualification",
                "meaning_es": "dinero; bienes; recursos; capital; solvencia",
                "radical": "贝",
                "radical_meaning_en": "cowrie shell / money",
                "meaning_component": "次 (order / sequence) + 贝 (cowrie shell / wealth backing)",
                "sound_component": "次 (cì)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Accumulating sequential reserves of wealth 贝 or merit 次 over time; signifies backing capital and qualifications.",
                "visual_mnemonic_story_en": "Accumulating valuable shell currency (贝) in orderly ranks (次) to earn status (资).",
                "visual_mnemonic_story_es": "Atesorar caudales valiosos (贝) en riguroso orden (次) para respaldar la solvencia y mérito (资).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MOBO",
                "traditional": "資"
            },
            {
                "character": "格",
                "pinyin": "gé",
                "meaning_en": "grid; standard; pattern; style; examine",
                "meaning_es": "cuadrícula; norma; patrón; estilo; examinar",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden branch / measuring frame) + 各 (distinct individual items)",
                "sound_component": "各 (gè)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A wooden lattice frame 木 used to measure and sort individual items 各 according to standards; marks standards.",
                "visual_mnemonic_story_en": "Using a wooden lattice frame (木) to classify items into proper categories (格).",
                "visual_mnemonic_story_es": "Una regla de madera (木) que clasifica cada objeto en su casilla correspondiente (格).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "DHER",
                "traditional": "格"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Accumulated resource capital (资) matching the official standard grid (格) grants formal qualifications (资格).",
            "composite_memory_hook_es": "El caudal de mérito acumulado (资) que encaja en la norma reglamentaria (格) confiere la cualificación (资格).",
            "cultural_and_cognitive_roots": "Originates from imperial civil examinations where candidates' family pedigree (资) and test standards (格) were scrutinized.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'zī gé' (55-35). High level pitch on 'zī', lifting smoothly on 'gé'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "姿", "pinyin": "zī", "meaning_en": "posture; gesture", "distinction_note": "Woman 女 under 次 instead of 贝"},
                {"character": "咨", "pinyin": "zī", "meaning_en": "consult; inquire", "distinction_note": "Mouth 口 under 次 instead of 贝"},
                {"character": "洛", "pinyin": "luò", "meaning_en": "Luo River", "distinction_note": "Water 氵 on left of 各 instead of 木"},
                {"character": "阁", "pinyin": "gé", "meaning_en": "pavilion; chamber", "distinction_note": "Door 门 around 各 instead of 木"}
            ],
            "etymological_cognates": [
                {"character": "资历", "pinyin": "zīlì", "gloss_en": "qualifications and record"},
                {"character": "资本", "pinyin": "zīběn", "gloss_en": "capital; assets"},
                {"character": "合格", "pinyin": "hégé", "gloss_en": "qualified; up to standard"},
                {"character": "品格", "pinyin": "pǐngé", "gloss_en": "moral character; caliber"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "资格 refers to satisfying requisite formal, professional, or legal criteria to undertake duties or enjoy rights.",
            "contrasts": [
                {"id": 1, "compared_word": "资格 vs. 条件", "pinyin": "tiáojiàn", "analysis": "条件 refers to broad objective factors or prerequisites, while 资格 specifically denotes legal/professional status and eligibility."},
                {"id": 2, "compared_word": "资格 vs. 能力", "pinyin": "nénglì", "analysis": "能力 is actual competence in execution, whereas 资格 can merely be a formal certificate or title."},
                {"id": 3, "compared_word": "资格 vs. 资历", "pinyin": "zīlì", "analysis": "资历 measures accumulated chronological tenure/seniority, while 资格 focuses on meeting qualifying standards."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "兵家常云：“为将者，未料胜，先料败。”统领数十万军民生死存亡的大将，必须具备过人的智谋、沉稳的心态与丰富的实战资历。赵括徒有一腔纸上谈兵的空论，缺乏带兵治军的真才实学，从根本上就不具备统领长平大军的资格。",
                "pinyin": "Bīngjiā cháng yún: 'Wéi jiàng zhě, wèi liào shèng, xiān liào bài.' Tǒnglǐng shùshí wàn jūnmín shēngsǐ-cúnwáng de dàjiàng, bìxū jùbèi guòrén de zhìmóu, chénwěn de xīntài yǔ fēngfù de shízhàn zīlì. Zhào Kuò tú yǒu yī qiāng zhǐshàng-tánbīng de kōnglùn, quēfá dài bīng zhì jūn de zhēncái-shíxué, cóng gēnběn shang jiù bù jùbèi tǒnglǐng Chángpíng dàjūn de zīgé.",
                "en": "Strategists say: 'A general calculates defeat before victory.' Commanding troops demands wisdom, composure, and combat credentials. Zhao Kuo held only empty book talk without real substance; he lacked the qualifications to lead.",
                "es": "Los maestros castrenses decían: 'El general antes de prever la victoria calcula la derrota.' Comandar miles de vidas exige temple y fogueo real. Zhao Kuo solo poseía vanas teorías; carecía de cualificación para semejante mando."
            },
            {
                "id": "#2",
                "hanzi": "在现代社会中，任何专业岗位的准入都建立在严格的资质审核基础之上。从医生的执业医师资格、律师的法律从业资格，到工程师的高级技术职称，只有通过严谨规范的专业考核获取相应资格，才能切实对公众安全负责。",
                "pinyin": "Zài xiàndài shèhuì zhōng, rènhé zhuānyè gǎngwèi de zhǔnrù dōu jiànlì zài yángé de zīzhì shěnhé jīchǔ zhīshàng. Cóng yīshēng de zhíyè yīshī zīgé, lǜshī de fǎlǜ cóngyè zīgé, dào gōngchéngshī de gāojí jìshù zhíchēng, zhǐyǒu tōngguò yánjǐn guīfàn de zhuānyè kǎohé huòqǔ xiāngyìng zīgé, cái néng qièshí duì gōngzhòng ānquán fùzé.",
                "en": "In modern society, entry into professions rests on strict qualification vetting. From medical licenses and bar exams to engineering certificates, only passing rigorous professional evaluations to earn qualifications ensures public safety.",
                "es": "En la sociedad moderna, el acceso a las profesiones descansa en la acreditación de títulos. Desde la colegiación médica hasta los títulos de ingeniería, acreditar la cualificación mediante exámenes rigurosos garantiza la seguridad pública."
            }
        ]
    }
]

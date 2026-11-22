# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 甲
    {
        "id": "11",
        "hanzi": "甲",
        "pinyin": "jiǎ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "first (in series); shell; armor; Party A",
            "es": "primero; caparazón; armadura; parte A"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the first of the ten Heavenly Stems, used to denote the first person, place, or grade in a sequence",
                "definition_es": "primero de los diez Troncos Celestiales, empleado para designar el primer elemento, grado o sujeto en una serie",
                "example_phrase": "甲乙两队 (Team A and Team B)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在今天下午举行的年级篮球友谊赛中，甲队凭借默契的战术配合始终占据场上优势。",
                "pinyin": "Zài jīntiān xiàwǔ jǔxíng de niánjí lánqiú yǒuyìsài zhōng, jiǎ duì píngjiè mòqì de zhànshù pèihé shǐzhōng zhànjù chǎngshang yōushì.",
                "en": "In this afternoon's grade-level basketball friendly match, Team A consistently held the upper hand through seamless tactical chemistry.",
                "es": "En el amistoso de baloncesto escolar de esta tarde, el equipo A dominó el encuentro gracias a una impecable compenetración táctica."
            },
            {
                "id": "#2",
                "hanzi": "商业合同的开头明确规定：甲方负责提供核心技术支持，乙方负责后续的市场开拓与运维服务。",
                "pinyin": "Shāngyè hétong de kāitóu míngquè guīdìng: jiǎfāng fùzé tígōng héxīn jìshù zhīchí, yǐfāng fùzé hòuxù de shìchǎng kāituò yǔ yùnwéi fúwù.",
                "en": "The preamble of the commercial contract clearly stipulates: Party A supplies core tech support, while Party B oversees market expansion and maintenance.",
                "es": "El contrato estipula claramente al inicio: la Parte A aportará el soporte técnico central, mientras que la Parte B asumirá la comercialización y el mantenimiento."
            }
        ],
        "collocations": [
            {"hanzi": "甲方", "en": "Party A (contractor)"},
            {"hanzi": "甲等", "en": "first grade / top class"},
            {"hanzi": "指甲", "en": "fingernail"},
            {"hanzi": "盔甲", "en": "armor and helmet"},
            {"hanzi": "甲级联赛", "en": "first division league"},
            {"hanzi": "甲天下", "en": "number one in the world"}
        ],
        "idioms": [
            {"hanzi": "桂林山水甲天下", "pinyin": "Guì lín shān shuǐ jiǎ tiān xià", "meaning_en": "Guilin's scenery is supreme under heaven"},
            {"hanzi": "披山带河", "pinyin": "pī shān dài hé", "meaning_en": "clad in mountains and girt by rivers; fortified land"},
            {"hanzi": "富甲一方", "pinyin": "fù jiǎ yī fāng", "meaning_en": "wealthiest across an entire region"},
            {"hanzi": "抛砖引玉", "pinyin": "pāo zhuān yǐn yù", "meaning_en": "toss brick to attract jade; offer modest starter"}
        ],
        "character_decomposition": [
            {
                "character": "甲",
                "pinyin": "jiǎ",
                "meaning_en": "first; shell; armor",
                "meaning_es": "primero; caparazón; armadura",
                "radical": "田",
                "radical_meaning_en": "field",
                "meaning_component": "pictograph of turtle shell plate or warrior's protective cuirass",
                "sound_component": "甲 (jiǎ)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictograph of a ribbed turtle shell or wooden shield plate; later first of the Heavenly Stems.",
                "visual_mnemonic_story_en": "A turtle's hard segmented back shell (田) extending down into a strong protective plate (甲).",
                "visual_mnemonic_story_es": "El duro caparazón segmentado de un galápago (田) prolongado en una coraza protectora (甲).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "WL",
                "traditional": "甲"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A hard protective shield or turtle shell plate (甲) always ranks first in rank and resilience.",
            "composite_memory_hook_es": "Una coraza de escudo o caparazón de tortuga (甲) encabeza siempre la jerarquía como primera en rango.",
            "cultural_and_cognitive_roots": "First of the Ten Heavenly Stems (天干) used for ancient astronomical reckoning, calendars, and formal contract drafting.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'jiǎ' (214). Drop into the lower register and rebound with clarity."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "甲", "pinyin": "jiǎ", "meaning_en": "first; shell", "distinction_note": "Vertical stroke extends downward from bottom"},
                {"character": "由", "pinyin": "yóu", "meaning_en": "from; cause", "distinction_note": "Vertical stroke extends upward through the top"},
                {"character": "申", "pinyin": "shēn", "meaning_en": "extend; ninth Earthly Branch", "distinction_note": "Vertical stroke extends both above and below"},
                {"character": "田", "pinyin": "tián", "meaning_en": "field", "distinction_note": "Enclosed square without extending strokes"}
            ],
            "etymological_cognates": [
                {"character": "乙", "pinyin": "yǐ", "gloss_en": "second Heavenly Stem"},
                {"character": "丙", "pinyin": "bǐng", "gloss_en": "third Heavenly Stem"},
                {"character": "丁", "pinyin": "dīng", "gloss_en": "fourth Heavenly Stem"},
                {"character": "魁", "pinyin": "kuí", "gloss_en": "chief; first place"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "甲 designates the foremost serial marker in lists, contracts, and paired competition.",
            "contrasts": [
                {"id": 1, "compared_word": "甲 vs. 乙", "pinyin": "yǐ", "analysis": "甲 is the first item or party in a legal contract, whereas 乙 represents the second counterpart."},
                {"id": 2, "compared_word": "甲 vs. 第一", "pinyin": "dì-yī", "analysis": "第一 is a general numerical cardinal/ordinal ranking, while 甲 is formal bureaucratic/categorical labeling."},
                {"id": 3, "compared_word": "甲 vs. 首", "pinyin": "shǒu", "analysis": "首 denotes headship or initial beginning in time, while 甲 designates a formal tabular class."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代天干地支纪年法源远流长，以‘甲子’为六十循环之首。千百年来，‘甲’字不仅被广泛运用于历法纪年与科举功名排行，更深深烙印在契约文书与世俗日常中，成为首屈一指与无可替代的文化符号。",
                "pinyin": "Zhōngguó gǔdài tiāngān-dìzhī jìnián fǎ yuányuǎn-liúcháng, yǐ 'jiǎzǐ' wéi liùshí xúnhuán zhī shǒu. Qiānbǎinián lái, 'jiǎ' zì bùjǐn bèi guǎngfàn yùnyòng yú lìfǎ jìnián yǔ kējǔ gōngmíng páiháng, gèng shēnshēn làoyìn zài qìyuē wénshū yǔ shìsú rìcháng zhōng, chéngwéi shǒuqū-yìzhǐ yǔ wúkětìdài de wénhuà fúhào.",
                "en": "The ancient Chinese Sexagenary Cycle traces back millennia, with Jiazi heading the sixty-year rotation. The character 'Jia' not only marked imperial exams and calendars, but was imprinted on commercial deeds as the quintessential emblem of primacy.",
                "es": "El ciclo sexagesimal chino encabeza su rotación con 'Jiazi'. Durante siglos, 'Jia' no sólo fijó los anales y oposiciones imperiales, sino que se grabó en contratos y fueros como emblema de máxima jerarquía."
            },
            {
                "id": "#2",
                "hanzi": "在一场别开生面的室内篮球模拟测试中，教练员将学员划分为甲队和乙队展开全场对抗。由于场地两头安装的桃筐缺乏漏底结构，甲队每当投篮得分后，乙队队员都必须暂停防守等待裁判取球，这让比赛气氛大打折扣。",
                "pinyin": "Zài yì chǎng biékāi-shēngmiàn de shìnèi lánqiú mónǐ cèshì zhōng, jiàoliànyuán jiāng xuéyuán huàfēn wéi jiǎ duì hé yǐ duì zhǎnkāi quánchǎng duìkàng. Yóuyú chǎngdì liǎngtóu ānzhuāng de táokuāng quēfá lòudǐ jiégòu, jiǎ duì měidāng tóulán défēn hòu, yǐ duì duìyuán dōu bìxū zàntíng fángshǒu děngdài cáipàn qǔ qiú, zhè ràng bǐsài qìfēn dàdǎ-zhékòu.",
                "en": "In an experimental indoor basketball test, the coach split trainees into Team A and Team B for a full-court scrimmage. Because peach baskets lacked open bottoms, whenever Team A scored, Team B had to halt defenses waiting for referees to extract the ball, dampening the atmosphere.",
                "es": "En un ensayo de baloncesto, el preparador dividió a los alumnos en equipos A y B. Como las canastas no tenían fondo abierto, cada tanto del equipo A obligaba al B a esperar que el árbitro sacara el balón, lastrando el ritmo."
            }
        ]
    },

    # 12 乙
    {
        "id": "12",
        "hanzi": "乙",
        "pinyin": "yǐ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "second (in series); Party B; second Heavenly Stem",
            "es": "segundo; parte B; segundo Tronco Celestial"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the second of the ten Heavenly Stems, used to denote the second person, grade, or party in a series",
                "definition_es": "segundo de los diez Troncos Celestiales, empleado para designar el segundo elemento, grado o contraparte en una serie",
                "example_phrase": "甲乙双方签署协议 (Parties A and B sign the agreement)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在学术研讨会上，甲组主张激进创新，而乙组则偏向稳健审慎，双方辩论非常热烈。",
                "pinyin": "Zài xuéshù yántǎohuì shang, jiǎ zǔ zhǔzhāng jījìn chuàngxīn, ér yǐ zǔ zé piānxiàng wěnjiàn shěnshèn, shuāngfāng biànlùn fēicháng rèliè.",
                "en": "At the academic symposium, Group A advocated radical innovation while Group B favored prudent stability, sparking a spirited debate.",
                "es": "En el simposio académico, el grupo A defendió una innovación audaz mientras que el B apostó por la prudencia, entablándose un vivo debate."
            },
            {
                "id": "#2",
                "hanzi": "根据保密协议条款，未经甲方书面许可，乙方不得将相关技术文档透露给第三方机构。",
                "pinyin": "Gēnjù bǎomì xiéyì tiáokuǎn, wèijīng jiǎfāng shūmiàn xǔkě, yǐfāng bùdé jiāng xiāngguān jìshù wéndàng tòulù gěi dì-sān fāng jīgòu.",
                "en": "According to the non-disclosure agreement, without Party A's prior written consent, Party B shall not disclose relevant technical documents to any third party.",
                "es": "Conforme al acuerdo de confidencialidad, la Parte B no divulgará documentos técnicos a terceros sin el consentimiento expreso y por escrito de la Parte A."
            }
        ],
        "collocations": [
            {"hanzi": "乙方", "en": "Party B (contractee)"},
            {"hanzi": "乙等", "en": "second grade / class B"},
            {"hanzi": "乙级联赛", "en": "second division league"},
            {"hanzi": "乙醇", "en": "ethanol; alcohol"},
            {"hanzi": "甲乙", "en": "Party A and Party B; serial sequence"},
            {"hanzi": "乙烯", "en": "ethylene"}
        ],
        "idioms": [
            {"hanzi": "各执一词", "pinyin": "gè zhí yī cí", "meaning_en": "each sticks to his own version; mutually conflicting stances"},
            {"hanzi": "伯仲之间", "pinyin": "bó zhòng zhī jiān", "meaning_en": "hard to choose between older and younger brother; closely matched"},
            {"hanzi": "相得益彰", "pinyin": "xiāng dé yì zhāng", "meaning_en": "bring out the best in each other; mutual complement"},
            {"hanzi": "不相上下", "pinyin": "bù xiāng shàng xià", "meaning_en": "equally matched; on par with each other"}
        ],
        "character_decomposition": [
            {
                "character": "乙",
                "pinyin": "yǐ",
                "meaning_en": "second; bent; Heavenly Stem",
                "meaning_es": "segundo; curvo; Tronco Celestial",
                "radical": "乙",
                "radical_meaning_en": "second / bent",
                "meaning_component": "pictograph of a sprouting seedling pushing its curved shoot up through soil",
                "sound_component": "乙 (yǐ)",
                "stroke_count": 1,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Single graceful winding stroke representing a tender shoot curving upward as it breaks through hard ground in spring.",
                "visual_mnemonic_story_en": "A tender green sprout curving gently (乙) as it pushes through earth, following Jia as the second stem.",
                "visual_mnemonic_story_es": "Un tierno brote curvándose (乙) al despuntar de la tierra, siguiendo a Jia como segundo tronco.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "N",
                "traditional": "乙"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A single curved stroke like a winding sprout (乙) marks the second tier in traditional ranking.",
            "composite_memory_hook_es": "Un único trazo curvado semejante a un brote (乙) designa la segunda posición en el orden tradicional.",
            "cultural_and_cognitive_roots": "Second of the Heavenly Stems, symbolizing the budding flexibility of springtime vegetation breaking soil.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'yǐ' (214). Drop cleanly and lift slightly at the finish."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "乙", "pinyin": "yǐ", "meaning_en": "second; stem", "distinction_note": "A single continuous stroke with horizontal, turn, and curved hook"},
                {"character": "一", "pinyin": "yī", "meaning_en": "one", "distinction_note": "Straight horizontal bar"},
                {"character": "已", "pinyin": "yǐ", "meaning_en": "already; stop", "distinction_note": "Half-open box with 3 strokes"},
                {"character": "己", "pinyin": "jǐ", "meaning_en": "self", "distinction_note": "Fully open upper box with 3 strokes"}
            ],
            "etymological_cognates": [
                {"character": "甲", "pinyin": "jiǎ", "gloss_en": "first Heavenly Stem"},
                {"character": "次", "pinyin": "cì", "gloss_en": "second; secondary"},
                {"character": "亚", "pinyin": "yà", "gloss_en": "inferior; runner-up"},
                {"character": "副", "pinyin": "fù", "gloss_en": "deputy; vice-"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "乙 denotes the immediate sequel or counterpart paired with 甲 in formal categorizations.",
            "contrasts": [
                {"id": 1, "compared_word": "乙 vs. 甲", "pinyin": "jiǎ", "analysis": "甲 precedes as the initiating partner or primary category, while 乙 follows as the responsive counterpart."},
                {"id": 2, "compared_word": "乙 vs. 第二", "pinyin": "dì-èr", "analysis": "第二 is plain ordinal ranking, while 乙 serves in bilateral agreements and codified schemas."},
                {"id": 3, "compared_word": "乙 vs. 亚军", "pinyin": "yàjūn", "analysis": "亚军 refers strictly to the silver medalist in sporting contests, not a logical category marker."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古人在订立买卖田契与借贷字据时，通篇皆以甲乙二人代称交易双方。这种简明规范的表述不仅清晰界定了彼此的权利与义务，更深刻影响了后世合同法律文书的行文体例，成为契约文明延续千年的重要载体。",
                "pinyin": "Gǔrén zài dìnglì mǎimài tiánqì yǔ jièdài zìjù shí, tōngpiān jiē yǐ jiǎ-yǐ èr rén dàichēng jiāoyì shuāngfāng. Zhè zhǒng jiǎnmíng guīfàn de biǎoshù bùjǐn qīngxī jièdìng le bǐcǐ de quánlì yǔ yìwù, gèng shēnkè yǐngxiǎng le hòushì hétong fǎlǜ wénshū de xíngwén tǐlì, chéngwéi qìyuē wénmíng yánxù qiānnián de zhòngyào zàitǐ.",
                "en": "In ancient deeds of sale and loans, the two trading sides were universally styled Party A and Party B. This standardized phrasing defined mutual rights and duties with precision, laying enduring stylistic foundations for modern contract jurisprudence.",
                "es": "Antiguamente, en escrituras de compraventa y préstamos, las partes se designaban como A y B. Esa fórmula concisa deslindaba con precisión derechos y deberes, influyendo decisivamente en la redacción de contratos hasta nuestros días."
            },
            {
                "id": "#2",
                "hanzi": "在春田学院最初的十八人对抗赛中，詹姆士·奈史密斯将学员随机平分为甲乙两组。由于早期的投篮规则极为严密，乙队即便凭借精湛球技屡屡突破得分，也常常被频繁中断比赛搬梯子取球的环节打乱节奏，球员们迫切盼望能有更为高效顺畅的比赛规则。",
                "pinyin": "Zài Chūntián xuéyuàn zuìchū de shíbā rén duìkàngsài zhōng, Zhānmǔshì Nàishǐmīsī jiāng xuéyuán suíjī píngfēn wéi jiǎ-yǐ liǎng zǔ. Yóuyú zǎoqī de tóulán guīzé jíwéi yánmì, yǐ duì jíbiàn píngjiè jīngzhàn qiújì lǚlǚ tūpò défēn, yě chángcháng bèi pínfán zhòngduàn bǐsài bān tīzi qǔ qiú de huánjié dǎluàn jiézòu, qiúyuánmen pòqiè pànwàng néng yǒu gèng wéi gāoxiào shùnchàng de bǐsài guīzé.",
                "en": "In the inaugural 18-player contest at Springfield College, James Naismith divided students equally into Teams A and B. Although Team B frequently scored with fine skill, their momentum was broken by paused matches to fetch ladders, fueling desires for smoother rules.",
                "es": "En el partido inaugural de 18 jugadores en Springfield, Naismith dividió a los alumnos en grupos A y B. Aunque el equipo B encestaba con pericia, las pausas para subir a la escalera quebraban su ritmo, ansiando un reglamento más ágil."
            }
        ]
    },

    # 13 工具
    {
        "id": "13",
        "hanzi": "工具",
        "pinyin": "gōng jù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "tool; instrument; implement; means",
            "es": "herramienta; instrumento; útil; medio"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an implement or machine used to carry out a particular physical or technical function",
                "definition_es": "objeto o utensilio manual o mecánico destinado a realizar un trabajo determinado",
                "example_phrase": "一套修理汽车的专用工具 (a set of specialized car repair tools)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a means or instrument employed to achieve an objective",
                "definition_es": "recurso o medio instrumental para alcanzar un propósito",
                "example_phrase": "语言是人类沟通的重要工具 (language is an essential tool for communication)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老电工随身携带的皮质工具箱里，整齐排列着螺丝刀、万用表和绝缘钳等常用工具。",
                "pinyin": "Lǎo diàngōng suíshēn xiédài de pízì gōngjùxiāng lǐ, zhěngqí páiliè zhe luósīdāo, wànyòngbiǎo hé juéyuánqián děng chángyòng gōngjù.",
                "en": "Inside the leather toolbox carried by the senior electrician, common tools like screwdrivers, multimeters, and insulated pliers were neatly arrayed.",
                "es": "En la caja de herramientas de cuero del veterano electricista se alineaban destornilladores, polímetros y alicates aislados."
            },
            {
                "id": "#2",
                "hanzi": "现代互联网和人工智能已经从前沿探索全面融入日常生产，成为人类认知世界与提升效率的得力工具。",
                "pinyin": "Xiàndài hùliánwǎng hé réngōng zhìnéng yǐjīng cóng qiányán tànsuǒ quánmiàn róngrù rìcháng shēngchǎn, chéngwéi rénlèi rènzhī shìjiè yǔ tíshēng xiàolǜ de délì gōngjù.",
                "en": "The modern internet and artificial intelligence have integrated into daily production, serving as powerful tools for humanity to comprehend the world and boost efficiency.",
                "es": "Internet y la inteligencia artificial se han integrado de lleno en el trabajo diario, alzándose como herramientas clave para potenciar la productividad humana."
            }
        ],
        "collocations": [
            {"hanzi": "交通工具", "en": "means of transportation"},
            {"hanzi": "工具箱", "en": "toolbox / tool kit"},
            {"hanzi": "辅助工具", "en": "auxiliary tool / aid"},
            {"hanzi": "专用工具", "en": "specialized tool"},
            {"hanzi": "通讯工具", "en": "communication tool"},
            {"hanzi": "工具书", "en": "reference book / dictionary"}
        ],
        "idioms": [
            {"hanzi": "工欲善其事", "pinyin": "gōng yù shàn qí shì", "meaning_en": "a workman must sharpen his tools if he is to do his work well"},
            {"hanzi": "巧夺天工", "pinyin": "qiǎo duó tiān gōng", "meaning_en": "superb craftsmanship outdoing nature"},
            {"hanzi": "莫衷一是", "pinyin": "mò zhōng yī shì", "meaning_en": "unable to agree on which is right; lack consensus"},
            {"hanzi": "游刃有余", "pinyin": "yóu rèn yǒu yú", "meaning_en": "handling a butcher's blade with ample leeway; doing with ease"}
        ],
        "character_decomposition": [
            {
                "character": "工",
                "pinyin": "gōng",
                "meaning_en": "work; craft; carpenter's square",
                "meaning_es": "trabajo; oficio; escuadra de carpintero",
                "radical": "工",
                "radical_meaning_en": "work / craft",
                "meaning_component": "pictograph of an ancient carpenter's plumb square",
                "sound_component": "工 (gōng)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of a carpenter's framing square tool; symbolizes skilled manual fabrication and labor.",
                "visual_mnemonic_story_en": "A carpenter's sturdy level square (工) used by craftsmen to measure perfect right angles.",
                "visual_mnemonic_story_es": "La escuadra de madera (工) usada por el carpintero para medir ángulos rectos en su oficio.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "M",
                "traditional": "工"
            },
            {
                "character": "具",
                "pinyin": "jù",
                "meaning_en": "tool; possess; prepare; utensils",
                "meaning_es": "útil; poseer; disponer; vajilla",
                "radical": "八",
                "radical_meaning_en": "eight",
                "meaning_component": "鼎 (cauldron) held by two hands 廾 (represented by 八)",
                "sound_component": "具 (jù)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two hands holding up a sacrificial bronze vessel full of food; extended to all equipment, utensils, and gear ready for use.",
                "visual_mnemonic_story_en": "Two hands (八) lifting a laden food vessel with multiple compartments, preparing table gear (具).",
                "visual_mnemonic_story_es": "Dos manos (八) elevando una vasija bien abastecida, preparando utensilios necesarios (具).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BAMC",
                "traditional": "具"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The carpenter's framing square (工) paired with handy workshop equipment (具) constitutes a trusty tool (工具).",
            "composite_memory_hook_es": "La escuadra del artesano (工) unida al equipo de taller listo para su uso (具) compone una herramienta útil (工具).",
            "cultural_and_cognitive_roots": "Tool making is recognized in Chinese philosophy (荀子 '善假于物也') as the hallmark distinguishing human wisdom from wild beasts.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling fourth tone: 'gōng jù' (55-51). Hold 'gōng' steady on a high pitch, then drop sharply on 'jù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "工", "pinyin": "gōng", "meaning_en": "work; craft", "distinction_note": "3 strokes with top/bottom horizontal bars"},
                {"character": "土", "pinyin": "tǔ", "meaning_en": "earth; soil", "distinction_note": "Upper horizontal stroke is shorter"},
                {"character": "具", "pinyin": "jù", "meaning_en": "tool; utensil", "distinction_note": "Has 3 horizontal bars inside the 目 framework"},
                {"character": "真", "pinyin": "zhēn", "meaning_en": "true; real", "distinction_note": "Has a top horizontal line with vertical stroke over 目"}
            ],
            "etymological_cognates": [
                {"character": "器", "pinyin": "qì", "gloss_en": "utensil; implement; vessel"},
                {"character": "械", "pinyin": "xiè", "gloss_en": "machinery; device"},
                {"character": "用", "pinyin": "yòng", "gloss_en": "use; employ"},
                {"character": "件", "pinyin": "jiàn", "gloss_en": "item; component"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "工具 primarily refers to physical implements held in the hand or instruments used for specific tasks.",
            "contrasts": [
                {"id": 1, "compared_word": "工具 vs. 仪器", "pinyin": "yíqì", "analysis": "仪器 denotes precision laboratory apparatus with calibrated measuring scales, unlike ordinary rugged manual 工具."},
                {"id": 2, "compared_word": "工具 vs. 机械", "pinyin": "jīxiè", "analysis": "机械 refers to motorized, heavy automated industrial machinery, whereas 工具 are typically hand-held implements."},
                {"id": 3, "compared_word": "工具 vs. 武器", "pinyin": "wǔqì", "analysis": "武器 designates offensive or defensive combat arms meant for warfare, not constructive craft tasks."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "人类之所以能够脱离茹毛饮血的原始蛮荒，关键就在于发明并使用劳动工具。从打制粗糙石斧到冶炼锋利青铜，工具的每一次重大技术迭代，都如同杠杆般撬动着生产力飞跃，深刻重塑着人类社会文明的发展轨迹。",
                "pinyin": "Rénlèi zhī suǒyǐ nénggòu tuōlí rúmáo-yǐnxuè de yuánshǐ mánhuāng, guānjiàn jiù zàiyú fāmíng bìng shǐyòng láodòng gōngjù. Cóng dǎzhì cūcāo shí fǔ dào yěliàn fēnglì qīngtóng, gōngjù de měi yí cì zhòngdà jìshù jiédài, dōu rútóng gànggǎn bān qiàodòng zhe shēngchǎnlì fēiyuè, shēnkè chóngsù zhe rénlèi shèhuì wénmíng de fāzhǎn guǐjì.",
                "en": "Humanity emerged from savage antiquity largely by inventing and mastering tools. From crude stone axes to cast bronze, each major technological leap in tools acted like a lever hoisting productivity and reshaping human civilization.",
                "es": "La humanidad abandonó el salvajismo primordial gracias a la creación de herramientas de trabajo. Del tosco hacha lítica al bronce afilado, cada salto instrumental multiplicó la fuerza productiva, transformando el curso de la civilización."
            },
            {
                "id": "#2",
                "hanzi": "当年奈史密斯发明篮球时，学校体育馆里既缺乏专门护具，也没有合手的投篮工具。面对反复踩梯子取球的笨拙局面，工匠找来最为寻常的锯子这一简单手工工具锯掉了竹筐底部，以极低的成本攻克了比赛流程中的巨大阻碍。",
                "pinyin": "Dāngnián Nàishǐmīsī fāmíng lánqiú shí, xuéxiào tǐyùguǎn lǐ jì quēfá zhuānmén hùjù, yě méiyǒu héshǒu de tóulán gōngjù. Miànduì fǎnfù cǎi tīzi qǔ qiú de bènzhuō júmiàn, gōngjiàng zhǎolái zuìwéi xúncháng de jùzi zhè yí jiǎndān shǒugōng gōngjù jù diào le zhúkuāng dǐbù, yǐ jí dī de chéngběn gōngkè le bǐsài liúchéng zhōng de jùdà zǔ'ài.",
                "en": "When Naismith created basketball, the gym lacked specialized gear and convenient scoring equipment. Faced with awkward ladder-climbing to retrieve balls, a craftsman grabbed an ordinary saw—a simple tool—to cut off the bottoms, solving the bottleneck at minimal cost.",
                "es": "Al nacer el baloncesto, el gimnasio carecía de protecciones e implementos adecuados. Ante el engorro de subir a escaleras para recuperar el balón, un conserje usó una modesta sierra para abrir el fondo, solventando el escollo con suma sencillez."
            }
        ]
    },

    # 14 投篮
    {
        "id": "14",
        "hanzi": "投篮",
        "pinyin": "tóu lán",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to shoot (basketball); to shoot a hoop",
            "es": "tirar a canasta; encestar; lanzar a la cesta"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to throw or shoot the basketball toward the hoop to score points",
                "definition_es": "lanzar el balón hacia la canasta o aro para anotar puntos en baloncesto",
                "example_phrase": "三分线外果断投篮 (shoot decisively from outside the three-point line)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在全场比赛只剩最后两秒的生死关头，主力后卫顶住防守压力后仰投篮，皮球压哨空心入网。",
                "pinyin": "Zài quánchǎng bǐsài zhǐ shèng zuìhòu liǎng miǎo de shēngsǐ guāntóu, zhǔlì hòuwèi dǐngzhù fángshǒu yālì hòuyǎng tóulán, píqiú yāshào kōngxīn rùwǎng.",
                "en": "With merely two seconds left on the clock, the lead guard braved tight defense and sank a buzzer-beating fadeaway jumper cleanly through the net.",
                "es": "Con dos segundos en el marcador, el base titular desafió el marcaje y encestó en suspensión un triple limpio sobre la bocina."
            },
            {
                "id": "#2",
                "hanzi": "要想显著提高比赛中的投篮命中率，运动员必须经过日复一日成千上万次肌肉记忆的强化训练。",
                "pinyin": "Yào xiǎng xiǎnzhù tígāo bǐsài zhōng de tóulán mìngzhònglǜ, yùndòngyuán bìxū jīngguò rì-fù-yírì chéngqiān-shàngwàn cì jīròu jìyì de qiánghuà xùnliàn.",
                "en": "To substantially improve in-game shooting accuracy, players must undergo tens of thousands of repetitions to build muscle memory day after day.",
                "es": "Para mejorar la eficacia de tiro en competición, los jugadores deben acumular miles de lanzamientos diarios consolidando la memoria muscular."
            }
        ],
        "collocations": [
            {"hanzi": "投篮命中率", "en": "field goal shooting percentage"},
            {"hanzi": "后仰投篮", "en": "fadeaway jump shot"},
            {"hanzi": "跳起投篮", "en": "jump shot"},
            {"hanzi": "定点投篮", "en": "set shot / spot-up shooting"},
            {"hanzi": "投篮得分", "en": "score by shooting a basket"},
            {"hanzi": "三分投篮", "en": "three-point shot"}
        ],
        "idioms": [
            {"hanzi": "百步穿杨", "pinyin": "bǎi bù chuān yáng", "meaning_en": "shoot willow leaf from hundred paces; pinpoint shooting accuracy"},
            {"hanzi": "箭无虚发", "pinyin": "jiàn wú xū fā", "meaning_en": "no arrow shot in vain; every shot hits target"},
            {"hanzi": "一发中的", "pinyin": "yī fā zhòng dì", "meaning_en": "hit the bullseye with a single shot; hit the nail on the head"},
            {"hanzi": "百发百中", "pinyin": "bǎi fā bǎi zhòng", "meaning_en": "hit the target a hundred times out of a hundred"}
        ],
        "character_decomposition": [
            {
                "character": "投",
                "pinyin": "tóu",
                "meaning_en": "cast; throw; fling; plunge",
                "meaning_es": "lanzar; arrojar; tirar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand hurling) + 殳 (lance / missile)",
                "sound_component": "殳 (shū / phonetic association)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 beside 殳 (hand holding a missile pole); the action of forcefully flinging or tossing a projectile toward a target.",
                "visual_mnemonic_story_en": "A muscular hand (扌) whipping forward to hurl a javelin missile (殳) toward the target ring (投).",
                "visual_mnemonic_story_es": "Una mano enérgica (扌) lanzando una jabalina (殳) con precisión hacia la meta (投).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "QHE",
                "traditional": "投"
            },
            {
                "character": "篮",
                "pinyin": "lán",
                "meaning_en": "basket; goal hoop",
                "meaning_es": "cesta; canasta; aro",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo weave) + 监 (reflecting supervisor basin)",
                "sound_component": "监 (jiān / phonetic)",
                "stroke_count": 16,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Bamboo radical 竹 over 监; a deep woven basket with handles, extended to the basketball target basket.",
                "visual_mnemonic_story_en": "A round basket woven from bamboo (竹) hung overhead for supervision (监), catching every ball (篮).",
                "visual_mnemonic_story_es": "Una canasta tejida de bambú (竹) suspendida en alto (监), lista para recibir el balón (篮).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HWTIT",
                "traditional": "籃"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Flinging with your hand (投) toward the elevated bamboo hoop (篮) is shooting a basket (投篮).",
            "composite_memory_hook_es": "Lanzar el balón con la mano (投) hacia la canasta suspendida de bambú (篮) es tirar a canasta (投篮).",
            "cultural_and_cognitive_roots": "Direct translation of basketball 'shooting', combining ancient hurling archery terms with modern team sports.",
            "tone_sandhi_and_pitch_modulation": "Two rising second tones: 'tóu lán' (35-35). Rise cleanly across both syllables with crisp, ascending inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "投", "pinyin": "tóu", "meaning_en": "throw; cast", "distinction_note": "Hand radical 扌 on left with 殳"},
                {"character": "没", "pinyin": "méi", "meaning_en": "not have; sink", "distinction_note": "Water radical 氵 on left"},
                {"character": "篮", "pinyin": "lán", "meaning_en": "basket", "distinction_note": "Bamboo radical 竹 on top over 监"},
                {"character": "蓝", "pinyin": "lán", "meaning_en": "blue color", "distinction_note": "Grass radical 艹 on top over 监"}
            ],
            "etymological_cognates": [
                {"character": "掷", "pinyin": "zhì", "gloss_en": "hurl; fling"},
                {"character": "抛", "pinyin": "pāo", "gloss_en": "toss; cast aside"},
                {"character": "扔", "pinyin": "rēng", "gloss_en": "throw; discard"},
                {"character": "射", "pinyin": "shè", "gloss_en": "shoot; emit"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "投篮 specifically denotes shooting the ball at the basket hoop in basketball.",
            "contrasts": [
                {"id": 1, "compared_word": "投篮 vs. 传球", "pinyin": "chuánqiú", "analysis": "传球 means passing the ball to a teammate to advance play, whereas 投篮 aims directly at scoring points."},
                {"id": 2, "compared_word": "投篮 vs. 射门", "pinyin": "shèmén", "analysis": "射门 denotes kicking or striking the ball into a soccer/hockey goal net, not shooting into an elevated hoop."},
                {"id": 3, "compared_word": "投篮 vs. 扣篮", "pinyin": "kòulán", "analysis": "扣篮 (dunk) involves leaping and forcefully slamming the ball downward through the rim, a subset of scoring attempts."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "黄昏的社区球场上，少年一遍又一遍地练习着中距离急停投篮。每一次高高跃起、手腕轻柔拨动皮球的瞬间，橙色的篮球便在空中划出一道优美圆润的弧线。汗水浸透了衣衫，但那声清脆的擦网声就是对坚持最好的奖赏。",
                "pinyin": "Huánghūn de shèqū qiúchǎng shang, shàonián yí biàn yòu yí biàn de liànxí zhe zhōng jùlí jítíng tóulán. Měi yí cì gāogāo yuèqǐ, shǒuwàn qīngróu bōdòng píqiú de shùnjiān, chéngsè de lánqiú biàn zài kōngzhōng huà chū yí dào yōuměi yuánrùn de húxiàn. Hànshuǐ jìntòu le yīshān, dàn nà shēng qīngcuì de cā wǎng shēng jiùshì duì jiānchí zuì hǎo de jiǎngshǎng.",
                "en": "On the community court at twilight, the boy practiced pull-up jump shots repeatedly. Every time he leaped and gently flicked his wrist, the orange ball traced a graceful arc through the air. Sweat drenched his jersey, but the crisp swish was the sweetest reward.",
                "es": "En la cancha del barrio al anochecer, el joven ensayaba tiros en suspensión una y otra vez. Cada salto y sutil giro de muñeca dibujaban en el aire una parábola perfecta. Empapado en sudor, el chasquido de la red premiaba su constancia."
            },
            {
                "id": "#2",
                "hanzi": "在一百多年前篮球刚被发明时，运动员投篮命中后的取球过程极为繁琐。因为球筐底部是封闭的，每次投篮成功后比赛都必须被迫中断，工作人员必须搬来长梯把球掏出来。直到人们锯掉筐底，投篮才真正成为连续、激烈且扣人心弦的高速竞技过程。",
                "pinyin": "Zài yìbǎi duō nián qián lánqiú gāng bèi fāmíng shí, yùndòngyuán tóulán mìngzhòng hòu de qǔ qiú guòchéng jíwéi fánsuǒ. Yīnwèi qiúkuāng dǐbù shì fēngbì de, měicì tóulán chénggōng hòu bǐsài dōu bìxū bèipò zhòngduàn, gōngzuò rényuán bìxū bān lái chángtī bǎ qiú tāo chūlái. Zhídào rénmen jù diào kuāngdǐ, tóulán cái zhēnzhèng chéngwéi liánxù, jīliè qiě kòurénxīnxuán de gāosù jìngjì guòchéng.",
                "en": "Over a century ago when basketball was invented, retrieving balls after a made basket was tedious. Because basket bottoms were sealed, every score halted the game for staff to haul ladders and fish out the ball. Only when bottoms were sawed open did shooting become a thrilling, continuous thrill.",
                "es": "Hace más de un siglo, recuperar el balón tras encestar era engorroso. Con canastas de fondo cerrado, cada acierto obligaba a parar el partido para bajar la bola con escalera. Al abrir el fondo, el tiro se tornó en un espectáculo trepidante y fluido."
            }
        ]
    },

    # 15 踩
    {
        "id": "15",
        "hanzi": "踩",
        "pinyin": "cǎi",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to step on; tread; stamp on; depress (pedal)",
            "es": "pisar; pisotear; presionar (pedal)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to put one's foot down upon something; to tread or stamp",
                "definition_es": "poner el pie sobre algo presionándolo con el peso corporal",
                "example_phrase": "踩着梯子爬上去 (climb up stepping on a ladder)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to depress a vehicle pedal (accelerator, brake)",
                "definition_es": "accionar un pedal mecánico con el pie",
                "example_phrase": "紧急踩刹车 (slam on the emergency brakes)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "司机在雨天湿滑的路段行驶时突然发现前方有障碍物，连忙果断踩下了防抱死紧急刹车。",
                "pinyin": "Sījī zài yǔtiān shīhuá de lùduàn xíngshǐ shí tūrán fāxiàn qiánfāng yǒu zhàng'àiwù, liánmáng guǒduàn cǎi xià le fángbàosǐ jǐnjí shāchē.",
                "en": "Driving along the wet and slippery road, the driver suddenly spotted an obstacle ahead and promptly stepped hard on the anti-lock emergency brakes.",
                "es": "Conducía sobre el asfalto mojado cuando divisó un obstáculo adelante, pisando de inmediato y con firmeza el freno de emergencia con ABS."
            },
            {
                "id": "#2",
                "hanzi": "为了在早春季节修剪屋檐下的枯树枝，园艺工小心翼翼地踩着折叠木梯一步步往上爬。",
                "pinyin": "Wèile zài zǎochūn jìjié xiūjiǎn wūyán xià de kū shùzhī, yuányìgōng xiǎoxīn-yìyì de cǎi zhe zhédié mùtī yíbùbù wǎng shàng pá.",
                "en": "To prune dead branches beneath the eaves in early spring, the gardener cautiously climbed up, stepping carefully on the folding wooden ladder.",
                "es": "Para podar ramas secas bajo el alero a principios de primavera, el jardinero subió paso a paso pisando con sumo tiento la escalera plegable."
            }
        ],
        "collocations": [
            {"hanzi": "踩刹车", "en": "step on the brake pedal"},
            {"hanzi": "踩油门", "en": "step on the gas accelerator"},
            {"hanzi": "踩在脚下", "en": "trample under foot"},
            {"hanzi": "踩着梯子", "en": "step on the rungs of a ladder"},
            {"hanzi": "不小心踩到", "en": "accidentally step on"},
            {"hanzi": "踩点", "en": "arrive right on the dot / stake out"}
        ],
        "idioms": [
            {"hanzi": "脚踏实地", "pinyin": "jiǎo tà shí dì", "meaning_en": "have one's feet planted on solid ground; conscientious and practical"},
            {"hanzi": "步步为营", "pinyin": "bù bù wéi yíng", "meaning_en": "build camp at every step; proceed cautiously and firmly"},
            {"hanzi": "登高望远", "pinyin": "dēng gāo wàng yuǎn", "meaning_en": "scale heights to gaze into distance; broad perspective"},
            {"hanzi": "践踏公义", "pinyin": "jiàn tà gōng yì", "meaning_en": "trample upon public justice and fair play"}
        ],
        "character_decomposition": [
            {
                "character": "踩",
                "pinyin": "cǎi",
                "meaning_en": "step on; tread; trample",
                "meaning_es": "pisar; pisotear",
                "radical": "足",
                "radical_meaning_en": "foot",
                "meaning_component": "足 (foot / stepping leg)",
                "sound_component": "采 (cǎi / gather; phonetic)",
                "stroke_count": 15,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Foot radical 足 beside 采 (hand plucking); placing one's foot firmly downward to step or tread upon something.",
                "visual_mnemonic_story_en": "A nimble foot (足) stepping down firmly while reaching hands gather (采) fruit from overhead.",
                "visual_mnemonic_story_es": "Un pie firme (足) que pisa con aplomo mientras las manos recolectan (采) fruta de lo alto.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RMBD",
                "traditional": "踩"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Your active foot (足) stepping onto the ground while harvesting (采) means to step on (踩).",
            "composite_memory_hook_es": "Poner el pie (足) apoyándolo con firmeza mientras cosechas (采) equivale a pisar (踩).",
            "cultural_and_cognitive_roots": "Everyday physical verb expressing physical foot pressure, stepping on rungs, or driving pedals.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'cǎi' (214). Drop into the lower vocal pit and curve gently up."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "踩", "pinyin": "cǎi", "meaning_en": "step on; tread", "distinction_note": "Foot radical 足 on left"},
                {"character": "采", "pinyin": "cǎi", "meaning_en": "pluck; gather; spirit", "distinction_note": "Base character without foot radical"},
                {"character": "彩", "pinyin": "cǎi", "meaning_en": "colorful; prize", "distinction_note": "Has 彡 (hair/feather brush) on right"},
                {"character": "睬", "pinyin": "cǎi", "meaning_en": "pay attention to; heed", "distinction_note": "Eye radical 目 on left"}
            ],
            "etymological_cognates": [
                {"character": "踏", "pinyin": "tà", "gloss_en": "tread; step firmly"},
                {"character": "蹬", "pinyin": "dēng", "gloss_en": "pedal; kick down"},
                {"character": "跨", "pinyin": "kuà", "gloss_en": "step across; straddle"},
                {"character": "踱", "pinyin": "duó", "gloss_en": "pace; stroll slowly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "踩 focuses on placing weight downward with the foot onto a surface or pedal.",
            "contrasts": [
                {"id": 1, "compared_word": "踩 vs. 踏", "pinyin": "tà", "analysis": "踏 is more literary and formal (脚踏实地, 踏步), while 踩 is the predominant colloquial term in daily life (踩刹车, 踩脚)."},
                {"id": 2, "compared_word": "踩 vs. 踢", "pinyin": "tī", "analysis": "踢 involves swinging the leg forward or sideways to strike a ball, whereas 踩 presses straight downward with body weight."},
                {"id": 3, "compared_word": "踩 vs. 跺", "pinyin": "duò", "analysis": "跺 emphasizes violently stomping one's feet in anger or cold (跺脚), unlike ordinary stepping (踩)."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "深秋清晨的古朴庭院里落满了厚厚的金黄银杏叶，踩上去发出沙沙的轻响，宛如踏在一张柔软温暖的金色地毯上。晨练的老人放慢了脚步，生怕惊扰了这一片静谧祥和的秋意。",
                "pinyin": "Shēnqiū qīngchén de gǔpǔ tíngyuàn lǐ luòmǎn le hòuhòu de jīnhuáng yínxìng yè, cǎi shàngqu fāchū shāshā de qīngxiǎng, wǎnrú tà zài yì zhāng róuruǎn wēnnuǎn de jīnsè dìtǎn shang. Chénliàn de lǎorén fàngmàn le jiǎobù, shēngpà jīngrǎo le zhè yí piàn jìngmì xiánghé de qiūyì.",
                "en": "In the courtyard on a late autumn morning, thick golden ginkgo leaves blanketed the flagstones, rustling softly underfoot like a warm carpet. An elderly jogger slowed his pace, reluctant to disturb the serene autumn calm.",
                "es": "En el patio señorial de otoño yacían hojas de ginkgo doradas, que crujían con suavidad bajo las pisadas como una alfombra mullida. El anciano paseante aminoró el paso para no turbar la apacible quietud del alba."
            },
            {
                "id": "#2",
                "hanzi": "在早期篮球比赛中，每当皮球落入竹筐，比赛就不得不被迫叫停。工作人员必须搬来折叠木梯，小心翼翼地踩着晃晃悠悠的梯恩子爬到三米多高处把球取出来。这种不断搬梯子、踩梯子的繁琐过程，极大消磨了现场观众和球员的激情。",
                "pinyin": "Zài zǎoqī lánqiú bǐsài zhōng, měidāng píqiú luòrù zhúkuāng, bǐsài jiù bùdébù bèipò jiàotíng. Gōngzuò rényuán bìxū bān lái zhédié mùtī, xiǎoxīn-yìyì de cǎi zhe huànghuang-yōuyōu de tīzi pá dào sān mǐ duō gāochù bǎ qiú qǔ chūlái. Zhè zhǒng búduàn bān tīzi, cǎi tīzi de fánsuǒ guòchéng, jídà xiāomó le xiànchǎng guānzhòng hé qiúyuán de jīqíng.",
                "en": "In early basketball games, whenever the ball lodged in the basket, play had to be paused. Custodians dragged over folding ladders, gingerly stepping up rickety rungs ten feet high to dislodge it. Continually hauling and stepping onto ladders severely drained players' passion.",
                "es": "Al comienzo del baloncesto, cada enceste paralizaba el juego. El personal arrastraba una escalera de madera y subía con cautela a más de tres metros para retirar la pelota. Aquel trajín de pisar peldaños enfriaba el fervor de jugadores y público."
            }
        ]
    },

    # 16 一再
    {
        "id": "16",
        "hanzi": "一再",
        "pinyin": "yí zài",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "repeatedly; time and again; over and over",
            "es": "reiteradamente; una y otra vez; repetidamente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "doing something repeatedly, multiple times, often regarding reminders, warnings, or occurrences",
                "definition_es": "hacer algo reiteradas veces, especialmente en advertencias, solicitudes o retrasos",
                "example_phrase": "一再强调安全生产 (repeatedly emphasize workplace safety)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "班主任在出发前一再叮嘱同学们，在野外徒步考察时必须听从领队指挥，切勿私自脱离团队行动。",
                "pinyin": "Bānzhǔrèn zài chūfā qián yízài dīngzhǔ tóngxuémen, zài yěwài túbù kǎochá shí bìxū tīngcóng lǐngduì zhǐhuī, qièwù sīsì tuōlí tuánduì xíngdòng.",
                "en": "Before setting off, the teacher repeatedly urged students to heed the group leader's orders during field hikes and never wander off alone.",
                "es": "Antes de partir, el tutor insistió repetidamente a los alumnos en obedecer al guía durante la excursión y no alejarse jamás del grupo."
            },
            {
                "id": "#2",
                "hanzi": "尽管项目组一再压缩开支并优化施工流程，但因国际原材料价格暴涨，整体预算依然超出了预期。",
                "pinyin": "Jǐnguǎn xiàngmùzǔ yízài yāsuō kāizhī bìng yōuhuà shīgōng liúchéng, dàn yīn guójì yuáncáiliào jiàgé bàozhǎng, zhěngtǐ yùsuàn yīrán chāochū le yùqī.",
                "en": "Although the project team repeatedly compressed expenses and streamlined operations, surging global raw material prices still drove budgets beyond expectations.",
                "es": "Aunque el equipo recortó gastos reiteradamente y optimizó los procesos, el alza internacional de materias primas disparó el presupuesto por encima de lo previsto."
            }
        ],
        "collocations": [
            {"hanzi": "一再强调", "en": "repeatedly emphasize"},
            {"hanzi": "一再推迟", "en": "repeatedly postpone / delay"},
            {"hanzi": "一再重申", "en": "reiterate time and again"},
            {"hanzi": "一再表示", "en": "express repeatedly"},
            {"hanzi": "一再要求", "en": "request insistently"},
            {"hanzi": "一再保证", "en": "guarantee repeatedly"}
        ],
        "idioms": [
            {"hanzi": "三番五次", "pinyin": "sān fān wǔ cì", "meaning_en": "time and time again; over and over repeatedly"},
            {"hanzi": "再三再四", "pinyin": "zài sān zài sì", "meaning_en": "again and again; repeated endlessly"},
            {"hanzi": "苦口婆心", "pinyin": "kǔ kǒu pó xīn", "meaning_en": "admonish with earnest patient words"},
            {"hanzi": "言犹在耳", "pinyin": "yán yóu zài ěr", "meaning_en": "words still ringing in one's ears"}
        ],
        "character_decomposition": [
            {
                "character": "一",
                "pinyin": "yī",
                "meaning_en": "one; single; whole",
                "meaning_es": "uno; solo; entero",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "pictograph of single counting rod",
                "sound_component": "一 (yī)",
                "stroke_count": 1,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Single horizontal line representing the primordial unity and initial starting point in counting.",
                "visual_mnemonic_story_en": "A single straight horizontal beam (一), marking the foundation of all counting.",
                "visual_mnemonic_story_es": "Una sola viga horizontal recta (一), base y principio de todo cálculo numérico.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "M",
                "traditional": "一"
            },
            {
                "character": "再",
                "pinyin": "zài",
                "meaning_en": "again; once more; second time",
                "meaning_es": "otra vez; de nuevo; reiterar",
                "radical": "冂",
                "radical_meaning_en": "down open box",
                "meaning_component": "two strokes stacked over a frame base",
                "sound_component": "再 (zài)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Originally a pair of horizontal counting sticks tied together, indicating two times, repetition, or renewal.",
                "visual_mnemonic_story_en": "Stacking another crossbar across the wooden frame, signifying repeating an action once more (再).",
                "visual_mnemonic_story_es": "Añadir otro travesaño sobre el bastidor, denotando repetir una acción una vez más (再).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GBY",
                "traditional": "再"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Doing once (一) and then once again (再) means doing something repeatedly (一再).",
            "composite_memory_hook_es": "Hacerlo una vez (一) y de inmediato otra vez más (再) expresa actuar reiteradamente (一再).",
            "cultural_and_cognitive_roots": "Expresses strong intentional insistence or unavoidable recurrence in classical and contemporary rhetoric.",
            "tone_sandhi_and_pitch_modulation": "Tone sandhi: 'yī' changes to rising second tone before fourth tone 'zài': 'yí zài' (35-51). Rise on 'yí', then drop forcefully on 'zài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "再", "pinyin": "zài", "meaning_en": "again; once more", "distinction_note": "Has horizontal stroke through top of 冂 and base line"},
                {"character": "在", "pinyin": "zài", "meaning_en": "at; in; exist", "distinction_note": "Starts with 𠂇 and has earth radical 土 at bottom"},
                {"character": "冉", "pinyin": "rǎn", "meaning_en": "gradually; drooping", "distinction_note": "Middle vertical stroke extends downward"},
                {"character": "甫", "pinyin": "fǔ", "meaning_en": "just; ancient honorific", "distinction_note": "Has a top dot and crossing vertical stroke"}
            ],
            "etymological_cognates": [
                {"character": "屡", "pinyin": "lǚ", "gloss_en": "repeatedly; frequently"},
                {"character": "频", "pinyin": "pín", "gloss_en": "frequency; repeatedly"},
                {"character": "复", "pinyin": "fù", "gloss_en": "duplicate; repeat"},
                {"character": "迭", "pinyin": "dié", "gloss_en": "alternate; repeatedly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "一再 indicates intentional human speech, insistence, or action recurring multiple times consecutively.",
            "contrasts": [
                {"id": 1, "compared_word": "一再 vs. 再次", "pinyin": "zàicì", "analysis": "再次 simply denotes doing something a second time or once more, while 一再 emphasizes persistent multiple repetitions (一再申明)."},
                {"id": 2, "compared_word": "一再 vs. 常常", "pinyin": "chángcháng", "analysis": "常常 describes habitual customary actions over time, whereas 一再 emphasizes insistent recurrence in a specific context."},
                {"id": 3, "compared_word": "一再 vs. 重新", "pinyin": "chóngxīn", "analysis": "重新 means starting over completely from the beginning, while 一再 signifies reiterating or repeating an existing act."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "科学家在发布气候变化评估报告时一再警告，全球气温持续上升将引发极端风暴与严重干旱。如果各国不能尽快达成碳减排约束性协议，人类社会赖以生存的生态平衡系统将在不远的将来面临不可逆转的灾难性崩溃。",
                "pinyin": "Kēxuéjiā zài fābù qìhòu biànhuà pínggū bàogào shí yízài jǐnggào, quánqiú qìwēn chíxù shàngshēng jiāng yǐnfā jíduān fēngbào yǔ yánzhòng gānhàn. Rúguǒ gèguó bùnéng jǐnkuài dáchéng tàn jiǎnpái yuēshùxìng xiéyì, rénlèi shèhuì làiyǐ shēngcún de shēngtài pínghéng xìtǒng jiāng zài bù yuǎn de jiānglái miànlín bùkě nìzhuǎn de zāinànxìng bēngkuì.",
                "en": "Scientists issuing climate assessment reports warned repeatedly that rising temperatures will trigger extreme storms and droughts. Without binding carbon reduction pacts, the ecological equilibrium sustaining civilization faces irreversible collapse.",
                "es": "Al presentar su informe climático, los científicos advirtieron reiteradamente del riesgo de tormentas extremas y sequías por el calentamiento. Sin pactos vinculantes de emisiones, el equilibrio ecológico del planeta colapsará de forma irreversible."
            },
            {
                "id": "#2",
                "hanzi": "在早期篮球教学实践中，学生们对每次投篮后不得不搬梯子取球的笨拙流程一再抱怨。比赛节奏的一再中断，让激烈的对抗气氛大打折扣。正是面对这种频繁发生的困扰，体育工匠才下定决心拿起锯子锯掉筐底，彻底革除了这一弊端。",
                "pinyin": "Zài zǎoqī lánqiú jiàoxué shíjiàn zhōng, xuéshengmen duì měicì tóulán hòu bùdébù bān tīzi qǔ qiú de bènzhuō liúchéng yízài bàoyuàn. Bǐsài jiézòu de yízài zhòngduàn, ràng jīliè de duìkàng qìfēn dàdǎ-zhékòu. Zhèng shì miànduì zhè zhǒng pínfán fāshēng de kùnrǎo, tǐyù gōngjiàng cái xiàdìng juéxīn ná qǐ jùzi jù diào kuāngdǐ, chèdǐ géchú le zhè yí bìduān.",
                "en": "During early basketball training, students complained repeatedly about fetching ladders after each score. The repeated game interruptions dampened the fierce competition. Prompted by these constant annoyances, craftsmen resolved to saw off the basket bottoms, eliminating the hassle forever.",
                "es": "En los primeros entrenamientos de baloncesto, los alumnos se quejaban reiteradamente de tener que acarrear escaleras tras cada canasta. El ritmo roto enfriaba el duelo, empujando a los conserjes a serrar el fondo para desterrar el problema."
            }
        ]
    },

    # 17 重复
    {
        "id": "17",
        "hanzi": "重复",
        "pinyin": "chóng fù",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to repeat; duplicate; reiterate; repetition",
            "es": "repetir; duplicar; reiterar; repetición"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to do, say, or undergo something again; to recur identically",
                "definition_es": "volver a hacer, decir o experimentar algo de forma idéntica",
                "example_phrase": "请把刚才的话重复一遍 (please repeat what you just said)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "由于网络信号在隧道中出现中断，会议主持人不得不把刚才的核心议题又向大家重复了一遍。",
                "pinyin": "Yóuyú wǎngluò xìnhào zài suìdào zhōng chūxiàn zhòngduàn, huìyì zhǔchírén bùdébù bǎ gāngcái de héxīn yìtí yòu xiàng dàjiā chóngfù le yí biàn.",
                "en": "Because network signals dropped inside the tunnel, the meeting host had to repeat the core agenda item to everyone once more.",
                "es": "Al cortarse la conexión en el túnel, el moderador de la reunión tuvo que repetir a los asistentes el punto central tratado."
            },
            {
                "id": "#2",
                "hanzi": "历史经验告诉我们，只有深刻汲取教训并完善制度，才能避免在相同的危机面前重复过去的错误。",
                "pinyin": "Lìshǐ jīngyàn gàosù wǒmen, zhǐyǒu shēnkè jíqǔ jiàoxùn bìng wánshàn zhìdù, cái néng bìmiǎn zài xiāngtóng de wēijī miànqián chóngfù guòqù de cuòwù.",
                "en": "Historical experience teaches that only by profoundly absorbing lessons and refining institutions can we avoid repeating past mistakes during similar crises.",
                "es": "La historia demuestra que sólo aprendiendo de los errores y mejorando las instituciones evitaremos repetir pasadas equivocaciones ante crisis semejantes."
            }
        ],
        "collocations": [
            {"hanzi": "重复一遍", "en": "repeat once again"},
            {"hanzi": "机械重复", "en": "mechanical mindless repetition"},
            {"hanzi": "重复建设", "en": "redundant construction / duplication"},
            {"hanzi": "重复使用", "en": "reuse / repeated use"},
            {"hanzi": "避免重复", "en": "avoid duplication"},
            {"hanzi": "重复劳动", "en": "repetitive manual toil"}
        ],
        "idioms": [
            {"hanzi": "重蹈覆辙", "pinyin": "chóng dǎo fù zhé", "meaning_en": "follow the overturned cart track; repeat the disastrous mistake"},
            {"hanzi": "周而复始", "pinyin": "zhōu ér fù shǐ", "meaning_en": "circle round and begin anew; cyclical recurrence"},
            {"hanzi": "日复一日", "pinyin": "rì fù yí rì", "meaning_en": "day after day; routine uninterrupted persistence"},
            {"hanzi": "老生常谈", "pinyin": "lǎo shēng cháng tán", "meaning_en": "old scholar's platitude; familiar shopworn talk"}
        ],
        "character_decomposition": [
            {
                "character": "重",
                "pinyin": "chóng",
                "meaning_en": "repeat; layer; again",
                "meaning_es": "repetir; capa; de nuevo",
                "radical": "里",
                "radical_meaning_en": "village / inside",
                "meaning_component": "pictograph of heavy baggage piled up in layers",
                "sound_component": "重 (chóng/zhòng)",
                "stroke_count": 9,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A person standing over a layered bundle or heavy grain sack; dual reading as heavy (zhòng) and layered repetition (chóng).",
                "visual_mnemonic_story_en": "Multiple heavy bundles stacked on top of one another layer upon layer (重).",
                "visual_mnemonic_story_es": "Múltiples fardos pesados apilados uno sobre otro capa tras capa (重).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HJG",
                "traditional": "重"
            },
            {
                "character": "复",
                "pinyin": "fù",
                "meaning_en": "return; repeat; complex",
                "meaning_es": "regresar; duplicar; complejo",
                "radical": "夂",
                "radical_meaning_en": "go / step",
                "meaning_component": "夂 (trailing footsteps) + 畐 (vessel)",
                "sound_component": "复 (fù)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Footsteps 夂 tracing a path back to a walled settlement; returning along original tracks to repeat an action.",
                "visual_mnemonic_story_en": "Footsteps (夂) turning around and retracing their exact path back to the starting point (复).",
                "visual_mnemonic_story_es": "Pasos (夂) que dan media vuelta desandando el camino exacto hacia el punto de partida (复).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OAE",
                "traditional": "複"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Layering over (重) and retracing footsteps back (复) leads to identical repetition (重复).",
            "composite_memory_hook_es": "Apilar capas (重) y desandar los pasos hacia el inicio (复) da lugar a una repetición idéntica (重复).",
            "cultural_and_cognitive_roots": "Foundational in cognitive learning theory (熟能生巧) and scientific experimentation where replicability validates truth.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'chóng fù' (35-51). Soar upward on 'chóng', then drive down decisively on 'fù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "重", "pinyin": "chóng/zhòng", "meaning_en": "repeat; heavy", "distinction_note": "Single vertical axis piercing horizontal bars"},
                {"character": "童", "pinyin": "tóng", "meaning_en": "child; youth", "distinction_note": "Has 立 (stand) on top instead of 千"},
                {"character": "复", "pinyin": "fù", "meaning_en": "repeat; complex", "distinction_note": "Has 夂 at bottom"},
                {"character": "夏", "pinyin": "xià", "meaning_en": "summer", "distinction_note": "Has 目-like head under the upper horizontal canopy"}
            ],
            "etymological_cognates": [
                {"character": "叠", "pinyin": "dié", "gloss_en": "stack; fold; repeat"},
                {"character": "蹈", "pinyin": "dǎo", "gloss_en": "tread; repeat steps"},
                {"character": "循", "pinyin": "xún", "gloss_en": "follow; cycle"},
                {"character": "环", "pinyin": "huán", "gloss_en": "ring; loop"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "重复 indicates the identical recurrence of an action, sound, or state without substantial variation.",
            "contrasts": [
                {"id": 1, "compared_word": "重复 vs. 反复", "pinyin": "fǎnfù", "analysis": "反复 often connotes back-and-forth instability or wavering (病情反复, 反复无常), whereas 重复 means straightforward copying or reiteration."},
                {"id": 2, "compared_word": "重复 vs. 循环", "pinyin": "xúnhuán", "analysis": "循环 implies a closed systemic loop (血液循环), while 重复 can be an isolated second occurrence of an event."},
                {"id": 3, "compared_word": "重复 vs. 重建", "pinyin": "chóngjiàn", "analysis": "重建 means building from ruins or reconstructing an organization, whereas 重复 merely repeats an action."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "科研工作者在实验室里日复一日地重复着枯燥的数据测定与化学配比实验。正是这种严谨求实、不厌其烦的高精度重复验证，才最终剥离掉偶然误差的干扰，让颠扑不破的科学真理在严苛检验中熠熠生辉。",
                "pinyin": "Kēyán gōngzuòzhě zài shíyànshì lǐ rì-fù-yírì de chóngfù zhe kūzào de shùjù cèdìng yǔ huàxué pèibǐ shíyàn. Zhèng shì zhè zhǒng yánjǐn qiúshí, bùyàn-qífán de gāo jīngdù chóngfù yànzhèng, cái zuìzhōng bōlí diào ǒurán wùchā de gānrǎo, ràng diānpū-bùpò de kēxué zhēnlǐ zài yánkē jiǎnyàn zhōng yìyì-shēnghuī.",
                "en": "Researchers repeated tedious data calibrations and chemical ratios day after day in the laboratory. It was this rigorous, untiring repetition that stripped away accidental errors, allowing immutable scientific truth to shine through.",
                "es": "Los científicos repetían mediciones y formulaciones día tras día en el laboratorio. Esa meticulosa comprobación reiterada permitió descartar errores fortuitos, corroborando con rigor la verdad científica ante la prueba experimental."
            },
            {
                "id": "#2",
                "hanzi": "早期的篮球比赛每得一分，裁判和队员都必须重复相同的繁琐动作：暂停走表、搬出梯子、爬上去把球取出、再放回场中重新跳球。这种单调机械的重复不仅打断了比赛的连贯性，更严重制约了体育竞技激情的释放。",
                "pinyin": "Zǎoqī de lánqiú bǐsài měi dé yì fēn, cáipàn hé duìyuán dōu bìxū chóngfù xiāngtóng de fánsuǒ dòngzuò: zàntíng zǒu biǎo, bān chū tīzi, pá shàngqu bǎ qiú qǔ chū, zài fàng huí chǎngzhōng chóngxīn tiào qiú. Zhè zhǒng dāndiào jīxiè de chóngfù bùjǐn dǎduàn le bǐsài de liánguànxìng, gèng yánzhòng zhìyuē le tǐyù jìngjì jīqíng de shìfàng.",
                "en": "Every scored point in early basketball forced players and referees to repeat the same tedious cycle: stop the clock, drag out a ladder, climb up to dislodge the ball, and resume with a jump ball. Such mechanical repetition crippled the game's continuity and spirit.",
                "es": "En los albores del baloncesto, cada canasta obligaba a repetir el mismo engorro: parar el reloj, arrastrar la escalera, descolgar el balón y hacer un salto entre dos. Esa pesada rutina cortaba la fluidez ahogando la emoción del juego."
            }
        ]
    },

    # 18 断断续续
    {
        "id": "18",
        "hanzi": "断断续续",
        "pinyin": "duàn duàn xù xù",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "intermittent; off and on; discontinuous; fitful",
            "es": "intermitente; entrecortado; discontinuo; a saltos"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "stopping and starting repeatedly at irregular intervals; discontinuous in time, sound, or action",
                "definition_es": "que cesa y recomienza sucesivamente con interrupciones frecuentes de tiempo o sonido",
                "example_phrase": "断断续续的琴声 (intermittent piano notes)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "深夜的山谷里下起了断断续续的微雨，清凉的雨滴敲打着窗外的芭蕉叶，伴随着淅淅沥沥的水声传入耳畔。",
                "pinyin": "Shēnyè de shāngǔ lǐ xià qǐ le duànduàn-xùxù de wēiyǔ, qīngliáng de yǔdī qiāodǎ zhe chuāngwài de bājiāoyè, bànsuí zhe xīxī-lìlì de shuǐshēng chuán rù ěrpàn.",
                "en": "In the valley at midnight, intermittent drizzle began to fall, cool raindrops tapping upon banana leaves outside the window with gentle splashes.",
                "es": "A medianoche caía una llovizna intermitente en el valle; las frescas gotas golpeaban los bananeros del patio arrullando el sueño con su leve rumor."
            },
            {
                "id": "#2",
                "hanzi": "由于山区基站遭受雷击损坏，前线救援队员只能依靠断断续续的卫星无线电信号与指挥中心保持微弱联络。",
                "pinyin": "Yóuyú shānqū jīzhàn shòuzāo léijī sǔnhuài, qiánxiàn jiùyuánduìyuán zhǐ néng yīkào duànduàn-xùxù de wèixīng wúxiàndiàn xìnhào yǔ zhǐhuī zhōngxīn bǎochí wēiruò liánluò.",
                "en": "Because mountain cell towers were damaged by lightning, rescue teams had to rely on intermittent satellite radio signals to maintain faint contact with headquarters.",
                "es": "Averiada la antena por un rayo, los rescatistas sólo pudieron mantener una débil comunicación con la base mediante señales de radio intermitentes."
            }
        ],
        "collocations": [
            {"hanzi": "断断续续的雨", "en": "intermittent rain / showers"},
            {"hanzi": "断断续续的声音", "en": "broken, intermittent sound"},
            {"hanzi": "断断续续地进行", "en": "proceed in fits and starts"},
            {"hanzi": "断断续续的记忆", "en": "patchy, fragmentary memories"},
            {"hanzi": "信号断断续续", "en": "spotty / intermittent signal"},
            {"hanzi": "断断续续地讲述", "en": "recount haltingly"}
        ],
        "idioms": [
            {"hanzi": "时断时续", "pinyin": "shí duàn shí xù", "meaning_en": "stopping and starting alternately; intermittent"},
            {"hanzi": "声断气噎", "pinyin": "shēng duàn qì yē", "meaning_en": "sobbing fitfully with broken gasps"},
            {"hanzi": "连绵不断", "pinyin": "liánmián bú duàn", "meaning_en": "continuous and unbroken; stretching endlessly"},
            {"hanzi": "藕断丝连", "pinyin": "ǒu duàn sī lián", "meaning_en": "lotus root snapped but fibers still cling; lingering ties"}
        ],
        "character_decomposition": [
            {
                "character": "断",
                "pinyin": "duàn",
                "meaning_en": "snap; break off; sever; decide",
                "meaning_es": "romper; quebrar; seccionar; decidir",
                "radical": "斤",
                "radical_meaning_en": "axe",
                "meaning_component": "斤 (axe chopping) + 米 (silk threads / grain bundles)",
                "sound_component": "断 (duàn)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An axe 斤 chopping through bundled skeins of thread 米; severing connection and snapping in two.",
                "visual_mnemonic_story_en": "An axe blade (斤) slicing straight through skeins of silk thread (米) to break them apart (断).",
                "visual_mnemonic_story_es": "El filo de un hacha (斤) cortando hebras de seda (米) para seccionarlas en dos (断).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VIDH",
                "traditional": "斷"
            },
            {
                "character": "续",
                "pinyin": "xù",
                "meaning_en": "continue; replenish; tie together",
                "meaning_es": "continuar; reanudar; enlazar",
                "radical": "纟",
                "radical_meaning_en": "silk thread",
                "meaning_component": "纟 (silk cords) + 卖 (prolonged trade)",
                "sound_component": "卖 (mài / phonetic association)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk radical 纟 beside 卖; tying broken ends of silk filaments together to maintain an unbroken continuum.",
                "visual_mnemonic_story_en": "Tying loose silk cords (纟) together at the marketplace (卖) to keep the thread going (续).",
                "visual_mnemonic_story_es": "Empatar cabos de seda sueltos (纟) para que la línea continúe sin romperse (续).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VFGND",
                "traditional": "續"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Breaking apart (断) and tying back together (续) over and over creates an intermittent rhythm (断断续续).",
            "composite_memory_hook_es": "Romper (断) y volver a empalmar (续) sucesivamente da lugar a una cadencia intermitente (断断续续).",
            "cultural_and_cognitive_roots": "A classic AABB four-character reduplicative adjective conveying rhythmic hesitation, fragmentation, or sporadic recurrence.",
            "tone_sandhi_and_pitch_modulation": "Four syllables: 'duàn duàn xù xù' (51-51-51-51). Pronounce with staccato, rhythmic falling tones mirroring fitful pauses."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "断", "pinyin": "duàn", "meaning_en": "break; snap", "distinction_note": "Axe radical 斤 on the right"},
                {"character": "继", "pinyin": "jì", "meaning_en": "succeed; follow", "distinction_note": "Has 纟 on left with 米 and 乚"},
                {"character": "续", "pinyin": "xù", "meaning_en": "continue; join", "distinction_note": "Has 纟 on left with 卖 on right"},
                {"character": "读", "pinyin": "dú", "meaning_en": "read; study", "distinction_note": "Speech radical 讠 on left with 卖"}
            ],
            "etymological_cognates": [
                {"character": "停", "pinyin": "tíng", "gloss_en": "stop; halt"},
                {"character": "歇", "pinyin": "xiē", "gloss_en": "rest; pause"},
                {"character": "顿", "pinyin": "dùn", "gloss_en": "pause; sudden"},
                {"character": "缀", "pinyin": "zhuì", "gloss_en": "stitch together; embellish"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "断断续续 expresses discontinuous cadence, halting pauses, or erratic recurrence.",
            "contrasts": [
                {"id": 1, "compared_word": "断断续续 vs. 陆陆续续", "pinyin": "lùlù-xùxù", "analysis": "陆陆续续 describes people arriving or events happening one after another over time without back-and-forth breaking, while 断断续续 stresses intermittent interruption."},
                {"id": 2, "compared_word": "断断续续 vs. 连续不断", "pinyin": "liánxù-búduàn", "analysis": "连续不断 denotes smooth unbroken continuity, the direct antonym of 断断续续."},
                {"id": 3, "compared_word": "断断续续 vs. 偶尔", "pinyin": "ǒu'ěr", "analysis": "偶尔 means occasional isolated instances, while 断断续续 implies an ongoing stream plagued by frequent stops and starts."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "病榻上的老红军呼吸微弱，拉着孙子的手断断续续地回忆起战火纷飞的峥嵘岁月。那些零散破碎的字句，虽被剧烈的咳嗽屡次打断，却依然如重锤般撞击着年轻人的心灵，传递着穿越时空的坚贞信仰。",
                "pinyin": "Bìngtà shang de lǎo hóngjūn hūxī wēiruò, lā zhe sūnzi de shǒu duànduàn-xùxù de huíyì qǐ zhànhuǒ fēnfēi de zhēngróng suìyuè. Nàxiē língsǎn pòsuì de zìjù, suī bèi jùliè de késou lǚcì dǎduàn, què yīrán rú zhòngchuí bān zhuàngjī zhe niánqīngrén de xīnlíng, chuándì zhe chuānyuè shíkōng de jiānzhēn xìnyǎng.",
                "en": "On his sickbed, the frail veteran gripped his grandson's hand, haltingly recalling wartime years. Though interrupted by coughing bouts, his fragmented words struck the young man's heart like hammers, conveying timeless steadfast faith.",
                "es": "En su lecho, el anciano combatiente rememoraba entrecortadamente los años de guerra. Aunque la tos quebraba sus palabras, aquel relato fragmentario conmovió hondamente a su nieto transmitiéndole una fe inquebrantable."
            },
            {
                "id": "#2",
                "hanzi": "未开底的桃筐曾给最初的篮球比赛带来了毁灭性的断断续续。每当双方球员在热烈呐喊中投球入网，裁判就必须强行按停计时表，场上热烈沸腾的气氛也随即冷却下来。正是为了消除这种令人烦躁的断断续续，才促成了锯开筐底的革新。",
                "pinyin": "Wèi kāidǐ de táokuāng céng gěi zuìchū de lánqiú bǐsài dài lái le huǐmièxìng de duànduàn-xùxù. Měidāng shuāngfāng qiúyuán zài rèliè nàhǎn zhōng tóu qiú rù wǎng, cáipàn jiù bìxū qiángxíng àntíng jìshíbiǎo, chǎngshang rèliè fèiténg de qìfēn yě suíjí lěngquè xiàlái. Zhèng shì wèile xiāochú zhè zhǒng lìngrén fánzào de duànduàn-xùxù, cái cùchéng le jù kāi kuāngdǐ de géxīn.",
                "en": "Peach baskets without open bottoms brought frustrating intermittence to early basketball. Whenever a ball went in amid cheers, referees had to freeze the clock, dousing the court's fiery momentum. Eliminating this annoying stop-and-start catalyzed sawing off the basket bottoms.",
                "es": "Las cestas ciegas provocaban una fastidiosa discontinuidad en el baloncesto primigenio. Tras cada enceste en plena ovación, el colegiado paraba el cronómetro enfriando el duelo. Erradicar esas pausas impulsó la genial idea de abrir el fondo."
            }
        ]
    },

    # 19 激烈
    {
        "id": "19",
        "hanzi": "激烈",
        "pinyin": "jī liè",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "intense; fierce; acute; sharp (competition/debate)",
            "es": "intenso; feroz; encarnizado; vehemente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "violent, sharp, or intensely competitive in action, speech, or contest",
                "definition_es": "vehemente, violento o sumamente reñido en disputas, combates o competiciones",
                "example_phrase": "激烈的市场竞争 (intense market competition)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过四节激烈焦灼的加时鏖战，客场作战的年轻球队终于以一分微弱优势险胜卫冕冠军。",
                "pinyin": "Jīngguò sì jié jīliè jiāozhuó de jiāshí áozhàn, kèchǎng zuòzhàn de niánqīng qiúduì zhōngyú yǐ yì fēn wēiruò yōushì xiǎnshèng wèimiǎn guànjūn.",
                "en": "After four quarters of intensely grueling overtime struggle, the young visiting team finally edged out the defending champions by a razor-thin one-point margin.",
                "es": "Tras cuatro periodos de encarnizada prórroga, el joven conjunto visitante se impuso al vigente campeón por la mínima renta de un punto."
            },
            {
                "id": "#2",
                "hanzi": "在今天举行的听证会上，双方律师围绕核心证据的法律效力展开了异常激烈而尖锐的言语交锋。",
                "pinyin": "Zài jīntiān jǔxíng de tīngzhènghuì shang, shuāngfāng lǜshī wéirào héxīn zhèngjù de fǎlǜ xiàolì zhǎnkāi le yìcháng jīliè ér jiānruì de yányǔ jiāofēng.",
                "en": "At today's hearing, opposing attorneys engaged in exceptionally fierce and sharp verbal clashes surrounding the admissibility of core evidence.",
                "es": "En la vista judicial de hoy, los letrados sostuvieron un duelo dialéctico sumamente vehemente en torno a la validez de la prueba pericial."
            }
        ],
        "collocations": [
            {"hanzi": "激烈竞争", "en": "fierce / intense competition"},
            {"hanzi": "激烈争论", "en": "heated / fierce debate"},
            {"hanzi": "战斗激烈", "en": "fierce fighting in battle"},
            {"hanzi": "言辞激烈", "en": "vehement / fierce words"},
            {"hanzi": "异常激烈", "en": "unusually intense"},
            {"hanzi": "激烈对抗", "en": "intense confrontation"}
        ],
        "idioms": [
            {"hanzi": "龙争虎斗", "pinyin": "lóng zhēng hǔ dòu", "meaning_en": "struggle between dragon and tiger; fierce titanic clash"},
            {"hanzi": "风起云涌", "pinyin": "fēng qǐ yún yǒng", "meaning_en": "winds gather and clouds surge; dramatic rapid developments"},
            {"hanzi": "惊心动魄", "pinyin": "jīng xīn dòng pò", "meaning_en": "thrilling and breathtaking; heart-stirring shock"},
            {"hanzi": "如火如荼", "pinyin": "rú huǒ rú tú", "meaning_en": "flourishing like wildfire; surging intensely"}
        ],
        "character_decomposition": [
            {
                "character": "激",
                "pinyin": "jī",
                "meaning_en": "surge; arouse; fierce water flow",
                "meaning_es": "desbordar; excitar; torrente",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (turbulent water) + 敫 (bright white light / strike)",
                "sound_component": "敫 (jiào / phonetic)",
                "stroke_count": 16,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 beside 敫; crashing water surging over rocks, generating rapid currents and white spray.",
                "visual_mnemonic_story_en": "Turbulent water currents (氵) violently striking against river boulders, surging in white spray (激).",
                "visual_mnemonic_story_es": "Aguas bravas (氵) que embisten contra los escollos rocosos alzando espumarajos turbulentos (激).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "EHSK",
                "traditional": "激"
            },
            {
                "character": "烈",
                "pinyin": "liè",
                "meaning_en": "blazing; ardent; fierce; violent",
                "meaning_es": "ardiente; violento; vehemente",
                "radical": "灬",
                "radical_meaning_en": "fire",
                "meaning_component": "灬 (four dots of raging fire) + 列 (split with knife)",
                "sound_component": "列 (liè / phonetic)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Raging fire flames 灬 burning fiercely beneath cleaved fuel 列; symbolizes extreme intensity, heat, and vehement force.",
                "visual_mnemonic_story_en": "Raging flames (灬) consuming split firewood (列) in an inferno of intense heat (烈).",
                "visual_mnemonic_story_es": "Llamas voraces (灬) devorando leña rajada (列) en una hoguera de calor abrasador (烈).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MNOF",
                "traditional": "烈"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Surging whitewater currents (激) meeting blazing fire flames (烈) produce intense ferocity (激烈).",
            "composite_memory_hook_es": "El ímpetu del torrente de agua (激) sumado a un fuego abrasador (烈) desata una lucha encarnizada (激烈).",
            "cultural_and_cognitive_roots": "Metaphor combining torrential water surges and roaring flames to describe heated struggles, sports, and debates.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling fourth tone: 'jī liè' (55-51). Sustain 'jī' with energy, then strike sharply down on 'liè'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "激", "pinyin": "jī", "meaning_en": "surge; fierce", "distinction_note": "Water radical 氵 on left with 敫"},
                {"character": "澈", "pinyin": "chè", "meaning_en": "crystal clear", "distinction_note": "Has 育 in middle instead of 白/方"},
                {"character": "烈", "pinyin": "liè", "meaning_en": "intense; fiery", "distinction_note": "Fire radical 灬 at bottom under 列"},
                {"character": "列", "pinyin": "liè", "meaning_en": "row; line; arrange", "distinction_note": "Without the fire dots at bottom"}
            ],
            "etymological_cognates": [
                {"character": "猛", "pinyin": "měng", "gloss_en": "fierce; ferocious"},
                {"character": "热", "pinyin": "rè", "gloss_en": "hot; ardent"},
                {"character": "酷", "pinyin": "kù", "gloss_en": "ruthless; harsh; intense"},
                {"character": "厉", "pinyin": "lì", "gloss_en": "stern; severe"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "激烈 describes dynamic confrontations, contests, motions, or debates that reach extreme fever pitch.",
            "contrasts": [
                {"id": 1, "compared_word": "激烈 vs. 强烈", "pinyin": "qiángliè", "analysis": "强烈 describes sensations, emotions, lights, or desires (强烈愿望, 强烈地震), while 激烈 depicts dynamic external actions, combats, and sports."},
                {"id": 2, "compared_word": "激烈 vs. 热烈", "pinyin": "rèliè", "analysis": "热烈 conveys joyful enthusiasm and warmth (热烈欢迎, 掌声热烈), whereas 激烈 emphasizes aggressive rivalry and conflict."},
                {"id": 3, "compared_word": "激烈 vs. 严厉", "pinyin": "yánlì", "analysis": "严厉 characterizes harsh disciplinary attitudes or punishment (严厉批评), not athletic contests."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "现代商业社会的竞争异常激烈，任何固步自封、安于现状的企业都会在转瞬之间被汹涌的技术浪潮所淘汰。唯有时刻保持敏锐的危机意识，敢于自我颠覆并不断推陈出新，方能在激烈的市场大潮中立于不败之地。",
                "pinyin": "Xiàndài shāngyè shèhuì de jìngzhēng yìcháng jīliè, rènhé gùbù-zìfēng, ānyú xiànzhuàng de qǐyè dōu huì zài zhuǎnshùn zhījiān bèi xiōngyǒng de jìshù làngcháo suǒ táotài. Wéi yǒu shíkè bǎochí mǐnruì de wēijī yìshí, gǎnyú zìwǒ diānfù bìng búduàn tuīchén-chūxīn, fāng néng zài jīliè de shìchǎng dàcháo zhōng lìyú-búbàizhīdì.",
                "en": "Modern commercial rivalry is brutally intense; any company resting on its laurels will be swept away by surging technological tides. Only by maintaining acute crisis awareness and bold self-disruption can one stay invincible amid fierce market headwinds.",
                "es": "La rivalidad comercial actual es implacable; las empresas acomodadas caen barridas por olas de innovación. Sólo quien mantiene alerta su sentido de supervivencia y se reinventa logra prevalecer invicto en ese agitado mercado."
            },
            {
                "id": "#2",
                "hanzi": "奈史密斯发明篮球旨在为冬季青年提供室内运动。随着规则完善，对抗日益激烈。球星们高超的投篮技艺与雷霆万钧的封盖，构成了当今体坛最令人热血沸腾的竞技盛景。",
                "pinyin": "Nàishǐmīsī fāmíng lánqiú zhǐzài wèi dōngjì qīngnián tígōng shìnèi yùndòng. Suízhe guīzé wánshàn, duìkàng rìyì jīliè. Qiúxīngmen gāocháo de tóulán jìyì yǔ léitíng-wànjūn de fēnggài, gòuchéng le dāngjīn tǐtán zuì lìngrén rèxuè-fèiténg de jìngjì shèngjǐng.",
                "en": "Naismith invented basketball to provide indoor athletic exercise for youth in winter. As rules matured, matchups grew fiercely competitive. Sublime shooting and thunderous blocks now form one of sports' most electrifying spectacles.",
                "es": "Naismith concibió el baloncesto para ejercitar a los jóvenes bajo techo en invierno. Con la madurez reglamentaria, el duelo se tornó encarnizado, deslumbrando al mundo con tiros magistrales y tapones colosales."
            }
        ]
    },

    # 20 气氛
    {
        "id": "20",
        "hanzi": "气氛",
        "pinyin": "qì fēn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "atmosphere; ambience; mood (of a place or gathering)",
            "es": "atmósfera; ambiente; clima (emocional o social)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the pervading tone, mood, or emotional climate of a place, meeting, or event",
                "definition_es": "estado o tono emocional que se respira en un lugar, reunión o espectáculo",
                "example_phrase": "热烈活跃的节日气氛 (a lively and warm festive atmosphere)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "除夕之夜全家人围坐在热气腾腾的火锅旁守岁，客厅里处处洋溢着团圆祥和的温馨气氛。",
                "pinyin": "Chúxī zhī yè quánjiā rén wéizuò zài rèqì-téngténg de huǒguō páng shǒusuì, kètīng lǐ chùchù yángyì zhe tuányuán xiánghé de wēnxīn qìfēn.",
                "en": "On New Year's Eve, the whole family gathered around the steaming hotpot to welcome the new year, the parlor brimming with a cozy atmosphere of reunion and peace.",
                "es": "En Nochevieja, la familia se congregó en torno al humeante caldero mongol, respirándose en la sala una atmósfera entrañable de armonía y reencuentro."
            },
            {
                "id": "#2",
                "hanzi": "谈判刚开始时双方各不相让，但随着主谈代表幽默机智的开场发言，紧张压抑的会谈气氛逐渐缓和了下来。",
                "pinyin": "Tánpàn gāng kāishǐ shí shuāngfāng gèbùxiāngràng, dàn suízhe zhǔtán dàibiǎo yōumò jīzhì de kāichǎng fāyán, jǐnzhāng yāyì de huìtán qìfēn zhújiàn huǎnhé le xiàlái.",
                "en": "The talks began with neither side yielding an inch, but with the chief negotiator's witty remarks, the tense and oppressive atmosphere gradually thawed.",
                "es": "La negociación arrancó con total rigidez, pero el ingenioso discurso inaugural del mediador destensó gradualmente el agobiante clima de la sala."
            }
        ],
        "collocations": [
            {"hanzi": "节日气氛", "en": "festive atmosphere"},
            {"hanzi": "紧张气氛", "en": "tense atmosphere"},
            {"hanzi": "热烈气氛", "en": "warm / spirited ambience"},
            {"hanzi": "活跃气氛", "en": "liven up the mood / atmosphere"},
            {"hanzi": "营造气氛", "en": "create an atmosphere"},
            {"hanzi": "气氛融洽", "en": "harmonious / congenial atmosphere"}
        ],
        "idioms": [
            {"hanzi": "欢天喜地", "pinyin": "huān tiān xǐ dì", "meaning_en": "overjoyed; filled with exuberant rejoicing"},
            {"hanzi": "喜气洋洋", "pinyin": "xǐ qì yáng yáng", "meaning_en": "beaming with joy; cheerful holiday spirit"},
            {"hanzi": "剑拔弩张", "pinyin": "jiàn bá nǔ zhāng", "meaning_en": "swords drawn and bows bent; touch-and-go explosive tension"},
            {"hanzi": "和风细雨", "pinyin": "hé fēng xì yǔ", "meaning_en": "gentle breeze and mild rain; patient kindly persuasion"}
        ],
        "character_decomposition": [
            {
                "character": "气",
                "pinyin": "qì",
                "meaning_en": "air; gas; energy; mood; spirit",
                "meaning_es": "aire; gas; aliento; espíritu",
                "radical": "气",
                "radical_meaning_en": "steam / breath",
                "meaning_component": "pictograph of rising clouds and curling steam",
                "sound_component": "气 (qì)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of layers of vapor and steam curling upward into the sky; vital life force and atmospheric air.",
                "visual_mnemonic_story_en": "Wisps of vapor and warm air (气) rising gently into the atmosphere.",
                "visual_mnemonic_story_es": "Volutas de vapor y aliento cálido (气) elevándose suavemente en el aire.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "ON",
                "traditional": "氣"
            },
            {
                "character": "氛",
                "pinyin": "fēn",
                "meaning_en": "atmosphere; vapor; misty haze",
                "meaning_es": "vaho; atmósfera; halo",
                "radical": "气",
                "radical_meaning_en": "steam / breath",
                "meaning_component": "气 (atmospheric vapor) + 分 (divide / share)",
                "sound_component": "分 (fēn / phonetic)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Air radical 气 enclosing 分; ambient vapor and mist dividing and drifting across the environment, setting its mood.",
                "visual_mnemonic_story_en": "Vapors (气) drifting and dispersing (分) to envelope an entire room in a distinct mood (氛).",
                "visual_mnemonic_story_es": "Vahos etéreos (气) que se dispersan (分) impregnando el ambiente de un matiz singular (氛).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "ONCSH",
                "traditional": "氛"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Vaporous air (气) spreading across the room (氛) creates the palpable atmosphere (气氛).",
            "composite_memory_hook_es": "El aliento invisible del aire (气) que impregna el espacio (氛) conforma la atmósfera del lugar (气氛).",
            "cultural_and_cognitive_roots": "Deeply linked to traditional Chinese concept of 'Qi' (气), the intangible energetic vibe uniting people and environment.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by level high tone: 'qì fēn' (51-55). Strike down on 'qì', then float evenly on high 'fēn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "氛", "pinyin": "fēn", "meaning_en": "atmosphere", "distinction_note": "Contains 分 inside 气"},
                {"character": "氧", "pinyin": "yǎng", "meaning_en": "oxygen", "distinction_note": "Contains 羊 inside 气"},
                {"character": "氮", "pinyin": "dàn", "meaning_en": "nitrogen", "distinction_note": "Contains 炎 inside 气"},
                {"character": "氢", "pinyin": "qīng", "meaning_en": "hydrogen", "distinction_note": "Contains 𢀖 inside 气"}
            ],
            "etymological_cognates": [
                {"character": "境", "pinyin": "jìng", "gloss_en": "environment; realm"},
                {"character": "情", "pinyin": "qíng", "gloss_en": "emotion; sentiment"},
                {"character": "象", "pinyin": "xiàng", "gloss_en": "phenomenon; aura"},
                {"character": "象", "pinyin": "xiàng", "gloss_en": "image; manifestation"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "气氛 denotes the psychological, emotional, or social ambience prevailing in a shared space.",
            "contrasts": [
                {"id": 1, "compared_word": "气氛 vs. 环境", "pinyin": "huánjìng", "analysis": "环境 refers to objective physical conditions, surroundings, or ecology, whereas 气氛 describes intangible emotional ambience."},
                {"id": 2, "compared_word": "气氛 vs. 气候", "pinyin": "qìhòu", "analysis": "气候 denotes meteorological weather patterns over decades, while 气氛 is the psychological tone of a gathering."},
                {"id": 3, "compared_word": "气氛 vs. 心情", "pinyin": "xīnqíng", "analysis": "心情 is an individual's private emotional state, whereas 气氛 is collective and shared across a group or venue."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "春节期间的大街小巷张灯结彩，到处弥漫着浓郁喜庆的年节气氛。爆竹声声伴随着清脆的欢笑，邻里之间互致吉祥问候，那一份份淳朴热烈的情感，在冬日暖阳的照耀下汇聚成最动人的社会温情画卷。",
                "pinyin": "Chūnjié qījiān de dàjiē-xiǎoxiàng zhāngdēng-jiécǎi, dàochù mímàn zhe nóngyù xǐqìng de niánjié qìfēn. Bàozhú shēngshēng bànsuí zhe qīngcuì de huānxiào, línlǐ zhījiān hùzhì jíxiáng wènhòu, nà yífènfèn chúnpǔ rèliè de qínggǎn, zài dōngrì nuǎnyáng de zhàoyào xià huìjù chéng zuì dòngrén de shèhuì wēnqíng huàjuàn.",
                "en": "During Spring Festival, streets were adorned with lanterns and festive streamers, suffused with celebratory holiday cheer. Firecrackers popped alongside laughter as neighbors exchanged blessings, weaving a moving tapestry of community warmth.",
                "es": "En Año Nuevo chino, las calles lucían farolillos entre una atmósfera festiva y entrañable. Petardos y risas se fundían con parabienes vecinales, conformando bajo el sol invernal un cálido tapiz de afecto social."
            },
            {
                "id": "#2",
                "hanzi": "篮球场上火热的竞技气氛，最忌讳被频繁机械的停顿所扑灭。早年因为桃筐未掏空底部，每次投篮进球后观众都必须百无聊赖地看着工人们踩梯取球，原本紧张刺激的比赛气氛瞬间变得索然无味。锯掉筐底的巧思，真正挽救了这项运动的灵魂活力。",
                "pinyin": "Lánqiúchǎng shang huǒrè de jìngjì qìfēn, zuì jìhuì bèi pínfán jīxiè de tíngdùn suǒ pūmiè. Zǎonián yīnwèi táokuāng wèi tāokōng dǐbù, měicì tóulán jìnqiú hòu guānzhòng dōu bìxū bǎiwú-liáolài de kàn zhe gōngrénmen cǎi tī qǔ qiú, yuánběn jǐnzhāng cìjī de bǐsài qìfēn shùnjiān biàn de suǒrán-wúwèi. Jù diào kuāngdǐ de qiǎosī, zhēnzhèng wǎnjiù le zhè xiàng yùndòng de línghún huólì.",
                "en": "The fiery atmosphere of the basketball court suffers most from mechanical interruptions. In early years, because peach baskets lacked open bottoms, fans boredly watched workers climb ladders after each score, deflating the thrilling mood. Sawing open the bottom truly salvaged the sport's electric soul.",
                "es": "El fervor de la pista de baloncesto se marchita con parones mecánicos. Al inicio, las canastas ciegas forzaban al público a contemplar cómo se bajaba el balón con escaleras, apagando la pasión. Abrir el fondo rescató el alma vibrante del juego."
            }
        ]
    }
]

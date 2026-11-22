# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 四合院
    {
        "id": "1",
        "hanzi": "四合院",
        "pinyin": "sì hé yuàn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "siheyuan; traditional Chinese quadrangle courtyard dwelling",
            "es": "siheyuan; patio cuadrangular tradicional de Pekín"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a traditional Chinese residential compound consisting of houses arranged around a central square courtyard on four sides",
                "definition_es": "vivienda residencial tradicional china compuesta por pabellones en cuatro lados en torno a un patio central",
                "example_phrase": "北京老城区的四合院 (traditional quadrangle courtyards of old Beijing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "爷爷在北京胡同里那座青砖灰瓦的四合院里生活了大半辈子，院子里常年种着石榴树与枣树。",
                "pinyin": "Yéye zài Běijīng hútòng lǐ nà zuò qīngzhuān-huīwǎ de sìhéyuàn lǐ shēnghuó le dàbànbèizi, yuànzi lǐ chángnián zhòng zhe shíliushù yǔ zǎoshù.",
                "en": "Grandfather lived for over half his life in that grey-brick and tiled courtyard house in a Beijing alley, where pomegranate and jujube trees grew year-round.",
                "es": "El abuelo vivió más de media vida en aquel patio cuadrangular de ladrillo gris en un hutong pekinés, donde crecían granados y azufaifos."
            },
            {
                "id": "#2",
                "hanzi": "作为中国传统建筑文化的杰出代表，保存完好的四合院如今已成为中外游客体验老北京民俗风情的必访之地。",
                "pinyin": "Zuòwéi Zhōngguó chuántǒng jiànzhù wénhuà de jiéchū dàibiǎo, bǎocún wánhǎo de sìhéyuàn rújīn yǐ chéngwéi zhōngwài yóukè tǐyàn lǎo Běijīng mínsú fēngqíng de bìfǎng zhīdì.",
                "en": "As an outstanding representative of traditional Chinese architectural culture, well-preserved courtyard homes are now must-visit sites for cultural immersion.",
                "es": "Como joya de la arquitectura tradicional china, los patios bien conservados son paradas obligadas para que viajeros de todo el mundo descubran el viejo Pekín."
            }
        ],
        "collocations": [
            {"hanzi": "北京四合院", "en": "Beijing quadrangle courtyard"},
            {"hanzi": "一座四合院", "en": "a courtyard compound (classifier 座)"},
            {"hanzi": "传统四合院", "en": "traditional quadrangle courtyard"},
            {"hanzi": "住在四合院", "en": "live in a quadrangle courtyard"},
            {"hanzi": "四合院建筑", "en": "siheyuan courtyard architecture"},
            {"hanzi": "四合院格局", "en": "courtyard layout structure"}
        ],
        "idioms": [
            {"hanzi": "深宅大院", "pinyin": "shēn zhái dà yuàn", "meaning_en": "deep mansions and spacious courtyards; aristocratic compounds"},
            {"hanzi": "庭院深深", "pinyin": "tíng yuàn shēn shēn", "meaning_en": "courtyards deep and secluded; classical quietude"},
            {"hanzi": "安居乐业", "pinyin": "ān jū lè yè", "meaning_en": "live in peace and work with contentment"},
            {"hanzi": "和睦相处", "pinyin": "hé mù xiāng chǔ", "meaning_en": "live together in peaceful harmony"}
        ],
        "character_decomposition": [
            {
                "character": "四",
                "pinyin": "sì",
                "meaning_en": "four; cardinal directions",
                "meaning_es": "cuatro; cuatro puntos cardinales",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (four-sided enclosure) + 八 (diverging lines)",
                "sound_component": "四 (sì)",
                "stroke_count": 5,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "Enclosed box 囗 with two dividing lines inside; represents the four cardinal orientations: East, West, South, and North.",
                "visual_mnemonic_story_en": "An enclosed space (囗) dividing cleanly into four cardinal quadrants (四).",
                "visual_mnemonic_story_es": "Un recinto cerrado (囗) dividido en cuatro cuadrantes cardinales (四).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "WC",
                "traditional": "四"
            },
            {
                "character": "合",
                "pinyin": "hé",
                "meaning_en": "join; enclose; unite; close",
                "meaning_es": "unir; juntar; cerrar; confluir",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "人 (roof / covering lid) + 一 + 口 (box container)",
                "sound_component": "合 (hé)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A lid 人 fitting seamlessly over a vessel 口; closing on all sides to form an enclosed harmonious unit.",
                "visual_mnemonic_story_en": "Fitting a snug lid (人) onto a square box container (口) so four walls join seamlessly (合).",
                "visual_mnemonic_story_es": "Ajustar una tapadera (人) sobre una caja (口) para que las cuatro paredes encajen en unión (合).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OMR",
                "traditional": "合"
            },
            {
                "character": "院",
                "pinyin": "yuàn",
                "meaning_en": "courtyard; compound; institution",
                "meaning_es": "patio; recinto; claustro",
                "radical": "阝",
                "radical_meaning_en": "mound / wall",
                "meaning_component": "阝 (earthen boundary wall) + 完 (complete / whole)",
                "sound_component": "完 (wán / phonetic association)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Boundary wall 阝 surrounding a completed domestic dwelling 完; a safe, open courtyard enclosed by perimeter walls.",
                "visual_mnemonic_story_en": "Solid earthen perimeter walls (阝) sheltering a fully completed residential homestead (完): a peaceful courtyard (院).",
                "visual_mnemonic_story_es": "Muros protectores (阝) que resguardan una vivienda entera y completa (完): el patio solariego (院).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NLJMU",
                "traditional": "院"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Four sides (四) joining in harmony (合) around an enclosed central courtyard (院) form a siheyuan (四合院).",
            "composite_memory_hook_es": "Cuatro alas (四) cerradas en armonía (合) abrazando un patio interior (院) definen el siheyuan (四合院).",
            "cultural_and_cognitive_roots": "Emblematic of ancient Chinese cosmological philosophy: square layout reflects 'round heaven and square earth' (天圆地方), fostering filial clan unity.",
            "tone_sandhi_and_pitch_modulation": "Three syllables: 'sì hé yuàn' (51-35-51). Descend firmly on 'sì', rise smoothly on 'hé', and drop with resonance on 'yuàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "院", "pinyin": "yuàn", "meaning_en": "courtyard; institution", "distinction_note": "Mound radical 阝 on left of 完"},
                {"character": "完", "pinyin": "wán", "meaning_en": "finish; complete", "distinction_note": "Roof 宀 over 元 without the 阝 radical"},
                {"character": "合", "pinyin": "hé", "meaning_en": "join; close", "distinction_note": "Roof 人 over 一 and 口"},
                {"character": "舍", "pinyin": "shè/shě", "meaning_en": "cottage; abandon", "distinction_note": "Has 舌-like structure below 𠆢"}
            ],
            "etymological_cognates": [
                {"character": "庭", "pinyin": "tíng", "gloss_en": "hall; courtyard"},
                {"character": "宅", "pinyin": "zhái", "gloss_en": "residence; homestead"},
                {"character": "第", "pinyin": "dì", "gloss_en": "mansion; grade"},
                {"character": "阁", "pinyin": "gé", "gloss_en": "pavilion; chamber"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "四合院 specifically denotes the quadrangle courtyard residential architecture of northern China.",
            "contrasts": [
                {"id": 1, "compared_word": "四合院 vs. 公寓", "pinyin": "gōngyù", "analysis": "公寓 designates modern multi-story apartment complexes with elevator lobbies, whereas 四合院 is a single-story walled inward-facing courtyard."},
                {"id": 2, "compared_word": "四合院 vs. 别墅", "pinyin": "biéshù", "analysis": "别墅 is a standalone suburban villa surrounded by open lawns, while 四合院 encloses an internal private courtyard hidden behind high outer walls."},
                {"id": 3, "compared_word": "四合院 vs. 窑洞", "pinyin": "yáodòng", "analysis": "窑洞 refers to cave dwellings carved into Loess Plateau bluffs in northwestern China, distinct from masonry 四合院."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "四合院是中国华北地区最为典型的民居建筑形式。所谓四合，‘四’指东、西、南、北四面房屋，‘合’则是四面房屋围在一起，中间形成一个宽敞的方形院落。这种建筑布局既保证了家族起居的私密，又充满了人伦温情。",
                "pinyin": "Sìhéyuàn shì Zhōngguó Huáběi dìqū zuìwéi diǎnxíng de mínjū jiànzhù xíngshì. Suǒwèi sìhé, 'sì' zhǐ dōng, xī, nán, běi sì miàn fángwū, 'hé' zé shì sì miàn fángwū wéi zài yìqǐ, zhōngjiān xíngchéng yí ge kuānchǎng de fāngxíng yuànluò. Zhè zhǒng jiànzhù bùjú jì bǎozhèng le jiāzú qǐjū de sīmì, yòu chōngmǎn le rénlún wēnqíng.",
                "en": "The siheyuan is the most typical traditional residence in North China. 'Four' refers to the houses on four sides, while 'join' means enclosing them to form a spacious central square courtyard. This layout secures domestic privacy while brimming with clan warmth.",
                "es": "El siheyuan es la vivienda tradicional más emblemática del norte de China. Las cuatro alas en los puntos cardinales abrazan un amplio patio cuadrado central, resguardando la intimidad familiar y albergando un entrañable calor de hogar."
            },
            {
                "id": "#2",
                "hanzi": "大户人家的四合院通常由好几座并列组成，院落之间往往有曲折的长廊相通。院内不仅种植着玉兰与海棠，还会摆放几口大水缸饲养金鱼。关起门来，四合院就是一个自成天地的独立世界；打开院门，邻里之间推心置腹，洋溢着极其浓郁的人情味。",
                "pinyin": "Dàhù rénjiā de sìhéyuàn tōngcháng yóu hǎojǐ zuò bìngliè zǔchéng, yuànluò zhījiān wǎngwǎng yǒu qūzhé de chángláng xiāngtōng. Yuànnèi bùjǐn zhòngzhí zhe yùlán yǔ hǎitáng, hái huì bǎifàng jǐ kǒu dà shuǐgāng sìyǎng jīnyú. Guān qǐ mén lái, sìhéyuàn jiùshì yí ge zìchéng-tiāndì de dúlì shìjiè; dǎkāi yuànmén, línlǐ zhījiān tuīxīn-zhìfù, yángyì zhe jíqí nóngyù de rénqíngwèi.",
                "en": "Wealthy siheyuan compounds comprised multiple courtyards side by side linked by winding verandas. Magnolias and crabapples flourished while ceramic vats held goldfish. Closed doors created a private haven; opened doors fostered neighborly warmth.",
                "es": "Las familias nobles alzaban varios patios yuxtapuestos enlazados por galerías. Plantaban magnolias y criaban peces de colores en tinajas. A puerta cerrada era un remanso íntimo; de par en par, emanaba una entrañable cordialidad vecinal."
            }
        ]
    },

    # 02 民居
    {
        "id": "2",
        "hanzi": "民居",
        "pinyin": "mín jū",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "civilian dwelling; traditional vernacular residence",
            "es": "vivienda vernácula; residencia tradicional; morada popular"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "traditional houses or residential vernacular dwellings built by ordinary people adapted to local climate and materials",
                "definition_es": "construcción habitacional tradicional civil adaptada a los usos, clima y materiales locales",
                "example_phrase": "独具地域特色的江南民居 (Jiangnan vernacular residences with distinct regional flair)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "依山傍水的皖南古民居以粉墙黛瓦和精美砖雕著称，宛如水墨画般静静坐落在青山绿水之间。",
                "pinyin": "Yīshān-bàngshuǐ de Wǎnnán gǔ mínjū yǐ fěnqiáng-dàiwǎ hé jīngměi zhuāndiāo zhùchēng, wǎnrú shuǐmòhuà bān jìngjìng zuòluò zài qīngshān-lǜshuǐ zhījiān.",
                "en": "Historic folk dwellings in southern Anhui nestled against hills and waters are famed for white walls, dark tiles, and brick carvings, resting like ink wash paintings.",
                "es": "Las casas tradicionales del sur de Anhui destacan por sus muros blancos, tejas oscuras y relieves primorosos, semejando una acuarela entre cerros y arroyos."
            },
            {
                "id": "#2",
                "hanzi": "建筑历史学者深入云贵高原考察传统民居的抗震构造，旨在为现代绿色生态建筑设计汲取宝贵灵感。",
                "pinyin": "Jiànzhù lìshǐ xuézhě shēnrù Yún-Guì gāoyuán kǎochá chuántǒng mínjū de kàngzhèn gòuzào, zhǐzài wèi xiàndài lǜsè shēngtài jiànzhù shèjì jíqǔ bǎoguì línggǎn.",
                "en": "Architectural historians traveled into the Yunnan-Guizhou plateau to investigate earthquake-resilient structures in folk dwellings, gleaning insights for green architecture.",
                "es": "Historiadores de la arquitectura exploraron las moradas tradicionales en la meseta de Yunnan-Guizhou para incorporar técnicas sismorresistentes a la ecoarquitectura."
            }
        ],
        "collocations": [
            {"hanzi": "传统民居", "en": "traditional folk residence"},
            {"hanzi": "古民居", "en": "ancient civilian dwelling"},
            {"hanzi": "特色民居", "en": "distinctive vernacular housing"},
            {"hanzi": "民居风格", "en": "vernacular architectural style"},
            {"hanzi": "民居建筑", "en": "vernacular domestic architecture"},
            {"hanzi": "保护古民居", "en": "preserve ancient folk residences"}
        ],
        "idioms": [
            {"hanzi": "安土重迁", "pinyin": "ān tǔ zhòng qiān", "meaning_en": "attached to one's native soil and reluctant to move away"},
            {"hanzi": "鳞次栉比", "pinyin": "lín cì zhì bǐ", "meaning_en": "arranged tightly like fish scales and comb teeth; dense buildings"},
            {"hanzi": "别具一格", "pinyin": "bié jù yì gé", "meaning_en": "possessing an extraordinary, unique style of one's own"},
            {"hanzi": "鸟语花香", "pinyin": "niǎo yǔ huā xiāng", "meaning_en": "birds singing and flowers fragrant; idyllic natural environment"}
        ],
        "character_decomposition": [
            {
                "character": "民",
                "pinyin": "mín",
                "meaning_en": "people; citizens; folk; civilian",
                "meaning_es": "pueblo; ciudadanos; paisano; plebe",
                "radical": "氏",
                "radical_meaning_en": "clan",
                "meaning_component": "pictograph of an eye pierced with a needle (ancient slaves/citizens)",
                "sound_component": "民 (mín)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone graph of a needle piercing an eye; originally captive labor, developing into common folk, populace, and civilians.",
                "visual_mnemonic_story_en": "Hardworking commoners and folk (民) toiling peacefully under the clan heavens.",
                "visual_mnemonic_story_es": "El pueblo laborioso y los ciudadanos comunes (民) conviviendo en paz comunitaria.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "RVP",
                "traditional": "民"
            },
            {
                "character": "居",
                "pinyin": "jū",
                "meaning_en": "dwell; reside; occupy; house",
                "meaning_es": "residir; habitar; morar; vivienda",
                "radical": "尸",
                "radical_meaning_en": "corpse / body frame",
                "meaning_component": "尸 (body seated at rest) + 古 (ancient seat / hearth)",
                "sound_component": "古 (gǔ / phonetic association)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Body frame 尸 resting on an ancient seat 古; settling down permanently to dwell in safety.",
                "visual_mnemonic_story_en": "A human body (尸) resting comfortably upon an ancient stone hearth (古): residing at home (居).",
                "visual_mnemonic_story_es": "El cuerpo humano (尸) acomodado sobre el viejo lar solariego (古): morar en el hogar (居).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "SJR",
                "traditional": "居"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The common folk (民) residing in peaceful homes (居) create vernacular folk dwellings (民居).",
            "composite_memory_hook_es": "El pueblo llano (民) morando en sus hogares ancestrales (居) da origen a la vivienda vernácula (民居).",
            "cultural_and_cognitive_roots": "Contrasts with monumental imperial or religious architecture (palaces, temples), representing bottom-up domestic wisdom.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by level high tone: 'mín jū' (35-55). Ascend smoothly on 'mín', then sustain an even high tone on 'jū'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "民", "pinyin": "mín", "meaning_en": "people; civilian", "distinction_note": "5 strokes with 氏 radical"},
                {"character": "眠", "pinyin": "mián", "meaning_en": "sleep", "distinction_note": "Eye radical 目 on left of 民"},
                {"character": "居", "pinyin": "jū", "meaning_en": "dwell; reside", "distinction_note": "Corpse 尸 over 古"},
                {"character": "据", "pinyin": "jù", "meaning_en": "according to; seize", "distinction_note": "Hand radical 扌 on left of 居"}
            ],
            "etymological_cognates": [
                {"character": "宅", "pinyin": "zhái", "gloss_en": "house; homestead"},
                {"character": "室", "pinyin": "shì", "gloss_en": "room; chamber"},
                {"character": "庐", "pinyin": "lú", "gloss_en": "thatched cottage; hut"},
                {"character": "舍", "pinyin": "shè", "gloss_en": "dwelling; lodge"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "民居 refers specifically to vernacular civilian houses and traditional residential architecture.",
            "contrasts": [
                {"id": 1, "compared_word": "民居 vs. 宫殿", "pinyin": "gōngdiàn", "analysis": "宫殿 refers exclusively to grand monumental imperial palaces, while 民居 belongs to common folk."},
                {"id": 2, "compared_word": "民居 vs. 住宅", "pinyin": "zhùzhái", "analysis": "住宅 is a neutral legal term for any residential housing or modern flat, whereas 民居 implies cultural and vernacular tradition."},
                {"id": 3, "compared_word": "民居 vs. 庙宇", "pinyin": "miàoyǔ", "analysis": "庙宇 designates sacred temples for worshipping gods, not everyday family residences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国幅员辽阔，多样的地理气候孕育了丰富多彩的传统民居样式。从陕北黄土高坡上的冬暖夏凉窑洞，到江南水乡临河筑居的吊脚楼，这些饱含民间造物智慧的传统民居，处处体现了天人合一与因地制宜的生态理念。",
                "pinyin": "Zhōngguó fúyuán-liáokuò, duōyàng de dìlǐ qìhòu yùnyù le fēngfù-duōcǎi de chuántǒng mínjū yàngshì. Cóng Shǎnběi huángtǔ gāopō shang de dōngnuǎn-xiàliáng yáodòng, dào Jiāngnán shuǐxiāng línhé zhù jū de diàojiǎolóu, zhèxiē bǎohán mínjiān zàowù zhìhuì de chuántǒng mínjū, chùchù tǐxiàn le tiānrén-héyī yǔ yīndì-zhìyí de shēngtài lǐniàn.",
                "en": "China's vast territory and varied climates birthed rich vernacular housing styles. From cave homes on Loess slopes to riverside stilt houses in water towns, these dwellings embody indigenous wisdom and harmony with nature.",
                "es": "La vasta geografía china alumbró diversas tipologías de vivienda popular. Desde las cuevas bioclimáticas de Shaanxi hasta los palafitos ribereños del sur, estas moradas populares reflejan sintonía ecológica con el medio."
            },
            {
                "id": "#2",
                "hanzi": "在华北平原广袤的大地上，四合院无疑是流传最广、最受推崇的代表性民居样式。这种建筑形式不仅与北方干燥寒冷的多风气候相契合，更凭借封闭内敛的四面房屋围合，为世代同堂的普通家族提供了遮风避雨、安居乐业的安宁天地。",
                "pinyin": "Zài Huáběi píngyuán guǎngmào de dàdì shang, sìhéyuàn wúyí shì liúchuán zuì guǎng, zuì shòu tuīchóng de dàibiǎoxìng mínjū yàngshì. Zhè zhǒng jiànzhù xíngshì bùjǐn yǔ běifāng gānzào hánlěng de duōfēng qìhòu xiāng qìhé, gèng píngjiè fēngbì nèiliǎn de sì miàn fángwū wéihé, wèi shìdài-tóngtáng de pǔtōng jiāzú tígōng le zhēfēng-bìyǔ, ānjū-lèyè de ānníng tiāndì.",
                "en": "Across North China's plains, the siheyuan is the most celebrated vernacular dwelling. Well-suited to the cold, windy climate, its inward-facing perimeter provided multi-generational families with shelter and tranquil harmony.",
                "es": "En la llanura septentrional, el siheyuan es la morada vernácula cumbre. Adaptado al frío y al viento seco, su diseño recogido brindó cobijo y armonía a sucesivas generaciones bajo un mismo techo."
            }
        ]
    },

    # 03 组合
    {
        "id": "3",
        "hanzi": "组合",
        "pinyin": "zǔ hé",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to combine; assemble; composite; combination",
            "es": "combinar; asociar; integrar; combinación; conjunto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to unite or bring together distinct components, persons, or groups into a coherent whole",
                "definition_es": "unir o enlazar elementos, personas o piezas diversas para formar un todo estructurado",
                "example_phrase": "自由组合成学习小组 (combine freely into study groups)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a combination, composite arrangement, or musical group",
                "definition_es": "conjunto estructurado de partes o agrupación artística",
                "example_phrase": "经典的沙发家具组合 (a classic sofa furniture combination set)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这套组合音响设备不仅音质清澈饱满，还支持多种无线传输协议，深受年轻音乐爱好者的青睐。",
                "pinyin": "Zhè tào zǔhé yīnxiǎng shèbèi bùjǐn yīnzhì qīngchè bǎomǎn, hái zhīchí duō zhǒng wúxiàn chuánshū xiéyì, shēn shòu niánqīng yīnyuè àihàozhě de qīnglài.",
                "en": "This modular audio system not only delivers rich sound, but supports multiple wireless protocols, earning high praise from young music buffs.",
                "es": "Este equipo de sonido modular no sólo ofrece fidelidad acústica, sino conectividad inalámbrica, cautivando a los jóvenes melómanos."
            },
            {
                "id": "#2",
                "hanzi": "大型建筑师团队将传统榫卯木构件与现代高强度碳纤维巧妙组合，打造出了具有东方美学的展馆顶棚。",
                "pinyin": "Dàxíng jiànzhùshī tuánduì jiāng chuántǒng sǔnmǎo mù gòujiàn yǔ xiàndài gāo qiángdù tànxiānwéi qiǎomiào zǔhé, dǎzào chū le jùyǒu dōngfāng měixué de zhǎnguǎn dǐngpéng.",
                "en": "Architects ingeniously combined traditional mortise-and-tenon timber with modern carbon fiber, crafting an exhibition canopy brimming with Oriental aesthetics.",
                "es": "Los arquitectos combinaron ensambles clásicos de madera con fibra de carbono, creando una cubierta que destila elegancia oriental."
            }
        ],
        "collocations": [
            {"hanzi": "组合家具", "en": "modular / sectional furniture"},
            {"hanzi": "强强组合", "en": "combination of powerhouses"},
            {"hanzi": "音乐组合", "en": "musical band / vocal group"},
            {"hanzi": "自由组合", "en": "combine freely"},
            {"hanzi": "有机组合", "en": "organic combination / integration"},
            {"hanzi": "重组", "en": "restructure; reorganize"}
        ],
        "idioms": [
            {"hanzi": "珠联璧合", "pinyin": "zhū lián bì hé", "meaning_en": "strings of pearls and linked jade; exquisite match of talents"},
            {"hanzi": "相得益彰", "pinyin": "xiāng dé yì zhāng", "meaning_en": "bring out the best in each other; mutual enhancement"},
            {"hanzi": "巧夺天工", "pinyin": "qiǎo duó tiān gōng", "meaning_en": "superb craftsmanship outdoing nature"},
            {"hanzi": "水乳交融", "pinyin": "shuǐ rǔ jiāo róng", "meaning_en": "blended like water and milk; deeply integrated"}
        ],
        "character_decomposition": [
            {
                "character": "组",
                "pinyin": "zǔ",
                "meaning_en": "group; organize; braided silk cord",
                "meaning_es": "grupo; organizar; cordón de seda",
                "radical": "纟",
                "radical_meaning_en": "silk thread",
                "meaning_component": "纟 (woven silk filaments) + 且 (ancestral altar / foundation)",
                "sound_component": "且 (qiě / phonetic association)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk radical 纟 beside 且; braiding strands of silk together to form ornamental sashes or cords; organizing parts into teams.",
                "visual_mnemonic_story_en": "Braiding separate strands of silk thread (纟) into a strong ceremonial cord (且): forming a group (组).",
                "visual_mnemonic_story_es": "Trenzar hebras sueltas de seda (纟) en un cordel firme (且): formar un grupo o conjunto (组).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "VFBM",
                "traditional": "組"
            },
            {
                "character": "合",
                "pinyin": "hé",
                "meaning_en": "join; close; fit together",
                "meaning_es": "unir; juntar; encajar",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "人 (roof / covering lid) + 一 + 口 (box container)",
                "sound_component": "合 (hé)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Lid 人 fitting over box 口; seamless convergence and closing together into a single whole.",
                "visual_mnemonic_story_en": "Fitting a snug lid (人) onto a square box container (口) so they join seamlessly (合).",
                "visual_mnemonic_story_es": "Ajustar una tapadera (人) sobre una caja (口) para que encajen a la perfección (合).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OMR",
                "traditional": "合"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Braiding parts together like silk strands (组) and fitting them snugly (合) forms an assembled combination (组合).",
            "composite_memory_hook_es": "Trenzar piezas sueltas (组) y ensamblarlas con ajuste perfecto (合) da lugar a una combinación sólida (组合).",
            "cultural_and_cognitive_roots": "Derived from classical silk weaving and joinery carpentry where composite structures gain strength exceeding single elements.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by rising second tone: 'zǔ hé' (214-35). Dip low on 'zǔ' and soar smoothly on 'hé'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "组", "pinyin": "zǔ", "meaning_en": "group; form", "distinction_note": "Silk radical 纟 with 且"},
                {"character": "阻", "pinyin": "zǔ", "meaning_en": "block; hinder", "distinction_note": "Mound radical 阝 on left of 且"},
                {"character": "粗", "pinyin": "cū", "meaning_en": "coarse; rough", "distinction_note": "Rice radical 米 on left of 且"},
                {"character": "租", "pinyin": "zū", "meaning_en": "rent; lease", "distinction_note": "Grain radical 禾 on left of 且"}
            ],
            "etymological_cognates": [
                {"character": "编", "pinyin": "biān", "gloss_en": "weave; compile"},
                {"character": "排", "pinyin": "pái", "gloss_en": "align; arrange"},
                {"character": "结", "pinyin": "jié", "gloss_en": "tie knot; bind"},
                {"character": "集", "pinyin": "jí", "gloss_en": "gather; collect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "组合 emphasizes assembling diverse, distinct parts into a harmonious functional set or team.",
            "contrasts": [
                {"id": 1, "compared_word": "组合 vs. 配合", "pinyin": "pèihé", "analysis": "配合 focuses on cooperative coordination between teammates in dynamic action (配合默契), while 组合 denotes structural grouping."},
                {"id": 2, "compared_word": "组合 vs. 集合", "pinyin": "jíhé", "analysis": "集合 means rallying individuals to gather at a physical location (操场集合), whereas 组合 is configuring elements into an organized whole."},
                {"id": 3, "compared_word": "组合 vs. 合并", "pinyin": "hébìng", "analysis": "合并 involves merging two separate entities into one single legal or physical body, eliminating their distinct identities."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "现代企业在组建跨学科攻关团队时，非常注重不同专业背景人才的科学组合。将具有前瞻视野的战略规划师与脚踏实地的软件工程师有机组合在一起，能够碰撞出思维的灵感火花，催生出颠覆性的前沿科技成果。",
                "pinyin": "Xiàndài qǐyè zài zǔjiàn kuà-xuékē gōngguān tuánduì shí, fēicháng zhùzhòng bùtóng zhuānyè bèijǐng réncái de kēxué zǔhé. Jiāng jùyǒu qiánzhān shìyě de zhànlüè guīhuàshī yǔ jiǎotà-shídì de ruǎnjiàn gōngchéngshī yǒujī zǔhé zài yìqǐ, nénggòu pèngzhuàng chū sīwéi de línggǎn huǒhuā, cuīshēng chū diānfùxìng de qiányán kējì chéngguǒ.",
                "en": "Modern enterprises building interdisciplinary teams focus on blending diverse talents. Pairing visionary strategists with pragmatic software engineers sparks creative inspiration, yielding disruptive innovations.",
                "es": "Las empresas que crean equipos interdisciplinares buscan combinar talentos diversos. Reunir a estrategas visionarios con ingenieros prácticos detona chispas creativas, alumbrando hallazgos revolucionarios."
            },
            {
                "id": "#2",
                "hanzi": "四合院正是华北民居中一种精巧绝伦的组合建筑形式。正房、东西厢房以及倒座房等单体建筑并列排布，通过回廊有机组合在一起。大户人家的四合院更是由多座院落纵横并列组合而成，展现了中国传统建筑聚散有度的非凡智慧。",
                "pinyin": "Sìhéyuàn zhèng shì Huáběi mínjū zhōng yì zhǒng jīngqiǎo-juélún de zǔhé jiànzhù xíngshì. Zhèngfáng, dōngxī xiāngfáng yǐjí dàozuòfáng děng dāntǐ jiànzhù bìngliè páibù, tōngguò huíláng yǒujī zǔhé zài yìqǐ. Dàhù rénjiā de sìhéyuàn gèng shì yóu duō zuò yuànluò zònghéng bìngliè zǔhé ér chéng, zhǎnxiàn le Zhōngguó chuántǒng jiànzhù jùsàn-yǒudù de fēifán zhìhuì.",
                "en": "The siheyuan is an exquisite composite architectural form. Master rooms, side wings, and southern halls align, linked by verandas. In wealthy homes, multiple courtyards combine in series, displaying classic architectural mastery.",
                "es": "El siheyuan es una ingeniosa estructura habitacional combinada. La sala principal, las alas laterales y estancias frontales se integran mediante galerías. En casas nobles, varios patios se yuxtaponen con sublime destreza."
            }
        ]
    },

    # 04 建筑
    {
        "id": "4",
        "hanzi": "建筑",
        "pinyin": "jiàn zhù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "building; architecture; to construct; to erect",
            "es": "edificio; arquitectura; construir; edificar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a building, structure, or physical edifice erected on land",
                "definition_es": "edificio, estructura o inmueble construido sobre el terreno",
                "example_phrase": "风格独特的古代木质建筑 (ancient wooden buildings of unique style)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to build, construct, or engineer edifices or structures",
                "definition_es": "diseñar, erigir o levantar construcciones arquitectónicas",
                "example_phrase": "建筑防洪大坝 (construct a flood-control dam)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "漫步在万国建筑博览群的外滩沿岸，一幢幢巍峨耸立的欧式石砌建筑见证了上海百年的沧桑变迁。",
                "pinyin": "Mànbù zài wànguó jiànzhù bólǎnqún de Wàitān yán'àn, yí zhuàngzhuàng wēi'é sǒnglì de Ōushì shíqì jiànzhù jiànzhèng le Shànghǎi bǎinián de cāngsāng biànqiān.",
                "en": "Strolling along the Bund with its multinational architectural expo, towering European-style stone buildings bear witness to Shanghai's century of changes.",
                "es": "Paseando por el Bund frente a edificios de estilo europeo, las construcciones de piedra atestiguan un siglo de transformaciones en Shanghái."
            },
            {
                "id": "#2",
                "hanzi": "现代建筑设计师越来越注重节能环保与低碳技术的应用，力争让每一座新建大楼都与城市自然生态融为一体。",
                "pinyin": "Xiàndài jiànzhù shèjìshī yuèláiyuè zhùzhòng jiénéng huánbǎo yǔ dītàn jìshù de yìngyòng, lìzhēng ràng měi yí zuò xīnjiàn dàlóu dōu yǔ chéngshì zìrán shēngtài róng wéi yītǐ.",
                "en": "Modern architects place increasing emphasis on eco-friendly efficiency and low-carbon tech, striving to harmonize every new tower with urban ecology.",
                "es": "Los arquitectos priorizan la eficiencia ecológica y tecnologías bajas en carbono, buscando integrar cada nuevo rascacielos en el ecosistema urbano."
            }
        ],
        "collocations": [
            {"hanzi": "传统建筑", "en": "traditional architecture / building"},
            {"hanzi": "标志性建筑", "en": "iconic landmark building"},
            {"hanzi": "建筑工人", "en": "construction worker"},
            {"hanzi": "建筑风格", "en": "architectural style"},
            {"hanzi": "建筑材料", "en": "building materials"},
            {"hanzi": "古代建筑", "en": "ancient architecture"}
        ],
        "idioms": [
            {"hanzi": "高楼大厦", "pinyin": "gāo lóu dà shà", "meaning_en": "high-rise skyscrapers and towering mansions"},
            {"hanzi": "琼楼玉宇", "pinyin": "qióng lóu yù yǔ", "meaning_en": "jeweled towers and jade palaces; fairy-tale architecture"},
            {"hanzi": "鳞次栉比", "pinyin": "lín cì zhì bǐ", "meaning_en": "buildings standing in close proximity like fish scales"},
            {"hanzi": "土木形骸", "pinyin": "tǔ mù xíng hái", "meaning_en": "unpretentious like wood and earth; natural simplicity"}
        ],
        "character_decomposition": [
            {
                "character": "建",
                "pinyin": "jiàn",
                "meaning_en": "build; establish; erect; set up",
                "meaning_es": "construir; fundar; erigir; establecer",
                "radical": "廴",
                "radical_meaning_en": "long stride",
                "meaning_component": "廴 (stride forward on long road) + 聿 (hand holding writing brush / measuring compass)",
                "sound_component": "聿 (yù / setting rules)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Hand holding surveying stylus 聿 marching forward 廴 to lay down city foundations; establishing constitutions or buildings.",
                "visual_mnemonic_story_en": "A surveyor striding forward (廴) with measuring compass (聿) to lay foundation stones for a new city (建).",
                "visual_mnemonic_story_es": "Un perito avanzando a paso firme (廴) con su compás (聿) para trazar los cimientos de la urbe (建).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NKLQ",
                "traditional": "建"
            },
            {
                "character": "筑",
                "pinyin": "zhù",
                "meaning_en": "build; ram earth; ancient zither",
                "meaning_es": "edificar; apisonar tierra; laúd antiguo",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo rammers/scaffolding) + 巩 (firm binding with craft 工 and 凡)",
                "sound_component": "巩 (gǒng / phonetic connection)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Bamboo radical 竹 atop 巩 (firm foundation); pounding tamped earth (夯土) walls between wooden planks with heavy rammers.",
                "visual_mnemonic_story_en": "Heavy bamboo pestles (竹) pounding layers of earth firmly (巩) into rammed earth walls (筑).",
                "visual_mnemonic_story_es": "Maderos y varas de bambú (竹) apisonando tierra con firmeza (巩) para alzar murallas macizas (筑).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HHVN",
                "traditional": "築"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Laying out foundations (建) and ramming earth walls with bamboo poles (筑) accomplishes architecture (建筑).",
            "composite_memory_hook_es": "Trazar los planos (建) y apisonar la tierra con pértigas de bambú (筑) define la arquitectura (建筑).",
            "cultural_and_cognitive_roots": "Rammed earth (夯土) and mortise-and-tenon timber form the twin pillars of historic Chinese construction culture.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'jiàn zhù' (51-51). Deliver two decisive downward cadences with strength."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "建", "pinyin": "jiàn", "meaning_en": "build; erect", "distinction_note": "Has long stride radical 廴 with 聿"},
                {"character": "健", "pinyin": "jiàn", "meaning_en": "healthy; robust", "distinction_note": "Person radical 亻 on left of 建"},
                {"character": "筑", "pinyin": "zhù", "meaning_en": "build; zither", "distinction_note": "Bamboo radical 竹 on top of 巩"},
                {"character": "恐", "pinyin": "kǒng", "meaning_en": "fear; dread", "distinction_note": "Heart radical 心 under 巩"}
            ],
            "etymological_cognates": [
                {"character": "造", "pinyin": "zào", "gloss_en": "create; manufacture"},
                {"character": "搭", "pinyin": "dā", "gloss_en": "erect; put up scaffolding"},
                {"character": "修", "pinyin": "xiū", "gloss_en": "repair; construct"},
                {"character": "立", "pinyin": "lì", "gloss_en": "stand; erect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "建筑 encompasses architectural engineering, buildings, and the physical act of construction.",
            "contrasts": [
                {"id": 1, "compared_word": "建筑 vs. 房屋", "pinyin": "fángwū", "analysis": "房屋 refers concretely to residential houses or rooms for living, while 建筑 covers towers, bridges, dams, monuments, and architecture as an art."},
                {"id": 2, "compared_word": "建筑 vs. 施工", "pinyin": "shīgōng", "analysis": "施工 denotes the operational frontline labor process of carrying out engineering blueprints, whereas 建筑 is broader design and discipline."},
                {"id": 3, "compared_word": "建筑 vs. 大厦", "pinyin": "dàshà", "analysis": "大厦 refers specifically to towering multi-story commercial office towers or grand mansions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统木构建筑以神奇的榫卯节点著称，通体不用一钉一铆，却能历经千年风雨侵蚀与剧烈地震考验而巍然屹立。山西应县木塔便是这一建筑奇迹的典范，完美彰显了古代华夏匠人登峰造极的结构力学智慧。",
                "pinyin": "Zhōngguó chuántǒng mùgòu jiànzhù yǐ shénqí de sǔnmǎo jiédiǎn zhùchēng, tōngtǐ bù yòng yì dīng yì mǎo, què néng lìjīng qiānnián fēngyǔ qīnshí yǔ jùliè dìzhèn kǎoyàn ér wēirán-yìlì. Shānxī Yìngxiàn mùtǎ biàn shì zhè yí jiànzhù qíjì de diǎnfàn, wánměi zhāngxiǎn le gǔdài Huàxià jiàngrén dēngfēng-zàojí de jiégòu lìxué zhìhuì.",
                "en": "Traditional Chinese wooden architecture is famed for ingenious mortise-and-tenon joints, enduring centuries of weathering and quakes without nails. The Yingxian Pagoda stands as an exemplar, showcasing peak structural mechanics.",
                "es": "La arquitectura tradicional china en madera brilla por sus ensambles sin clavos, soportando terremotos durante siglos. La Pagoda de Yingxian es muestra cumbre del dominio mecánico de los maestros constructores."
            },
            {
                "id": "#2",
                "hanzi": "四合院不仅是华北平原最具代表性的民居建筑形式，更是一部镌刻在青砖灰瓦间的家族伦理文化史。四合院由正房、厢房和倒座房等单体建筑围合而成，严谨对称的建筑格局，深刻映照出中国传统社会长幼有序、内外有别的宗法礼乐规范。",
                "pinyin": "Sìhéyuàn bùjǐn shì Huáběi píngyuán zuì jù dàibiǎoxìng de mínjū jiànzhù xíngshì, gèng shì yí bù juānkè zài qīngzhuān-huīwǎ jiān de jiāzú lúnlǐ wénhuà shǐ. Sìhéyuàn yóu zhèngfáng, xiāngfáng hé dàozuòfáng děng dāntǐ jiànzhù wéihé ér chéng, yánjǐn duìchèn de jiànzhù géjú, shēnkè yìngzhào chū Zhōngguó chuántǒng shèhuì zhǎngyòu-yǒuxù, nèiwài-yǒubié de zōngfǎ lǐyuè guīfàn.",
                "en": "The siheyuan is not only North China's signature vernacular architecture, but a clan history engraved in bricks. Arranging master halls and wings around a courtyard, its symmetrical layout mirrors traditional patriarchal ethics.",
                "es": "El siheyuan no es sólo la morada vernácula cumbre del norte, sino un compendio de ética familiar grabado en ladrillos. Su rigurosa simetría refleja los cánones confucianos de jerarquía y decoro doméstico."
            }
        ]
    },

    # 05 形式
    {
        "id": "5",
        "hanzi": "形式",
        "pinyin": "xíng shì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "form; mode; shape; formality; format",
            "es": "forma; modalidad; formato; apariencia exterior; formalidad"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the outward shape, structural mode, or organizational manifestation of an entity as opposed to its content",
                "definition_es": "modo o estructura exterior en que se manifiesta una cosa, en oposición a su contenido",
                "example_phrase": "采取多种多样的组织形式 (adopt diverse organizational forms)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "优秀的艺术作品应当实现思想内容与艺术形式的高度统一，切不可为了盲目追求炫目的外在技巧而牺牲作品灵魂。",
                "pinyin": "Yōuxiù de yìshù zuòpǐn yīngdāng shíxiàn sīxiǎng nèiróng yǔ yìshù xíngshì de gāodù tǒngyī, qiè bùkě wèile mángmù zhuīqiú xuànmù de wàizài jìqiǎo ér xīshēng zuòpǐn línghún.",
                "en": "Masterpieces must achieve sublime unity between ideological content and artistic form, never sacrificing soul for dazzling outward technique.",
                "es": "Una gran obra artística debe aunar armónicamente fondo y forma, sin sacrificar jamás el alma de la creación en pos de fuegos de artificio técnicos."
            },
            {
                "id": "#2",
                "hanzi": "不少所谓的节日促销活动往往只是流于形式，商家口头承诺的优惠打折并不能真正让普通消费者获得实惠。",
                "pinyin": "Bùshǎo suǒwèi de jiérì cùxiāo huódòng wǎngwǎng zhǐshì liú yú xíngshì, shāngjiā kǒutóu chéngnuò de yōuhuì dǎzhé bìng bùnéng zhēnzhèng ràng pǔtōng xiāofèizhě huòdé shíhuì.",
                "en": "Many so-called holiday promotions are mere formalities; verbal discounts promised by merchants rarely provide genuine benefits to consumers.",
                "es": "Muchas rebajas festivas se quedan en mera formalidad; los descuentos prometidos por los comerciantes rara vez aportan un ahorro real."
            }
        ],
        "collocations": [
            {"hanzi": "表现形式", "en": "form of expression / manifestation"},
            {"hanzi": "形式多样", "en": "diverse in forms"},
            {"hanzi": "流于形式", "en": "become a mere formality"},
            {"hanzi": "走形式", "en": "go through the motions"},
            {"hanzi": "组织形式", "en": "organizational structure / form"},
            {"hanzi": "艺术形式", "en": "artistic form / medium"}
        ],
        "idioms": [
            {"hanzi": "形式主义", "pinyin": "xíng shì zhǔ yì", "meaning_en": "formalism; superficial adherence to rules"},
            {"hanzi": "名存实亡", "pinyin": "míng cún shí wáng", "meaning_en": "exist in name only; hollow shell"},
            {"hanzi": "形神兼备", "pinyin": "xíng shén jiān bèi", "meaning_en": "possessing both accurate form and vibrant spirit"},
            {"hanzi": "千姿百态", "pinyin": "qiān zī bǎi tài", "meaning_en": "in thousands of postures and poses; endless varieties"}
        ],
        "character_decomposition": [
            {
                "character": "形",
                "pinyin": "xíng",
                "meaning_en": "shape; form; appearance; body",
                "meaning_es": "forma; figura; cuerpo; manifestar",
                "radical": "彡",
                "radical_meaning_en": "bristle / hair",
                "meaning_component": "开 / 井 (framing lattice) + 彡 (strokes of beauty / contour)",
                "sound_component": "井 / 开 (phonetic association)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A framing lattice 开 decorated with hair strokes 彡; visible contours, bodily shapes, and outward silhouettes.",
                "visual_mnemonic_story_en": "Drawing contour brushstrokes (彡) over a framing grid to outline an elegant physical form (形).",
                "visual_mnemonic_story_es": "Trazar pinceladas de contorno (彡) sobre una cuadrícula para plasmar una figura visible (形).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MTHHH",
                "traditional": "形"
            },
            {
                "character": "式",
                "pinyin": "shì",
                "meaning_en": "type; pattern; style; ceremony; formula",
                "meaning_es": "modelo; estilo; ceremonia; fórmula",
                "radical": "弋",
                "radical_meaning_en": "shoot arrow / stake",
                "meaning_component": "弋 (arrow stake marker) + 工 (carpenter's square / craft)",
                "sound_component": "弋 (yì / phonetic link)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Carpenter's square 工 affixed to an arrow stake 弋; an officially approved template, formula, or ceremonial standard.",
                "visual_mnemonic_story_en": "A carpenter aligning his tool (工) against an upright reference post (弋) to set a standard pattern (式).",
                "visual_mnemonic_story_es": "El artesano calibrando su escuadra (工) con una estaca patrón (弋) para fijar el modelo normativo (式).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IPMO",
                "traditional": "式"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Visible outward shape (形) modeled on a standard structural pattern (式) determines its form (形式).",
            "composite_memory_hook_es": "La figura externa visible (形) ajustada a un patrón normativo (式) constituye la forma (形式).",
            "cultural_and_cognitive_roots": "Central philosophical polarity in Chinese literary theory: the dialectic between 'Content' (内容) and 'Form' (形式).",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'xíng shì' (35-51). Lift upwards on 'xíng', then drop firmly on 'shì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "形", "pinyin": "xíng", "meaning_en": "form; shape", "distinction_note": "Has 彡 (three slants) on the right"},
                {"character": "刑", "pinyin": "xíng", "meaning_en": "punishment; criminal", "distinction_note": "Has knife radical 刂 on the right"},
                {"character": "式", "pinyin": "shì", "meaning_en": "pattern; ceremony", "distinction_note": "Has 工 inside 弋 without extra dots"},
                {"character": "戒", "pinyin": "jiè", "meaning_en": "quit; warn", "distinction_note": "Has 廾 inside 弋"}
            ],
            "etymological_cognates": [
                {"character": "态", "pinyin": "tài", "gloss_en": "attitude; posture"},
                {"character": "貌", "pinyin": "mào", "gloss_en": "appearance; feature"},
                {"character": "样", "pinyin": "yàng", "gloss_en": "appearance; model"},
                {"character": "格", "pinyin": "gé", "gloss_en": "pattern; lattice"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "形式 denotes the structural mode, format, or outward presentation framework.",
            "contrasts": [
                {"id": 1, "compared_word": "形式 vs. 内容", "pinyin": "nèiróng", "analysis": "内容 is the core substantive message or material inside, while 形式 is the external structural vehicle conveying it."},
                {"id": 2, "compared_word": "形式 vs. 形状", "pinyin": "xíngzhuàng", "analysis": "形状 refers strictly to geometric contour (round, square, triangular), whereas 形式 describes systemic and institutional modes."},
                {"id": 3, "compared_word": "形式 vs. 仪式", "pinyin": "yíshì", "analysis": "仪式 specifically denotes ceremonial solemn rites (wedding ceremony, coronation), a specialized ritual subtype."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代艺术创作中，艺术家们不断探索突破传统媒介形式的崭新可能。从架上绘画延伸到沉浸式数字光影互动，艺术的表现形式虽然历经沧桑巨变，但其核心所承载的人文关怀与对真善美的永恒追寻，却始终历久弥新。",
                "pinyin": "Zài xiàndài yìshù chuàngzuò zhōng, yìshùjiāmen búduàn tànsuǒ tūpò chuántǒng méijiè xíngshì de zhǎnxīn kěnéng. Cóng jiàshàng huìhuà yánshēn dào chénjìnsì shùzì guāngyǐng hùdòng, yìshù de biǎoxiàn xíngshì suīrán lìjīng cāngsāng jùbiàn, dàn qí héxīn suǒ chéngzài de rénwén guānhuái yǔ duì zhēn-shàn-měi de yǒnghéng zhuīxún, què shǐzhōng lìjiǔ-míxīn.",
                "en": "In contemporary art, creators constantly explore new possibilities breaking classical formats. From canvas paintings to digital light projections, while artistic forms transform, the pursuit of truth, goodness, and beauty remains eternal.",
                "es": "En el arte actual, los creadores trascienden formatos clásicos. Del lienzo a las instalaciones lumínicas digitales, aunque la forma de expresión mute, el anhelo humanista de verdad y belleza pervive intacto."
            },
            {
                "id": "#2",
                "hanzi": "四合院是中国传统民居建筑中最具生命力的经典组合形式。四合院由正房、倒座房及东西厢房在四面围合而成，这种形式既有效阻挡了北方的早春风沙与冬季严寒，又在院落中央为家人留出了栽花种草、享受天伦之乐的露天生活空间。",
                "pinyin": "Sìhéyuàn shì Zhōngguó chuántǒng mínjū jiànzhù zhōng zuì jù shēngmìnglì de jīngdiǎn zǔhé xíngshì. Sìhéyuàn yóu zhèngfáng, dàozuòfáng jí dōngxī xiāngfáng zài sì miàn wéihé ér chéng, zhè zhǒng xíngshì jì yǒuxiào zǔdǎng le běifāng de zǎochūn fēngshā yǔ dōngjì yánhán, yòu zài yuànluò zhōngyāng wèi jiārén liú chū le zāihuā-zhòngcǎo, xiǎngshòu tiānlúnzhīlè de lùtiān shēnghuó kōngjiān.",
                "en": "The siheyuan is the most vital composite form in traditional Chinese housing. Enclosed on four sides by halls and wings, this format blocks cold desert winds while securing a private open garden courtyard for clan communion.",
                "es": "El siheyuan es la forma arquitectónica combinada más señera de China. Rodeado por cuatro alas, este modelo aísla de ventiscas y polvo, reservando un patio al aire libre para disfrutar de la dicha familiar."
            }
        ]
    },

    # 06 所谓
    {
        "id": "6",
        "hanzi": "所谓",
        "pinyin": "suǒ wèi",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "so-called; what is called; what is known as",
            "es": "el llamado; lo que se conoce como; el presunto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "what is meant by or commonly called; explaining terminology",
                "definition_es": "lo que comúnmente se denomina o entiende por tal concepto",
                "example_phrase": "所谓四合，即四面房屋围在一起 (the so-called 'four-join' means houses on four sides)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "so-called (used skeptically or disapprovingly to denote false claims)",
                "definition_es": "presunto o supuesto con matiz escéptico o irónico",
                "example_phrase": "别相信那些所谓专家的养生秘诀 (don't trust those so-called experts' secrets)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "所谓四合院，‘四’指东、西、南、北四面，‘合’则是四面房屋围在一起，形成封闭的方形院落。",
                "pinyin": "Suǒwèi sìhéyuàn, 'sì' zhǐ dōng, xī, nán, běi sì miàn, 'hé' zé shì sì miàn fángwū wéi zài yìqǐ, xíngchéng fēngbì de fāngxíng yuànluò.",
                "en": "As for the so-called siheyuan, 'four' signifies the four directions, while 'join' means enclosing houses on four sides into a private square courtyard.",
                "es": "En el llamado siheyuan, 'cuatro' alude a los cuatro puntos cardinales y 'juntar' describe cuatro pabellones abrazando un patio cuadrado íntimo."
            },
            {
                "id": "#2",
                "hanzi": "消费者应当保持理性清醒，切勿轻信网络上那些未经权威科学认证的所谓‘抗衰老神药’。",
                "pinyin": "Xiāofèizhě yīngdāng bǎochí lǐxìng qīngxǐng, qièwù qīngxìn wǎngluò shang nàxiē wèijīng quánwēi kēxué rènzhèng de suǒwèi 'kàng shuāilǎo shényào'.",
                "en": "Consumers should stay rational and avoid falling for uncertified 'anti-aging miracles' touted by so-called medical gurus online.",
                "es": "Los consumidores deben mantener la cautela y desconfiar de los supuestos 'remedios milagrosos antiedad' que proliferan en internet sin aval científico."
            }
        ],
        "collocations": [
            {"hanzi": "所谓四合", "en": "the so-called four-join"},
            {"hanzi": "所谓专家", "en": "so-called experts"},
            {"hanzi": "所谓的成功", "en": "so-called success"},
            {"hanzi": "无所谓", "en": "doesn't matter; indifferent"},
            {"hanzi": "所谓何事", "en": "what is this concerning (formal)"},
            {"hanzi": "所谓事实", "en": "the alleged facts"}
        ],
        "idioms": [
            {"hanzi": "顾名思义", "pinyin": "gù míng sī yì", "meaning_en": "as the name implies; self-explanatory from the name"},
            {"hanzi": "名不副实", "pinyin": "míng bù fù shí", "meaning_en": "the name does not match the reality; unworthy of the name"},
            {"hanzi": "开宗明义", "pinyin": "kāi zōng míng yì", "meaning_en": "state the primary purpose right at the beginning"},
            {"hanzi": "理所当然", "pinyin": "lǐ suǒ dāng rán", "meaning_en": "taken for granted; natural and proper as a matter of course"}
        ],
        "character_decomposition": [
            {
                "character": "所",
                "pinyin": "suǒ",
                "meaning_en": "place; particle indicating receiver of action",
                "meaning_es": "lugar; partícula que sustantiva el objeto",
                "radical": "斤",
                "radical_meaning_en": "axe",
                "meaning_component": "户 (single door) + 斤 (axe chopping timber on doorstep)",
                "sound_component": "所 (suǒ)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An axe 斤 chopping wood at a homestead door 户; originally the designated chopping spot, developing into places and passive pronoun particle.",
                "visual_mnemonic_story_en": "Setting down an axe (斤) at the wooden threshold (户) to mark an established dwelling place (所).",
                "visual_mnemonic_story_es": "Apoyar el hacha (斤) en el umbral de la puerta (户) para señalar el lugar de asiento (所).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "HSHML",
                "traditional": "所"
            },
            {
                "character": "谓",
                "pinyin": "wèi",
                "meaning_en": "say; speak of; call; meaning",
                "meaning_es": "decir; llamar; denominar; significar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken words) + 胃 (stomach / inner intent)",
                "sound_component": "胃 (wèi / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Speech radical 讠 beside stomach 胃; voicing words that express what is harbored in one's stomach/mind.",
                "visual_mnemonic_story_en": "Uttering spoken words (讠) straight from the gut (胃) to name and define a truth (谓).",
                "visual_mnemonic_story_es": "Pronunciar palabras claras (讠) que brotan de las entrañas (胃) para nombrar las cosas (谓).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IWBG",
                "traditional": "謂"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "What (所) is stated and named by spoken words (谓) defines the so-called term (所谓).",
            "composite_memory_hook_es": "Aquello (所) que se enuncia y denomina con palabras (谓) es lo que se llama (所谓).",
            "cultural_and_cognitive_roots": "Essential classical expository marker (所谓的 'what is termed...') used in academic definition and dialectical skepticism.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by falling fourth tone: 'suǒ wèi' (214-51). Dip low on 'suǒ', then descend decisively on 'wèi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "所", "pinyin": "suǒ", "meaning_en": "place; particle", "distinction_note": "Single door 户 on left of axe 斤"},
                {"character": "断", "pinyin": "duàn", "meaning_en": "snap; break", "distinction_note": "Has 米 and 乚 on left of 斤"},
                {"character": "谓", "pinyin": "wèi", "meaning_en": "call; speak", "distinction_note": "Speech radical 讠 on left of 胃"},
                {"character": "渭", "pinyin": "wèi", "meaning_en": "Wei River", "distinction_note": "Water radical 氵 on left of 胃"}
            ],
            "etymological_cognates": [
                {"character": "称", "pinyin": "chēng", "gloss_en": "weigh; call; praise"},
                {"character": "名", "pinyin": "míng", "gloss_en": "name; term; famous"},
                {"character": "号", "pinyin": "hào", "gloss_en": "call; name; mark"},
                {"character": "指", "pinyin": "zhǐ", "gloss_en": "point; refer to"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "所谓 introduces an explicit definition of a concept or expresses ironic skepticism toward a label.",
            "contrasts": [
                {"id": 1, "compared_word": "所谓 vs. 名义", "pinyin": "míngyì", "analysis": "名义 is a noun meaning titular capacity or pretext (以朋友的名义), while 所谓 is a modifier explaining definitions or questioning authenticity."},
                {"id": 2, "compared_word": "所谓 vs. 据说", "pinyin": "jùshuō", "analysis": "据说 introduces reported hearsay from outside sources (据说要下雨), while 所谓 defines terminology or questions validity."},
                {"id": 3, "compared_word": "所谓 vs. 称作", "pinyin": "chēngzuò", "analysis": "称作 is a transitive predicate verb meaning 'to be called' (这种鸟被称作翠鸟), while 所谓 is an attributive modifier."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "探寻传统建筑之美，必须先理解其造字立意的文化源头。所谓四合，‘四’指东、西、南、北四面房屋，‘合’则是四面房屋围合在一起。这简简单单的两个汉字，生动凝练地勾勒出了北方民居中正平和的审美意境。",
                "pinyin": "Tànxún chuántǒng jiànzhù zhī měi, bìxū xiān lǐjiě qí zàozì lìyì de wénhuà yuántóu. Suǒwèi sìhé, 'sì' zhǐ dōng, xī, nán, běi sì miàn fángwū, 'hé' zé shì sì miàn fángwū wéihé zài yìqǐ. Zhè jiǎnjiǎn-dāndān de liǎng ge Hànzì, shēngdòng níngliàn de gōulè chū le běifāng mínjū zhōngzhèng-pínghé de shěnměi yìjìng.",
                "en": "Exploring the beauty of architecture requires understanding cultural etymology. The 'four-join' implies buildings on four sides enclosing a yard. These two characters sketch the harmonious aesthetic core of northern vernacular homes.",
                "es": "Para apreciar la arquitectura tradicional conviene desentrañar sus raíces léxicas. Lo de 'cuatro juntas' define pabellones en los cuatro rumbos cerrándose en torno al patio, compendiando la serena armonía solariega."
            },
            {
                "id": "#2",
                "hanzi": "在快节奏的商业炒作中，不少打着所谓‘传统古建’旗号的新建仿古街区，由于过度追求商业利益而丧失了原汁原味的民俗烟火气。真正值得我们倍加珍视的，从来不是冰冷的水泥仿品，而是老北京四合院里世代相传的质朴温情。",
                "pinyin": "Zài kuài jiézòu de shāngyè chǎozuò zhōng, bùshǎo dǎ zhe suǒwèi 'chuántǒng gǔjiàn' qíhào de xīnjiàn fǎnggǔ jiēqū, yóuyú guòdù zhuīqiú shāngyè lìyì ér sàngshī le yuánzhī-yuánwèi de mínsú yānhuǒqì. Zhēnzhèng zhíde wǒmen bèijiā zhēnshì de, cónglái búshì bīnglěng de shuǐní fǎngpǐn, érshì lǎo Běijīng sìhéyuàn lǐ shìdài-xiāngchuán de zhípǔ wēnqíng.",
                "en": "Amid commercial hype, many new pedestrian streets under so-called 'heritage' banners forfeit authentic community life in greed. What deserves cherishing is never cold concrete facsimiles, but the timeless warmth preserved in old courtyards.",
                "es": "Entre el bullicio mercantil, muchos recintos que se anuncian como 'patrimonio histórico' pierden su autenticidad por el lucro. Lo que de veras vale la pena rescatar es el calor humano vivo de los patios tradicionales."
            }
        ]
    },

    # 07 方
    {
        "id": "7",
        "hanzi": "方",
        "pinyin": "fāng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "square; rectangular; upright; direction; party",
            "es": "cuadrado; recto; probo; dirección; bando"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "having four equal sides and four right angles; square or rectangular in shape",
                "definition_es": "de cuatro lados iguales y ángulos rectos; de figura cuadrada o rectangular",
                "example_phrase": "中间形成一个方形的院子 (forms a square courtyard in the middle)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "upright, honest, and morally principled in character",
                "definition_es": "recto, íntegro y firme de carácter moral",
                "example_phrase": "为人正直方正 (a person upright and scrupulously honest)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "中国古代四合院的四面房屋围合在一起，正好在中央形成一个规整方正的庭院空间。",
                "pinyin": "Zhōngguó gǔdài sìhéyuàn de sì miàn fángwū wéihé zài yìqǐ, zhènghǎo zài zhōngyāng xíngchéng yí ge guīzhěng fāngzhèng de tíngyuàn kōngjiān.",
                "en": "The houses on four sides of a traditional siheyuan enclose each other, forming a neatly square courtyard space right in the center.",
                "es": "Los pabellones a cuatro vientos del siheyuan tradicional confluyen delimitando en el centro un patio cuadrangular de gran armonía."
            },
            {
                "id": "#2",
                "hanzi": "做人应当有方有圆，既要恪守内心的原则底线，又要懂得在处世待人时保持柔和宽容。",
                "pinyin": "Zuòrén yīngdāng yǒufāng-yǒuyuán, jì yào kèshǒu nèixīn de yuánzé dǐxiàn, yòu yào dǒngde zài chǔshì dàirén shí bǎochí róuhé kuānróng.",
                "en": "In conducting oneself, one should blend square principles with circular adaptability—holding ethical baselines while remaining gentle toward others.",
                "es": "En la vida conviene aunar firmeza y flexibilidad: ser fiel a los principios morales inquebrantables, pero afable y comprensivo en el trato social."
            }
        ],
        "collocations": [
            {"hanzi": "方形", "en": "square shape"},
            {"hanzi": "四面八方", "en": "all directions; far and wide"},
            {"hanzi": "方正", "en": "square and upright; principled"},
            {"hanzi": "方向", "en": "direction; orientation"},
            {"hanzi": "方法", "en": "method; way"},
            {"hanzi": "对方", "en": "counterpart; the other side"}
        ],
        "idioms": [
            {"hanzi": "方兴未艾", "pinyin": "fāng xīng wèi ài", "meaning_en": "in the ascent and not yet peaking; rapidly growing"},
            {"hanzi": "落落大方", "pinyin": "luò luò dà fāng", "meaning_en": "poised, dignified, and natural in bearing"},
            {"hanzi": "方圆百里", "pinyin": "fāng yuán bǎi lǐ", "meaning_en": "within a radius of a hundred li; across the entire territory"},
            {"hanzi": "天圆地方", "pinyin": "tiān yuán dì fāng", "meaning_en": "round heaven and square earth; ancient cosmology"}
        ],
        "character_decomposition": [
            {
                "character": "方",
                "pinyin": "fāng",
                "meaning_en": "square; raft; direction; upright",
                "meaning_es": "cuadrado; balsa; rumbo; recto",
                "radical": "方",
                "radical_meaning_en": "square / direction",
                "meaning_component": "pictograph of two wooden ferry boats or rafts lashed side by side",
                "sound_component": "方 (fāng)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of two twin boats tied parallel to cross rivers; evolved into straight edges, squares, and spatial directions.",
                "visual_mnemonic_story_en": "Twin wooden boats lashed parallel with straight squared sides (方) to cross the waterway smoothly.",
                "visual_mnemonic_story_es": "Dos barcas de madera acopladas en paralelo con cantos rectos (方) para cruzar el río.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YHS",
                "traditional": "方"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Twin boats lashed straight (方) form four right angles and determine spatial cardinal directions (方).",
            "composite_memory_hook_es": "Dos barcazas amarradas en ángulo recto (方) evocan la rectitud del cuadrado y los rumbos (方).",
            "cultural_and_cognitive_roots": "Foundational in Chinese cosmology ('天圆地方' round sky, square earth); geometry of city planning from Chang'an to Beijing.",
            "tone_sandhi_and_pitch_modulation": "Level high tone: 'fāng' (55). Hold an even, clear high pitch without wavering."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "方", "pinyin": "fāng", "meaning_en": "square; direction", "distinction_note": "Dot, horizontal, turning hook, and sweep"},
                {"character": "万", "pinyin": "wàn", "meaning_en": "ten thousand", "distinction_note": "No top dot; horizontal line directly leads into hook"},
                {"character": "芳", "pinyin": "fāng", "meaning_en": "fragrant", "distinction_note": "Grass radical 艹 on top of 方"},
                {"character": "仿", "pinyin": "fǎng", "meaning_en": "imitate; like", "distinction_note": "Person radical 亻 on left of 方"}
            ],
            "etymological_cognates": [
                {"character": "矩", "pinyin": "jǔ", "gloss_en": "carpenter's square; rule"},
                {"character": "直", "pinyin": "zhí", "gloss_en": "straight; upright"},
                {"character": "正", "pinyin": "zhèng", "gloss_en": "proper; correct"},
                {"character": "端", "pinyin": "duān", "gloss_en": "end; upright"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "方 describes right-angled, square geometric structure as well as moral uprightness.",
            "contrasts": [
                {"id": 1, "compared_word": "方 vs. 圆", "pinyin": "yuán", "analysis": "方 denotes four-sided right-angled rigidity, while 圆 represents fluid, curved circularity without corners."},
                {"id": 2, "compared_word": "方 vs. 直", "pinyin": "zhí", "analysis": "直 means one-dimensional straightness without bends, while 方 describes a two-dimensional square shape."},
                {"id": 3, "compared_word": "方 vs. 平", "pinyin": "píng", "analysis": "平 denotes flat, level surface elevation without bumps, whereas 方 refers to planar polygon geometry."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代铜钱外圆内方，将‘天圆地方’的哲学宇宙观巧妙地熔铸于方寸金属之间。古人借这枚小小的钱币告诫后世子孙：处世当外圆内方，对外应圆融通达、谦和宽厚，对内则当心如明镜、秉持正道，坚守立身原则。",
                "pinyin": "Zhōngguó gǔdài tóngqián wàiyuán-nèifāng, jiāng 'tiānyuán-dìfāng' de zhéxué yǔzhòuguān qiǎomiào de róngzhù yú fāngcùn jīnshǔ zhījiān. Gǔrén jiè zhè méi xiǎoxiǎo de qiánbì gàojiè hòushì zǐsūn: chǔshì dāng wàiyuán-nèifāng, duìwài yīng yuánróng-tōngdá, qiānhé kuānhòu, duìnèi zé dāng xīnrú-míngjìng, bǐngchí zhèngdào, jiānshǒu lìshēn yuánzé.",
                "en": "Ancient coins had a round exterior with a square hole, embodying 'round heaven, square earth'. Sages used this design to instruct descendants: be adaptable like a circle outwardly, but unyielding and upright like a square within.",
                "es": "Las monedas clásicas chinas eran redondas con orificio cuadrado, plasmando el cosmos. Enseñaban a ser circulares por fuera en afabilidad, pero cuadrados por dentro en rectitud y fidelidad a los principios."
            },
            {
                "id": "#2",
                "hanzi": "所谓四合院，正是由东、西、南、北四面房屋围合在一起，在正中央形成一个规整方正的庭院。这种方方正正的四合院格局，不仅反映了华夏先民对秩序对称与中正之美的追求，更营造出一种安定沉稳、聚气凝神的绝佳居住环境。",
                "pinyin": "Suǒwèi sìhéyuàn, zhèng shì yóu dōng, xī, nán, běi sì miàn fángwū wéihé zài yìqǐ, zài zhèng zhōngyāng xíngchéng yí ge guīzhěng fāngzhèng de tíngyuàn. Zhè zhǒng fāngfang-zhèngzhèng de sìhéyuàn géjú, bùjǐn fǎnyìng le Huàxià xiānmín duì zhìxù duìchèn yǔ zhōngzhèng zhī měi de zhuīqiú, gèng yíngzào chū yì zhǒng āndìng chénwěn, jùqì-níngshén de juéjiā jūzhù huánjìng.",
                "en": "The siheyuan is formed by houses on four sides enclosing a neat square courtyard in the center. This squared layout reflects ancient desires for symmetry and balance, creating an oasis of stability that gathers positive vitality.",
                "es": "El siheyuan abraza un patio cuadrado en su corazón gracias a sus cuatro pabellones. Esa pulcra traza cuadrangular refleja el amor por la simetría y el orden, forjando un remanso apacible para la vida en familia."
            }
        ]
    },

    # 08 广泛
    {
        "id": "8",
        "hanzi": "广泛",
        "pinyin": "guǎng fàn",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "extensive; widespread; broad; wide-ranging",
            "es": "amplio; extenso; generalizado; de gran alcance"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "covering a large area, broad scope, or having widespread application across diverse fields",
                "definition_es": "que abarca un gran espacio, número de personas, materias o campos de aplicación",
                "example_phrase": "引起社会的广泛关注 (attract widespread social attention)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "随着新能源汽车技术的日益成熟，这种绿色低碳的出行方式正在全国各大城市得到广泛普及。",
                "pinyin": "Suízhe xīnnéngyuán qìchē jìshù de rìyì chéngshú, zhè zhǒng lǜsè dītàn de chūxíng fāngshì zhèng zài quánguó gèdà chéngshì dédào guǎngfàn pǔjí.",
                "en": "With new energy vehicle technologies maturing, this green and low-carbon travel mode is gaining widespread adoption across major cities.",
                "es": "Con el avance del coche eléctrico, este medio de transporte limpio se difunde de forma generalizada en las principales metrópolis del país."
            },
            {
                "id": "#2",
                "hanzi": "这位博学多才的大学教授不仅精通古代文献考据，还广泛涉猎天文学、心理学以及认知神经科学。",
                "pinyin": "Zhè wèi bóxué-duōcái de dàxué jiàoshòu bùjǐn jīngtōng gǔdài wénxiàn kǎojù, hái guǎngfàn shèliè tiānwénxué, xīnlǐxué yǐjí rènzhī shénjīng kēxué.",
                "en": "This erudite professor is not only versed in classical philology, but reads broadly across astronomy, psychology, and cognitive neuroscience.",
                "es": "Este sabio catedrático no sólo domina la filología clásica, sino que estudia con amplitud la astronomía, la psicología y la neurociencia cognitiva."
            }
        ],
        "collocations": [
            {"hanzi": "广泛应用", "en": "widespread application"},
            {"hanzi": "广泛关注", "en": "widespread attention"},
            {"hanzi": "广泛分布", "en": "widely distributed"},
            {"hanzi": "广泛征求意见", "en": "solicit opinions broadly"},
            {"hanzi": "兴趣广泛", "en": "broad interests"},
            {"hanzi": "广泛涉猎", "en": "read or explore extensively"}
        ],
        "idioms": [
            {"hanzi": "遍地开花", "pinyin": "biàn dì kāi huā", "meaning_en": "blossom everywhere; widespread proliferation"},
            {"hanzi": "博览群书", "pinyin": "bó lǎn qún shū", "meaning_en": "read widely across all volumes; well-read scholar"},
            {"hanzi": "见多识广", "pinyin": "jiàn duō shí guǎng", "meaning_en": "experienced and knowledgeable with wide horizons"},
            {"hanzi": "举世皆知", "pinyin": "jǔ shì jiē zhī", "meaning_en": "known universally across the entire world"}
        ],
        "character_decomposition": [
            {
                "character": "广",
                "pinyin": "guǎng",
                "meaning_en": "broad; wide; vast; spacious",
                "meaning_es": "ancho; amplio; vasto",
                "radical": "广",
                "radical_meaning_en": "cliff / broad shelter",
                "meaning_component": "pictograph of a spacious open hall built against a hillside cliff",
                "sound_component": "广 (guǎng)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A spacious mountain pavilion roof built on high crags; vast breadth and far-reaching spatial expanse.",
                "visual_mnemonic_story_en": "A spacious hillside hall (广) commanding vast unobstructed views across distant plains.",
                "visual_mnemonic_story_es": "Un amplio cobertizo en el monte (广) con vistas despejadas a extensas llanuras.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "I",
                "traditional": "廣"
            },
            {
                "character": "泛",
                "pinyin": "fàn",
                "meaning_en": "float; overflow; general; diffuse",
                "meaning_es": "flotar; desbordar; general; esparcir",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water flow) + 乏 (run out / empty / overturn)",
                "sound_component": "乏 (fá / phonetic connection)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 beside 乏; flood waters overflowing river banks, diffusing and spreading far across plains.",
                "visual_mnemonic_story_en": "Flood waters (氵) drifting and overflowing wide banks, diffusing far and wide (泛).",
                "visual_mnemonic_story_es": "Corrientes de agua (氵) que se desbordan mansamente esparciéndose por el llano (泛).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EHIO",
                "traditional": "泛"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A spacious hall's breadth (广) combined with overflowing water diffusing across plains (泛) is widespread (广泛).",
            "composite_memory_hook_es": "La vasta amplitud del monte (广) unida al agua que se desborda por el llano (泛) denota lo extenso (广泛).",
            "cultural_and_cognitive_roots": "Combines spatial breadth (广) with hydrological diffusion (泛) to signify extensive coverage across society and geography.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by falling fourth tone: 'guǎng fàn' (214-51). Dip low on 'guǎng' and strike firmly down on 'fàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "广", "pinyin": "guǎng", "meaning_en": "broad; wide", "distinction_note": "3 strokes: dot, horizontal, and downward left slash"},
                {"character": "厂", "pinyin": "chǎng", "meaning_en": "factory; plant", "distinction_note": "2 strokes: without the top dot"},
                {"character": "泛", "pinyin": "fàn", "meaning_en": "float; general", "distinction_note": "Water radical 氵 on left with 乏"},
                {"character": "眨", "pinyin": "zhǎ", "meaning_en": "blink; wink", "distinction_note": "Eye radical 目 on left of 乏"}
            ],
            "etymological_cognates": [
                {"character": "博", "pinyin": "bó", "gloss_en": "extensive; abundant"},
                {"character": "阔", "pinyin": "kuò", "gloss_en": "broad; vast"},
                {"character": "普", "pinyin": "pǔ", "gloss_en": "universal; general"},
                {"character": "漫", "pinyin": "màn", "gloss_en": "overflow; boundless"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "广泛 denotes extensive geographic distribution, large participant scale, or multi-disciplinary coverage.",
            "contrasts": [
                {"id": 1, "compared_word": "广泛 vs. 普遍", "pinyin": "pǔbiàn", "analysis": "普遍 means common or typical across most cases (普遍现象), while 广泛 highlights wide scope and breadth of reach (广泛涉猎)."},
                {"id": 2, "compared_word": "广泛 vs. 宽阔", "pinyin": "kuānkuò", "analysis": "宽阔 refers strictly to concrete physical dimensions of spaces or rivers (宽阔的马路), whereas 广泛 applies to abstract domains."},
                {"id": 3, "compared_word": "广泛 vs. 全面", "pinyin": "quánmiàn", "analysis": "全面 emphasizes thoroughness without missing angles (全面分析), while 广泛 emphasizes far-flung reach."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统草本医药在数千年的防病治病实践中积累了丰富经验，其安全有效的治疗理念在世界各地赢得了日益广泛的国际认可。越来越多的海外科研机构建立合作中心，对中医药的天然活性分子展开深入系统研究。",
                "pinyin": "Zhōngguó chuántǒng cǎoběn yīyào zài shùqiān nián de fángbìng-zhìbìng shíjiàn zhōng jīlěi le fēngfù jīngyàn, qí ānquán yǒuxiào de zhìliáo lǐniàn zài shìjiè gèdì yíngdé le rìyì guǎngfàn de guójì rènkě. Yuèláiyuè duō de hǎiwài kēyán jīgòu jiànlì hézuò zhōngxīn, duì zhōngyīyào de tiānrán huóxìng fēnzǐ zhǎnkāi shēnrù xìtǒng yánjiū.",
                "en": "Traditional Chinese herbal medicine accumulated clinical experience over millennia, winning widespread international acclaim for its safety. Global research centers increasingly partner to analyze natural active molecules.",
                "es": "La medicina herbaria tradicional china goza de un creciente reconocimiento internacional gracias a su eficacia milenaria. Prestigiosos centros extranjeros investigan sus compuestos activos en proyectos conjuntos."
            },
            {
                "id": "#2",
                "hanzi": "四合院不仅在北京老城落地生根，作为中国北方传统民居的重要代表，它在河北、山东以及山西等广大北方省份都有着极其广泛的分布。不论是市井平民的简朴小院，还是王府巨贾的深宅大院，四合院的样式都展现出了跨越阶层的强大文化凝聚力。",
                "pinyin": "Sìhéyuàn bùjǐn zài Běijīng lǎochéng luòdì-shēnggēn, zuòwéi Zhōngguó běifāng chuántǒng mínjū de zhòngyào dàibiǎo, tā zài Héběi, Shāndōng yǐjí Shānxī děng guǎngdà běifāng shěngfèn dōu yǒuzhe jíqí guǎngfàn de fēnbù. Búlùn shì shìjǐng píngmín de jiǎnpǔ xiǎoyuàn, háishì wángfǔ jùjiǎ de shēnzhái-dàyuàn, sìhéyuàn de yàngshì dōu zhǎnxiàn chū le kuàyuè jiēcéng de qiángdà wénhuà níngjùlì.",
                "en": "The siheyuan not only rooted in Beijing, but was widely distributed across Hebei, Shandong, and Shanxi. From humble alley courtyards to aristocratic mansions, the siheyuan showcased unifying cultural cohesion across classes.",
                "es": "El siheyuan floreció en Pekín y se extendió con amplitud por Hebei, Shandong y Shanxi. De las modestas casas del pueblo a los palacetes nobiliarios, este modelo derrochó una admirable cohesión cultural."
            }
        ]
    },

    # 09 样式
    {
        "id": "9",
        "hanzi": "样式",
        "pinyin": "yàng shì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "style; pattern; design; model; fashion",
            "es": "estilo; modelo; diseño; hechura; corte"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the design, pattern, cut, or stylistic format of clothing, buildings, or manufactured goods",
                "definition_es": "forma, diseño, corte o modelo exterior de prendas, construcciones o artefactos",
                "example_phrase": "新颖大方的服装样式 (a novel and elegant clothing style)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这款新上市的运动鞋在外观样式上巧妙融入了中国传统山水纹样，一经推出便赢得了年轻消费者的热烈追捧。",
                "pinyin": "Zhè kuǎn xīn shàngshì de yùndòngxié zài wàiguān yàngshì shang qiǎomiào róngrù le Zhōngguó chuántǒng shānshuǐ wényàng, yījīng tuīchū biàn yíngdé le niánqīng xiāofèizhě de rèliè zhuīpěng.",
                "en": "This newly released sneaker seamlessly blends traditional Chinese landscape patterns into its design style, instantly captivating young consumers.",
                "es": "Esta nueva zapatilla incorpora motivos de pintura paisajística tradicional en su diseño exterior, cautivando al público juvenil desde su lanzamiento."
            },
            {
                "id": "#2",
                "hanzi": "在老城区建筑立面改造过程中，工程师们严格参照历史档案，力求精准还原民国时期的门窗样式。",
                "pinyin": "Zài lǎochéngqū jiànzhù lìmiàn gǎizào guòchéng zhōng, gōngchéngshīmen yángé cānzhào lìshǐ dàng'àn, lìqiú jīngzhǔn huányuán Mínguó shíqí de ménchuāng yàngshì.",
                "en": "During facade restorations in the old quarters, engineers consulted historic archives to faithfully restore Republican-era window and door styles.",
                "es": "En la rehabilitación de fachadas del casco viejo, los peritos consultaron archivos históricos para recrear fielmente la hechura de puertas y cancelas de época."
            }
        ],
        "collocations": [
            {"hanzi": "服装样式", "en": "clothing style / design"},
            {"hanzi": "建筑样式", "en": "architectural style / pattern"},
            {"hanzi": "发型样式", "en": "haircut style"},
            {"hanzi": "新颖样式", "en": "novel design / style"},
            {"hanzi": "传统样式", "en": "traditional pattern / design"},
            {"hanzi": "改变样式", "en": "change the style"}
        ],
        "idioms": [
            {"hanzi": "千姿百态", "pinyin": "qiān zī bǎi tài", "meaning_en": "in diverse postures and forms; multifaceted variety"},
            {"hanzi": "别具匠心", "pinyin": "bié jù jiàng xīn", "meaning_en": "show exceptional ingenuity in design or craft"},
            {"hanzi": "花样翻新", "pinyin": "huā yàng fān xīn", "meaning_en": "create fresh novel patterns; renovate designs"},
            {"hanzi": "依样画葫芦", "pinyin": "yī yàng huà hú lu", "meaning_en": "draw gourd copying original model; copy slavishly"}
        ],
        "character_decomposition": [
            {
                "character": "样",
                "pinyin": "yàng",
                "meaning_en": "appearance; shape; pattern; sample",
                "meaning_es": "apariencia; muestra; modelo; tipo",
                "radical": "木",
                "radical_meaning_en": "tree / wood",
                "meaning_component": "木 (wooden casting mold) + 羊 (sheep / auspicious horn shape)",
                "sound_component": "羊 (yáng / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tree radical 木 beside 羊; originally a wooden casting mold carved with decorative patterns to shape prototypes and samples.",
                "visual_mnemonic_story_en": "Carving fine wooden molds (木) shaped like graceful ram horns (羊) to forge beautiful samples (样).",
                "visual_mnemonic_story_es": "Tallar moldes de madera (木) con la fina curva de cuernos de carnero (羊) para crear modelos (样).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "DTO",
                "traditional": "樣"
            },
            {
                "character": "式",
                "pinyin": "shì",
                "meaning_en": "type; pattern; style; rule; formula",
                "meaning_es": "tipo; patrón; norma; fórmula",
                "radical": "弋",
                "radical_meaning_en": "shoot arrow / stake",
                "meaning_component": "弋 (reference stake marker) + 工 (carpenter's square)",
                "sound_component": "弋 (yì)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A carpenter's tool 工 aligned against a stake 弋; an officially approved standard prototype, rule, or model.",
                "visual_mnemonic_story_en": "Calibrating a craftsman's square (工) against an upright post (弋) to define standard style (式).",
                "visual_mnemonic_story_es": "Alinear la escuadra artesanal (工) frente al poste patrón (弋) para dictar el estilo normativo (式).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IPMO",
                "traditional": "式"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A carved wooden prototype (样) combined with an approved standard rule (式) defines a tangible style (样式).",
            "composite_memory_hook_es": "Un molde de madera tallado (样) sumado al patrón normativo (式) compone el estilo o hechura (样式).",
            "cultural_and_cognitive_roots": "Historic title of imperial architectural draftsmen in Beijing: '样式雷' (Style Lei family), master architects of the Forbidden City and Summer Palace.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'yàng shì' (51-51). Strike both syllables with decisive, balanced downward cadence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "样", "pinyin": "yàng", "meaning_en": "sample; pattern", "distinction_note": "Tree radical 木 on left with 羊"},
                {"character": "洋", "pinyin": "yáng", "meaning_en": "ocean; foreign", "distinction_note": "Water radical 氵 on left of 羊"},
                {"character": "详", "pinyin": "xiáng", "meaning_en": "detailed; clear", "distinction_note": "Speech radical 讠 on left of 羊"},
                {"character": "式", "pinyin": "shì", "meaning_en": "pattern; formula", "distinction_note": "Contains 工 inside 弋"}
            ],
            "etymological_cognates": [
                {"character": "款", "pinyin": "kuǎn", "gloss_en": "design; model; fund"},
                {"character": "型", "pinyin": "xíng", "gloss_en": "type; mold; model"},
                {"character": "范", "pinyin": "fàn", "gloss_en": "pattern; model; limit"},
                {"character": "类", "pinyin": "lèi", "gloss_en": "category; kind"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "样式 refers to the visual design, cut, or aesthetic configuration of physical manufactured goods or structures.",
            "contrasts": [
                {"id": 1, "compared_word": "样式 vs. 模式", "pinyin": "móshì", "analysis": "模式 refers to abstract business, operational, or economic paradigms (商业模式), while 样式 denotes tangible physical shape and cut."},
                {"id": 2, "compared_word": "样式 vs. 款式", "pinyin": "kuǎnshì", "analysis": "款式 is commonly used for commercial fashion apparel and consumer gadgets (最新款式), while 样式 encompasses architecture and traditional crafts."},
                {"id": 3, "compared_word": "样式 vs. 形式", "pinyin": "xíngshì", "analysis": "形式 is philosophical/abstract (form vs content), while 样式 is concrete visual aesthetics."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在故宫与颐和园的营造史中，清代内务府‘样式房’执掌了所有皇家宫殿的设计大权。其中声名赫赫的‘样式雷’世家历经八代传承，绘制了成千上万件烫样与精美图纸，将中国古建筑样式的美感推向了举世瞩目的艺术巅峰。",
                "pinyin": "Zài Gùgōng yǔ Yíhéyuán de yíngzào shǐ zhōng, Qīngdài Nèiwùfǔ 'Yàngshì Fáng' zhízhǎng le suǒyǒu huángjiā gōngdiàn de shèjì dàquán. Qízhōng shēngmíng-hèhè de 'Yàngshì Léi' shìjiā lìjīng bā dài chuánchéng, huìzhì le chéngqiān-shàngwàn jiàn tàngyàng yǔ jīngměi túzhǐ, jiāng Zhōngguó gǔ jiànzhù yàngshì de měigǎn tuīxiàng le jǔshì-zhǔmù de yìshù diānfēng.",
                "en": "In Forbidden City and Summer Palace history, the Qing Imperial Workshop's 'Style Chamber' oversaw designs. The famed 'Style Lei' family across eight generations produced thousands of architectural models, elevating palace styles to global peaks.",
                "es": "En la corte Qing, la 'Cámara de Estilo' diseñó la Ciudad Prohibida. La célebre dinastía 'Estilo Lei' forjó maquetas y planos primorosos durante ocho generaciones, elevando la arquitectura palaciega a su cúspide."
            },
            {
                "id": "#2",
                "hanzi": "四合院是北方传统民居最经典的典型样式。这种建筑样式分布广泛，虽然在各地因地制宜产生过细微的构造演化，但四面合围、尊卑有别以及中轴对称的核心格局始终未曾改变，成为千百年来北方人安放乡愁的温馨依托。",
                "pinyin": "Sìhéyuàn shì běifāng chuántǒng mínjū zuì jīngdiǎn de diǎnxíng yàngshì. Zhè zhǒng jiànzhù yàngshì fēnbù guǎngfàn, suīrán zài gèdì yīndì-zhìyí chǎnshēng guò xìwēi de gòuzào yǎnhuà, dàn sì miàn héwéi, zūnbēi-yǒubié yǐjí zhōngzhóu duìchèn de héxīn géjú shǐzhōng wèicéng gǎibiàn, chéngwéi qiānbǎinián lái běifāngrén ānfàng xiāngchóu de wēnxīn yītuō.",
                "en": "The siheyuan is the signature archetype of northern vernacular dwellings. Widely distributed, while adapting locally with subtle structural tweaks, its central axis symmetry and enclosed yard remained unchanged, cradling nostalgic warmth.",
                "es": "El siheyuan es el modelo arquetípico de la vivienda popular norteña. Con sutiles adaptaciones locales, su patio cerrado y rigurosa simetría se mantuvieron inmutables, acogiendo el apego solariego de generaciones."
            }
        ]
    },

    # 10 代表
    {
        "id": "10",
        "hanzi": "代表",
        "pinyin": "dài biǎo",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "representative; delegate; to represent; stand for",
            "es": "representante; delegado; representar; simbolizar; ejemplar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person chosen or appointed to act or speak on behalf of an organization, constituency, or nation",
                "definition_es": "persona elegida o comisionada para actuar en nombre de una colectividad",
                "example_phrase": "出席国际气候峰会的各国代表 (delegates attending international climate summits)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to serve as a typical symbol, personification, or embodiment of a class, culture, or institution",
                "definition_es": "simbolizar, personificar o constituir la muestra típica de una clase o cultura",
                "example_phrase": "四合院代表了北方民居文化 (siheyuan represents northern dwelling culture)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "作为青年科研人员代表，他在全国科技创新表彰大会上作了激情澎湃的汇报发言。",
                "pinyin": "Zuòwéi qīngnián kēyán rényuán dàibiǎo, tā zài quánguó kējì chuàngxīn biǎozhāng dàhuì shang zuò le jīqíng-péngpài de huìbào fāyán.",
                "en": "As a representative of young scientific researchers, he delivered an impassioned keynote speech at the National Science and Technology Innovation Conference.",
                "es": "Como portavoz de los jóvenes investigadores, pronunció un vibrante discurso en el Congreso Nacional de Innovación Tecnológica."
            },
            {
                "id": "#2",
                "hanzi": "红墙黄瓦的故宫不仅是古代皇权建筑的顶峰，更代表了中华民族源远流长的营造智慧与审美追求。",
                "pinyin": "Hóngqiáng-huángwǎ de Gùgōng bùjǐn shì gǔdài huángquán jiànzhù de dǐngfēng, gèng dàibiǎo le Zhōnghuá mínzú yuányuǎn-liúcháng de yíngzào zhìhuì yǔ shěnměi zhuīqiú.",
                "en": "The Forbidden City with red walls and yellow glazed tiles is not only the pinnacle of imperial architecture, but represents China's enduring craftsmanship and aesthetic pursuit.",
                "es": "La Ciudad Prohibida no sólo encarna la cúspide palaciega, sino que representa la milenaria sabiduría constructiva y el ideal estético chino."
            }
        ],
        "collocations": [
            {"hanzi": "代表作", "en": "masterpiece; representative work"},
            {"hanzi": "代表团", "en": "delegation; deputation"},
            {"hanzi": "人民代表", "en": "people's representative / deputy"},
            {"hanzi": "法定代表人", "en": "legal representative"},
            {"hanzi": "代表性", "en": "representativeness; typicality"},
            {"hanzi": "完全代表", "en": "fully represent"}
        ],
        "idioms": [
            {"hanzi": "当之无愧", "pinyin": "dāng zhī wú kuì", "meaning_en": "fully worthy of the title; deserve honor without compunction"},
            {"hanzi": "推陈出新", "pinyin": "tuī chén chū xīn", "meaning_en": "weed out the chaff to bring forth the new; innovate"},
            {"hanzi": "独领风骚", "pinyin": "dú lǐng fēng sāo", "meaning_en": "lead the trend exclusively; outshine all peers"},
            {"hanzi": "名副其实", "pinyin": "míng fù qí shí", "meaning_en": "worthy of the name; name reflects reality"}
        ],
        "character_decomposition": [
            {
                "character": "代",
                "pinyin": "dài",
                "meaning_en": "replace; substitute; era; generation",
                "meaning_es": "sustituir; relevar; época; generación",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person proxy) + 弋 (stake marker)",
                "sound_component": "弋 (yì / phonetic association)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 standing beside a boundary stake 弋 to relieve or substitute a sentry; replacing, acting as proxy, or generation.",
                "visual_mnemonic_story_en": "A relief guard (亻) taking his station by the watchtower post (弋) to act as proxy (代).",
                "visual_mnemonic_story_es": "Un relevo de guardia (亻) que ocupa su puesto junto al poste vigía (弋) en sustitución (代).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OIP",
                "traditional": "代"
            },
            {
                "character": "表",
                "pinyin": "biǎo",
                "meaning_en": "exterior; surface; show; express; watch",
                "meaning_es": "exterior; superficie; manifestar; reloj",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (fur collar / garment) + 毛 (outer fleece strokes)",
                "sound_component": "表 (biǎo)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Garment radical 衣 displaying outer fur on its surface; the visible exterior manifested outward for all to witness.",
                "visual_mnemonic_story_en": "Wearing a warm fur robe (衣) with lustrous fleece visible outside, expressing outer dignity (表).",
                "visual_mnemonic_story_es": "Lucir una túnica (衣) cuyo forro viste por fuera mostrando apostura visible (表).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "QMV",
                "traditional": "表"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Standing as a personal proxy (代) to manifest outward representation (表) makes one a delegate (代表).",
            "composite_memory_hook_es": "Actuar como portavoz suplente (代) para manifestar externamente una voz (表) es representar (代表).",
            "cultural_and_cognitive_roots": "Blends proxy delegation (代) with manifestation (表), central to governance and canonical typology.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by dipping third tone: 'dài biǎo' (51-214). Drop firmly on 'dài', then dip low and scoop upward on 'biǎo'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "代", "pinyin": "dài", "meaning_en": "era; replace", "distinction_note": "Person radical 亻 on left with 弋"},
                {"character": "伐", "pinyin": "fá", "meaning_en": "fell timber; attack", "distinction_note": "Person radical 亻 with weapon 戈 on right"},
                {"character": "表", "pinyin": "biǎo", "meaning_en": "surface; watch", "distinction_note": "Upper horizontal stroke with crossed vertical over 衣"},
                {"character": "衰", "pinyin": "shuāi", "meaning_en": "decline; wane", "distinction_note": "Has 口-like middle element in 衣"}
            ],
            "etymological_cognates": [
                {"character": "理", "pinyin": "lǐ", "gloss_en": "manage; reason"},
                {"character": "使", "pinyin": "shǐ", "gloss_en": "send; envoy"},
                {"character": "征", "pinyin": "zhēng", "gloss_en": "symbol; token"},
                {"character": "兆", "pinyin": "zhào", "gloss_en": "omen; sign"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "代表 indicates authorized proxy status or serving as the definitive exemplar of an entire category.",
            "contrasts": [
                {"id": 1, "compared_word": "代表 vs. 象征", "pinyin": "xiàngzhēng", "analysis": "象征 refers to symbolic metaphors or artistic emblems (鸽子象征和平), while 代表 denotes authoritative proxy delegation or exemplary prototypes."},
                {"id": 2, "compared_word": "代表 vs. 代理", "pinyin": "dàilǐ", "analysis": "代理 focuses strictly on commercial or legal agency powers (代理人, 代理品牌), whereas 代表 carries broader cultural embodiment."},
                {"id": 3, "compared_word": "代表 vs. 典型", "pinyin": "diǎnxíng", "analysis": "典型 is primarily an adjective meaning quintessential or representative (典型案例), while 代表 can function actively as a verb."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国优秀文学经典作品往往以深刻的人物命运折射出整个时代的精神风貌。鲁迅先生笔下的阿Q形象，作为旧中国国民劣根性与精神胜利法的艺术代表，以极其辛辣深刻的讽刺笔触，唤醒了无数沉睡麻木的心灵。",
                "pinyin": "Zhōngguó yōuxiù wénxué jīngdiǎn zuòpǐn wǎngwǎng yǐ shēnkè de rénwù mìngyùn zhéshè chū zhěnggè shídài de jīngshén fēngmào. Lǔ Xùn xiānsheng bǐxià de Ā Q xíngxiàng, zuòwéi jiù Zhōngguó guómín liègènxìng yǔ jīngshén-shènglìfǎ de yìshù dàibiǎo, yǐ jíqí xīnlà shēnkè de fěngcì bǐchù, huànxǐng le wúshù chénsùi māmù de xīnlíng.",
                "en": "Chinese literary masterpieces mirror eras through profound character destinies. Lu Xun's Ah Q, as the artistic embodiment of psychological victory and complacency, awakened numb souls with biting, piercing satire.",
                "es": "Las obras maestras chinas retratan épocas mediante destinos memorables. El célebre Ah Q de Lu Xun, como símbolo artístico del autoengaño resignado, sacudió conciencias con una sátira lúcida e implacable."
            },
            {
                "id": "#2",
                "hanzi": "四合院不仅是历史悠久的传统民居，更是北方建筑文化当之无愧的重要代表。四面房屋形成的封闭空间，不仅体现了长幼有序的儒家家族伦理，更生动代表了中国人向内凝聚、安居守正的居住哲学，在岁月变迁中绽放着不朽的文明光彩。",
                "pinyin": "Sìhéyuàn bùjǐn shì lìshǐ-yōujiǔ de chuántǒng mínjū, gèng shì běifāng jiànzhù wénhuà dāngzhī-wúkuì de zhòngyào dàibiǎo. Sì miàn fángwū xíngchéng de fēngbì kōngjiān, bùjǐn tǐxiàn le zhǎngyòu-yǒuxù de Rújiā jiāzú lúnlǐ, gèng shēngdòng dàibiǎo le Zhōngguórén xiàngnèi níngjù, ānjū-shǒuzhèng de jūzhù zhéxué, zài suìyuè biànqiān zhōng zhànfàng zhe bùxiǔ de wénmíng guāngcǎi.",
                "en": "The siheyuan is not only an ancient folk house, but an undisputed representative of northern architectural culture. Its enclosed space embodies Confucian family ethics and reflective residential philosophy, radiating timeless brilliance.",
                "es": "El siheyuan es la máxima encarnación de la cultura constructiva septentrional. Su recinto cerrado simboliza la armonía confuciana y la filosofía del recogimiento sereno, brillando como un legado inmortal."
            }
        ]
    }
]

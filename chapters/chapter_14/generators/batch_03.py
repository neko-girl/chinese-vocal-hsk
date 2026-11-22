# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 走廊
    {
        "id": "21",
        "hanzi": "走廊",
        "pinyin": "zǒu láng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "corridor; hallway; veranda; covered walkway",
            "es": "pasillo; corredor; galería cubierta; soportal"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a roofed passageway or corridor connecting rooms or buildings, often open on one or both sides",
                "definition_es": "pasadizo o galería techada que comunica diversas habitaciones o pabellones",
                "example_phrase": "漫步在走廊上 (strolling along the corridor)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "北京四合院里的抄手走廊将正房与东西厢房紧密相连，即使雨雪天气也能在各屋之间自如穿行。",
                "pinyin": "Běijīng sìhéyuàn lǐ de chāoshǒu zǒuláng jiāng zhèngfáng yǔ dōngxī xiāngfáng jǐnmì xiānglián, jíshǐ yǔxuě tiānqì yě néng zài gè wū zhījiān zìrú chuānxíng.",
                "en": "The covered verandas in Beijing courtyards connect the main room with the wings, allowing people to walk sheltered even during rain or snow.",
                "es": "Las galerías cubiertas del siheyuan pekinés conectan la sala principal con las alas, permitiendo circular a cubierto incluso con lluvia o nieve."
            },
            {
                "id": "#2",
                "hanzi": "这栋现代办公大楼的中心走廊两侧，悬挂着许多展示企业发展历程的历史照片。",
                "pinyin": "Zhè dòng xiàndài bàngōng dàlóu de zhōngxīn zǒuláng liǎngcè, xuánguà zhe xǔduō zhǎnshì qǐyè fāzhǎn lìchéng de lìshǐ zhàopiàn.",
                "en": "Along both sides of the modern office building's central corridor hang numerous historical photographs detailing the company's evolution.",
                "es": "A ambos lados del pasillo central del moderno edificio corporativo cuelgan fotografías históricas que relatan la trayectoria de la empresa."
            }
        ],
        "collocations": [
            {"hanzi": "抄手走廊", "en": "covered courtyard veranda / corridor"},
            {"hanzi": "穿过走廊", "en": "pass through the corridor"},
            {"hanzi": "走廊尽头", "en": "at the end of the corridor"},
            {"hanzi": "露天走廊", "en": "open-air veranda"},
            {"hanzi": "艺术走廊", "en": "art corridor / gallery"},
            {"hanzi": "绿色走廊", "en": "green ecological corridor"}
        ],
        "idioms": [
            {"hanzi": "雕梁画栋", "pinyin": "diāo liáng huà dòng", "meaning_en": "carved beams and painted rafters; ornate architectural elegance"},
            {"hanzi": "回廊曲折", "pinyin": "huí láng qū zhé", "meaning_en": "winding verandas and zigzagging corridors"},
            {"hanzi": "步移景异", "pinyin": "bù yí jǐng yì", "meaning_en": "scenery transforms with every shifting step"},
            {"hanzi": "曲径通幽", "pinyin": "qū jìng tōng yōu", "meaning_en": "winding path leading to a secluded sanctuary"}
        ],
        "character_decomposition": [
            {
                "character": "走",
                "pinyin": "zǒu",
                "meaning_en": "walk; go; leave; run",
                "meaning_es": "caminar; andar; marchar; irse",
                "radical": "走",
                "radical_meaning_en": "walk / run",
                "meaning_component": "pictograph of a running person with swinging arms and stride",
                "sound_component": "走 (zǒu)",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone glyph depicting a person swinging arms while striding forward swiftly.",
                "visual_mnemonic_story_en": "A brisk walker stepping energetically with arms swinging (走).",
                "visual_mnemonic_story_es": "Un caminante enérgico que bracea con determinación al andar (走).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "GYO",
                "traditional": "走"
            },
            {
                "character": "廊",
                "pinyin": "láng",
                "meaning_en": "corridor; porch; veranda; hall",
                "meaning_es": "corredor; porche; galería; galería columnada",
                "radical": "广",
                "radical_meaning_en": "shelter / wide roof",
                "meaning_component": "广 (broad rooftop shelter) + 郎 (lofty court pavilion)",
                "sound_component": "郎 (láng)",
                "stroke_count": 11,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A roofed colonnade 广 extending outward from noble pavilions 郎; denotes covered passageways.",
                "visual_mnemonic_story_en": "A graceful overhanging roof shelter (广) lining the pavilion path to shield strollers (廊).",
                "visual_mnemonic_story_es": "Un elegante alero techado (广) que resguarda el sendero columnado de la galería (廊).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IIIL",
                "traditional": "廊"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Walking along (走) a sheltered colonnade veranda (廊) brings one through the courtyard corridor (走廊).",
            "composite_memory_hook_es": "Caminar (走) al amparo de una galería columnada techada (廊) define el corredor o pasillo (走廊).",
            "cultural_and_cognitive_roots": "Essential element in classical Chinese garden and compound architecture, serving both practical transit and picturesque contemplation.",
            "tone_sandhi_and_pitch_modulation": "Third tone to second tone: 'zǒu láng' (214-35). Dip deep on 'zǒu' and rise melodiously on 'láng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "郎", "pinyin": "láng", "meaning_en": "young man; official", "distinction_note": "Lacks the enclosing shelter radical 广"},
                {"character": "朗", "pinyin": "lǎng", "meaning_en": "bright; clear", "distinction_note": "Moon radical 月 on right instead of 阝"},
                {"character": "赶", "pinyin": "gǎn", "meaning_en": "rush; catch up", "distinction_note": "Shield radical 干 to the right of 走"},
                {"character": "超", "pinyin": "chāo", "meaning_en": "transcend; exceed", "distinction_note": "Knife/call radical 召 to the right of 走"}
            ],
            "etymological_cognates": [
                {"character": "长廊", "pinyin": "chángláng", "gloss_en": "long covered corridor; colonnade"},
                {"character": "游廊", "pinyin": "yóuláng", "gloss_en": "covered ambulatory walkway"},
                {"character": "走动", "pinyin": "zǒudòng", "gloss_en": "walk about; visit"},
                {"character": "行走", "pinyin": "xíngzǒu", "gloss_en": "walk; stride"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "走廊 emphasizes a covered indoor or veranda-style architectural transit passageway.",
            "contrasts": [
                {"id": 1, "compared_word": "走廊 vs. 街道", "pinyin": "jiēdào", "analysis": "街道 refers to open public streets flanked by city shops, whereas 走廊 is a domestic or building corridor."},
                {"id": 2, "compared_word": "走廊 vs. 胡同", "pinyin": "hútòng", "analysis": "胡同 specifically designates northern Chinese city lanes between compounds, not an internal covered walkway."},
                {"id": 3, "compared_word": "走廊 vs. 大厅", "pinyin": "dàtīng", "analysis": "大厅 is a wide stationary hall, whereas 走廊 is an elongated passageway connecting destinations."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的抄手游廊极富诗意。这道带顶的曲折走廊顺着院墙蜿蜒伸展，不仅遮挡烈日与骤雨，廊檐下的彩绘更如画卷般引人入胜。雨天漫步走廊，听屋檐滴水，看庭前花木，令人顿生无限雅兴。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de chāoshǒu yóuláng jí fù shīyì. Zhè dào dài dǐng de qūzhé zǒuláng shùnzhe yuànqiáng wānyán shēnzhǎn, bùjǐn zhēdǎng lièrì yǔ zhòuyǔ, lángyán xià de cǎihuì gèng rú huàjuàn bān yǐnrén-rùshèng. Yǔtiān mànbù zǒuláng, tīng wūyán dīshuǐ, kàn tíngqián huāmù, lìngrén dùn shēng wúxiàn yǎxìng.",
                "en": "The covered veranda in old Beijing courtyards is intensely poetic. Winding along the compound wall, it shelters against sun and downpours, while vivid beam paintings resemble scrolls, turning rainy courtyard strolls into tranquil joy.",
                "es": "La galería techada del siheyuan pekinés encierra una intensa poesía. Serpenteando junto al muro, resguarda del sol y aguaceros, mientras sus vigas policromadas emulan lienzos que invitan a contemplar la lluvia con serenidad."
            },
            {
                "id": "#2",
                "hanzi": "在现代建筑设计与生态规划中，“绿色走廊”概念日益受到重视。设计师在林立的城市高楼之间打造通风采光的生态走廊，让候鸟迁徙与冷空气顺利流通，有效缓解了都市热岛效应，赋予了传统走廊更广阔的时代内涵。",
                "pinyin": "Zài xiàndài jiànzhù shèjì yǔ shēngtài guīhuà zhōng, 'lǜsè zǒuláng' gàiniàn rìyì shòudào zhòngshì. Shèjìshī zài línlì de chéngshì gāolóu zhījiān dǎzào tōngfēng cǎiguāng de shēngtài zǒuláng, ràng hòuniǎo qiānxǐ yǔ lěngkōngqì shùnlì liútōng, yǒuxiào huǎnjiě le dūshì rèdǎo xiàoyìng, fùyǔ le chuántǒng zǒuláng gèng guǎngkuò de shídài nèihán.",
                "en": "In modern architecture and ecological planning, the concept of 'green corridors' receives growing attention. Urban planners weave breezeways among skyscrapers to enable bird migration and ventilation, mitigating urban heat islands.",
                "es": "En la arquitectura contemporánea, el concepto de 'corredor verde' cobra relieve. Los urbanistas integran galerías ecológicas entre rascacielos para facilitar el vuelo de aves y la ventilación, atenuando las islas de calor urbano."
            }
        ]
    },

    # 22 空间
    {
        "id": "22",
        "hanzi": "空间",
        "pinyin": "kōng jiān",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "space; room; clearance; outer space",
            "es": "espacio; amplitud; margen; espacio exterior"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "physical expanse or volume available for occupation; room for activity or growth; outer space",
                "definition_es": "extensión física tridimensional disponible; cabida o margen para maniobra; cosmos",
                "example_phrase": "生活空间 (living space)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院中心宽敞明亮的天井，为一家老小提供了亲近自然、开展日常交往的开阔空间。",
                "pinyin": "Sìhéyuàn zhōngxīn kuānchǎng míngliàng de tiānjǐng, wèi yī jiā lǎoxiǎo tígōng le qīnjìn zìrán, kāizhǎn rìcháng jiāowǎng de kāikuò kōngjiān.",
                "en": "The spacious central courtyard provides the whole family with an expansive open space to commune with nature and engage in daily socializing.",
                "es": "El diáfano patio central del siheyuan brinda a la familia un holgado espacio al aire libre para convivir y disfrutar de la naturaleza."
            },
            {
                "id": "#2",
                "hanzi": "优秀的城市规划师不仅关注建筑外形，更注重为社区居民营造富有人情味的公共活动空间。",
                "pinyin": "Yōuxiù de chéngshì guīhuàshī bùjǐn guānzhù jiànzhù wàixíng, gèng zhùzhòng wèi shèqū jūmín yíngzào fùyǒu rénqíngwèi de gōnggòng huódòng kōngjiān.",
                "en": "Talented urban planners focus not only on building aesthetics, but also on crafting public activity spaces rich in human warmth for residents.",
                "es": "Los urbanistas virtuosos no solo atienden a la volumetría exterior, sino a brindar a los vecinos espacios públicos acogedores para la convivencia."
            }
        ],
        "collocations": [
            {"hanzi": "生存空间", "en": "living / survival space"},
            {"hanzi": "公共空间", "en": "public space"},
            {"hanzi": "活动空间", "en": "activity space / room to maneuver"},
            {"hanzi": "广阔空间", "en": "vast space / wide scope"},
            {"hanzi": "提升空间", "en": "room for improvement"},
            {"hanzi": "外层空间", "en": "outer space"}
        ],
        "idioms": [
            {"hanzi": "海阔天空", "pinyin": "hǎi kuò tiān kōng", "meaning_en": "as boundless as sea and sky; broad-minded and free"},
            {"hanzi": "天高地厚", "pinyin": "tiān gāo dì hòu", "meaning_en": "high as the heavens and deep as the earth; profound complexity"},
            {"hanzi": "虚怀若谷", "pinyin": "xū huái ruò gǔ", "meaning_en": "modest mind as receptive as an open valley"},
            {"hanzi": "别有洞天", "pinyin": "bié yǒu dòng tiān", "meaning_en": "a whole new enchanted world opening up"}
        ],
        "character_decomposition": [
            {
                "character": "空",
                "pinyin": "kōng",
                "meaning_en": "empty; sky; void; open air",
                "meaning_es": "vacío; cielo; aire libre; hueco",
                "radical": "穴",
                "radical_meaning_en": "cave / den",
                "meaning_component": "穴 (open hollow cave) + 工 (work tool / craft boundary)",
                "sound_component": "工 (gōng)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Excavating an underground cave 穴 until an expansive, open empty cavity 空 emerges.",
                "visual_mnemonic_story_en": "Digging open a rocky cave entrance (穴) to reveal a vast, airy open cavern (空).",
                "visual_mnemonic_story_es": "Abrir la entrada de una caverna (穴) para descubrir una cámara despejada y vacía (空).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JCM",
                "traditional": "空"
            },
            {
                "character": "间",
                "pinyin": "jiān",
                "meaning_en": "between; interval; space; room",
                "meaning_es": "entre; intervalo; estancia; medio",
                "radical": "门",
                "radical_meaning_en": "gate / door",
                "meaning_component": "门 (double-leaf gateway) + 日 (sunlight shining through crack)",
                "sound_component": "间 (jiān)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Sunlight 日 streaming through the gap between two closed gateway doors 门; marks space between.",
                "visual_mnemonic_story_en": "Beams of sun (日) filtering brightly through the crevice between closed doors (门).",
                "visual_mnemonic_story_es": "Rayos de sol (日) que se cuelan por el intersticio entre las hojas de la puerta (门).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "LNA",
                "traditional": "間"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Open expanse (空) opening between physical boundaries (间) defines three-dimensional space (空间).",
            "composite_memory_hook_es": "La amplitud diáfana (空) que media entre límites físicos (间) conforma el espacio disponible (空间).",
            "cultural_and_cognitive_roots": "Paired with 'time' (时间) in Chinese metaphysics: 宇 (infinite space) and 宙 (infinite time), combining emptiness and boundary.",
            "tone_sandhi_and_pitch_modulation": "Double first tone: 'kōng jiān' (55-55). Maintain a clear, elevated, sustained tone across both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "突", "pinyin": "tū", "meaning_en": "sudden; dash", "distinction_note": "Dog radical 犬 inside 穴 instead of 工"},
                {"character": "究", "pinyin": "jiū", "meaning_en": "investigate; after all", "distinction_note": "Nine radical 九 inside 穴 instead of 工"},
                {"character": "问", "pinyin": "wèn", "meaning_en": "ask; inquire", "distinction_note": "Mouth radical 口 inside 门 instead of 日"},
                {"character": "闭", "pinyin": "bì", "meaning_en": "close; shut", "distinction_note": "Talent radical 才 inside 门 instead of 日"}
            ],
            "etymological_cognates": [
                {"character": "空闲", "pinyin": "kòngxián", "gloss_en": "idle time; leisure"},
                {"character": "天空", "pinyin": "tiānkōng", "gloss_en": "sky; heavens"},
                {"character": "房间", "pinyin": "fángjiān", "gloss_en": "room; chamber"},
                {"character": "时间", "pinyin": "shíjiān", "gloss_en": "time; temporal duration"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "空间 denotes three-dimensional physical room, clearance, or figurative scope for growth.",
            "contrasts": [
                {"id": 1, "compared_word": "空间 vs. 时间", "pinyin": "shíjiān", "analysis": "时间 governs the temporal dimension (hours, duration), while 空间 governs spatial dimensions (volume, area)."},
                {"id": 2, "compared_word": "空间 vs. 地点", "pinyin": "dìdiǎn", "analysis": "地点 pinpoint a specific geographic location, whereas 空间 emphasizes the internal volume or capacity."},
                {"id": 3, "compared_word": "空间 vs. 拥挤", "pinyin": "yōngjǐ", "analysis": "拥挤 describes crowded conditions resulting from an acute shortage of 空间."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统院落特别擅长在有限的占地内营造富有层次的空间体验。四合院通过游廊、垂花门与影壁的巧妙穿插，将原本规整的物理空间划分为庭院、起居与私密等不同领域，展现出静谧深沉的东方空间美学。",
                "pinyin": "Zhōngguó chuántǒng yuànluò tèbié shàncháng zài yǒuxiàn de zhàndì nèi yíngzào fùyǒu céngcì de kōngjiān tǐyàn. Sìhéyuàn tōngguò yóuláng, chuíhuāmén yǔ yǐngbì de qiǎomiào chuānchā, jiāng yuánběn guīzhěng de wùlǐ kōngjiān huàfēn wéi tíngyuàn, qǐjū yǔ sìmì děng bùtóng lǐngyù, zhǎnxiàn chū jìngmì shēnchén de dōngfāng kōngjiān měixué.",
                "en": "Traditional Chinese compounds excel at creating layered spatial experiences within limited footprints. Interlacing verandas, ornate gates, and screen walls partition physical space into garden, living, and private realms with quiet Eastern aesthetics.",
                "es": "El patio tradicional chino descuella por articular ricas transiciones espaciales en solares acotados. Galerías, puertas caladas y cancelas modulan el espacio físico en zonas comunes, privadas y de jardín, expresando una sobria estética oriental."
            },
            {
                "id": "#2",
                "hanzi": "探索未知的外层空间，是人类追寻文明未来的宏伟征途。从最早的近地轨道卫星发射，到宇航员在国际空间站长期开展尖端科研，人类对深远空间的求索从未止步。浩瀚无垠的宇宙空间，激发着我们永恒的科学探索精神。",
                "pinyin": "Tànsuǒ wèizhī de wàicéng kōngjiān, shì rénlèi zhuīxún wénmíng wèilái de hóngwěi zhēngtú. Cóng zuìzǎo de jìndì guǐdào wèixīng fāshè, dào yǔhángyuán zài guójì kōngjiānzhàn chángqī kāizhǎn jiānduān kēyán, rénlèi duì shēnyuǎn kōngjiān de qiúsuǒ cóng wèi zhǐbù. Hàohàn-wúyín de yǔzhòu kōngjiān, jīfā zhe wǒmen yǒnghéng de kēxué tànsuǒ jīngshén.",
                "en": "Exploring unknown outer space represents humanity's grand quest for civilizational advancement. From early near-Earth satellites to long-duration stays aboard international space stations, cosmic space sparks our endless scientific spirit.",
                "es": "La exploración del espacio exterior constituye la gran odisea de la civilización hacia el porvenir. Desde los satélites en órbita baja hasta las misiones en estaciones espaciales, el cosmos infinito aviva un afán inagotable de descubrimiento."
            }
        ]
    },

    # 23 种
    {
        "id": "23",
        "hanzi": "种",
        "pinyin": "zhòng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to plant; cultivate; grow; sow",
            "es": "plantar; cultivar; sembrar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to put seeds, bulbs, or plants into the earth to grow; cultivate vegetation",
                "definition_es": "sembrar simientes o plantar vegetales en la tierra para que crezcan; cultivar",
                "example_phrase": "在院子里种树 (plant trees in the courtyard)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "北京人喜欢在四合院的中央天井里种上几株石榴树与海棠花，寓意着家族子孙兴旺、吉祥如意。",
                "pinyin": "Běijīng rén xǐhuan zài sìhéyuàn de zhōngyāng tiānjǐng lǐ zhòng shang jǐ zhū shíliushù yǔ hǎitánghuā, yùyì zhe jiāzú zǐsūn xīngwàng, jíxiáng-rúyì.",
                "en": "Beijingers love to plant pomegranates and crabapple trees in their courtyard centers, symbolizing thriving progeny and good fortune.",
                "es": "A los pequineses les complace plantar granados y begonias en el patio central del siheyuan, augurando descendencia floreciente y dicha."
            },
            {
                "id": "#2",
                "hanzi": "退休后，王老师在郊区租下了一小块菜地，每天细心浇水除草，享受种菜的田园乐趣。",
                "pinyin": "Tuìxiū hòu, Wáng lǎoshī zài jiāoqū zū xià le yī xiǎo kuài càidì, měitiān xìxīn jiāoshuǐ chúcǎo, xiǎngshòu zhòng cài de tiányuán lèqù.",
                "en": "After retirement, Teacher Wang leased a small vegetable plot in the suburbs, watering and weeding daily to relish the idyllic fun of gardening.",
                "es": "Tras jubilarse, el profesor Wang arrendó una parcela en las afueras, dedicándose a regar y escardar para saborear la paz de cultivar hortalizas."
            }
        ],
        "collocations": [
            {"hanzi": "种花种草", "en": "grow flowers and plants"},
            {"hanzi": "种树造林", "en": "plant trees and afforest"},
            {"hanzi": "种植农作物", "en": "cultivate agricultural crops"},
            {"hanzi": "播种希望", "en": "sow the seeds of hope"},
            {"hanzi": "种菜园", "en": "plant a vegetable patch"},
            {"hanzi": "亲手栽种", "en": "plant with one's own hands"}
        ],
        "idioms": [
            {"hanzi": "种瓜得瓜，种豆得豆", "pinyin": "zhòng guā dé guā, zhòng dòu dé dòu", "meaning_en": "as you sow, so shall you reap"},
            {"hanzi": "十年树木，百年树人", "pinyin": "shí nián shù mù, bǎi nián shù rén", "meaning_en": "it takes ten years to grow trees, but a hundred years to cultivate talent"},
            {"hanzi": "广种薄收", "pinyin": "guǎng zhòng bó shōu", "meaning_en": "plant extensively but reap meagerly; low yield across broad tracts"},
            {"hanzi": "播种未来", "pinyin": "bō zhòng wèi lái", "meaning_en": "sow the fertile seeds of tomorrow"}
        ],
        "character_decomposition": [
            {
                "character": "种",
                "pinyin": "zhòng",
                "meaning_en": "plant; cultivate; seed; kind",
                "meaning_es": "plantar; cultivar; semilla; especie",
                "radical": "禾",
                "radical_meaning_en": "grain / cereal crop",
                "meaning_component": "禾 (tender grain seedling) + 中 (penetrating soil stake)",
                "sound_component": "中 (zhōng / phonetic root)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Placing a grain seedling 禾 deep into the center 中 of fertile soil to take root; to cultivate.",
                "visual_mnemonic_story_en": "Carefully planting a young cereal shoot (禾) into the heart (中) of tilled soil (种).",
                "visual_mnemonic_story_es": "Hincar una espiga lozana (禾) en el seno (中) de la tierra labrada para que brote (种).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HDL",
                "traditional": "種"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Inserting a grain seedling (禾) into the heart of the ground (中) means to plant (种).",
            "composite_memory_hook_es": "Enterrar un tallo de cereal (禾) en el centro fértil del surco (中) define el acto de sembrar (种).",
            "cultural_and_cognitive_roots": "Central to traditional Chinese agrarian civilization where planting seasonal crops regulated calendar rhythms and social customs.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone as verb: 'zhòng' (51). Distinct from third-tone noun/classifier 'zhǒng' (kind/type). Pronounce with resolute downward pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "和", "pinyin": "hé", "meaning_en": "peace; harmony; with", "distinction_note": "Mouth radical 口 on the right instead of 中"},
                {"character": "秋", "pinyin": "qiū", "meaning_en": "autumn; fall", "distinction_note": "Fire radical 火 on the right instead of 中"},
                {"character": "秒", "pinyin": "miǎo", "meaning_en": "second (time)", "distinction_note": "Little radical 少 on the right instead of 中"},
                {"character": "科", "pinyin": "kē", "meaning_en": "science; branch", "distinction_note": "Dipper radical 斗 on the right instead of 中"}
            ],
            "etymological_cognates": [
                {"character": "种植", "pinyin": "zhòngzhí", "gloss_en": "plant; cultivate"},
                {"character": "栽种", "pinyin": "zāizhòng", "gloss_en": "plant; set in ground"},
                {"character": "耕种", "pinyin": "gēngzhòng", "gloss_en": "till and sow; cultivate farmland"},
                {"character": "种子", "pinyin": "zhǒngzi", "gloss_en": "seed; grain for sowing"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "种 (zhòng) functions as a transitive agricultural/horticultural verb meaning to embed seeds or saplings into earth.",
            "contrasts": [
                {"id": 1, "compared_word": "种 (zhòng) vs. 种 (zhǒng)", "pinyin": "zhǒng", "analysis": "Fourth tone 种 (zhòng) is strictly verbal (to plant), whereas third tone 种 (zhǒng) is nominal/classifier (seed, kind, sort)."},
                {"id": 2, "compared_word": "种 vs. 养", "pinyin": "yǎng", "analysis": "种 applies to flora and plants in earth, whereas 养 primarily targets animals (fish, birds) or ongoing personal care."},
                {"id": 3, "compared_word": "种 vs. 收", "pinyin": "shōu", "analysis": "收 is the direct antonym meaning to harvest or reap what was previously planted."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在老北京的四合院文化中，院落里的绿植栽种非常讲究。人们喜欢种石榴寓意“多子多福”，种海棠象征“富贵吉祥”，种紫藤增添春日雅趣。这些亲手栽种的花木，使院落一年四季都洋溢着勃勃生机。",
                "pinyin": "Zài lǎo Běijīng de sìhéyuàn wénhuà zhōng, yuànluò lǐ de lǜzhí zāizhòng fēicháng jiǎngjiu. Rénmen xǐhuan zhòng shíliu yùyì 'duō zǐ duō fú', zhòng hǎitáng xiàngzhēng 'fùguì jíxiáng', zhòng zǐténg zēngtiān chūnrì yǎqù. Zhèxiē qīnshǒu zāizhòng de huāmù, shǐ yuànluò yī nián sìjì dōu yángyì zhe bóbó shēngjī.",
                "en": "In the courtyard culture of old Beijing, planting greenery followed refined symbolism. Pomegranates meant fruitful posterity, crabapples heralded wealth, and wisteria lent spring elegance. These plants filled courtyards with vibrant vitality.",
                "es": "En la tradición del siheyuan pekinés, plantar especies vegetales respondía a delicados simbolismos. El granado auguraba bendición familiar, la begonia prosperidad y la glicina distinción primaveral, infundiendo lozanía al hogar."
            },
            {
                "id": "#2",
                "hanzi": "春种一粒粟，秋收万颗子。大自然的农耕法则生动诠释了付出与回报的朴素道理。只有在春天辛勤播种、耐得住酷暑里的默默灌溉与耕耘，才能在金秋时节迎来稻谷飘香的丰收喜悦。种下的每一滴汗水，都将结出生命的实果。",
                "pinyin": "Chūn zhòng yī lì sù, qiū shōu wàn kē zǐ. Dàzìrán de nónggēng fǎzé shēngdòng quánshì le fùchū yǔ huíbào de pǔsù dàolǐ. Zhǐyǒu zài chūntiān xīnqín bōzhòng, nàidézhe kùshǔ lǐ de mòmò guàngài yǔ gēngyún, cái néng zài jīnqiū shíjié yínglái dàogǔ piāoxiāng de fēngshōu xǐyuè. Zhòng xià de měi yī dī hànshuǐ, dōu jiāng jiéchū shēngmìng de shíguǒ.",
                "en": "Sow a single grain in spring, reap ten thousand seeds in autumn. Nature's agrarian law demonstrates the truth of effort and return. Only those who toil patiently in planting and irrigating will celebrate fragrant harvest joy in autumn.",
                "es": "Sembrar un grano en primavera y cosechar miríadas en otoño ilustra la relación entre esfuerzo y fruto. Solo la constancia al sembrar y regar en estío permite gozar en otoño de la mies dorada; cada gota de sudor fructifica en vida."
            }
        ]
    },

    # 24 竹子
    {
        "id": "24",
        "hanzi": "竹子",
        "pinyin": "zhú zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "bamboo",
            "es": "bambú"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a fast-growing woody perennial evergreen plant with hollow stems, revered in Chinese culture for upright resilience",
                "definition_es": "planta perenne leñosa de tallos huecos y nudos marcados, venerada en la cultura china por su rectitud e integridad",
                "example_phrase": "一片翠绿的竹子 (a patch of emerald green bamboo)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "主人在四合院的西南隅种了一丛挺拔的翠绿竹子，微风拂过时沙沙作响，别有一番诗情画意。",
                "pinyin": "Zhǔrén zài sìhéyuàn de xīnányú zhòng le yī cóng tǐngbá de cuìlǜ zhúzi, wēifēng fúguò shí shāshā zuòxiǎng, bié yǒu yī fān shīqíng-huàyì.",
                "en": "The homeowner planted a cluster of emerald bamboos in the courtyard's southwest corner; when breezes stirred, they rustled poetically.",
                "es": "El dueño sembró matas de erguido bambú en un rincón del patio; con el roce de la brisa susurraban hojas, evocando viva poesía."
            },
            {
                "id": "#2",
                "hanzi": "在中国传统文化中，坚韧不拔的竹子常常被文人雅士视为刚正高洁君子品格的生动象征。",
                "pinyin": "Zài Zhōngguó chuántǒng wénhuà zhōng, jiānrèn-bùbá de zhúzi chángcháng bèi wénrén yǎshì shìwéi gāngzhèng gāojié jūnzǐ pǐngé de shēngdòng xiàngzhēng.",
                "en": "In traditional Chinese culture, tenacious and upright bamboo is frequently hailed by scholars as an emblem of gentlemanly integrity.",
                "es": "En la tradición cultural china, el tenaz bambú ha sido ensalzado por letrados como símbolo de la rectitud e integridad del noble caballero."
            }
        ],
        "collocations": [
            {"hanzi": "一丛竹子", "en": "a clump of bamboo"},
            {"hanzi": "翠绿的竹子", "en": "emerald green bamboo"},
            {"hanzi": "挺拔的竹子", "en": "tall, upright bamboo"},
            {"hanzi": "竹子制品", "en": "bamboo wares / handicrafts"},
            {"hanzi": "种竹子", "en": "plant bamboo"},
            {"hanzi": "竹子节节高", "en": "bamboo joints rising step by step (prosperity)"}
        ],
        "idioms": [
            {"hanzi": "胸有成竹", "pinyin": "xiōng yǒu chéng zhú", "meaning_en": "have a well-thought-out plan in mind beforehand"},
            {"hanzi": "势如破竹", "pinyin": "shì rú pò zhú", "meaning_en": "like splitting bamboo; sweeping forward with irresistible momentum"},
            {"hanzi": "青梅竹马", "pinyin": "qīng méi zhú mǎ", "meaning_en": "childhood sweethearts playing together from youth"},
            {"hanzi": "竹篮打水", "pinyin": "zhú lán dǎ shuǐ", "meaning_en": "drawing water with a bamboo basket; all labor in vain"}
        ],
        "character_decomposition": [
            {
                "character": "竹",
                "pinyin": "zhú",
                "meaning_en": "bamboo",
                "meaning_es": "bambú",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "pictograph of paired drooping pointed bamboo leaves",
                "sound_component": "竹 (zhú)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient pictograph representing two clusters of pointed bamboo leaves hanging downward.",
                "visual_mnemonic_story_en": "Slender pointed bamboo leaves (竹) rustling gently on straight green culms.",
                "visual_mnemonic_story_es": "Hojas de bambú lanceoladas (竹) suspendidas con gracia sobre cañas verdes erguidas.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HH",
                "traditional": "竹"
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; son; child",
                "meaning_es": "sufijo nominal; hijo; criatura",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "pictograph of an infant swaddled with outstretched arms",
                "sound_component": "子 (zǐ)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "An infant baby waving arms; here serving as a standard nominalizing noun suffix.",
                "visual_mnemonic_story_en": "A cheerful baby extending welcoming hands (子).",
                "visual_mnemonic_story_es": "Una pequeña criatura con los bracitos abiertos en ademán vivaz (子).",
                "tone_mnemonic_anchor": "neutral",
                "cangjie": "ND",
                "traditional": "子"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The noble green bamboo stalks (竹) affixed with the everyday noun suffix (子) gives the word for bamboo (竹子).",
            "composite_memory_hook_es": "Las varas estilizadas de bambú (竹) acompañadas del sufijo nominal (子) designan al bambú (竹子).",
            "cultural_and_cognitive_roots": "Revered as one of the 'Four Gentlemen' (梅兰竹菊) and 'Three Friends of Winter' (岁寒三友) for staying green through frost.",
            "tone_sandhi_and_pitch_modulation": "Second tone to neutral tone: 'zhú zi' (35-neutral). Rise crisply on 'zhú' and drop gently into a light, unstressed 'zi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "笃", "pinyin": "dǔ", "meaning_en": "sincere; devoted", "distinction_note": "Horse radical 马 under the bamboo crown ⺮"},
                {"character": "竿", "pinyin": "gān", "meaning_en": "pole; rod", "distinction_note": "Shield radical 干 under the bamboo crown ⺮"},
                {"character": "笋", "pinyin": "sǔn", "meaning_en": "bamboo shoot", "distinction_note": "Ten radical 十 or 尹 variant under ⺮"},
                {"character": "简", "pinyin": "jiǎn", "meaning_en": "simple; bamboo slip", "distinction_note": "Door radical 间 under ⺮"}
            ],
            "etymological_cognates": [
                {"character": "竹林", "pinyin": "zhúlín", "gloss_en": "bamboo forest / grove"},
                {"character": "竹笋", "pinyin": "zhúsǔn", "gloss_en": "bamboo shoots (edible)"},
                {"character": "竹竿", "pinyin": "zhúgān", "gloss_en": "bamboo pole"},
                {"character": "竹叶", "pinyin": "zhúyè", "gloss_en": "bamboo leaf"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "竹子 refers specifically to the bamboo plant, its hollow canes, and cultural aesthetic connotations.",
            "contrasts": [
                {"id": 1, "compared_word": "竹子 vs. 树木", "pinyin": "shùmù", "analysis": "树木 designates woody broadleaf or coniferous trees with bark and solid trunks, unlike hollow-stemmed 竹子."},
                {"id": 2, "compared_word": "竹子 vs. 芦苇", "pinyin": "lúwěi", "analysis": "芦苇 refers to wetlands reeds, which lack the hard woody resilience and tall timber quality of 竹子."},
                {"id": 3, "compared_word": "竹子 vs. 竹笋", "pinyin": "zhúsǔn", "analysis": "竹笋 denotes the tender edible young shoots emerging from the soil, prior to maturing into adult 竹子."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "“宁可食无肉，不可居无竹。”北宋文豪苏东坡的名句道出了中国文人对竹子的偏爱。在老北京四合院中栽种几竿竹子，春发绿枝，冬经寒霜而不凋，使幽静的庭院平添了几分超尘脱俗的高雅风韵。",
                "pinyin": "'Nìngkě shí wú ròu, bùkě jū wú zhú.' Běisòng wénháo Sū Dōngpō de míngjù dàochū le Zhōngguó wénrén duì zhúzi de piān'ài. Zài lǎo Běijīng sìhéyuàn zhōng zāizhòng jǐ gān zhúzi, chūn fā lǜzhī, dōng jīng hánshuāng ér bù diāo, shǐ yōujìng de tíngyuàn píngtiān le jǐ fēn chāochén-tuōsú de gāoyǎ fēngyùn.",
                "en": "'Better to dine without meat than live without bamboo.' Su Dongpo's famous line captured scholars' devotion. Planting bamboo in courtyards preserved evergreen grace through frost, lending tranquil compounds an ethereal elegance.",
                "es": "'Mejor comer sin carne que habitar sin bambú.' La célebre máxima de Su Dongpo encarna la devoción letrada. Unas cañas de bambú en el patio desafiaban la escarcha sin marchitarse, confiriendo al hogar un aire noble y desprendido."
            },
            {
                "id": "#2",
                "hanzi": "竹子不仅具有优美的观赏价值，在日常生活中更有极广的实用功能。从结实耐磨的竹席、轻巧坚固的竹椅，到文房四宝中的竹制毛笔筒，竹子以其坚韧与柔韧并存的独特物理特质，深深融入了中国百姓衣食住行的方方面面。",
                "pinyin": "Zhúzi bùjǐn jùyǒu yōuměi de guānshǎng jiàzhí, zài rìcháng shēnghuó zhōng gèng yǒu jí guǎng de shíyòng gōngnéng. Cóng jiēshi-nàimó de zhúxí, qīngqiǎo jiāngù de zhúyǐ, dào wénfángsìbǎo zhōng de zhúzhì máobǐtǒng, zhúzi yǐ qí jiānrèn yǔ róurèn bìngcún de dútè wùlǐ tèzhì, shēnkè róngrù le Zhōngguó bǎixìng yī-shí-zhù-xíng de fāngfāng-miànmiàn.",
                "en": "Beyond ornamental grace, bamboo serves extensive practical utilities in daily life. From durable bamboo mats and light chairs to brush holders on writing desks, its balance of strength and flexibility touches every dimension of living.",
                "es": "Más allá de su belleza paisajística, el bambú atesora múltiples utilidades prácticas. Desde esteras resistentes y sillas ligeras hasta portalápices de caligrafía, aúna flexibilidad y firmeza para integrarse en la vida diaria."
            }
        ]
    },

    # 25 则
    {
        "id": "25",
        "hanzi": "则",
        "pinyin": "zé",
        "part_of_speech": "Conjunction",
        "meanings_summary": {
            "en": "whereas; on the other hand; then; rule; item",
            "es": "mientras que; por el contrario; en cambio; norma; artículo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Conjunction",
                "register": "Standard",
                "definition_en": "used to indicate contrast between clauses (whereas / while), or conditional sequence (then)",
                "definition_es": "empleado para marcar contraste entre proposiciones (en cambio, mientras que) o consecuencia lógica",
                "example_phrase": "东厢房住长子，西厢房则住次子 (eldest son in east wing, whereas second son in west wing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在老北京四合院中，正房通常由家里的长辈居住，东西两侧的厢房则安排给晚辈读书生活。",
                "pinyin": "Zài lǎo Běijīng sìhéyuàn zhōng, zhèngfáng tōngcháng yóu jiālǐ de zhǎngbèi jūzhù, dōngxī liǎngcè de xiāngfáng zé ānpái gěi wǎnbèi dúshū shēnghuó.",
                "en": "In old Beijing courtyards, the main room was usually occupied by family elders, whereas the side wings were allocated for juniors to study and live.",
                "es": "En el siheyuan pekinés, la estancia principal era para los mayores, mientras que las alas laterales se destinaban al estudio y descanso de los jóvenes."
            },
            {
                "id": "#2",
                "hanzi": "遇到突发技术故障时，新手往往容易手忙脚乱，经验丰富的工程师则能沉着冷静地排查隐患。",
                "pinyin": "Yùdào tūfā jìshù gùzhàng shí, xīnshǒu wǎngwǎng róngyì shǒumáng-jiǎoluàn, jīngyàn fēngfù de gōngchéngshī zé néng chénzhuó-lěngjìng de páichá yǐnhuàn.",
                "en": "When confronting unexpected technical breakdowns, novices tend to panic, whereas seasoned engineers investigate hidden risks calmly.",
                "es": "Ante averías técnicas imprevistas, los novatos suelen perder la serenidad, mientras que los ingenieros curtidos localizan los fallos con calma."
            }
        ],
        "collocations": [
            {"hanzi": "一则消息", "en": "an item of news (classifier 则)"},
            {"hanzi": "规则法则", "en": "rules and regulations"},
            {"hanzi": "反之则不然", "en": "the reverse, on the contrary, is not so"},
            {"hanzi": "原则问题", "en": "matter of principle"},
            {"hanzi": "细则规定", "en": "detailed rules / bylaws"},
            {"hanzi": "多则……少则……", "en": "at most ..., at least ..."}
        ],
        "idioms": [
            {"hanzi": "穷则思变", "pinyin": "qióng zé sī biàn", "meaning_en": "when at an impasse, think of change and reform"},
            {"hanzi": "以身作则", "pinyin": "yǐ shēn zuò zé", "meaning_en": "set an example by one's own actions"},
            {"hanzi": "有则改之", "pinyin": "yǒu zé gǎi zhī", "meaning_en": "correct errors if you have them, guard against them if not"},
            {"hanzi": "物极必反", "pinyin": "wù jí bì fǎn", "meaning_en": "things turn into opposites when reaching extremes"}
        ],
        "character_decomposition": [
            {
                "character": "则",
                "pinyin": "zé",
                "meaning_en": "rule; law; standard; whereas; then",
                "meaning_es": "norma; ley; criterio; en cambio; entonces",
                "radical": "刂",
                "radical_meaning_en": "knife / blade",
                "meaning_component": "贝 (bronze cauldron / cowrie currency) + 刂 (engraving knife)",
                "sound_component": "则 (zé)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Using a knife 刂 to carve binding statutory laws into bronze vessels 贝; signifies standard laws and conditional clauses.",
                "visual_mnemonic_story_en": "Carving precise statutory regulations into a bronze vessel with a knife (刂) to establish standard rules (则).",
                "visual_mnemonic_story_es": "Grabar ordenanzas con un buril (刂) sobre el bronce ceremonial para consagrar la ley (则).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BCLN",
                "traditional": "則"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Carving standard dividing lines with a knife (刂) establishes clear criteria and contrasts (则).",
            "composite_memory_hook_es": "Marcar deslindes normativos con la hoja del buril (刂) define el criterio legal y la contraposición (则).",
            "cultural_and_cognitive_roots": "Essential classical particle functioning as a pivotal turning marker in prose to balance paired contrasts and deductions.",
            "tone_sandhi_and_pitch_modulation": "Second tone: 'zé' (35). Lift the pitch swiftly with crisp tonal clarity."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "恻", "pinyin": "cè", "meaning_en": "sorrow; sympathy", "distinction_note": "Heart radical 忄 to the left of 则"},
                {"character": "侧", "pinyin": "cè", "meaning_en": "side; incline", "distinction_note": "Person radical 亻 to the left of 则"},
                {"character": "厕", "pinyin": "cè", "meaning_en": "toilet; latrine", "distinction_note": "Shelter radical 厂 around 则"},
                {"character": "刚", "pinyin": "gāng", "meaning_en": "just; firm", "distinction_note": "Mountain radical 冈 to the left of 刂"}
            ],
            "etymological_cognates": [
                {"character": "原则", "pinyin": "yuánzé", "gloss_en": "principle; fundamental rule"},
                {"character": "法则", "pinyin": "fǎzé", "gloss_en": "law; rule of nature"},
                {"character": "准则", "pinyin": "zhǔnzé", "gloss_en": "norm; criterion"},
                {"character": "规则", "pinyin": "guīzé", "gloss_en": "rule; regulation"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "则 serves primarily in formal prose as a contrastive connective marker highlighting differing parallel behaviors.",
            "contrasts": [
                {"id": 1, "compared_word": "则 vs. 但是", "pinyin": "dànshì", "analysis": "但是 introduces a sharp spoken adversative turn ('but'), whereas 则 gently sets up parallel contrasts ('whereas/while')."},
                {"id": 2, "compared_word": "则 vs. 却", "pinyin": "què", "analysis": "却 highlights an outcome contrary to expectations, whereas 则 simply aligns two contrasting facts side by side."},
                {"id": 3, "compared_word": "则 vs. 而", "pinyin": "ér", "analysis": "而 links general coordination or transition, whereas 则 emphasizes categorical divergence between subjects."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统哲学强调阴阳互济。在四合院的建筑格局中，高大敞亮的正房属阳，处于主导地位；相对低矮的配房与厢房则属阴，处于辅佐地位。二者分工明确、刚柔并济，体现了和谐共生的古老宇宙观。",
                "pinyin": "Zhōngguó chuántǒng zhéxué qiángdiào yīnyáng-hùjì. Zài sìhéyuàn de jiànzhù géjú zhōng, gāodà kuānchǎng de zhèngfáng shǔ yáng, chǔyú zhǔdǎo dìwèi; xiāngduì dī'ǎi de pèifáng yǔ xiāngfáng zé shǔ yīn, chǔyú fǔzuǒ dìwèi. Èrzhě fēngōng míngquè, gāngróu-bìngjì, tǐxiàn le héxié-gòngshēng de gǔlǎo yǔzhòuguān.",
                "en": "Traditional Chinese philosophy stresses mutual complementarity between Yin and Yang. In courtyards, the spacious main room belongs to Yang in dominant standing, whereas lower wing-rooms belong to Yin in auxiliary role, balancing harmony.",
                "es": "La filosofía tradicional china postula el equilibrio entre el yin y el yang. En el siheyuan, la amplia estancia principal representa la fuerza yang, mientras que las alas laterales encarnan la mesura yin, conjugando orden cósmico."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的市场风云，盲目跟风的企业往往容易陷入危机，坚守核心原则与持续技术创新的企业则能化险为夷。审时度势、以变应变，则是优秀管理者带领团队在激烈的商业竞争中立于不败之地的制胜法宝。",
                "pinyin": "Miànduì shùnxī-wànbiàn de shìchǎng fēngyún, mángmù gēnfēng de qǐyè wǎngwǎng róngyì xiànrù wēijī, jiānshǒu héxīn yuánzé yǔ chíxù jìshù chuàngxīn de qǐyè zé néng huàxiǎn-wéiyí. Shěnshí-duóshì, yǐ biàn yīng biàn, zé shì yōuxiù guǎnlǐzhě dàilǐng tuánduì zài jīliè de shāngyè jìngzhēng zhōng lìyú-bùbàizhīdì de zhìshèng fǎbǎo.",
                "en": "Facing unpredictable market tides, enterprises following trends blindly fall into crises, whereas firms maintaining core principles and technical innovation turn perils into opportunities, mastering dynamic adaptability.",
                "es": "Ante la volatilidad del mercado, las empresas que imitan a ciegas caen en crisis, mientras que las firmas fieles a sus principios e innovación superan la adversidad; adaptarse al cambio constituye la clave del éxito."
            }
        ]
    },

    # 26 金鱼
    {
        "id": "26",
        "hanzi": "金鱼",
        "pinyin": "jīn yú",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "goldfish",
            "es": "pez dorado; pez de colores"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a small domesticated freshwater cyprinid fish, bred for brilliant colors and ornamental beauty in garden ponds and bowls",
                "definition_es": "pequeño pez de agua dulce de vistosos colores y aletas ondulantes, criado con fines ornamentales en estanques y peceras",
                "example_phrase": "大鱼缸里养金鱼 (raise goldfish in a large fishbowl)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的庭院正中，常常摆放着一口青石大鱼缸，几尾红艳艳的金鱼在浮萍间悠然游动。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de tíngyuàn zhèngzhōng, chángcháng bǎifàng zhe yī kǒu qīngshí dà yúgāng, jǐ wěi hóngyànyàn de jīnyú zài fúpíng jiān yōurán yóudòng.",
                "en": "In the center of old Beijing courtyards, a large bluestone fish bowl often stood, where crimson goldfish glided leisurely among duckweed.",
                "es": "En medio del patio del siheyuan pekinés solía colocarse una pila de piedra donde varios peces dorados nadaban apacibles entre lentejas de agua."
            },
            {
                "id": "#2",
                "hanzi": "公园人工湖畔聚集了许多儿童，兴高采烈地用小网兜捞着游来游去的小金鱼。",
                "pinyin": "Gōngyuán réngōnghúpàn jùjí le xǔduō értóng, xìnggāo-cǎiliè de yòng xiǎo wǎngdōu lāo zhe yóu lái yóu qù de xiǎo jīnyú.",
                "en": "Many children gathered by the park's artificial lake, joyfully scooping up swimming little goldfish with small dip nets.",
                "es": "Junto al estanque del parque se congregaban niños entusiasmados, atrapando con salabardos los pececillos dorados que surcaban el agua."
            }
        ],
        "collocations": [
            {"hanzi": "几尾金鱼", "en": "several goldfish (classifier 尾/条)"},
            {"hanzi": "金鱼缸", "en": "goldfish bowl / aquarium"},
            {"hanzi": "养金鱼", "en": "keep / raise goldfish"},
            {"hanzi": "喂金鱼", "en": "feed goldfish"},
            {"hanzi": "红金鱼", "en": "red goldfish"},
            {"hanzi": "金鱼摆尾", "en": "goldfish swishing its tail"}
        ],
        "idioms": [
            {"hanzi": "金玉满堂", "pinyin": "jīn yù mǎn táng", "meaning_en": "hall brimming with gold and jade; boundless wealth and learning"},
            {"hanzi": "如鱼得水", "pinyin": "rú yú dé shuǐ", "meaning_en": "like a fish back in water; in one's natural element"},
            {"hanzi": "年年有余", "pinyin": "nián nián yǒu yú", "meaning_en": "surplus year after year (homophonic pun on 鱼 and 余)"},
            {"hanzi": "鱼跃鸢飞", "pinyin": "yú yuè yuān fēi", "meaning_en": "fishes leap and hawks soar; nature thriving in freedom"}
        ],
        "character_decomposition": [
            {
                "character": "金",
                "pinyin": "jīn",
                "meaning_en": "gold; metal; golden; money",
                "meaning_es": "oro; metal; dorado; dinero",
                "radical": "金",
                "radical_meaning_en": "gold / metal",
                "meaning_component": "人 (roof/cover) + 土 (earth) + two gold nuggets buried inside",
                "sound_component": "金 (jīn)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Precious nuggets of gleaming metal buried deep inside the subterranean earth 土; signifies gold.",
                "visual_mnemonic_story_en": "Precious gold nuggets shining beneath the earthen surface (金).",
                "visual_mnemonic_story_es": "Pepitas de oro refulgentes enterradas en las entrañas de la tierra (金).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OP",
                "traditional": "金"
            },
            {
                "character": "鱼",
                "pinyin": "yú",
                "meaning_en": "fish",
                "meaning_es": "pez; pescado",
                "radical": "鱼",
                "radical_meaning_en": "fish",
                "meaning_component": "pictograph of fish head, scale body, and fin tail",
                "sound_component": "鱼 (yú)",
                "stroke_count": 8,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictograph of a fish showing head ⺈, scaled belly 田, and tail 一/灬.",
                "visual_mnemonic_story_en": "A graceful fish with scales and a swishing tail gliding through water (鱼).",
                "visual_mnemonic_story_es": "Un pez estilizado con escamas y aleta caudal nadando en aguas cristalinas (鱼).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "NWM",
                "traditional": "魚"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A shining golden-scaled (金) aquatic creature (鱼) is an ornamental goldfish (金鱼).",
            "composite_memory_hook_es": "Un pez (鱼) de brillantes escamas color oro (金) conforma el pez dorado (金鱼).",
            "cultural_and_cognitive_roots": "Bred in China since the Song Dynasty; '金鱼' puns with '金玉' (gold and jade), symbolizing wealth and good fortune in domestic compounds.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'jīn yú' (55-35). Clear elevated pitch on 'jīn', rising smoothly on 'yú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "全", "pinyin": "quán", "meaning_en": "all; whole; complete", "distinction_note": "Roof 人 over 王 instead of full metal form"},
                {"character": "釜", "pinyin": "fǔ", "meaning_en": "cauldron; pot", "distinction_note": "Father radical 父 above 金"},
                {"character": "鲁", "pinyin": "lǔ", "meaning_en": "blunt; Shandong", "distinction_note": "Fish 鱼 above sun 日"},
                {"character": "鲜", "pinyin": "xiān", "meaning_en": "fresh; delicious", "distinction_note": "Sheep 羊 beside fish 鱼"}
            ],
            "etymological_cognates": [
                {"character": "黄金", "pinyin": "huángjīn", "gloss_en": "gold metal"},
                {"character": "金黄色", "pinyin": "jīnhuángsè", "gloss_en": "golden yellow color"},
                {"character": "游鱼", "pinyin": "yóuyú", "gloss_en": "swimming fish"},
                {"character": "捕鱼", "pinyin": "bǔyú", "gloss_en": "catch fish; fishing"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "金鱼 specifically denotes domestic ornamental varieties of carp cultivated for vibrant color and decorative tanks.",
            "contrasts": [
                {"id": 1, "compared_word": "金鱼 vs. 鲤鱼", "pinyin": "lǐyú", "analysis": "鲤鱼 denotes common culinary carp, while 金鱼 are bred purely as ornamental pets in garden bowls."},
                {"id": 2, "compared_word": "金鱼 vs. 热带鱼", "pinyin": "rèdàiyú", "analysis": "热带鱼 refers to warm-water tropical species requiring heated tanks, whereas 金鱼 are temperate freshwater fish."},
                {"id": 3, "compared_word": "金鱼 vs. 鲨鱼", "pinyin": "shāyú", "analysis": "鲨鱼 denotes predatory marine sharks, entirely distinct from docile domestic 金鱼."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院有“天棚鱼缸石榴树，先生肥狗胖丫头”的俗谚，其中大鱼缸里养金鱼是不可或缺的闲趣。坐在葡萄架下，看着大瓷缸里金鱼摆动着飘逸如丝的尾鳍游来游去，生活平添了无限恬淡与宁静。",
                "pinyin": "Lǎo Běijīng sìhéyuàn yǒu 'tiānpéng yúgāng shíliushù, xiānsheng féigǒu pàng yātou' de súyàn, qízhōng dà yúgāng lǐ yǎng jīnyú shì bùkě-huòquē de xiánqù. Zuò zài pútáojià xià, kàn zhe dà cígāng lǐ jīnyú bǎidòng zhe piāoyì rú sī de wěiqí yóu lái yóu qù, shēnghuó píngtiān le wúxiàn tiándàn yǔ níngjìng.",
                "en": "Old Beijing folklore recalls courtyards with 'awnings, fish bowls, and pomegranates.' Keeping goldfish in stone basins was an indispensable pleasure; watching their silky fins flutter brought immense serenity to everyday life.",
                "es": "Un viejo adagio pekinés evocaba los patios con 'toldos, estanques y granados'. Criar peces dorados en pilas de barro era un placer inexcusable: ver ondular sus sedosas colas bajo la parra impregnaba la vida de calma."
            },
            {
                "id": "#2",
                "hanzi": "中国金鱼的培育历史已有一千多年，被誉为“东方圣鱼”。古代养鱼名家通过代代精心选育，培育出了龙睛、水泡、狮子头等数百种体态优美、色彩斑斓的品种。这种将生命之美融入日常闲赏的艺术，生动展现了中华造物智慧。",
                "pinyin": "Zhōngguó jīnyú de péiyù lìshǐ yǐ yǒu yīqiān duō nián, bèi yù wéi 'dōngfāng shèngyú'. Gǔdài yǎngyú míngjiā tōngguò dàidài jīngxīn xuǎnyù, péiyù chū le lóngjīng, shuǐpào, shīzitóu děng shùbǎi zhǒng tǐtài yōuměi, sècǎi bānlán de pǐnzhǒng. Zhè zhǒng jiāng shēngmìng zhī měi róngrù rìcháng xiánshǎng de yìshù, shēngdòng zhǎnxiàn le Zhōnghuá zàowù zhìhuì.",
                "en": "China's breeding of goldfish spans over a millennium, earning them the title 'Sacred Fish of the Orient.' Master breeders developed hundreds of graceful varieties, integrating the beauty of nature into leisurely aesthetic contemplation.",
                "es": "La cría del pez dorado en China supera el milenio, apodado 'pez sagrado de Oriente'. Selecciones milenarias dieron origen a variedades de insólita belleza, uniendo el arte de la contemplación y la maestría zootécnica tradicional."
            }
        ]
    },

    # 27 创造
    {
        "id": "27",
        "hanzi": "创造",
        "pinyin": "chuàng zào",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to create; produce; bring about; innovation",
            "es": "crear; producir; engendrar; innovación"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to bring something entirely new into existence through intellect, labor, imagination, or skill",
                "definition_es": "dar existencia a algo nuevo o inédito mediante el intelecto, trabajo, inventiva o destreza",
                "example_phrase": "创造美好生活 (create a wonderful life)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "中国古代劳动人民凭借非凡的智慧，在四合院的规整天地中创造出了人与自然亲密交融的生活环境。",
                "pinyin": "Zhōngguó gǔdài láodòng rénmín píngjiè fēifán de zhìhuì, zài sìhéyuàn de guīzhěng tiāndì zhōng chuàngzào chū le rén yǔ zìrán qīnmì jiāoróng de shēnghuó huánjìng.",
                "en": "Relying on remarkable wisdom, ancient Chinese working people created a living environment where humanity and nature harmoniously blended inside quadrangles.",
                "es": "Con sabiduría admirable, el pueblo trabajador de la China clásica creó en el siheyuan un entorno residencial donde el hombre y la naturaleza se funden."
            },
            {
                "id": "#2",
                "hanzi": "科研团队通过夜以继日的攻关试验，成功创造了一项具有国际自主知识产权的核心技术专利。",
                "pinyin": "Kēyán tuánduì tōngguò yèyǐjìrì de gōngguān shìyàn, chénggōng chuàngzào le yī xiàng jùyǒu guójì zìzhǔ zhīshichǎnquán de héxīn jìshù zhuānlì.",
                "en": "Through day-and-night testing breakthroughs, the research team successfully created a core technological patent with international proprietary rights.",
                "es": "A través de infatigables pruebas de laboratorio, el equipo científico creó con éxito una patente técnica primordial de titularidad propia."
            }
        ],
        "collocations": [
            {"hanzi": "创造奇迹", "en": "create miracles"},
            {"hanzi": "创造财富", "en": "create wealth"},
            {"hanzi": "创造力", "en": "creativity / creative power"},
            {"hanzi": "创造价值", "en": "create value"},
            {"hanzi": "创造良好条件", "en": "create favorable conditions"},
            {"hanzi": "开拓创造", "en": "pioneer and create"}
        ],
        "idioms": [
            {"hanzi": "巧夺天工", "pinyin": "qiǎo duó tiān gōng", "meaning_en": "superb craftsmanship excelling nature itself"},
            {"hanzi": "标新立异", "pinyin": "biāo xīn lì yì", "meaning_en": "pioneer something original and fresh"},
            {"hanzi": "开天辟地", "pinyin": "kāi tiān pì dì", "meaning_en": "split open heaven and earth; epoch-making creation"},
            {"hanzi": "别出心裁", "pinyin": "bié chū xīn cái", "meaning_en": "display original and creative genius"}
        ],
        "character_decomposition": [
            {
                "character": "创",
                "pinyin": "chuàng",
                "meaning_en": "start; create; initiate; establish",
                "meaning_es": "iniciar; crear; fundar; emprender",
                "radical": "刂",
                "radical_meaning_en": "knife / cutting edge",
                "meaning_component": "仓 (storehouse / granary structure) + 刂 (cutting tool)",
                "sound_component": "仓 (cāng)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Carving new timber foundations with a blade 刂 to build a new grain storehouse 仓; to initiate or create.",
                "visual_mnemonic_story_en": "Chiseling raw materials with a sharp knife (刂) to pioneer an innovative design (创).",
                "visual_mnemonic_story_es": "Desbastar la madera con un cuchillo (刂) para fundar una obra nueva y singular (创).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OSLN",
                "traditional": "創"
            },
            {
                "character": "造",
                "pinyin": "zào",
                "meaning_en": "make; build; construct; manufacture",
                "meaning_es": "hacer; fabricar; construir; elaborar",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (dynamic motion) + 告 (speech proclamation / bull horns)",
                "sound_component": "告 (gào)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Active physical motion 辶 executing an announced plan 告 to construct tangible works; to make or build.",
                "visual_mnemonic_story_en": "Taking swift action on foot (辶) to build and fabricate an impressive artifact (造).",
                "visual_mnemonic_story_es": "Emprender la marcha (辶) para confeccionar y levantar una edificación palpable (造).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YHGR",
                "traditional": "造"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Initiating a pioneering start (创) and fashioning it into reality (造) means to create (创造).",
            "composite_memory_hook_es": "Fundar una novedad (创) y fabricarla con destreza (造) sintetiza el acto creador (创造).",
            "cultural_and_cognitive_roots": "Blends the conceptual inception of an idea (创) with the manual execution of building it (造), driving human civilization.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'chuàng zào' (51-51). Articulate both syllables with energetic downward punch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "仓", "pinyin": "cāng", "meaning_en": "granary; storehouse", "distinction_note": "Lacks the knife radical 刂 on the right"},
                {"character": "抢", "pinyin": "qiǎng", "meaning_en": "rob; scramble for", "distinction_note": "Hand radical 扌 on left of 仓"},
                {"character": "选", "pinyin": "xuǎn", "meaning_en": "choose; elect", "distinction_note": "First radical 先 under 辶 instead of 告"},
                {"character": "迫", "pinyin": "pò", "meaning_en": "force; compel", "distinction_note": "White radical 白 under 辶 instead of 告"}
            ],
            "etymological_cognates": [
                {"character": "创新", "pinyin": "chuàngxīn", "gloss_en": "innovate; innovation"},
                {"character": "创业", "pinyin": "chuàngyè", "gloss_en": "start an enterprise / venture"},
                {"character": "制造", "pinyin": "zhìzào", "gloss_en": "manufacture; fabricate"},
                {"character": "塑造", "pinyin": "sùzào", "gloss_en": "shape; mold; sculpt"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "创造 emphasizes bringing unprecedented new ideas, artworks, or social wealth into reality from scratch.",
            "contrasts": [
                {"id": 1, "compared_word": "创造 vs. 制造", "pinyin": "zhìzào", "analysis": "制造 focuses on routine industrial manufacturing along existing blueprints, whereas 创造 invents original concepts."},
                {"id": 2, "compared_word": "创造 vs. 发现", "pinyin": "fāxiàn", "analysis": "发现 reveals pre-existing things hitherto unnoticed (e.g. islands, laws), while 创造 constructs entirely novel things."},
                {"id": 3, "compared_word": "创造 vs. 模仿", "pinyin": "mófǎng", "analysis": "模仿 is the direct antonym meaning to copy or reproduce existing templates."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代建筑工匠在四合院的营建中展现了惊人的创造才能。他们巧妙利用砖雕、木雕与彩绘艺术，在普通的房檐与门簪上创造出寓意深远的图案，把质朴的居住空间升华为富有诗意与人文温度的艺术殿堂。",
                "pinyin": "Zhōngguó gǔdài jiànzhù gōngjiàng zài sìhéyuàn de yíngjiàn zhōng zhǎnxiàn le jīngrén de chuàngzào cáinéng. Tāmen qiǎomiào lìyòng zhuāndiāo, mùdiāo yǔ cǎihuì yìshù, zài pǔtōng de fángyán yǔ ménzān shang chuàngzào chū yùyì shēnyuǎn de tú'àn, bǎ zhìpǔ de jūzhù kōngjiān shēnghuá wéi fùyǒu shīyì yǔ rénwén wēndù de yìshù diàntáng.",
                "en": "Ancient artisans demonstrated astounding creative talent constructing courtyards. Ingeniously employing brick carvings and woodwork on eaves, they created profound motifs, sublimating living spaces into artistic halls steeped in poetic warmth.",
                "es": "Los artesanos constructores de la China clásica hicieron gala de un pasmoso ingenio creador. Mediante tallas en ladrillo y madera, crearon motivos de hondo simbolismo en los aleros, transformando la vivienda en una joya artística de viva poesía."
            },
            {
                "id": "#2",
                "hanzi": "创新是推动人类文明进步的根本动力。当代青年应当敢于打破传统思维的陈旧藩篱，在科学技术与文化艺术的广阔天地中勇于创造。通过持续不断的探索与实践，我们才能为社会创造出更具价值的成果，让生活变得更加美好。",
                "pinyin": "Chuàngxīn shì tuīdòng rénlèi wénmíng jìnbù de gēnběn dònglì. Dāngdài qīngnián yīngdāng gǎnyú dǎpò chuántǒng sīwéi de chénjiù fānlí, zài kēxué jìshù yǔ wénhuà yìshù de guǎngkuò tiāndì zhōng yǒngyú chuàngzào. Tōngguò chíxù-bùduàn de tànsuǒ yǔ shíjiàn, wǒmen cái néng wèi shèhuì chuàngzào chū gèng jù jiàzhí de chéngguǒ, ràng shēnghuó biànde gèngjiā měihǎo.",
                "en": "Innovation serves as the fundamental engine driving human progress. Modern youth must dare to shatter dogmas and create courageously across arts and sciences. Constant exploration generates higher value, enriching human existence.",
                "es": "La innovación constituye el motor cardinal del avance humano. La juventud de hoy debe atreverse a derribar dogmas vetustos y crear con audacia en las artes y las ciencias. La experimentación continua crea valor perdurable para el bienestar común."
            }
        ]
    },

    # 28 情趣
    {
        "id": "28",
        "hanzi": "情趣",
        "pinyin": "qíng qù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "emotional appeal; charm; aesthetic delight; taste; interest",
            "es": "encanto; gusto estético; deleite; atractivo emocional"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "aesthetic charm, emotional interest, or refined taste that brings delight to everyday life",
                "definition_es": "gracia, encanto estético o refinamiento afectivo que ameniza y eleva la vida cotidiana",
                "example_phrase": "富有生活情趣 (rich in life's charm and flavor)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老北京四合院中种花养鸟、摆石理水的生活方式，处处充满了悠闲高雅的东方生活情趣。",
                "pinyin": "Lǎo Běijīng sìhéyuàn zhōng zhònghuā yǎngniǎo, bǎishí lǐshuǐ de shēnghuó fāngshì, chùchù chōngmǎn le yōuxián gāoyǎ de dōngfāng shēnghuó qíngqù.",
                "en": "The lifestyle of growing flowers, keeping pet birds, and arranging rockeries in courtyards brimmed with relaxed, refined Eastern life charm.",
                "es": "El modo de vida del siheyuan pekinés, cultivando flores, aves canoras y rocallas, rebosaba del distinguido encanto estético del sosiego oriental."
            },
            {
                "id": "#2",
                "hanzi": "小李在书房里摆放了一盆苍劲的文竹与精致的紫砂茶具，使整个房间增添了浓郁的文雅情趣。",
                "pinyin": "Xiǎo Lǐ zài shūfáng lǐ bǎifàng le yī pén cāngjìn de wénzhú yǔ jīngzhì de zǐshā chájù, shǐ zhěnggè fángjiān zēngtiān le nóngyù de wényǎ qíngqù.",
                "en": "Xiao Li arranged a vigorous asparagus fern and delicate clay tea set in his study, infusing the entire room with refined scholarly charm.",
                "es": "Xiao Li dispuso en su estudio un bonsái y un juego de té de gres fino, impregnando la estancia de un elegante gusto letrado."
            }
        ],
        "collocations": [
            {"hanzi": "生活情趣", "en": "charm of daily life / zest for living"},
            {"hanzi": "高雅情趣", "en": "refined aesthetic taste / elegant delight"},
            {"hanzi": "富有情趣", "en": "rich in aesthetic charm and interest"},
            {"hanzi": "增添情趣", "en": "add charm / enhance delight"},
            {"hanzi": "别有情趣", "en": "possess a unique charm of its own"},
            {"hanzi": "低级情趣", "en": "vulgar taste / low interest"}
        ],
        "idioms": [
            {"hanzi": "雅俗共赏", "pinyin": "yǎ sú gòng shǎng", "meaning_en": "enjoyed by both refined scholars and the common folk alike"},
            {"hanzi": "自得其乐", "pinyin": "zì dé qí lè", "meaning_en": "find contentment and delight in one's own hobbies"},
            {"hanzi": "情真意切", "pinyin": "qíng zhēn yì qiè", "meaning_en": "genuine feelings and heartfelt sincerity"},
            {"hanzi": "意趣盎然", "pinyin": "yì qù àng rán", "meaning_en": "brimming with rich flavor and engaging delight"}
        ],
        "character_decomposition": [
            {
                "character": "情",
                "pinyin": "qíng",
                "meaning_en": "feeling; emotion; affection; passion",
                "meaning_es": "sentimiento; afecto; emoción; pasión",
                "radical": "忄",
                "radical_meaning_en": "heart",
                "meaning_component": "忄 (heart feeling) + 青 (lush verdant youth / clarity)",
                "sound_component": "青 (qīng)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spontaneous feelings bubbling forth from the heart 忄 as fresh and pure as green shoots 青.",
                "visual_mnemonic_story_en": "A heart (忄) blooming with fresh, verdant emotions like spring greenery (情).",
                "visual_mnemonic_story_es": "Un corazón (忄) que vibra con sentimientos limpios y lozanos como la primavera (情).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "PQB",
                "traditional": "情"
            },
            {
                "character": "趣",
                "pinyin": "qù",
                "meaning_en": "interest; delight; fun; flavor",
                "meaning_es": "interés; deleite; gracia; gusto",
                "radical": "走",
                "radical_meaning_en": "walk / run",
                "meaning_component": "走 (hasten toward) + 取 (grasp with hands / ear focus)",
                "sound_component": "取 (qǔ)",
                "stroke_count": 15,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Hurrying eagerly on foot 走 to seize and enjoy 取 something captivating; denotes fun and charm.",
                "visual_mnemonic_story_en": "Rushing forward enthusiastically (走) to grasp an engaging, delightful experience (趣).",
                "visual_mnemonic_story_es": "Avanzar con paso ágil (走) para asir una experiencia amena y deleitable (趣).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GOSE",
                "traditional": "趣"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Heartfelt sentiment (情) combined with captivating delight (趣) produces refined emotional charm (情趣).",
            "composite_memory_hook_es": "El sentimiento hondo (情) enlazado al deleite lúdico (趣) engendra el encanto estético de la vida (情趣).",
            "cultural_and_cognitive_roots": "A core concept of classical literati aesthetics valuing tea, calligraphy, zither, and gardening to transcend mundane chores.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'qíng qù' (35-51). Lift cleanly on 'qíng' and conclude with an expressive downward slope on 'qù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "清", "pinyin": "qīng", "meaning_en": "clear; pure", "distinction_note": "Water radical 氵 on left instead of heart 忄"},
                {"character": "晴", "pinyin": "qíng", "meaning_en": "clear; sunny sky", "distinction_note": "Sun radical 日 on left instead of heart 忄"},
                {"character": "赶", "pinyin": "gǎn", "meaning_en": "rush; catch up", "distinction_note": "Shield radical 干 beside 走 instead of 取"},
                {"character": "越", "pinyin": "yuè", "meaning_en": "surpass; cross over", "distinction_note": "Halberd radical 戉 beside 走 instead of 取"}
            ],
            "etymological_cognates": [
                {"character": "兴趣", "pinyin": "xìngqù", "gloss_en": "interest; hobby"},
                {"character": "趣味", "pinyin": "qùwèi", "gloss_en": "fun; interest; taste"},
                {"character": "情感", "pinyin": "qínggǎn", "gloss_en": "emotion; sentiment"},
                {"character": "心境", "pinyin": "xīnjìng", "gloss_en": "state of mind; mood"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "情趣 denotes aesthetic delight, tasteful hobbies, and poetic sensibility enriching everyday living.",
            "contrasts": [
                {"id": 1, "compared_word": "情趣 vs. 兴趣", "pinyin": "xìngqù", "analysis": "兴趣 is curiosity or preference for a specific activity (sports, games), while 情趣 emphasizes poetic refinement and aesthetic charm."},
                {"id": 2, "compared_word": "情趣 vs. 趣味", "pinyin": "qùwèi", "analysis": "趣味 leans toward playful fun or amusement, whereas 情趣 embodies deeper spiritual taste and romantic nuance."},
                {"id": 3, "compared_word": "情趣 vs. 乏味", "pinyin": "fáwèi", "analysis": "乏味 is the direct antonym meaning dull, bland, and entirely devoid of delight."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统文人极其讲究起居生活的艺术情趣。在四合院的一隅，摆一盆苍翠菖蒲，焚一炉淡雅线香，邀二三知己在廊檐下品茗漫谈，不求富丽堂皇，但求恬淡自得。这种超凡脱俗的生活情趣，滋养着国人的心灵世界。",
                "pinyin": "Zhōngguó chuántǒng wénrén jíqí jiǎngjiu qǐjū shēnghuó de yìshù qíngqù. Zài sìhéyuàn de yī yú, bǎi yī pén cāngcuì chāngpú, fén yī lú dànyǎ xiànxiāng, yāo èr sān zhījǐ zài lángyán xià pǐnmíng màntán, bù qiú fùlì-tánghuáng, dàn qiú tiándàn zìdé. Zhè zhǒng chāofán-tuōsú de shēnghuó qíngqù, zīyǎng zhe guórén de xīnlíng shìjiè.",
                "en": "Traditional literati cultivated refined aesthetic taste in daily living. Tending calamus pots, burning incense, and sipping tea with confidants beneath verandas sought no luxury, but tranquil contentment that nurtured the soul.",
                "es": "Los letrados tradicionales cultivaban con esmero el encanto estético en lo cotidiano. Colocar un cálamo verde, quemar incienso y saborear té con amigos bajo el alero no buscaba la opulencia, sino la serenidad interior que nutre el espíritu."
            },
            {
                "id": "#2",
                "hanzi": "在快节奏的现代生活中，保持对日常琐事的细腻情趣尤为珍贵。在窗台上栽一束芬芳的鲜花，为家人亲手烹制一道精致的小点心，都能让平凡的日子重新焕发光彩。懂得品味生活情趣的人，总能在纷繁复杂的世界里发现美好的诗意。",
                "pinyin": "Zài kuàijiézòu de xiàndài shēnghuó zhōng, bǎochí duì rìcháng suǒshì de xìnì qíngqù yóuwéi zhēnguì. Zài chuāngtái shang zāi yī shù fēnfāng de xiānhuā, wèi jiārén qīnshǒu pēngzhì yī dào jīngzhì de xiǎodiǎnxin, dōu néng ràng píngfán de rìzi chóngxīn huànfā guāngcǎi. Dǒngdé pǐnwèi shēnghuó qíngqù de rén, zǒng néng zài fēnfán-fùzá de shìjiè lǐ fāxiàn měihǎo de shīyì.",
                "en": "Amid modern fast-paced living, preserving delicate charm toward everyday chores is precious. Flowers on windowsills and home-baked pastries illuminate routine days. Those with taste for life's charm always uncover poetic grace amidst chaos.",
                "es": "En la vorágine actual, preservar el deleite estético por los pequeños detalles es un tesoro. Unas flores en la ventana o repostería casera devuelven el brillo a los días ordinarios; quien sabe saborear la vida halla poesía dondequiera que mire."
            }
        ]
    },

    # 29 因而
    {
        "id": "29",
        "hanzi": "因而",
        "pinyin": "yīn ér",
        "part_of_speech": "Conjunction",
        "meanings_summary": {
            "en": "therefore; as a result; thus; consequently",
            "es": "por lo tanto; en consecuencia; por ende; de ahí que"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Conjunction",
                "register": "Standard",
                "definition_en": "connects two clauses to indicate that the latter is the natural consequence, result, or deduction from the former",
                "definition_es": "conector lógico que enlaza dos proposiciones indicando que la segunda es consecuencia directa de la primera",
                "example_phrase": "因而不受干扰 (consequently free from disturbance)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院的四面建筑紧密围合，隔绝了外界街巷的喧嚣，因而能够为院内居民营造出安宁静谧的生活氛围。",
                "pinyin": "Sìhéyuàn de sìmiàn jiànzhù jǐnmì wéihé, géjué le wàijiè jiēxiàng de xuānxīao, yīn'ér nénggòu wèi yuànnèi jūmín yíngzào chū ānníng jìngmì de shēnghuó fēnwéi.",
                "en": "The quadrangle's four-sided structures tightly enclose the space, sealing off exterior alley clamor; as a result, it fosters an ambiance of serene quiet.",
                "es": "Los edificios del siheyuan cierran el recinto aislando el estruendo de los callejones, por lo que brindan a los vecinos un sosiego reconfortante."
            },
            {
                "id": "#2",
                "hanzi": "实验室采用了最先进的高精度自动化仪器，因而大幅度提升了日常科研数据的采集效率与准确度。",
                "pinyin": "Shíyànshì cǎiyòng le zuì xiānjìn de gāojīngdù zìdònghuà yíqì, yīn'ér dàfúdù tíshēng le rìcháng kēyán shùjù de cǎijí xiàolǜ yǔ zhǔnquèdù.",
                "en": "The laboratory adopted state-of-the-art high-precision automated instruments; consequently, data acquisition efficiency and precision soared.",
                "es": "El laboratorio incorporó instrumentación automatizada de alta precisión, mejorando sustancialmente la rapidez y exactitud en la recolección de datos."
            }
        ],
        "collocations": [
            {"hanzi": "因而产生", "en": "consequently produce / arise"},
            {"hanzi": "因而获益", "en": "benefit as a result"},
            {"hanzi": "因而受到好评", "en": "consequently earn high praise"},
            {"hanzi": "因而发生变化", "en": "consequently undergo change"},
            {"hanzi": "因而推断", "en": "deduce as a result"},
            {"hanzi": "因而得名", "en": "derive its name as a result"}
        ],
        "idioms": [
            {"hanzi": "水到渠成", "pinyin": "shuǐ dào qú chéng", "meaning_en": "when water flows, a canal is formed; matters succeed naturally"},
            {"hanzi": "顺理成章", "pinyin": "shùn lǐ chéng zhāng", "meaning_en": "follow logically and smoothly; natural course of events"},
            {"hanzi": "因势利导", "pinyin": "yīn shì lì dǎo", "meaning_en": "guide action along existing momentum"},
            {"hanzi": "防患未然", "pinyin": "fáng huàn wèi rán", "meaning_en": "prevent troubles before they happen"}
        ],
        "character_decomposition": [
            {
                "character": "因",
                "pinyin": "yīn",
                "meaning_en": "cause; reason; because; rely on",
                "meaning_es": "causa; motivo; por; apoyarse en",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (enclosure) + 大 (person resting on mat)",
                "sound_component": "因 (yīn)",
                "stroke_count": 6,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "A person 大 resting securely upon an enclosed sleeping mat 囗; represents the ground, basis, or cause.",
                "visual_mnemonic_story_en": "A person (大) reclining on a woven resting mat (囗) as the basis and reason for rest (因).",
                "visual_mnemonic_story_es": "Una persona (大) descansando sobre una estera (囗), fundamento y causa de su reposo (因).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "WK",
                "traditional": "因"
            },
            {
                "character": "而",
                "pinyin": "ér",
                "meaning_en": "and; yet; but; and then",
                "meaning_es": "y; además; pero; por ende",
                "radical": "而",
                "radical_meaning_en": "beard / whiskers",
                "meaning_component": "pictograph of flowing facial whiskers or chin beard",
                "sound_component": "而 (ér)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Flowing facial whiskers hanging downward; serves as a universal connective marker in speech.",
                "visual_mnemonic_story_en": "Flowing wisps of a sage's beard (而) smoothly connecting thoughts together.",
                "visual_mnemonic_story_es": "Los mechones de la barba de un sabio (而) que enlazan con fluidez ideas sucesivas.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MBLL",
                "traditional": "而"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Taking a cause (因) and carrying it forward (而) yields the conclusive result (因而).",
            "composite_memory_hook_es": "Tomar la causa originaria (因) y proseguir el curso lógico (而) arroja el desenlace natural (因而).",
            "cultural_and_cognitive_roots": "A formal coordinating consecutive conjunction in written Chinese that seamlessly ties prerequisite conditions to inevitable outcomes.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'yīn ér' (55-35). Start with a level high pitch on 'yīn', then rise smoothly on 'ér'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "田", "pinyin": "tián", "meaning_en": "field; farmland", "distinction_note": "Cross inside 囗 instead of 大"},
                {"character": "四", "pinyin": "sì", "meaning_en": "four", "distinction_note": "Eight 八 inside 囗 instead of 大"},
                {"character": "面", "pinyin": "miàn", "meaning_en": "face; surface", "distinction_note": "Contains 自/目 frame at the top"},
                {"character": "耍", "pinyin": "shuǎ", "meaning_en": "play; fool with", "distinction_note": "Woman radical 女 under 而"}
            ],
            "etymological_cognates": [
                {"character": "因为", "pinyin": "yīnwèi", "gloss_en": "because; owing to"},
                {"character": "原因", "pinyin": "yuányīn", "gloss_en": "cause; origin"},
                {"character": "因此", "pinyin": "yīncǐ", "gloss_en": "therefore; consequently"},
                {"character": "而且", "pinyin": "érqiě", "gloss_en": "moreover; furthermore"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "因而 explicitly marks an inevitable outcome or natural consequence resulting from the preceding premise.",
            "contrasts": [
                {"id": 1, "compared_word": "因而 vs. 因为", "pinyin": "yīnwèi", "analysis": "因为 introduces the causal antecedent ('because'), whereas 因而 introduces the resulting consequence ('consequently')."},
                {"id": 2, "compared_word": "因而 vs. 因此", "pinyin": "yīncǐ", "analysis": "因此 is broader and common in spoken register, while 因而 highlights the causal chain's natural progression."},
                {"id": 3, "compared_word": "因而 vs. 反而", "pinyin": "fǎn'ér", "analysis": "反而 indicates an outcome contrary to expectations, whereas 因而 confirms expected logical consequences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的建筑格局严格遵照坐北朝南的朝向，正房因而能够在一整年里获取最充沛的日照与良好的自然通风。夏季南风徐来，冬季北风受阻，因而形成了一个极为适宜日常安居的健康微气候。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de jiànzhù guīzhì yángé zūnzhào zuòběi-cháonán de cháoxiàng, zhèngfáng yīn'ér nénggòu zài yī zhěng nián lǐ huòqǔ zuì chōngpèi de rìzhào yǔ liánghǎo de zìrán tōngfēng. Xiàjì nánfēng xú lái, dōngjì běifēng shòuzǔ, yīn'ér xíngchéng le yī gè jíwéi shìyí rìcháng ānjū de jiànkāng wēiqìhòu.",
                "en": "Beijing quadrangles strictly face south; as a result, the main room obtains optimal daylight and natural ventilation year-round. Summer breezes enter while winter gales are blocked; consequently, a healthy microclimate is forged.",
                "es": "El siheyuan pekinés se orienta estrictamente al sur; de ahí que su sala principal disfrute de luz y ventilación óptimas todo el año. En verano entran brisas y en invierno se frena el cierzo, forjando un microclima ideal."
            },
            {
                "id": "#2",
                "hanzi": "科研团队在关键算法的设计中始终贯彻轻量化理念，代码执行效率因而提升了数倍，能源消耗因而显著降低。这项突破不仅赢得了国际同行的广泛赞誉，更因而为公司在激烈的海外市场竞争中赢得了宝贵的先机。",
                "pinyin": "Kēyán tuánduì zài guānjiàn suànfǎ de shèjì zhōng shǐzhōng guàngchè qīngliànghuà lǐniàn, dàimǎ zhíxíng xiàolǜ yīn'ér tíshēng le shù bèi, néngyuán xiāohào yīn'ér xiǎnzhù jiàngdī. Zhè xiàng tūpò bùjǐn yíngdé le guójì tóngháng de guǎngfàn zànyù, gèng yīn'ér wèi gōngsī zài jīliè de hǎiwài shìchǎng jìngzhēng zhōng yíngdé le bǎoguì de xiānjī.",
                "en": "The research team pursued lightweight design in its algorithms; consequently, execution efficiency surged and power consumption dropped. This breakthrough not only won international praise, but thus secured an advantage in markets.",
                "es": "El equipo aplicó criterios de aligeramiento en sus algoritmos, multiplicando la velocidad y reduciendo el consumo; este logro cosechó elogios internacionales y por ende aseguró una valiosa ventaja comercial."
            }
        ]
    },

    # 30 为
    {
        "id": "30",
        "hanzi": "为",
        "pinyin": "wéi",
        "part_of_speech": "Preposition",
        "meanings_summary": {
            "en": "by (passive); as; to act as; to serve as; to become",
            "es": "por (voz pasiva); como; hacer de; servir de; considerarse"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Preposition",
                "register": "Standard",
                "definition_en": "used in passive constructions (often paired with 所 as 为……所……) to introduce the agent of action, or to denote serving as",
                "definition_es": "empleado en construcciones pasivas (a menudo en el patrón 为……所……) para introducir el agente, o con valor de servir de",
                "example_phrase": "为世人所称赞 (praised by all people in the world)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院这种凝聚了东方哲学智慧的传统建筑形式，历经沧桑变迁，至今仍为中外建筑学者所赞叹。",
                "pinyin": "Sìhéyuàn zhè zhǒng níngjù le dōngfāng zhéxué zhìhuì de chuántǒng jiànzhù xíngshì, lìjīng cāngsāng biànqiān, zhìjīn réng wéi zhōngwài jiànzhù xuézhě suǒ zàntàn.",
                "en": "As a traditional architecture embodying Eastern philosophical wisdom, courtyards withstand shifting eras and are praised by scholars worldwide.",
                "es": "El siheyuan, síntesis de la sabiduría filosófica oriental, pervive tras siglos de vicisitudes y sigue siendo elogiado por arquitectos del mundo entero."
            },
            {
                "id": "#2",
                "hanzi": "他不仅在学术界享有崇高威望，更被同行们一致推选为本届国际地质学会理事长。",
                "pinyin": "Tā bùjǐn zài xuéshùjiè xiǎngyǒu chónggāo wēiwàng, gèng bèi tóngháng men yīzhì tuīxuǎn wéi běnjiè guójì dìzhì xuéhuì lǐshìzhǎng.",
                "en": "Not only does he enjoy lofty prestige in academia, but he was also unanimously elected by peers to serve as president of the Geological Society.",
                "es": "No solo goza de sólido prestigio académico, sino que fue elegido por sus colegas para actuar como presidente de la Sociedad Geológica Internacional."
            }
        ],
        "collocations": [
            {"hanzi": "为人所知", "en": "known by people / widely recognized"},
            {"hanzi": "为……所吸引", "en": "captivated by ..."},
            {"hanzi": "选为代表", "en": "elected as representative"},
            {"hanzi": "化为乌有", "en": "vanish into thin air / come to nothing"},
            {"hanzi": "变被动为主动", "en": "turn passive into active"},
            {"hanzi": "转败为胜", "en": "turn defeat into victory"}
        ],
        "idioms": [
            {"hanzi": "为人师表", "pinyin": "wéi rén shī biǎo", "meaning_en": "serve as a paragon for others to emulate"},
            {"hanzi": "下不为例", "pinyin": "xià bù wéi lì", "meaning_en": "not to be taken as a precedent in the future"},
            {"hanzi": "敢作敢为", "pinyin": "gǎn zuò gǎn wéi", "meaning_en": "daring to act and take responsibility"},
            {"hanzi": "合二为一", "pinyin": "hé èr wéi yī", "meaning_en": "combine two into one single unit"}
        ],
        "character_decomposition": [
            {
                "character": "为",
                "pinyin": "wéi",
                "meaning_en": "act; do; serve as; become; by",
                "meaning_es": "actuar; hacer; servir de; ser; por",
                "radical": "丶",
                "radical_meaning_en": "dot",
                "meaning_component": "hand leading an elephant by the trunk to work",
                "sound_component": "为 (wéi)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of a human hand leading an elephant by its trunk to execute heavy physical labor.",
                "visual_mnemonic_story_en": "A guiding hand leading a gentle working elephant forward to accomplish tasks (为).",
                "visual_mnemonic_story_es": "Una mano humana que guía a un dócil elefante para emprender faenas pesadas (为).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IKS",
                "traditional": "為"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A hand guiding action to serve as an agent or cause (为) marks passive agency (为……所……).",
            "composite_memory_hook_es": "Una mano guiando la acción para fungir de agente o causa (为) articula la voz pasiva (为……所……).",
            "cultural_and_cognitive_roots": "Versatile grammatical particle originating in Bronze script meaning 'to manage or act', central to classical passives and transformations.",
            "tone_sandhi_and_pitch_modulation": "Second tone: 'wéi' (35). Distinct from fourth tone preposition 'wèi' (for the sake of). Rise smoothly."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "办", "pinyin": "bàn", "meaning_en": "handle; manage", "distinction_note": "Eight 八 framing 力 instead of dot strokes"},
                {"character": "力", "pinyin": "lì", "meaning_en": "power; strength", "distinction_note": "Single muscular stroke without inner dots"},
                {"character": "头", "pinyin": "tóu", "meaning_en": "head; top", "distinction_note": "Big 大 frame with two dots on top"},
                {"character": "买", "pinyin": "mǎi", "meaning_en": "buy; purchase", "distinction_note": "Hook frame 乛 over 头-like structure"}
            ],
            "etymological_cognates": [
                {"character": "作为", "pinyin": "zuòwéi", "gloss_en": "conduct; deed; as"},
                {"character": "行为", "pinyin": "xíngwéi", "gloss_en": "action; behavior"},
                {"character": "成为", "pinyin": "chéngwéi", "gloss_en": "become; turn into"},
                {"character": "认为", "pinyin": "rènwéi", "gloss_en": "consider; deem"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "为 (wéi, second tone) functions in formal registers as a passive marker (被/为……所) or copular verb meaning 'to serve as/become'.",
            "contrasts": [
                {"id": 1, "compared_word": "为 (wéi) vs. 为 (wèi)", "pinyin": "wèi", "analysis": "Second-tone 为 (wéi) denotes passivity or acting as, whereas fourth-tone 为 (wèi) marks benefactive purpose ('for the sake of')."},
                {"id": 2, "compared_word": "为 vs. 被", "pinyin": "bèi", "analysis": "被 is the colloquial modern passive preposition, while 为……所 is an elevated literary passive structure."},
                {"id": 3, "compared_word": "为 vs. 当", "pinyin": "dāng", "analysis": "当 focuses on serving in a concrete professional post (当老师), while 为 covers broader functional roles (选为代表)."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统四合院建筑的严整规制与深厚文化底蕴，不仅深受国人自豪珍视，更广为世界建筑界所瞩目。许多外国学者不远万里来到北京胡同，实地考察四合院的梁架雕饰，皆为其巧夺天工的匠心所折服。",
                "pinyin": "Zhōngguó chuántǒng sìhéyuàn jiànzhù de yánzhěng guīzhì yǔ shēnhòu wénhuà dǐyùn, bùjǐn shēn shòu guórén zìháo zhēnshì, gèng guǎng wéi shìjiè jiànzhùjiè suǒ zhǔmù. Xǔduō wàiguó xuézhě bùyuǎn-wànlǐ lái dào Běijīng hútòng, shídì kǎochá sìhéyuàn de liángjià diāoshì, jiē wéi qí qiǎoduó-tiāngōng de jiàngxīn suǒ zhéfú.",
                "en": "The rigorous structure and profound culture of Chinese courtyards are cherished domestically and noticed by the global architectural community. Foreign scholars travel to Beijing alleys, consistently captivated by the ingenious craftsmanship.",
                "es": "La armoniosa traza y hondo bagaje cultural del siheyuan son orgullo nacional y despiertan admiración internacional. Eruditos de todo el mundo viajan a los hutongs de Pekín, rindiéndose ante su primorosa maestría artesanal."
            },
            {
                "id": "#2",
                "hanzi": "在漫长的历史长河中，优秀的中华传统美德世代相传，化为民族精神的血脉源泉。历代仁人志士以天下兴亡为己任，百折不挠，他们崇高的人格风范永远为后人所景仰与缅怀，激励着一代代青年奋发图强。",
                "pinyin": "Zài màncháng de lìshǐ chánghé zhōng, yōuxiù de Zhōnghuá chuántǒng měidé shìdài xiāngchuán, huà wéi mínzú jīngshén de xuèmài yuánquán. Lìdài rénrén-zhìshì yǐ tiānxià xīngwáng wéi jǐ rèn, bǎizhé-bùnáo, tāmen chónggāo de réngé fēngfàn yǒngyuǎn wéi hòurén suǒ jǐngyǎng yǔ miǎnhuái, jīlì zhe yīdàidài qīngnián fènfā-túqiáng.",
                "en": "Across Chinese history, traditional virtues passed down to become the lifeblood of national spirit. Patriots shouldered responsibility for the common good; their integrity is revered by posterity, inspiring generations to strive.",
                "es": "A lo largo de la historia, las virtudes clásicas se transmitieron como savia del espíritu patrio. Ilustres próceres asumieron el destino común; su entereza moral sigue siendo venerada por las generaciones venideras."
            }
        ]
    }
]

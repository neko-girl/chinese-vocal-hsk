# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 写作
    {
        "id": "11",
        "hanzi": "写作",
        "pinyin": "xiě zuò",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to write; to compose; writing; literary composition",
            "es": "escribir; redactar; composición; creación literaria"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to compose literary works, articles, books, or poems",
                "definition_es": "redactar o componer obras literarias, artículos, libros o poesías",
                "example_phrase": "从事写作 (engage in writing)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the process or craft of literary composition",
                "definition_es": "el oficio, disciplina o proceso de la composición escrita",
                "example_phrase": "提高写作技巧 (improve writing skills)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了完成这部长篇小说的写作，作者深入西南山区体验生活了整整三年，积累了丰富素材。",
                "pinyin": "Wèile wánchéng zhè bù chángpiān xiǎoshuō de xiězuò, zuòzhě shēnrù xīnán shānqū tǐyàn shēnghuó le zhěngzhěng sān nián, jīlěi le fēngfù sùcái.",
                "en": "To complete writing this novel, the author lived in the southwest mountains for three whole years, gathering rich material.",
                "es": "Para redactar esta novela extensa, el autor se adentró en las sierras del suroeste durante tres años a recopilar vivencias."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅的日记中记录了大量深夜写作的琐屑，伏案工作之余，品茶抽烟便成了他舒缓神经的习惯。",
                "pinyin": "Lǔ Xùn de rìjì zhōng jìlù le dàliàng shēnyè xiězuò de suǒxiè, fú'àn gōngzuò zhī yú, pǐnchá chōuyān biàn chéngwéi tā shūhuǎn shénjīng de xíguàn.",
                "en": "Lu Xun's journals recorded many details of late-night writing; after hours at his desk, tea and cigarettes relieved tension.",
                "es": "El diario de Lu Xun consigna vigilias dedicadas a escribir; tras largas horas al pupitre, fumar y tomar té aliviaban su fatiga."
            }
        ],
        "collocations": [
            {"hanzi": "从事写作", "en": "engage in writing"},
            {"hanzi": "写作技巧", "en": "writing techniques"},
            {"hanzi": "文学写作", "en": "literary writing"},
            {"hanzi": "写作风格", "en": "writing style"},
            {"hanzi": "学术写作", "en": "academic writing"},
            {"hanzi": "完成写作", "en": "finish writing"}
        ],
        "idioms": [
            {"hanzi": "妙笔生花", "pinyin": "miào bǐ shēng huā", "meaning_en": "a gifted pen brings forth flowers; brilliant writing"},
            {"hanzi": "行云流水", "pinyin": "xíng yún liú shuǐ", "meaning_en": "floating clouds and flowing water; natural and smooth style"},
            {"hanzi": "文不加点", "pinyin": "wén bù jiā diǎn", "meaning_en": "write without needing corrections; swift literary facility"},
            {"hanzi": "一挥而就", "pinyin": "yì huī ér jiù", "meaning_en": "accomplish in one flourish of the pen"}
        ],
        "character_decomposition": [
            {
                "character": "写",
                "pinyin": "xiě",
                "meaning_en": "write; draw; depict; compose",
                "meaning_es": "escribir; dibujar; retratar; componer",
                "radical": "冖",
                "radical_meaning_en": "cover",
                "meaning_component": "冖 (cover/canopy)",
                "sound_component": "与 (yǔ, simplified component)",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Traditional 寫 shows placing objects into a container under a roof 宀; simplified to 写 for putting words on paper.",
                "visual_mnemonic_story_en": "Under a desk canopy (冖), strokes of ink flow with (与) deliberate grace to write (写) truth.",
                "visual_mnemonic_story_es": "Bajo la lámpara de la mesa (冖), los trazos fluyen con (与) armonía para escribir (写) verdades.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "BYM",
                "traditional": "寫"
            },
            {
                "character": "作",
                "pinyin": "zuò",
                "meaning_en": "make; do; create; write; act",
                "meaning_es": "hacer; crear; componer; actuar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person/creator)",
                "sound_component": "乍 (zhà, sudden burst / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing an active artisan 亻 suddenly 乍 beginning a new constructive creation.",
                "visual_mnemonic_story_en": "A creative person (亻) abruptly (乍) begins to fashion a masterwork with their hands (作).",
                "visual_mnemonic_story_es": "Una persona industriosa (亻) se pone de pronto (乍) manos a la obra para crear algo nuevo (作).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OHS",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When a creative mind (作) puts ink to paper (写), powerful writing (写作) is born.",
            "composite_memory_hook_es": "Cuando la mano creadora (作) plasma la tinta sobre el papel (写), surge la viva escritura (写作).",
            "cultural_and_cognitive_roots": "In the Chinese Confucian tradition, writing ('wén') carried the sacred mission of conveying moral dao ('文以载道'); combining 'xiě' (inscribing) with 'zuò' (creative generation) denotes purposeful art.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by falling tone: 'xiě zuò' (214-51). Pronounce 'xiě' with a low dip before dropping into 4th tone 'zuò'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "军", "pinyin": "jūn", "meaning_en": "army; military", "distinction_note": "Has 车 inside 冖 instead of 与"},
                {"character": "昨", "pinyin": "zuó", "meaning_en": "yesterday", "distinction_note": "Has sun radical 日 on left instead of 亻"},
                {"character": "炸", "pinyin": "zhà", "meaning_en": "explode; deep fry", "distinction_note": "Has fire radical 火 on left instead of 亻"},
                {"character": "咋", "pinyin": "zǎ", "meaning_en": "how; why", "distinction_note": "Has mouth radical 口 on left instead of 亻"}
            ],
            "etymological_cognates": [
                {"character": "述", "pinyin": "shù", "gloss_en": "narrate; recount on paths"},
                {"character": "撰", "pinyin": "zhuàn", "gloss_en": "compile; author with hands"},
                {"character": "著", "pinyin": "zhù", "gloss_en": "author; manifest clearly"},
                {"character": "创", "pinyin": "chuàng", "gloss_en": "create; initiate with blades"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "写作 focuses on the active creative or technical process of producing written prose, articles, or books.",
            "contrasts": [
                {"id": "1", "compared_word": "写作 vs. 创作", "pinyin": "chuàngzuò", "analysis": "创作 applies broadly to original artistic creation across all mediums (music, painting, theater), while 写作 is strictly text-based."},
                {"id": "2", "compared_word": "写作 vs. 起草", "pinyin": "qǐcǎo", "analysis": "起草 refers specifically to producing preliminary bureaucratic or legal drafts of treaties and laws, unlike general literary 写作."},
                {"id": "3", "compared_word": "写作 vs. 抄写", "pinyin": "chāoxiě", "analysis": "抄写 is merely copying existing text onto paper without creative input, while 写作 requires cognitive ideation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "写作是一场孤独而又丰盈的心灵远征。作家在夜深人静时面对素白的稿纸，将心底最隐秘的感悟化作跳动的文字。那些在生活磨难中提炼出的深刻句子，不仅慰藉了创作者孤寂的灵魂，更穿越时空温暖了无数素昧平生的读者。",
                "pinyin": "Xiězuò shì yì chǎng gūdú ér yòu fēngyíng de xīnlíng yuǎnzhēng. Zuòjiā zài yèshēn-rénjìng shí miànduì sùbái de gǎozhǐ, jiāng xīndǐ zuì yǐnmì de gǎnwù huàzuò tiàodòng de wénzì. Nàxiē zài shēnghuó mónàn zhōng tíliàn chū de shēnkè jùzi, bùjǐn wèijiè le chuàngzuòzhě gūjì de línghún, gèng chuānyuè shíkōng wēnduǎn le wúshù sùmèi-píngshēng de dúzhě.",
                "en": "Writing is a lonely yet fruitful pilgrimage of the soul. In the quiet of night, authors turn inner feelings into living words on white sheets. Profound sentences forged through hardship comfort the creator and warm readers across time.",
                "es": "Escribir es una travesía íntima, solitaria y fecunda. En el sosiego nocturno, el autor plasma sus emociones en el papel en blanco. Esas frases forjadas en la adversidad no solo consuelan al creador, sino que arropan a lectores remotos."
            },
            {
                "id": "#2",
                "hanzi": "随着人工智能技术的飞速演进，机器辅助写作正在深刻重塑传统传媒生态。智能算法能够在数秒内生成结构完整的财经快讯与行业简报，促使专业记者将更多精力投入深度调查与批判性写作，以守护新闻叙事的人文深度与思想温度。",
                "pinyin": "Suízhe réngōng zhìnéng jìshù de fēisù yǎnjìn, jīqì fùzhù xiězuò zhèngzài shēnkè chóngshù chuántǒng chuánméi shēngtài. Zhìnéng suànfǎ nénggòu zài shù miǎo nèi shēngchéng jiégòu wánzhěng de cáiqīng kuàixùn yǔ hángyè jiǎnbào, cùshǐ zhuānyè jìzhě jiāng gèng duō jīnglì tóurù shēndù diàochá yǔ pīpànxìng xiězuò, yǐ shǒuhù xīnwén xùshì de rénwén shēndù yǔ sīxiǎng wēndù.",
                "en": "With AI advancing, machine writing reshapes journalism. Algorithms generate newsflashes in seconds, compelling reporters to focus on investigative and critical writing to preserve the human depth and intellectual warmth of narratives.",
                "es": "Con el avance de la inteligencia artificial, la redacción automatizada transforma el periodismo. Los algoritmos generan síntesis en segundos, empujando a los cronistas hacia la investigación profunda para preservar el pulso humano de las noticias."
            }
        ]
    },

    # 12 点心
    {
        "id": "12",
        "hanzi": "点心",
        "pinyin": "diǎn xin",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "dim sum; pastry; snack; dessert; refreshment",
            "es": "repostería; pastelitos; merienda; tentempié; dim sum"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "traditional baked, steamed, or fried cakes, dumplings, and sweet or savory snacks served between meals",
                "definition_es": "pasteles, bollos o bocadillos dulces o salados que se toman como merienda o tentempié",
                "example_phrase": "可口的小点心 (delicious little pastries)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每逢周末，母亲总会亲手烘焙几样精致的点心，搭配浓郁的热红茶，让全家人享受惬意的下午茶时光。",
                "pinyin": "Měiféng zhòumò, mǔqīn zǒng huì qīnshǒu hōngbèi jǐ yàng jīngzhì de diǎnxin, dàipèi nóngyù de rè hóngchá, ràng quánjiā rén xiǎngshòu qièyì de xiàwǔchá shíguāng.",
                "en": "Every weekend, mother bakes delicate pastries by hand, paired with rich black tea for the family to enjoy cozy afternoon tea.",
                "es": "Cada fin de semana, madre hornea finos pastelitos para acompañar con té caliente, brindando una plácida merienda familiar."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅先生极爱甜食，下班路过北京稻香村时，总要买上几包传统的精致点心带回家中招待来客。",
                "pinyin": "Lǔ Xùn xiānsheng jí ài tiánshí, xiàbān lùguò Běijīng Dàoxiāngcūn shí, zǒng yào mǎi shàng jǐ bāo chuántǒng de jīngzhì diǎnxin dài huí jiā zhōng zhāodài láikè.",
                "en": "Mr. Lu Xun had a great sweet tooth; passing Daoxiangcun after work, he always bought traditional pastries to treat guests at home.",
                "es": "A Lu Xun le fascinaban los dulces; al pasar por la confitería Daoxiangcun compraba cajas de repostería típica para agasajar a sus visitas."
            }
        ],
        "collocations": [
            {"hanzi": "精美点心", "en": "delicate pastries"},
            {"hanzi": "广式点心", "en": "Cantonese dim sum"},
            {"hanzi": "传统点心", "en": "traditional snacks/pastries"},
            {"hanzi": "点心匣子", "en": "traditional pastry gift box"},
            {"hanzi": "烘焙点心", "en": "bake pastries"},
            {"hanzi": "茶水点心", "en": "tea and refreshments"}
        ],
        "idioms": [
            {"hanzi": "脍炙人口", "pinyin": "kuài zhì rén kǒu", "meaning_en": "appealing to all tastes; universally praised"},
            {"hanzi": "茶余饭后", "pinyin": "chá yú fàn hòu", "meaning_en": "over tea and meals; during leisurely spare time"},
            {"hanzi": "秀色可餐", "pinyin": "xiù sè kě cān", "meaning_en": "ravishing beauty feast for the eyes"},
            {"hanzi": "甘之如饴", "pinyin": "gān zhī rú yí", "meaning_en": "taste as sweet as malt sugar; bear hardships willingly"}
        ],
        "character_decomposition": [
            {
                "character": "点",
                "pinyin": "diǎn",
                "meaning_en": "drop; dot; touch; spot; light up",
                "meaning_es": "punto; gota; tocar levemente; encender",
                "radical": "灬",
                "radical_meaning_en": "fire",
                "meaning_component": "黑 (black/soot) + 灬 (fire)",
                "sound_component": "占 (zhàn, divine / phonetic)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient character showing soot marks from a lamp flame 灬; later simplified to touching or touching lightly.",
                "visual_mnemonic_story_en": "A spark of flame (灬) touches the wick to place a small dot of light on the table (点).",
                "visual_mnemonic_story_es": "Una chispa de fuego (灬) roza la mecha depositando una pizca de luz sobre la mesa (点).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "YRBO",
                "traditional": "點"
            },
            {
                "character": "心",
                "pinyin": "xin",
                "meaning_en": "heart; core; mind; affection",
                "meaning_es": "corazón; centro; mente; afecto",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "心 (pictogram of the human heart)",
                "sound_component": "心 (xīn)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram of the human heart showing ventricles and aorta chambers.",
                "visual_mnemonic_story_en": "The three drops surround the curved ventricle chamber to depict the living human heart (心).",
                "visual_mnemonic_story_es": "Las tres gotas rodean la cavidad central para representar el corazón humano palpitante (心).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "P",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A light snack touches (点) and comforts the stomach and heart (心), hence pastry (点心).",
            "composite_memory_hook_es": "Un bocado ligero que toca (点) y conforta el corazón (心) se convierte en merienda (点心).",
            "cultural_and_cognitive_roots": "Folklore traces 'diǎnxīn' to the Tang/Song dynasties, signifying eating a tiny bite just enough to 'touch the heart' (点点心意) before hunger strikes.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by neutral tone: 'diǎn xin' (214-2). Deliver 'diǎn' with a full 3rd tone and drop 'xin' softly into an unstressed neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "占", "pinyin": "zhàn", "meaning_en": "occupy; divine", "distinction_note": "Lacks the four bottom fire dots 灬 of 点"},
                {"character": "店", "pinyin": "diàn", "meaning_en": "shop; store", "distinction_note": "Has shelter radical 广 instead of bottom fire dots"},
                {"character": "必", "pinyin": "bì", "meaning_en": "must; surely", "distinction_note": "Has a long diagonal slashing stroke through 心"},
                {"character": "忒", "pinyin": "tuī", "meaning_en": "excessive", "distinction_note": "Has 弋 on the upper right of 心"}
            ],
            "etymological_cognates": [
                {"character": "糕", "pinyin": "gāo", "gloss_en": "steamed cake of rice/flour"},
                {"character": "饼", "pinyin": "bǐng", "gloss_en": "round flat biscuit or pastry"},
                {"character": "馅", "pinyin": "xiàn", "gloss_en": "pastry stuffing or filling"},
                {"character": "馍", "pinyin": "mó", "gloss_en": "steamed flour bun or bread"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "点心 refers to baked, steamed, or fried pastries and snacks eaten between formal meals.",
            "contrasts": [
                {"id": "1", "compared_word": "点心 vs. 零食", "pinyin": "língshí", "analysis": "零食 encompasses all processed casual snacks (candies, chips, nuts) eaten casually, while 点心 specifically refers to cooked, baked, or culinary pastries."},
                {"id": "2", "compared_word": "点心 vs. 甜点", "pinyin": "tiándiǎn", "analysis": "甜点 is strictly sweet desserts served at the conclusion of meals, whereas 点心 includes both savory meat buns and sweet pastries."},
                {"id": "3", "compared_word": "点心 vs. 小吃", "pinyin": "xiǎochī", "analysis": "小吃 covers regional street foods (noodles, tofu, skewers), while 点心 leans toward refined flour/rice pastries and teahouse refreshments."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "午后暖阳斜照在雕花木桌上，一壶清冽的龙井配上两块软糯的桂花点心，勾勒出岁月静好的江南午后。那甜而不腻的豆沙馅料入口即化，在唇齿间弥散开淡淡的花香，将所有的奔波劳碌都化作了舌尖上的温存。",
                "pinyin": "Wǔhòu nuǎnyáng xiézhào zài diāohuā mùzhuō shàng, yì hú qīngliè de Lóngjǐng pèishàng liǎng kuài ruǎnnuò de guìhuā diǎnxin, gōulè chū suìyuè-jìnghǎo de Jiāngnán wǔhòu. Nà tián ér bú nì de dòushā xiànliào rùkǒu-jíhuà, zài chúnchǐ jiān mísàn kāi dàndàn de huāxiāng, jiāng suǒyǒu de bēnbō-láolù dōu huàzuò le shéjiān shàng de wēncún.",
                "en": "Warm afternoon sun slants across the carved table, where Longjing tea and sweet osmanthus pastries outline southern tranquility. The delicate bean paste melts on the tongue, dispersing floral fragrance and melting daily weariness.",
                "es": "El sol vespertino baña la mesa de madera labrada; una tetera de té Longjing y pastelitos de osmanto dibujan la quietud del sur. El dulce relleno se deshace en el paladar, disipando las fatigas del día con su sutil aroma floral."
            },
            {
                "id": "#2",
                "hanzi": "传统中式点心不仅是美味的物质享受，更承载着中华民族深厚的节庆民俗与礼仪文化。从八月十五象征阖家团圆的月饼，到端午时节包裹青竹清香的粽子，每一道手工点心的纹样与馅料，都寄托着人们对美好生活的永恒期盼。",
                "pinyin": "Chuántǒng zhōngshì diǎnxin bùjǐn shì měiwèi de wùzhì xiǎngshòu, gèng chéngzài zhe Zhōnghuá mínzú shēnhòu de jiéqìng mínsú yǔ lǐyí wénhuà. Cóng bāyuè shíwǔ xiàngzhēng héjiā-tuányuán de yuèbǐng, dào Duānwǔ shíjié bāoguǒ qīngzhú qīngxiāng de zòngzi, měi yí dào shǒugōng diǎnxin de wényàng yǔ xiànliào, dōu jìtuō zhe rénmen duì měihǎo shēnghuó de yǒnghéng qīpàn.",
                "en": "Traditional pastries offer not only culinary pleasure, but embody festive customs and etiquette. From Mid-Autumn mooncakes symbolizing reunion to Dragon Boat dumplings wrapped in bamboo, every pattern carries hopes for a good life.",
                "es": "La repostería china tradicional encarna un rico legado festivo. Desde los pasteles de luna que celebran la unión familiar hasta los tamales de bambú en el festival del dragón, cada manjar artesano alberga los mejores deseos de bienestar."
            }
        ]
    },

    # 13 作为
    {
        "id": "13",
        "hanzi": "作为",
        "pinyin": "zuò wéi",
        "part_of_speech": "Preposition / Verb / Noun",
        "meanings_summary": {
            "en": "as; in the capacity of; to act as; accomplishment; conduct; deed",
            "es": "como; en calidad de; actuar como; logro; acción; conducta"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Preposition",
                "register": "Standard",
                "definition_en": "in the role, capacity, or identity of",
                "definition_es": "en calidad de; en el papel o condición de",
                "example_phrase": "作为一名教师 (as a teacher)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to regard as; to use or take as",
                "definition_es": "tomar como; considerar o emplear en concepto de",
                "example_phrase": "作为参考 (take as a reference)"
            },
            {
                "sense_number": "3",
                "part_of_speech": "Noun",
                "register": "Formal",
                "definition_en": "significant deeds, positive accomplishments, or enterprise",
                "definition_es": "hazaña, logro o iniciativa de envergadura",
                "example_phrase": "大有作为 (have great prospects for accomplishment)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "作为这个项目的团队负责人，他时刻把员工的安全与身心健康放在首要位置。",
                "pinyin": "Zuòwéi zhè ge xiàngmù de tuánduì fùzérén, tā shíkè bǎ yuángōng de ānquán yǔ shēnxīn jiànkāng fàng zài shǒuyào wèizhì.",
                "en": "As the leader of this project team, he constantly prioritizes employee safety and mental well-being.",
                "es": "Como responsable del equipo en este proyecto, antepone en todo momento la seguridad y la salud de sus colaboradores."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅将饮食文化作为观察近代中国社会百态的一面镜子，在笔墨间展现了极其深厚的人间温情。",
                "pinyin": "Lǔ Xùn jiāng yǐnshí wénhuà zuòwéi guānchá jìndài Zhōngguó shèhuì bǎitài de yí miàn jìngzi, zài bǐmò jiān zhǎnxiàn le jíqí shēnhòu de rénjiān wēnqíng.",
                "en": "Lu Xun used food culture as a mirror to observe modern Chinese society, showing deep human warmth in his writings.",
                "es": "Lu Xun empleó la gastronomía como un espejo para observar la sociedad moderna, plasmando con su pluma una entrañable calidez humana."
            }
        ],
        "collocations": [
            {"hanzi": "作为代表", "en": "as a representative"},
            {"hanzi": "大有作为", "en": "have brilliant prospects"},
            {"hanzi": "毫无作为", "en": "accomplish nothing; passive inaction"},
            {"hanzi": "作为依据", "en": "use as a basis"},
            {"hanzi": "担当作为", "en": "take responsibility and take action"},
            {"hanzi": "作为参考", "en": "as a reference"}
        ],
        "idioms": [
            {"hanzi": "胡作非为", "pinyin": "hú zuò fēi wéi", "meaning_en": "act recklessly and commit illegal atrocities"},
            {"hanzi": "量力而为", "pinyin": "liàng lì ér wéi", "meaning_en": "act according to one's capabilities"},
            {"hanzi": "有所作为", "pinyin": "yǒu suǒ zuò wéi", "meaning_en": "make a promising mark; achieve notable success"},
            {"hanzi": "敢作敢当", "pinyin": "gǎn zuò gǎn dāng", "meaning_en": "bold enough to act and brave enough to face the consequences"}
        ],
        "character_decomposition": [
            {
                "character": "作",
                "pinyin": "zuò",
                "meaning_en": "do; make; act; write; work",
                "meaning_es": "hacer; crear; actuar; componer",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person)",
                "sound_component": "乍 (zhà, sudden initiation / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic ideogram showing a person 亻 undertaking active creative endeavor 乍.",
                "visual_mnemonic_story_en": "A capable artisan (亻) stands up to begin making (作) useful things for the community.",
                "visual_mnemonic_story_es": "Un individuo diligente (亻) se pone en pie para iniciar la labor constructiva (作).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OHS",
                "traditional": ""
            },
            {
                "character": "为",
                "pinyin": "wéi",
                "meaning_en": "act as; serve as; become; do",
                "meaning_es": "actuar como; servir de; hacer; ser",
                "radical": "丶",
                "radical_meaning_en": "dot",
                "meaning_component": "爪 (hand guiding an elephant in traditional 為)",
                "sound_component": "为 (wéi)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram of a human hand 爪 leading an elephant, meaning to direct work or perform deeds.",
                "visual_mnemonic_story_en": "A firm guiding hand reaches out to direct work, acting as (为) an able leader.",
                "visual_mnemonic_story_es": "Una mano firme guía la labor con destreza, sirviendo de (为) orientadora eficaz.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IKS",
                "traditional": "為"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "To work actively (作) and serve in a guiding role (为) is to act in the capacity of an authority (作为).",
            "composite_memory_hook_es": "Trabajar con empeño (作) y servir de guía (为) significa desempeñarse en calidad de líder (作为).",
            "cultural_and_cognitive_roots": "A cornerstone term in Chinese philosophy; Daoism warns of 'wúwéi' (无为, effortless non-forcing), while Confucianism urges active moral initiative ('yǒusuǒ-zuòwéi', 有所作为).",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by rising tone: 'zuò wéi' (51-35). Syllable 'zuò' descends sharply, while 'wéi' rises smoothly from pitch 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "昨", "pinyin": "zuó", "meaning_en": "yesterday", "distinction_note": "Has sun radical 日 on left instead of 亻"},
                {"character": "办", "pinyin": "bàn", "meaning_en": "manage; do", "distinction_note": "Has 力 in center flanked by two dots, unlike 为"},
                {"character": "刃", "pinyin": "rèn", "meaning_en": "blade edge", "distinction_note": "Has 刀 with single dot inside, unlike 为"},
                {"character": "仿", "pinyin": "fǎng", "meaning_en": "imitate", "distinction_note": "Has 方 on right instead of 乍"}
            ],
            "etymological_cognates": [
                {"character": "办", "pinyin": "bàn", "gloss_en": "manage; handle affairs"},
                {"character": "行", "pinyin": "xíng", "gloss_en": "walk; carry out action"},
                {"character": "施", "pinyin": "shī", "gloss_en": "execute; dispense benevolence"},
                {"character": "当", "pinyin": "dāng", "gloss_en": "serve as; undertake office"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "作为 denotes operating in a defined capacity/identity, or refers formally to purposeful human accomplishments.",
            "contrasts": [
                {"id": "1", "compared_word": "作为 vs. 当作", "pinyin": "dàngzuò", "analysis": "当作 is strictly a transitive verb meaning to treat or mistake A for B ('把他当作朋友'), whereas 作为 primarily introduces an identity role ('作为朋友')."},
                {"id": "2", "compared_word": "作为 vs. 行为", "pinyin": "xíngwéi", "analysis": "行为 denotes objective human conduct and motor actions, while 作为 as a noun specifically denotes significant positive accomplishments ('大有作为')."},
                {"id": "3", "compared_word": "作为 vs. 以为", "pinyin": "yǐwéi", "analysis": "以为 indicates subjective (often erroneous) cognitive assumption, while 作为 indicates functional identity or purposeful deed."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "作为社会的一分子，每个人都在用自己的行动书写历史。无论身处平凡的岗位还是显赫的舞台，只要怀揣善意认真做事，就能为他人带去光明。不因位卑而自弃，不因艰难而退缩，这才是作为一个人最崇高的尊严。",
                "pinyin": "Zuòwéi shèhuì de yì fēnzǐ, měi ge rén dōu zài yòng zìjǐ de xíngdòng shūxiě lìshǐ. Wúlùn shēnchǔ píngfán de gǎngwèi háishì xiǎnhè de wǔtái, zhǐyào huáichuāi shànyì rènzhēn zuòshì, jiù néng wèi tārén dàiqù guāngmíng. Bù yīn wèibēi ér zìqì, bù yīn jiānnán ér tuìsuō, zhè cáishì zuòwéi yí ge rén zuì chónggāo de zūnyán.",
                "en": "As members of society, all write history with actions. Whether in humble posts or grand stages, acting with goodwill brings light to others. Not abandoning oneself for low status is the highest human dignity.",
                "es": "Como miembros de la sociedad, todos forjamos la historia con nuestros actos. Ya sea en un puesto humilde o en un gran escenario, obrar con buena fe alumbra a los demás. No desanimarse ante la dificultad dignifica la condición humana."
            },
            {
                "id": "#2",
                "hanzi": "在推动生态文明建设的进程中，政府部门必须积极作为。通过建立严格的环境保护问责制度，杜绝个别企业以牺牲绿水青山为代价换取短期经济效益的违法行为。唯有勇于担当作为，才能为子孙后代留下一片天蓝水清的美好家园。",
                "pinyin": "Zài tuīdòng shēngtài wénmíng jiànshè de jìnchéng zhōng, zhèngfǔ bùmén bìxū jījí zuòwéi. Tōngguò jiànlì yángé de huánjìng bǎohù wènzé zhìdù, dùjué gèbié qǐyè yǐ xīshēng lǜshuǐ-qīngshān wéi dàijià huànqǔ duǎnqī jīngjì xiàoyì de wéifǎ xíngwéi. Wéiyǒu yǒngyú dāndāng zuòwéi, cáinéng wèi zǐsūn-hòudài liúxià yí piàn tiānlán-shuǐqīng de měihǎo jiāyuán.",
                "en": "In promoting ecological progress, government bodies must take proactive action. Strict environmental accountability prevents firms from sacrificing nature for short-term gain. Bold initiative ensures clean skies for future generations.",
                "es": "En la salvaguarda ecológica, los poderes públicos deben actuar con firmeza. Exigir responsabilidades ambientales frena a las empresas que sacrifican la naturaleza por lucro efímero. Solo asumiendo el deber se legará un entorno limpio a la posteridad."
            }
        ]
    },

    # 14 学问
    {
        "id": "14",
        "hanzi": "学问",
        "pinyin": "xué wen",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "knowledge; learning; scholarship; erudition; wisdom; knack",
            "es": "conocimiento; saber; erudición; ciencia; arte; sabiduría práctica"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "systematic academic knowledge, deep erudition, or profound intellectual scholarship",
                "definition_es": "conocimiento académico sistemático, profunda erudición o sabiduría intelectual",
                "example_phrase": "有高深的学问 (possess profound scholarship)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Colloquial",
                "definition_en": "hidden technique, special knack, or practical wisdom embedded in everyday affairs",
                "definition_es": "truco especial, secreto técnico o sabiduría práctica oculta en el quehacer cotidiano",
                "example_phrase": "这里面大有学问 (there is a great deal of skill/knack in this)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老教授一生潜心钻研甲骨文，学问渊博品德高尚，受到了海内外学界的一致尊崇。",
                "pinyin": "Lǎo jiàoshòu yìshēng qiánxīn zuānyán jiǎgǔwén, xuéwen yuānbó pǐndé gāoshàng, shòudào le hǎinèiwài xuéjiè de yízhì zūnchóng.",
                "en": "The veteran professor dedicated his life to oracle bone research; his profound learning and noble virtue won universal scholarly respect.",
                "es": "El catedrático consagró su vida al desciframiento de los huesos oraculares; su vasta erudición y probidad le valieron gran estima académica."
            },
            {
                "id": "#2",
                "hanzi": "在鲁迅看来，烹饪选料与饮食调味里处处藏着大学问，懂得品味美食也是体察世情的一种方式。",
                "pinyin": "Zài Lǔ Xùn kànlái, pēngrèn xuǎnliào yǔ yǐnshí tiáowèi lǐ chùchù cáng zhe dà xuéwen, dǒngdé pǐnwèi měishí yě shì tǐchá shìqíng de yì zhǒng fāngshì.",
                "en": "In Lu Xun's eyes, selecting culinary ingredients and seasonings harbored profound wisdom; savoring food was a way to observe life.",
                "es": "Para Lu Xun, la elección de ingredientes y el sazón culinario albergaban un profundo saber; saborear delicias era otra forma de entender la vida."
            }
        ],
        "collocations": [
            {"hanzi": "学问渊博", "en": "profound and vast learning"},
            {"hanzi": "大有学问", "en": "contain profound knowledge/wisdom"},
            {"hanzi": "潜心学问", "en": "immerse oneself in scholarship"},
            {"hanzi": "做学问", "en": "conduct scholarly research"},
            {"hanzi": "大学问家", "en": "scholar of immense erudition"},
            {"hanzi": "日常学问", "en": "practical daily wisdom"}
        ],
        "idioms": [
            {"hanzi": "博古通今", "pinyin": "bó gǔ tōng jīn", "meaning_en": "conversant with both ancient and modern learning"},
            {"hanzi": "学无止境", "pinyin": "xué wú zhǐ jìng", "meaning_en": "there is no limit to learning; lifelong study"},
            {"hanzi": "敏而好学", "pinyin": "mǐn ér hào xué", "meaning_en": "clever and fond of learning"},
            {"hanzi": "满腹经纶", "pinyin": "mǎn fù jīng lún", "meaning_en": "full of political and administrative scholarship"}
        ],
        "character_decomposition": [
            {
                "character": "学",
                "pinyin": "xué",
                "meaning_en": "study; learn; knowledge; school",
                "meaning_es": "estudiar; aprender; conocimiento; escuela",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (child under roof)",
                "sound_component": "爻 (yáo, counting slips)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient ideogram showing a child 子 learning arithmetic tallies beneath a thatched classroom roof.",
                "visual_mnemonic_story_en": "A child (子) under a roof eagerly studies classic texts to acquire lifelong knowledge (学).",
                "visual_mnemonic_story_es": "Un joven estudiante (子) bajo el tejado escolar asimila los libros para cultivar el saber (学).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "FBD",
                "traditional": "學"
            },
            {
                "character": "问",
                "pinyin": "wen",
                "meaning_en": "ask; inquire; question; problem",
                "meaning_es": "preguntar; inquirir; interrogar; cuestión",
                "radical": "门",
                "radical_meaning_en": "door/gate",
                "meaning_component": "门 (entrance gate)",
                "sound_component": "口 (kǒu, mouth asking questions)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Ideogram showing an open mouth 口 at the gate 门 of a master's courtyard asking for instruction.",
                "visual_mnemonic_story_en": "A seeker arrives at the teacher's doorway (门) and opens their mouth (口) to inquire and ask (问).",
                "visual_mnemonic_story_es": "Un aprendiz se asoma al portón (门) del sabio y abre la boca (口) para inquirir y preguntar (问).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LSR",
                "traditional": "問"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "True knowledge is forged by coupling diligent study (学) with constant inquiring (问) to master deep scholarship (学问).",
            "composite_memory_hook_es": "El verdadero conocimiento nace de aunar el estudio constante (学) con la pregunta incisiva (问) para forjar el saber (学问).",
            "cultural_and_cognitive_roots": "Confucius taught in the Analects that one must 'learn and inquire' (学而问之); true Chinese scholarship rejects passive intake in favor of persistent philosophical questioning.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by neutral tone: 'xué wen' (35-2). Syllable 'xué' glides upward, while 'wen' is pronounced as a light neutral syllable."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "字", "pinyin": "zì", "meaning_en": "character", "distinction_note": "Has 宀 instead of the upper strokes of 学"},
                {"character": "闪", "pinyin": "shǎn", "meaning_en": "flash; dodge", "distinction_note": "Has person 人 inside 门 instead of 口"},
                {"character": "闭", "pinyin": "bì", "meaning_en": "close; shut", "distinction_note": "Has 才 inside 门 instead of 口"},
                {"character": "间", "pinyin": "jiān", "meaning_en": "between; space", "distinction_note": "Has sun 日 inside 门 instead of 口"}
            ],
            "etymological_cognates": [
                {"character": "习", "pinyin": "xí", "gloss_en": "practice; flap wings repeatedly"},
                {"character": "识", "pinyin": "shí", "gloss_en": "know; discern with words"},
                {"character": "闻", "pinyin": "wén", "gloss_en": "hear with ear at gate; reputation"},
                {"character": "智", "pinyin": "zhì", "gloss_en": "wisdom; knowing words over days"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "学问 denotes systematic erudition, profound scholarship, or the intricate wisdom embedded in craft techniques.",
            "contrasts": [
                {"id": "1", "compared_word": "学问 vs. 知识", "pinyin": "zhīshi", "analysis": "知识 refers to discrete informational facts and data, whereas 学问 implies deep, integrated, lifelong scholarship and philosophical insight."},
                {"id": "2", "compared_word": "学问 vs. 学术", "pinyin": "xuéshù", "analysis": "学术 refers strictly to formal institutional university research and scientific theory, while 学问 can also describe practical knacks in daily life ('泡茶有学问')."},
                {"id": "3", "compared_word": "学问 vs. 经验", "pinyin": "jīngyàn", "analysis": "经验 refers to empirical habits gathered through repetition, while 学问 emphasizes reasoned principles and scholarly mastery."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "真正的学问从不只存在于故纸堆中，它鲜活地流淌在柴米油盐的人间烟火里。无论是木匠手中精准无误的榫卯构造，还是厨师火候中出神入化的调味平衡，只要用心体悟精益求精，平凡琐事之中皆藏着深奥的大学问。",
                "pinyin": "Zhēnzhèng de xuéwen cóng bù zhǐ cúnzài yú gùzhǐduī zhōng, tā xiānhuó de liútǎng zài cháimǐ-yóuyán de rénjiān yānhuǒ lǐ. Wúlùn shì mùjiang shǒuzhōng jīngzhǔn-wúwù de sǔnmǎo gòuzào, háishì chúshī huǒhòu zhōng chūshén-rùhuà de tiáowèi pínghéng, zhǐyào yòngxīn tǐwù jīngyì-qiújīng, píngfán suǒshì zhīzhōng jiē cáng zhe shēn'ào de dà xuéwen.",
                "en": "True learning lives not merely in dusty tomes, but flows through daily life. From a carpenter's seamless mortise joints to a chef's balanced seasonings, ordinary tasks harbor profound wisdom if approached with dedication.",
                "es": "El saber genuino no habita solo en viejos legajos, sino en las tareas cotidianas. Desde las ensambladuras precisas del carpintero hasta el sazón magistral del cocinero, la búsqueda de la perfección encierra una honda sabiduría."
            },
            {
                "id": "#2",
                "hanzi": "求学问之道在于知行合一。先贤倡导博学之、审问之、慎思之、明辨之、笃行之，强调学术研究不能脱离社会现实。学者只有扎根大地洞察民生疾苦，将理论创见转化为解决实际问题的良方，才能成就无愧于时代的大大学问。",
                "pinyin": "Qiú xuéwen zhī dào zàiyú zhīxíng-héyī. Xiānxián chàngdǎo bóxué zhī, shěnwèn zhī, shènsī zhī, míngbiàn zhī, dǔxíng zhī, qiángdiào xuéshù yánjiū bùnéng tuōlí shèhuì xiànshí. Xuézhě zhǐyǒu zhāgēn dàdì dòngchá mínshēng jíkǔ, jiāng lǐlùn chuàngjiàn zhuǎnhuà wéi jiějué shíjì wèntí de liángfāng, cáinéng chéngjiù wúkuì yú shídài de dà xuéwen.",
                "en": "The path of scholarship requires unity of knowing and doing. Sages urged wide learning, questioning, thinking, discerning, and practicing. Scholars must ground theories in real life, turning insights into remedies to achieve great scholarship.",
                "es": "El camino del saber exige unir conocimiento y acción. Los antiguos exhortaban a estudiar, inquirir, reflexionar y obrar con rectitud. Solo arraigando la teoría en los dilemas reales se forja una ciencia digna de su tiempo."
            }
        ]
    },

    # 15 讲究
    {
        "id": "15",
        "hanzi": "讲究",
        "pinyin": "jiǎng jiu",
        "part_of_speech": "Verb / Adjective / Noun",
        "meanings_summary": {
            "en": "to be particular about; to pay attention to; exquisite; tasteful; particularity",
            "es": "ser exigente con; cuidar al detalle; refinado; primoroso; esmero; minuciosidad"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to pay meticulous attention to, stress, or be exceptionally discerning and particular about quality or etiquette",
                "definition_es": "prestar minuciosa atención a, ser sumamente exigente con o cuidar con esmero la calidad o el protocolo",
                "example_phrase": "讲究卫生 (pay attention to hygiene)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "tasteful, exquisite, sophisticated, or delicately made",
                "definition_es": "primoroso, refinado, elegante o primorosamente elaborado",
                "example_phrase": "陈设很讲究 (furnishings are very tasteful)"
            },
            {
                "sense_number": "3",
                "part_of_speech": "Noun",
                "register": "Colloquial",
                "definition_en": "intricate rules, delicate techniques, or fine points to be observed",
                "definition_es": "reglas sutiles, detalles protocolarios o pormenores a tener en cuenta",
                "example_phrase": "很有讲究 (involves a great deal of fine points)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这间茶室的布置极为讲究，无论是几案上的宋瓷插花还是墙上的古画，都透出淡雅的文人趣味。",
                "pinyin": "Zhè jiān cháchì de bùzhì jíwéi jiǎngjiu, wúlùn shì jī'àn shàng de Sòng cí chāhuā háishì qiáng shàng de gǔhuà, dōu tòuchū dànyǎ de wénrén qùwèi.",
                "en": "The decor of this teahouse is extremely exquisite; whether the Song porcelain flower arrangement or antique scrolls, it exudes literati elegance.",
                "es": "La decoración de este salón de té es primorosa; tanto los jarrones de porcelana Song como las pinturas murales respiran refinamiento letrado."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅先生对饮食极为讲究，不仅挑选食材严苛，更对火候掌控与菜肴搭配有着极高的美学追求。",
                "pinyin": "Lǔ Xùn xiānsheng duì yǐnshí jíwéi jiǎngjiu, bùjǐn tiāoxuǎn shícái yánkē, gèng duì huǒhou zhǎngkòng yǔ càiyáo dāpèi yǒuzhe jí gāo de měixué zhuīqiú.",
                "en": "Mr. Lu Xun was extremely particular about dining; he not only selected ingredients rigorously, but held high aesthetic standards for cooking heat and pairings.",
                "es": "Lu Xun era muy exigente con la comida; no solo seleccionaba los ingredientes con rigor, sino que cuidaba al detalle el fuego y la armonía de los platos."
            }
        ],
        "collocations": [
            {"hanzi": "讲究卫生", "en": "pay attention to hygiene"},
            {"hanzi": "讲究吃穿", "en": "be particular about food and clothing"},
            {"hanzi": "穿着讲究", "en": "tastefully and impeccably dressed"},
            {"hanzi": "颇有讲究", "en": "have considerable fine points"},
            {"hanzi": "讲究实效", "en": "stress practical results"},
            {"hanzi": "讲究方法", "en": "pay attention to proper methods"}
        ],
        "idioms": [
            {"hanzi": "精益求精", "pinyin": "jīng yì qiú jīng", "meaning_en": "constantly strive for ever greater perfection"},
            {"hanzi": "一丝不苟", "pinyin": "yì sī bù gǒu", "meaning_en": "scrupulously meticulous; not overlooking a single thread"},
            {"hanzi": "吹毛求疵", "pinyin": "chuī máo qiú cī", "meaning_en": "nitpick and blow aside hair looking for tiny flaws"},
            {"hanzi": "登峰造极", "pinyin": "dēng fēng zào jí", "meaning_en": "reach the pinnacle of excellence"}
        ],
        "character_decomposition": [
            {
                "character": "讲",
                "pinyin": "jiǎng",
                "meaning_en": "speak; explain; stress; negotiate",
                "meaning_es": "hablar; explicar; enfatizar; negociar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (speech/words)",
                "sound_component": "井 (jǐng, well / orderly grid)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where speech 讠 is structured in an orderly grid 井, meaning to discuss and stress rules.",
                "visual_mnemonic_story_en": "Orderly words (讠) laid out like a neat square water well (井) explain instructions carefully (讲).",
                "visual_mnemonic_story_es": "Palabras claras (讠) ordenadas como el brocal de un pozo (井) exponen las normas con rigor (讲).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "IVTT",
                "traditional": "講"
            },
            {
                "character": "究",
                "pinyin": "jiu",
                "meaning_en": "investigate; examine thoroughly; after all",
                "meaning_es": "indagar; examinar a fondo; al fin",
                "radical": "穴",
                "radical_meaning_en": "cave",
                "meaning_component": "穴 (cave/depth)",
                "sound_component": "九 (jiǔ, nine / exhaustive limit)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ideogram showing probing to the ninth 九 extreme depth of a cave 穴, meaning exhaustive scrutiny.",
                "visual_mnemonic_story_en": "Probing deep into a dark cave (穴) nine (九) times leaves no stone unturned in thorough research (究).",
                "visual_mnemonic_story_es": "Explorar el fondo de la caverna (穴) hasta el límite nueve (九) no deja rincón sin escrutar (究).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JCKN",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Discuss rules with precision (讲) and probe to the deepest cave (究) to ensure everything is exquisite and particular (讲究).",
            "composite_memory_hook_es": "Expón las normas (讲) e indaga hasta el fondo (究) para asegurar que todo sea primoroso y refinado (讲究).",
            "cultural_and_cognitive_roots": "Originates from scholar-official aesthetics where living was elevated into an art form; 'jiǎngjiu' denotes mindful taste and refined restraint rather than vulgar ostentation.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by neutral tone: 'jiǎng jiu' (214-2). Syllable 'jiǎng' dips fully, and 'jiu' is softened into a light neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "许", "pinyin": "xǔ", "meaning_en": "allow; perhaps", "distinction_note": "Has 午 on right instead of 井"},
                {"character": "突", "pinyin": "tū", "meaning_en": "sudden; dash", "distinction_note": "Has 犬 below 穴 instead of 九"},
                {"character": "穷", "pinyin": "qióng", "meaning_en": "poor; exhausted", "distinction_note": "Has 力 below 穴 instead of 九"},
                {"character": "空", "pinyin": "kōng", "meaning_en": "empty; sky", "distinction_note": "Has 工 below 穴 instead of 九"}
            ],
            "etymological_cognates": [
                {"character": "雅", "pinyin": "yǎ", "gloss_en": "refined; elegant; standard"},
                {"character": "精", "pinyin": "jīng", "gloss_en": "refined rice; essence; exquisite"},
                {"character": "琢", "pinyin": "zhuó", "gloss_en": "carve jade meticulously"},
                {"character": "致", "pinyin": "zhì", "gloss_en": "delicate; fine; send"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "讲究 denotes meticulous attention to quality and refined aesthetic standards, or describes tastefully made artifacts.",
            "contrasts": [
                {"id": "1", "compared_word": "讲究 vs. 注重", "pinyin": "zhùzhòng", "analysis": "注重 is a neutral verb meaning to place emphasis on something, while 讲究 implies refined aesthetic taste, etiquette, or demanding connoisseurship."},
                {"id": "2", "compared_word": "讲究 vs. 精致", "pinyin": "jīngzhì", "analysis": "精致 is solely an adjective describing finely crafted physical objects, whereas 讲究 can function as verb (to stress), adjective (tasteful), or noun (delicate rule)."},
                {"id": "3", "compared_word": "讲究 vs. 挑剔", "pinyin": "tiāoti", "analysis": "挑剔 carries a negative nuance of being fussily hypercritical, whereas 讲究 represents cultured elegance and high standards."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活里的讲究，不是挥金如土的奢侈，而是一种取悦内心的自律与从容。清晨给花瓶换上一束带露的雏菊，沏茶时严格把握水温，这些看似繁琐的细节，正是让平淡日子开出花来的秘诀。讲究，是把平凡日子过成诗意。",
                "pinyin": "Shēnghuó lǐ de jiǎngjiu, bú shì huījīn-rútǔ de shěchǐ, ér shì yì zhǒng qǔyuè nèixīn de zìlǜ yǔ cóngróng. Qīngchén gěi huāpíng huànshàng yí shù dài lù de chújú, qīchá shí yángé bǎwò shuǐwēn, zhèxiē kànsì fánsuǒ de xìjié, zhèng shì ràng píngdàn rìzi kāichū huā lái de mìjué. Jiǎngjiu, shì bǎ píngfán rìzi guò chéng shīyì.",
                "en": "Being particular about life is not squandering money, but self-discipline and tranquility that pleases the soul. Replacing daisies with morning dew or controlling tea water temperature turns ordinary days into poetic moments.",
                "es": "El esmero cotidiano no es derroche, sino templanza y deleite interior. Poner margaritas frescas al alba o cuidar la temperatura del agua al preparar té son detalles que hacen florecer la rutina, convirtiendo lo ordinario en poesía."
            },
            {
                "id": "#2",
                "hanzi": "中国传统建筑对营造法式有着极其严苛的讲究。从梁架榫卯的咬合精度，到斗拱排布的力学结构，无不体现出古代匠人对天人合一哲学思想的崇高追求。这种对工艺极致讲究的工匠精神，正是中华传统营建文脉生生不息的根基。",
                "pinyin": "Zhōngguó chuántǒng jiànzhù duì yíngzào fǎshì yǒuzhe jíqí yánkē de jiǎngjiu. Cóng liángjià sǔnmǎo de yǎohé jīngdù, dào dǒugǒng páibù de lìxué jiégòu, wúbù tǐxiàn chū gǔdài jiàngrén duì tiānrén-héyī zhéxué sīxiǎng de chónggāo zhuīqiú. Zhè zhǒng duì gōngyì jízhì jiǎngjiu de gōngjiàng jīngshén, zhèng shì Zhōnghuá chuántǒng yíngjiàn wénmài shēngshēng-bùxī de gēnjī.",
                "en": "Traditional Chinese architecture enforces rigorous standards. From mortise precision to bracket mechanics, it reflects harmony between humanity and nature. This relentless commitment to craft excellence forms the foundation of architectural heritage.",
                "es": "La arquitectura tradicional china sigue pautas de construcción muy exigentes. Desde el ajuste de las vigas hasta los soportes ménsula, todo refleja la unión del hombre y el cosmos. Ese primoroso rigor artesanal sustenta la memoria edilicia."
            }
        ]
    },

    # 16 平均
    {
        "id": "16",
        "hanzi": "平均",
        "pinyin": "píng jūn",
        "part_of_speech": "Adjective / Adverb / Verb",
        "meanings_summary": {
            "en": "average; mean; equally; evenly divided; on average",
            "es": "promedio; medio; por término medio; igualar; equitativo; parejo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "equally distributed without bias, or representing an arithmetic mean",
                "definition_es": "distribuido a partes iguales o que representa una media aritmética",
                "example_phrase": "平均分配 (distribute equally)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "on average; evenly across units of time or count",
                "definition_es": "por término medio; de manera uniforme por unidad de tiempo o cuenta",
                "example_phrase": "平均每月 (on average each month)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "根据气象台的统计数据，该地区年平均气温在十五摄氏度左右，气候十分宜人舒适。",
                "pinyin": "Gēnjù qìxiàngtái de tǒngjì shùjù, gāi dìqū nián píngjūn qìwēn zài shíwǔ shèshìdù zuǒyòu, qìhòu shífēn yírén shūshì.",
                "en": "According to meteorological data, the annual average temperature in this region is around 15 degrees Celsius, very pleasant.",
                "es": "Según los registros meteorológicos, la temperatura media anual ronda los quince grados, haciendo el clima muy grato."
            },
            {
                "id": "#2",
                "hanzi": "查阅鲁迅在北京时期的日记发现，他平均每个月都要同挚友聚餐数次，足迹遍及各大知名餐馆。",
                "pinyin": "Cháyuè Lǔ Xùn zài Běijīng shíqī de rìjì fāxiàn, tā píngjūn měi ge yuè dōu yào tóng zhìyǒu jùcān shù cì, zújì biànjí gèdà zhīmíng cānguǎn.",
                "en": "Reviewing Lu Xun's Beijing diaries reveals that on average he dined out with close friends several times a month across famous restaurants.",
                "es": "Al consultar los diarios de Lu Xun en Pekín, se aprecia que por término medio se reunía a comer con amigos íntimos varias veces al mes."
            }
        ],
        "collocations": [
            {"hanzi": "平均水平", "en": "average level"},
            {"hanzi": "平均分配", "en": "equal distribution"},
            {"hanzi": "平均寿命", "en": "average life expectancy"},
            {"hanzi": "平均速度", "en": "average speed"},
            {"hanzi": "人均/平均收入", "en": "average income per capita"},
            {"hanzi": "平均分摊", "en": "share costs equally"}
        ],
        "idioms": [
            {"hanzi": "平分秋色", "pinyin": "píng fēn qiū sè", "meaning_en": "divide autumn scenery equally; share honors equally"},
            {"hanzi": "一视同仁", "pinyin": "yí shì tóng rén", "meaning_en": "treat everyone equally with same benevolence"},
            {"hanzi": "不患寡而患不均", "pinyin": "bú huàn guǎ ér huàn bù jūn", "meaning_en": "worry not about scarcity, but about unequal distribution"},
            {"hanzi": "水涨船高", "pinyin": "shuǐ zhǎng chuán gāo", "meaning_en": "when the water rises, the boat goes up too; tied fortunes"}
        ],
        "character_decomposition": [
            {
                "character": "平",
                "pinyin": "píng",
                "meaning_en": "flat; level; calm; equal; peace",
                "meaning_es": "plano; llano; sereno; igual; paz",
                "radical": "干",
                "radical_meaning_en": "shield/stem",
                "meaning_component": "于 (breath expanding levelly)",
                "sound_component": "八 (divide symmetrically)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideogram showing breath dispersing evenly to both sides along a level balance beam.",
                "visual_mnemonic_story_en": "A balanced scale rests level across the center bar, weighing both pans in fair equality (平).",
                "visual_mnemonic_story_es": "Una balanza de platillos se mantiene nivelada sobre el fiel, repartiendo el peso con equidad (平).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MFJ",
                "traditional": ""
            },
            {
                "character": "均",
                "pinyin": "jūn",
                "meaning_en": "equal; even; all; uniform",
                "meaning_es": "igual; parejo; uniforme; equitativo",
                "radical": "土",
                "radical_meaning_en": "earth",
                "meaning_component": "土 (soil/land to divide)",
                "sound_component": "匀 (yún, even / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where land 土 is apportioned evenly 匀 among farmers.",
                "visual_mnemonic_story_en": "Mounds of fertile soil (土) are divided evenly and uniformly (匀) among the field hands (均).",
                "visual_mnemonic_story_es": "Parcelas de tierra (土) se reparten de modo equitativo (匀) entre los campesinos (均).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "GPMM",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Level the scales (平) and distribute the soil evenly (均) to establish a fair average (平均).",
            "composite_memory_hook_es": "Nivela la balanza (平) y reparte la tierra por igual (均) para calcular el promedio (平均).",
            "cultural_and_cognitive_roots": "Derived from ancient agrarian land surveying (井田制) and balance scales; represents the Confucian value of egalitarian fairness and mathematical equilibrium.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by level high tone: 'píng jūn' (35-55). Smooth upward rise on 'píng', followed by a sustained high tone on 'jūn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "乎", "pinyin": "hū", "meaning_en": "particle", "distinction_note": "Has curved slant at top instead of flat horizontal line of 平"},
                {"character": "匀", "pinyin": "yún", "meaning_en": "even; uniform", "distinction_note": "Lacks the earth radical 土 on the left of 均"},
                {"character": "钓", "pinyin": "diào", "meaning_en": "fish with hook", "distinction_note": "Has metal radical 钅 on left instead of 土"},
                {"character": "半", "pinyin": "bàn", "meaning_en": "half", "distinction_note": "Vertical stroke crosses top stroke, unlike 平"}
            ],
            "etymological_cognates": [
                {"character": "衡", "pinyin": "héng", "gloss_en": "balance beam; weigh equally"},
                {"character": "齐", "pinyin": "qí", "gloss_en": "aligned; even like ear of wheat"},
                {"character": "等", "pinyin": "děng", "gloss_en": "equal; bamboo tallies equalized"},
                {"character": "称", "pinyin": "chèng", "gloss_en": "steelyard balance; weigh"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "平均 emphasizes mathematical arithmetic mean or dividing an aggregate equally across parts.",
            "contrasts": [
                {"id": "1", "compared_word": "平均 vs. 平等", "pinyin": "píngděng", "analysis": "平等 denotes political, legal, and human rights equality, while 平均 refers to mathematical quantities, statistical averages, or physical distribution."},
                {"id": "2", "compared_word": "平均 vs. 均匀", "pinyin": "jūnyún", "analysis": "均匀 describes spatial, temporal, or density consistency ('搅拌均匀', stir evenly), whereas 平均 emphasizes mathematical division or mean values."},
                {"id": "3", "compared_word": "平均 vs. 平常", "pinyin": "píngcháng", "analysis": "平常 means ordinary, commonplace, or routine, while 平均 denotes quantitative calculation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活的美好从不取决于平均分配的物质多寡，而在于感知幸福的心灵敏感度。同样是面对清风明月，有人视若无睹终日愁容满面，有人却能在粗茶淡饭中自得其乐。学会抚平内心的浮躁，生活才能展现出它温润柔和的原色。",
                "pinyin": "Shēnghuó de měihǎo cóng bù qǔjué yú píngjūn fēnpèi de wùzhì duōguǎ, ér zàiyú gǎnzhī xìngfú de xīnlíng mǐngǎndù. Tóngyàng shì miànduì qīngfēng-míngyuè, yǒurén shìruò-wúdǔ zhōngrì chóuróng-mǎnmiàn, yǒurén què néng zài chūchá-dànfàn zhōng zìdé-qílè. Xuéhuì fǔpíng nèixīn de fúzào, shēnghuó cáinéng zhǎnxiàn chū tā wēnrùn róuhé de yuánsè.",
                "en": "Life's beauty depends not on equally divided material wealth, but the soul's sensitivity to joy. Facing the breeze and moon, some fret while others find peace in simple meals. Calming inner restlessness reveals life's gentle colors.",
                "es": "La gracia de vivir no estriba en repartir bienes por igual, sino en abrir el corazón al gozo. Ante la luna y la brisa, unos viven pesarosos mientras otros hallan paz en la sencillez. Al serenar el ánimo, la vida revela su dulzura natural."
            },
            {
                "id": "#2",
                "hanzi": "随着公共卫生体系的持续健全，全国人均预期寿命已突破七十八岁大关。这一显著提升的平均数字背后，凝聚着基层医疗资源的均衡覆盖与重大疾病防治能力的全面跃升，切实保障了最广大人民群众最基本的健康权益。",
                "pinyin": "Suízhe gōnggòng wèishēng tǐxì de chíxù jiànquán, quánguó rénjūn yùqī shòumìng yǐ tūpò qīshíbā suì dàguān. Zhè yí xiǎnzhù tíshēng de píngjūn shùzì bèihòu, níngjù zhe jīcéng yīliáo zīyuán de jūnhéng fùgài yǔ zhòngdà jíbìng fángzhì nénglì de quánmiàn yuèshēng, qièshí bǎozhàng le zuì guǎngdà rénmín qúnzhòng zuì jīběn de jiànkāng quányì.",
                "en": "With public healthcare improving, average national life expectancy has surpassed 78 years. Behind this rising average figure lies balanced primary care coverage and disease prevention, safeguarding foundational health rights.",
                "es": "Con el afianzamiento sanitario, la esperanza media de vida ha superado los 78 años. Tras este promedio en alza se aúnan la cobertura equitativa de ambulatorios y la lucha contra dolencias graves, amparando el bienestar colectivo."
            }
        ]
    },

    # 17 胡同
    {
        "id": "17",
        "hanzi": "胡同",
        "pinyin": "hú tòng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "hutong; traditional narrow lane or alleyway (especially in Beijing)",
            "es": "hutong; callejón tradicional estrecho (especialmente en Pekín)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "traditional narrow street, lane, or alley formed by lines of siheyuan courtyards in northern Chinese cities",
                "definition_es": "callejuela o callejón tradicional flanqueado por casas con patio (siheyuan) típico de ciudades norteñas",
                "example_phrase": "穿过狭窄的胡同 (walk through a narrow hutong)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老北京的胡同曲径通幽，灰瓦四合院门前的大槐树下，几位老人正摇着蒲扇悠闲地下着象棋。",
                "pinyin": "Lǎo Běijīng de hútòng qūjìng-tōngyōu, huīwǎ sìhéyuàn ménqián de dà huáishù xià, jǐ wèi lǎorén zhèng yáo zhe púshàn yōuxián de xià zhe xiàngqí.",
                "en": "Old Beijing hutongs wind quietly; under the locust tree before grey-tiled courtyards, elders wave cattail fans, playing chess leisurely.",
                "es": "Los callejones del viejo Pekín serpentean apacibles; bajo las acacias ante patios señoriales, los ancianos juegan ajedrez con su abanico."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在北京生活了十四年，曾先后居住在南半截胡同的会馆与西三条胡同的四合院，留下了无数文学名篇。",
                "pinyin": "Lǔ Xùn zài Běijīng shēnghuó le shísì nián, céng xiānhòu jūzhù zài Nánbànjié Hútòng de huìguǎn yǔ Xīsāntiáo Hútòng de sìhéyuàn, liúxià le wúshù wénxué míngpiān.",
                "en": "Lu Xun lived in Beijing for 14 years, residing in Nanbanjie Hutong guild and Xisantiao courtyard, authoring countless literary masterworks.",
                "es": "Lu Xun residió 14 años en Pekín, viviendo en el callejón Nanbanjie y en el patio de Xisantiao, donde redactó célebres páginas literarias."
            }
        ],
        "collocations": [
            {"hanzi": "穿过胡同", "en": "pass through a hutong"},
            {"hanzi": "胡同文化", "en": "hutong culture"},
            {"hanzi": "老北京胡同", "en": "old Beijing hutong"},
            {"hanzi": "死胡同", "en": "dead end; blind alley; impasse"},
            {"hanzi": "胡同深处", "en": "deep in the hutong"},
            {"hanzi": "胡同人家", "en": "households in the alley"}
        ],
        "idioms": [
            {"hanzi": "曲径通幽", "pinyin": "qū jìng tōng yōu", "meaning_en": "a winding path leads to a quiet, secluded sanctuary"},
            {"hanzi": "深宅大院", "pinyin": "shēn zhái dà yuàn", "meaning_en": "spacious mansion with secluded inner courtyards"},
            {"hanzi": "街谈巷议", "pinyin": "jiē tán xiàng yì", "meaning_en": "street gossip and alley discussions"},
            {"hanzi": "走投无路", "pinyin": "zǒu tóu wú lù", "meaning_en": "have no way out; reach a dead end"}
        ],
        "character_decomposition": [
            {
                "character": "胡",
                "pinyin": "hú",
                "meaning_en": "reckless; beard; northern tribes; non-Han",
                "meaning_es": "imprudente; barba; pueblos del norte; nómada",
                "radical": "月",
                "radical_meaning_en": "moon / flesh",
                "meaning_component": "月 (flesh / dewlap of animal)",
                "sound_component": "古 (gǔ, ancient / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character showing dewlap flesh 月 of oxen; loan character transcribing Mongolian 'hottog' (water well).",
                "visual_mnemonic_story_en": "Ancient elders (古) stroke their long beards (月) while resting near northern water wells (胡).",
                "visual_mnemonic_story_es": "Ancianos (古) acarician sus largas barbas (月) junto a los pozos norteños de agua (胡).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JRB",
                "traditional": ""
            },
            {
                "character": "同",
                "pinyin": "tòng",
                "meaning_en": "same; alley; together",
                "meaning_es": "mismo; callejón; juntos",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "冂 (enclosure) + 一 (one)",
                "sound_component": "口 (kǒu, mouth in agreement)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Ideogram showing people speaking with one unified voice under an enclosure; used as phonetic loan for lane in hutong.",
                "visual_mnemonic_story_en": "Neighbors gather together under one enclosure (冂) to speak with one mouth (口) along the shared alley (同).",
                "visual_mnemonic_story_es": "Los vecinos se congregan bajo un mismo techo (冂) hablando a una sola voz (口) en el callejón común (同).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BMR",
                "traditional": "衚衕"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Northern travelers (胡) gathered together in agreement (同) around water-well settlements, giving birth to the hutong (胡同).",
            "composite_memory_hook_es": "Los pobladores del norte (胡) se agrupaban juntos (同) junto a los pozos de agua, creando el callejón hutong (胡同).",
            "cultural_and_cognitive_roots": "Linguistically derived from Mongolian 'hottog' (water well) during the Yuan Dynasty (Dadu / Beijing); settlements clustered around wells became narrow communal alleys.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone or neutral tone: 'hú tòng' (35-51 or 35-2 in Beijing dialect). Syllable 'tòng' drops firmly, often lightened in vernacular speech."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "糊", "pinyin": "hú", "meaning_en": "paste; paste up", "distinction_note": "Has rice radical 米 on the left side of 胡"},
                {"character": "湖", "pinyin": "hú", "meaning_en": "lake", "distinction_note": "Has water radical 氵 on the left side of 胡"},
                {"character": "洞", "pinyin": "dòng", "meaning_en": "cave; hole", "distinction_note": "Has water radical 氵 on left of 同"},
                {"character": "周", "pinyin": "zhōu", "meaning_en": "week; circle; complete", "distinction_note": "Has 土 at top instead of flat 一"}
            ],
            "etymological_cognates": [
                {"character": "巷", "pinyin": "xiàng", "gloss_en": "lane; narrow urban alleyway"},
                {"character": "街", "pinyin": "jiē", "gloss_en": "broad thoroughfare; street"},
                {"character": "弄", "pinyin": "lòng", "gloss_en": "lane in Shanghai shikumen alleys"},
                {"character": "坊", "pinyin": "fāng", "gloss_en": "urban residential subdivision ward"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "胡同 specifically denotes traditional northern Chinese residential alleys bordered by grey-brick courtyard walls.",
            "contrasts": [
                {"id": "1", "compared_word": "胡同 vs. 街道", "pinyin": "jiēdào", "analysis": "街道 refers broadly to paved city traffic streets with motor vehicles, whereas 胡同 refers to intimate residential alleys formed by courtyard walls."},
                {"id": "2", "compared_word": "胡同 vs. 弄堂", "pinyin": "lòngtáng", "analysis": "胡同 is the northern (Beijing) cultural term for lanes, while 弄堂 (or 里弄) specifically describes Shanghai and southern alleyways."},
                {"id": "3", "compared_word": "胡同 vs. 小巷", "pinyin": "xiǎoxiàng", "analysis": "小巷 is a generic, literary term for any narrow passage in any city, while 胡同 carries specific historical identity tied to Yuan, Ming, and Qing Beijing."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京的魂，大半凝固在错落有致的胡同里。斑驳的朱漆大门，门口蹲坐着威武的石狮，门墩上雕刻着吉祥的花草纹样。傍晚时分炊烟渐起，一声清脆悠长的鸽哨掠过瓦檐，那是深宅大院里最富有人情味的天伦图景。",
                "pinyin": "Lǎo Běijīng de hún, dàbàn nínggù zài cuòluò-yǒuzhì de hútòng lǐ. Bānbó de zhūqī dàmén, ménkǒu dūnzuò zhe wēiwǔ de shíshī, méndūn shàng diāokè zhe jíxiáng de huācǎo wényàng. Bàngwǎn shífēn chuīyān jiàn qǐ, yì shēng qīngcuì yōucháng de gēshào lüèguò wǎyán, nà shì shēnzhái-dàyuàn lǐ zuì fùyǒu rénqíngwèi de tiānlún tújǐng.",
                "en": "Old Beijing's soul is set in winding hutongs. Peeling vermilion gates flanked by stone lions and auspicious carvings welcome evening hearth smoke. A crisp pigeon whistle grazes tile eaves, painting a scene rich with human warmth.",
                "es": "El alma de Pekín reposa en sus callejones. Portones bermejos flanqueados por leones de piedra guardan el humo de las cocinas al atardecer. El silbido de las palomas surca los tejados, dibujando una estampa entrañable de convivencia."
            },
            {
                "id": "#2",
                "hanzi": "在现代城市更新与历史文化名城保护的交汇点上，胡同肌理的修复成了关键课题。市政规划者摒弃大拆大建的粗暴模式，转而推行渐进式的“微循环”改造。在保留原住民市井记忆的同时，完善供暖排污管网，让古老胡同焕发出现代宜居生机。",
                "pinyin": "Zài xiàndài chéngshì gēngxīn yǔ lìshǐ wénhuà míngchéng bǎohù de jiāohuìdiǎn shàng, hútòng jīlǐ de xiūfù chéng le guānjiàn kètí. Shìzhèng guīhuàzhě bǐngqì dàchāi-dàjiàn de cūbào móshì, zhuǎn'ér tuīxíng jiànjìnxìng de 'wēixúnhuán' gǎizào. Zài bǎoliú yuánzhùmín shìjǐng jìyì de tóngshí, wánshàn gōngnuǎn páiwū guǎnwǎng, ràng gǔlǎo hútòng huànfā chū xiàndài yíjū shēngjī.",
                "en": "Preserving historical cities makes hutong restoration pivotal. Planners abandon demolition for organic micro-renovation. Preserving resident memories while modernizing heating and drainage breathes livable vitality into ancient alleys.",
                "es": "En la renovación urbana, la restauración de los hutongs es crucial. Los urbanistas rechazan el derribo masivo y optan por mejoras graduales. Al renovar saneamientos y calefacción sin desalojar vecinos, los viejos callejones cobran nueva vida."
            }
        ]
    },

    # 18 位于
    {
        "id": "18",
        "hanzi": "位于",
        "pinyin": "wèi yú",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to be located at / in; to lie; to be situated in",
            "es": "situarse en; ubicarse en; hallarse en; encontrarse en"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to occupy a specific geographical position or physical location",
                "definition_es": "ocupar una posición geográfica determinada o hallarse emplazado en un lugar",
                "example_phrase": "位于市中心 (located in the city center)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这座闻名遐迩的历史文化名城位于长江下游平原，水网密布气候温和，自古就是鱼米之乡。",
                "pinyin": "Zhè zuò wénmíng-xiá'ěr de lìshǐ wénhuà míngchéng wèiyú Chángjiāng xiàyóu píngyuán, shuǐwǎng mìbù qìhòu wēnhé, zìgǔ jiùshì yúmǐ-zhīxiāng.",
                "en": "This famous historical city is located on the lower Yangtze plain; interlaced with canals and mild, it has been a land of fish and rice since antiquity.",
                "es": "Esta célebre urbe histórica se ubica en la llanura del curso bajo del Yangtsé; con clima templado y ríos, ha sido desde siempre emporio de arroz."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在北京长期居住的故居位于阜成门内宫门口二条，如今已被改建为国家级鲁迅博物馆。",
                "pinyin": "Lǔ Xùn zài Běijīng chángqī jūzhù de gùjū wèiyú Fùchéngmén nèi Gōngménkǒu èrtiáo, rújīn yǐ bèi gǎijiàn wéi guójiājí Lǔ Xùn Bówùguǎn.",
                "en": "Lu Xun's long-term former residence in Beijing is located at Fuchengmen; today it has been renovated into the national Lu Xun Museum.",
                "es": "La antigua morada de Lu Xun en Pekín se ubica en el callejón Gongmenkou de Fuchengmen; hoy ha sido convertida en Museo Nacional Lu Xun."
            }
        ],
        "collocations": [
            {"hanzi": "位于中心", "en": "located in the center"},
            {"hanzi": "位于沿海", "en": "located along the coast"},
            {"hanzi": "位于交界处", "en": "situated at the border/junction"},
            {"hanzi": "位于两座山之间", "en": "located between two mountains"},
            {"hanzi": "地理位置位于", "en": "geographical location is situated at"},
            {"hanzi": "位于核心区", "en": "situated in the core zone"}
        ],
        "idioms": [
            {"hanzi": "身居要职", "pinyin": "shēn jū yào zhí", "meaning_en": "occupy an essential, pivotal official post"},
            {"hanzi": "得天独厚", "pinyin": "dé tiān dú hòu", "meaning_en": "blessed with exceptional natural advantages"},
            {"hanzi": "坐北朝南", "pinyin": "zuò běi cháo nán", "meaning_en": "face south with back to the north; ideal orientation"},
            {"hanzi": "依山傍水", "pinyin": "yī shān bàng shuǐ", "meaning_en": "nestled against mountains and beside water"}
        ],
        "character_decomposition": [
            {
                "character": "位",
                "pinyin": "wèi",
                "meaning_en": "position; place; seat; status",
                "meaning_es": "posición; lugar; asiento; estatus",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person)",
                "sound_component": "立 (lì, stand upright / position)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing an official person 亻 standing upright 立 in an assigned rank or court seat.",
                "visual_mnemonic_story_en": "A respected person (亻) stands tall (立) at their rightful appointed post and seat (位).",
                "visual_mnemonic_story_es": "Una persona digna (亻) permanece erguida (立) ocupando el puesto y sitial que le corresponde (位).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OYT",
                "traditional": ""
            },
            {
                "character": "于",
                "pinyin": "yú",
                "meaning_en": "in; at; on; than; by",
                "meaning_es": "en; a; sobre; que; por",
                "radical": "二",
                "radical_meaning_en": "two",
                "meaning_component": "一 (heaven and earth bounds)",
                "sound_component": "亅 (hook / breath)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictogram showing breath curling forth freely; grammatical preposition denoting location in or at.",
                "visual_mnemonic_story_en": "A level beam supports a vertical plumb line that marks exact placement at (于) the destination.",
                "visual_mnemonic_story_es": "El travesaño horizontal sostiene una plomada que señala la ubicación exacta en (于) el mapa.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MD",
                "traditional": "於"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Take an assigned place (位) at a specific geographical coordinate (于) to be located in (位于).",
            "composite_memory_hook_es": "Ocupa un sitial físico (位) en un punto exacto (于) para hallarte ubicado en (位于).",
            "cultural_and_cognitive_roots": "Combining the spatial noun 'wèi' (seat/post) with the classical locative coverb 'yú' (in/at); standard formal expression in geographic and academic literature.",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by rising tone: 'wèi yú' (51-35). Crisp descent on 'wèi', followed by a smooth upward glide on 'yú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "拉", "pinyin": "lā", "meaning_en": "pull", "distinction_note": "Has hand radical 扌 on left instead of person 亻"},
                {"character": "泣", "pinyin": "qì", "meaning_en": "weep", "distinction_note": "Has water radical 氵 on left instead of 亻"},
                {"character": "干", "pinyin": "gān", "meaning_en": "dry; stem", "distinction_note": "Has straight vertical stroke without bottom right hook"},
                {"character": "子", "pinyin": "zǐ", "meaning_en": "child", "distinction_note": "Has curved hook and crossing horizontal stroke"}
            ],
            "etymological_cognates": [
                {"character": "置", "pinyin": "zhì", "gloss_en": "place; set down firmly"},
                {"character": "坐", "pinyin": "zuò", "gloss_en": "sit; face direction"},
                {"character": "座", "pinyin": "zuò", "gloss_en": "seat; pedestal; base"},
                {"character": "处", "pinyin": "chù", "gloss_en": "dwelling place; department"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "位于 is a formal locative verb indicating precise geographical coordinates or physical orientation.",
            "contrasts": [
                {"id": "1", "compared_word": "位于 vs. 在", "pinyin": "zài", "analysis": "在 is the ubiquitous everyday preposition/verb for general presence, whereas 位于 is a formal written verb reserved for geography, buildings, and territories."},
                {"id": "2", "compared_word": "位于 vs. 处于", "pinyin": "chǔyú", "analysis": "位于 denotes static physical/geographic placement ('位于东亚'), whereas 处于 denotes dynamic abstract condition, status, or stage ('处于转型期')."},
                {"id": "3", "compared_word": "位于 vs. 坐落", "pinyin": "zuòluò", "analysis": "坐落 is poetic and descriptive of buildings resting on landscapes ('坐落于山谷'), while 位于 is objective, factual, and cartographic."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "位于云贵高原深处的古老村落，千百年来被苍翠的崇山峻岭环抱。奔腾的溪流穿寨而过，青石板路在薄雾中若隐若现。这里没有都市车马的喧嚣，只有晨钟暮鼓与袅袅炊烟，宛如世外桃源般静谧安详，守护着古朴的民风。",
                "pinyin": "Wèiyú Yún-Guì gāoyuán shēnchù de gǔlǎo cūnluò, qiānbǎi nián lái bèi cāngcuì de chóngshān-jùnlǐng huánbào. Bēnténg de xīliú chuānzhài-érguò, qīngshíbǎn lù zài báowù zhōng ruòyǐn-ruòxiàn. Zhèlǐ méiyǒu dūshì chēmǎ de xuānxiāo, zhǐyǒu chénzhōng-mùgǔ yǔ niǎoniǎo chuīyān, wǎnrú shìwài-táoyuán bān jìngmì ānxiáng, shǒuhù zhe gǔpǔ de mínfēng.",
                "en": "The ancient village located in the Yunnan-Guizhou plateau has been cradled by peaks for millennia. Rushing streams bisect stone paths in mist. Free from urban clamor, morning bells and hearth smoke guard pastoral tranquility.",
                "es": "Ubicada en la meseta de Yunnan y Guizhou, la aldea milenaria reposa entre cumbres. El arroyo cruza las veredas de piedra bajo la niebla. Lejos del fragor urbano, las campanas y el humo del hogar custodian la paz rústica."
            },
            {
                "id": "#2",
                "hanzi": "位于欧亚大陆十字路口的中亚重镇，自古便是丝绸之路贸易通道上的战略要冲。随着跨境货运班列的常态化开行，这座内陆枢纽城市焕发出勃勃生机，现代物流基地与保税仓储设施拔地而起，有力促进了跨区域多边经贸合作。",
                "pinyin": "Wèiyú Ōu-Yà dàlù shízìlùkǒu de Zhōngyà zhòngzhèn, zìgǔ biàn shì Sīchóu zhī Lù màoyì tōngdào shàng de zhànlüè yàochōng. Suízhe kuājìng huòyùn bānliè de chángtàihuà kāixíng, zhè zuò nèilù shūniǔ chéngshì huànfā chū bóbó shēngjī, xiàndài wùliú jīdì yǔ bǎoshuì cāngchǔ shèshī bádì-érqǐ, yǒulì cùjìn le kuà-qūyù duōbiān jīngmào hézuò.",
                "en": "A central Asian town located at the Eurasian crossroads has long been a Silk Road bastion. Regular cross-border rail links revive this hub, where logistics parks and bonded warehouses boost multilateral trade.",
                "es": "Ubicado en la encrucijada euroasiática, este enclave de Asia Central fue baluarte de la Ruta de la Seda. Gracias al ferrocarril transfronterizo, el nodo renace con almacenes logísticos que impulsan el comercio multilateral."
            }
        ]
    },

    # 19 首
    {
        "id": "19",
        "hanzi": "首",
        "pinyin": "shǒu",
        "part_of_speech": "Noun / Measure Word / Adjective",
        "meanings_summary": {
            "en": "head; chief; first; leader; measure word for poems, songs, and melodies",
            "es": "cabeza; primero; líder; principal; clasificador para poemas y canciones"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Formal",
                "definition_en": "head of a body, or the leader/head of an organization",
                "definition_es": "cabeza física, o máxima autoridad y líder de una comitiva o estado",
                "example_phrase": "昂首挺胸 (hold head high with chest out)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Measure Word",
                "register": "Standard",
                "definition_en": "classifier for poems, poetic verses, lyrics, and musical songs",
                "definition_es": "clasificador para composiciones poéticas, canciones y melodías",
                "example_phrase": "一首动人的歌 (a moving song)"
            },
            {
                "sense_number": "3",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "first in order, primary, or initial",
                "definition_es": "primero en orden, primordial o de rango prioritario",
                "example_phrase": "首次登台 (first appearance on stage)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "晚会上，音乐家深情弹唱了一首脍炙人口的经典老歌，唤起了现场观众无尽的美好回忆。",
                "pinyin": "Wǎnhuì shàng, yīnyuèjiā shēnqíng tánchàng le yì shǒu kuàizhì-rénkǒu de jīngdiǎn lǎogē, huànqǐ le xiànchǎng guānzhòng wújìn de měihǎo huíyì.",
                "en": "At the gala, the musician passionately sang a beloved classic song, awakening endless fond memories in the audience.",
                "es": "En la velada, el músico entonó con emoción una canción clásica inolvidable, despertando bellos recuerdos en los asistentes."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅先生发表的《狂人日记》是中国现代文学史上第一篇白话短篇小说，堪称新文学运动的首发之作。",
                "pinyin": "Lǔ Xùn xiānsheng fābiǎo de 《Kuángrén Rìjì》 shì Zhōngguó xiàndài wénxué shǐ shàng dì yī piān báihuà duǎnpiān xiǎoshuō, kānchēng xīn wénxué yùndòng de shǒufā zhī zuò.",
                "en": "Lu Xun's 'Diary of a Madman' was the first vernacular short story in modern Chinese literature, truly the inaugural work of the New Literature movement.",
                "es": "El 'Diario de un loco' de Lu Xun fue el primer relato en lengua vernácula de las letras chinas modernas, hito inaugural de la nueva literatura."
            }
        ],
        "collocations": [
            {"hanzi": "一首诗", "en": "a poem"},
            {"hanzi": "一首歌", "en": "a song"},
            {"hanzi": "首次", "en": "for the first time"},
            {"hanzi": "首要任务", "en": "primary task; top priority"},
            {"hanzi": "首席执行官", "en": "chief executive officer (CEO)"},
            {"hanzi": "首都", "en": "national capital"}
        ],
        "idioms": [
            {"hanzi": "首屈一指", "pinyin": "shǒu qū yì zhǐ", "meaning_en": "bend the thumb first; second to none; top notch"},
            {"hanzi": "昂首阔步", "pinyin": "áng shǒu kuò bù", "meaning_en": "stride forward proudly with head held high"},
            {"hanzi": "马首是瞻", "pinyin": "mǎ shǒu shì zhān", "meaning_en": "follow the leader's horse head; follow another's lead"},
            {"hanzi": "始料未及", "pinyin": "shǐ liào wèi jí", "meaning_en": "unforeseen from the very beginning"}
        ],
        "character_decomposition": [
            {
                "character": "首",
                "pinyin": "shǒu",
                "meaning_en": "head; chief; first; poem classifier",
                "meaning_es": "cabeza; principal; primero; clasificador",
                "radical": "首",
                "radical_meaning_en": "head",
                "meaning_component": "自 (nose/face) + 丷 (hair on head)",
                "sound_component": "首 (shǒu)",
                "stroke_count": 9,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram depicting a human head with hair 丷 and prominent nose/eye; source of concepts of leadership and beginning.",
                "visual_mnemonic_story_en": "Wisps of hair (丷) crown the forehead above facial features to represent the vital head and leader (首).",
                "visual_mnemonic_story_es": "Mechones de pelo (丷) coronan la frente sobre los ojos para representar la cabeza y la primacía (首).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "TBU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The head (首) sits at the very top of the body, designating the first rank and the measure word for a song (首).",
            "composite_memory_hook_es": "La cabeza (首) corona la cima del cuerpo, simbolizando lo primero y sirviendo de clasificador para canciones (首).",
            "cultural_and_cognitive_roots": "An anatomical radical in Kangxi lexicography; bodily primacy of the head gave rise to political leadership (首领, 元首) and numerical commencement (首先, 首席).",
            "tone_sandhi_and_pitch_modulation": "Dipping 3rd tone: 'shǒu' (214). Pronounce with an articulate dipping and rising tone contour without rushing."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "道", "pinyin": "dào", "meaning_en": "road; way", "distinction_note": "Has walking radical 辶 wrapping around 首"},
                {"character": "自", "pinyin": "zì", "meaning_en": "self", "distinction_note": "Lacks the top two hair strokes 丷 that crown 首"},
                {"character": "百", "pinyin": "bǎi", "meaning_en": "hundred", "distinction_note": "Has flat horizontal stroke at top without hair horns"},
                {"character": "盲", "pinyin": "máng", "meaning_en": "blind", "distinction_note": "Has 亡 over 目 instead of 首"}
            ],
            "etymological_cognates": [
                {"character": "头", "pinyin": "tóu", "gloss_en": "head; beginning; first"},
                {"character": "领", "pinyin": "lǐng", "gloss_en": "neck; collar; lead; govern"},
                {"character": "初", "pinyin": "chū", "gloss_en": "initial; cut cloth at beginning"},
                {"character": "元", "pinyin": "yuán", "gloss_en": "first; head; original sovereign"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "首 designates the foremost position, head rank, or functions as a classical measure word for poems/songs.",
            "contrasts": [
                {"id": "1", "compared_word": "首 vs. 头", "pinyin": "tóu", "analysis": "头 is the common everyday colloquial word for physical head, while 首 is elevated, formal, and poetic ('昂首', '元首')."},
                {"id": "2", "compared_word": "首 vs. 首/曲", "pinyin": "qǔ", "analysis": "曲 is a measure word restricted solely to musical tunes and melodies ('一曲梁祝'), while 首 applies to both poems and lyrics."},
                {"id": "3", "compared_word": "首 vs. 第一", "pinyin": "dì-yī", "analysis": "第一 is a general ordinal number (first), whereas 首 combines ordinal priority with chief executive status ('首席')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "诗歌是人类心灵最纯粹的低语。在孤独清冷的夜晚，捧读一首直击心灵的哲理诗，那些凝练如金石的字句，瞬间抚平了浮躁与疲惫。好的诗作如同一盏明灯，在漫漫长夜里为疲惫的旅人照亮回归内心的归途。",
                "pinyin": "Shīgē shì rénlèi xīnlíng zuì chúncuì de dīyǔ. Zài gūdú qīnglěng de yèwǎn, pěngdú yì shǒu zhíjī-xīnlíng de zhélǐshī, nàxiē níngliàn rú jīnshí de zìjù, shùnjiān fǔpíng le fúzào yǔ píbèi. Hǎo de shīzuò rútóng yì zhǎn míngdēng, zài mànmàn chángyè lǐ wèi píbèi de lǚrén zhàoliàng huíguī nèixīn de guītú.",
                "en": "Poetry is the soul's purest whisper. On lonely nights, reading a philosophical poem with words condensed like jade soothes exhaustion. Fine poems are lanterns lighting the traveler's return to peace.",
                "es": "La poesía es el susurro más íntimo del alma. En la quietud nocturna, leer un poema que cala hondo disipa la fatiga. Los versos maestros son candiles que alumbran al caminante cansado en su regreso al sosiego interior."
            },
            {
                "id": "#2",
                "hanzi": "把保障和改善民生作为经济社会发展的首要任务，是执政为民理念的生动体现。各地政府通过完善多层次社会保障网，将解决好群众关心的就业、教育、医疗等实际问题放在首位，切实提升广大百姓的获得感与安全感。",
                "pinyin": "Bǎ bǎozhàng yǔ gǎishàn mínshēng zuòwéi jīngjì shèhuì fāzhǎn de shǒuyào rènwù, shì zhízhèng-wèimín lǐniàn de shēngdòng tǐxiàn. Gèdì zhèngfǔ tōngguò wánshàn duō céngcì shèhuì bǎozhàng wǎng, jiāng jiějué hǎo qúnzhòng guānxīn de jiùyè, jiàoyù, yīliáo děng shíjì wèntí fàng zài shǒuwèi, qièshí tíshēng guǎngdà bǎixìng de huòdé gǎn yǔ ānquán gǎn.",
                "en": "Making public well-being the primary task of development embodies service to the people. Expanding social security networks prioritizes employment, schooling, and healthcare, enhancing the populace's sense of security.",
                "es": "Priorizar el bienestar ciudadano como tarea primordial traduce el compromiso social en hechos. Al afianzar la seguridad social y atender empleo, salud y educación, los gobiernos fortalecen la certidumbre colectiva."
            }
        ]
    },

    # 20 豪华
    {
        "id": "20",
        "hanzi": "豪华",
        "pinyin": "háo huá",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "luxurious; lavish; sumptuous; opulent; splendid",
            "es": "lujoso; suntuoso; fastuoso; opulento; de gran lujo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "lavishly decorated, sumptuous, highly expensive, and opulent in appointments or lifestyle",
                "definition_es": "decorado con suntuosidad, sumamente costoso, espléndido u opulento en instalaciones o estilo",
                "example_phrase": "豪华酒店 (luxury hotel)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这座豪华的海景度假酒店设施一应俱全，窗外便是碧海银沙，吸引了许多游客前来度假。",
                "pinyin": "Zhè zuò háohuá de hǎijǐng dùjià jiǔdiàn shèshī yìyīng-jùquán, chuāngwài biàn shì bìhǎi-yínshā, xīyǐn le xǔduō yóukè qiánlái dùjià.",
                "en": "This luxurious oceanfront resort hotel is fully appointed; with azure sea and white sand outside, it attracts numerous holidaymakers.",
                "es": "Este lujoso complejo turístico frente al mar cuenta con todos los servicios; sus vistas de arena y agua turquesa atraen a muchos viajeros."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅常去的北京广和居饭馆虽然称不上豪华，但菜肴风味地道，极适合好友促膝畅谈。",
                "pinyin": "Lǔ Xùn cháng qù de Běijīng Guǎnghéjū fànguǎn suīrán chēngbùshàng háohuá, dàn càiyáo fēngwèi dìdao, jí shìhé hǎoyǒu cùxī-chàngtán.",
                "en": "Although Guangheju restaurant where Lu Xun dined could hardly be called luxurious, its authentic flavors were perfect for intimate talks.",
                "es": "Aunque el mesón Guangheju que Lu Xun frecuentaba no era lujoso, su sazón castizo era idóneo para largas sobremesas de amigos."
            }
        ],
        "collocations": [
            {"hanzi": "豪华客房", "en": "deluxe guestroom"},
            {"hanzi": "豪华轿车", "en": "luxury sedan/limousine"},
            {"hanzi": "阵容豪华", "en": "star-studded lineup"},
            {"hanzi": "豪华装修", "en": "sumptuous interior renovation"},
            {"hanzi": "奢靡豪华", "en": "lavish and extravagant"},
            {"hanzi": "豪华游轮", "en": "luxury cruise ship"}
        ],
        "idioms": [
            {"hanzi": "富丽堂皇", "pinyin": "fù lì táng huáng", "meaning_en": "sumptuous and magnificent; splendid palace-like grandeur"},
            {"hanzi": "金碧辉煌", "pinyin": "jīn bì huī huáng", "meaning_en": "resplendent with gold and jade luster; glittering"},
            {"hanzi": "琼楼玉宇", "pinyin": "qióng lóu yù yǔ", "meaning_en": "magnificent jade halls in fairy realm"},
            {"hanzi": "朴实无华", "pinyin": "pǔ shí wú huá", "meaning_en": "simple and unadorned; plain and genuine"}
        ],
        "character_decomposition": [
            {
                "character": "豪",
                "pinyin": "háo",
                "meaning_en": "grand; heroic; bold; opulent; porcupine",
                "meaning_es": "grandioso; heroico; audaz; magnate",
                "radical": "豕",
                "radical_meaning_en": "pig",
                "meaning_component": "豕 (boar with bristling spines)",
                "sound_component": "高 (gāo, tall / noble / phonetic)",
                "stroke_count": 14,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient pictogram showing a wild boar 豕 with formidable bristling spines, symbolizing unrestrained heroic grandeur.",
                "visual_mnemonic_story_en": "A majestic leader stands tall (高) alongside mighty guardian assets (豕), exuding noble boldness (豪).",
                "visual_mnemonic_story_es": "Un prócer eminente se alza alto (高) protegiendo el vigoroso porcino (豕) con porte magnánimo (豪).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YRMSO",
                "traditional": ""
            },
            {
                "character": "华",
                "pinyin": "huá",
                "meaning_en": "splendid; flowery; illustrious; China",
                "meaning_es": "espléndido; florido; ilustre; China",
                "radical": "十",
                "radical_meaning_en": "ten",
                "meaning_component": "艸 (flowers blooming in traditional 華)",
                "sound_component": "于 (breath) + 夸 (kuā, grand)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Traditional 華 depicts abundant radiant tree blossoms; simplified to 华 representing glorious radiance.",
                "visual_mnemonic_story_en": "Lush branches blossom with vibrant flowers, creating splendid visual magnificence (华).",
                "visual_mnemonic_story_es": "Ramas lozanas florecen con exhuberancia, creando un espectáculo espléndido y radiante (华).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OPJ",
                "traditional": "華"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Heroic bold power (豪) paired with radiant flowering splendor (华) creates magnificent luxury (豪华).",
            "composite_memory_hook_es": "El porte señorial (豪) sumado al esplendor florido (华) engendra el mayor lujo (豪华).",
            "cultural_and_cognitive_roots": "Derived from classical descriptions of high aristocratic life; 'háo' denoted noble chivalric wealth and 'huá' denoted resplendent ornamentation.",
            "tone_sandhi_and_pitch_modulation": "Two rising tones: 'háo huá' (35-35). Smooth parallel rising pitch contours from mid to high."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "家", "pinyin": "jiā", "meaning_en": "family", "distinction_note": "Has 宀 at top instead of 亠 and 口"},
                {"character": "毫", "pinyin": "háo", "meaning_en": "hair; fine millimeter", "distinction_note": "Has 毛 at bottom instead of 豕"},
                {"character": "毕", "pinyin": "bì", "meaning_en": "complete", "distinction_note": "Has 比 at top instead of 人 and horizontal strokes"},
                {"character": "化", "pinyin": "huà", "meaning_en": "transform", "distinction_note": "Has 亻 and 匕 side-by-side, unlike 华"}
            ],
            "etymological_cognates": [
                {"character": "奢", "pinyin": "shē", "gloss_en": "luxurious; extravagant"},
                {"character": "侈", "pinyin": "chǐ", "gloss_en": "excessive; waste of wealth"},
                {"character": "盛", "pinyin": "shèng", "gloss_en": "flourishing; abundant feast"},
                {"character": "丽", "pinyin": "lì", "gloss_en": "beautiful; magnificent pair"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "豪华 describes extravagant, highly expensive, and lavishly appointed environments, vehicles, or lineups.",
            "contrasts": [
                {"id": "1", "compared_word": "豪华 vs. 奢华", "pinyin": "shēhuá", "analysis": "奢华 carries a stronger flavor of ostentatious, wasteful private indulgence, while 豪华 can describe positive world-class hotel or theater amenities."},
                {"id": "2", "compared_word": "豪华 vs. 雄伟", "pinyin": "xióngwěi", "analysis": "雄伟 emphasizes grand physical scale and imposing mountain/architectural stature, while 豪华 stresses high monetary cost and plush interior fittings."},
                {"id": "3", "compared_word": "豪华 vs. 考究", "pinyin": "kǎojiu", "analysis": "考究 emphasizes refined, meticulous craftsmanship and connoisseur taste, whereas 豪华 emphasizes sheer opulence and scale."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "真正的富足不在于拥有豪华的豪宅与名车，而在于内心世界的宁静与坦荡。当一个人褪去了对物质奢华的盲目执念，方能在山川草木中领略造化之美，在简朴平淡的生活中品味出最纯粹的幸福。心若丰盈，处处皆胜景。",
                "pinyin": "Zhēnzhèng de fùzú bú zàiyú yǒngyǒu háohuá de háozhái yǔ míngchē, ér zàiyú nèixīn shìjiè de níngjìng yǔ tǎndàng. Dāng yí ge rén tuìqù le duì wùzhì shēhuá de mángmù zhíniàn, fāng néng zài shānchuān-cǎomù zhōng lǐnglüè zàohuà zhī měi, zài jiǎnpǔ píngdàn de shēnghuó zhōng pǐnwèi chū zuì chúncuì de xìngfú. Xīn ruò fēngyíng, chùchù jiē shèngjǐng.",
                "en": "True wealth lies not in luxury mansions or cars, but tranquility of the soul. Stripping away blind attachment to opulence allows one to appreciate nature's beauty and taste pure happiness in simplicity. A rich mind finds wonders everywhere.",
                "es": "La riqueza cabal no reside en mansiones o coches lujosos, sino en la serenidad de ánimo. Quien se desprende del apego suntuoso descubre la belleza del paisaje y saborea la dicha en lo humilde. Un corazón fecundo halla hermosura en todo rincón."
            },
            {
                "id": "#2",
                "hanzi": "近年来，文化消费呈现出从追求豪华排场向注重精神内涵的理性回归。观众不再仅仅为金碧辉煌的舞台布景与豪华明星阵容买单，而是愈发看重艺术剧目的叙事深度与思想张力。这一转变倒逼演艺市场去粗取精，回归创作本体。",
                "pinyin": "Jìnniánlái, wénhuà xiāofèi chéngxiàn chū cóng zhuīqiú háohuá páichǎng xiàng zhùzhòng jīngshén nèihán de lǐxìng huíguī. Guānzhòng bù zài jǐnjǐn wèi jīnbì-huīhuáng de wǔtái bùjǐng yǔ háohuá míngxīng zhènróng mǎidān, ér shì yùfā kànzhòng yìshù jùmù de xùshì shēndù yǔ sīxiǎng zhānglì. Zhè yí zhuǎnbiàn dàobī yǎnyì shìchǎng qùcū-qǔjīng, huíguī chuàngzuò běntǐ.",
                "en": "Cultural consumption is returning from lavish spectacles to spiritual substance. Audiences no longer pay just for glittering sets or luxury star casts, but value narrative depth, compelling theaters to focus on core artistic creation.",
                "es": "El consumo cultural retorna del fasto escénico a la sustancia intelectual. El público ya no premia decorados dorados o repartos deslumbrantes, sino el calado dramático, empujando a los escenarios a depurar su oferta y volver a la esencia."
            }
        ]
    }
]

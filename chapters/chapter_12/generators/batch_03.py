# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 称霸
    {
        "id": "21",
        "hanzi": "称霸",
        "pinyin": "chēng bà",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to dominate; reign supreme; hold hegemony; lord it over",
            "es": "dominar; erigirse en potencia hegemónica; imponer supremacía; reinar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to dominate, rule supreme, or exert undisputed hegemony in a commercial, political, or sporting arena",
                "definition_es": "ejercer hegemonía o dominio indiscutible en el terreno comercial, político o deportivo",
                "example_phrase": "称霸市场 (dominate the market)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在群雄逐鹿的国际移动社交市场上，传统西方应用长期称霸的格局正受到新兴创新力量的强力挑战。",
                "pinyin": "Zài qúnxióng-zhùlù de guójì yídòng shèjiāo shìchǎng shàng, chuántǒng xīfāng yìngyòng chángqī chēngbà de gégú zhèng shòudào xīnxīng chuàngxīn lìliang de qiánglì tiǎozhàn.",
                "en": "In the fiercely contested international mobile social market, the long-term dominance of traditional Western apps is being strongly challenged by emerging innovators.",
                "es": "En el reñido mercado global de redes móviles, la hegemonía histórica de las apps occidentales afronta el pujante reto de nuevos rivales."
            },
            {
                "id": "#2",
                "hanzi": "这家老牌足球豪门在过去十几年间多次称霸欧洲冠军联赛，铸就了一段辉煌夺目的王朝传奇。",
                "pinyin": "Zhè jiā lǎopái zúqiú háomén zài guòqù shí jǐ nián jiān duō cì chēngbà Ōuzhōu Guānjùn Liánsài, zhùjiùle yī duàn huīhuáng duómù de wángcháo chuánqí.",
                "en": "This storied football powerhouse dominated the UEFA Champions League multiple times over the past decade, forging a glorious dynasty legend.",
                "es": "Este histórico coloso del fútbol reinó en varias ediciones de la Liga de Campeones en la última década, forjando una dinastía legendaria."
            }
        ],
        "collocations": [
            {"hanzi": "称霸世界", "en": "dominate the world; achieve world hegemony"},
            {"hanzi": "称霸市场", "en": "dominate the market"},
            {"hanzi": "称霸一方", "en": "hold sway over a whole region"},
            {"hanzi": "企图称霸", "en": "attempt to seek hegemony"},
            {"hanzi": "难以称霸", "en": "hard to dominate"},
            {"hanzi": "长期称霸", "en": "dominate for a long time"}
        ],
        "idioms": [
            {"hanzi": "称霸一方", "pinyin": "chēng bà yī fāng", "meaning_en": "hold undisputed sway over a region; local despot"},
            {"hanzi": "独霸天下", "pinyin": "dú bà tiān xià", "meaning_en": "monopolize supreme power over all under heaven"},
            {"hanzi": "争霸天下", "pinyin": "zhēng bà tiān xià", "meaning_en": "contend for hegemony over the whole realm"},
            {"hanzi": "横行霸道", "pinyin": "héng xíng bà dào", "meaning_en": "tyrannize and ride roughshod over everyone"}
        ],
        "character_decomposition": [
            {
                "character": "称",
                "pinyin": "chēng",
                "meaning_en": "call; praise; weigh; claim",
                "meaning_es": "llamar; proclamar; elogiar; pesar; atribuirse",
                "radical": "禾",
                "radical_meaning_en": "grain",
                "meaning_component": "禾 (grain harvest on scale) + 爯 (hand lifting balance scale weight)",
                "sound_component": "爯 (chēng, balance / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand lifting a steelyard scale 爯 to balance and weigh grain 禾; extended to evaluating, calling, claiming, or proclaiming titles.",
                "visual_mnemonic_story_en": "Holding up a scale to weigh harvested grain (禾) fairly determines and claims title (称).",
                "visual_mnemonic_story_es": "Alzar una balanza para calibrar el grano cosechado (禾) y proclamar su justo rango (称).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "HDFB",
                "traditional": "稱"
            },
            {
                "character": "霸",
                "pinyin": "bà",
                "meaning_en": "hegemon; overlord; tyrant; dominate",
                "meaning_es": "hegemón; señor feudal supremo; tirano; dominar",
                "radical": "雨",
                "radical_meaning_en": "rain",
                "meaning_component": "雨 (clouds/rain pouring down) + 革/月 (moonlight crescent / leather force)",
                "sound_component": "Archaic phonetic nuance in 覇",
                "stroke_count": 21,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Originally the emerging white glow of the new moon beneath rain clouds; extended in the Spring and Autumn period to feudal warlords who held supreme military hegemony (五霸).",
                "visual_mnemonic_story_en": "Thunderclouds of rain (雨) gathering over a defiant warrior wielding supreme warlord might (霸).",
                "visual_mnemonic_story_es": "Nubarrone de lluvia (雨) bajo los que se alza un caudillo marcial que impone su supremacía (霸).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MBUB",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Proclaiming titles on the scales (称) backed by undisputed warlord hegemony (霸) is dominating the realm (称霸).",
            "composite_memory_hook_es": "Proclamarse con orgullo (称) señor hegemónico supremo (霸) es dominar o reinar (称霸).",
            "cultural_and_cognitive_roots": "Originates from the Spring and Autumn Period (春秋五霸): powerful dukes who subdued all other feudal lords through formidable military alliances and supreme power.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by fourth tone: 'chēng bà' (55-51). Hold high pitch 55, then execute a sharp decisive fall to 51."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "秤", "pinyin": "chèng", "meaning_en": "steelyard balance", "distinction_note": "Has 平 on right of 禾 instead of 尔 in simplified 称"},
                {"character": "积", "pinyin": "jī", "meaning_en": "accumulate", "distinction_note": "Has 只 on right of 禾"},
                {"character": "霞", "pinyin": "xiá", "meaning_en": "sunset clouds", "distinction_note": "Has 叚 under rain 雨 instead of 䩗 in 霸"},
                {"character": "霜", "pinyin": "shuāng", "meaning_en": "frost", "distinction_note": "Has 相 under rain 雨"}
            ],
            "etymological_cognates": [
                {"character": "统", "pinyin": "tǒng", "gloss_en": "unify; govern"},
                {"character": "主", "pinyin": "zhǔ", "gloss_en": "master; lord"},
                {"character": "雄", "pinyin": "xióng", "gloss_en": "hero; powerful entity"},
                {"character": "王", "pinyin": "wáng", "gloss_en": "king; rule"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "称霸 emphasizes asserting overwhelming, undisputed hegemony or monopoly over rivals in an industry, market, or athletic arena.",
            "contrasts": [
                {"id": "1", "compared_word": "称霸 vs. 垄断", "pinyin": "lǒngduàn", "analysis": "垄断 is an economic legal term for market monopoly cornering supply/pricing, while 称霸 highlights triumphant supremacy, athletic reign, or military dominance."},
                {"id": "2", "compared_word": "称霸 vs. 领先", "pinyin": "lǐngxiān", "analysis": "领先 simply means being in the lead in score, speed, or tech ('技术领先'), without necessarily subjugating or overpowering all rivals."},
                {"id": "3", "compared_word": "称霸 vs. 称雄", "pinyin": "chēngxióng", "analysis": "称雄 is more literary and positive, praising heroic eminence and prowess, while 称霸 can carry overtones of aggressive overbearing hegemony."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在当今高科技半导体产业竞争中，没有任何一家跨国巨头能够凭借昔日的专利壁垒永远称霸市场。随着新兴经济体在先进制程与材料科学领域的全力追赶，全球芯片产业链正迎来前所未有的多元重构时代。",
                "pinyin": "Zài dāngjīn gāokējì bàndǎotǐ chǎnyè jìngzhēng zhōng, méiyǒu rènhé yī jiā kuàguó jùtóu nénggòu píngjiè xīrì de zhuānlì bìlěi yǒngyuǎn chēngbà shìchǎng. Suízhe xīnxīng jīngjìtǐ zài xiānjìn zhìchéng yǔ cáiliào kēxué lǐngyù de quánlì zhuīgǎn, quánqiú xīnpiàn chǎnyèliàn zhèng yínglái qiánsuǒwèiyǒu de duōyuán chónggòu shídài.",
                "en": "In semiconductor competition, no multinational giant can dominate the market forever relying on legacy patent barriers. As emerging economies catch up in advanced fabrication, the global chip chain enters a diverse era of restructuring.",
                "es": "En la pugna de semiconductores, ningún titán domina el mercado para siempre amparado en viejas patentes. Con economías emergentes recortando distancias en nanotecnología, la cadena de microchips se diversifica como nunca."
            },
            {
                "id": "#2",
                "hanzi": "中国女子乒乓球队在国际体坛长期称霸数十载，凭借的是科学严谨的选拔梯队、日复一日的高强度体能磨砺以及永不言败的坚韧斗志。面对世界各国顶尖高手的轮番冲击，女乒健儿始终临危不乱，用沉甸甸的金牌捍卫了王者荣耀。",
                "pinyin": "Zhōngguó nǚzǐ pīngpāngqiú duì zài guójì tǐtán chángqī chēngbà shùshí zǎi, píngjiè de shì kēxué yánjǐn de xuǎnbá tīduì, rìfùyīrì de gāoxiàngdù tǐnéng mólì yǐjí yǒngbùyánbài de jiānrèn dòuzhì. Miànduì shìjiè gè guó dǐngjiān gāoshǒu de lúnfān chōngjī, nǚpīng jiàn'ér shǐzhōng línwéi-búlùan, yòng chéndiāndiān de jīnpái hànwèile wángzhě róngyào.",
                "en": "The Chinese women's table tennis team has dominated international sports for decades, relying on scientific selection, grueling training, and an indomitable spirit. Facing global challengers, players remain calm, defending glory with gold medals.",
                "es": "El equipo femenino chino de tenis de mesa reina en el deporte mundial desde hace décadas gracias a su rigurosa cantera, disciplina espartana y espíritu indómito. Ante rivales internacionales, las jugadoras defienden su hegemonía con oro."
            }
        ]
    },

    # 22 背景
    {
        "id": "22",
        "hanzi": "背景",
        "pinyin": "bèi jǐng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "background; backdrop; context; social/family connections",
            "es": "fondo; telón de fondo; contexto; antecedentes personales; respaldo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the scenery or ground behind the main object in a picture, stage, or view; backdrop",
                "definition_es": "paisaje, decorado o parte posterior sobre la que destaca la figura principal de una pintura, foto o escenario",
                "example_phrase": "照片背景 (photo background)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the historical context, cultural milieu, or personal social connections underlying an event or individual",
                "definition_es": "contexto histórico, entorno cultural o antecedentes personales y familiares que rodean un hecho",
                "example_phrase": "时代背景 (historical background / context of the era)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在全球智能手机全面爆发的历史背景下，微信抓住了移动互联网转型浪潮，迅速完成了海外多语言布局。",
                "pinyin": "Zài quánqiú zhìnéng shǒujī quánmiàn bàofā de lìshǐ bèijǐng xià, Wēixìn zhuāzhùle yídòng hùliánwǎng zhuǎnxíng làngcháo, xùnsù wánchéngle hǎiwài duōyǔyán bùjú.",
                "en": "Against the historical backdrop of global smartphone explosion, WeChat seized the mobile internet transition wave, quickly completing its multilingual overseas layout.",
                "es": "Con el auge de los móviles como telón de fondo, WeChat aprovechó la ola digital completando con presteza su despliegue multilingüe internacional."
            },
            {
                "id": "#2",
                "hanzi": "在面试新员工时，企业管理者不仅看重应聘者的学术教育背景，更关注其在跨文化团队中的协作沟通能力。",
                "pinyin": "Zài miànshì xīn yuángōng shí, qǐyè guǎnlǐzhě bùjǐn kànzhòng yìngpìnzhě de xuéshù jiàoyù bèijǐng, gèng guānzhù qí zài kuàwénhuà tuánduì zhōng de xiézuò gōutōng nénglì.",
                "en": "When interviewing new recruits, managers value not only candidates' academic education background, but even more their communication skills in multicultural teams.",
                "es": "Al entrevistar a candidatos, los directivos valoran su formación académica, pero priorizan su capacidad de comunicación en equipos multiculturales."
            }
        ],
        "collocations": [
            {"hanzi": "时代背景", "en": "background of the era; zeitgeist context"},
            {"hanzi": "教育背景", "en": "educational background"},
            {"hanzi": "历史背景", "en": "historical background"},
            {"hanzi": "文化背景", "en": "cultural background"},
            {"hanzi": "背景音乐", "en": "background music (BGM)"},
            {"hanzi": "家庭背景", "en": "family background"}
        ],
        "idioms": [
            {"hanzi": "烘云托月", "pinyin": "hōng yún tuō yuè", "meaning_en": "paint clouds to set off the moon; provide effective background contrast"},
            {"hanzi": "源远流长", "pinyin": "yuán yuǎn liú cháng", "meaning_en": "dating back to a distant past and enduring across time"},
            {"hanzi": "错综复杂", "pinyin": "cuò zōng fù zá", "meaning_en": "intricate, complex, and tangled in context"},
            {"hanzi": "追本溯源", "pinyin": "zhuī běn sù yuán", "meaning_en": "trace back to the primordial source or root context"}
        ],
        "character_decomposition": [
            {
                "character": "背",
                "pinyin": "bèi",
                "meaning_en": "back of body; behind; turn away; memorize",
                "meaning_es": "espalda; detrás; dar la espalda; memorizar",
                "radical": "月",
                "radical_meaning_en": "flesh",
                "meaning_component": "北 (two persons standing back to back) + 月/肉 (flesh / dorsal human body)",
                "sound_component": "北 (běi, north / phonetic nuance bèi)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two people standing back to back 北 over flesh 月; represents the dorsal back of the human torso or rear side of objects.",
                "visual_mnemonic_story_en": "Two figures turning back to back (北) reveal the dorsal spine of the human body (月) as the back (背).",
                "visual_mnemonic_story_es": "Dos figuras dándose la espalda (北) revelan la espina dorsal del cuerpo (月) marcando la espalda (背).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LPB",
                "traditional": ""
            },
            {
                "character": "景",
                "pinyin": "jǐng",
                "meaning_en": "scenery; view; landscape; situation",
                "meaning_es": "paisaje; vista; decorado; situación; panorama",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun / daylight illumination) + 京 (tall imperial city watchtower)",
                "sound_component": "京 (jīng, capital / phonetic jǐng)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Sunlight 日 illuminating a high imperial pavilion tower 京; radiant scenery, vista, spectacle, and backdrop setting.",
                "visual_mnemonic_story_en": "Bright sunshine (日) illuminating a towering capital pavilion (京) creates a scenic panorama (景).",
                "visual_mnemonic_story_es": "La luz del sol (日) iluminando una torre monumental (京) compone un panorama escénico (景).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "AYRF",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The scenic panorama (景) resting quietly at the rear back (背) of the main subject constitutes the background (背景).",
            "composite_memory_hook_es": "El decorado escénico (景) que descansa detrás en la parte trasera (背) conforma el fondo o contexto (背景).",
            "cultural_and_cognitive_roots": "Derived from classical theatrical staging: scenery panels hung behind (背) the acting stage to evoke historical place and mood (景).",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by third tone: 'bèi jǐng' (51-214). Sharp initial fall dropping into a full low-dip third tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "肯", "pinyin": "kěn", "meaning_en": "willing; agree", "distinction_note": "Has 止 at top over 月 instead of 北 in 背"},
                {"character": "胄", "pinyin": "zhòu", "meaning_en": "helmet; descendant", "distinction_note": "Has 由 over 月"},
                {"character": "影", "pinyin": "yǐng", "meaning_en": "shadow; film", "distinction_note": "Has hair/pattern radical 彡 on right of 景"},
                {"character": "晾", "pinyin": "liàng", "meaning_en": "air-dry in sun", "distinction_note": "Has 日 on left of 京 instead of on top in 景"}
            ],
            "etymological_cognates": [
                {"character": "底", "pinyin": "dǐ", "gloss_en": "bottom; base"},
                {"character": "后", "pinyin": "hòu", "gloss_en": "back; rear"},
                {"character": "境", "pinyin": "jìng", "gloss_en": "milieu; border"},
                {"character": "象", "pinyin": "xiàng", "gloss_en": "image; phenomenon"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "背景 encompasses the physical backdrop of visual imagery, as well as the historical, socioeconomic context or personal pedigree.",
            "contrasts": [
                {"id": "1", "compared_word": "背景 vs. 环境", "pinyin": "huánjìng", "analysis": "环境 refers to surrounding physical ecological conditions or social atmosphere ('生活环境', '生态环境'), whereas 背景 focuses on underlying historical backdrop or pedigree."},
                {"id": "2", "compared_word": "背景 vs. 情景", "pinyin": "qíngjǐng", "analysis": "情景 describes a specific dynamic scene or dramatic tableau unfolding before one's eyes ('感人的情景'), while 背景 is the static context behind it."},
                {"id": "3", "compared_word": "背景 vs. 幕后", "pinyin": "mùhòu", "analysis": "幕后 refers to behind-the-scenes confidential operations or unseen backstage masterminds ('幕后推手'), whereas 背景 is contextual setting."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "理解一部伟大的文学经典，离不开对其创作时代背景的深入考证。作家笔下栩栩如生的人物命运与悲欢离合，无不深深镌刻着特定历史时期的政治风云与社会思想烙印，展现出时代精神对个人灵魂的塑造力量。",
                "pinyin": "Lǐjiě yī bù wěidà de wénxué jīngdiǎn, líbùkāi duì qí chuàngzuò shídài bèijǐng de shēnrù kǎozhèng. Zuòjiā bǐxià xǔxǔ-rúshēng de rénwù mìngyùn yǔ bēihuān-líhé, wúbù shēndēn juānkè zhe tèdìng lìshǐ shíqī de zhèngzhì fēngyún yǔ shèhuì sīxiǎng làoyìn, zhǎnxiàn chū shídài jīngshén duì gèrén línghún de shùzào lìliang.",
                "en": "Understanding a literary classic is inseparable from exploring its historical context. The vivid destinies and sorrows depicted by an author are deeply stamped with political winds and social thought, showing how eras mold human souls.",
                "es": "Comprender un clásico literario exige ahondar en el contexto de su época. Los destinos humanos plasmados por el autor llevan la impronta de las corrientes políticas de su tiempo, reflejando cómo la historia forja el alma."
            },
            {
                "id": "#2",
                "hanzi": "在经济全球化与数字化转型的宏大背景下，不同文化背景的跨国科研人员汇聚在同一个云端协同平台。大家虽然母语与习俗各异，但凭借对真理的共同执着追求，成功打破了文化偏见与思维藩篱，开创了国际学术合作的新典范。",
                "pinyin": "Zài jīngjì quánqiúhuà yǔ shùzìhuà zhuǎnxíng de hóngdà bèijǐng xià, bùtóng wénhuà bèijǐng de kuàguó kēyán rényuán huìjù zài tóng yī gè yúnduān xiétóng píngtái. Dàjiā suīrán mǔyǔ yǔ xísú gèyì, dàn píngjiè duì zhēnlǐ de gòngtóng zhízhuó zhuīqiú, chénggōng dǎpòle wénhuà piānjiàn yǔ sīwéi fānlí, kāichuàngle guójì xuéshù hézuò de xīn diǎnfàn.",
                "en": "Against the backdrop of globalization and digital transition, researchers from diverse cultural backgrounds unite on cloud platforms. Despite different tongues, their shared pursuit of truth breaks cultural prejudices, forging a paradigm of cooperation.",
                "es": "Con la globalización y la digitalización de fondo, científicos de diversos orígenes culturales coinciden en plataformas en la nube. Pese a hablar distintas lenguas, su amor a la ciencia derriba prejuicios creando un modelo de cooperación."
            }
        ]
    },

    # 23 高级
    {
        "id": "23",
        "hanzi": "高级",
        "pinyin": "gāo jí",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "high-ranking; senior; high-grade; advanced; premium",
            "es": "de alto rango; superior; avanzado; de alta gama; distinguido; prémium"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "ranking high in hierarchy, status, professional seniority, or technological advancement",
                "definition_es": "situado en un nivel jerárquico superior, de categoría avanzada o gran maestría profesional",
                "example_phrase": "高级工程师 (senior engineer)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "luxurious, high-grade, premium quality, or tasteful",
                "definition_es": "de primera calidad, lujoso, refinado o de gama alta",
                "example_phrase": "高级餐厅 (high-end / fine-dining restaurant)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "腾讯集团委派多位资深高级副总裁亲自负责海外业务拓展，彰显出企业对国际化战略的高度重视。",
                "pinyin": "Téngxùn jítuán wěipài duō wèi zīshēn gāojí fù-zǒngcái qīnzì fùzé hǎiwài yèwù tuòzhǎn, zhāngxiǎn chū qǐyè duì guójìhuà zhànlüè de gāodù zhòngshì.",
                "en": "Tencent appointed several senior vice presidents to personally oversee overseas expansion, underscoring the firm's profound commitment to globalization.",
                "es": "Tencent designó a varios vicepresidentes sénior para liderar la expansión exterior, demostrando su firme compromiso con la internacionalización."
            },
            {
                "id": "#2",
                "hanzi": "这家高科技研发中心汇聚了数十位高级算法专家，致力于攻克新一代量子计算核心理论难题。",
                "pinyin": "Zhè jiā gāokējì yánfā zhōngxīn huìjùle shùshí wèi gāojí suànfǎ zhuānjiā, zhìlì yú gōngkè xīn yí dài liàngzǐ jìsuàn héxīn lǐlùn nántí.",
                "en": "This high-tech R&D center gathers dozens of senior algorithm experts dedicated to cracking core theoretical bottlenecks in next-gen quantum computing.",
                "es": "Este centro de I+D reúne a decenas de expertos en algoritmos avanzados consagrados a resolver dilemas en computación cuántica."
            }
        ],
        "collocations": [
            {"hanzi": "高级官员", "en": "senior official; high-ranking official"},
            {"hanzi": "高级副总裁", "en": "Senior Vice President (SVP)"},
            {"hanzi": "高级职称", "en": "senior professional title"},
            {"hanzi": "高级餐厅", "en": "high-end / fine-dining restaurant"},
            {"hanzi": "高级阶段", "en": "advanced stage"},
            {"hanzi": "高级定制", "en": "haute couture; premium customization"}
        ],
        "idioms": [
            {"hanzi": "高瞻远瞩", "pinyin": "gāo zhān yuǎn zhǔ", "meaning_en": "stand high and see far; possess visionary foresight"},
            {"hanzi": "高屋建瓴", "pinyin": "gāo wū jiàn líng", "meaning_en": "pour water from rooftop; operate from a vantage point of commanding height"},
            {"hanzi": "步步高升", "pinyin": "bù bù gāo shēng", "meaning_en": "rise step by step in official ranking; steady promotion"},
            {"hanzi": "高朋满座", "pinyin": "gāo péng mǎn zuò", "meaning_en": "hall filled with distinguished and eminent guests"}
        ],
        "character_decomposition": [
            {
                "character": "高",
                "pinyin": "gāo",
                "meaning_en": "tall; high; elevated; lofty; superior",
                "meaning_es": "alto; elevado; noble; superior; eminente",
                "radical": "高",
                "radical_meaning_en": "tall / high",
                "meaning_component": "Pictograph of a multi-tiered wooden watchtower or city gate pavilion rising into the sky",
                "sound_component": "Pictograph of high tower gāo",
                "stroke_count": 10,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of a soaring multi-story gate tower with an arched entrance 口, rooftop 亠, and viewing chamber; denotes height and superiority.",
                "visual_mnemonic_story_en": "A multi-tiered majestic imperial watchtower rises tall and lofty into the clouds (高).",
                "visual_mnemonic_story_es": "Una atalaya imperial de varios pisos que se alza majestuosa hacia las nubes (高).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YRBR",
                "traditional": ""
            },
            {
                "character": "级",
                "pinyin": "jí",
                "meaning_en": "level; grade; rank; step; degree",
                "meaning_es": "nivel; grado; peldaño; rango; escalón",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (graded silk threads arranged in ordered sequence) + 及 (reach / attain)",
                "sound_component": "及 (jí, reach / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk fibers 纟 arranged sequentially according to quality until each grade reaches 及 its proper standard; steps, ranks, and degrees.",
                "visual_mnemonic_story_en": "Strands of silk (纟) reaching up step by step (及) climb to the next higher rank (级).",
                "visual_mnemonic_story_es": "Madejas de seda (纟) que alcanzan (及) un peldaño superior en la escala de categorías (级).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "VMNE",
                "traditional": "級"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Standing at the loftiest tower heights (高) on the highest hierarchical step (级) is advanced or senior-ranking (高级).",
            "composite_memory_hook_es": "Situarse en la torre más alta (高) sobre el peldaño supremo de la jerarquía (级) es de alto rango o avanzado (高级).",
            "cultural_and_cognitive_roots": "Derived from bureaucratic rank examinations in imperial China: ascending nine official grades (九品中正制) toward senior court rank (高级官员).",
            "tone_sandhi_and_pitch_modulation": "First tone followed by second tone: 'gāo jí' (55-35). Hold high ceiling 55, then glide up cleanly to 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "亮", "pinyin": "liàng", "meaning_en": "bright; shine", "distinction_note": "Has 几 at bottom instead of 口 in 高"},
                {"character": "亭", "pinyin": "tíng", "meaning_en": "pavilion", "distinction_note": "Has 丁 at bottom"},
                {"character": "极", "pinyin": "jí", "meaning_en": "extreme; pole", "distinction_note": "Has wood radical 木 on left of 及 instead of silk 纟 in 级"},
                {"character": "吸", "pinyin": "xī", "meaning_en": "inhale; suck", "distinction_note": "Has mouth radical 口 on left of 及"}
            ],
            "etymological_cognates": [
                {"character": "上", "pinyin": "shàng", "gloss_en": "upper; superior"},
                {"character": "尊", "pinyin": "zūn", "gloss_en": "venerable; senior"},
                {"character": "贵", "pinyin": "guì", "gloss_en": "noble; premium"},
                {"character": "超", "pinyin": "chāo", "gloss_en": "super; surpass"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "高级 indicates high rank in an organization, advanced technological maturity, or premium/luxurious consumer tier.",
            "contrasts": [
                {"id": "1", "compared_word": "高级 vs. 高等", "pinyin": "gāoděng", "analysis": "高等 applies strictly to advanced education or biological taxonomy ('高等教育', '高等动物'), while 高级 applies to personnel rank, tech maturity, and quality."},
                {"id": "2", "compared_word": "高级 vs. 高档", "pinyin": "gāodàng", "analysis": "高档 specifically refers to consumer commodities, apparel, or furnishings that are expensive and high-grade ('高档商品'), whereas 高级 can describe abstract theories, ranks, and jobs."},
                {"id": "3", "compared_word": "高级 vs. 顶级", "pinyin": "dǐngjí", "analysis": "顶级 denotes the very pinnacle apex or tier-one best in the entire world ('顶级配置'), surpassing regular 高级."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "现代跨国企业在选拔高级管理人才时，越来越看重候选人的战略大局观与危机应变能力。一位称职的高级主管不仅要在顺境中带领团队开疆拓土，更要在行业遭遇严冬时临危不乱，以远见卓识为企业开辟出全新的增长空间。",
                "pinyin": "Xiàndài kuàguó qǐyè zài xuǎnbá gāojí guǎnlǐ réncái shí, yuèláiyuè kànzhòng hòuxuǎnrén de zhànlüè dàjúguān yǔ wēijī yìngbiàn nénglì. Yī wèi chènzhí de gāojí zhǔguǎn bùjǐn yào zài shùnjìng zhōng dàilǐng tuánduì kāijiāng-tuòtǔ, gèng yào zài hángyè zāoyù yándōng shí línwéi-búlùan, yǐ yuǎnjiàn-zhuóshí wèi qǐyè kāipì chū quánxīn de zēngzhǎng kōngjiān.",
                "en": "Multinationals increasingly value vision and crisis response when selecting senior executives. A competent senior director not only expands business during good times, but stays calm during industry downturns, charting fresh growth avenues.",
                "es": "Las multinacionales valoran la visión estratégica y la gestión de crisis al elegir directivos sénior. Un alto ejecutivo competente no solo expande el negocio en tiempos de bonanza, sino que mantiene el temple en recesiones abriendo nuevos horizontes."
            },
            {
                "id": "#2",
                "hanzi": "随着我国综合国力与居民生活水平的持续提升，消费市场呈现出从基础物质满足向高级精神享受转变的鲜明趋势。越来越多的消费者愿意为高级文化定制旅游、高雅艺术展演以及高品质有机健康食品买单，催生出多元蓬勃的品质消费新蓝海。",
                "pinyin": "Suízhe wǒguó zōnghé guólì yǔ jūmín shēnghuó shuǐpíng de chíxù tíshēng, xiāofèi shìchǎng chéngxiàn chū cóng jīchǔ wùzhí mǎnzú xiàng gāojí jīngshén xiǎngshòu zhuǎnbiàn de xiānmíng qūshì. Yuèláiyuè duō de xiāofèizhě yuànyì wèi gāojí wénhuà dìngzhì lǚyóu, gāoyǎ yìshù zhǎnyǎn yǐjí gāopǐnzhì yǒujī jiànkāng shípǐn mǎidān, cuīshēng chū duōyuán péngbó de pǐnzhì xiāofèi xīn lánhǎi.",
                "en": "With rising living standards, the consumer market is shifting from basic material needs toward higher spiritual enjoyment. Consumers readily pay for premium customized travel, fine arts, and organic health foods, spurring vibrant quality markets.",
                "es": "Con la mejora del nivel de vida, el consumo evoluciona de cubrir necesidades básicas hacia el disfrute cultural refinado. Crece la demanda de viajes exclusivos, arte selecto y alimentos ecológicos prémium, impulsando un mercado de gran calidad."
            }
        ]
    },

    # 24 副
    {
        "id": "24",
        "hanzi": "副",
        "pinyin": "fù",
        "part_of_speech": "Adjective / Measure Word",
        "meanings_summary": {
            "en": "vice-; deputy; secondary; classifier for sets/pairs (glasses, gloves, expressions)",
            "es": "vice-; adjunto; segundo; clasificador para juegos, pares o expresiones (gafas, guantes, cara)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "occupying a secondary, assisting, or deputy rank beneath a chief or principal officer",
                "definition_es": "que ocupa un rango subalterno o de auxilio inmediato respecto al cargo titular principal",
                "example_phrase": "副总裁 (vice president)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Measure Word",
                "register": "Standard",
                "definition_en": "classifier for things in pairs or sets (glasses, gloves), or facial expressions and attitudes",
                "definition_es": "clasificador para objetos que van en pares o juegos (gafas, guantes), o para expresiones del semblante",
                "example_phrase": "一副眼镜 (a pair of glasses)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这位刚刚晋升的高级副总裁在新闻发布会上宣布，微信海外用户注册量已突破一亿大关。",
                "pinyin": "Zhè wèi gānggāng jìnshēng de gāojí fù-zǒngcái zài xīnwén fābùhuì shàng xuānbù, Wēixìn hǎiwài yònghù zhùcèliàng yǐ tūpò yī yì dàguān.",
                "en": "This newly promoted senior vice president announced at the press conference that overseas registered WeChat users had surpassed the 100 million mark.",
                "es": "El recién ascendido vicepresidente sénior anunció en rueda de prensa que los usuarios de WeChat en el extranjero superaron la barrera de cien millones."
            },
            {
                "id": "#2",
                "hanzi": "他戴上一副深黑色的太阳镜，脸上挂着一副自信从容的微笑，大步流星地走上国际讲台。",
                "pinyin": "Tā dàishàng yī fù shēnhēisè de tàiyángjìng, liǎn shàng guàzhe yī fù zìxìn cóngróng de wēixiào, dàbù-liúxīng de zǒushàng guójì jiǎngtái.",
                "en": "Wearing a pair of dark sunglasses and sporting a confident, calm smile, he strode vigorously onto the international podium.",
                "es": "Poniéndose unas gafas de sol oscuras y luciendo una sonrisa serena y segura, subió con paso firme al estrado internacional."
            }
        ],
        "collocations": [
            {"hanzi": "副总裁", "en": "Vice President (VP)"},
            {"hanzi": "副总理", "en": "Vice Premier / Deputy Prime Minister"},
            {"hanzi": "一副眼镜", "en": "a pair of glasses"},
            {"hanzi": "一副手套", "en": "a pair of gloves"},
            {"hanzi": "副作用", "en": "side effect"},
            {"hanzi": "副业", "en": "sideline production / moonlighting occupation"}
        ],
        "idioms": [
            {"hanzi": "名副其实", "pinyin": "míng fù qí shí", "meaning_en": "worthy of the name; name matches reality"},
            {"hanzi": "全副武装", "pinyin": "quán fù wǔ zhuāng", "meaning_en": "fully armed from head to toe; fully equipped"},
            {"hanzi": "盛气凌人", "pinyin": "shèng qì líng rén", "meaning_en": "put on overbearing arrogant airs"},
            {"hanzi": "严阵以待", "pinyin": "yán zhèn yǐ dài", "meaning_en": "stand in tight battle array awaiting enemy"}
        ],
        "character_decomposition": [
            {
                "character": "副",
                "pinyin": "fù",
                "meaning_en": "vice; deputy; assist; divide; classifier for sets",
                "meaning_es": "vice; adjunto; secundario; dividir; clasificador de juegos o pares",
                "radical": "刂",
                "radical_meaning_en": "knife",
                "meaning_component": "畐 (full clay jar / abundance) + 刂 (knife dividing into matching halves)",
                "sound_component": "畐 (fú, jar / phonetic nuance fù)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Using a knife 刂 to split a full sacrificial vessel 畐 into two complementary halves; signifies a secondary matching duplicate or deputy.",
                "visual_mnemonic_story_en": "A sharp knife (刂) neatly dividing a full vessel (畐) into matching auxiliary sets creates a deputy copy (副).",
                "visual_mnemonic_story_es": "Una cuchilla afilada (刂) que divide una tinaja llena (畐) en mitades complementarias crea un duplicado adjunto (副).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MTLN",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Dividing a full jar in half with a blade (刂) produces an auxiliary counterpart (副) ready to assist the principal.",
            "composite_memory_hook_es": "Dividir una tinaja colmada con el cuchillo (刂) rinde una mitad auxiliar (副) que complementa al titular.",
            "cultural_and_cognitive_roots": "Originates from ancient imperial ritual tallies (契约剖半): jade or bronze tallies cut in two, with the sovereign holding the master and the deputy general holding the auxiliary tally (副符).",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'fù' (51). Crisp, authoritative falling drop."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "福", "pinyin": "fú", "meaning_en": "fortune; blessing", "distinction_note": "Has altar radical 礻 on left instead of knife 刂 on right in 副"},
                {"character": "幅", "pinyin": "fú", "meaning_en": "width; classifier for paintings", "distinction_note": "Has cloth radical 巾 on left of 畐"},
                {"character": "富", "pinyin": "fù", "meaning_en": "rich; wealthy", "distinction_note": "Has roof radical 宀 on top of 畐"},
                {"character": "逼", "pinyin": "bī", "meaning_en": "force; compel", "distinction_note": "Has walk radical 辶 on outside of 畐"}
            ],
            "etymological_cognates": [
                {"character": "佐", "pinyin": "zuǒ", "gloss_en": "assist; auxiliary officer"},
                {"character": "助", "pinyin": "zhù", "gloss_en": "help; assist"},
                {"character": "配", "pinyin": "pèi", "gloss_en": "match; subordinate mate"},
                {"character": "套", "pinyin": "tào", "gloss_en": "set; suit"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "副 serves as an adjective prefix for deputy/assistant roles, or as a measure word for paired items (glasses, gloves) and facial expressions.",
            "contrasts": [
                {"id": "1", "compared_word": "副 vs. 正", "pinyin": "zhèng", "analysis": "正 is the direct antonym meaning principal, chief, or head officer ('正局长' vs. '副局长')."},
                {"id": "2", "compared_word": "副 vs. 双", "pinyin": "shuāng", "analysis": "双 is a measure word for symmetric natural body pairs like shoes, socks, hands, and eyes ('一双鞋'), while 副 applies to composite sets like glasses, gloves, playing cards ('一副扑克牌', '一副手套')."},
                {"id": "3", "compared_word": "副 vs. 套", "pinyin": "tào", "analysis": "套 classifies complete multi-piece suites, furniture sets, apartments, or series of suits ('一套西装', '一套房子'), while 副 is for smaller accessories or expressions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代企业高管团队中，副职干部承担着承上启下与统筹协调的关键中枢职责。优秀的副总裁善于精准领会董事长的宏观战略意图，并在分管的具体业务领域雷厉风行地抓好执行落实，成为协助一把手决策的得力助手。",
                "pinyin": "Zài xiàndài qǐyè gāoguǎn tuánduì zhōng, fùzhí gànbù chéngdān zhe chéngshàng-qǐxià yǔ tǒngchóu xiétiáo de guānjiàn zhōngshū zhízé. Yōuxiù de fù-zǒngcái shànyú jīngzhǔn lǐnghuì dǒngshìzhǎng de hóngguān zhànlüè yìtú, bìng zài fēnguǎn de jùtǐ yèwù lǐngyù léilì-fēngxíng de zhuāhǎo zhíxíng luòshí, chéngwéi xiézhù yībǎshǒu juécè de délì zhùshǒu.",
                "en": "In modern corporate executive teams, deputy leaders shoulder the vital hub duty of bridging top strategy and execution. An exceptional VP accurately grasps the chairman's vision and vigorously executes within their division as a trusted right hand.",
                "es": "En la cúpula corporativa, los directivos adjuntos asumen la crucial labor de enlace y coordinación. Un vicepresidente brillante interpreta la visión de la presidencia y la ejecuta con dinamismo en su división como mano derecha indispensable."
            },
            {
                "id": "#2",
                "hanzi": "寒冬腊月里的北方乡村，集市上摆满了红彤彤的对联与窗花。老书法家铺展红纸、饱蘸浓墨，挥毫为赶集的乡邻书写出一副副寓意吉祥喜庆的新春对联。红纸黑字映衬着老百姓一张张幸福的笑脸，勾勒出浓郁淳厚的年味图景。",
                "pinyin": "Hándōng-làyuè lǐ de běifāng xiāngcūn, jíshì shàng bǎimǎnle hóngtōngtōng de duìlián yǔ chuānghuā. Lǎo shūfǎjiā pūzhǎn hóngzhǐ, bǎozhàn nóngmò, huīháo wèi gǎnjí de xiānglín shūxiě chū yī fù fù yùyì jíxiáng xǐqìng de xīnchūn duìlián. Hóngzhǐ hēizì yìngchèn zhe lǎobǎixìng yī zhāng zhāng xìngfú de xiàoliǎn, gōulè chū nóngyù chúnhòu de niánwèi tújǐng.",
                "en": "In deep winter northern villages, rural markets brim with crimson couplets and paper-cuttings. Veteran calligraphers dip brushes into rich ink, penning pairs of auspicious New Year couplets for villagers, framing joy and warm festive cheer.",
                "es": "En pleno rigor invernal en el norte rural, los mercados rebosan de coplas y recortables escarlata. Calígrafos veteranos empapan sus pinceles en tinta china componiendo pares de pareados festivos que enmarcan las sonrisas de los aldeanos."
            }
        ]
    },

    # 25 开发
    {
        "id": "25",
        "hanzi": "开发",
        "pinyin": "kāi fā",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to develop; exploit; open up (resources, software, products, markets)",
            "es": "desarrollar; explotar; poner en valor; programar; abrir (recursos, software, mercados)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to systematically research, engineer, and build software programs, technologies, or industrial products",
                "definition_es": "investigar, programar y construir sistemáticamente software, productos o patentes tecnológicas",
                "example_phrase": "开发新软件 (develop new software)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to open up, exploit, and put natural resources, tourist attractions, or virgin land into productive economic use",
                "definition_es": "abrir, explotar o poner en valor productivo yacimientos naturales, parajes turísticos o tierras yermas",
                "example_phrase": "开发新能源 (develop new energy sources)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "腾讯广州研发团队仅用不到三个月时间，就成功开发出了微信最初的第一代即时通讯核心版本。",
                "pinyin": "Téngxùn Guǎngzhōu yánfā tuánduì jǐn yòng búdào sān gè yuè shíjiān, jiù chénggōng kāifā chūle Wēixìn zuìchū de dì-yī dài jíshí tōngxùn héxīn bǎnběn.",
                "en": "In less than three months, Tencent's Guangzhou R&D team successfully developed WeChat's very first generation instant messaging core version.",
                "es": "En menos de tres meses, el equipo de I+D de Tencent en Cantón desarrolló con éxito la primera versión de mensajería instantánea de WeChat."
            },
            {
                "id": "#2",
                "hanzi": "为了摆脱对化石燃料的严重依赖，沿海各省正大力投资开发海上风电与潮汐发电等清洁海洋资源。",
                "pinyin": "Wèile bǎituō duì huàshí ránliào de yánzhòng yīlài, yánhǎi gè shěng zhèng dàlì tóuzī kāifā hǎishàng fēngdiàn yǔ cháoxī fādiàn děng qīngjié hǎiyáng zīyuán.",
                "en": "To break heavy reliance on fossil fuels, coastal provinces are heavily investing to develop clean marine resources like offshore wind and tidal power.",
                "es": "Para dejar atrás la dependencia de combustibles fósiles, las provincias litorales invierten con fuerza en desarrollar energía eólica marina y mareomotriz."
            }
        ],
        "collocations": [
            {"hanzi": "软件开发", "en": "software development"},
            {"hanzi": "产品开发", "en": "product development"},
            {"hanzi": "开发资源", "en": "develop / exploit resources"},
            {"hanzi": "自主开发", "en": "independent / in-house development"},
            {"hanzi": "开发市场", "en": "develop / open up a market"},
            {"hanzi": "开发区", "en": "development zone (economic/tech)"}
        ],
        "idioms": [
            {"hanzi": "开天辟地", "pinyin": "kāi tiān pì dì", "meaning_en": "split heaven and earth apart; epoch-making creation"},
            {"hanzi": "开疆拓土", "pinyin": "kāi jiāng tuò tǔ", "meaning_en": "open up borders and expand territorial frontiers"},
            {"hanzi": "大显身手", "pinyin": "dà xiǎn shēn shǒu", "meaning_en": "fully display one's prowess and capabilities"},
            {"hanzi": "发家致富", "pinyin": "fā jiā zhì fù", "meaning_en": "build up family fortune and achieve prosperity"}
        ],
        "character_decomposition": [
            {
                "character": "开",
                "pinyin": "kāi",
                "meaning_en": "open; unlock; commence; operate",
                "meaning_es": "abrir; descerrajar; iniciar; operar",
                "radical": "廾",
                "radical_meaning_en": "two hands",
                "meaning_component": "Two hands 廾 lifting off the gate crossbar 一 to open up an entrance",
                "sound_component": "Historical phonetic nuance in 開",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Two hands removing a locking bar to throw open gates; extended to initiating, pioneering, and unlocking new potential.",
                "visual_mnemonic_story_en": "Two hands lifting away a barrier bar throw open wide gates to new frontiers (开).",
                "visual_mnemonic_story_es": "Dos manos apartan la traba para abrir de par en par los portales de lo nuevo (开).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MT",
                "traditional": "開"
            },
            {
                "character": "发",
                "pinyin": "fā",
                "meaning_en": "shoot arrow; emit; launch; develop; prosper",
                "meaning_es": "disparar flecha; emitir; lanzar; desarrollarse; prosperar",
                "radical": "又",
                "radical_meaning_en": "hand / again",
                "meaning_component": "A hand shooting an arrow from a drawn bow; simplified from 發",
                "sound_component": "Historical phonetic nuance in 發",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Releasing an arrow from an archer's bowstring; setting into powerful forward flight, launching, expanding, and developing.",
                "visual_mnemonic_story_en": "An arrow shot from a bowstring surges forward with unstoppable momentum (发).",
                "visual_mnemonic_story_es": "Una flecha disparada desde el arco que se proyecta con fuerza incontenible (发).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "IVE",
                "traditional": "發"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Throwing open new gates (开) and releasing productive forces into forward flight (发) is development (开发).",
            "composite_memory_hook_es": "Abrir nuevos caminos (开) y lanzar con fuerza el potencial creador (发) es desarrollar o explotar (开发).",
            "cultural_and_cognitive_roots": "Derived from classical frontier statecraft (辟土开发): clearing wilderness and opening mines to enrich the national treasury and people's livelihood.",
            "tone_sandhi_and_pitch_modulation": "Two high level first tones: 'kāi fā' (55-55). Maintain steady, clear high melodic level throughout."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "升", "pinyin": "shēng", "meaning_en": "rise; liter", "distinction_note": "Has slanted top-left drop, unlike 开"},
                {"character": "井", "pinyin": "jǐng", "meaning_en": "water well", "distinction_note": "Has two vertical parallel strokes crossing two horizontals"},
                {"character": "伐", "pinyin": "fá", "meaning_en": "cut down; fell trees", "distinction_note": "Has person radical 亻 on left of halberd 戈, unlike 发"},
                {"character": "拨", "pinyin": "bō", "meaning_en": "dial; push aside", "distinction_note": "Has hand radical 扌 on left of 发"}
            ],
            "etymological_cognates": [
                {"character": "研", "pinyin": "yán", "gloss_en": "grind; research"},
                {"character": "制", "pinyin": "zhì", "gloss_en": "manufacture; make"},
                {"character": "拓", "pinyin": "tuò", "gloss_en": "expand; pioneer"},
                {"character": "掘", "pinyin": "jué", "gloss_en": "dig; unearth"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "开发 emphasizes systematically building software, uncovering natural resources, or opening new commercial markets from scratch.",
            "contrasts": [
                {"id": "1", "compared_word": "开发 vs. 发展", "pinyin": "fāzhǎn", "analysis": "发展 is an intransitive or broad noun/verb describing natural or economic growth, expansion, and maturation ('经济发展'), while 开发 is active human engineering/exploitation."},
                {"id": "2", "compared_word": "开发 vs. 研制", "pinyin": "yánzhì", "analysis": "研制 emphasizes trial laboratory scientific synthesis and prototype manufacturing ('研制新药', '研制火箭'), while 开发 encompasses commercial software and resources."},
                {"id": "3", "compared_word": "开发 vs. 开辟", "pinyin": "kāipì", "analysis": "开辟 focuses on physically cutting a new path or symbolically inaugurating a new historical era ('开辟新航线', '开辟新纪元')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在人工智能革命汹涌澎湃的浪潮中，软件开发工程师的角色正经历着深刻的重构。过去繁重冗长的基础代码编写工作正逐步被大语言模型接管，开发者能够将更多心力聚焦于顶层架构设计与底层算法的突破性创新。",
                "pinyin": "Zài réngōng zhìnéng gémìng xiōngyǒng-péngpài de làngcháo zhōng, ruǎnjiàn kāifā gōngchéngshī de juésè zhèng jīnglì zhe shēnchén de chónggòu. Guòqù fánzhòng rǒngcháng de jīchǔ dàimǎ biānxiě gōngzuò zhèng zhúbù bèi dàyǔyán móxíng jiēguǎn, kāifāzhě nénggòu jiāng gèngduō xīnlì jùjiāo yú dǐngcéng jiàgòu shèjì yǔ dǐcéng suànfǎ de tūpòxìng chuàngxīn.",
                "en": "Amid the surging AI revolution, the role of software engineers is undergoing profound reconstruction. Tedious coding is increasingly assumed by large language models, letting developers focus on top-level architecture and algorithmic breakthroughs.",
                "es": "En plena revolución de la inteligencia artificial, el rol del programador se reinventa a fondo. La tediosa escritura de código básico recae en grandes modelos lingüísticos, permitiendo a los creadores centrarse en la arquitectura del sistema."
            },
            {
                "id": "#2",
                "hanzi": "合理开发利用自然资源是实现经济社会可持续发展的必然要求。在推进矿产与水利资源开发的同时，必须坚持生态保护红线不动摇，严格落实水土保持与环境修复治理，绝不能以牺牲绿水青山为代价换取短期的经济收益。",
                "pinyin": "Hélǐ kāifā lìyòng zìrán zīyuán shì shíxiàn jīngjì shèhuì kěchíxù fāzhǎn de bìrán yāoqiú. Zài tuījìn kuàngchǎn yǔ shuǐlì zīyuán kāifā de tóngshí, bìxū jiānchí shēngtài bǎohù hóngxiàn bù dòngyáo, yángé luòshí shuǐtǔ bǎochí yǔ huánjìng xiūfù zhìlǐ, juébù néng yǐ xīshēng lǜshuǐ-qīngshān wéi dàijià huànqǔ duǎnqī de jīngjì shōuyì.",
                "en": "Rational exploitation of natural resources is mandatory for sustainable development. While tapping minerals and hydropower, red lines for ecological protection must remain unswerving, never trading pristine waters and green mountains for short-term gain.",
                "es": "La explotación racional de los recursos naturales es indispensable para el desarrollo sostenible. Al aprovechar yacimientos y saltos de agua, deben blindarse los ecosistemas sin sacrificar jamás la naturaleza por ganancias efímeras."
            }
        ]
    },

    # 26 中心
    {
        "id": "26",
        "hanzi": "中心",
        "pinyin": "zhōng xīn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "center; heart; core; hub; institution/facility (research center, sports center)",
            "es": "centro; núcleo; corazón; eje neurálgico; sede o complejo institucional"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the middle point or central part of an area, geometry, or city; the core or heart of an activity",
                "definition_es": "punto central o parte neurálgica de un espacio, ciudad o asunto",
                "example_phrase": "市中心 (city center / downtown)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an organization, agency, or physical facility dedicated to a specific operational or research mission",
                "definition_es": "organismo, entidad o instalación destinada a una actividad especializada",
                "example_phrase": "研发中心 (R&D center)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了贴近海外用户的真实使用习惯，腾讯在海外多个大都市设立了本地化技术支持与运营中心。",
                "pinyin": "Wèile tiējìn hǎiwài yònghù de zhēnshí shǐyòng xíguàn, Téngxùn zài hǎiwài duō gè dàdūshì shèlìle běndìhuà jìshù zhīchí yǔ yùnyíng zhōngxīn.",
                "en": "To stay close to overseas users' authentic usage habits, Tencent established local tech support and operations centers across major foreign metropolises.",
                "es": "Para ajustarse a los hábitos de los usuarios extranjeros, Tencent abrió centros de soporte técnico y operaciones en varias metrópolis mundiales."
            },
            {
                "id": "#2",
                "hanzi": "繁华的国际金融中心不仅汇聚了全球顶尖的跨国银行，更掌握着庞大资本在全球范围内的配置方向。",
                "pinyin": "Fánhuá de guójì jīnróng zhōngxīn bùjǐn huìjùle quánqiú dǐngjiān de kuàguó yínháng, gèng zhǎngwò zhe pángdà zīběn zài quánqiú fànwéi nèi de pèizhì fāngxiàng.",
                "en": "The bustling international financial center not only gathers the world's top multinational banks, but steers the global allocation of massive capital.",
                "es": "El floreciente centro financiero internacional reúne a los mayores bancos mundiales y pilota la distribución de ingentes capitales por el globo."
            }
        ],
        "collocations": [
            {"hanzi": "研发中心", "en": "R&D center"},
            {"hanzi": "市中心", "en": "city center / downtown"},
            {"hanzi": "数据中心", "en": "data center"},
            {"hanzi": "金融中心", "en": "financial center"},
            {"hanzi": "中心任务", "en": "central task / primary mission"},
            {"hanzi": "购物中心", "en": "shopping center / mall"}
        ],
        "idioms": [
            {"hanzi": "正中下怀", "pinyin": "zhèng zhòng xià huái", "meaning_en": "fit in exactly with one's wishes; just what one hoped for"},
            {"hanzi": "万人空巷", "pinyin": "wàn rén kōng xiàng", "meaning_en": "thousands empty out streets to flock to a central event"},
            {"hanzi": "独具匠心", "pinyin": "dú jù jiàng xīn", "meaning_en": "possessing ingenious core craftsmanship and original mind"},
            {"hanzi": "众望所归", "pinyin": "zhòng wàng suǒ guī", "meaning_en": "central pivot of all people's hopes; universally acclaimed"}
        ],
        "character_decomposition": [
            {
                "character": "中",
                "pinyin": "zhōng",
                "meaning_en": "middle; center; within; inside; hit",
                "meaning_es": "medio; centro; interior; acertar; dentro",
                "radical": "丨",
                "radical_meaning_en": "vertical line",
                "meaning_component": "A flagpole with banners 口 planted precisely in the geometric center with a vertical staff 丨",
                "sound_component": "Self-phonetic zhōng",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A ceremonial banner pole planted squarely in the middle of a military camp; represents the exact center and golden mean.",
                "visual_mnemonic_story_en": "A vertical staff (丨) planted squarely in the center box (口) marks the exact bullseye middle (中).",
                "visual_mnemonic_story_es": "Un asta vertical (丨) clavada justo en el medio del recuadro (口) marca el centro exacto (中).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "L",
                "traditional": ""
            },
            {
                "character": "心",
                "pinyin": "xīn",
                "meaning_en": "heart; mind; core; feeling; spirit",
                "meaning_es": "corazón; mente; núcleo; sentimiento",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "Pictograph of the human physical heart with chambers and aorta valves",
                "sound_component": "Pictograph of heart xīn",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of the muscular human heart showing ventricle chambers; regarded in traditional thought as the seat of thought and vital core.",
                "visual_mnemonic_story_en": "The curved muscular chamber of the human heart (心) pulsates as the vital core of life.",
                "visual_mnemonic_story_es": "La cavidad muscular del corazón humano (心) que late como motor vital de la existencia.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "P",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The exact geometric middle (中) joined with the beating life core (心) forms the true heart and center (中心).",
            "composite_memory_hook_es": "El centro geométrico exacto (中) unido al corazón vital palpitante (心) conforma el núcleo o centro (中心).",
            "cultural_and_cognitive_roots": "Derived from the ancient cosmology of the Central Plain (中原) and the human heart as the supreme ruler (心者，君主之官) in Chinese traditional medicine.",
            "tone_sandhi_and_pitch_modulation": "Two high level first tones: 'zhōng xīn' (55-55). Hold clear, sustained high level 55 pitch across both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "申", "pinyin": "shēn", "meaning_en": "express; state", "distinction_note": "Vertical stroke crosses top and bottom, unlike 中 which enters bottom"},
                {"character": "巾", "pinyin": "jīn", "meaning_en": "cloth; towel", "distinction_note": "Has downward left slant flap"},
                {"character": "必", "pinyin": "bì", "meaning_en": "must; surely", "distinction_note": "Has a long slash stroke crossing right through 心"},
                {"character": "沁", "pinyin": "qìn", "meaning_en": "soak; percolate", "distinction_note": "Has water radical 氵 on left of 心"}
            ],
            "etymological_cognates": [
                {"character": "核", "pinyin": "hé", "gloss_en": "core; nucleus"},
                {"character": "枢", "pinyin": "shū", "gloss_en": "pivot; hub"},
                {"character": "基", "pinyin": "jī", "gloss_en": "base; foundation"},
                {"character": "央", "pinyin": "yāng", "gloss_en": "center; middle"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "中心 designates the geometric core, downtown hub, or specialized organizational facility (data center, research center).",
            "contrasts": [
                {"id": "1", "compared_word": "中心 vs. 核心", "pinyin": "héxīn", "analysis": "核心 emphasizes the indispensable essence, crucial nucleus, or key deciding element ('核心竞争力', '核心技术'), while 中心 can be purely spatial or institutional."},
                {"id": "2", "compared_word": "中心 vs. 中间", "pinyin": "zhōngjiān", "analysis": "中间 simply refers to physical relative position between two extremes or temporal intervals ('坐在两人中间'), while 中心 is a focal hub."},
                {"id": "3", "compared_word": "中心 vs. 枢纽", "pinyin": "shūniǔ", "analysis": "枢纽 emphasizes traffic or network interconnection switching (e.g. 交通枢纽 transport hub), whereas 中心 focuses on attraction and aggregation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在超大型现代化城市规划中，多中心组团式布局正逐步取代传统的单中心扩张模式。通过在城市外围副中心高标准配套优质教育、医疗资源与综合交通枢纽，有效缓解了主城区的交通拥堵，实现了城市功能的均衡布局。",
                "pinyin": "Zài chāodàxíng xiàndàihuà chéngshì guīhuà zhōng, duōzhōngxīn zǔtuánshì bùjú zhèng zhúbù qǔdài chuántǒng de dānzhōngxīn kuòzhāng móshì. Tōngguò zài chéngshì wàiwéi fùzhōngxīn gāobiāozhǔn pèitào yōuzhì jiàoyù, yīliáo zīyuán yǔ zōnghé jiāotōng shūniǔ, yǒuxiào huǎnjiěle zhǔchéngqū de jiāotōng yōngdǔ, shíxiànle chéngshì gōngnéng de jīnhéng bùjú.",
                "en": "In megacity planning, polycentric clustered layouts are replacing monocentric sprawl. Equipping sub-centers with quality schools, healthcare, and transit hubs eases downtown congestion, achieving balanced urban functionality.",
                "es": "En el urbanismo de grandes urbes, los esquemas policéntricos relevan la concentración en un solo núcleo. Dotar a centros periféricos de colegios, hospitales y nudos de transporte descongestiona el centro histórico equilibrando la ciudad."
            },
            {
                "id": "#2",
                "hanzi": "国家超级计算中心作为支撑战略高科技前沿探索的核心大科学装置，在天气预报精细模拟、深空探测轨道计算以及新药分子动力学筛选等领域发挥着中流砥柱的作用。源源不断的澎湃算力，成为推动国家创新驱动发展的强大引擎。",
                "pinyin": "Guójiā chāojí jìsuàn zhōngxīn zuòwéi zhīchēng zhànlüè gāokējì qiányán tànsuǒ de héxīn dàkēxué zhuāngzhì, zài tiānqì yùbào jīngxì mónǐ, shēnkōng tàncè guǐdào jìsuàn yǐjí xīnyào fēnzǐ dònglìxué shāixuǎn děng lǐngyù fāhuī zhe zhōngliú-dǐzhù de zuòyòng. Yuányuán-bùduàn de péngbài suànlì, chéngwéi tuīdòng guójiā chuàngxīn qūdòng fāzhǎn de qiángdà yǐnqíng.",
                "en": "As a large-scale facility supporting frontier tech, the National Supercomputing Center anchors fine weather modeling, deep space orbit plotting, and drug discovery. Continuous computational power acts as an engine driving innovation.",
                "es": "El Centro Nacional de Supercomputación, como gran infraestructura de ciencia de frontera, es un pilar en predicción meteorológica, cálculo aeroespacial y diseño de fármacos. Su inagotable potencia de cómputo propulsa el desarrollo."
            }
        ]
    },

    # 27 相关
    {
        "id": "27",
        "hanzi": "相关",
        "pinyin": "xiāng guān",
        "part_of_speech": "Adjective / Verb",
        "meanings_summary": {
            "en": "related; relevant; correlated; pertinent; to be interrelated",
            "es": "relacionado; pertinente; correspondiente; correlativo; vincularse"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "having a mutual connection, correlation, or logical relevance to a topic or event",
                "definition_es": "que guarda conexión, afinidad lógica o relación de interdependencia con otro asunto",
                "example_phrase": "相关政策 (relevant policies)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Formal",
                "definition_en": "to be interrelated or linked with one another in cause, effect, or operation",
                "definition_es": "estar mutuamente vinculado o guardar estrecha relación causal o funcional",
                "example_phrase": "息息相关 (closely bound together; vitally interrelated)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在进入海外不同国家市场前，企业合规团队必须细致研读当地与数据跨境传输相关的法律法规。",
                "pinyin": "Zài jìnrù hǎiwài bùtóng guójiā shìchǎng qián, qǐyè hégūi tuánduì bìxū xìzhì yándú dāngdì yǔ shùjù kuàjìng chuánshū xiāngguān de fǎlǜ fǎguī.",
                "en": "Before entering diverse overseas markets, the corporate compliance team must meticulously study local laws and regulations related to cross-border data transfer.",
                "es": "Antes de desembarcar en mercados extranjeros, el departamento legal examina con rigor las leyes locales relativas a la transferencia de datos."
            },
            {
                "id": "#2",
                "hanzi": "现代医学流行病学调查证实，日常长期高糖高盐的饮食结构与心血管慢性疾病的诱发高度相关。",
                "pinyin": "Xiàndài yīxué liúxíngbìngxué diàochá zhèngshí, rìcháng chángqī gāotáng gāoyán de yǐnshí jiégòu yǔ xīnxuěguǎn mànxìng jíbìng de yòufā gāodù xiāngguān.",
                "en": "Epidemiological studies confirm that long-term daily diets high in sugar and salt are highly correlated with the onset of chronic cardiovascular diseases.",
                "es": "Estudios epidemiológicos demuestran que las dietas ricas en azúcares y sal están sumamente correlacionadas con dolencias cardiovasculares crónicas."
            }
        ],
        "collocations": [
            {"hanzi": "相关部门", "en": "relevant departments / authorities"},
            {"hanzi": "相关政策", "en": "pertinent policies"},
            {"hanzi": "密切相关", "en": "closely related / intimately correlated"},
            {"hanzi": "相关法律", "en": "relevant laws"},
            {"hanzi": "息息相关", "en": "closely linked; bound together"},
            {"hanzi": "相关数据", "en": "relevant data / correlated figures"}
        ],
        "idioms": [
            {"hanzi": "息息相关", "pinyin": "xī xī xiāng guān", "meaning_en": "as closely interrelated as breath to life; inextricably linked"},
            {"hanzi": "休戚相关", "pinyin": "xiū qī xiāng guān", "meaning_en": "bound up together in mutual weal and woe"},
            {"hanzi": "相辅相成", "pinyin": "xiāng fǔ xiāng chéng", "meaning_en": "supplement and complement each other"},
            {"hanzi": "声气相通", "pinyin": "shēng qì xiāng tōng", "meaning_en": "in close harmony and mutual sympathy"}
        ],
        "character_decomposition": [
            {
                "character": "相",
                "pinyin": "xiāng",
                "meaning_en": "each other; mutual; look at; appearance",
                "meaning_es": "mutuo; recíproco; mirar; aspecto",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "木 (tree branch) + 目 (human eye closely observing tree)",
                "sound_component": "Self-phonetic xiāng",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An eye 目 gazing thoughtfully at a tree 木 to inspect its quality; extended to mutual reciprocal inspection and interrelationship.",
                "visual_mnemonic_story_en": "An eye (目) looking thoughtfully at a tree (木) reflects reciprocal interaction (相).",
                "visual_mnemonic_story_es": "Un ojo vigilante (目) que examina la madera del árbol (木) observando de forma recíproca (相).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DB",
                "traditional": ""
            },
            {
                "character": "关",
                "pinyin": "guān",
                "meaning_en": "frontier pass; close; shut; connect; concern",
                "meaning_es": "paso fronterizo; cerrar; trancar; conectar; concernir",
                "radical": "丷",
                "radical_meaning_en": "eight / disperse",
                "meaning_component": "Double crossbars barring an imperial mountain pass gate; simplified from 關",
                "sound_component": "Historical phonetic nuance in 關",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A mountain pass checkpoint with locked wooden gates; passing through the barrier connects regions and concerns vital safety.",
                "visual_mnemonic_story_en": "Passing through the barred boundary gate marks the crucial checkpoint connection (关).",
                "visual_mnemonic_story_es": "Franquear la barrera del paso fortificado conecta valles y concierne a la seguridad (关).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YTK",
                "traditional": "關"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Interacting mutually with one another (相) across the crucial connection barrier (关) establishes relevance and correlation (相关).",
            "composite_memory_hook_es": "Interactuar de forma recíproca (相) enlazados a través de un paso común (关) define lo pertinente o correlativo (相关).",
            "cultural_and_cognitive_roots": "Ancient philosophical notion of resonance (天人感应): events in human affairs and nature are invisibly interconnected through resonant gates (相关关联).",
            "tone_sandhi_and_pitch_modulation": "Two high level first tones: 'xiāng guān' (55-55). Hold clear, sustained high level pitch throughout."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "想", "pinyin": "xiǎng", "meaning_en": "think; miss", "distinction_note": "Has heart radical 心 at bottom under 相"},
                {"character": "箱", "pinyin": "xiāng", "meaning_en": "box; chest", "distinction_note": "Has bamboo radical 竹 on top of 相"},
                {"character": "美", "pinyin": "měi", "meaning_en": "beautiful", "distinction_note": "Has 羊 at top over 大 instead of 丷 in 关"},
                {"character": "天", "pinyin": "tiān", "meaning_en": "sky; day", "distinction_note": "Lacks the top two dots of 关"}
            ],
            "etymological_cognates": [
                {"character": "联", "pinyin": "lián", "gloss_en": "connect; link"},
                {"character": "系", "pinyin": "xì", "gloss_en": "tie; system; relation"},
                {"character": "连", "pinyin": "lián", "gloss_en": "link; continuous"},
                {"character": "牵", "pinyin": "qiān", "gloss_en": "pull; involve"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "相关 functions as an adjective prefix for pertinent/connected subjects or statistical correlation.",
            "contrasts": [
                {"id": "1", "compared_word": "相关 vs. 有关", "pinyin": "yǒuguān", "analysis": "有关 often introduces a prepositional phrase ('有关环境保护的报告' report concerning environmental protection), whereas 相关 frequently functions directly as an adjective modifier ('相关文件' relevant documents) or statistical term ('正相关')."},
                {"id": "2", "compared_word": "相关 vs. 相连", "pinyin": "xiānglián", "analysis": "相连 denotes direct spatial or physical contiguous contact ('山水相连'), whereas 相关 indicates logical, causal, or statistical linkage."},
                {"id": "3", "compared_word": "相关 vs. 相应", "pinyin": "xiāngyìng", "analysis": "相应 means corresponding, matching, or commensurate in proportion/countermeasure ('采取相应措施'), while 相关 merely denotes connection."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代大数据与人工智能分析领域，“相关性并不等同于因果性”是一条至关重要的统计学准则。两个经济变量之间存在高度相关，可能仅仅是因为它们同时受到某个未被观测到的深层第三方因素驱动，需要科学家严谨辨析。",
                "pinyin": "Zài xiàndài dàshùjù yǔ réngōng zhìnéng fēnxī lǐngyù, 'xiāngguānxìng bìng bù děngtóng yú yīnguǒxìng' shì yī tiáo zhìguān zhòngyào de tǒngjìxué zhǔnzé. Liǎng gè jīngjì biànliàng zhījiān cúnzài gāodù xiāngguān, kěnéng jǐnjǐn shì yīnwèi tāmen tóngshí shòudào mǒu gè wèibèi guāncè dào de shēncéng dì-sān fāng yīnsù qūdòng, xūyào kēxuéjiā yánjǐn biànxī.",
                "en": "In big data and AI analysis, 'correlation does not imply causation' is a crucial axiom. High correlation between two economic variables may stem from an unobserved third factor, requiring rigorous scientific differentiation.",
                "es": "En la analítica de macrodatos e IA, 'correlación no implica causalidad' es una máxima crucial. Dos variables correlacionadas pueden responder a un tercer factor oculto, requiriendo un riguroso discernimiento científico."
            },
            {
                "id": "#2",
                "hanzi": "生态系统的健康稳定与每一种珍稀物种的生存繁衍息息相关。科学家通过长期生态监测发现，森林中顶级掠食者数量的骤降，会直接引发食草动物过度繁殖并破坏植被，最终导致整片森林水土流失加剧，破坏生物多样性。",
                "pinyin": "Shēngtài xìtǒng de jiànkāng wěndìng yǔ měi yī zhǒng zhēnxī wùzhǒng de shēngcún fányǎn xīxī-xiāngguān. Kēxuéjiā tōngguò chángqī shēngtài jiāncè fāxiàn, sēnlín zhōng dǐngjí lüèshízhě shùliàng de zhòujiàng, huì zhíjiē yǐnfā shícǎo dòngwù guòdù fánzhí bìng pòhuài zhíbèi, zuìzhōng dǎozhì zhěng piàn sēnlín shuǐtǔ liúshī jiājù, pòhuài shēngwù duōyàngxìng.",
                "en": "Ecosystem stability is closely related to the survival of rare species. Long-term monitoring shows that a sudden drop in apex predators causes herbivores to overpopulate and degrade flora, ultimately exacerbating erosion and harming biodiversity.",
                "es": "La salud del ecosistema está íntimamente ligada a la supervivencia de especies raras. El declive de grandes depredadores dispara la sobrepoblación de herbívoros dañando la flora y desatando la erosión del suelo forestal."
            }
        ]
    },

    # 28 业务
    {
        "id": "28",
        "hanzi": "业务",
        "pinyin": "yè wù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "business; professional work; commercial operations; service transactions",
            "es": "negocio; operaciones comerciales; actividad profesional; gestiones o servicios"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the specialized operations, commercial transactions, or professional services conducted by an enterprise or institution",
                "definition_es": "operaciones comerciales, cartera de servicios o actividad técnica propia de una empresa o entidad",
                "example_phrase": "拓展海外业务 (expand overseas business)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "随着海外用户数量的急剧攀升，微信迅速设立了专门负责跨国支付与企业级云服务的海外业务部。",
                "pinyin": "Suízhe hǎiwài yònghù shùliàng de jíjù pānshēng, Wēixìn xùnsù shèlìle zhuānmén fùzé kuàguó zhīfù yǔ qǐyèjí yún fúwù de hǎiwài yèwùbù.",
                "en": "With the sharp surge in overseas users, WeChat quickly established an overseas business department dedicated to cross-border payments and enterprise cloud services.",
                "es": "Ante el fuerte incremento de usuarios en el extranjero, WeChat creó un departamento internacional dedicado a pagos transfronterizos y servicios en la nube."
            },
            {
                "id": "#2",
                "hanzi": "银行大厅里增设了多台智能化自助服务终端，使市民办理个人储蓄与转账业务的时间缩短了一大半。",
                "pinyin": "Yínháng dàtīng lǐ zēngshèle duō tái zhìnénghuà zìzhù fúwù zhōngduān, shǐ shìmín bànlǐ gèrén chǔxù yǔ zhuǎnzhàng yèwù de shíjiān suōduǎnle yí dàbàn.",
                "en": "Additional smart self-service kiosks were installed in the bank lobby, cutting the time citizens spend on personal savings and transfer transactions by more than half.",
                "es": "Se instalaron cajeros inteligentes en el vestíbulo del banco reduciendo a más de la mitad el tiempo para gestionar depósitos y transferencias."
            }
        ],
        "collocations": [
            {"hanzi": "开展业务", "en": "conduct / carry out business"},
            {"hanzi": "业务范围", "en": "scope of business"},
            {"hanzi": "业务能力", "en": "professional competence / operational skill"},
            {"hanzi": "海外业务", "en": "overseas business operations"},
            {"hanzi": "核心业务", "en": "core business"},
            {"hanzi": "办理业务", "en": "transact business / handle service matters"}
        ],
        "idioms": [
            {"hanzi": "业精于勤", "pinyin": "yè jīng yú qín", "meaning_en": "mastery in one's profession thrives on diligence"},
            {"hanzi": "恪尽职守", "pinyin": "kè jìn zhí shǒu", "meaning_en": "scrupulously abide by one's professional duty"},
            {"hanzi": "精益求精", "pinyin": "jīng yì qiú jīng", "meaning_en": "constantly refine skills and pursue professional perfection"},
            {"hanzi": "蒸蒸日上", "pinyin": "zhēng zhēng rì shàng", "meaning_en": "business flourishing and prospering day by day"}
        ],
        "character_decomposition": [
            {
                "character": "业",
                "pinyin": "yè",
                "meaning_en": "profession; business; industry; undertaking; karma",
                "meaning_es": "oficio; profesión; negocio; industria; patrimonio",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "A sturdy carved frame used to hang ceremonial bells and drums in ancient rituals",
                "sound_component": "Archaic phonetic yè",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Carved notched stand supporting grand ritual musical instruments; extended to lifelong business pursuits and professional vocations.",
                "visual_mnemonic_story_en": "A majestic framed stand for ritual instruments represents lifelong professional enterprise (业).",
                "visual_mnemonic_story_es": "Un sólido atril para instrumentos rituales que encarna el patrimonio y la vocación profesional (业).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TC",
                "traditional": "業"
            },
            {
                "character": "务",
                "pinyin": "wù",
                "meaning_en": "affair; business; be engaged in; duty",
                "meaning_es": "asunto; tarea; deber; dedicarse a; ocupación",
                "radical": "力",
                "radical_meaning_en": "power / strength",
                "meaning_component": "攴/攵 (hand holding whip/tool to guide) + 力 (physical strength/exertion)",
                "sound_component": "Archaic phonetic nuance in 務",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Exerting physical strength 力 with hands driven to complete assigned tasks; denotes duties, tasks, and commercial affairs.",
                "visual_mnemonic_story_en": "Directing physical strength (力) onto essential chores completes assigned duties (务).",
                "visual_mnemonic_story_es": "Aplicar esfuerzo y fuerza física (力) para cumplir con esmero los deberes encomendados (务).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EHK",
                "traditional": "務"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Applying diligent strength to assigned tasks (务) within one's professional vocation (业) drives commercial business (业务).",
            "composite_memory_hook_es": "Consagrar esfuerzo al cumplimiento del deber (务) en el ámbito del oficio o empresa (业) son las operaciones comerciales (业务).",
            "cultural_and_cognitive_roots": "From classical administrative maxims (勤于吏务): officials devoting constant energy (力) to state affairs without neglecting economic craft (治业).",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'yè wù' (51-51). Pronounce both syllables with firm, crisp falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "亚", "pinyin": "yà", "meaning_en": "Asia; second", "distinction_note": "Has two horizontal bars enclosing center, unlike vertical strokes of 业"},
                {"character": "严", "pinyin": "yán", "meaning_en": "strict; severe", "distinction_note": "Has top bars and slanted bottom stroke"},
                {"character": "条", "pinyin": "tiáo", "meaning_en": "strip; classifier", "distinction_note": "Has tree radical 木 at bottom instead of 力 in 务"},
                {"character": "冬", "pinyin": "dōng", "meaning_en": "winter", "distinction_note": "Has two dots at bottom instead of 力"}
            ],
            "etymological_cognates": [
                {"character": "职", "pinyin": "zhí", "gloss_en": "duty; office"},
                {"character": "事", "pinyin": "shì", "gloss_en": "matter; business"},
                {"character": "责", "pinyin": "zé", "gloss_en": "duty; responsibility"},
                {"character": "商", "pinyin": "shāng", "gloss_en": "trade; commerce"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "业务 specifically refers to concrete commercial operations, professional lines of service, or routine administrative procedures.",
            "contrasts": [
                {"id": "1", "compared_word": "业务 vs. 职业", "pinyin": "zhíyè", "analysis": "职业 denotes a person's broad career, trade, or occupation (e.g. teacher, lawyer), while 业务 refers to the concrete operational work or commercial transactions conducted."},
                {"id": "2", "compared_word": "业务 vs. 事务", "pinyin": "shìwù", "analysis": "事务 refers to routine clerical, administrative, or housekeeping affairs ('日常事务'), while 业务 emphasizes specialized commercial services or professional functions."},
                {"id": "3", "compared_word": "业务 vs. 商业", "pinyin": "shāngyè", "analysis": "商业 is the macroeconomic concept of commerce and trade in society, whereas 业务 is a specific firm's line of operational service."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在数字化转型大潮中，商业银行纷纷重构核心业务流程。通过全面引入人工智能风控算法与人脸识别技术，不仅大幅压缩了中小微企业贷款审批的业务流转时间，更有效防范了金融欺诈风险，实现了业务创新与稳健运营的双赢。",
                "pinyin": "Zài shùzìhuà zhuǎnxíng dàcháo zhōng, shāngyè yínháng fēnfēn chónggòu héxīn yèwù liúchéng. Tōngguò quánmiàn yǐnrù réngōng zhìnéng fēngkòng suànfǎ yǔ rénliǎn shíbié jìshù, bùjǐn dàfú yāsuōle zhōng-xiǎo-wēi qǐyè dàikuǎn shěnpī de yèwù liúzhuǎn shíjiān, gèng yǒuxiào fángfànle jīnróng qīzhà fēngxiǎn, shíxiànle yèwù chuàngxīn yǔ wěnjiàn yùnyíng de shuāngyíng.",
                "en": "Amid digital transformation, commercial banks are restructuring core business processes. Introducing AI risk control and facial recognition shortens SME loan approval times and guards against fraud, achieving a win-win in innovation and stability.",
                "es": "En la digitalización bancaria, las entidades rediseñan sus operaciones clave. Incorporando control de riesgos por IA y reconocimiento facial, agilizan créditos a pymes y blindan fraudes, aunando innovación y seguridad financiera."
            },
            {
                "id": "#2",
                "hanzi": "一家高科技企业的持续生命力，取决于其能否在深耕主营核心业务的同时敏锐捕捉未来产业新赛道。科技巨头在巩固传统移动通信与广告业务盈利优势的基础上，果断布局智能云计算与大模型服务，为公司业务的长远稳健增长打下了坚实基础。",
                "pinyin": "Yī jiā gāokējì qǐyè de chíxù shēngmìnglì, qǔjué yú qí néngfǒu zài shēngēng zhǔyíng héxīn yèwù de tóngshí mǐnruì bǔzhuō wèilái chǎnyè xīn sàidào. Kējì jùtóu zài gǒnggù chuántǒng yídòng tōngxìn yǔ guǎnggào yèwù yínglì yōushì de jīchǔ shàng, guǒduàn bùjú zhìnéng yúnjìsuàn yǔ dàmóxíng fúwù, wèi gōngsī yèwù de chángyuǎn wěnjiàn zēngzhǎng dǎxiàle jiānshí jīchǔ.",
                "en": "A tech firm's vitality hinges on cultivating its core operations while capturing future industries. Solidifying mobile communications and advertising, tech giants boldly deploy cloud computing and LLM services, laying ground for long-term growth.",
                "es": "La vitalidad de una tecnológica radica en afianzar su actividad medular mientras explora nuevos nichos. Consolidando telecomunicaciones y publicidad, los gigantes apuestan por la computación en la nube para asegurar su crecimiento futuro."
            }
        ]
    },

    # 29 现实
    {
        "id": "29",
        "hanzi": "现实",
        "pinyin": "xiàn shí",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "reality; actual fact; realistic; practical; down-to-earth",
            "es": "realidad; hechos reales; realista; práctico; pragmático"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the state of things as they actually exist objectively, as opposed to idealistic, fictional, or imaginary notions",
                "definition_es": "el estado objetivo y tangible de las cosas tal como existen, frente a lo ilusorio o imaginario",
                "example_phrase": "面对现实 (face reality)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "conforming to actual situations; practical, sensible, and down-to-earth",
                "definition_es": "que se atiene a los hechos y circunstancias reales; práctico y realista",
                "example_phrase": "现实的想法 (a realistic / practical idea)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在规划海外市场扩张蓝图时，企业既要满怀抱负，也必须清醒面对各地文化习惯与法律准入差异的客观现实。",
                "pinyin": "Zài guīhuà hǎiwài shìchǎng kuòzhāng lántú shí, qǐyè jì yào mǎnhuái bàofù, yě bìxū qīngxǐng miànduì gèdì wénhuà xíguàn yǔ fǎlǜ zhǔnrù chāyì de kèguān xiànshí.",
                "en": "When planning an overseas expansion blueprint, enterprises must be ambitious yet soberly face the objective reality of cultural and legal regulatory differences across regions.",
                "es": "Al trazar planes de expansión exterior, las empresas deben albergar ambición pero asumir con lucidez la realidad de las diferencias culturales y legales."
            },
            {
                "id": "#2",
                "hanzi": "经过科学家数十年坚持不懈的攻关，当年科幻小说中描绘的无人驾驶汽车如今已经真正化作了现实。",
                "pinyin": "Jīngguò kēxuéjiā shùshí nián jiānchí-búxiè de gōngguān, dāngnián kēhuàn xiǎoshuō zhōng miáohuì de wúrén jiàshǐ qìchē rújīn yǐjīng zhēnzhèng huàzuòle xiànshí.",
                "en": "Through decades of unremitting efforts by scientists, the autonomous self-driving cars once depicted in science fiction novels have truly materialized into reality.",
                "es": "Tras decenios de tesonero empeño científico, los vehículos autónomos descritos antaño en relatos de ciencia ficción se han trocado en realidad palpable."
            }
        ],
        "collocations": [
            {"hanzi": "面对现实", "en": "face reality"},
            {"hanzi": "客观现实", "en": "objective reality"},
            {"hanzi": "变成现实", "en": "turn into reality; materialize"},
            {"hanzi": "脱离现实", "en": "divorced from reality; out of touch with facts"},
            {"hanzi": "现实意义", "en": "practical / realistic significance"},
            {"hanzi": "现实生活", "en": "real life"}
        ],
        "idioms": [
            {"hanzi": "实事求是", "pinyin": "shí shì qiú shì", "meaning_en": "seek truth from facts; realistic and pragmatic"},
            {"hanzi": "脚踏实地", "pinyin": "jiǎo tà shí dì", "meaning_en": "feet planted firmly on solid ground; earnest and down-to-earth"},
            {"hanzi": "空中楼阁", "pinyin": "kōng zhōng lóu gé", "meaning_en": "castles in the air; unrealistic fantasies"},
            {"hanzi": "梦想成真", "pinyin": "mèng xiǎng chéng zhēn", "meaning_en": "dreams come true; aspirations turn into reality"}
        ],
        "character_decomposition": [
            {
                "character": "现",
                "pinyin": "xiàn",
                "meaning_en": "appear; present; now; visible; manifest",
                "meaning_es": "aparecer; presente; ahora; visible; manifestar",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王/玉 (glistening jade jewel) + 见 (open eye seeing clearly)",
                "sound_component": "见 (jiàn, see / phonetic nuance xiàn)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A lustrous jade gem 王 uncovered and placed directly before one's eyes 见; present, visible, actual reality.",
                "visual_mnemonic_story_en": "A sparkling jade gem (王) brought out into the open to see (见) manifests in the present (现).",
                "visual_mnemonic_story_es": "Una gema de jade (王) expuesta ante los ojos de todos (见) se manifiesta en el presente (现).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MGBU",
                "traditional": "現"
            },
            {
                "character": "实",
                "pinyin": "shí",
                "meaning_en": "solid; real; true; fruit; substance",
                "meaning_es": "sólido; real; verdadero; fruto; sustancia",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (safe domestic house) + 头/贯 (abundant wealth and grain filling house)",
                "sound_component": "Historical phonetic nuance in 實",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A house 宀 packed full of solid tangible treasures and grain; indicates substance, factuality, and solid reality.",
                "visual_mnemonic_story_en": "A house (宀) filled to the roof with solid grain embodies tangible truth (实).",
                "visual_mnemonic_story_es": "Un hogar (宀) colmado de grano sólido y cosechas encarna la verdad palpable (实).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JYK",
                "traditional": "實"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Visible present facts (现) filled with solid tangible substance (实) constitute reality (现实).",
            "composite_memory_hook_es": "Lo que se manifiesta visible en el presente (现) respaldado por hechos sólidos (实) es la realidad (现实).",
            "cultural_and_cognitive_roots": "Philosophical concept contrasting the ethereal void (虚) with tangible actuality (实): grounding human endeavors in actual worldly conditions.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by second tone: 'xiàn shí' (51-35). Crisp falling 51 tone gliding immediately up to rising 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "观", "pinyin": "guān", "meaning_en": "view; watch", "distinction_note": "Has 又 on left of 见 instead of jade 王 in 现"},
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; compass", "distinction_note": "Has husband 夫 on left of 见"},
                {"character": "头", "pinyin": "tóu", "meaning_en": "head", "distinction_note": "Lacks the roof radical 宀 of 实"},
                {"character": "买", "pinyin": "mǎi", "meaning_en": "buy", "distinction_note": "Has 乛 on top instead of 宀"}
            ],
            "etymological_cognates": [
                {"character": "真", "pinyin": "zhēn", "gloss_en": "true; authentic"},
                {"character": "存", "pinyin": "cún", "gloss_en": "exist; survive"},
                {"character": "确", "pinyin": "què", "gloss_en": "solid; certain"},
                {"character": "在", "pinyin": "zài", "gloss_en": "exist; present"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "现实 denotes objective, tangible reality versus fiction, or describes an attitude of being pragmatic and realistic.",
            "contrasts": [
                {"id": "1", "compared_word": "现实 vs. 实际", "pinyin": "shíjì", "analysis": "实际 highlights practical operation or concrete down-to-earth action ('从实际出发'), while 现实 highlights objective reality versus imagination or ideals ('理想与现实')."},
                {"id": "2", "compared_word": "现实 vs. 真实", "pinyin": "zhēnshí", "analysis": "真实 emphasizes genuineness and truth versus falsehood/lies ('真实的故事', '真实情况'), while 现实 emphasizes objective existence."},
                {"id": "3", "compared_word": "现实 vs. 事实", "pinyin": "shìshí", "analysis": "事实 refers to specific individual historical facts or evidence already proven ('铁的事实'), whereas 现实 is the comprehensive present state of affairs."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "青年人在确立人生奋斗目标时，既需要仰望星空的远大理想，更离不开脚踏实地的现实态度。如果脱离社会发展规律与自身客观条件的现实基础，哪怕再宏伟壮丽的抱负，最终也只能沦为脱离大地的空中楼阁。",
                "pinyin": "Qīngniánrén zài quèlì rénshēng fèndòu mùbiāo shí, jì xūyào yǎngwàng xīngkōng de yuǎndà lǐxiǎng, gèng líbùkāi jiǎotà-shídì de xiànshí tàidù. Rúguǒ tuōlí shèhuì fāzhǎn guīlǜ yǔ zìshēn kèguān tiáojiàn de xiànshí jīchǔ, nǎpà zài hóngwěi zhuànglì de bàofù, zuìzhōng yě zhǐnéng lúnwéi tuōlí dàdì de kōngzhōng-lóugé.",
                "en": "When setting life goals, youth need lofty ideals looking up at the stars, but equally require a realistic attitude with feet on the ground. Divorced from objective social realities, even the grandest ambition becomes a castle in the air.",
                "es": "Al fijar metas vitales, los jóvenes deben aspirar a las estrellas sin despegar los pies del suelo con actitud realista. Desconectadas de las leyes sociales y la realidad objetiva, las mayores ambiciones se tornan castillos en el aire."
            },
            {
                "id": "#2",
                "hanzi": "现实主义文学艺术长盛不衰的生命力，在于创作者始终怀着深厚的人文关怀去凝视社会的真实百态。优秀的艺术家敢于直面复杂的现实矛盾，通过细腻传神的笔触勾勒出普通百姓的喜怒哀乐，引发跨越时代的强烈心灵共鸣。",
                "pinyin": "Xiànshízhǔyì wénxué yìshù chángshèng-bùshuāi de shēngmìnglì, zàiyú chuàngzuòzhě shǐzhōng huáizhe shēnhòu de rénwén guānhuái qù níngshì shèhuì de zhēnshí bǎitài. Yōuxiù de yìshùjiā gǎnyú zhímiàn fùzá de xiànshí máodùn, tōngguò xìnì chuánshén de bǐchù gōulè chū pǔtōng bǎixìng de xǐ-nù-āi-lè, yǐnfā kuàyuè shídài de qiángliè xīnlíng gòngmíng.",
                "en": "The enduring vitality of realist art lies in creators gazing at social reality with profound human care. Exceptional artists face complex contradictions, sketching ordinary people's sorrows and joys to evoke soul-stirring resonance across eras.",
                "es": "La perenne vigencia del arte realista emana de contemplar la sociedad con honda sensibilidad humana. Grandes creadores encaran contradicciones palpables retratando los anhelos del pueblo y conmoviendo a través del tiempo."
            }
        ]
    },

    # 30 个人
    {
        "id": "30",
        "hanzi": "个人",
        "pinyin": "gè rén",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "individual; personal; private; oneself",
            "es": "individuo; persona particular; personal; privado; particular"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a single distinct human being as contrasted with a collective group, society, or state",
                "definition_es": "el ser humano individual considerado en contraposición a la colectividad, grupo o Estado",
                "example_phrase": "个人利益 (individual interests)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "concerning or belonging to a single private person rather than the public or an organization",
                "definition_es": "propio o perteneciente a una persona determinada; privado o particular",
                "example_phrase": "个人隐私 (personal privacy)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在拓展海外市场的过程中，微信高度尊重并严格保护不同国家用户的个人隐私与数据安全。",
                "pinyin": "Zài tuòzhǎn hǎiwài shìchǎng de guòchéng zhōng, Wēixìn gāodù zūnzhòng bìng yángé bǎohù bùtóng guójiā yònghù de gèrén yǐnsī yǔ shùjù ānquán.",
                "en": "In expanding overseas markets, WeChat highly respects and strictly safeguards the personal privacy and data security of users across nations.",
                "es": "Al expandirse en ultramar, WeChat respeta escrupulosamente la privacidad personal y la seguridad de los datos de usuarios de todo el mundo."
            },
            {
                "id": "#2",
                "hanzi": "这篇学术论文中所阐述的政策建议仅代表学者的个人观点，并不代表其所在研究所的官方立场。",
                "pinyin": "Zhè piān xuéshù lùnwén zhōng suǒ chánshù de zhèngcè jiànyì jǐn dàibiǎo xuézhě de gèrén guāndiǎn, bìng bù dàibiǎo qí suǒzài yánjiūsuǒ de guānfāng lìchǎng.",
                "en": "The policy recommendations elaborated in this academic paper represent solely the scholar's personal views, not the official stance of the research institute.",
                "es": "Las propuestas formuladas en este artículo académico reflejan exclusivamente la opinión personal del autor, no la postura oficial de su instituto."
            }
        ],
        "collocations": [
            {"hanzi": "个人隐私", "en": "personal privacy"},
            {"hanzi": "个人所得税", "en": "individual income tax"},
            {"hanzi": "个人简历", "en": "personal resume / CV"},
            {"hanzi": "个人观点", "en": "personal viewpoint / individual opinion"},
            {"hanzi": "个人利益", "en": "individual / personal interest"},
            {"hanzi": "个人空间", "en": "personal space"}
        ],
        "idioms": [
            {"hanzi": "各抒己见", "pinyin": "gè shū jǐ jiàn", "meaning_en": "each expresses one's own personal opinion freely"},
            {"hanzi": "人人自危", "pinyin": "rén rén zì wēi", "meaning_en": "everyone feels personally insecure and endangered"},
            {"hanzi": "推己及人", "pinyin": "tuī jǐ jí rén", "meaning_en": "treat others by putting oneself in their personal shoes"},
            {"hanzi": "严于律己", "pinyin": "yán yú lǜ jǐ", "meaning_en": "be strict with oneself in personal conduct"}
        ],
        "character_decomposition": [
            {
                "character": "个",
                "pinyin": "gè",
                "meaning_en": "individual; piece; single; classifier",
                "meaning_es": "individual; pieza; unidad; clasificador general",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "人 (human person standing upright) + 丨 (single vertical bamboo slip / unit)",
                "sound_component": "Self-phonetic gè",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A single person 人 holding a single tally stick 丨; denotes a distinct individual unit or single item.",
                "visual_mnemonic_story_en": "A single person (人) holding one upright tally stick (丨) stands as one distinct individual (个).",
                "visual_mnemonic_story_es": "Una persona singular (人) con un listón vertical (丨) representa una unidad individual (个).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OL",
                "traditional": "個"
            },
            {
                "character": "人",
                "pinyin": "rén",
                "meaning_en": "person; human; people; mankind",
                "meaning_es": "persona; ser humano; gente; hombre",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "Pictograph of a human being standing erect on two walking legs",
                "sound_component": "Pictograph of human rén",
                "stroke_count": 2,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A profile pictograph of a human being standing upright with two legs supporting the torso; human being, individual, or people.",
                "visual_mnemonic_story_en": "A human standing tall on two walking legs walking upright in the world (人).",
                "visual_mnemonic_story_es": "Un ser humano que se alza y camina sobre dos piernas erguido en el mundo (人).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "O",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A single individual unit (个) of a human being (人) forms an individual or personal self (个人).",
            "composite_memory_hook_es": "La unidad singular (个) de un ser humano (人) constituye el individuo o lo personal (个人).",
            "cultural_and_cognitive_roots": "Contrasts with the Confucian collective concept of society (集体、家国): balancing the moral integrity of the individual (修身) with harmonious community.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by second tone: 'gè rén' (51-35). Crisp falling 51 gliding up to smooth rising 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "入", "pinyin": "rù", "meaning_en": "enter", "distinction_note": "Right stroke overlaps over left, opposite of 人"},
                {"character": "八", "pinyin": "bā", "meaning_en": "eight", "distinction_note": "Two strokes do not touch at top, leaving gap"},
                {"character": "大", "pinyin": "dà", "meaning_en": "big; large", "distinction_note": "Has horizontal bar 一 across 人"},
                {"character": "介", "pinyin": "jiè", "meaning_en": "introduce; between", "distinction_note": "Has two strokes inside 人"}
            ],
            "etymological_cognates": [
                {"character": "己", "pinyin": "jǐ", "gloss_en": "oneself; self"},
                {"character": "私", "pinyin": "sī", "gloss_en": "private; personal"},
                {"character": "自", "pinyin": "zì", "gloss_en": "self; from"},
                {"character": "独", "pinyin": "dú", "gloss_en": "solitary; alone"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "个人 highlights the single private human being in contrast to the collective, group, or state.",
            "contrasts": [
                {"id": "1", "compared_word": "个人 vs. 集体", "pinyin": "jítǐ", "analysis": "集体 is the direct antonym meaning collective group or organization, whereas 个人 is the individual entity."},
                {"id": "2", "compared_word": "个人 vs. 自己", "pinyin": "zìjǐ", "analysis": "自己 is a reflexive pronoun meaning oneself ('我自己' myself), while 个人 can be an adjective ('个人账户') or noun contrastive to society."},
                {"id": "3", "compared_word": "个人 vs. 私人", "pinyin": "sīrén", "analysis": "私人 strongly emphasizes non-public private ownership, secrecy, or personal confidentiality ('私人财产', '私人飞机'), while 个人 is a neutral demographic term."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代法治社会中，依法加强个人信息保护已成为维护公民合法权益的重中之重。随着人工智能与大数据技术的深度应用，必须严厉打击非法采集与贩卖个人数据的违法行径，切实为每一位公民筑牢个人数字安全屏障。",
                "pinyin": "Zài xiàndài fǎzhì shèhuì zhōng, yīfǎ jiāqiáng gèrén xìnxī bǎohù yǐ chéngwéi wéihù gōngmín héfǎ quányì de zhòngzhōngzhīzhòng. Suízhe réngōng zhìnéng yǔ dàshùjù jìshù de shēndù yìngyòng, bìxū yánlì dǎjī fēifǎ cǎijí yǔ fànmài gèrén shùjù de wéifǎ xíngjìng, qièshí wèi měi yī wèi gōngmín zhùláo gèrén shùzì ānquán píngzhàng.",
                "en": "In a modern rule-of-law society, protecting personal information under law has become a top priority. With deep AI and big data usage, illegal harvesting of personal data must be cracked down on to erect solid digital safety barriers for all.",
                "es": "En un Estado de derecho, blindar los datos personales es prioritario para salvaguardar derechos cívicos. Ante el uso de la IA, debe castigarse el tráfico de información privada afianzando un escudo digital para cada ciudadano."
            },
            {
                "id": "#2",
                "hanzi": "个人的成长成才从来不是孤立进行的，而是与国家的前途命运紧密相连。青年学者应当将个人的学术志趣主动融入解决国家重大科技难题的实践中去，在为社会大众创造福祉的宏伟事业中，实现个人崇高的人生理想与时代价值。",
                "pinyin": "Gèrén de chéngzhǎng chéngcái cónglái búshì gūlì jìnxíng de, érshì yǔ guójiā de qiántú mìngyùn jǐnmì xiānglián. Qīngnián xuézhě yīngdāng jiāng gèrén de xuéshù zhìqù zhǔdòng róngrù jiějué guójiā zhòngdà kējì nántí de shíjiàn zhōng qù, zài wèi shèhuì dàzhòng chuàngzào fúzhǐ de hóngwěi shìyè zhōng, shíxiàn gèrén chónggāo de rénshēng lǐxiǎng yǔ shídài jiàzhí.",
                "en": "Individual growth never unfolds in isolation, but is intimately intertwined with national destiny. Young scholars should weave personal interests into solving critical tech challenges, fulfilling ideals and values by creating social welfare.",
                "es": "El desarrollo individual jamás ocurre aislado, sino entrelazado con el destino colectivo. Los jóvenes investigadores deben volcar su vocación en solventar retos estratégicos realizando sus ideales al servicio del bien común."
            }
        ]
    }
]

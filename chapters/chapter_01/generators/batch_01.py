from core.toon_builder import save_word

words_batch1 = [
    # 01 细节
    {
        "id": "1",
        "hanzi": "细节",
        "pinyin": "xì jié",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "details; particulars; minor points",
            "es": "detalles; pormenores; minucias"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "details; minute aspects; particulars of an event or object",
                "definition_es": "detalles; aspectos minuciosos; pormenores de un hecho u objeto",
                "example_phrase": "注意细节 (pay attention to details)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老艺术家的画作细腻生动，连花瓣上的露珠这种细节都被表现得惟妙惟肖。",
                "pinyin": "Lǎo yìshùjiā de huàzuò xìnì shēngdòng, lián huābàn shàng de lùzhū zhè zhǒng xìjié dōu bèi biǎoxiàn de wéimiàowéixiào.",
                "en": "The veteran artist's paintings are exquisite and vivid; even such details as dew on petals are depicted to perfection.",
                "es": "Las pinturas del veterano artista son exquisitas y vivaces; incluso detalles como el rocío en los pétalos están plasmados a la perfección."
            },
            {
                "id": "#2",
                "hanzi": "在复杂的外交谈判中，代表团对协议文本的每一处细节都进行了反复推敲和严谨确认。",
                "pinyin": "Zài fùzá de wàijiāo tánpàn zhōng, dàibiǎotuán duì xiéyì wénběn de měi yí chù xìjié dōu jìnxíng le fǎnfù tuīqiāo hé yánjǐn quèrèn.",
                "en": "In complex diplomatic negotiations, the delegation repeatedly scrutinized and rigorously confirmed every detail of the agreement text.",
                "es": "En las complejas negociaciones diplomáticas, la delegación examinó minuciosamente y confirmó con rigor cada detalle del texto del acuerdo."
            }
        ],
        "collocations": [
            {"hanzi": "注意细节", "en": "pay attention to details"},
            {"hanzi": "忽略细节", "en": "overlook details"},
            {"hanzi": "具体细节", "en": "specific details"},
            {"hanzi": "技术细节", "en": "technical details"},
            {"hanzi": "细节决定成败", "en": "details determine success or failure"},
            {"hanzi": "丰富细节", "en": "enrich the details"}
        ],
        "idioms": [
            {"hanzi": "不拘小节", "pinyin": "bù jū xiǎo jié", "meaning_en": "not bother about trifles; not adhere strictly to trivial rules"},
            {"hanzi": "细水长流", "pinyin": "xì shuǐ cháng liú", "meaning_en": "a fine stream flows long; economize to ensure long-term sustainability"},
            {"hanzi": "节衣缩食", "pinyin": "jié yī suō shí", "meaning_en": "live frugally; practice strict economy in clothing and food"},
            {"hanzi": "明察秋毫", "pinyin": "míng chá qiū háo", "meaning_en": "perceive the finest detail; see clearly down to an autumn hair"}
        ],
        "character_decomposition": [
            {
                "character": "细",
                "pinyin": "xì",
                "meaning_en": "fine; thin; meticulous",
                "meaning_es": "fino; delgado; meticuloso",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (silk, suggesting fine threads)",
                "sound_component": "田 (tián, phonetic harmony)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic compound where silk radical indicates delicate spun fiber.",
                "visual_mnemonic_story_en": "A silken thread (纟) stretched across an open rice field (田) is so fine it captures the tiniest dew drops.",
                "visual_mnemonic_story_es": "Un hilo de seda (纟) tendido sobre un campo de arroz (田) es tan fino que atrapa las gotas más diminutas.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMW",
                "traditional": "細"
            },
            {
                "character": "节",
                "pinyin": "jié",
                "meaning_en": "joint; node; segment; moderation",
                "meaning_es": "nudo; articulación; segmento; moderación",
                "radical": "艸",
                "radical_meaning_en": "grass",
                "meaning_component": "艸 (grass, derived from bamboo nodes)",
                "sound_component": "卩 (jié, simplified form marker)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Originally written with bamboo radical 節 indicating the distinct nodes dividing bamboo into measured sections.",
                "visual_mnemonic_story_en": "Sprouts of vegetation (艹) growing up to a seal (卩) mark the measured seasonal breaks of a stem.",
                "visual_mnemonic_story_es": "Brotes de hierba (艹) que crecen junto a un sello (卩) marcan las secciones medidas del tallo.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "TSL",
                "traditional": "節"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Examine every fine silk thread (细) tied at each bamboo joint (节) to grasp the true details.",
            "composite_memory_hook_es": "Examina cada fino hilo de seda (细) atado en cada nudo de bambú (节) para comprender los verdaderos detalles.",
            "cultural_and_cognitive_roots": "Traditional Chinese philosophy posits that wholeness emerges from the disciplined harmony of micro-units; 'xì' (fine thread) and 'jié' (bamboo joint) signify that elegance resides in flawless joints.",
            "tone_sandhi_and_pitch_modulation": "Pronounced with a 51-35 pitch contour (4th tone falling sharply, followed by 2nd tone rising cleanly). Do not truncate the rising contour of jié."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "粗", "pinyin": "cū", "meaning_en": "coarse; rough", "distinction_note": "Has radical 米 (rice) instead of 纟 (silk); semantically its direct antonym"},
                {"character": "组", "pinyin": "zǔ", "meaning_en": "group; organize", "distinction_note": "Shares radical 纟 but has 且 on the right instead of 田"},
                {"character": "符", "pinyin": "fú", "meaning_en": "tally; symbol", "distinction_note": "Has bamboo radical 竹 over 付; unrelated to 节"},
                {"character": "爷", "pinyin": "yé", "meaning_en": "grandfather; lord", "distinction_note": "Has top radical 父; distinct lower structure from 节"}
            ],
            "etymological_cognates": [
                {"character": "丝", "pinyin": "sī", "gloss_en": "silk; minute thread"},
                {"character": "幼", "pinyin": "yòu", "gloss_en": "infant; tender micro-growth"},
                {"character": "竹", "pinyin": "zhú", "gloss_en": "bamboo; parent radical of traditional 節"},
                {"character": "阶", "pinyin": "jiē", "gloss_en": "steps; discrete levels"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "细节 refers specifically to concrete micro-components, particulars, or subtle nuances embedded within a whole entity or situation.",
            "contrasts": [
                {"id": "1", "compared_word": "细节 vs. 详细", "pinyin": "xiángxì", "analysis": "细节 is a noun referring to the discrete facts or structural particulars, whereas 详细 is an adjective meaning thorough, detailed, or exhaustive in explanation."},
                {"id": "2", "compared_word": "细节 vs. 环节", "pinyin": "huánjié", "analysis": "细节 denotes static individual elements or subtle touches, while 环节 represents a vital link, stage, or operational phase within a sequential process."},
                {"id": "3", "compared_word": "细节 vs. 情节", "pinyin": "qíngjié", "analysis": "细节 applies broadly to any physical, technical, or behavioural detail, whereas 情节 is restricted to narrative plots, storylines, or dramatic sequences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活的美好往往隐藏在那些不被注意的细节之中。清晨桌案上一杯温热的红茶，窗台前一盆悄然绽放的花，都在静默中诉说着温度。懂得捕捉细节的人，才能在平凡岁月中体会生命的温润。",
                "pinyin": "Shēnghuó de měihǎo wǎngwǎng yǐncáng zài nàxiē bú bèi zhùyì de xìjié zhīzhōng. Qīngchén zhuō'àn shàng yì bēi wēnrè de hóngchá, chuāngtái qián yì pén qiǎorán zhànfàng de huā, dōu zài jìngmò zhōng sùshuō zhe wēndù. Dǒngdé bǔzhuō xìjié de rén, cáinǐng zài píngfán suìyuè zhōng tǐhuì shēngmìng de wēnrùn.",
                "en": "The beauty of life often hides within unnoticed details. A warm cup of black tea on the morning desk and a flower quietly blooming by the window silently convey warmth. Only those who know how to capture details can savor life's gentle grace in ordinary days.",
                "es": "La belleza de la vida a menudo se oculta en aquellos detalles que pasan desapercibidos. Una taza de té tibio sobre la mesa matutina y una flor que florece en silencio junto a la ventana expresan calidez. Solo quien sabe apreciar los detalles logra percibir la ternura de la existencia."
            },
            {
                "id": "#2",
                "hanzi": "制造业的竞争力正转向精密制造。在高端装备与半导体产业中，公差控制的微米级细节往往决定了整体性能与良品率。国际标准对生产细节的严苛要求，倒逼企业建立全生命周期的精细化管理体系。",
                "pinyin": "Zhìzàoyè de jìngzhēnglì zhèng zhuǎnxiàng jīngmì zhìzào. Zài gāoduān zhuāngbèi yǔ bàndǎotǐ chǎnyè zhōng, gōngchā kòngzhì de wēimǐ jí xìjié wǎngwǎng juédìng le zhěngtǐ xìngnéng yǔ liángpǐnlǜ. Guójì biāozhǔn duì shēngchǎn xìjié de yánkē yāoqiú, dàobī qǐyè jiànlì quán shēngmìng zhōuqī de jīngxìhuà guǎnlǐ tǐxì.",
                "en": "Manufacturing competitiveness is shifting toward precision engineering. In high-end equipment and semiconductor sectors, micron-level tolerance details often determine overall performance and yield. Stringent international standards on production details compel enterprises to establish lifecycle refined management systems.",
                "es": "La competitividad manufacturera evoluciona hacia la ingeniería de precisión. En equipos avanzados y semiconductores, los detalles de tolerancia micrométrica determinan el rendimiento y la calidad. Las exigentes normas internacionales sobre detalles productivos obligan a implantar una gestión refinada integral."
            }
        ]
    },

    # 02 电台
    {
        "id": "2",
        "hanzi": "电台",
        "pinyin": "diàn tái",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "radio station; broadcasting station; transceiver station",
            "es": "emisora de radio; estación de radio; radiotransmisor"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "radio broadcasting station; transceiver apparatus",
                "definition_es": "estación de radiodifusión; aparato transmisor y receptor de radio",
                "example_phrase": "收听电台 (listen to the radio station)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每当深夜开车行驶在空旷的高速公路上，我总习惯打开车载广播，收听音乐电台的经典老歌。",
                "pinyin": "Měidāng shēnyè kāichē xíngshǐ zài kōngkuàng de gāosù gōnglù shàng, wǒ zǒng xíguàn dǎkāi chēzài guǎngbō, shōutīng yīnyuè diàntái de jīngdiǎn lǎogē.",
                "en": "Whenever I drive on the empty highway late at night, I am accustomed to turning on the car radio to listen to classics on the music station.",
                "es": "Cada vez que conduzco de noche por la autopista despejada, suelo encender la radio del coche para escuchar canciones clásicas en la emisora musical."
            },
            {
                "id": "#2",
                "hanzi": "在发生重大自然灾害导致移动通信网络中断时，民用无线电台成了灾区与外界取得联系的关键通道。",
                "pinyin": "Zài fāshēng zhòngdà zìrán zāihài dǎozhì yídòng tōngxìn wǎngluò zhōngduàn shí, mínyòng wúxiàndiàn diàntái chéng le zāiqū yǔ wàijiè qǔdé liánxì de guānjiàn tōngdào.",
                "en": "When a major natural disaster cuts off cellular networks, civilian radio transceiver stations become the crucial channel connecting the disaster area with the outside world.",
                "es": "Cuando un gran desastre natural interrumpe las redes móviles, las estaciones de radiotransmisión civil se convierten en el canal decisivo para comunicar la zona afectada con el exterior."
            }
        ],
        "collocations": [
            {"hanzi": "广播电台", "en": "radio broadcasting station"},
            {"hanzi": "收听电台", "en": "listen to a radio station"},
            {"hanzi": "地方电台", "en": "local radio station"},
            {"hanzi": "无线电台", "en": "wireless transceiver station"},
            {"hanzi": "电台主持人", "en": "radio show host"},
            {"hanzi": "电台频率", "en": "radio station frequency"}
        ],
        "idioms": [
            {"hanzi": "风驰电掣", "pinyin": "fēng chí diàn chè", "meaning_en": "swift as the wind and quick as lightning"},
            {"hanzi": "雷电交加", "pinyin": "léi diàn jiāo jiā", "meaning_en": "lightning accompanied by thunder; severe storms"},
            {"hanzi": "电光石火", "pinyin": "diàn guāng shí huǒ", "meaning_en": "lightning flash and spark of flint; in a flash"},
            {"hanzi": "登台亮相", "pinyin": "dēng tái liàng xiàng", "meaning_en": "mount the stage and make an appearance"}
        ],
        "character_decomposition": [
            {
                "character": "电",
                "pinyin": "diàn",
                "meaning_en": "electricity; lightning",
                "meaning_es": "electricidad; rayo",
                "radical": "田",
                "radical_meaning_en": "field",
                "meaning_component": "田 (field / cloud matrix)",
                "sound_component": "乚 (lightning bolt curving downwards)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Originally depicted a flash of lightning bursting through rain clouds.",
                "visual_mnemonic_story_en": "Sun and clouds overhead (日) discharge a bright curved bolt of lightning (乚) onto the land.",
                "visual_mnemonic_story_es": "El sol y las nubes (日) descargan un rayo curvo y luminoso (乚) sobre la tierra.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LWU",
                "traditional": "電"
            },
            {
                "character": "台",
                "pinyin": "tái",
                "meaning_en": "platform; stage; station",
                "meaning_es": "plataforma; escenario; estación",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth, speaking or commanding)",
                "sound_component": "厶 (sī, phonetic marker)",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Simplification conflating 台 (elevated structure/terrace) and 臺 (watchtower).",
                "visual_mnemonic_story_en": "A speaker stands on a private platform (厶) projecting announcements through a megaphone mouth (口).",
                "visual_mnemonic_story_es": "Un locutor se para sobre una plataforma elevada (厶) y transmite su mensaje a través de la boca (口).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IR",
                "traditional": "臺"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Harnessing electric lightning waves (电) on an elevated broadcast platform (台) creates a radio station.",
            "composite_memory_hook_es": "Aprovechar las ondas eléctricas (电) sobre una plataforma elevada (台) da vida a una emisora de radio.",
            "cultural_and_cognitive_roots": "Early 20th-century Chinese modernization combined 'diàn' (lightning/electricity) with 'tái' (high terrace or altar), conceptualizing mass radio broadcasting as an elevated electric stage beaming voices into every household.",
            "tone_sandhi_and_pitch_modulation": "51-35 pitch contour (4th tone falling sharp, 2nd tone rising smooth). Avoid neutralizing the second syllable into a light tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "申", "pinyin": "shēn", "meaning_en": "express; state", "distinction_note": "Vertical stroke extends through both top and bottom, unlike 电"},
                {"character": "甲", "pinyin": "jiǎ", "meaning_en": "first; armor", "distinction_note": "Vertical stroke extends only downward from 田, unlike 电 which curls"},
                {"character": "合", "pinyin": "hé", "meaning_en": "combine; join", "distinction_note": "Has roof 人/一 on top instead of 厶; distinct from 台"},
                {"character": "苔", "pinyin": "tái", "meaning_en": "moss", "distinction_note": "Has grass radical 艹 above 台; refers to botanical moss"}
            ],
            "etymological_cognates": [
                {"character": "雷", "pinyin": "léi", "gloss_en": "thunder; shares rain/storm root with traditional 電"},
                {"character": "震", "pinyin": "zhèn", "gloss_en": "shock; quake; meteorological family"},
                {"character": "坛", "pinyin": "tán", "gloss_en": "altar; elevated platform"},
                {"character": "基", "pinyin": "jī", "gloss_en": "base; foundation stage"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "电台 specifically denotes a radio transmission station or apparatus that broadcasts voice and acoustic signals over electromagnetic airwaves.",
            "contrasts": [
                {"id": "1", "compared_word": "电台 vs. 电视台", "pinyin": "diànshìtái", "analysis": "电台 broadcasts purely auditory content over radio frequencies, whereas 电视台 produces and broadcasts audio-visual television programming."},
                {"id": "2", "compared_word": "电台 vs. 广播", "pinyin": "guǎngbō", "analysis": "电台 is the institutional facility, organization, or physical station, while 广播 refers to the medium or action of broadcasting audio signals."},
                {"id": "3", "compared_word": "电台 vs. 报社", "pinyin": "bàoshè", "analysis": "电台 is an electronic audio broadcasting institution, whereas 报社 is a print or digital newspaper publishing house."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在收音机普及的岁月里，电台播音曾陪伴了一代人的青春。每当夜幕降临，主持人温和的声音穿透黑暗，抚慰着无数孤独的心灵。电台用电波架起了一座温暖之桥。",
                "pinyin": "Zài shōuyīnjī pǔjí de suìyuè lǐ, diàntái bōyīn céng péibàn le yí dài rén de qīngchūn. Měidāng yèmù jiànglín, zhǔchírén wēnhé de shēngyīn chuāntòu hēi'àn, fǔwèi zhe wúshù gūdú de xīnlíng. Diàntái yòng diànbō jiàqǐ le yí zuò wēnnuǎn zhī qiáo.",
                "en": "In the days when radios were widespread, radio broadcasts accompanied a generation's youth. As night fell, the host's gentle voice pierced the darkness, comforting lonely hearts. The station built a bridge of warmth with radio waves.",
                "es": "En la época en que la radio era común, sus emisiones acompañaron a toda una generación. Al caer la noche, la voz serena del locutor atravesaba la penumbra, reconfortando corazones solitarios y tendiendo un puente de calidez."
            },
            {
                "id": "#2",
                "hanzi": "随着融媒体时代的发展，传统广播电台正加快数字化转型步伐。许多电台进军音频客户端与网络播客，重构交互式内容生态，不仅拓宽了受众边界，更提升了现代公共传媒的传播实效。",
                "pinyin": "Suízhe róng méitǐ shídài de fāzhǎn, chuántǒng guǎngbō diàntái zhèng jiākuài shùzìhuà zhuǎnxíng bùfá. Xǔduō diàntái jìnjūn yīnpín kèhùduān yǔ wǎngluò bōkè, zhònggòu jiāohùshì nèiróng shēngtài, bùjǐn tuòkuān le shòuzhòng biānjiè, gèng tíshēng le xiàndài gōnggòng chuánméi de chuánbō shíxiào.",
                "en": "With the development of media convergence, traditional radio stations are accelerating digital transformation. Many stations enter audio apps and podcasts to reshape interactive ecosystems, broadening audiences and improving public communication.",
                "es": "Con el avance de la convergencia de medios, las emisoras tradicionales aceleran su digitalización. Al incursionar en aplicaciones y podcasts, reconstruyen un ecosistema interactivo que amplía audiencias y optimiza la comunicación pública."
            }
        ]
    },

    # 03 恩爱
    {
        "id": "3",
        "hanzi": "恩爱",
        "pinyin": "ēn ài",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "(of husband and wife) affectionate; loving; deeply devoted",
            "es": "(entre cónyuges) cariñoso; amoroso; profundamente afectuoso"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "mutually loving and deeply affectionate (specifically used for married couples)",
                "definition_es": "afectuoso y enamorado recíprocamente (empleado en particular para parejas de cónyuges)",
                "example_phrase": "夫妻恩爱 (affectionate married couple)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "爷爷奶奶结婚五十年了，日常生活中互敬互助，街坊邻里都羡慕他们十分恩爱。",
                "pinyin": "Yéye nǎinai jiéhūn wǔshí nián le, rìcháng shēnghuó zhōng hù jìng hù zhù, jiēfang línlǐ dōu xiànmù tāmen shífēn ēn'ài.",
                "en": "Grandpa and grandma have been married for fifty years; they respect and help each other daily, and all the neighbors admire how deeply affectionate they are.",
                "es": "El abuelo y la abuela llevan cincuenta años casados; se respetan y ayudan mutuamente cada día, y todos los vecinos admiran lo cariñosos y unidos que son."
            },
            {
                "id": "#2",
                "hanzi": "家庭社会学调研显示，夫妻恩爱且沟通顺畅的家庭环境，对于未成年子女健全人格的塑造具有决定性影响。",
                "pinyin": "Jiātíng shèhuìxué diàoyán xiǎnshì, fūqī ēn'ài qiě gōutōng shùnchàng de jiātíng huánjìng, duìyú wèichéngnián zǐnǚ jiànquán réngé de shùzào jùyǒu juédìngxìng yǐngxiǎng.",
                "en": "Family sociology surveys demonstrate that an affectionate marital environment with smooth communication exerts a decisive influence on shaping wholesome personalities in underage children.",
                "es": "Los estudios de sociología familiar demuestran que un entorno doméstico donde los cónyuges son amorosos y mantienen una comunicación fluida tiene un impacto decisivo en la formación de una personalidad sana en los hijos menores."
            }
        ],
        "collocations": [
            {"hanzi": "夫妻恩爱", "en": "loving married couple"},
            {"hanzi": "十分恩爱", "en": "extremely affectionate"},
            {"hanzi": "恩爱夫妻", "en": "devoted husband and wife"},
            {"hanzi": "恩爱如初", "en": "as loving as in the beginning"},
            {"hanzi": "恩爱有加", "en": "exceptionally loving and caring"},
            {"hanzi": "秀恩爱", "en": "publicly display affection"}
        ],
        "idioms": [
            {"hanzi": "恩重如山", "pinyin": "ēn zhòng rú shān", "meaning_en": "benevolence as heavy as a mountain; immense gratitude"},
            {"hanzi": "爱不释手", "pinyin": "ài bù shì shǒu", "meaning_en": "love something so much that one cannot bear to part with it"},
            {"hanzi": "相濡以沫", "pinyin": "xiāng rú yǐ mò", "meaning_en": "moisten each other with saliva; share meager resources in adversity"},
            {"hanzi": "恩威并施", "pinyin": "ēn wēi bìng shī", "meaning_en": "combine mercy with severity; balance kindness and authority"}
        ],
        "character_decomposition": [
            {
                "character": "恩",
                "pinyin": "ēn",
                "meaning_en": "grace; favor; gratitude; kindness",
                "meaning_es": "gracia; favor; gratitud; bondad",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "心 (heart, feelings of gratitude)",
                "sound_component": "因 (yīn, phonetic root)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic compound composed of 因 (cause/source) over 心 (heart), evoking deep gratitude felt in the heart for kindness received.",
                "visual_mnemonic_story_en": "When someone gives you a reason (因) to survive hardship, your heart (心) fills with lifelong grace.",
                "visual_mnemonic_story_es": "Cuando alguien te brinda un motivo (因) para superar la adversidad, tu corazón (心) se llena de gratitud eterna.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "WKP",
                "traditional": '""'
            },
            {
                "character": "爱",
                "pinyin": "ài",
                "meaning_en": "love; affection; cherish",
                "meaning_es": "amor; afecto; apreciar",
                "radical": "爫",
                "radical_meaning_en": "claw / hand",
                "meaning_component": "爫 (hand holding gently) + 友 (friendship/embrace)",
                "sound_component": "冖 (cover/canopy protecting)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Originally featured 心 (heart) in traditional 愛; simplified to shelter (爫/冖) over friend (友), denoting tender embrace.",
                "visual_mnemonic_story_en": "A protective canopy (冖) extends caring hands (爫) to shelter a cherished friend (友).",
                "visual_mnemonic_story_es": "Un manto protector (冖) extiende manos cariñosas (爫) para cobijar a un amigo entrañable (友).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BBE",
                "traditional": "愛"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Mutual kindness and lifelong grace (恩) combined with passionate tenderness (爱) define marital devotion.",
            "composite_memory_hook_es": "La bondad mutua y la gratitud compartida (恩) unidas a la ternura sincera (爱) definen el amor conyugal.",
            "cultural_and_cognitive_roots": "In Chinese marital ethics, romantic passion alone is fragile; true matrimonial harmony requires 'ēn' (benevolence, mutual obligation, and shared loyalty) alongside 'ài' (emotional affection). Hence, conjugal love is conceived as moral and emotional reciprocity.",
            "tone_sandhi_and_pitch_modulation": "55-51 pitch contour (1st tone high level at 55, smoothly sliding into 4th tone falling from 5 to 1). Note the glottal onset or smooth liaison between ēn and ài."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "思", "pinyin": "sī", "meaning_en": "think; consider", "distinction_note": "Features 田 (field) over 心 (heart) instead of 因 (cause)"},
                {"character": "受", "pinyin": "shòu", "meaning_en": "receive; endure", "distinction_note": "Lacks the top stroke and has 又 at the bottom; distinct from 爱"},
                {"character": "妥", "pinyin": "tuǒ", "meaning_en": "appropriate; settled", "distinction_note": "Features 女 (woman) below 爫 instead of 友"},
                {"character": "息", "pinyin": "xī", "meaning_en": "breath; rest", "distinction_note": "Has 自 (nose/self) above 心 instead of 因"}
            ],
            "etymological_cognates": [
                {"character": "因", "pinyin": "yīn", "gloss_en": "cause; reason; phonetic matrix for 恩"},
                {"character": "德", "pinyin": "dé", "gloss_en": "virtue; moral grace sharing heart radical"},
                {"character": "友", "pinyin": "yǒu", "gloss_en": "friend; companion component of simplified 爱"},
                {"character": "慈", "pinyin": "cí", "gloss_en": "compassionate; merciful love"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "恩爱 specifically characterizes reciprocal tenderness, devotion, and moral-emotional bonding between spouses.",
            "contrasts": [
                {"id": "1", "compared_word": "恩爱 vs. 相爱", "pinyin": "xiāng'ài", "analysis": "恩爱 is strictly used to describe married couples possessing enduring mutual care, whereas 相爱 can refer broadly to lovers, partners, or people falling in love at any relationship stage."},
                {"id": "2", "compared_word": "恩爱 vs. 亲热", "pinyin": "qīnrè", "analysis": "恩爱 denotes deep emotional and spiritual harmony in marriage, while 亲热 emphasizes overtly affectionate, warm, or physically intimate behaviour between friends or partners."},
                {"id": "3", "compared_word": "恩爱 vs. 关爱", "pinyin": "guān'ài", "analysis": "恩爱 describes mutual spousal devotion, while 关爱 is a transitive verb/noun referring to caring for and looking after elders, children, subordinates, or the vulnerable."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "世间最动人的爱情，往往是步入晚年后依然相濡以沫的恩爱。当岁月的风霜爬满额头，彼此依然能读懂对方眼中的温存，在柴米油盐中相守一生。这种恩爱早已化作生命的契约。",
                "pinyin": "Shìjiān zuì dòngrén de àiqíng, wǎngwǎng shì bùrù wǎnnián hòu yīrán xiāngrúyǐmò de ēn'ài. Dāng suìyuè de fēngshuāng pámǎn étóu, bǐcǐ yīrán néng dúdǒng duìfāng yǎn zhōng de wēncún, zài cháimǐyóuyán zhōng xiāngshǒu yìshēng. Zhè zhǒng ēn'ài zǎoyǐ huàzuò shēngmìng de qìyuē.",
                "en": "The most touching love is the lifelong affection of growing old together. When frost marks their foreheads, they still read tenderness in each other's eyes throughout daily life. Such marital love becomes an enduring covenant of existence.",
                "es": "El amor más conmovedor es el afecto conyugal que perdura en la vejez. Cuando el tiempo marca el rostro, ambos siguen leyendo ternura en sus miradas a través de la vida diaria, convirtiendo su cariño en un pacto indestructible."
            },
            {
                "id": "#2",
                "hanzi": "在快节奏生活下，夫妻情感凝聚力成为重要的社会议题。婚姻学者强调，健康的恩爱关系需要在同甘共苦中培育责任认同。通过建立良性倾听机制与情感仪式感，才能有效抵御现代家庭的解构风险。",
                "pinyin": "Zài kuài jièzòu shēnghuó xià, fūqī qínggǎn níngjùlì chéngwéi zhòngyào de shèhuì yìtí. Hūnyīn xuézhě qiángdiào, jiànkāng de ēn'ài guānxì xūyào zài tónggāngòngkǔ zhōng péiyù zérèn rèntóng. Tōngguò jiànlì liángxìng qīngtīng jīzhì yǔ qínggǎn yíshìgǎn, cáinǐng yǒuxiào dǐyù xiàndài jiātíng de jiěgòu fēngxiǎn.",
                "en": "In fast-paced life, spousal cohesion is an essential social issue. Scholars emphasize that healthy marital love requires cultivating shared responsibility through thick and thin. Establishing listening habits and emotional rituals effectively resists the risk of family fragmentation.",
                "es": "En la vida contemporánea, la cohesión conyugal es una cuestión social clave. Los especialistas señalan que un amor matrimonial sano exige cultivar la responsabilidad compartida. La escucha mutua y los rituales afectivos protegen a la familia frente a la fragmentación."
            }
        ]
    },

    # 04 对比
    {
        "id": "4",
        "hanzi": "对比",
        "pinyin": "duì bǐ",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to compare; to contrast; contrast; comparison",
            "es": "comparar; contrastar; contraste; comparación"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to juxtapose two or more things to examine their differences and similarities",
                "definition_es": "yuxtaponer dos o más cosas para examinar sus diferencias y similitudes",
                "example_phrase": "对比两组数据 (compare two sets of data)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a marked contrast or juxtaposition",
                "definition_es": "un marcado contraste o contraposición",
                "example_phrase": "形成鲜明对比 (form a sharp contrast)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老师让我们仔细对比这两篇题材相同的作文，分析它们在写作手法与结构上的异同。",
                "pinyin": "Lǎoshī ràng wǒmen zǐxì duìbǐ zhè liǎng piān tícái xiāngtóng de zuòwén, fēnxī tāmen zài xiězuò shǒufǎ yǔ jiégòu shàng de yìtóng.",
                "en": "The teacher had us carefully compare these two essays on the same topic, analyzing similarities and differences in writing techniques and structure.",
                "es": "El profesor nos pidió comparar detenidamente estas dos redacciones sobre el mismo tema, analizando similitudes y diferencias en sus técnicas narrativas y estructura."
            },
            {
                "id": "#2",
                "hanzi": "经济研究团队通过对比过去三十年间的进出口贸易数据，深入论证了新兴产业转型升级的战略成效。",
                "pinyin": "Jīngjì yánjiū tuánduì tōngguò duìbǐ guòqù sānshí nián jiān de jìnchūkǒu màoyì shùjù, shēnrù lùnzhèng le xīnxīng chǎnyè zhuǎnxíng shēngjí de zhànlüè chéngxiào.",
                "en": "By contrasting import and export trade data over the past thirty years, the economic research team substantiated the strategic efficacy of emerging industry upgrades.",
                "es": "Al contrastar los datos comerciales de importación y exportación de las últimas tres décadas, el equipo de investigación económica demostró la eficacia estratégica de la transformación industrial emergente."
            }
        ],
        "collocations": [
            {"hanzi": "鲜明对比", "en": "sharp contrast"},
            {"hanzi": "强烈对比", "en": "strong contrast"},
            {"hanzi": "对比分析", "en": "comparative analysis"},
            {"hanzi": "对比数据", "en": "compare data"},
            {"hanzi": "横向对比", "en": "horizontal/peer comparison"},
            {"hanzi": "纵向对比", "en": "longitudinal/historical comparison"}
        ],
        "idioms": [
            {"hanzi": "截然不同", "pinyin": "jié rán bù tóng", "meaning_en": "completely different; worlds apart"},
            {"hanzi": "对比鲜明", "pinyin": "duì bǐ xiān míng", "meaning_en": "in striking contrast; sharply demarcated"},
            {"hanzi": "针锋相对", "pinyin": "zhēn fēng xiāng duì", "meaning_en": "tit for tat; sharply oppose head-on"},
            {"hanzi": "比上不足", "pinyin": "bǐ shàng bù zú", "meaning_en": "fall short of the best, but better than the worst"}
        ],
        "character_decomposition": [
            {
                "character": "对",
                "pinyin": "duì",
                "meaning_en": "face; pair; opposite; correct",
                "meaning_es": "frente a; pareja; opuesto; correcto",
                "radical": "寸",
                "radical_meaning_en": "inch / hand measurement",
                "meaning_component": "寸 (inch/rule for measurement)",
                "sound_component": "又 (hand/phonetic simplification)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Originally depicted standing face-to-face and answering appropriately under royal measure (寸).",
                "visual_mnemonic_story_en": "Two hands (又) measure with a small inch ruler (寸) to ensure two objects face each other evenly.",
                "visual_mnemonic_story_es": "Dos manos (又) miden con una regla de pulgada (寸) para asegurarse de que dos piezas se enfrenten con exactitud.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EDI",
                "traditional": "對"
            },
            {
                "character": "比",
                "pinyin": "bǐ",
                "meaning_en": "compare; emulate; close together",
                "meaning_es": "comparar; competir; estar juntos",
                "radical": "比",
                "radical_meaning_en": "compare",
                "meaning_component": "匕 (person standing next to another)",
                "sound_component": "匕 (bǐ, mirrored human figures)",
                "stroke_count": 4,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Pictogram of two people walking side by side shoulder-to-shoulder, compared against each other.",
                "visual_mnemonic_story_en": "Two people (匕 + 匕) stand side by side back-to-back to compare their heights.",
                "visual_mnemonic_story_es": "Dos personas (匕 + 匕) se paran hombro con hombro para comparar sus estaturas.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "PP",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Place two objects face-to-face (对) and stand them side by side (比) to highlight their contrast.",
            "composite_memory_hook_es": "Coloca dos objetos frente a frente (对) y ponlos hombro con hombro (比) para contrastar sus diferencias.",
            "cultural_and_cognitive_roots": "The cognitive framework of 'duì' (confronting/pairing) and 'bǐ' (parallel alignment) stems from ancient Chinese logic of polar dialectics: understanding truth requires balancing symmetrical opposites.",
            "tone_sandhi_and_pitch_modulation": "51-214 contour. The first syllable is a crisp falling 4th tone (51), followed by the dipping 3rd tone of bǐ (214). When followed by another syllable, bǐ drops to a low dipping tone (21)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "寸", "pinyin": "cùn", "meaning_en": "inch", "distinction_note": "Lacks the left component 又 of 对"},
                {"character": "北", "pinyin": "běi", "meaning_en": "north; flee", "distinction_note": "Depicts two people back-to-back (opposite facing), while 比 has both facing the same direction"},
                {"character": "皆", "pinyin": "jiē", "meaning_en": "all; each", "distinction_note": "Features 比 over 白 (white); denotes universality"},
                {"character": "毕", "pinyin": "bì", "meaning_en": "complete; finish", "distinction_note": "Has 比 at the top over 十; means to conclude"}
            ],
            "etymological_cognates": [
                {"character": "匹", "pinyin": "pǐ", "gloss_en": "match; equal counterpart; sharing pairing nuance"},
                {"character": "从", "pinyin": "cóng", "gloss_en": "follow; two people aligned sequentially"},
                {"character": "齐", "pinyin": "qí", "gloss_en": "even; uniform level"},
                {"character": "双", "pinyin": "shuāng", "gloss_en": "pair; two hands together"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "对比 emphasizes laying two contrasting entities side by side to discern discrepancies, discrepancies of scale, or oppositional characteristics.",
            "contrasts": [
                {"id": "1", "compared_word": "对比 vs. 比较", "pinyin": "bǐjiào", "analysis": "比较 is a general verb/adverb meaning to compare or 'relatively', whereas 对比 strongly highlights stark differences, polarity, or visual/analytical juxtaposition."},
                {"id": "2", "compared_word": "对比 vs. 相比", "pinyin": "xiāngbǐ", "analysis": "相比 is typically used in introductory adverbial frames (如“与……相比”), whereas 对比 functions directly as a transitive verb or an independent noun (如“鲜明的对比”)."},
                {"id": "3", "compared_word": "对比 vs. 对照", "pinyin": "duìzhào", "analysis": "对照 implies checking against a standard, benchmark, or reference text (e.g., verifying against a translation), whereas 对比 investigates thematic or statistical divergences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古老的青砖瓦房与高耸的现代玻璃幕墙在晨光中形成了鲜明的对比。历史的厚重与现代的轻盈在街头对话，让人体会到岁月的流变。正是在这种对比中，城市记忆才更加立体丰满。",
                "pinyin": "Gǔlǎo de qīngzhuān wǎfáng yǔ gāosǒng de xiàndài bōlí mùqiáng zài chénguāng zhōng xíngchéng le xiānmíng de duìbǐ. Lìshǐ de hòuzhòng yǔ xiàndài de qīngyíng zài jiētóu duìhuà, ràng rén tǐhuì dào suìyuè de liúbiàn. Zhèng shì zài zhè zhǒng duìbǐ zhōng, chéngshì jìyì cái gèngjiā lìtǐ fēngmǎn.",
                "en": "Ancient grey tile cottages and soaring modern glass curtain walls form a vivid contrast in the morning light. Historical gravitas converses with contemporary grace, making urban memories richer through contrast.",
                "es": "Las antiguas casas de teja gris y los modernos muros de cristal forman un vivo contraste bajo la luz matutina. La solidez histórica dialoga con la ligereza contemporánea, enriqueciendo la memoria urbana a través de este contraste."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业战略管理中，标杆管理方法的核心正是跨行业对比。企业通过对标行业领军者的周转速度与创新周期，精准识别价值链短板。深入的对比分析不仅能打破路径依赖，更为流程再造提供了量化依据。",
                "pinyin": "Zài xiàndài qǐyè zhànlüè guǎnlǐ zhōng, biāogān guǎnlǐ fāngfǎ de héxīn zhèng shì kuà hángyè duìbǐ. Qǐyè tōngguò duìbiāo hángyè lǐngjūnzhě de zhōuzhuǎn sùdù yǔ chuàngxīn zhōuqī, jīngzhǔn shíbié jiàzhíliàn duǎnbǎn. Shēnrù de duìbǐ fēnxī bùjǐn néng dǎpò lùjìng yīlài, gèng wèi liúchéng zàizào tígōng le liànghuà yījù.",
                "en": "In corporate strategy, benchmarking centers on cross-industry comparison. By comparing turnover velocity and innovation cycles with leaders, firms identify value-chain weaknesses. Deep comparative analysis breaks path dependency and provides quantitative grounds for reengineering.",
                "es": "En la estrategia empresarial moderna, el benchmarking se basa en la comparación intersectorial. Al contrastar la velocidad de rotación e innovación con los líderes, las empresas identifican fallos y obtienen bases cuantitativas para rediseñar procesos."
            }
        ]
    },

    # 05 入围
    {
        "id": "5",
        "hanzi": "入围",
        "pinyin": "rù wéi",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to be shortlisted; to qualify for the next round; to make the finalist list",
            "es": "ser seleccionado; quedar como finalista; pasar a la ronda final"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to pass preliminary screening and enter the final selection or shortlist of a competition",
                "definition_es": "superar la selección preliminar y entrar en la lista de finalistas de un certamen o concurso",
                "example_phrase": "入围决赛 (make it to the finals)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过长达半年的刻苦备战，我们学校的辩论队凭借出色的发挥顺利入围全国中学生辩论锦标赛总决赛。",
                "pinyin": "Jīngguò chángdá bàn nián de kèkǔ bèizhàn, wǒmen xuéxiào de biànlùn duì píngjiè chūsè de fāhuī shùnlì rùwéi quánguó zhōngxuéshēng biànlùn jǐnbiāosài zǒngjuésài.",
                "en": "After half a year of arduous preparation, our school debate team smoothly qualified for the national high school debate championship grand finals.",
                "es": "Tras medio año de rigurosa preparación, el equipo de debate de nuestra escuela logró clasificarse con éxito para la gran final del campeonato nacional escolar."
            },
            {
                "id": "#2",
                "hanzi": "该项绿色能源专利技术凭借显著的减排效益，成功入围联合国工业发展组织全球可持续技术前沿榜单。",
                "pinyin": "Gāi xiàng lǜsè néngyuán zhuānlì jìshù píngjiè xiǎnzhù de jiǎnpái xiàoyì, chénggōng rùwéi Liánhéguó Gōngyè Fāzhǎn Zǔzhī quánqiú kěchíxù jìshù qiányán bǎngdān.",
                "en": "By virtue of significant emission reduction efficacy, this green energy patent successfully made the shortlist of UNIDO's global sustainable technology frontier ranking.",
                "es": "Gracias a su notable eficacia en reducción de emisiones, esta patente de energía verde logró ser seleccionada en la prestigiosa lista de tecnologías sostenibles de la ONUDI."
            }
        ],
        "collocations": [
            {"hanzi": "成功入围", "en": "successfully shortlisted"},
            {"hanzi": "入围名单", "en": "shortlist / finalists roster"},
            {"hanzi": "入围作品", "en": "shortlisted works"},
            {"hanzi": "入围决赛", "en": "qualify for the finals"},
            {"hanzi": "入围奖项", "en": "shortlisted for awards"},
            {"hanzi": "顺利入围", "en": "smoothly made the cut"}
        ],
        "idioms": [
            {"hanzi": "脱颖而出", "pinyin": "tuō yǐng ér chū", "meaning_en": "stand out from the crowd; talent revealing itself"},
            {"hanzi": "入木三分", "pinyin": "rù mù sān fēn", "meaning_en": "penetrate deeply; keen and incisive"},
            {"hanzi": "金榜题名", "pinyin": "jīn bǎng tí míng", "meaning_en": "pass the civil examination; succeed in a competitive test"},
            {"hanzi": "重围之中", "pinyin": "chóng wéi zhī zhōng", "meaning_en": "amid tight encirclement; in the thick of a cordon"}
        ],
        "character_decomposition": [
            {
                "character": "入",
                "pinyin": "rù",
                "meaning_en": "enter; join; admit",
                "meaning_es": "entrar; ingresar; admitir",
                "radical": "入",
                "radical_meaning_en": "enter",
                "meaning_component": "入 (pictogram of sharp downward entry)",
                "sound_component": "入 (inherent archaic sound)",
                "stroke_count": 2,
                "composition_type": "独体字",
                "etymology_and_mnemonic": "Pictogram of an arrow or wedge penetrating downward through a membrane or portal.",
                "visual_mnemonic_story_en": "A sharp root or wedge (入) pushes its tip deep into the soil to gain entry.",
                "visual_mnemonic_story_es": "Una cuña afilada (入) se abre paso hacia abajo para penetrar en la tierra.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OH",
                "traditional": '""'
            },
            {
                "character": "围",
                "pinyin": "wéi",
                "meaning_en": "surround; enclose; corral; perimeter",
                "meaning_es": "rodear; cercar; recinto; perímetro",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (surrounding boundary wall)",
                "sound_component": "韦 (wéi, leather/encircling belt)",
                "stroke_count": 7,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "Depicts an enclosing border wall (囗) surrounding leather perimeter guards (韦).",
                "visual_mnemonic_story_en": "Soldiers wearing leather armor (韦) stand inside fortified city walls (囗) guarding the designated perimeter.",
                "visual_mnemonic_story_es": "Guardianes con corazas de cuero (韦) vigilan dentro de las murallas (囗) el perímetro del recinto.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "ODS",
                "traditional": "圍"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Penetrating (入) inside the exclusive enclosure (围) means you have officially made the shortlist.",
            "composite_memory_hook_es": "Penetrar (入) dentro del recinto exclusivo (围) significa que has sido seleccionado como finalista.",
            "cultural_and_cognitive_roots": "Derived from the ancient imperial examination and hunting cordon where only top performers were permitted to enter the inner imperial enclosure ('wéi'); modern usage adapts this to entering competitive shortlists.",
            "tone_sandhi_and_pitch_modulation": "51-35 pitch contour. The entering tone of rù falls swiftly (51), followed by the smooth rising contour of wéi (35)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "人", "pinyin": "rén", "meaning_en": "person; human", "distinction_note": "Left falling stroke extends above the right stroke, unlike 入 where right overlaps left"},
                {"character": "八", "pinyin": "bā", "meaning_en": "eight", "distinction_note": "The two strokes do not touch at the top, leaving an open apex"},
                {"character": "国", "pinyin": "guó", "meaning_en": "country; nation", "distinction_note": "Contains 玉 (jade) inside the 囗 enclosure instead of 韦"},
                {"character": "园", "pinyin": "yuán", "meaning_en": "garden; park", "distinction_note": "Contains 元 inside the 囗 enclosure instead of 韦"}
            ],
            "etymological_cognates": [
                {"character": "进", "pinyin": "jìn", "gloss_en": "advance; enter forward"},
                {"character": "内", "pinyin": "nèi", "gloss_en": "inside; interior, sharing inward penetration root"},
                {"character": "圈", "pinyin": "quān", "gloss_en": "circle; bounded ring"},
                {"character": "界", "pinyin": "jiè", "gloss_en": "boundary; border scope"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "入围 specifically denotes crossing the threshold of preliminary selection to secure a designated spot on the final nominee list.",
            "contrasts": [
                {"id": "1", "compared_word": "入围 vs. 晋级", "pinyin": "jìnjí", "analysis": "入围 stresses entering an elite shortlist or nomination bracket (e.g., film awards), while 晋级 emphasizes tournament stage progression (e.g., advancing from round of 16 to quarterfinals)."},
                {"id": "2", "compared_word": "入围 vs. 获奖", "pinyin": "huòjiǎng", "analysis": "入围 indicates qualification as a finalist or nominee, whereas 获奖 denotes actually winning an award or final prize."},
                {"id": "3", "compared_word": "入围 vs. 入选", "pinyin": "rùxuǎn", "analysis": "入选 means being chosen or accepted into a team, anthology, or roster, whereas 入围 strictly implies qualifying for an ongoing competitive final round."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "对青年电影人而言，作品入围国际电影节主竞赛单元，是一份极大的肯定。当掌声在影厅响起，所有的付出都在这一刻化为前行的力量。入围不仅关乎荣耀，更关乎被看见的喜悦。",
                "pinyin": "Duì qīngnián diànyǐngrén éryán, zuòpǐn rùwéi guójì diànyǐngjié zhǔ jìngsài dānyuán, shì yí fèn jídà de kěndìng. Dāng zhǎngshēng zài yǐngtīng xiǎngqǐ, suǒyǒu de fùchū dōu zài zhè yí kè huàwéi qiánxíng de lìliàng. Rùwéi bùjǐn guānhū róngyào, gèng guānhū bèi kànjiàn de xǐyuè.",
                "en": "For young filmmakers, having a work shortlisted in an international festival's main competition is immense validation. When applause rings out, all effort turns into strength to forge ahead. Being shortlisted is not just about honor, but the joy of being seen.",
                "es": "Para un joven cineasta, que su obra quede finalista en la sección oficial de un festival internacional es un gran reconocimiento. Los aplausos convierten todo esfuerzo en impulso. Ser finalista no es solo un honor, sino la alegría de ser apreciado."
            },
            {
                "id": "#2",
                "hanzi": "在大型工程招标实践中，资格预审入围是防范履约风险的首要关卡。招标方从财务稳健度、技术资质及历史绩效等维度展开全面审查。只有成功入围的联合体，方有资格递交最终商务标书。",
                "pinyin": "Zài dàxíng gōngchéng zhāobiāo shíjiàn zhōng, zīgé yùshěn rùwéi shì fángfàn lǚyuē fēngxiǎn de shǒuyào guānkǎ. Zhāobiāofāng cóng cáiwù wěnjiàndù, jìshù zīzhì jí lìshǐ jìxiào děng wéidù zhǎnkāi quánmiàn shěnchá. Zhǐyǒu chénggōng rùwéi de liánhétǐ, fāng yǒu zīgé dìjiāo zuìzhōng shāngwù biāoshū.",
                "en": "In major project tendering, prequalification shortlisting is the primary defense against default risk. Tendering authorities review financial health, technical qualifications, and track record. Only shortlisted consortia may submit final commercial proposals.",
                "es": "En licitaciones de gran envergadura, la preselección de finalistas es el filtro principal contra riesgos de incumplimiento. Se revisan solvencia económica, capacidad técnica e historial. Solo los consorcios seleccionados pueden presentar ofertas comerciales definitivas."
            }
        ]
    }
]

if __name__ == '__main__':
    for w in words_batch1:
        save_word(w)

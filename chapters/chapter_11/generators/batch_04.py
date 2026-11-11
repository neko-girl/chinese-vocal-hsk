# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 精神
    {
        "id": "31",
        "hanzi": "精神",
        "pinyin": "jīng shén",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "spirit; mind; consciousness; energetic; lively",
            "es": "espíritu; mente; ánimo; enérgico; vivaz; despierto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "spirit, mind, mental state, or conscious psychological vitality",
                "definition_es": "espíritu, mente, estado anímico o vitalidad psíquica",
                "example_phrase": "精神饱满 (full of vitality / energetic in spirit)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "vigorous, spirited, lively, looking smart and energetic",
                "definition_es": "despierto, vivaz, lozano o con aspecto saludable y enérgico",
                "example_phrase": "小伙子很精神 (the young man looks very sharp and lively)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "规律的作息与充足的睡眠能够让人每天早晨保持饱满的精神状态，显著提高学习和工作效率。",
                "pinyin": "Guīlǜ de zuòxī yǔ chōngzú de shuìmián nénggòu ràng rén měitiān zǎochén bǎochí bǎomǎn de jīngshén zhuàngtài, xiǎnzhù tígāo xuéxí hé gōngzuò xiàolǜ.",
                "en": "A regular daily schedule and sufficient sleep enable people to maintain an energetic mental state every morning, significantly boosting study and work efficiency.",
                "es": "Tener horarios regulares y dormir lo suficiente permite a las personas mantener un ánimo radiante cada mañana, aumentando notablemente la eficiencia."
            },
            {
                "id": "#2",
                "hanzi": "这位年轻军官穿上整洁的军装后显得格外精神，步伐坚定而充满自信。",
                "pinyin": "Zhè wèi niánqīng jūnguān chuānshàng zhěngjié de jūnzhuāng hòu xiǎnde géwài jīngshen, bùfá jiāndìng ér chōngmǎn zìxìn.",
                "en": "Wearing a crisp uniform, this young military officer looked exceptionally spirited, marching with firm and confident strides.",
                "es": "Con el pulcro uniforme militar puesto, este joven oficial lucía sumamente apuesto y vivaz, marchando con paso firme y seguro."
            }
        ],
        "collocations": [
            {"hanzi": "精神饱满", "en": "full of energy; high-spirited"},
            {"hanzi": "精神状态", "en": "mental state; condition"},
            {"hanzi": "时代精神", "en": "spirit of the times; zeitgeist"},
            {"hanzi": "精神财富", "en": "spiritual wealth; cultural legacy"},
            {"hanzi": "提振精神", "en": "boost one's spirits"},
            {"hanzi": "精神压力", "en": "mental stress; psychological strain"}
        ],
        "idioms": [
            {"hanzi": "精益求精", "pinyin": "jīng yì qiú jīng", "meaning_en": "constantly perfect one's skills; pursue perfection"},
            {"hanzi": "聚精会神", "pinyin": "jù jīng huì shén", "meaning_en": "concentrate one's attention; fully focused"},
            {"hanzi": "神采奕奕", "pinyin": "shén cǎi yì yì", "meaning_en": "radiant with vigor and high spirits"},
            {"hanzi": "心旷神怡", "pinyin": "xīn kuàng shén yí", "meaning_en": "relaxed in mind and joyful in spirit"}
        ],
        "character_decomposition": [
            {
                "character": "精",
                "pinyin": "jīng",
                "meaning_en": "essence; pure; refined; spirit; skilled",
                "meaning_es": "esencia; puro; refinado; espíritu; hábil",
                "radical": "米",
                "radical_meaning_en": "rice",
                "meaning_component": "米 (husked refined white rice) + 青 (pure clear blue/green)",
                "sound_component": "青 (qīng, clear / phonetic)",
                "stroke_count": 14,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Milled white rice 米 refined to perfection with 青 symbolizing pure clear essence; hence the finest core quality.",
                "visual_mnemonic_story_en": "Polished premium rice grains (米) cleansed to pristine green purity (青) represent essence (精).",
                "visual_mnemonic_story_es": "Granos de arroz puro (米) seleccionados con frescura vegetal (青) encarnan la quintaesencia (精).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "FDQB",
                "traditional": ""
            },
            {
                "character": "神",
                "pinyin": "shén",
                "meaning_en": "spirit; deity; soul; expression; mind",
                "meaning_es": "dios; divinidad; espíritu; alma; expresión",
                "radical": "礻",
                "radical_meaning_en": "altar / ritual sign",
                "meaning_component": "礻 (ancestral altar / spiritual revelation) + 申 (lightning bolts / stretch)",
                "sound_component": "申 (shēn, stretch / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Altar sign 礻 paired with 申 depicting celestial lightning bolts descending from heaven; divinity and invisible soul power.",
                "visual_mnemonic_story_en": "At a sacred altar (礻), lightning flashes in the sky (申), manifesting divine spirit (神).",
                "visual_mnemonic_story_es": "Frente al altar sagrado (礻), un rayo cruza el cielo (申) revelando la presencia del espíritu divino (神).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IFLWL",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The refined quintessence of grain (精) united with divine consciousness (神) constitutes true human spirit and vitality (精神).",
            "composite_memory_hook_es": "La quintaesencia refinada del cereal (精) unida a la conciencia divina (神) forja el espíritu y vigor humano (精神).",
            "cultural_and_cognitive_roots": "In traditional Chinese medicine and philosophy, 精 (vital physical essence) and 神 (conscious mental awareness) form the dual foundation of health.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by second tone: 'jīng shén' (55-35). When used colloquially as an adjective ('真精神'), 'shén' often softens into a light neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "晴", "pinyin": "qíng", "meaning_en": "sunny; clear", "distinction_note": "Has sun radical 日 on left instead of rice 米 in 精"},
                {"character": "清", "pinyin": "qīng", "meaning_en": "clear; clean", "distinction_note": "Has water radical 氵 on left"},
                {"character": "绅", "pinyin": "shēn", "meaning_en": "gentry; gentleman", "distinction_note": "Has silk radical 纟 on left instead of altar 礻 in 神"},
                {"character": "伸", "pinyin": "shēn", "meaning_en": "stretch; extend", "distinction_note": "Has person radical 亻 on left of 申"}
            ],
            "etymological_cognates": [
                {"character": "心", "pinyin": "xīn", "gloss_en": "heart; conscious mind"},
                {"character": "气", "pinyin": "qì", "gloss_en": "vital life breath"},
                {"character": "志", "pinyin": "zhì", "gloss_en": "will; aspiration"},
                {"character": "魂", "pinyin": "hún", "gloss_en": "ethereal soul"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "精神 refers to mental energy, conscious psychological state, or the overarching soul/ideology of an era, while also acting as an adjective for looking lively.",
            "contrasts": [
                {"id": "1", "compared_word": "精神 vs. 思想", "pinyin": "sīxiǎng", "analysis": "思想 focuses on intellectual thought, cognitive ideology, or philosophical viewpoints, whereas 精神 denotes psychological vitality, courage, or emotional energy."},
                {"id": "2", "compared_word": "精神 vs. 情绪", "pinyin": "qíngxù", "analysis": "情绪 refers to transient psychological mood swings (e.g. happiness, anger, depression), while 精神 reflects overall vitality, morale, or inner spirit."},
                {"id": "3", "compared_word": "精神 vs. 活力", "pinyin": "huólì", "analysis": "活力 emphasizes dynamic physical and bodily stamina, whereas 精神 combines psychological alertness with physical vigor."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "健康的生活方式是滋养充沛精神的基石。在当今节奏飞快的社会中，长期的熬夜与心理重压容易导致精神萎靡。唯有坚持科学锻炼与规律睡眠，才能使人神采飞扬，以最佳状态迎接每日挑战。",
                "pinyin": "Jiànkāng de shēnghuó fāngshì shì zīyǎng chōngpèi jīngshén de jīshí. Zài dāngjīn jiézòu fēikuài de shèhuì zhōng, chángqī de áoyè yǔ xīnlǐ zhòngyā róngyì dǎozhì jīngshén wěimǐ. Wéiyǒu jiānchí kēxué duànliàn yǔ guīlǜ shuìmián, cáinéng shǐ rén shéncǎi-fēiyáng, yǐ zuìjiā zhuàngtài yíngjiē měirì tiǎozhàn.",
                "en": "A healthy lifestyle forms the cornerstone for nourishing abundant vitality. In fast-paced modern society, chronic late nights and psychological stress easily cause spiritual exhaustion. Only scientific exercise and regular sleep keep one radiant.",
                "es": "Un estilo de vida saludable cimienta la vitalidad anímica. En la apresurada sociedad moderna, trasnochar y el estrés psíquico minan el vigor. Solo el ejercicio metódico y el sueño regular nos mantienen radiantes ante los retos diarios."
            },
            {
                "id": "#2",
                "hanzi": "中华民族在五千年的历史长河中，铸就了坚忍不拔、自强不息的伟大精神。无论面对自然灾害还是外来挑战，这种深沉的文化精神力量始终激励着亿万儿女团结奋斗，在困境中开拓前行，开创出举世瞩目的繁荣发展奇迹。",
                "pinyin": "Zhōnghuá mínzú zài wǔqiān nián de lìshǐ chánghé zhōng, zhùjiùle jiānrěn-bùbá, zìqiáng-bùxī de wěidà jīngshén. Wúlùn miànduì zìrán zāihài háishì wàilái tiǎozhàn, zhèzhǒng shēnchén de wénhuà jīngshén lìliang shǐzhōng jīlì zhe yìwàn érnǚ tuánjié fèndòu, zài kùnjìng zhōng kāituò qiánxíng, kāichuàng chū jǔshì zhǔmù de fánróng fāzhǎn qíjī.",
                "en": "Through five thousand years of history, the Chinese nation has forged an indomitable spirit of self-reliance. Facing natural disasters or hardships, this profound cultural spirit inspires unity and perseverance, creating miracles of development.",
                "es": "A lo largo de cinco milenios, la nación china forjó un espíritu tenaz de superación constante. Ante adversidades naturales o desafíos, esta honda fuerza espiritual impulsa la unión y el avance perseverante, alumbrando milagros de prosperidad admirados por el mundo."
            }
        ]
    },

    # 32 专家
    {
        "id": "32",
        "hanzi": "专家",
        "pinyin": "zhuān jiā",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "expert; specialist; authority in a professional field",
            "es": "experto; especialista; perito; autoridad profesional"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person who has authoritative, specialized knowledge or skill in a specific technical, medical, scientific, or artistic domain",
                "definition_es": "persona con profundos conocimientos técnicos, científicos o artísticos en una disciplina concreta",
                "example_phrase": "医学专家 (medical specialist / authority)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "睡眠医学专家指出，长期依赖刺耳的机械闹钟容易诱发心血管疾病与情绪焦虑。",
                "pinyin": "Shuìmián yīxué zhuānjiā zhǐchū, chángqī yīlài cì'ěr de jīxiè nàozhōng róngyì yòufā xīnxuěguǎn jíbìng yǔ qíngxù jiāolǜ.",
                "en": "Sleep medicine experts point out that long-term reliance on jarring mechanical alarms easily triggers cardiovascular problems and emotional anxiety.",
                "es": "Expertos en medicina del sueño señalan que depender crónicamente de alarmas estridentes provoca dolencias cardiovasculares y ansiedad."
            },
            {
                "id": "#2",
                "hanzi": "为了攻克技术难关，研究所特意邀请了多位海外人工智能领域的知名专家前来进行学术指导。",
                "pinyin": "Wèile gōngkè jìshù nánguān, yánjiūsuǒ tèyì yāoqǐngle duō wèi hǎiwài réngōng zhìnéng lǐngyù de zhīmíng zhuānjiā qiánlái jìnxíng xuéshù zhǐdǎo.",
                "en": "To overcome technological bottlenecks, the research institute specially invited several renowned overseas AI specialists for academic guidance.",
                "es": "Para superar escollos técnicos, el instituto invitó expresamente a varios célebres expertos foráneos en inteligencia artificial para asesoramiento."
            }
        ],
        "collocations": [
            {"hanzi": "知名专家", "en": "renowned expert; famous specialist"},
            {"hanzi": "特聘专家", "en": "specially appointed expert"},
            {"hanzi": "行业专家", "en": "industry expert; trade specialist"},
            {"hanzi": "专家学者", "en": "experts and scholars"},
            {"hanzi": "专家意见", "en": "expert opinion / advisory advice"},
            {"hanzi": "咨询专家", "en": "consult an expert"}
        ],
        "idioms": [
            {"hanzi": "行家手笔", "pinyin": "háng jiā shǒu bǐ", "meaning_en": "the master stroke of an expert; professional workmanship"},
            {"hanzi": "名家辈出", "pinyin": "míng jiā bèi chū", "meaning_en": "celebrated masters emerging generation after generation"},
            {"hanzi": "专心致志", "pinyin": "zhuān xīn zhì zhì", "meaning_en": "wholly devoted and deeply concentrated"},
            {"hanzi": "博古通今", "pinyin": "bó gǔ tōng jīn", "meaning_en": "erudite in both ancient lore and modern knowledge"}
        ],
        "character_decomposition": [
            {
                "character": "专",
                "pinyin": "zhuān",
                "meaning_en": "specialized; concentrated; exclusive; single-minded",
                "meaning_es": "especializado; dedicado; concentrado; exclusivo",
                "radical": "一",
                "radical_meaning_en": "one",
                "meaning_component": "A hand 寸 rotating a spindle of spun thread; simplified to focused devotion",
                "sound_component": "Historical phonetic zhān",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Originally depicting a spinning spindle handled with extreme steady care; transformed to mean single-minded specialized focus.",
                "visual_mnemonic_story_en": "Focusing every stroke of work exclusively on one single (一) path creates mastery (专).",
                "visual_mnemonic_story_es": "Concentrar cada trazo en una sola (一) meta constante engendra maestría (专).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QNI",
                "traditional": "專"
            },
            {
                "character": "家",
                "pinyin": "jiā",
                "meaning_en": "family; home; master; specialist",
                "meaning_es": "familia; hogar; maestro; especialista de renombre",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (sheltering roof) + 豕 (pig / domestic wealth and family school)",
                "sound_component": "豕 (shǐ / domestic symbol)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A roof 宀 with domestic livestock 豕 beneath; extended to denote a prestigious household, scholastic tradition, or distinguished master.",
                "visual_mnemonic_story_en": "Under the roof (宀) of a scholastic household, a master raises knowledge to become a specialist (家).",
                "visual_mnemonic_story_es": "Bajo el techo (宀) de la escuela o gremio, el virtuoso se corona maestro consumado (家).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JMO",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "One who devotes single-minded focus (专) to master an entire intellectual school or discipline (家) is an expert (专家).",
            "composite_memory_hook_es": "Quien dedica consagración absoluta (专) a dominar una escuela o rama del saber (家) es un experto (专家).",
            "cultural_and_cognitive_roots": "In classical Chinese, 家 denotes philosophical schools (e.g. 儒家 Confucianism, 道家 Daoism) and masters of recognized crafts (画家, 作家).",
            "tone_sandhi_and_pitch_modulation": "Two high level first tones: 'zhuān jiā' (55-55). Maintain steady high melodic ceiling without dropping pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "传", "pinyin": "chuán", "meaning_en": "pass on; transmit", "distinction_note": "Has person radical 亻 on left of 专"},
                {"character": "转", "pinyin": "zhuǎn", "meaning_en": "turn; rotate", "distinction_note": "Has vehicle radical 车 on left of 专"},
                {"character": "冢", "pinyin": "zhǒng", "meaning_en": "mound; tomb", "distinction_note": "Has 冖 cover over 豕 with extra stroke, unlike 家"},
                {"character": "稼", "pinyin": "jià", "meaning_en": "sow grain; crops", "distinction_note": "Has grain radical 禾 on left of 家"}
            ],
            "etymological_cognates": [
                {"character": "师", "pinyin": "shī", "gloss_en": "master; teacher"},
                {"character": "匠", "pinyin": "jiàng", "gloss_en": "artisan; craftsman"},
                {"character": "工", "pinyin": "gōng", "gloss_en": "work; engineer"},
                {"character": "儒", "pinyin": "rú", "gloss_en": "scholar"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "专家 denotes an established specialist or authority with deep technical or academic credentials in a specific discipline.",
            "contrasts": [
                {"id": "1", "compared_word": "专家 vs. 学者", "pinyin": "xuézhě", "analysis": "学者 highlights academic and theoretical research in universities/humanities, whereas 专家 encompasses practical engineering, clinical, or technical masters."},
                {"id": "2", "compared_word": "专家 vs. 行家", "pinyin": "hángjia", "analysis": "行家 emphasizes practical savvy, trade experience, and knack in a commercial market ('这行里的行家'), while 专家 is more formal and authoritative."},
                {"id": "3", "compared_word": "专家 vs. 大师", "pinyin": "dàshī", "analysis": "大师 is an exalted title for pinnacle creative or spiritual giants (e.g. painting, chess), whereas 专家 is a standard professional classification."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着现代生活节奏不断加快，大众对健康的关注度日益提升。各大医院的睡眠医学专家建议，睡前一小时尽量远离电子屏幕，营造昏暗安静的卧室氛围，从而利用人体自然的生理机制平稳进入深度睡眠。",
                "pinyin": "Suízhe xiàndài shēnghuó jiézòu bùduàn jiākuài, dàzhòng duì jiànkāng de guānzhùdù rìyì tíshēng. Gè dà yīyuàn de shuìmián yīxué zhuānjiā jiànyì, shuì qián yī xiǎoshí jǐnliàng yuǎnlí diànzǐ píngmù, yíngzào hūn'àn ānjìng de wòshì fēnwéi, cóng'ér lìyòng réntǐ zìrán de shēnglǐ jīzhì píngwěn jìnrù shēndù shuìmián.",
                "en": "As modern life speeds up, public attention to health steadily climbs. Sleep medicine experts recommend staying away from electronic screens an hour before bed and creating a dim quiet bedroom atmosphere to smoothly enter deep sleep.",
                "es": "Con el ritmo de vida moderno acelerándose, el interés por la salud crece. Expertos en medicina del sueño aconsejan alejarse de las pantallas una hora antes de dormir y procurar un dormitorio tenue y silencioso para conciliar el sueño profundo."
            },
            {
                "id": "#2",
                "hanzi": "在城市规划与环境保护项目中，政府广泛听取了生态学与地质学专家的科学论证。专家们通过大数据模拟分析，提出了兼顾经济发展与绿水青山的多套建设方案，为城市未来的可持续发展奠定了扎实坚实的科学依据。",
                "pinyin": "Zài chéngshì guīhuà yǔ huánjìng bǎohù xiàngmù zhōng, zhèngfǔ guǎngfàn tīngqǔle shēngtàixué yǔ dìzhìxué zhuānjiā de kēxué lùnzhèng. Zhuānjiāmen tōngguò dàshùjù mónǐ fēnxī, tíchūle jiāngù jīngjì fāzhǎn yǔ lǜshuǐ-qīngshān de duō tào jiànshè fāng'àn, wèi chéngshì wèilái de kěchíxù fāzhǎn diàndìngle zhāshi jiānshí de kēxué yījù.",
                "en": "In urban planning and environmental projects, the government widely consulted scientific evaluations from ecological and geological experts. Through big data simulations, specialists proposed balanced plans laying solid scientific ground.",
                "es": "En planes de urbanismo y medio ambiente, las autoridades recabaron dictámenes de expertos en ecología y geología. Mediante simulaciones de macrodatos, los especialistas formularon proyectos equilibrados para garantizar un desarrollo urbano sostenible."
            }
        ]
    },

    # 33 采用
    {
        "id": "33",
        "hanzi": "采用",
        "pinyin": "cǎi yòng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to adopt; employ; apply; introduce (a method, policy, or technology)",
            "es": "adoptar; emplear; utilizar; aplicar (métodos, criterios o tecnologías)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to select and implement or put to use a specific technique, proposal, material, or approach after evaluation",
                "definition_es": "escoger y poner en práctica una determinada técnica, propuesta, material o política tras evaluar su idoneidad",
                "example_phrase": "采用新技术 (adopt new technology)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了减小对心脏的突发惊吓，很多上班族开始采用模拟日出的光线渐亮闹钟来代替刺耳的铃声。",
                "pinyin": "Wèile jiǎnxiǎo duì xīnzàng de tūfā jīngxià, hěnduō shàngbānzú kāishǐ cǎiyòng mónǐ rìchū de guāngxiàn jiànliàng nàozhōng lái dàitì cì'ěr de língshēng.",
                "en": "To lessen sudden fright to the heart, many commuters have begun adopting sunrise-simulating light-gradual alarms instead of harsh bells.",
                "es": "Para mitigar sobresaltos al corazón, muchos oficinistas comenzaron a adoptar alarmas que simulan el amanecer en vez de timbres estridentes."
            },
            {
                "id": "#2",
                "hanzi": "这家环保企业在生产过程中大胆采用可降解材料，极大降低了工业废弃物对自然环境的污染。",
                "pinyin": "Zhè jiā huánbǎo qǐyè zài shēngchǎn guòchéng zhōng dàdǎn cǎiyòng kějiàngjiě cáiliào, jídà jiàngdīle gōngyè fèiqìwù duì zìrán huánjìng de wūrǎn.",
                "en": "This eco-friendly enterprise boldly adopted biodegradable materials during production, tremendously reducing industrial waste pollution.",
                "es": "Esta empresa ecológica adoptó resueltamente materiales biodegradables en su producción, reduciendo con creces los residuos contaminantes."
            }
        ],
        "collocations": [
            {"hanzi": "采用方法", "en": "adopt a method"},
            {"hanzi": "采用技术", "en": "apply / employ technology"},
            {"hanzi": "采用标准", "en": "adopt a standard"},
            {"hanzi": "采用建议", "en": "adopt a recommendation / suggestion"},
            {"hanzi": "广泛采用", "en": "widely adopt / employ extensively"},
            {"hanzi": "决定采用", "en": "decide to adopt"}
        ],
        "idioms": [
            {"hanzi": "采长补短", "pinyin": "cǎi cháng bǔ duǎn", "meaning_en": "adopt others' strengths to make up for one's shortcomings"},
            {"hanzi": "兼收并蓄", "pinyin": "jiān shōu bìng xù", "meaning_en": "absorb and assimilate broadly; embrace everything"},
            {"hanzi": "物尽其用", "pinyin": "wù jìn qí yòng", "meaning_en": "make the best and fullest use of all materials"},
            {"hanzi": "博采众长", "pinyin": "bó cǎi zhòng cháng", "meaning_en": "gather and adopt strengths from many sources"}
        ],
        "character_decomposition": [
            {
                "character": "采",
                "pinyin": "cǎi",
                "meaning_en": "pick; pluck; collect; choose",
                "meaning_es": "recoger; recolectar; seleccionar; escoger",
                "radical": "爫",
                "radical_meaning_en": "claw / hand grasping from above",
                "meaning_component": "爫 (hand reaching down) + 木 (tree branch / fruits)",
                "sound_component": "Pictographic pluck",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A hand 爫 reaching down to pluck ripe fruit or leaves from a tree 木; picking out and selecting the best.",
                "visual_mnemonic_story_en": "A hand reaching from above (爫) plucks select ripe fruits from a tree (木) to gather (采).",
                "visual_mnemonic_story_es": "Una mano descendente (爫) recolecta fruta madura del árbol (木) para escoger lo mejor (采).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "BD",
                "traditional": ""
            },
            {
                "character": "用",
                "pinyin": "yòng",
                "meaning_en": "use; employ; apply; consume",
                "meaning_es": "usar; emplear; aplicar; utilizar",
                "radical": "用",
                "radical_meaning_en": "use",
                "meaning_component": "Depiction of a divinatory turtle shell pierced with strokes, ready to be utilized in ritual",
                "sound_component": "Self-phonetic yòng",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Pictograph of an implement, vessel, or oracle bone being put to active operational use.",
                "visual_mnemonic_story_en": "A framed tool bucket ready in hand to be put to active functional use (用).",
                "visual_mnemonic_story_es": "Una herramienta encuadrada dispuesta para prestar servicio y utilidad inmediata (用).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BQI",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Selectively plucking the best method (采) and putting it into active practice (用) is adopting it (采用).",
            "composite_memory_hook_es": "Recolectar y elegir la opción idónea (采) para darle uso práctico (用) es adoptar o aplicar (采用).",
            "cultural_and_cognitive_roots": "Derived from classical governance and agronomy: selecting (采) proven folk techniques and deploying (用) them across the realm.",
            "tone_sandhi_and_pitch_modulation": "Third tone followed by fourth tone: 'cǎi yòng' (214-51). Dip low with 214 then drop sharply with 51."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "彩", "pinyin": "cǎi", "meaning_en": "color; prize; splendor", "distinction_note": "Has hair/pattern radical 彡 on right of 采"},
                {"character": "踩", "pinyin": "cǎi", "meaning_en": "step on; trample", "distinction_note": "Has foot radical 足 on left of 采"},
                {"character": "甩", "pinyin": "shuǎi", "meaning_en": "swing; fling", "distinction_note": "Bottom stroke bends rightwards like a flicking tail, unlike 用"},
                {"character": "角", "pinyin": "jiǎo", "meaning_en": "horn; corner", "distinction_note": "Has knife-like top slant, unlike squared top of 用"}
            ],
            "etymological_cognates": [
                {"character": "选", "pinyin": "xuǎn", "gloss_en": "choose; select"},
                {"character": "取", "pinyin": "qǔ", "gloss_en": "take; seize"},
                {"character": "使", "pinyin": "shǐ", "gloss_en": "use; deploy"},
                {"character": "行", "pinyin": "xíng", "gloss_en": "put into action"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "采用 implies selecting a policy, measure, method, standard, or material among alternatives and putting it into implementation.",
            "contrasts": [
                {"id": "1", "compared_word": "采用 vs. 使用", "pinyin": "shǐyòng", "analysis": "使用 is generic for operating or using any physical tool, phone, or money ('使用工具'), while 采用 focuses on adopting strategic methods, models, or materials."},
                {"id": "2", "compared_word": "采用 vs. 采取", "pinyin": "cǎiqǔ", "analysis": "采取 collocates primarily with abstract actions, stances, or measures ('采取行动', '采取态度'), whereas 采用 emphasizes concrete systems, techniques, or inputs."},
                {"id": "3", "compared_word": "采用 vs. 采纳", "pinyin": "cǎinà", "analysis": "采纳 specifically means accepting verbal advice, opinions, or proposals from other people ('采纳建议'), whereas 采用 applies to designs and methods."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代智能制造领域，许多工厂纷纷采用全自动机器人流水线来替代繁重的高危人工岗位。这不仅大幅提升了装配精度与产能，还有效避免了工伤事故的发生，为企业带来了显著的竞争优势。",
                "pinyin": "Zài xiàndài zhìnéng zhìzào lǐngyù, xǔduō gōngchǎng fēnfēn cǎiyòng quánzìdòng jīqìrén liúshuǐxiàn lái tìdài fánzhòng de gāowēi réngōng gǎngwèi. Zhè bùjǐn dàfú tíshēngle zhuāngpèi jīngdù yǔ chǎnnéng, hái yǒuxiào bìmiǎnle gōngshāng shìgù de fāshēng, wèi qǐyè dàiláile xiǎnzhù de jìngzhēng yōushì.",
                "en": "In intelligent manufacturing, many factories have adopted fully automated robotic assembly lines to replace hazardous manual posts. This not only elevates precision and capacity but also averts workplace injuries, yielding competitive edge.",
                "es": "En la fabricación inteligente, múltiples fábricas han adoptado líneas automatizadas de robots en sustitución de labores peligrosas. Ello no solo mejora la precisión y la producción, sino que evita percances laborales, generando ventajas competitivas."
            },
            {
                "id": "#2",
                "hanzi": "为了应对全球气候变暖带来的挑战，国际建筑行业正积极采用新型隔热节能材料与自然通风系统。这种绿色低碳设计不仅降低了建筑物夏季制冷的电能消耗，还创造出宜居舒适的室内小气候，深受崇尚环保的现代居民青睐。",
                "pinyin": "Wèile yìngduì quánqiú qìhòu biànnuǎn dàilái de tiǎozhàn, guójì jiànzhù hángyè zhèng jījí cǎiyòng xīnxíng gérè jiénéng cáiliào yǔ zìrán tōngfēng xìtǒng. Zhèzhǒng lǜsè dītàn shèjì bùjǐn jiàngdīle jiànzhùwù xiàjì zhìlěng de diànnéng xiāohào, hái chuàngzào chū yíjū shūshì de shìnèi xiǎoqìhòu, shēnshòu chóngshàng huánbǎo de xiàndài jūmín qīnglài.",
                "en": "To combat global warming challenges, international architects actively adopt novel thermal insulation materials and natural ventilation. Such eco-designs decrease cooling power consumption while creating comfortable indoor microclimates favored by residents.",
                "es": "Ante el reto del calentamiento global, la arquitectura internacional adopta nuevos materiales aislantes y ventilación natural. Estos diseños ecológicos reducen el consumo eléctrico de refrigeración y crean microclimas confortables muy valorados por ciudadanos concienciados."
            }
        ]
    },

    # 34 柔和
    {
        "id": "34",
        "hanzi": "柔和",
        "pinyin": "róu hé",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "gentle; soft; mild; mellow; soothing (light, voice, tone, texture)",
            "es": "suave; blando; apacible; tenue; meloso (luz, voz, tono, textura)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "gentle, mild, and pleasing to the senses without sharpness or glare (of light, color, sound, texture, or temperament)",
                "definition_es": "suave, tenue, templado o agradable a los sentidos sin estridencias (dícese de luz, voz, color o carácter)",
                "example_phrase": "柔和的光线 (gentle / diffused light)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清晨柔和的阳光透过薄窗帘洒在床头，唤醒了沉睡中的身体，让人感到格外舒服惬意。",
                "pinyin": "Qīngchén róuhé de yángguāng tòuguò báo chuānglián sǎ zài chuángtóu, huànxǐngle chénshuì zhōng de shēntǐ, ràng rén gǎndào géwài shūfu qièyì.",
                "en": "Gentle morning sunlight filtered through the thin curtains onto the bedside, gently awakening the sleeping body and making one feel exceptionally cozy.",
                "es": "La tenue luz matinal atravesó el fino visillo sobre la cabecera despertando el cuerpo dormido con una sensación sumamente apacible."
            },
            {
                "id": "#2",
                "hanzi": "心理咨询师用柔和而平缓的语调与来访者交谈，帮助他们逐渐放松紧绷的神经。",
                "pinyin": "Xīnlǐ zīxúnshī yòng róuhé ér pínghuǎn de yǔdiào yǔ láifǎngzhě jiāotán, bāngzhù tāmen zhújiàn fàngsōng jǐnbēng de shénjīng.",
                "en": "The counselor spoke in a gentle and soothing tone with the visitor, helping them gradually relax their tense nerves.",
                "es": "El terapeuta conversó con el visitante en un tono suave y sosegado, ayudándole a relajar paso a paso sus tensos nervios."
            }
        ],
        "collocations": [
            {"hanzi": "柔和的光线", "en": "soft / gentle light"},
            {"hanzi": "声音柔和", "en": "gentle voice / mellow sound"},
            {"hanzi": "色调柔和", "en": "subdued / soft hues"},
            {"hanzi": "目光柔和", "en": "gentle gaze / kind eyes"},
            {"hanzi": "触感柔和", "en": "soft to the touch"},
            {"hanzi": "柔和的音乐", "en": "gentle / soothing music"}
        ],
        "idioms": [
            {"hanzi": "以柔克刚", "pinyin": "yǐ róu kè gāng", "meaning_en": "overcome hardness with softness; subdue brute force by gentle means"},
            {"hanzi": "和风细雨", "pinyin": "hé fēng xì yǔ", "meaning_en": "gentle breeze and mild rain; patient persuasion"},
            {"hanzi": "心平气和", "pinyin": "xīn píng qì hé", "meaning_en": "tranquil mind and even temper; calm and good-humored"},
            {"hanzi": "温柔体贴", "pinyin": "wēn róu tǐ tiē", "meaning_en": "gentle, considerate, and deeply tender"}
        ],
        "character_decomposition": [
            {
                "character": "柔",
                "pinyin": "róu",
                "meaning_en": "soft; pliable; flexible; gentle",
                "meaning_es": "blando; flexible; maleable; suave",
                "radical": "木",
                "radical_meaning_en": "wood / tree",
                "meaning_component": "矛 (spear handle bent pliantly) + 木 (pliant tree twig)",
                "sound_component": "矛 (máo / archaic flex)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A supple tree branch 木 pliable enough to bend without snapping; flexibility and tender softness.",
                "visual_mnemonic_story_en": "A slender wooden branch (木) bending gracefully like a spear shaft (矛) displays softness (柔).",
                "visual_mnemonic_story_es": "La rama tierna del árbol (木) que se comba dócil como asta elástica (矛) personifica la suavidad (柔).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "NHD",
                "traditional": ""
            },
            {
                "character": "和",
                "pinyin": "hé",
                "meaning_en": "harmonious; calm; gentle; peace; and",
                "meaning_es": "armonioso; apacible; templado; paz; y",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "禾 (grain stalks) + 口 (mouth singing or sharing grain)",
                "sound_component": "禾 (hé, grain / phonetic harmony)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Mouth 口 fed harmoniously with seasonal grain 禾; symbolizes peaceful consensus, balance, and mild harmony.",
                "visual_mnemonic_story_en": "Stalks of ripe grain (禾) nourishing every hungry mouth (口) cultivate peaceful harmony (和).",
                "visual_mnemonic_story_es": "Las espigas de trigo (禾) que colman la boca (口) engendran sosiego, calidez y armonía (和).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HDR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pliant bending softness (柔) paired with balanced soothing harmony (和) yields gentle soothing comfort (柔和).",
            "composite_memory_hook_es": "La elasticidad blanda (柔) hermanada con la melodiosa armonía (和) da lugar a una textura o luz apacible y suave (柔和).",
            "cultural_and_cognitive_roots": "Daoist aesthetic principle: softness (柔) endures while brittleness breaks; harmonious moderation (中和) creates timeless elegance.",
            "tone_sandhi_and_pitch_modulation": "Two rising second tones: 'róu hé' (35-35). Rise cleanly across both syllables smoothly."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "揉", "pinyin": "róu", "meaning_en": "rub; knead", "distinction_note": "Has hand radical 扌 on left of 柔"},
                {"character": "桑", "pinyin": "sāng", "meaning_en": "mulberry tree", "distinction_note": "Has three hands 又 over 木, lacking spear 矛"},
                {"character": "私", "pinyin": "sī", "meaning_en": "private; selfish", "distinction_note": "Has 厶 on right of 禾 instead of 口 in 和"},
                {"character": "利", "pinyin": "lì", "meaning_en": "sharp; profit", "distinction_note": "Has knife radical 刂 on right of 禾"}
            ],
            "etymological_cognates": [
                {"character": "温", "pinyin": "wēn", "gloss_en": "warm; mild"},
                {"character": "软", "pinyin": "ruǎn", "gloss_en": "soft; pliable"},
                {"character": "缓", "pinyin": "huǎn", "gloss_en": "gentle; slow"},
                {"character": "顺", "pinyin": "shùn", "gloss_en": "smooth; compliant"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "柔和 describes sensory qualities (lighting, vocal tone, color, melody) or dispositions that are mellow, non-glaring, and gently pleasing.",
            "contrasts": [
                {"id": "1", "compared_word": "柔和 vs. 柔软", "pinyin": "róuruǎn", "analysis": "柔软 specifically describes physical, tactile flexibility and plush softness of touch (e.g. beddings, pillows, wool), whereas 柔和 describes light, sound, and mood."},
                {"id": "2", "compared_word": "柔和 vs. 温和", "pinyin": "wēnhé", "analysis": "温和 focuses primarily on personality, climate/temperature, or medicinal effects ('脾气温和', '气候温和'), while 柔和 is strongly tied to optical and acoustic sensations."},
                {"id": "3", "compared_word": "柔和 vs. 平和", "pinyin": "pínghé", "analysis": "平和 denotes emotional equanimity, balance, and lack of confrontation ('心态平和'), whereas 柔和 is perceptual soothing softness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "室内设计师在布置卧室时，通常偏好采用米黄色等柔和的色彩系统。柔和的光线不仅能缓解视网膜的日间疲劳，更能从心理层面上消除戒备与焦虑，引导身心在宁静温馨的氛围中逐步放松。",
                "pinyin": "Shìnèi shèjìshī zài bùzhì wòshì shí, tōngcháng piānhào cǎiyòng mǐhuángsè děng róuhé de sècǎi xìtǒng. Róuhé de guāngxiàn bùjǐn néng huǎnjiě shìwǎngmó de rìjiān píláo, gèng néng cóng xīnlǐ céngmiàn shàng xiāochú jièbèi yǔ jiāolǜ, yǐndǎo shēnxīn zài níngjìng wēnxīn de fēnwéi zhōng zhúbù fàngsōng.",
                "en": "Interior designers typically prefer soft color palettes like beige when decorating bedrooms. Soft light not only relieves retinal fatigue accumulated during daytime, but also psychologically diffuses tension, guiding mind and body into calm rest.",
                "es": "Los interioristas prefieren gamas suaves como el crema al decorar dormitorios. La luz tenue mitiga la fatiga ocular y disipa la ansiedad a nivel psicológico, invitando al cuerpo y la mente a relajarse en una atmósfera acogedora."
            },
            {
                "id": "#2",
                "hanzi": "暮色降临时，海滩上的风渐渐平息，晚霞为整片海湾披上了一层柔和的金红色轻纱。散步的人们伴着舒缓的浪花声低语交谈，空气中弥漫着宁静的气息，白日里一切喧嚣与烦恼都在这柔和的黄昏景致中融化消散。",
                "pinyin": "Mùsè jiànglín shí, hǎitān shàng de fēng jiànjiàn píngxī, wǎnxiá wèi zhěng piàn hǎiwān pīshàngle yī céng róuhé de jīnhóngsè qīngshā. Sànbù de rénmen bànzhe shūhuǎn de lànghuā shēng dīyǔ jiāotán, kōngqì zhōng mímàn zhe níngjìng de qìxī, báirì lǐ yīqiè xuānxiāo yǔ fánnǎo dōu zài zhè róuhé de huánghūn jǐngzhì zhōng rónghuà xiāosàn.",
                "en": "At dusk, coastal breezes softened, and the sunset cast a gentle veil of gold and crimson over the bay. Strollers whispered along the rhythmic waves, as all daytime hubbub dissolved effortlessly into the soothing twilight landscape.",
                "es": "Al caer el crepúsculo, la brisa marina amainó y el arrebol cubrió la bahía con un velo suave de tonos dorados y rojizos. Los paseantes conversaban al compás de las olas, desvaneciendo las tribulaciones del día en la quietud de la tarde."
            }
        ]
    },

    # 35 愿望
    {
        "id": "35",
        "hanzi": "愿望",
        "pinyin": "yuàn wàng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "wish; desire; aspiration; longing",
            "es": "deseo; anhelo; aspiración; ilusión"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an earnest desire, wish, or aspiration for a particular state of affairs or future outcome to come true",
                "definition_es": "deseo o anhelo vehemente de que se cumpla algo favorable o esperado en el porvenir",
                "example_phrase": "美好的愿望 (cherished / beautiful wish)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每天清晨能在自然光线中舒服地自然醒来，是很多饱受闹钟折磨的上班族最朴素的愿望。",
                "pinyin": "Měitiān qīngchén néng zài zìrán guāngxiàn zhōng shūfu de zìrán xǐnglái, shì hěnduō bǎoshòu nàozhōng zhémó de shàngbānzú zuì pǔsù de yuànwàng.",
                "en": "Being able to wake up comfortably and naturally in morning daylight every day is the most modest wish of many office workers tormented by alarms.",
                "es": "Poder despertarse plácidamente con la luz natural cada mañana es el anhelo más sencillo de multitud de oficinistas martirizados por el despertador."
            },
            {
                "id": "#2",
                "hanzi": "经过多年的刻苦攻读与拼搏，他终于实现了考取重点大学的童年愿望。",
                "pinyin": "Jīngguò duō nián de kèkǔ gōngdú yǔ pīnbó, tā zhōngyú shíxiànle kǎoqǔ zhòngdiǎn dàxué de tóngnián yuànwàng.",
                "en": "After years of assiduous study and hard work, he finally realized his childhood wish of gaining admission into a key university.",
                "es": "Tras años de empeño y estudio tesonero, vio cumplido por fin su sueño de infancia de ingresar en una universidad de prestigio."
            }
        ],
        "collocations": [
            {"hanzi": "实现愿望", "en": "fulfill a wish / realize an aspiration"},
            {"hanzi": "美好愿望", "en": "cherished wish; wonderful hope"},
            {"hanzi": "表达愿望", "en": "express one's desire / wish"},
            {"hanzi": "共同愿望", "en": "shared desire; common aspiration"},
            {"hanzi": "强烈的愿望", "en": "fervent wish; strong longing"},
            {"hanzi": "童年愿望", "en": "childhood wish"}
        ],
        "idioms": [
            {"hanzi": "如愿以偿", "pinyin": "rú yuàn yǐ cháng", "meaning_en": "have one's wish completely fulfilled"},
            {"hanzi": "天从人愿", "pinyin": "tiān cóng rén yuàn", "meaning_en": "Heaven fulfills human wishes; events turn out as hoped"},
            {"hanzi": "事与愿违", "pinyin": "shì yǔ yuàn wéi", "meaning_en": "things turn out contrary to one's wishes"},
            {"hanzi": "梦寐以求", "pinyin": "mèng mèi yǐ qiú", "meaning_en": "crave something even in one's dreams"}
        ],
        "character_decomposition": [
            {
                "character": "愿",
                "pinyin": "yuàn",
                "meaning_en": "wish; willing; desire; honest",
                "meaning_es": "desear; querer; voluntad; anhelo",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "原 (meadow source / sincere plainness) + 心 (inner heart's intent)",
                "sound_component": "原 (yuán, origin / phonetic)",
                "stroke_count": 14,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Heart 心 resting beneath meadow source 原; the honest, unvarnished desire bubbling up from deep within one's soul.",
                "visual_mnemonic_story_en": "From the original spring source (原) of the heart (心) flows sincere willingness and wish (愿).",
                "visual_mnemonic_story_es": "Desde el manantial original (原) del corazón (心) brota el anhelo puro y la voluntad (愿).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MHP",
                "traditional": "願"
            },
            {
                "character": "望",
                "pinyin": "wàng",
                "meaning_en": "look into distance; hope; gaze; expect",
                "meaning_es": "mirar a lo lejos; esperar; contemplar; anhelar",
                "radical": "月",
                "radical_meaning_en": "moon",
                "meaning_component": "亡 (hide / vanish) + 月 (full moon) + 王/𡈼 (person standing on tiptoe to gaze)",
                "sound_component": "Historical phonetic wàng",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A person standing tall on high ground gazing at the distant full moon 月; looking far away with intense longing.",
                "visual_mnemonic_story_en": "Standing tall on tiptoes to gaze toward the moon (月), eyes filled with hopeful longing (望).",
                "visual_mnemonic_story_es": "De puntillas sobre una colina contemplando la luna llena (月), la mirada se llena de anhelo y esperanza (望).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YGB",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A deep heart's intent (愿) looking toward distant lunar heights (望) creates an earnest wish (愿望).",
            "composite_memory_hook_es": "El sincero sentir del corazón (愿) oteando esperanzas lejanas (望) da cuerpo al anhelo o deseo (愿望).",
            "cultural_and_cognitive_roots": "Derived from the ancient poetic custom of gazing at the full moon (望月) while whispering unspoken prayers for reunion and fortune.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'yuàn wàng' (51-51). Execute two crisp authoritative drops."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "原", "pinyin": "yuán", "meaning_en": "origin; meadow", "distinction_note": "Lacks heart radical 心 at bottom of 愿"},
                {"character": "怨", "pinyin": "yuàn", "meaning_en": "resentment; blame", "distinction_note": "Has 夗 at top instead of 原"},
                {"character": "忘", "pinyin": "wàng", "meaning_en": "forget", "distinction_note": "Has 亡 over 心, lacking moon 月"},
                {"character": "妄", "pinyin": "wàng", "meaning_en": "absurd; rash", "distinction_note": "Has 亡 over woman radical 女"}
            ],
            "etymological_cognates": [
                {"character": "希", "pinyin": "xī", "gloss_en": "hope; rare"},
                {"character": "盼", "pinyin": "pàn", "gloss_en": "look forward to"},
                {"character": "祈", "pinyin": "qí", "gloss_en": "pray for"},
                {"character": "求", "pinyin": "qiú", "gloss_en": "seek; beseech"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "愿望 refers to an inner, cherished hope or subjective yearning for happiness, peace, or personal aspirations.",
            "contrasts": [
                {"id": "1", "compared_word": "愿望 vs. 希望", "pinyin": "xīwàng", "analysis": "希望 can act as both verb ('我希望...') and noun ('满怀希望'), whereas 愿望 is predominantly a noun signifying a specific cherished wish."},
                {"id": "2", "compared_word": "愿望 vs. 理想", "pinyin": "lǐxiǎng", "analysis": "理想 denotes grand, rational life ambitions and socio-political ideals ('崇高理想'), whereas 愿望 often reflects immediate, personal sentiments."},
                {"id": "3", "compared_word": "愿望 vs. 欲望", "pinyin": "yùwàng", "analysis": "欲望 carries a strong appetite, instinctive urge, or acquisitive craving ('金钱欲望'), while 愿望 is benign, positive, and gentle."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在孩子纯真的心目中，新年最大的愿望往往不过是得到一件心仪的玩具，或是父母能抽空陪自己去游乐园度过周末。这种简单质朴的心愿，却映射出家庭温暖对童年成长无可替代的珍贵意义。",
                "pinyin": "Zài háizi chúnzhēn de xīnmù zhōng, xīnnián zuìdà de yuànwàng wǎngwǎng búguò shì dédào yī jiàn xīnyí de wánjù, huòshì fùmǔ néng chōukòng péi zìjǐ qù yóulèyuán dùguò zhōumò. Zhèzhǒng jiǎndān zhìpǔ de xīnyuàn, què yìngshè chū jiātíng wēnnuǎn duì tóngnián chéngzhǎng wúkě tìdài de zhēnguì yìyì.",
                "en": "In the innocent eyes of children, the greatest New Year wish is often just getting a favorite toy or spending the weekend at an amusement park with parents. Such simple longings mirror the irreplaceable warmth of family in childhood.",
                "es": "Para el corazón inocente de un niño, el mayor anhelo de Año Nuevo suele ser un juguete soñado o que sus padres le lleven al parque de atracciones. Tan entrañable ilusión refleja el calor familiar insustituible en la infancia."
            },
            {
                "id": "#2",
                "hanzi": "渴望和平与繁荣是全人类跨越国界与种族的共同愿望。历史深刻证明，封闭隔阂只会加剧争端，唯有坚持合作共赢与开放包容，才能让各国人民安居乐业的美好憧憬真正化作生动的现实，携手构建和谐美好的地球家园。",
                "pinyin": "Kěwàng hépíng yǔ fánróng shì quán rénlèi kuàyuè guójiè yǔ zhǒngzú de gòngtóng yuànwàng. Lìshǐ shēnkè zhèngmíng, fēngbì géhé zhǐhuì jiājù zhēngduān, wéiyǒu jiānchí hézuò gòngyíng yǔ kāifàng bāoróng, cáinéng ràng gè guó rénmín ānjū-lèyè de měihǎo chōngjǐng zhēnzhèng huàzuò shēngdòng de xiànshí, xiéshǒu gòujiàn héxié měihǎo de dìqiú jiāyuán.",
                "en": "Longing for peace and prosperity is a shared aspiration of mankind across borders. History proves isolation heightens conflict; only cooperation and open inclusion transform the dream of peaceful living into reality.",
                "es": "El anhelo de paz y bonanza une a toda la humanidad por encima de fronteras. La historia demuestra que el aislamiento agrava disputas; solo la cooperación y la inclusión hacen realidad el sueño de vivir en armonía en nuestro planeta común."
            }
        ]
    },

    # 36 窗帘
    {
        "id": "36",
        "hanzi": "窗帘",
        "pinyin": "chuāng lián",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "window curtain; drapes; window blinds",
            "es": "cortina; visillo; cortinaje de ventana"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a hanging cloth, screen, or drapery used to cover a window to block out light, provide privacy, or decorate an interior",
                "definition_es": "paño o tejido suspendido en una ventana para tamizar la luz solar, preservar la intimidad o decorar el aposento",
                "example_phrase": "拉开窗帘 (draw open the curtains)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "专家建议睡前不要把窗帘拉得过于严实，留出一道缝隙让清晨柔和的阳光洒入房间。",
                "pinyin": "Zhuānjiā jiànyì shuì qián búyào bǎ chuānglián lā de guòyú yánshi, liúchū yī dào fèngxì ràng qīngchén róuhé de yángguāng sǎ rù fángjiān.",
                "en": "Experts suggest not drawing the window curtains shut too tightly before sleep, leaving a small gap for gentle morning light to filter in.",
                "es": "Los especialistas aconsejan no cerrar las cortinas del todo al acostarse, dejando una rendija para que penetre la tenue luz matutina."
            },
            {
                "id": "#2",
                "hanzi": "她轻轻拉上卧室的遮光窗帘，隔绝了窗外繁华街道闪烁的霓虹灯光，安静地躺下入睡。",
                "pinyin": "Tā qīngqīng lāshàng wòshì de zhēguāng chuānglián, géjuéle chuāngwài fánhuá jiēdào shǎnshuò de níhóng dēngguāng, ānjìng de tǎngxià rùshuì.",
                "en": "She gently drew the bedroom blackout curtains shut, blocking out the glittering neon lights of the busy street, and laid down quietly to sleep.",
                "es": "Corrió suavemente las cortinas tupidas del dormitorio, aislando el resplandor de los neones de la concurrida calle para dormir en paz."
            }
        ],
        "collocations": [
            {"hanzi": "拉开窗帘", "en": "draw open the curtains"},
            {"hanzi": "拉上窗帘", "en": "close / draw the curtains"},
            {"hanzi": "遮光窗帘", "en": "blackout curtain"},
            {"hanzi": "百叶窗帘", "en": "Venetian blinds / louver curtain"},
            {"hanzi": "窗帘布", "en": "curtain fabric"},
            {"hanzi": "更换窗帘", "en": "replace window curtains"}
        ],
        "idioms": [
            {"hanzi": "开窗见日", "pinyin": "kāi chuāng jiàn rì", "meaning_en": "open the window to see the bright sun; instant clarity"},
            {"hanzi": "铁幕窗下", "pinyin": "tiě mù chuāng xià", "meaning_en": "behind heavy iron curtains; cloistered secrecy"},
            {"hanzi": "帘卷西风", "pinyin": "lián juǎn xī fēng", "meaning_en": "curtains stirred by autumn west winds; bittersweet wistfulness"},
            {"hanzi": "垂帘听政", "pinyin": "chuí lián tīng zhèng", "meaning_en": "govern from behind the curtain (imperial empress dowager rule)"}
        ],
        "character_decomposition": [
            {
                "character": "窗",
                "pinyin": "chuāng",
                "meaning_en": "window; opening",
                "meaning_es": "ventana; tragaluz; vano",
                "radical": "穴",
                "radical_meaning_en": "cave / hole",
                "meaning_component": "穴 (roof opening/cave) + 囱 (chimney / smoke hole with lattice bars)",
                "sound_component": "囱 (cōng, smoke flue / phonetic)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A cave dwelling opening 穴 with a wooden lattice 囱 to ventilate smoke and admit natural daylight; hence a window.",
                "visual_mnemonic_story_en": "A vent cut into a cave roof (穴) crossed with wooden window grates (囱) lets light through the window (窗).",
                "visual_mnemonic_story_es": "Una abertura en la cueva (穴) cruzada con una celosía (囱) permite que la luz entre por la ventana (窗).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JCHUK",
                "traditional": ""
            },
            {
                "character": "帘",
                "pinyin": "lián",
                "meaning_en": "curtain; screen; banner",
                "meaning_es": "cortina; visillo; biombo; tela suspendida",
                "radical": "巾",
                "radical_meaning_en": "cloth / towel",
                "meaning_component": "穴 (window aperture) + 巾 (hanging cloth / textile drapery)",
                "sound_component": "廉 (lián, phonetic in full traditional form 簾)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A piece of cloth 巾 hung over a window aperture 穴 to shield against draft and sunlight; a hanging drapery screen.",
                "visual_mnemonic_story_en": "A soft cloth fabric (巾) suspended across an aperture (穴) hangs gracefully as a curtain (帘).",
                "visual_mnemonic_story_es": "Una tela de paño (巾) suspendida sobre el vano (穴) actúa como cortina protectora (帘).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JCLB",
                "traditional": "簾"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A window opening (窗) fitted with a protective hanging cloth (帘) forms the household curtain (窗帘).",
            "composite_memory_hook_es": "El vano de la ventana (窗) cubierto por un paño suspendido (帘) compone la cortina (窗帘).",
            "cultural_and_cognitive_roots": "Traditional courtyard houses used bamboo screens (竹帘) in summer and silk padded drapes (布帘) in winter to regulate temperature and social privacy.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by second tone: 'chuāng lián' (55-35). Hold high 55, then glide up smoothly to 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "窜", "pinyin": "cuàn", "meaning_en": "flee; scurry", "distinction_note": "Has rat 鼠 at bottom under 穴 instead of 囱 in 窗"},
                {"character": "窟", "pinyin": "kū", "meaning_en": "hole; cave", "distinction_note": "Has 屈 under 穴"},
                {"character": "市", "pinyin": "shì", "meaning_en": "market; city", "distinction_note": "Single character with 亠 over 巾, lacking 穴 in 帘"},
                {"character": "希", "pinyin": "xī", "meaning_en": "hope", "distinction_note": "Has 乂 over cloth 巾"}
            ],
            "etymological_cognates": [
                {"character": "幕", "pinyin": "mù", "gloss_en": "curtain; theatrical drape"},
                {"character": "帐", "pinyin": "zhàng", "gloss_en": "canopy; tent; screen"},
                {"character": "幔", "pinyin": "màn", "gloss_en": "hanging drapery"},
                {"character": "屏", "pinyin": "píng", "gloss_en": "folding screen"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "窗帘 refers specifically to window drapes or curtains meant for shading light and protecting indoor privacy.",
            "contrasts": [
                {"id": "1", "compared_word": "窗帘 vs. 门帘", "pinyin": "ménlián", "analysis": "门帘 is a curtain hung at a doorway or entrance portal to block cold drafts or insects, whereas 窗帘 is hung at windows."},
                {"id": "2", "compared_word": "窗帘 vs. 帷幕", "pinyin": "wéimù", "analysis": "帷幕 refers to large-scale theatrical curtains, formal stage drapes, or figurative political curtains ('拉开帷幕'), not domestic window curtains."},
                {"id": "3", "compared_word": "窗帘 vs. 百叶窗", "pinyin": "bǎiyèchuāng", "analysis": "百叶窗 refers to slatted blinds (made of wood, aluminum, or plastic), while 窗帘 broadly denotes fabric drapes or curtains in general."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "现代智能家居系统赋予了窗帘崭新的科技内涵。用户可以通过手机软件预设开启时间，每天清晨窗帘便会自动缓缓拉开一道缝隙，让初升的旭日柔和地唤醒睡眠者，帮助人体生物钟实现平稳的自然过渡。",
                "pinyin": "Xiàndài zhìnéng jiājū xìtǒng fùyǔle chuānglián zhǎnxīn de kējì nèihán. Yònghù kěyǐ tōngguò shǒujī ruǎnjiàn yùshè kāiqǐ shíjiān, měitiān qīngchén chuānglián biàn huì zìdòng huǎnhuǎn lākāi yī dào fèngxì, ràng chūshēng de xùrì róuhé de huànxǐng shuìmiánzhě, bāngzhù réntǐ shēngwùzhōng shíxiàn píngwěn de zìrán guòdù.",
                "en": "Modern smart home systems give window curtains fresh technological utility. Users preset opening times via smartphone apps, allowing curtains to automatically part slightly at dawn, letting sunrise gently awaken the sleeper.",
                "es": "La domótica moderna confiere a las cortinas un papel tecnológico puntero. Mediante aplicaciones móviles, se programa su apertura para que el sol matutino despierte plácidamente al durmiente, regulando el reloj biológico."
            },
            {
                "id": "#2",
                "hanzi": "老宅书房的那副厚实亚麻窗帘，见证了祖父伏案著书的数十载光阴。每当午后斜阳照耀，拉上一半窗帘便能让斑驳柔和的光影洒在满架线装古籍上。微风吹过，窗帘轻轻摇曳，伴着浓郁的墨香，勾勒出一幅宁静深邃的传统文人生活图景。",
                "pinyin": "Lǎozhái shūfáng de nà fù hòushí yàmá chuānglián, jiànzhèngle zǔfù fú'àn zhùshū de shùshí zǎi guāngyīn. Měidāng wǔhòu xiéyáng zhàoyào, lāshàng yībàn chuānglián biàn néng ràng bānbó róuhé de guāngyǐng sǎ zài mǎnjià xiànzhuāng gǔjí shàng. Wēifēng chuīguò, chuānglián qīngqīng yáoyè, bànzhe nóngyù de mòxiāng, gōulè chū yī fú níngjìng shēnsuì de chuántǒng wénrén shēnghuó tújǐng.",
                "en": "The thick linen curtains in the ancestral study witnessed decades of grandfather writing books. Drawing them halfway diffused gentle afternoon shadows over antique shelves, drifting with ink fragrance into an aura of scholarly peace.",
                "es": "Las gruesas cortinas de lino del viejo despacho presenciaron décadas de labor literaria del abuelo. Correrlas a medias matizaba sombras suaves sobre volúmenes antiguos, trazando un cuadro sereno de aromas de tinta y calma letrada."
            }
        ]
    },

    # 37 市场
    {
        "id": "37",
        "hanzi": "市场",
        "pinyin": "shì chǎng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "market; marketplace; commercial arena; market demand",
            "es": "mercado; plaza de abastos; ámbito comercial; demanda de mercado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a physical or virtual commercial arena where goods, commodities, and services are traded between buyers and sellers",
                "definition_es": "espacio físico o virtual donde se compran y venden mercancías, bienes o servicios",
                "example_phrase": "开拓海外市场 (open up overseas markets)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the collective demand and commercial purchasing potential for a particular product category",
                "definition_es": "la demanda colectiva y potencial comercial de un determinado tipo de producto o servicio",
                "example_phrase": "市场潜力巨大 (tremendous market potential)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "敏锐的商家洞察到现代人对健康唤醒的迫切需求，在市场上推出了各式各样模拟自然光线的智能闹钟。",
                "pinyin": "Mǐnruì de shāngjiā dòngchá dào xiàndàirén duì jiànkāng huànxǐng de pòqiè xūqiú, zài shìchǎng shàng tuīchūle gèshì-gèyàng mónǐ zìrán guāngxiàn de zhìnéng nàozhōng.",
                "en": "Keen merchants discerned modern people's urgent need for healthy wake-ups and launched various smart alarms simulating natural daylight onto the market.",
                "es": "Comerciantes perspicaces detectaron la necesidad de un despertar saludable y lanzaron al mercado despertadores inteligentes que simulan la luz natural."
            },
            {
                "id": "#2",
                "hanzi": "面对日趋激烈的国际竞争，企业唯有不断加大技术创新投入，才能在全球市场上立于不败之地。",
                "pinyin": "Miànduì rìqū jīliè de guójì jìngzhēng, qǐyè wéiyǒu bùduàn jiādà jìshù chuàngxīn tóurù, cáinéng zài quánqiú shìchǎng shàng lìyú búbài zhī dì.",
                "en": "Facing increasingly fierce international competition, enterprises can remain invincible in the global market only by continually increasing technological innovation.",
                "es": "Ante la encarnizada competencia internacional, las empresas solo se mantendrán invictas en el mercado mundial redoblando su inversión en innovación."
            }
        ],
        "collocations": [
            {"hanzi": "开拓市场", "en": "expand / open up the market"},
            {"hanzi": "市场需求", "en": "market demand"},
            {"hanzi": "市场份额", "en": "market share"},
            {"hanzi": "国际市场", "en": "international market"},
            {"hanzi": "市场准入", "en": "market access"},
            {"hanzi": "市场竞争", "en": "market competition"}
        ],
        "idioms": [
            {"hanzi": "门庭若市", "pinyin": "mén tíng ruò shì", "meaning_en": "courtyard bustling like a crowded marketplace; busy with visitors"},
            {"hanzi": "招摇过市", "pinyin": "zhāo yáo guò shì", "meaning_en": "parade boastfully through the streets to attract attention"},
            {"hanzi": "日中为市", "pinyin": "rì zhōng wéi shì", "meaning_en": "gather at noon for marketing (ancient trade custom)"},
            {"hanzi": "市场繁荣", "pinyin": "shì chǎng fán róng", "meaning_en": "flourishing market and thriving commercial activity"}
        ],
        "character_decomposition": [
            {
                "character": "市",
                "pinyin": "shì",
                "meaning_en": "market; city; trade; municipality",
                "meaning_es": "mercado; ciudad; comercio; municipio",
                "radical": "巾",
                "radical_meaning_en": "cloth",
                "meaning_component": "亠 (city gate roof) + 巾 (market trade banner)",
                "sound_component": "Pictographic trading post banner",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A trading flag 巾 flying high over the town pavilion 亠 where merchants gathered to barter; later denoting city and market.",
                "visual_mnemonic_story_en": "Under a market roof (亠), trade banners (巾) flutter to welcome merchants to the market (市).",
                "visual_mnemonic_story_es": "Bajo el pabellón comunal (亠), el estandarte textil (巾) anuncia la plaza comercial y mercado (市).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YBL",
                "traditional": ""
            },
            {
                "character": "场",
                "pinyin": "chǎng",
                "meaning_en": "open ground; field; threshing floor; scene",
                "meaning_es": "campo; plaza; explanada; era; escenario",
                "radical": "土",
                "radical_meaning_en": "earth / ground",
                "meaning_component": "土 (earth/ground) + 𠃓/昜 (open sunlight shining broadly)",
                "sound_component": "昜 (yáng, sunlit open / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "An open leveled ground of earth 土 warmed by sunshine where grain was threshed and people assembled for public events.",
                "visual_mnemonic_story_en": "A wide plot of leveled earth (土) bathed in open sunlight serves as a public assembly field (场).",
                "visual_mnemonic_story_es": "Una explanada de tierra llana (土) al sol abierto que sirve de era, plaza o escenario (场).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "GNSH",
                "traditional": "場"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A civic trading center (市) situated on a broad public gathering ground (场) constitutes a market (市场).",
            "composite_memory_hook_es": "El comercio urbano (市) celebrado en una explanada o plaza comunal (场) forma el mercado (市场).",
            "cultural_and_cognitive_roots": "From the ancient Zhou Dynasty 'well-field' system: farmers gathered at noon on public threshing grounds (场) to trade surpluses (市).",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by third tone: 'shì chǎng' (51-214). Sharp initial fall dropping into a full low-dip third tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "布", "pinyin": "bù", "meaning_en": "cloth; spread", "distinction_note": "Has 𠂇 at top instead of 亠 in 市"},
                {"character": "帅", "pinyin": "shuài", "meaning_en": "commander; handsome", "distinction_note": "Has 刂-like stroke on left of 巾"},
                {"character": "扬", "pinyin": "yáng", "meaning_en": "raise; scatter", "distinction_note": "Has hand radical 扌 on left instead of earth 土 in 场"},
                {"character": "汤", "pinyin": "tāng", "meaning_en": "soup; hot water", "distinction_note": "Has water radical 氵 on left"}
            ],
            "etymological_cognates": [
                {"character": "商", "pinyin": "shāng", "gloss_en": "commerce; merchant"},
                {"character": "贾", "pinyin": "gǔ", "gloss_en": "trader; goods"},
                {"character": "市", "pinyin": "shì", "gloss_en": "fair; marketplace"},
                {"character": "坊", "pinyin": "fāng", "gloss_en": "workshop; urban quarter"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "市场 encompasses both concrete physical marketplaces (farmer's market, supermarket) and abstract commercial macroeconomic systems.",
            "contrasts": [
                {"id": "1", "compared_word": "市场 vs. 商场", "pinyin": "shāngchǎng", "analysis": "商场 specifically refers to a large physical commercial department store or modern shopping mall ('去商场购物'), whereas 市场 can refer to abstract economic demand ('股票市场', '全球市场')."},
                {"id": "2", "compared_word": "市场 vs. 集市", "pinyin": "jíshì", "analysis": "集市 denotes traditional rural periodic bazaars or country fairs, whereas 市场 is the modern comprehensive economic term."},
                {"id": "3", "compared_word": "市场 vs. 行业", "pinyin": "hángyè", "analysis": "行业 categorizes a specific domain of trade/industry (e.g. IT, finance), while 市场 reflects trading transactions and consumer demand."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着消费者对睡眠健康认知的不断深化，全球助眠产品市场迎来爆发式增长。从智能香薰机到光照唤醒灯，各类高科技睡眠产品层出不穷，精准切中都市职场人群的痛点，展现出巨大的市场增长潜力。",
                "pinyin": "Suízhe xiāofèizhě duì shuìmián jiànkāng rènzhī de bùduàn shēnhuà, quánqiú zhùmián chǎnpǐn shìchǎng yínglái bàofāshì zēngzhǎng. Cóng zhìnéng xiāngxūnjī dào guāngzhào huànxǐngdēng, gèlèi gāokējì shuìmián chǎnpǐn céngchū-bùqióng, jīngzhǔn qièzhòng dūshì zhíchǎng rénqún de tòngdiǎn, zhǎnxiàn chū jùdà de shìchǎng zēngzhǎng qiánlì.",
                "en": "With deepening consumer awareness of sleep health, the global sleep-aid market is experiencing explosive growth. From aromatherapy diffusers to wake-up lights, diverse gadgets emerge continuously, showing immense market potential.",
                "es": "Con el aumento de la conciencia sobre la salud del sueño, el mercado global de artículos de descanso vive un auge espectacular. Desde difusores inteligentes hasta lámparas de amanecer, surgen productos que muestran un enorme potencial de mercado."
            },
            {
                "id": "#2",
                "hanzi": "开放有序的市场环境是激发实体经济活力的根本保障。政府部门通过持续优化营商环境、打破行业垄断壁垒，有效保护了中小型创新企业的合法权益，促使优质资源在全球市场大循环中实现更加高效的配置。",
                "pinyin": "Kāifàng yǒuxù de shìchǎng huánjìng shì jīfā shítǐ jīngjì huólì de gēnběn bǎozhàng. Zhèngfǔ bùmén tōngguò chíxù yōuhuà yíngshāng huánjìng, dǎpò hángyè lǒngduàn bìlěi, yǒuxiào bǎohùle zhōng-xiǎoxíng chuàngxīn qǐyè de héfǎ quányì, cùshǐ yōuzhì zīyuán zài quánqiú shìchǎng dàxúnhuán zhōng shíxiàn gèngjiā gāoxiào de pèizhì.",
                "en": "An open and orderly market environment is the fundamental guarantee for vitalizing the real economy. By optimizing business environments and lowering barriers, governments protect small innovators and allocate resources efficiently.",
                "es": "Un entorno de mercado abierto y ordenado apuntala la economía productiva. Al mejorar las condiciones comerciales y suprimir monopolios, las autoridades tutelan a pequeñas empresas innovadoras y asignan recursos con suma eficiencia."
            }
        ]
    },

    # 38 产品
    {
        "id": "38",
        "hanzi": "产品",
        "pinyin": "chǎn pǐn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "product; merchandise; goods; manufactured output",
            "es": "producto; mercancía; artículo fabricado; bien producido"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "tangible goods, items, or commercial services manufactured, processed, or developed to satisfy market consumer needs",
                "definition_es": "artículo manufacturado, bien material o servicio elaborado para satisfacer necesidades en el mercado",
                "example_phrase": "电子产品 (electronic products / gadgets)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "科研团队历时两年研发出这款新型助眠产品，能通过渐进式柔和光线模拟大自然的日出过程。",
                "pinyin": "Kēyán tuánduì lìshí liǎng nián yánfā chū zhè kuǎn xīnxíng zhùmián chǎnpǐn, néng tōngguò jiànjìnshì róuhé guāngxiàn mónǐ dàzìrán de rìchū guòchéng.",
                "en": "The research team spent two years developing this new sleep-aid product, which simulates nature's sunrise through progressive gentle light.",
                "es": "El equipo científico dedicó dos años a concebir este nuevo producto para dormir, que simula el amanecer natural con luz suave progresiva."
            },
            {
                "id": "#2",
                "hanzi": "只有严格把控每一个生产环节的产品质量，企业才能在激烈的市场竞争中赢得消费者的信赖。",
                "pinyin": "Zhǐyǒu yángé bǎkòng měi yī gè shēngchǎn huánjié de chǎnpǐn zhìliàng, qǐyè cáinéng zài jīliè de shìchǎng jìngzhēng zhōng yíngdé xiāofèizhě de xìnlài.",
                "en": "Only by strictly controlling product quality at every production phase can an enterprise win consumer trust amid fierce market competition.",
                "es": "Solo supervisando con rigor la calidad del producto en cada eslabón productivo puede la empresa granjearse la lealtad del consumidor."
            }
        ],
        "collocations": [
            {"hanzi": "产品质量", "en": "product quality"},
            {"hanzi": "研发产品", "en": "research and develop a product"},
            {"hanzi": "产品设计", "en": "product design"},
            {"hanzi": "电子产品", "en": "electronic products"},
            {"hanzi": "产品线", "en": "product line"},
            {"hanzi": "推广产品", "en": "promote / market a product"}
        ],
        "idioms": [
            {"hanzi": "优胜劣汰", "pinyin": "yōu shèng liè tài", "meaning_en": "survival of the fittest; superior wins and inferior is weeded out"},
            {"hanzi": "品学兼优", "pinyin": "pǐn xué jiān yōu", "meaning_en": "excelling in both moral character and academic learning"},
            {"hanzi": "推陈出新", "pinyin": "tuī chén chū xīn", "meaning_en": "weed through the old to bring forth the new"},
            {"hanzi": "价廉物美", "pinyin": "jià lián wù měi", "meaning_en": "excellent quality at a modest price"}
        ],
        "character_decomposition": [
            {
                "character": "产",
                "pinyin": "chǎn",
                "meaning_en": "produce; give birth; output; property",
                "meaning_es": "producir; engendrar; parir; bienes; producción",
                "radical": "亠",
                "radical_meaning_en": "lid / roof",
                "meaning_component": "A newborn plant growing out of fertile soil; simplified from 產",
                "sound_component": "Historical phonetic component",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Depicts a living plant sprouting forth and bearing fruit; represents giving birth, producing, yield, and manufactured output.",
                "visual_mnemonic_story_en": "Sprouts rising out of fertile land yielding harvest produce (产).",
                "visual_mnemonic_story_es": "Tallos que brotan de tierra fértil rindiendo cosecha y producción (产).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "YHH",
                "traditional": "產"
            },
            {
                "character": "品",
                "pinyin": "pǐn",
                "meaning_en": "goods; quality; grade; evaluate; taste",
                "meaning_es": "mercancía; calidad; grado; degustar; catar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "Three mouths 口 stacked together representing many vessels or people tasting and judging items",
                "sound_component": "Ideographic cluster of mouths evaluating goods",
                "stroke_count": 9,
                "composition_type": "品字结构",
                "etymology_and_mnemonic": "Three mouths 口 arranged in a pyramid, depicting multiple judges evaluating, savoring, and grading the quality of merchandise.",
                "visual_mnemonic_story_en": "Three critical mouths (口) sample and appraise goods to ensure certified grade and quality (品).",
                "visual_mnemonic_story_es": "Tres bocas (口) que degustan y evalúan mercancías para calibrar su calidad y categoría (品).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RRR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Goods produced through human labor (产) inspected and certified for consumer taste (品) form a product (产品).",
            "composite_memory_hook_es": "Bienes engendrados o producidos (产) cuya calidad pasa la prueba de los evaluadores (品) integran un producto (产品).",
            "cultural_and_cognitive_roots": "Derived from ancient guild standards where newly produced items (产) had to pass threefold taste/grade scrutiny (品) before reaching public trade.",
            "tone_sandhi_and_pitch_modulation": "Two third tones in succession: 'chǎn pǐn' transforms via tone sandhi into (35-214). Pronounce 'chán pǐn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "严", "pinyin": "yán", "meaning_en": "strict; severe", "distinction_note": "Has two horizontal bars at top, unlike 产"},
                {"character": "立", "pinyin": "lì", "meaning_en": "stand; erect", "distinction_note": "Bottom horizontal stroke is straight without downward sweep"},
                {"character": "器", "pinyin": "qì", "meaning_en": "utensil; vessel", "distinction_note": "Has dog 犬 enclosed by four mouths 口"},
                {"character": "晶", "pinyin": "jīng", "meaning_en": "crystal; glittering", "distinction_note": "Composed of three suns 日, not mouths 口"}
            ],
            "etymological_cognates": [
                {"character": "物", "pinyin": "wù", "gloss_en": "thing; commodity"},
                {"character": "货", "pinyin": "huò", "gloss_en": "goods; merchandise"},
                {"character": "商", "pinyin": "shāng", "gloss_en": "trade; commodity"},
                {"character": "具", "pinyin": "jù", "gloss_en": "tool; appliance"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "产品 emphasizes the output of manufacturing, software development, or industrial processing designed for commercial utility.",
            "contrasts": [
                {"id": "1", "compared_word": "产品 vs. 商品", "pinyin": "shāngpǐn", "analysis": "商品 specifically stresses goods circulating in monetary trade on the market, while 产品 emphasizes the manufactured item itself (even before selling)."},
                {"id": "2", "compared_word": "产品 vs. 用品", "pinyin": "yòngpǐn", "analysis": "用品 denotes items grouped by everyday utility function (e.g. 办公用品, 生活用品), whereas 产品 is a broader industrial category."},
                {"id": "3", "compared_word": "产品 vs. 作品", "pinyin": "zuòpǐn", "analysis": "作品 refers to creative, artistic, literary, or intellectual works (books, paintings, symphonies), while 产品 refers to commercial/industrial output."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代科技企业中，优秀的产品经理必须始终将用户体验置于首位。一款成功的科技硬件产品不仅需要具备出色的工业设计与稳定的功能表现，更应融入对当代人生活痛点的人文关怀，让科技真正润物无声地服务于人。",
                "pinyin": "Zài xiàndài kējì qǐyè zhōng, yōuxiù de chǎnpǐn jīnglǐ bìxū shǐzhōng jiāng yònghù tǐyàn zhìyú shǒuwèi. Yī kuǎn chénggōng de kējì yìngjiàn chǎnpǐn bùjǐn xūyào jùbèi chūsè de gōngyè shèjì yǔ wěndìng de gōngnéng biǎoxiàn, gèng yīng róngrù duì dāngdàirén shēnghuó tòngdiǎn de rénwén guānhuái, ràng kējì zhēnzhèng rùnwù-wúshēng de fúwù yú rén.",
                "en": "In tech firms, great product managers prioritize user experience above all. A successful tech hardware product demands exceptional industrial design, stable performance, and humane care addressing daily pain points.",
                "es": "En las tecnológicas, los jefes de producto priorizan la experiencia del usuario. Un producto de hardware exitoso conjuga un diseño depurado, estabilidad funcional y sensibilidad humana hacia los problemas cotidianos."
            },
            {
                "id": "#2",
                "hanzi": "随着全球绿色低碳消费风潮的兴起，节能环保型产品正迅速占据各大消费市场的主流地位。制造厂商积极更新工艺，减少产品在整个生命周期中的能源消耗与碳排放，不仅履行了企业社会责任，也塑造了卓越的品牌形象。",
                "pinyin": "Suízhe quánqiú lǜsè dītàn xiāofèi fēngcháo de xīngqǐ, jiénéng huánbǎoxíng chǎnpǐn zhèng xùnsù zhànjù gè dà xiāofèi shìchǎng de zhǔliú dìwèi. Zhìzào chǎngshāng jījí gēngxīn gōngyì, jiǎnshǎo chǎnpǐn zài zhěnggè shēngmìng zhōuqī zhōng de néngyuán xiāohào yǔ tànpáifàng, bùjǐn lǚxíngle qǐyè shèhuì zérèn, yě shùzàole zhuóyuè de pǐnpái xíngxiàng.",
                "en": "With the rise of green consumption, eco-friendly products are rapidly dominating mainstream markets. Manufacturers actively upgrade processes to cut life-cycle energy consumption and carbon emissions, fulfilling social duties while elevating brand image.",
                "es": "Con el auge del consumo ecológico, los productos energéticamente sostenibles dominan el mercado. Los fabricantes renuevan sus procesos recortando emisiones y huella de carbono a lo largo del ciclo vital del producto, forjando un prestigio ejemplar."
            }
        ]
    },

    # 39 模仿
    {
        "id": "39",
        "hanzi": "模仿",
        "pinyin": "mó fǎng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to imitate; mimic; emulate; model after; copy",
            "es": "imitar; remedar; copiar; emular; reproducir pautas"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to copy, simulate, or model one's behavior, style, sound, or mechanism after an existing example or natural phenomenon",
                "definition_es": "reproducir o copiar adrede los ademanes, el aspecto, el funcionamiento o el sonido de un modelo natural o ajeno",
                "example_phrase": "模仿自然声音 (mimic natural sounds)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "新型健康闹钟通过模仿大自然中鸟鸣和清泉的流动声，让人们在清晨舒缓地苏醒过来。",
                "pinyin": "Xīnxíng jiànkāng nàozhōng tōngguò mófǎng dàzìrán zhōng niǎomíng hé qīngquán de liúdòng shēng, ràng rénmen zài qīngchén shūhuǎn de sūxǐng guòlái.",
                "en": "New wellness alarms awaken people soothingly in the morning by mimicking birdsong and flowing springs found in nature.",
                "es": "Los nuevos despertadores saludables despiertan a las personas con suavidad matutina imitando el trino de pájaros y el fluir de manantiales."
            },
            {
                "id": "#2",
                "hanzi": "儿童在语言学习的初期阶段，主要通过大量模仿父母的语音和语调来掌握日常交流表达。",
                "pinyin": "Értóng zài yǔyán xuéxí de chūqī jiēduàn, zhǔyào tōngguò dàliàng mófǎng fùmǔ de yǔyīn hé yǔdiào lái zhǎngwò rìcháng jiāoliú biǎodá.",
                "en": "In early stages of language acquisition, children master daily communication expressions mainly through mimicking parents' pronunciation and intonation.",
                "es": "En fases tempranas de adquisición lingüística, los niños dominan la expresión cotidiana imitando ampliamente la entonación de sus padres."
            }
        ],
        "collocations": [
            {"hanzi": "模仿能力", "en": "imitative ability / capacity to mimic"},
            {"hanzi": "盲目模仿", "en": "blindly imitate"},
            {"hanzi": "模仿声音", "en": "mimic sounds / voices"},
            {"hanzi": "刻意模仿", "en": "deliberately emulate / imitate"},
            {"hanzi": "模仿动作", "en": "mimic movements / actions"},
            {"hanzi": "善于模仿", "en": "be good at imitating"}
        ],
        "idioms": [
            {"hanzi": "东施效颦", "pinyin": "dōng shī xiào pín", "meaning_en": "blindly mimic others with ridiculous and grotesque results"},
            {"hanzi": "惟妙惟肖", "pinyin": "wéi miào wéi xiào", "meaning_en": "imitated or portrayed with remarkable fidelity and lifelikeness"},
            {"hanzi": "鹦鹉学舌", "pinyin": "yīng wǔ xué shé", "meaning_en": "parrot others' words without genuine comprehension"},
            {"hanzi": "生搬硬套", "pinyin": "shēng bān yìng tào", "meaning_en": "mechanically copy and apply rules without adapting to context"}
        ],
        "character_decomposition": [
            {
                "character": "模",
                "pinyin": "mó",
                "meaning_en": "mold; pattern; model; standard",
                "meaning_es": "molde; patrón; modelo; pauta",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden casting mold) + 莫 (dusk / phonetic casting frame)",
                "sound_component": "莫 (mò, dusk / phonetic)",
                "stroke_count": 14,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A wooden mold 木 used by artisans to cast duplicates into uniform shape; hence a model, archetype, or standard pattern.",
                "visual_mnemonic_story_en": "Carving wood (木) into a prototype mold (莫) allows accurate reproduction of models (模).",
                "visual_mnemonic_story_es": "Tallar madera (木) para hacer un molde maestro (莫) permite reproducir fielmente un modelo (模).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "DTAK",
                "traditional": ""
            },
            {
                "character": "仿",
                "pinyin": "fǎng",
                "meaning_en": "resemble; imitate; copy; like",
                "meaning_es": "parecerse; imitar; asemejarse; copiar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / human action) + 方 (square / standard boundary)",
                "sound_component": "方 (fāng, square / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 aligning gestures according to the square measurements 方 of an existing archetype; imitating.",
                "visual_mnemonic_story_en": "A person (亻) shaping behavior to fit the exact four-corner frame (方) of a teacher imitates (仿).",
                "visual_mnemonic_story_es": "Una persona (亻) que ajusta sus ademanes al patrón cuadrado (方) del maestro imita con destreza (仿).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "OYHS",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Taking a standard archetype mold (模) and having a person copy its shape (仿) is imitating (模仿).",
            "composite_memory_hook_es": "Tomar un molde patrón (模) y hacer que la persona reproduzca su diseño (仿) es imitar (模仿).",
            "cultural_and_cognitive_roots": "Bionics (仿生学): human engineering has historically advanced by observing and copying flight, acoustics, and camouflage from nature.",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by third tone: 'mó fǎng' (35-214). Smooth rising glide followed by low dipping third tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "摸", "pinyin": "mō", "meaning_en": "touch; feel; grope", "distinction_note": "Has hand radical 扌 on left instead of wood 木 in 模"},
                {"character": "膜", "pinyin": "mó", "meaning_en": "membrane; film", "distinction_note": "Has flesh radical 月 on left"},
                {"character": "访", "pinyin": "fǎng", "meaning_en": "visit; interview", "distinction_note": "Has speech radical 讠 on left instead of person 亻 in 仿"},
                {"character": "防", "pinyin": "fáng", "meaning_en": "defend; guard", "distinction_note": "Has mound radical 阝 on left"}
            ],
            "etymological_cognates": [
                {"character": "拟", "pinyin": "nǐ", "gloss_en": "simulate; draft"},
                {"character": "抄", "pinyin": "chāo", "gloss_en": "copy; transcribe"},
                {"character": "效", "pinyin": "xiào", "gloss_en": "emulate; effect"},
                {"character": "学", "pinyin": "xué", "gloss_en": "study; learn by imitation"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "模仿 involves actively observing an external model (behavior, speech, nature) and reproducing its characteristics.",
            "contrasts": [
                {"id": "1", "compared_word": "模仿 vs. 模拟", "pinyin": "mónǐ", "analysis": "模拟 emphasizes technical simulation, scientific modeling, or mock testing (e.g. 模拟考试, 模拟飞行), while 模仿 leans toward human or artistic imitation."},
                {"id": "2", "compared_word": "模仿 vs. 抄袭", "pinyin": "chāoxí", "analysis": "抄袭 carries strong negative legal and moral condemnation for plagiarizing essays, songs, or patents, whereas 模仿 can be a neutral learning method."},
                {"id": "3", "compared_word": "模仿 vs. 效仿", "pinyin": "xiàofǎng", "analysis": "效仿 is more formal, often describing following an admirable historical role model or policy precedent ('效仿先贤')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "仿生学是一门建立在向大自然求教基础上的前沿交叉学科。科学家通过深入观察与模仿鸟类飞行的羽翼结构、海豚游动的流线体态，成功研制出阻力极小的超高速飞行器和潜艇，极大推动了现代交通工程的革新跨越。",
                "pinyin": "Fǎngshēngxué shì yī mén jiànlì zài xiàng dàzìrán qiújiào jīchǔ shàng de qiányán jiāochā xuékē. Kēxuéjiā tōngguò shēnrù guānchá yǔ mófǎng niǎolèi fēixíng de yǔyì jiégòu, hǎitún yóudòng de liúxiàntǐ tài, chénggōng yánzhì chū zǔlì jí xiǎo de chāogāosù fēixíngqì hé qiántǐng, jídà tuīdòngle xiàndài jiāotōng gōngchéng de géxīn kuàyuè.",
                "en": "Bionics is a frontier discipline built on learning from nature. By observing and mimicking birds' wing structures and dolphins' streamlined bodies, scientists engineered aircraft and submersibles with minimal drag, revolutionizing transit.",
                "es": "La biónica es una disciplina puntera nacida de aprender de la naturaleza. Imitando el diseño de las alas de aves y la silueta hidrodinámica de delfines, los científicos concibieron naves y sumergibles que reducen la resistencia revolucionando el transporte."
            },
            {
                "id": "#2",
                "hanzi": "初涉艺术创作的青年画师，往往需要经历一段临摹大师经典的模仿阶段。然而，真正的艺术家绝不会永远停留于简单机械的模仿。唯有在扎实掌握传统笔墨技巧后勇敢融入个人独到的生命体验，方能破茧成蝶，开创出自成一家的独特美学风格。",
                "pinyin": "Chūshè yìshù chuàngzuò de qīngnián huàshī, wǎngwǎng xūyào jīnglì yī duàn línmó dàshī jīngdiǎn de mófǎng jiēduàn. Rán'ér, zhēnzhèng de yìshùjiā juébù huì yǒngyuǎn tíngliú yú jiǎndān jīxiè de mófǎng. Wéiyǒu zài zhāshi zhǎngwò chuántǒng bǐmò jìqiǎo hòu yǒnggǎn róngrù gèrén d способ/dúdào de shēngmìng tǐyàn, fāng néng pòjiǎn-chéngdié, kāichuàng chū zìchéng-yījiā de dútè měixué fēnggé.",
                "en": "Young painters starting in art often pass through a stage of imitating masters. Yet true artists never stagnate in mechanical copying. Only by infusing personal life experience after mastering fundamentals can one forge a distinct aesthetic style.",
                "es": "Los pintores noveles suelen atravesar una etapa de imitación copiando obras maestras. Con todo, el auténtico creador no se estanca en la copia mecánica; solo infundiendo vivencias propias tras dominar el oficio brota un estilo estético genuino."
            }
        ]
    },

    # 40 避免
    {
        "id": "40",
        "hanzi": "避免",
        "pinyin": "bì miǎn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to avoid; avert; prevent; steer clear of (harm, errors, conflicts)",
            "es": "evitar; eludir; esquivar; prevenir (daños, errores, colisiones)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to take preventive measures to keep an undesirable, unfavorable, or harmful situation from taking place",
                "definition_es": "tomar precauciones para impedir que suceda una situación desfavorable, perjudicial o conflictiva",
                "example_phrase": "避免发生意外 (prevent / avoid accidents)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "改用渐亮的光线闹钟能够有效避免身体在深睡眠中突然受到惊吓，从而呵护心血管系统健康。",
                "pinyin": "Gǎiyòng jiànliàng de guāngxiàn nàozhōng nénggòu yǒuxiào bìmiǎn shēntǐ zài shēn shuìmián zhōng tūrán shòudào jīngxià, cóng'ér hēhù xīnxuěguǎn xìtǒng jiànkāng.",
                "en": "Switching to a light-gradual alarm can effectively avoid the body being abruptly startled during deep sleep, protecting cardiovascular health.",
                "es": "Pasarse a un despertador de luz gradual previene eficazmente que el cuerpo sufra sobresaltos en pleno sueño profundo, cuidando el corazón."
            },
            {
                "id": "#2",
                "hanzi": "在方案制订过程中多方征求团队意见，有助于及时发现设计漏洞，避免不必要的人力与资金浪费。",
                "pinyin": "Zài fāng'àn zhìdìng guòchéng zhōng duōfāng zhēngqiú tuánduì yìjiàn, yǒuzhùyú jíshí fāxiàn shèjì lòudòng, bìmiǎn bú bìyào de rénlì yǔ zījīn làngfèi.",
                "en": "Soliciting multi-party team feedback while formulating plans helps detect design loopholes promptly and avoids unnecessary waste of labor and funds.",
                "es": "Consultar al equipo al trazar un plan ayuda a detectar fallos a tiempo, evitando despilfarros innecesarios de personal y presupuesto."
            }
        ],
        "collocations": [
            {"hanzi": "避免发生", "en": "prevent from happening; avoid occurring"},
            {"hanzi": "不可避免", "en": "unavoidable; inevitable"},
            {"hanzi": "有效避免", "en": "effectively avert / prevent"},
            {"hanzi": "避免冲突", "en": "avoid conflict / confrontation"},
            {"hanzi": "避免错误", "en": "avoid mistakes / errors"},
            {"hanzi": "尽量避免", "en": "try one's best to avoid"}
        ],
        "idioms": [
            {"hanzi": "在所难免", "pinyin": "zài suǒ nán miǎn", "meaning_en": "hard to avoid; virtually inevitable"},
            {"hanzi": "防患未然", "pinyin": "fáng huàn wèi rán", "meaning_en": "take preventive measures before mishaps occur"},
            {"hanzi": "未雨绸缪", "pinyin": "wèi yǔ chóu móu", "meaning_en": "repair house before it rains; plan ahead prudently"},
            {"hanzi": "避实就虚", "pinyin": "bì shí jiù xū", "meaning_en": "avoid the enemy's strength and strike at his weakness"}
        ],
        "character_decomposition": [
            {
                "character": "避",
                "pinyin": "bì",
                "meaning_en": "avoid; evade; shun; seek shelter",
                "meaning_es": "evitar; esquivar; huir de; resguardarse",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walking/moving away) + 辟 (law punishment / danger)",
                "sound_component": "辟 (bì/pì, punish / phonetic)",
                "stroke_count": 16,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Walking footsteps 辶 actively moving aside to evade criminal punishment or danger 辟; dodging peril.",
                "visual_mnemonic_story_en": "Stepping along the path (辶) away from hazardous confrontations (辟) to avoid danger (避).",
                "visual_mnemonic_story_es": "Apresurar los pasos (辶) para sortear una sanción o peligro eminente (辟) esquivándolo a tiempo (避).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YSRJ",
                "traditional": ""
            },
            {
                "character": "免",
                "pinyin": "miǎn",
                "meaning_en": "exempt; excuse; remove; avoid",
                "meaning_es": "eximir; dispensar; quitar; librar de",
                "radical": "刀",
                "radical_meaning_en": "knife",
                "meaning_component": "Pictograph of an official taking off a heavy ceremonial helmet to be excused from duty",
                "sound_component": "Phonetic carrier in traditional scripts",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Removing headgear or shedding an official burden; signifies exemption, forgiveness, or being spared from danger.",
                "visual_mnemonic_story_en": "Taking off a heavy restrictive helmet to be exempt and spared from burdensome trial (免).",
                "visual_mnemonic_story_es": "Despojarse del pesado casco militar quedando exonerado o libre de penalidad (免).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "NAU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Dodging sideways on foot (避) to be spared and exempt from hardship (免) is actively avoiding trouble (避免).",
            "composite_memory_hook_es": "Apartarse a paso ligero (避) para quedar eximido o a salvo de percances (免) es evitar (避免).",
            "cultural_and_cognitive_roots": "Classical Sunzi Art of War: true strategic victory lies not in bloody clashes, but in avoiding enemy strongholds (避实击虚) and preventing unnecessary casualties.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone followed by third tone: 'bì miǎn' (51-214). Sharp decisive fall dropping into low dipping contour."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "僻", "pinyin": "pì", "meaning_en": "isolated; remote", "distinction_note": "Has person radical 亻 on left of 辟 instead of walk 辶 in 避"},
                {"character": "壁", "pinyin": "bì", "meaning_en": "wall; cliff", "distinction_note": "Has earth radical 土 at bottom"},
                {"character": "兔", "pinyin": "tù", "meaning_en": "rabbit; hare", "distinction_note": "Has extra dot inside representing a rabbit's tail, unlike 免"},
                {"character": "勉", "pinyin": "miǎn", "meaning_en": "strive; exhort", "distinction_note": "Has power radical 力 on right of 免"}
            ],
            "etymological_cognates": [
                {"character": "躲", "pinyin": "duǒ", "gloss_en": "hide; evade"},
                {"character": "防", "pinyin": "fáng", "gloss_en": "defend; guard against"},
                {"character": "省", "pinyin": "shěng", "gloss_en": "save; spare"},
                {"character": "闪", "pinyin": "shǎn", "gloss_en": "dodge; flash"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "避免 is an active transitive verb indicating taking prudent preventive measures to forestall errors, accidents, or undesirable outcomes.",
            "contrasts": [
                {"id": "1", "compared_word": "避免 vs. 逃避", "pinyin": "táobì", "analysis": "逃避 has a negative connotation of cowardly shirking responsibilities, reality, or legal duties ('逃避现实', '逃避责任'), whereas 避免 is rational preventive caution."},
                {"id": "2", "compared_word": "避免 vs. 阻止", "pinyin": "zǔzhǐ", "analysis": "阻止 means actively stepping in to physically halt an action already underway ('阻止他的鲁莽行为'), while 避免 forestalls events beforehand."},
                {"id": "3", "compared_word": "避免 vs. 免除", "pinyin": "miǎnchú", "analysis": "免除 means officially waiving, exempting, or removing a duty, tax, or debt ('免除学费'), while 避免 prevents bad consequences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代航空安全管理体系中，预防性检修是避免重大飞行安全事故的核心屏障。地勤机务人员严格依照规范流程对引擎、电子雷达及液压线路展开细致排查，唯有将隐患消灭在萌芽状态，才能确保万米高空飞行万无一失。",
                "pinyin": "Zài xiàndài hángkōng ānquán guǎnlǐ tǐxì zhōng, yùfángxìng jiǎnxiū shì bìmiǎn zhòngdà fēixíng ānquán shìgù de héxīn píngzhàng. Dìqín jīwù rényuán yángé yīzhào guīfàn liúchéng duì yǐnqíng, diànzǐ léidá jí yèyā xiànlù zhǎnkāi xìzhì páichá, wéiyǒu jiāng yǐnhuàn xiāomiè zài méngyá zhuàngtài, cáinéng quèbǎo wàn mǐ gāokōng fēixíng wànwúyīshī.",
                "en": "In modern aviation safety, preventive maintenance is the core barrier to avoiding major flight accidents. Ground crews scrupulously inspect engines, radars, and hydraulics according to protocol, nipping hazards in the bud to ensure absolute safety.",
                "es": "En la seguridad aeronáutica, las revisiones preventivas son la barrera clave para evitar siniestros. El personal de tierra inspecciona minuciosamente motores y circuitos para atajar riesgos en su origen y garantizar vuelos seguros."
            },
            {
                "id": "#2",
                "hanzi": "人际交往中难免会产生观点分歧，明智的沟通者懂得换位思考，通过委婉温和的表达来避免正面语言冲突。学会倾听对方的真实顾虑，不仅能够有效化解误会与隔阂，更能为双方维系长久而稳固的信任基石。",
                "pinyin": "Rénjì jiāowǎng zhōng nánmiǎn huì chǎnshēng guāndiǎn fēnqí, míngzhì de gōutōngzhě dǒngde huànwèi-sīkǎo, tōngguò wěiwǎn wēnhé de biǎodá lái bìmiǎn zhèngmiàn yǔyán chōngtū. Xuéhuì qīngtīng duìfāng de zhēnshí gùlǜ, bùjǐn nénggòu yǒuxiào huàjiě wùhuì yǔ géhé, gèng néng wèi shuāngfāng wéixì chángjiǔ ér wěngù de xìnlài jīshí.",
                "en": "In interpersonal exchanges, divergent views inevitably arise. Wise communicators practice empathy and use gentle phrasing to avoid direct clashes. Listening to genuine concerns resolves misunderstandings and cements long-lasting trust.",
                "es": "En el trato humano surgen desacuerdos de forma inevitable. Quien se comunica con sensatez sabe ponerse en el lugar del otro y expresarse con tacto para eludir choques frontales, disipando malentendidos y consolidando la confianza mutua."
            }
        ]
    },

    # 41 传统
    {
        "id": "41",
        "hanzi": "传统",
        "pinyin": "chuán tǒng",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "tradition; traditional; conventional; heritage",
            "es": "tradición; tradicional; convencional; legado cultural"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "historical customs, ethical norms, cultural values, and practices handed down from generation to generation",
                "definition_es": "costumbres históricas, valores éticos y prácticas culturales transmitidas de generación en generación",
                "example_phrase": "优良传统 (fine tradition / glorious heritage)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "conforming to long-established custom or practice rather than modern innovations",
                "definition_es": "que se apega a las pautas y hábitos consuetudinarios frente a las novedades modernas",
                "example_phrase": "传统手工艺 (traditional handicraft / craftsmanship)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "与传统机械闹钟刺耳的铃声相比，新型智能光照唤醒设备更符合人体自然清醒的生理规律。",
                "pinyin": "Yǔ chuántǒng jīxiè nàozhōng cì'ěr de língshēng xiāngbǐ, xīnxíng zhìnéng guāngzhào huànxǐng shèbèi gèng fúhé réntǐ zìrán qīngxǐng de shēnglǐ guīlǜ.",
                "en": "Compared to the harsh ringing of traditional mechanical alarms, new smart lighting wake-up devices conform better to natural physiological waking laws.",
                "es": "Frente al estridente timbre del despertador tradicional mecánico, los nuevos dispositivos de luz inteligente armonizan mejor con la fisiología humana."
            },
            {
                "id": "#2",
                "hanzi": "每逢中秋佳节，全家人围坐在一起品尝月饼、共赏明月，是中华民族流传千百年的美好传统。",
                "pinyin": "Měiféng zhōngqiū jiājié, quánjiā rén wéizuò zài yīqǐ pǐncháng yuèbǐng, gòngshǎng míngyuè, shì Zhōnghuá mínzú liúchuán qiānbǎi nián de měihǎo chuántǒng.",
                "en": "Every Mid-Autumn Festival, the entire family gathering to savor mooncakes and admire the full moon is a cherished tradition passed down for centuries.",
                "es": "Cada Fiesta del Medio Otoño, la familia congregada degustando pasteles de luna bajo el plenilunio celebra una hermosa tradición centenaria."
            }
        ],
        "collocations": [
            {"hanzi": "传统文化", "en": "traditional culture"},
            {"hanzi": "传统美德", "en": "traditional virtues"},
            {"hanzi": "继承传统", "en": "inherit / carry forward traditions"},
            {"hanzi": "发扬传统", "en": "carry forward / promote traditional heritage"},
            {"hanzi": "传统节日", "en": "traditional festival"},
            {"hanzi": "打破传统", "en": "break with tradition"}
        ],
        "idioms": [
            {"hanzi": "薪火相传", "pinyin": "xīn huǒ xiāng chuán", "meaning_en": "pass the torch from generation to generation"},
            {"hanzi": "因循守旧", "pinyin": "yīn xún shǒu jiù", "meaning_en": "stick to conventions and resist reform"},
            {"hanzi": "继往开来", "pinyin": "jì wǎng kāi lái", "meaning_en": "carry forward past heritage and forge ahead into future"},
            {"hanzi": "代代相传", "pinyin": "dài dài xiāng chuán", "meaning_en": "handed down from generation to generation"}
        ],
        "character_decomposition": [
            {
                "character": "传",
                "pinyin": "chuán",
                "meaning_en": "pass on; hand down; transmit; impart",
                "meaning_es": "transmitir; difundir; traspasar; propagar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person passing along) + 专 (spinning spindle thread / focused transmission)",
                "sound_component": "专 (zhuān, carrier / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A postal relay person 亻 handing down messages like uninterrupted spun thread 专 along roads; transmitting knowledge.",
                "visual_mnemonic_story_en": "A messenger person (亻) carrying single-minded focus (专) transmits news across generations (传).",
                "visual_mnemonic_story_es": "Un mensajero (亻) que corre con devoción concentrada (专) transmite legados y noticias sin cesar (传).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OQNI",
                "traditional": "傳"
            },
            {
                "character": "统",
                "pinyin": "tǒng",
                "meaning_en": "interconnected thread; unify; gather; govern",
                "meaning_es": "hilo conductor; unificar; reunir; regir; sistema",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (continuous silk strand) + 充 (fill up / nourish completely)",
                "sound_component": "充 (chōng, phonetic carrier)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "The main guiding thread 纟 that gathers and unifies all filling fibers 充 into a coherent fabric; lineage and system.",
                "visual_mnemonic_story_en": "A continuous silk thread (纟) gathering all parts into an interconnected whole (充) unifies the system (统).",
                "visual_mnemonic_story_es": "La hebra de seda (纟) que enlaza y nutre la totalidad del tejido (充) mantiene unido el linaje (统).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "VMYIU",
                "traditional": "統"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Passing along down the ages (传) through an uninterrupted lineage thread (统) constitutes living tradition (传统).",
            "composite_memory_hook_es": "Transmitir de generación en generación (传) a lo largo de un hilo conductor histórico (统) conforma la tradición (传统).",
            "cultural_and_cognitive_roots": "Derived from historiographical lineages (正统, 道统): Confucian cultural continuity preserved like a seamless silk thread passing across dynastic shifts.",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by third tone: 'chuán tǒng' (35-214). Smooth rising glide followed by dip-and-rise contour."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "专", "pinyin": "zhuān", "meaning_en": "specialized; focused", "distinction_note": "Lacks person radical 亻 on left of 传"},
                {"character": "转", "pinyin": "zhuǎn", "meaning_en": "turn; shift", "distinction_note": "Has vehicle radical 车 on left of 专"},
                {"character": "统", "pinyin": "tǒng", "meaning_en": "unify; tradition", "distinction_note": "Has silk radical 纟 on left of 充"},
                {"character": "充", "pinyin": "chōng", "meaning_en": "fill; charge", "distinction_note": "Lacks silk radical 纟 on left"}
            ],
            "etymological_cognates": [
                {"character": "承", "pinyin": "chéng", "gloss_en": "inherit; carry on"},
                {"character": "继", "pinyin": "jì", "gloss_en": "continue; succeed"},
                {"character": "俗", "pinyin": "sú", "gloss_en": "custom; convention"},
                {"character": "祖", "pinyin": "zǔ", "gloss_en": "ancestor; origin"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "传统 refers to long-standing cultural customs, ethical practices, and time-honored conventions passed down across generations.",
            "contrasts": [
                {"id": "1", "compared_word": "传统 vs. 习俗", "pinyin": "xísú", "analysis": "习俗 focuses on specific folk customs and habits (e.g. eating zongzi, lion dances), whereas 传统 encompasses deep philosophical values, artistic lineages, and institutions."},
                {"id": "2", "compared_word": "传统 vs. 常规", "pinyin": "chángguī", "analysis": "常规 refers to routine administrative rules, standard operational procedures, or normal conventions, lacking 传统's historical cultural depth."},
                {"id": "3", "compared_word": "传统 vs. 古老", "pinyin": "gǔlǎo", "analysis": "古老 simply describes age and ancient vintage ('古老的城堡'), while 传统 emphasizes living transmission and active generational heritage."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "优秀传统文化是一座取之不竭的精神宝库。在现代文创设计中，青年设计师巧妙地将传统水墨写意美学与现代数码科技相融合，让陈列在博物馆深处的千年非物质文化遗产重新焕发出蓬勃的当代生机。",
                "pinyin": "Yōuxiù chuántǒng wénhuà shì yī zuò qǔzhībùjié de jīngshén bǎokù. Zài xiàndài wénchuàng shèjì zhōng, qīngnián shèjìshī qiǎomiào de jiāng chuántǒng shuǐmò xièyì měixué yǔ xiàndài shùmǎ kējì xiāng rónghé, ràng chénliè zài bówùguǎn shēnchù de qiān nián fēiwùzhì wénhuà yíchǎn chóngxīn huànfā chū péngbó de dāngdài shēngjī.",
                "en": "Fine traditional culture is an inexhaustible treasure house of spirit. In contemporary creative design, young artists blend ink-wash aesthetics with digital technologies, breathing vibrant life into intangible cultural heritage.",
                "es": "La cultura tradicional es un manantial inagotable de riqueza espiritual. En el diseño contemporáneo, los creadores funden la aguada clásica con tecnologías digitales, revitalizando el patrimonio inmaterial con brío renovado."
            },
            {
                "id": "#2",
                "hanzi": "随着全球化浪潮奔涌向前，如何在坚守民族文化传统的同时拥抱世界文明，成为各国共同探索的重要时代课题。历史证明，唯有立足自身优秀的文化传统根基，以包容开放的胸襟博采众长，文明之树才能根深叶茂、历久弥新。",
                "pinyin": "Suízhe quánqiúhuà làngcháo bēnyǒng qiánxiáng, rúhé zài jiānshǒu mínzú wénhuà chuántǒng de tóngshí yōngbào shìjiè wénmíng, chéngwéi gè guó gòngtóng tànsuǒ de zhòngyào shídài kètí. Lìshǐ zhèngmíng, wéiyǒu lìzú zìshēn yōuxiù de wénhuà chuántǒng gēnjī, yǐ bāoróng kāifàng de xiōngjīn bócǎi-zhòngcháng, wénmíng zhī shù cáinéng gēnshēn-yèmào, lìjiǔ-míxīn.",
                "en": "As globalization surges, preserving national traditions while embracing world civilizations has become a vital shared question. Grounded in cultural roots while adopting diverse strengths, civilization flourishes with enduring vitality.",
                "es": "Con el avance imparable de la globalización, preservar las tradiciones patrias al tiempo que se abraza la civilización mundial es un reto clave. Solo arraigados en el legado propio y abiertos al diálogo florece la cultura con perenne vigor."
            }
        ]
    }
]

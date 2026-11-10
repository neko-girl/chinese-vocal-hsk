# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 戒
    {
        "id": "31",
        "hanzi": "戒",
        "pinyin": "jiè",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to give up; to quit; to abstain from; to warn; to guard against",
            "es": "dejar de; abandonar (un hábito); abstenerse; prevenir; precaverse"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to renounce, quit, or abstain from an addictive habit such as smoking or drinking",
                "definition_es": "abandonar, dejar o abstenerse de un mal hábito adictivo como fumar o beber",
                "example_phrase": "戒烟戒酒 (quit smoking and drinking)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Formal",
                "definition_en": "to guard against, take warning from, or be vigilant against errors or vices",
                "definition_es": "precaverse, precaver o guardarse de cometer faltas o vicios",
                "example_phrase": "引以为戒 (take as a warning)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了改善日益严重的慢性咽喉炎与心肺健康，父亲下定决心彻底戒掉了抽了三十年的香烟。",
                "pinyin": "Wèile gǎishàn rìyì yánzhòng de mànxìng yānhóuyán yǔ xīnfèi jiànkāng, fùqīn xiàdìng juéxīn chèdǐ jièdiào le chōu le sānshí nián de xiāngyān.",
                "en": "To improve worsening chronic pharyngitis and cardiopulmonary health, father firmly resolved to completely quit smoking cigarettes after thirty years.",
                "es": "Para aliviar su faringitis crónica y proteger el corazón, el padre decidió con firmeza dejar para siempre el tabaco tras treinta años fumando."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅晚年因肺病与胃病屡屡发作，医生曾严厉告诫他必须戒酒戒烟，但他为了写作依然难以割舍烟草。",
                "pinyin": "Lǔ Xùn wǎnnián yīn fèibìng yǔ wèibìng lǚlǚ fāzuò, yīshēng céng yánlì gàojiè tā bìxū jièjiǔ jièyān, dàn tā wèile xiězuò yīrán nányǐ gēshě yāncǎo.",
                "en": "Suffering recurrent lung and stomach crises in his final years, doctors sternly warned Lu Xun to quit alcohol and tobacco, but writing kept him bound to it.",
                "es": "Por sus afecciones de pulmón y estómago, los médicos conminaron a Lu Xun a dejar el tabaco y el alcohol; mas para escribir no podía prescindir de fumar."
            }
        ],
        "collocations": [
            {"hanzi": "戒烟", "en": "quit smoking"},
            {"hanzi": "戒酒", "en": "quit drinking alcohol"},
            {"hanzi": "戒备", "en": "be on guard; alert vigilance"},
            {"hanzi": "引以为戒", "en": "take as a warning/caution"},
            {"hanzi": "戒骄戒躁", "en": "guard against arrogance and rashness"},
            {"hanzi": "戒掉坏毛病", "en": "kick a bad habit"}
        ],
        "idioms": [
            {"hanzi": "戒骄戒躁", "pinyin": "jiè jiāo jiè zào", "meaning_en": "guard against arrogance and impetuosity"},
            {"hanzi": "前车之鉴", "pinyin": "qián chē zhī jiàn", "meaning_en": "warning from the overturned cart ahead; lessons from past errors"},
            {"hanzi": "严加戒备", "pinyin": "yán jiā jiè bèi", "meaning_en": "mount strict security vigilance"},
            {"hanzi": "惩前毖后", "pinyin": "chéng qián bì hòu", "meaning_en": "criticize former errors to take warning for the future"}
        ],
        "character_decomposition": [
            {
                "character": "戒",
                "pinyin": "jiè",
                "meaning_en": "warn; guard against; quit; ring; precept",
                "meaning_es": "advertir; precaverse; dejar; precepto; anillo",
                "radical": "戈",
                "radical_meaning_en": "halberd/dagger-axe",
                "meaning_component": "戈 (dagger-axe weapon) + 廾 (two hands holding weapon)",
                "sound_component": "戒 (jiè)",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram showing two hands 廾 firmly gripping a halberd 戈 in defensive guard against danger.",
                "visual_mnemonic_story_en": "Two hands hold a halberd (戈) ready on guard to warn against incoming danger and ward off bad habits (戒).",
                "visual_mnemonic_story_es": "Dos manos empuñan la alabarda (戈) en guardia defensiva, alertando del peligro y cortando malos hábitos (戒).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IT",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Hold weapons high in defensive guard (戒) to cut off and quit destructive addictions (戒).",
            "composite_memory_hook_es": "Empuña el arma en guardia vigilante (戒) para erradicar y dejar hábitos perniciosos (戒).",
            "cultural_and_cognitive_roots": "Originating from military garrison sentries holding halberds; adopted in Buddhist monastic rules (戒律, śīla) as moral prohibitions against vices, and later in medicine for cessation.",
            "tone_sandhi_and_pitch_modulation": "Falling 4th tone: 'jiè' (51). Crisp, decisive descent from pitch 5 to pitch 1, reflecting resolute willpower."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "戎", "pinyin": "róng", "meaning_en": "military; arms", "distinction_note": "Has 十 cross inside 戈 instead of two parallel vertical lines of 戒"},
                {"character": "成", "pinyin": "chéng", "meaning_en": "accomplish; become", "distinction_note": "Has 勹 wrapped inside 戈"},
                {"character": "或", "pinyin": "huò", "meaning_en": "maybe; perhaps", "distinction_note": "Has 口 and 一 inside 戈"},
                {"character": "械", "pinyin": "xiè", "meaning_en": "weapon; machinery", "distinction_note": "Has tree radical 木 on left side of 戒"}
            ],
            "etymological_cognates": [
                {"character": "断", "pinyin": "duàn", "gloss_en": "sever; cut off completely"},
                {"character": "绝", "pinyin": "jué", "gloss_en": "cut off threads; absolute"},
                {"character": "防", "pinyin": "fáng", "gloss_en": "guard against; earthen embankment"},
                {"character": "警", "pinyin": "jǐng", "gloss_en": "warn with words; alert"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "戒 denotes proactively and resolutely severing an ingrained addiction or habit through conscious willpower.",
            "contrasts": [
                {"id": "1", "compared_word": "戒 vs. 戒备", "pinyin": "jièbèi", "analysis": "戒备 is solely a noun or verb meaning defensive military/security alert against external enemies, while 戒 alone often means quitting habits ('戒烟')."},
                {"id": "2", "compared_word": "戒 vs. 放弃", "pinyin": "fàngqì", "analysis": "放弃 means giving up rights, opportunities, or struggles passively, whereas 戒 means voluntarily quitting harmful addictions."},
                {"id": "3", "compared_word": "戒 vs. 禁", "pinyin": "jìn", "analysis": "禁 means external prohibition by law or authority ('禁止吸烟'), while 戒 emphasizes personal internal self-restraint ('戒烟')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "戒除一个根深蒂固的不良嗜好，本质上是一场与自我惰性的顽强博弈。无论是放下对尼古丁的依赖，还是告别深夜沉迷手机的恶习，都需要刮骨疗毒的决绝勇气。唯有敢于向昨天的软弱告别，生命才能重获清爽与掌控。",
                "pinyin": "Jièchú yí ge gēnshēn-dìgù de bùliáng shìhào, běnzhì shàng shì yì chǎng yǔ zìwǒ duòxìng de wánqiáng bóyì. Wúlùn shì fàngxià duì nígǔdīng de yīlài, háishì gàobié shēnyè chénmí shǒujī de èxí, dōu xūyào guāgǔ-liáodú de juéjué yǒngqì. Wéiyǒu gǎnyú xiàng zuótiān de ruǎnruò gàobié, shēngmìng cáinéng chónghuò qīngshuǎng yǔ zhǎngkòng.",
                "en": "Quitting an ingrained vice is essentially a tenacious duel with personal inertia. Whether abandoning nicotine or midnight screen addiction, it takes resolute courage. Only by daring to part with past weakness can life regain fresh mastery.",
                "es": "Erradicar un vicio arraigado es un pulso tenaz contra la inercia interior. Romper con la nicotina o el desvelo ante las pantallas exige coraje sin titubeos. Solo despidiéndose de la flaqueza pretérita recobra la vida su vigor y timón."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的金融衍生品市场，投资机构必须时刻紧绷风险防控之弦，切忌盲目激进加杠杆。行业监管部门发布的一系列风险预警通报，督促各类资产管理机构引以为戒，切实完善内控合规体系，坚决守住不发生系统性金融风险的底线。",
                "pinyin": "Miànduì shùnxī-wànbiàn de jīnróng yǎnshēngpǐn shìchǎng, tóuzī jīgòu bìxū shíkè jǐnběng fēngxiǎn fángkòng zhī xián, qièjì mángmù jījìn jiā gànggǎn. Hángyè jiānguǎn bùmén fābù de yíxìliè fēngxiǎn yùjǐng tōngbào, dūcù gèlèi zīchǎn guǎnlǐ jīgòu yǐnyǐwéijiè, qièshí wánshàn nèikòng hégūi tǐxì, jiānjué shǒuzhù bù fāshēng xìtǒngxìng jīnróng fēngxiǎn de dǐxiàn.",
                "en": "In volatile financial markets, investment institutions must keep risk control tight, strictly avoiding blind leverage. Regulatory warnings urge firms to take heed, refine compliance, and firmly defend the baseline against systemic risks.",
                "es": "Ante mercados financieros volátiles, los fondos deben extremar el control de riesgos y evitar el apalancamiento temerario. Las advertencias de los supervisores instan a precaverse y afianzar la auditoría, blindando la estabilidad sistémica."
            }
        ]
    },

    # 32 保存
    {
        "id": "32",
        "hanzi": "保存",
        "pinyin": "bǎo cún",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to preserve; to conserve; to keep; to save (files/data); to maintain intact",
            "es": "guardar; conservar; preservar; mantener; salvar (archivos informáticos)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to keep things, documents, or biological specimens safe, undamaged, and intact over time",
                "definition_es": "guardar cosas, documentos o muestras para que no se deterioren, pierdan o dañen",
                "example_phrase": "妥善保存文件 (keep documents safe and well-preserved)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to save electronic computer files, database records, or digital configurations",
                "definition_es": "guardar o salvar archivos informáticos, bases de datos o configuraciones en soporte digital",
                "example_phrase": "保存修改内容 (save modified contents)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这些泛黄的老照片被外婆妥善保存在铁盒子里，记录了半个世纪以来全家人的温情岁月。",
                "pinyin": "Zhèxiē fànhuáng de lǎo zhàopiàn bèi wàipó tuǒshàn bǎocún zài tiě hézi lǐ, jìlù le bàn ge shìjì yǐlái quánjiā rén de wēnqíng suìyuè.",
                "en": "These yellowed old photos were properly preserved by grandmother in a tin box, documenting half a century of family warmth.",
                "es": "Estas fotos amarillentas fueron conservadas por la abuela en una lata, guardando medio siglo de entrañable memoria familiar."
            },
            {
                "id": "#2",
                "hanzi": "北京鲁迅博物馆精心保存了鲁迅生前的大量珍贵手稿、藏书和生活用具，具有极高的历史文化价值。",
                "pinyin": "Běijīng Lǔ Xùn Bówùguǎn jīngxīn bǎocún le Lǔ Xùn shēngqián de dàliàng zhēnguì shǒugǎo, cángshū hé shēnghuó yòngjù, jùyǒu jí gāo de lìshǐ wénhuà jiàzhí.",
                "en": "The Beijing Lu Xun Museum meticulously preserves many of his manuscripts, book collections, and daily utensils, of immense cultural value.",
                "es": "El Museo Lu Xun de Pekín conserva con celo manuscritos, volúmenes y enseres de su vida cotidiana, de incalculable valor histórico."
            }
        ],
        "collocations": [
            {"hanzi": "妥善保存", "en": "properly keep/preserve"},
            {"hanzi": "保存完好", "en": "preserved in perfect condition"},
            {"hanzi": "保存文件", "en": "save files/documents"},
            {"hanzi": "保存实力", "en": "conserve strength/resources"},
            {"hanzi": "保存期", "en": "shelf life; retention period"},
            {"hanzi": "点击保存", "en": "click to save"}
        ],
        "idioms": [
            {"hanzi": "历久弥新", "pinyin": "lì jiǔ mí xīn", "meaning_en": "remain fresh and vibrant with the passage of time"},
            {"hanzi": "完璧归赵", "pinyin": "wán bì guī Zhào", "meaning_en": "return the jade intact to Zhao; return untouched to owner"},
            {"hanzi": "安然无恙", "pinyin": "ān rán wú yàng", "meaning_en": "safe and sound without the slightest blemish"},
            {"hanzi": "硕果仅存", "pinyin": "shuò guǒ jǐn cún", "meaning_en": "the sole surviving great fruit; one of the few survivors"}
        ],
        "character_decomposition": [
            {
                "character": "保",
                "pinyin": "bǎo",
                "meaning_en": "protect; maintain; keep; guarantee",
                "meaning_es": "proteger; mantener; amparar; garantizar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (adult guardian)",
                "sound_component": "呆 (infant child swaddled on back)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Oracle bone pictogram showing an adult guardian 亻 carrying an infant child on their back, protecting it from harm.",
                "visual_mnemonic_story_en": "A loving adult (亻) holds a baby safely swaddled on their back, protecting and keeping it unharmed (保).",
                "visual_mnemonic_story_es": "Un tutor protector (亻) lleva a un niño a la espalda, amparándolo y protegiéndolo de todo daño (保).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ORD",
                "traditional": ""
            },
            {
                "character": "存",
                "pinyin": "cún",
                "meaning_en": "exist; live; survive; deposit; retain",
                "meaning_es": "existir; vivir; subsistir; depositar; guardar",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (child/offspring)",
                "sound_component": "才 (cái, plant sprout / phonetic)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Ancient ideogram showing a fresh sprout 才 sprouting above an offspring 子, signifying ongoing existence and survival.",
                "visual_mnemonic_story_en": "A tender sprout grows safely under roof shelter for the child (子), ensuring it survives and exists (存).",
                "visual_mnemonic_story_es": "Un brote tierno germina al amparo del hogar para el niño (子), garantizando su subsistencia (存).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "KND",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Protect with loving care (保) so that precious heritage continues to exist intact (存), preserving it safely (保存).",
            "composite_memory_hook_es": "Ampara con celo (保) para que el legado siga existiendo intacto (存), logrando conservarlo (保存).",
            "cultural_and_cognitive_roots": "Combining protective guardianship (保) with existential permanence (存); in traditional culture, preserving family ancestral tablets (宗祠) and genealogies formed the sacred core of continuity.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by rising tone: 'bǎo cún' (214-35). Syllable 'bǎo' dips down, followed by an energetic rising tone on 'cún'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "堡", "pinyin": "bǎo", "meaning_en": "fortress", "distinction_note": "Has earth radical 土 at bottom of 保"},
                {"character": "在", "pinyin": "zài", "meaning_en": "at; in", "distinction_note": "Has 土 at bottom instead of 子 in 存"},
                {"character": "右", "pinyin": "yòu", "meaning_en": "right", "distinction_note": "Has 口 at bottom instead of 子"},
                {"character": "友", "pinyin": "yǒu", "meaning_en": "friend", "distinction_note": "Has 又 at bottom instead of 子"}
            ],
            "etymological_cognates": [
                {"character": "藏", "pinyin": "cáng", "gloss_en": "hide; store away securely"},
                {"character": "护", "pinyin": "hù", "gloss_en": "protect; guard with hand"},
                {"character": "留", "pinyin": "liú", "gloss_en": "remain; detain; preserve"},
                {"character": "蓄", "pinyin": "xù", "gloss_en": "accumulate; store crops"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "保存 focuses on keeping physical items, documents, food, or computer files intact without loss or spoilage.",
            "contrasts": [
                {"id": "1", "compared_word": "保存 vs. 保留", "pinyin": "bǎoliú", "analysis": "保留 emphasizes keeping or retaining rights, opinions, seats, or customs without altering them, while 保存 emphasizes protecting items from physical/digital decay."},
                {"id": "2", "compared_word": "保存 vs. 保护", "pinyin": "bǎohù", "analysis": "保护 focuses on shielding an entity from active external danger, violence, or harm, whereas 保存 focuses on storage and long-term conservation."},
                {"id": "3", "compared_word": "保存 vs. 存储", "pinyin": "cúnchǔ", "analysis": "存储 is a technical computing/warehousing term for storing large volumes of data or physical stock, while 保存 is general and everyday."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "岁月是一条奔流不息的大河，唯有那些被爱妥善保存的记忆，才能在时光的淘洗中闪耀出温润的光泽。一封泛黄的家书，一枚斑驳的纪念章，静静躺在抽屉深处，默默守护着漫漫人生旅途中最珍贵的深情与执着。",
                "pinyin": "Suìyuè shì yì tiáo bēnliú-bùxī de dàhé, wéiyǒu nàxiē bèi ài tuǒshàn bǎocún de jìyì, cáinéng zài shíguāng de táoxǐ zhōng shǎnyào chū wēnrùn de guāngzé. Yì fēng fànhuáng de jiāshū, yì méi bānbó de jìniànzhāng, jìngjìng tǎng zài chōutì shēnchù, mòmò shǒuhù zhe mànmàn rénshēng lǚtú zhōng zuì zhēnguì de shēnqíng yǔ zhízhuó.",
                "en": "Years are a rushing river; only memories lovingly preserved shine with warm luster through time. A yellowed family letter and a worn medal lying in a drawer quietly guard life's most precious devotion and resolve.",
                "es": "Los años son un río impetuoso; solo los recuerdos conservados con amor brillan en el tiempo. Una carta amarillenta y una medalla gastada en el cajón custodian en silencio los afectos más puros y nobles del camino vivido."
            },
            {
                "id": "#2",
                "hanzi": "古籍文献数字化工程为抢救与永久保存珍贵古籍开辟了全新路径。技术团队采用高光谱无损扫描与三维建模技术，将宋元珍本的纸张纤维与朱墨字迹完好记录。这不仅实现了历史典籍的永久保存，更极大地促进了中华优秀传统文化的开放共享。",
                "pinyin": "Gǔjí wénxiàn shùzìhuà gōngchéng wèi qiǎngjiù yǔ yǒngjiǔ bǎocún zhēnguì gǔjí kāipì le quánxīn lùjìng. Jìshù tuánduì cǎiyòng gāoguāngpǔ wúsǔn sǎomiáo yǔ sānwéi jiànmó jìshù, jiāng Sòng-Yuán zhēnběn de zhǐzhāng xiānwéi yǔ zhūmò zìjì wánhǎo jìlù. Zhè bùjǐn shíxiàn le lìshǐ diǎnjí de yǒngjiǔ bǎocún, gèng jídà de cùjìn le Zhōnghuá yōuxiù chuántǒng wénhuà de kāifàng gòngxiǎng.",
                "en": "Digitization of ancient manuscripts opens new paths for permanent preservation. Using non-destructive scanning and 3D modeling, teams record Song and Yuan rarities, ensuring eternal conservation and promoting open cultural sharing.",
                "es": "La digitalización abre nuevas vías para conservar incunables antiguos. Mediante escaneo hiperespectral no invasivo y modelado 3D, se capturan las fibras de códices Song y Yuan, garantizando su preservación y divulgación pública."
            }
        ]
    },

    # 33 资料
    {
        "id": "33",
        "hanzi": "资料",
        "pinyin": "zī liào",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "data; material; information; reference documents; resources",
            "es": "datos; material; información; documentación; fuentes de referencia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "factual information, archival documents, statistics, or reference sources collected for study or work",
                "definition_es": "información factual, documentos de archivo, estadísticas o fuentes de consulta reunidas para el trabajo",
                "example_phrase": "搜集第一手资料 (collect firsthand material)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Formal",
                "definition_en": "material means or resources for production or living",
                "definition_es": "medios de producción o subsistencia material para la vida",
                "example_phrase": "生产资料与生活资料 (means of production and means of subsistence)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了撰写毕业论文，他在图书馆查阅了大量的历史档案资料，做了厚厚三大本读书笔记。",
                "pinyin": "Wèile zhuànxiě bìyè lùnwén, tā zài túshūguǎn cháyuè le dàliàng de lìshǐ dàng'àn zīliào, zuò le hòuhòu sān dà běn dúshū bǐjì.",
                "en": "To write his thesis, he consulted a large volume of historical archival material in the library, filling three thick notebooks.",
                "es": "Para redactar su tesis, consultó copiosa documentación de archivo en la biblioteca, llenando tres gruesos cuadernos de notas."
            },
            {
                "id": "#2",
                "hanzi": "学者们通过比对鲁迅日记与民国报刊资料，系统还原了他当年在京沪两地的交往脉络与餐饮开销。",
                "pinyin": "Xuézhěmen tōngguò bǐduì Lǔ Xùn rìjì yǔ Mínguó bàokān zīliào, xìtǒng huányuán le tā dāngnián zài Jīng-Hù liǎng dì de jiāowǎng màiluò yǔ cānyǐn kāixiāo.",
                "en": "By comparing Lu Xun's diaries with Republican newspaper records, scholars systematically reconstructed his social network and dining expenses.",
                "es": "Cotejando los diarios de Lu Xun con la hemeroteca republicana, los expertos reconstruyeron su red de amistades y sus cuentas gastronómicas."
            }
        ],
        "collocations": [
            {"hanzi": "收集资料", "en": "collect information/data"},
            {"hanzi": "第一手资料", "en": "firsthand material/data"},
            {"hanzi": "参考资料", "en": "reference materials"},
            {"hanzi": "档案资料", "en": "archival records"},
            {"hanzi": "资料齐全", "en": "complete documentation"},
            {"hanzi": "生产资料", "en": "means of production"}
        ],
        "idioms": [
            {"hanzi": "引经据典", "pinyin": "yǐn jīng jù diǎn", "meaning_en": "quote classic texts and cite authoritative sources"},
            {"hanzi": "搜罗殆尽", "pinyin": "sōu luó dài jìn", "meaning_en": "collect and comb through almost everything thoroughly"},
            {"hanzi": "信而有征", "pinyin": "xìn ér yǒu zhēng", "meaning_en": "proven true by verifiable evidence and reliable documentation"},
            {"hanzi": "汗牛充栋", "pinyin": "hàn niú chōng dòng", "meaning_en": "immense volume of books making pack-oxen sweat; voluminous"}
        ],
        "character_decomposition": [
            {
                "character": "资",
                "pinyin": "zī",
                "meaning_en": "capital; wealth; resources; subsidize; qualifications",
                "meaning_es": "capital; recursos; bienes; fondos; títulos",
                "radical": "贝",
                "radical_meaning_en": "shell / money",
                "meaning_component": "贝 (cowrie shell / monetary currency)",
                "sound_component": "次 (cì, second / orderly sequence)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character where valuable cowrie shell wealth 贝 provides necessary capital resources.",
                "visual_mnemonic_story_en": "Neatly stacked cowrie coins (贝) supply the vital financial capital and resources (资) for projects.",
                "visual_mnemonic_story_es": "Monedas de concha (贝) apiladas con orden brindan el capital y los fondos necesarios (资).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MOBU",
                "traditional": ""
            },
            {
                "character": "料",
                "pinyin": "liào",
                "meaning_en": "material; grain; measure; expect; foresee",
                "meaning_es": "materia; material; grano; calcular; prever",
                "radical": "斗",
                "radical_meaning_en": "peck / measure",
                "meaning_component": "斗 (peck measuring ladle)",
                "sound_component": "米 (mǐ, rice grain to be measured)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing measuring out rations of grain 米 using a volumetric wooden peck ladle 斗, meaning material rations.",
                "visual_mnemonic_story_en": "Using a wooden measuring ladle (斗) to scoop out grain rations (米) provides raw materials (料).",
                "visual_mnemonic_story_es": "Con el cazo de medir (斗) se reparte la ración de grano (米), suministrando la materia prima (料).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FDYJ",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Gather your informational capital resources (资) and measure raw facts like grain (料) to compile research data (资料).",
            "composite_memory_hook_es": "Reúne tus recursos de información (资) y mide los datos como grano (料) para compilar documentación (资料).",
            "cultural_and_cognitive_roots": "Combining economic funds (资) with measured physical ingredients (料); expanded in modern lexicography to encompass intellectual resources and data.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'zī liào' (55-51). Articulate 'zī' on level pitch 55, then descend firmly on 'liào'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "姿", "pinyin": "zī", "meaning_en": "posture; gesture", "distinction_note": "Has woman radical 女 at bottom instead of 贝"},
                {"character": "科", "pinyin": "kē", "meaning_en": "branch of study", "distinction_note": "Has 禾 on left instead of 米 in 料"},
                {"character": "抖", "pinyin": "dǒu", "meaning_en": "shake; tremble", "distinction_note": "Has hand radical 扌 on left instead of 米"},
                {"character": "斜", "pinyin": "xié", "meaning_en": "slanted; oblique", "distinction_note": "Has 余 on left instead of 米"}
            ],
            "etymological_cognates": [
                {"character": "材", "pinyin": "cái", "gloss_en": "timber; raw material; talent"},
                {"character": "据", "pinyin": "jù", "gloss_en": "evidence; grasp with hand"},
                {"character": "籍", "pinyin": "jí", "gloss_en": "records; books on bamboo"},
                {"character": "案", "pinyin": "àn", "gloss_en": "case table; legal records"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "资料 emphasizes factual, textual, or statistical reference inputs collected for research, writing, or practical production.",
            "contrasts": [
                {"id": "1", "compared_word": "资料 vs. 材料", "pinyin": "cáiliào", "analysis": "材料 emphasizes physical substances used in manufacture (steel, wood) or written drafts, while 资料 emphasizes intellectual data and reference documents."},
                {"id": "2", "compared_word": "资料 vs. 信息", "pinyin": "xìnxī", "analysis": "信息 refers to dynamic real-time communication signals, messages, or news data, while 资料 denotes compiled reference documents and dossiers."},
                {"id": "3", "compared_word": "资料 vs. 数据", "pinyin": "shùjù", "analysis": "数据 strictly refers to quantitative numerical figures, metrics, and computer bits, while 资料 includes qualitative texts and images."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "学术研究是一场板凳甘坐十年冷的漫长探索。学者为了弄清一个历史细节，往往需要在浩瀚如烟海的古籍资料中反复搜求、比对考证。正是在这一份份泛黄的档案资料里，历史那模糊的面庞才一点点变得清晰可感。",
                "pinyin": "Xuéshù yánjiū shì yì chǎng bǎndèng gānzuò shí nián lěng de màncháng tànsuǒ. Xuézhě wèile nòngqīng yí ge lìshǐ xìjié, wǎngwǎng xūyào zài hàohàn rú yānhǎi de gǔjí zīliào zhōng fǎnfù sōuqiú, bǐduì kǎozhèng. Zhèng shì zài zhè yífènfèn fànhuáng de dàng'àn zīliào lǐ, lìshǐ nà móhu de miànpáng cái yìdiǎndiǎn biàn de qīngxī kě gǎn.",
                "en": "Scholarship is a patient decade-long pursuit. To clarify a single historical detail, researchers sift through seas of ancient documents, comparing evidence. In these yellowed archival records, history's blurred face gradually becomes distinct.",
                "es": "La investigación académica exige años de paciente estudio. Para esclarecer un pormenor histórico, el sabio escudriña legajos antiguos cotejando datos. Es en esa documentación amarillenta donde el rostro borroso del pasado cobra nitidez."
            },
            {
                "id": "#2",
                "hanzi": "在数字化大数据时代，保护个人敏感资料与数据安全已上升为国家战略。相关法律法规严格规范互联网企业对用户个人信息资料的采集、存储与跨境传输行为，依法严厉打击非法买卖公民资料犯罪，全面筑牢数字经济时代的信息安全堤坝。",
                "pinyin": "Zài shùzìhuà dàshùjù shídài, bǎohù gèrén mǐngǎn zīliào yǔ shùjù ānquán yǐ shàngshēng wéi guójiā zhànlüè. Xiāngguān fǎlǜ fǎguī yángé guīfàn hùliánwǎng qǐyè duì yònghù gèrén xìnxī zīliào de cǎijí, cúnchǔ yǔ kuàjìng chuánshū xíngwéi, yīfǎ yánlì dǎjī fēifǎ mǎimài gōngmín zīliào fànzuì, quánmiàn zhùláo shùzì jīngjì shídài de xìnxī ānquán dībà.",
                "en": "In the big data era, protecting sensitive personal information has become a national strategy. Strict laws regulate collection, storage, and cross-border transfer of user data by tech firms, cracking down on illegal trafficking to fortify security.",
                "es": "En la era de los macrodatos, proteger la información sensible es una prioridad nacional. Las leyes regulan la recogida y almacenamiento de datos por firmas tecnológicas y penalizan el tráfico de expedientes, blindando la seguridad digital."
            }
        ]
    },

    # 34 曾经
    {
        "id": "34",
        "hanzi": "曾经",
        "pinyin": "céng jīng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "once; formerly; previously; at one time in the past",
            "es": "una vez; antaño; en otro tiempo; anteriormente; haber ocurrido en el pasado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "indicates that an action or state occurred or existed at a specific prior time in the past",
                "definition_es": "indica que una acción o estado tuvo lugar o existió en un momento anterior del pasado",
                "example_phrase": "曾经去过北京 (once visited Beijing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "青年时代他曾经独自背着行囊周游大江南北，那些艰苦而充实的旅途岁月磨砺了他坚韧的性格。",
                "pinyin": "Qīngnián shídài tā céngjīng dúzì bēizhe xíngnáng zhōuyóu Dàjiāng-nánběi, nàxiē jiānkǔ ér chōngshí de lǚtú suìyuè mólì le tā jiānrèn de xìnggé.",
                "en": "In his youth he once traveled across the nation alone with a backpack; those arduous and fulfilling journeys honed his resilient character.",
                "es": "En su juventud recorrió en solitario el país con una mochila; aquellas duras y ricas andanzas templaron su tenaz personalidad."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在给友人的信件中曾经深情形容故乡绍兴的乌篷船与社戏，那些童年水乡记忆是他一生的精神慰藉。",
                "pinyin": "Lǔ Xùn zài gěi yǒurén de xìnjiàn zhōng céngjīng shēnqíng xíngróng gùxiāng Shàoxīng de wūpéngchuán yǔ shèxì, nàxiē tóngnián shuǐxiāng jìyì shì tā yìshēng de jīngshén wèijiè.",
                "en": "In letters to friends, Lu Xun once affectionately described the awning boats and village operas of Shaoxing, a lifelong spiritual comfort.",
                "es": "En cartas a amigos, Lu Xun evocó con cariño las barcas de toldo negro y las óperas de Shaoxing, recuerdos de infancia que fueron su consuelo vital."
            }
        ],
        "collocations": [
            {"hanzi": "曾经发生", "en": "once occurred"},
            {"hanzi": "曾经辉煌", "en": "once glorious / historically splendid"},
            {"hanzi": "曾经说过", "en": "once said"},
            {"hanzi": "曾经相识", "en": "once acquainted with each other"},
            {"hanzi": "曾经沧海", "en": "having seen the wide sea (experienced much)"},
            {"hanzi": "曾经拥有", "en": "once possessed"}
        ],
        "idioms": [
            {"hanzi": "曾经沧海", "pinyin": "céng jīng cāng hǎi", "meaning_en": "having sailed the vast ocean, other waters pale in comparison"},
            {"hanzi": "时过境迁", "pinyin": "shí guò jìng qiān", "meaning_en": "time has passed and the circumstances have changed"},
            {"hanzi": "事过境迁", "pinyin": "shì guò jìng qiān", "meaning_en": "things change with the passage of time"},
            {"hanzi": "今非昔比", "pinyin": "jīn fēi xī bǐ", "meaning_en": "the present cannot be compared to the past; dramatic change"}
        ],
        "character_decomposition": [
            {
                "character": "曾",
                "pinyin": "céng",
                "meaning_en": "already; past; once; previous; great-grand-",
                "meaning_es": "ya; antes; otrora; anterior; bis-",
                "radical": "日",
                "radical_meaning_en": "sun / day",
                "meaning_component": "八 (diverge upward) + 丷 (steam)",
                "sound_component": "日 (sun marking past days)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of a clay steaming cauldron with steam rising; borrowed phonetically to signify already passed time.",
                "visual_mnemonic_story_en": "Steam rises into the air above the cauldron, marking past days (日) that have already elapsed (曾).",
                "visual_mnemonic_story_es": "El vapor se eleva sobre la olla cocedora, simbolizando los días (日) ya transcurridos (曾).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "CWA",
                "traditional": ""
            },
            {
                "character": "经",
                "pinyin": "jīng",
                "meaning_en": "pass through; experience; warp; classics",
                "meaning_es": "pasar por; experimentar; urdimbre; clásicos",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (longitudinal warp silk threads)",
                "sound_component": "巠 (jīng, underground water flow / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where longitudinal silk threads 纟 run continuously through the loom, denoting passing through time.",
                "visual_mnemonic_story_en": "Long silk threads (纟) pass through the loom from end to end, weaving experiences along the way (经).",
                "visual_mnemonic_story_es": "Finos hilos de seda (纟) atraviesan el telar de principio a fin, tejiendo el paso del tiempo (经).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VMNOM",
                "traditional": "經"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "What has already elapsed in past days (曾) and passed through life's loom (经) happened previously (曾经).",
            "composite_memory_hook_es": "Lo que ya transcurrió en días idos (曾) y pasó por el telar de la vida (经) ocurrió en otro tiempo (曾经).",
            "cultural_and_cognitive_roots": "A time-aspect adverb dating to Middle Chinese; marks completed experiences situated in a bygone temporal frame, often evoking nostalgic or reflective emotional coloring.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by level high tone: 'céng jīng' (35-55). Smooth rising contour on 'céng', followed by a sustained high tone on 'jīng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "增", "pinyin": "zēng", "meaning_en": "increase", "distinction_note": "Has earth radical 土 on left of 曾"},
                {"character": "赠", "pinyin": "zèng", "meaning_en": "give as gift", "distinction_note": "Has cowrie radical 贝 on left of 曾"},
                {"character": "红", "pinyin": "hóng", "meaning_en": "red", "distinction_note": "Has 工 on right of 纟 instead of 圣/巠"},
                {"character": "轻", "pinyin": "qīng", "meaning_en": "light weight", "distinction_note": "Has vehicle radical 车 on left instead of 纟"}
            ],
            "etymological_cognates": [
                {"character": "往", "pinyin": "wǎng", "gloss_en": "past; go to; former"},
                {"character": "昔", "pinyin": "xī", "gloss_en": "former times; sun over dried meat"},
                {"character": "历", "pinyin": "lì", "gloss_en": "pass through; calendar history"},
                {"character": "过", "pinyin": "guò", "gloss_en": "cross over; pass by on road"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "曾经 is an aspectual adverb indicating that an event definitively took place in the past, often contrasting with the present.",
            "contrasts": [
                {"id": "1", "compared_word": "曾经 vs. 已经", "pinyin": "yǐjīng", "analysis": "已经 indicates that an action is currently completed ('已经做完'), whereas 曾经 emphasizes that it occurred in a bygone past period ('曾经做过')."},
                {"id": "2", "compared_word": "曾经 vs. 从前", "pinyin": "cóngqián", "analysis": "从前 is a time noun meaning 'in the past / once upon a time', while 曾经 is an adverb directly preceding verbal predicates."},
                {"id": "3", "compared_word": "曾经 vs. 过去", "pinyin": "guòqù", "analysis": "过去 functions as a broad noun for the past ('在过去') or directional verb, unlike the preverbal aspect marker 曾经."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "曾经走过的弯路与吃过的苦头，最终都会化作生命中最珍贵的养分。那些在至暗时刻咬牙坚持的岁月，如今回望起来不过是轻舟已过的万重山峦。不必沉溺于过去的遗憾，所有曾经的磨难，都是为了成全今日更坚韧的自己。",
                "pinyin": "Céngjīng zǒuguò de wānlù yǔ chīguò de kǔtou, zuìzhōng dōu huì huàzuò shēngmìng zhōng zuì zhēnguì de yǎngfèn. Nàxiē zài zhì'àn shíkè yǎoyá jiānchí de suìyuè, rújīn huíwàng qǐlái bùguò shì qīngzhōu-yǐguò de wànchóng shānluán. Búbì chénnì yú guòqù de yíhàn, suǒyǒu céngjīng de mónàn, dōu shì wèile chéngquán jīnrì gèng jiānrèn de zìjǐ.",
                "en": "The detours and hardships once endured ultimately become life's richest nutrients. Dark hours endured with grit now seem like distant mountains passed by a swift boat. Regret not the past; all trials forge a stronger self.",
                "es": "Los desvíos y sinsabores vividos antaño terminan siendo el mejor abono del alma. Las horas aciagas resistidas con coraje parecen hoy cumbres lejanas dejadas atrás. No cabe llorar el ayer: las pruebas sufridas forjan la entereza presente."
            },
            {
                "id": "#2",
                "hanzi": "回首近代以来中华民族走过的风雨征程，无数仁人志士曾经为了救亡图存抛头颅洒热血。从积贫积弱的半殖民地旧中国，到今日繁荣昌盛的世界第二大经济体，这片古老大地上曾经饱经沧桑的历史记忆，始终激励着亿万中华儿女奋勇前行。",
                "pinyin": "Huíshǒu jìndài yǐlái Zhōnghuá mínzú zǒuguò de fēngyǔ zhēngchéng, wúshù rénrén-zhìshì céngjīng wèile jiùwáng-túcún pāotóu-sǎrèxuè. Cóng jīpín-jīruò de bàn zhímíndì jiù Zhōngguó, dào jīnrì fánróng-chāngshèng de shìjiè dì-èr dà jīngjìtǐ, zhè piàn gǔlǎo dàdì shàng céngjīng bǎojīng-cāngsāng de lìshǐ jìyì, shǐzhōng jīlì zhe yìwàn Zhōnghuá érnǚ fènyǒng qiánxíng.",
                "en": "Looking back on modern trials, patriots once shed blood to save the nation. From a broken semi-colony to the world's second-largest economy, memories of hardship once endured on this soil inspire millions to advance boldly.",
                "es": "Al contemplar las vicisitudes de la era moderna, incontables patriotas dieron su sangre por la nación. De la humillación colonial al vigor de la segunda potencia económica, las penalidades sufridas antaño alientan a avanzar con tesón."
            }
        ]
    },

    # 35 形容
    {
        "id": "35",
        "hanzi": "形容",
        "pinyin": "xíng róng",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to describe; to depict; to portray; appearance; countenance",
            "es": "describir; retratar; calificar; semblante; apariencia física"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to describe or depict a person's appearance, emotion, or the state of an affair through words or analogies",
                "definition_es": "describir, retratar o calificar el aspecto, ánimo o estado de algo mediante palabras o símiles",
                "example_phrase": "难以用语言形容 (hard to describe in words)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Literary",
                "definition_en": "external physical appearance, facial countenance, or emaciated look",
                "definition_es": "semblante, aspecto físico o traza del rostro",
                "example_phrase": "形容憔悴 (haggard and emaciated appearance)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "站在巍峨的雪山之巅，面对日照金山的壮丽奇观，那种震撼的心情简直无法用言语来形容。",
                "pinyin": "Zhàn zài wéi'é de xuěshān zhī diān, miànduì rìzhào-jīnshān de zhuànglì qíguān, nà zhǒng zhènhàn de xīnqíng jiǎnzhí wúfǎ yòng yányǔ lái xíngróng.",
                "en": "Standing atop the snow-capped peak before the golden sunrise, that awe-inspiring emotion simply defies verbal description.",
                "es": "En la cumbre de la montaña nevada ante el amanecer dorado, la honda emoción que sentí resulta imposible de describir con palabras."
            },
            {
                "id": "#2",
                "hanzi": "郁达夫曾撰文形容鲁迅先生的相貌与风度：“醉眼朦胧，悠悠自得”，生动勾勒出鲁迅文人生活的一面。",
                "pinyin": "Yù Dáfū céng zhuànwén xíngróng Lǔ Xùn xiānsheng de xiàngmào yǔ fēngdù: 'zuìyǎn ménglóng, yōuyōu zìdé', shēngdòng gōulè chū Lǔ Xùn wénrén shēnghuó de yí miàn.",
                "en": "Yu Dafu once described Mr. Lu Xun's countenance: 'eyes hazy from wine, leisurely and content', vividly sketching his literati lifestyle.",
                "es": "Yu Dafu describió la traza de Lu Xun: 'ojos entornados por el vino, plácido y dueño de sí', retratando con viveza su temple letrado."
            }
        ],
        "collocations": [
            {"hanzi": "难以形容", "en": "hard to describe"},
            {"hanzi": "恰当形容", "en": "describe appropriately"},
            {"hanzi": "用来形容", "en": "used to describe"},
            {"hanzi": "形容词", "en": "adjective (grammar)"},
            {"hanzi": "形容憔悴", "en": "haggard and emaciated look"},
            {"hanzi": "生动形容", "en": "vividly describe"}
        ],
        "idioms": [
            {"hanzi": "不可名状", "pinyin": "bù kě míng zhuàng", "meaning_en": "indescribable; beyond words to depict"},
            {"hanzi": "惟妙惟肖", "pinyin": "wéi miào wéi xiào", "meaning_en": "depicted with consummate lifelikeness and fidelity"},
            {"hanzi": "绘声绘色", "pinyin": "huì shēng huì sè", "meaning_en": "describe with vivid sound and color; picturesque"},
            {"hanzi": "妙语连珠", "pinyin": "miào yǔ lián zhū", "meaning_en": "sparkling pearls of wit flow in rapid succession"}
        ],
        "character_decomposition": [
            {
                "character": "形",
                "pinyin": "xíng",
                "meaning_en": "form; shape; appearance; body; depict",
                "meaning_es": "forma; figura; cuerpo; aspecto; plasmar",
                "radical": "彡",
                "radical_meaning_en": "hair / bristles / pattern",
                "meaning_component": "彡 (hair/artistic brushstrokes)",
                "sound_component": "开 (kāi, frame / phonetic harmony)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where elegant brushstrokes 彡 sketch out visible physical contours.",
                "visual_mnemonic_story_en": "Delicate brushstrokes (彡) trace out the physical contours and visible shape (形) of an object.",
                "visual_mnemonic_story_es": "Trazos de pincel (彡) dibujan los contornos y la figura visible (形) de un cuerpo.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MTHH",
                "traditional": ""
            },
            {
                "character": "容",
                "pinyin": "róng",
                "meaning_en": "countenance; look; contain; tolerate",
                "meaning_es": "semblante; rostro; contener; tolerar",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (sheltering roof) + 谷 (valley mouth)",
                "sound_component": "容 (róng)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ideogram showing a spacious valley 谷 sheltered under a roof 宀, meaning accommodating; extended to facial appearance.",
                "visual_mnemonic_story_en": "Under the roof (宀), a serene valley (谷) accommodates all things, reflecting peaceful facial countenance (容).",
                "visual_mnemonic_story_es": "Bajo el alero (宀), el amplio valle (谷) acoge los arroyos, reflejando el rostro sereno (容).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JCOR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Observe external shapes (形) and facial countenance (容) to vividly describe and portray reality (形容).",
            "composite_memory_hook_es": "Observa la figura externa (形) y el semblante (容) para describir la realidad con maestría (形容).",
            "cultural_and_cognitive_roots": "Originally denoted a person's physical demeanor and facial looks ('xíngtài róngmào'); in classical rhetoric it shifted into using verbal similes to capture essence.",
            "tone_sandhi_and_pitch_modulation": "Two rising tones: 'xíng róng' (35-35). Two steady parallel rising glides from mid to high pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "刑", "pinyin": "xíng", "meaning_en": "punishment", "distinction_note": "Has knife radical 刂 on right instead of 彡 in 形"},
                {"character": "型", "pinyin": "xíng", "meaning_en": "mold; type", "distinction_note": "Has earth radical 土 below 刑"},
                {"character": "客", "pinyin": "kè", "meaning_en": "guest", "distinction_note": "Has 各 below 宀 instead of 谷 in 容"},
                {"character": "谷", "pinyin": "gǔ", "meaning_en": "valley", "distinction_note": "Lacks the top roof radical 宀 of 容"}
            ],
            "etymological_cognates": [
                {"character": "描", "pinyin": "miáo", "gloss_en": "trace; describe with hand"},
                {"character": "摹", "pinyin": "mó", "gloss_en": "imitate; trace outline on paper"},
                {"character": "写", "pinyin": "xiě", "gloss_en": "sketch; write lifelike scene"},
                {"character": "绘", "pinyin": "huì", "gloss_en": "draw; paint colorful pictures"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "形容 emphasizes using verbal metaphors, adjectives, or analogies to portray physical appearance or sensory experience.",
            "contrasts": [
                {"id": "1", "compared_word": "形容 vs. 描写", "pinyin": "miáoxiě", "analysis": "描写 denotes systematic literary prose depicting scenes or actions in extended paragraphs, while 形容 is frequently used for concise qualitative analogies ('用...来形容')."},
                {"id": "2", "compared_word": "形容 vs. 描述", "pinyin": "miáoshù", "analysis": "描述 is a formal, objective verb for narrating facts or procedural details ('描述事故经过'), whereas 形容 emphasizes figurative imagery."},
                {"id": "3", "compared_word": "形容 vs. 形象", "pinyin": "xíngxiàng", "analysis": "形容 is a verb (to describe), whereas 形象 is primarily a noun (image/figure) or adjective (vivid/graphic)."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "大自然造化之美，往往超越了人类语言形容的极限。黄昏时分夕阳熔金，漫天晚霞将整片海面染成了瑰丽的紫红色，波光潋滟美不胜收。面对如此雄奇壮丽的天地大美，任何华丽的修辞都显得苍白无力，唯有静默赞叹。",
                "pinyin": "Dàzìrán zàohuà zhī měi, wǎngwǎng chāoyuè le rénlèi yǔyán xíngróng de jíxiàn. Huánghūn shífēn xīyáng róngjīn, màntiān wǎnxiá jiāng zhěng piàn hǎimiàn rǎnchéng le guīlì de zǐhóngsè, bōguāng-liànyàn měibùshèngshōu. Miànduì rúcǐ xióngqí zhuànglì de tiāndì dàměi, rènhé huálì de xiūcí dōu xiǎnde cāngbái-wúlì, wéiyǒu jìngmò zàntàn.",
                "en": "Nature's beauty often exceeds the limits of human description. At dusk, melting golden sunsets dye the entire sea in magnificent violet. Facing such grand splendor, any ornate rhetoric pales; only reverent silence remains.",
                "es": "La creación natural desborda los límites de la descripción humana. Al crepúsculo, el sol poniente tiñe las olas de un púrpura fastuoso. Ante tanta majestuosidad, cualquier retórica resulta vana y solo cabe el silencio extasiado."
            },
            {
                "id": "#2",
                "hanzi": "优秀的文学家总能以独特的洞察力提炼出生动传神的比喻。在现代文学经典名篇中，鲁迅以“风马牛不相及”形容世态的冷漠隔阂，用“路是人走出来的”形象激励青年勇于开拓。这些贴切生动的形容，具有穿越时代的永恒艺术生命力。",
                "pinyin": "Yōuxiù de wénxuéjiā zǒng néng yǐ dútè de dòngchálì tíliàn chū shēngdòng chuánshén de bǐyù. Zài xiàndài wénxué jīngdiǎn míngpiān zhōng, Lǔ Xùn yǐ 'fēngmǎniú bù xiāng jí' xíngróng shìtài de lěngmò géhé, yòng 'lù shì rén zǒuchūlái de' xíngxiàng jīlì qīngnián yǒngyú kāituò. Zhèxiē tiēqiè shēngdòng de xíngróng, jùyǒu chuānyuè shídài de yǒnghéng yìshù shēngmìnglì.",
                "en": "Master authors extract vivid metaphors with keen insight. In classic essays, Lu Xun described social indifference with pungent sayings and encouraged youth by writing 'paths are made by walking'. Such apt descriptions possess timeless vitality.",
                "es": "Los grandes literatos forjan metáforas imborrables. En sus clásicos, Lu Xun calificó la frialdad social con mordaces símiles y exhortó a los jóvenes recordando que el camino se hace al andar. Tales descripciones atesoran vigencia eterna."
            }
        ]
    },

    # 36 朦胧
    {
        "id": "36",
        "hanzi": "朦胧",
        "pinyin": "méng lóng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "hazy; dim; obscure; misty; blurred (from wine, mist, or twilight)",
            "es": "brumoso; borroso; tenue; velado; difuso; soñoliento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "dim, indistinct, or blurred in sight or consciousness due to moonlight, mist, sleepiness, or light intoxication",
                "definition_es": "tenue, borroso o poco nítido para la vista o la conciencia por la niebla, el crepúsculo o el vino",
                "example_phrase": "月色朦胧 (hazy moonlight)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清晨薄雾笼罩着湖畔，远处的亭台楼阁与垂柳在朦胧的水汽中若隐若现，宛如水墨仙境。",
                "pinyin": "Qīngchén báowù lǒngzhào zhe húpàn, yuǎnchù de tíngtái-lóugé yǔ chuíliǔ zài ménglóng de shuǐqì zhōng ruòyǐn-ruòxiàn, wǎnrú shuǐmò xiānjìng.",
                "en": "Morning mist enshrouded the lakeshore; distant pavilions and willows faded in and out in hazy vapor like an ink-wash dreamland.",
                "es": "La neblina matinal cubría la orilla; quioscos y sauces llorones asomaban entre el vaho brumoso como una acuarela de hadas."
            },
            {
                "id": "#2",
                "hanzi": "友人撰文回忆鲁迅宴饮时的神采，称他酒过三巡后“醉眼朦胧”，神情极为亲切和蔼，尽显文人真性情。",
                "pinyin": "Yǒurén zhuànwén huíyì Lǔ Xùn yànyǐn shí de shéncǎi, chēng tā jiǔguò-sānxún hòu 'zuìyǎn ménglóng', shénqíng jíwéi qīnqiè hé'ǎi, jìnxiǎn wénrén zhēnxìngqíng.",
                "en": "Friends recalled Lu Xun's demeanor after wine: 'eyes hazy from drink', warmly amiable, revealing his genuine literati nature.",
                "es": "Sus amigos recordaban a Lu Xun tras brindar varias rondas: con los ojos entornados y brumosos, cordial y mostrando su genio más franco."
            }
        ],
        "collocations": [
            {"hanzi": "月色朦胧", "en": "hazy moonlight"},
            {"hanzi": "睡眼朦胧", "en": "eyes hazy with sleep"},
            {"hanzi": "醉眼朦胧", "en": "eyes dim and hazy with wine"},
            {"hanzi": "朦胧美", "en": "hazy aesthetic beauty"},
            {"hanzi": "朦胧的记忆", "en": "hazy/dim memories"},
            {"hanzi": "夜色朦胧", "en": "dimly obscure night"}
        ],
        "idioms": [
            {"hanzi": "若隐若现", "pinyin": "ruò yǐn ruò xiàn", "meaning_en": "partly hidden and partly visible; faint"},
            {"hanzi": "雾里看花", "pinyin": "wù lǐ kàn huā", "meaning_en": "view flowers through mist; vague, blurred perception"},
            {"hanzi": "扑朔迷离", "pinyin": "pū shuò mí lí", "meaning_en": "complicated, confusing, and difficult to unravel"},
            {"hanzi": "浮想联翩", "pinyin": "fú xiǎng lián piān", "meaning_en": "thoughts and fancies drift in rapid succession"}
        ],
        "character_decomposition": [
            {
                "character": "朦",
                "pinyin": "méng",
                "meaning_en": "dim moonlight; obscure; hazy",
                "meaning_es": "luna tenue; brumoso; velado",
                "radical": "月",
                "radical_meaning_en": "moon",
                "meaning_component": "月 (moon behind clouds)",
                "sound_component": "蒙 (méng, cover / blind / phonetic)",
                "stroke_count": 17,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where the moon 月 is obscured and covered 蒙 by drifting mist and night clouds.",
                "visual_mnemonic_story_en": "The pale moon (月) is wrapped in covered veils of cloud (蒙), shedding dim, hazy light (朦).",
                "visual_mnemonic_story_es": "La pálida luna (月) queda envuelta bajo velos de nubes (蒙), emitiendo una luz tenue y brumosa (朦).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BTOE",
                "traditional": ""
            },
            {
                "character": "胧",
                "pinyin": "lóng",
                "meaning_en": "dim; twilight; cloudy moon",
                "meaning_es": "difuso; crepúsculo; luna velada",
                "radical": "月",
                "radical_meaning_en": "moon",
                "meaning_component": "月 (moon)",
                "sound_component": "龙 (lóng, dragon / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where the nocturnal moon 月 shines indistinctly like a dragon 龙 concealed in clouds.",
                "visual_mnemonic_story_en": "The nocturnal crescent moon (月) drifts like a dragon (龙) through misty night fog, creating twilight (胧).",
                "visual_mnemonic_story_es": "La luna creciente (月) serpentea como un dragón (龙) entre la niebla nocturna creando un halo difuso (胧).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BIKP",
                "traditional": "朧"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When the moon is shrouded by clouds (朦) and drifts like a twilight dragon (胧), the landscape turns hazy and dim (朦胧).",
            "composite_memory_hook_es": "Cuando la luna queda velada (朦) y serpentea en la penumbra (胧), el paisaje se torna brumoso y difuso (朦胧).",
            "cultural_and_cognitive_roots": "A celebrated aesthetic term in classical Chinese poetry; 'ménglóng' values evocative poetic indeterminacy ('朦胧诗') over stark, clinical clarity.",
            "tone_sandhi_and_pitch_modulation": "Two rising tones: 'méng lóng' (35-35). Two gentle, continuous upward sweeps capturing the soft, indistinct imagery."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "蒙", "pinyin": "méng", "meaning_en": "cover; ignorant", "distinction_note": "Has grass radical 艹 at top; lacks left moon radical 月"},
                {"character": "朦", "pinyin": "méng", "meaning_en": "dim moon", "distinction_note": "Pair with 胧; do not confuse with 庞 (large/face)"},
                {"character": "珑", "pinyin": "lóng", "meaning_en": "tinkling jade", "distinction_note": "Has jade radical 王 on left instead of 月"},
                {"character": "笼", "pinyin": "lóng", "meaning_en": "cage; basket", "distinction_note": "Has bamboo radical 竹 at top instead of 月"}
            ],
            "etymological_cognates": [
                {"character": "雾", "pinyin": "wù", "gloss_en": "fog; water droplets in air"},
                {"character": "霭", "pinyin": "ǎi", "gloss_en": "mist; evening twilight clouds"},
                {"character": "茫", "pinyin": "máng", "gloss_en": "vast; blurred; water expanse"},
                {"character": "恍", "pinyin": "huǎng", "gloss_en": "dimly; as if in a daze"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "朦胧 characterizes a soft, aesthetically pleasing indistinctness caused by moonlight, mist, sleep, or mild wine.",
            "contrasts": [
                {"id": "1", "compared_word": "朦胧 vs. 模糊", "pinyin": "móhu", "analysis": "模糊 is an everyday, technical term for blurred vision, damaged lenses, or indistinct logic, whereas 朦胧 carries strong poetic, evocative beauty."},
                {"id": "2", "compared_word": "朦胧 vs. 隐约", "pinyin": "yǐnyuē", "analysis": "隐约 can describe both faint sights and distant sounds ('隐约听到'), while 朦胧 predominantly describes visual twilight, mist, or mental haze."},
                {"id": "3", "compared_word": "朦胧 vs. 明晰", "pinyin": "míngxī", "analysis": "明晰 (crystal clear and sharply defined) is the direct antonym of 朦胧."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "江南春夜，月色朦胧。细雨初歇的石板路上倒映着点点红灯笼的光晕，乌篷船在桨声灯影里悠然摇曳。古镇在湿润的水汽中半睡半醒，那种若即若离的朦胧诗意，宛如一幅晕染开来的宋代山水长卷，令人沉醉不知归路。",
                "pinyin": "Jiāngnán chūnyè, yuèxiè ménglóng. Xìyǔ chū xiē de shíbǎnlù shàng dàoyìng zhe diǎndiǎn hóng dēnglong de guāngyùn, wūpéngchuán zài jiǎngshēng-dēngyǐng lǐ yōurán yáoyè. Gǔzhèn zài shīrùn de shuǐqì zhōng bànshuì-bànxǐng, nà zhǒng ruòjí-ruòlí de ménglóng shīyì, wǎnrú yì fú yùnrǎn kāilái de Sòngdài shānshuǐ chángjuàn, lìngrén chénzuì bùzhī guīlù.",
                "en": "On a spring night south of the Yangtze, the moon shines hazy. Lantern glows shimmer on wet stone paths as awning boats sway. Half-awake in mist, the ancient town's poetic haze intoxicates like a Song landscape scroll.",
                "es": "En la noche primaveral del sur, la luna brilla tenue. Los farolillos rojos se reflejan en el empedrado mientras las barcas se mecen. Entre la bruma húmeda, el pueblo antiguo destila una poesía que embriaga como un lienzo Song."
            },
            {
                "id": "#2",
                "hanzi": "在二十世纪七八十年代的中国诗坛上，“朦胧诗”派以其独特的艺术探索开创了现代诗歌的新纪元。诗人通过多义性的意象组合与富有哲思的意境留白，打破了传统现实主义诗歌单一说教的僵化模式，唤醒了无数读者对于人性、尊严与独立思考的深刻觉醒。",
                "pinyin": "Zài èrshí shìjì qībāshí niándài de Zhōngguó shītán shàng, 'Ménglóngshī' pài yǐ qí dútè de yìshù tànsuǒ kāichuàng le xiàndài shīgē de xīn jìyuán. Shīrén tōngguò duōyìxìng de yìxiàng zǔhé yǔ fùyǒu zhésī de yìjìng liúbái, dǎpò le chuántǒng xiànshí zhǔyì shīgē dānyī shuōjiào de jiānghuà móshì, huànxǐng le wúshù dúzhě duìyú rénxìng, zūnyán yǔ dúlì sīkǎo de shēnkè juéxǐng.",
                "en": "In late 20th-century Chinese poetry, the 'Misty Poets' opened a new era through artistic exploration. Multi-layered imagery and reflective spaces shattered rigid didacticism, awakening readers to human dignity and independent thought.",
                "es": "La corriente de la 'Poesía Brumosa' inauguró una nueva era en las letras chinas. Sus metáforas polisémicas y silencios meditados rompieron el didactismo monolítico, despertando la dignidad humana y el pensamiento crítico en millones de lectores."
            }
        ]
    },

    # 37 悠悠
    {
        "id": "37",
        "hanzi": "悠悠",
        "pinyin": "yōu yōu",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "leisurely; unhurried; lingering; protracted; long-drawn-out; endless (of time)",
            "es": "apacible; sosegado; parsimonioso; prolongado; interminable; milenario"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "leisurely, relaxed, slow, and completely free from rush or anxiety",
                "definition_es": "sosegado, tranquilo, pausado y sin prisas ni agobios",
                "example_phrase": "闲情悠悠 (leisurely and carefree mood)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Literary",
                "definition_en": "long, protracted, or lingering continuously across vast expanses of time or space",
                "definition_es": "prolongado, interminable o milenario a través de eras remotas o distancias",
                "example_phrase": "悠悠岁月 (the long, lingering years)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "山间古寺钟声悠悠回荡在云雾缭绕的峡谷之中，洗涤着红尘过客心头的浮躁与疲惫。",
                "pinyin": "Shānjiān gǔsì zhōngshēng yōuyōu huídàng zài yúnwù-liáorào de xiágǔ zhīzhōng, xǐdí zhe hóngchén guòkè xīntóu de fúzào yǔ píbèi.",
                "en": "The bell of the mountain temple echoed leisurely and lingeringly in the mist-veiled canyon, washing away travelers' restless fatigue.",
                "es": "La campana del templo serrano resonaba con pausado eco en el cañón cubierto de niebla, lavando las fatigas del caminante."
            },
            {
                "id": "#2",
                "hanzi": "在老友郁达夫笔下，鲁迅饮酒微醺时有着“悠悠自得”的神态，那是严峻斗士卸下防备后最本真的文人风骨。",
                "pinyin": "Zài lǎoyǒu Yù Dáfū bǐxià, Lǔ Xùn yǐnjiǔ wēixūn shí yǒuzhe 'yōuyōu-zìdé' de shéntài, nà shì yánjùn dòushì xièxià fángbèi hòu zuì běnzhēn de wénrén fēnggǔ.",
                "en": "In friend Yu Dafu's words, when Lu Xun was slightly tipsy he wore an unhurried, content air, the authentic grace of a warrior letting down his guard.",
                "es": "En la pluma de Yu Dafu, Lu Xun lucía un porte sosegado al brindar, revelando la entraña franca del luchador que desciende la guardia."
            }
        ],
        "collocations": [
            {"hanzi": "悠悠岁月", "en": "the long, lingering years"},
            {"hanzi": "悠悠自得", "en": "leisurely and content with oneself"},
            {"hanzi": "悠悠琴声", "en": "lingering notes of the zither"},
            {"hanzi": "历史悠悠", "en": "long, protracted history"},
            {"hanzi": "悠悠白云", "en": "slow-drifting white clouds"},
            {"hanzi": "钟声悠悠", "en": "leisurely chime of the bell"}
        ],
        "idioms": [
            {"hanzi": "悠然自得", "pinyin": "yōu rán zì dé", "meaning_en": "carefree and leisurely; completely self-content"},
            {"hanzi": "从容不迫", "pinyin": "cóng róng bú pò", "meaning_en": "calm, unhurried, and unruffled"},
            {"hanzi": "白云苍狗", "pinyin": "bái yún cāng gǒu", "meaning_en": "white clouds turn into grey dogs; swift worldly vicissitudes"},
            {"hanzi": "悠悠忽忽", "pinyin": "yōu yōu hū hū", "meaning_en": "in a dazed, unhurried reverie"}
        ],
        "character_decomposition": [
            {
                "character": "悠",
                "pinyin": "yōu",
                "meaning_en": "long; leisurely; distant; lingering",
                "meaning_es": "largo; apacible; lejano; pausado",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "心 (heart/peace)",
                "sound_component": "攸 (yōu, flowing water line / phonetic)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character combining heart 心 with 攸 (flowing calm water), denoting an unruffled, relaxed soul and lingering distance.",
                "visual_mnemonic_story_en": "A calm heart (心) flows like gentle unhurried water (攸), resting in peaceful leisure and lingering time (悠).",
                "visual_mnemonic_story_es": "Un corazón sereno (心) fluye como agua mansa (攸), descansando en dulce sosiego y tiempo prolongado (悠).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OKP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A calm, unhurried heart duplicated twice (悠悠) floats leisurely across vast expanses of time (悠悠).",
            "composite_memory_hook_es": "Un corazón sosegado repetido dos veces (悠悠) flota con parsimonia a través del tiempo milenario (悠悠).",
            "cultural_and_cognitive_roots": "A classical poetic reduplication found in the Book of Songs (诗经: '青青子衿，悠悠我心'); conveys the lingering emotional resonance of longing, leisurely contentment, and deep historical time.",
            "tone_sandhi_and_pitch_modulation": "Two high level tones: 'yōu yōu' (55-55). Sustained, steady high plateau pitch capturing peaceful, prolonged flow."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "您", "pinyin": "nín", "meaning_en": "you (polite)", "distinction_note": "Has 你 at top over 心 instead of 攸"},
                {"character": "您", "pinyin": "yōu", "meaning_en": "long", "distinction_note": "Do not confuse with 愁 (has 禾 and 火 over 心)"},
                {"character": "怒", "pinyin": "nù", "meaning_en": "anger", "distinction_note": "Has 奴 over 心 instead of 攸"},
                {"character": "怨", "pinyin": "yuàn", "meaning_en": "resentment", "distinction_note": "Has 夗 over 心 instead of 攸"}
            ],
            "etymological_cognates": [
                {"character": "闲", "pinyin": "xián", "gloss_en": "leisure; moonlight through gate"},
                {"character": "逸", "pinyin": "yì", "gloss_en": "ease; rabbit escaping into freedom"},
                {"character": "舒", "pinyin": "shū", "gloss_en": "relax; stretch out gently"},
                {"character": "漫", "pinyin": "màn", "gloss_en": "free-flowing; boundless water"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "悠悠 describes the unhurried, peaceful tempo of life, or the vast, lingering passage of historical time and musical echoes.",
            "contrasts": [
                {"id": "1", "compared_word": "悠悠 vs. 悠闲", "pinyin": "yōuxián", "analysis": "悠闲 strictly describes an individual's leisurely lifestyle or relaxed mood, while 悠悠 can describe lingering sounds, vast centuries ('悠悠万事'), or drifting clouds."},
                {"id": "2", "compared_word": "悠悠 vs. 漫长", "pinyin": "màncháng", "analysis": "漫长 emphasizes lengthy, tedious duration ('漫长的等待'), while 悠悠 carries poetic, nostalgic, and serene grace."},
                {"id": "3", "compared_word": "悠悠 vs. 匆匆", "pinyin": "cōngcōng", "analysis": "匆匆 (hurried and rushed in haste) is the direct semantic antonym of 悠悠."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "放慢匆忙的脚步，才能听见生活悠悠流淌的清音。坐在老藤椅上泡一盏淡茶，看庭前落花随风起舞，天边白云悠悠远去。不必焦虑未来的风雨，在这份不慌不忙的从容里，灵魂方能重获久违的安顿与宁静。",
                "pinyin": "Fàngmàn cōngmáng de jiǎobù, cáinéng tīngjiàn shēnghuó yōuyōu liútǎng de qīngyīn. Zuò zài lǎoténgyǐ shàng pào yì zhǎn dànchá, kàn tíngqián luòhuā suífēng qǐwǔ, tiānbiān báiyún yōuyōu yuǎnqù. Búbì jiāolǜ wèilái de fēngyǔ, zài zhè fèn bùhuāng-bùmáng de cóngróng lǐ, línghún fāng néng chónghuò jiǔwéi de āndùn yǔ níngjìng.",
                "en": "Slowing rushed footsteps allows one to hear life's gentle melody. Sipping tea in a rattan chair, watching fallen flowers dance and clouds drift afar, anxieties fade as the soul regains peace in unhurried composure.",
                "es": "Frenar las prisas permite escuchar el rumor apacible de la vida. En una mecedora con té tibio, viendo bailar las flores y pasar nubes lentas, se disipan los desvelos y el alma recobra su sosiego soñado."
            },
            {
                "id": "#2",
                "hanzi": "五千年华夏文明历经悠悠岁月的洗礼，展现出坚韧不拔的强大生命力。从甲骨青铜的深邃记忆，到唐诗宋词的绝美华章，滚滚长江东逝水淘尽千古风流，唯有那份深植于血脉深处的文化自信，在历史长河中历久弥新、生生不息。",
                "pinyin": "Wǔqiān nián Huáxià wénmíng lìjīng yōuyōu suìyuè de xǐlǐ, zhǎnxiàn chū jiānrèn-bùbá de qiángdà shēngmìnglì. Cóng jiǎgǔ-qīngtóng de shēnsuì jìyì, dào Tángshī-Sòngcí de juéměi huázhāng, gǔngǔn Chángjiāng dōng shì shuǐ táojìn qiāngǔ fēngliú, wéiyǒu nà fèn shēnzhí yú xuèmài shēnchù de wénhuà zìxìn, zài lìshǐ chánghé zhōng lìjiǔ-míxīn, shēngshēng-bùxī.",
                "en": "Tested by lingering millennia, five thousand years of Chinese civilization reveal enduring vigor. From oracle bronzes to Tang and Song poetry, though rivers wash away heroes, deep cultural confidence remains immortal and vibrant.",
                "es": "A lo largo de eras milenarias, la civilización china muestra una recia vitalidad. De los bronces arcaicos a la lírica de Tang y Song, aunque las aguas del Yangtsé arrastren héroes, la confianza cultural florece perenne."
            }
        ]
    },

    # 38 形象
    {
        "id": "38",
        "hanzi": "形象",
        "pinyin": "xíng xiàng",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "image; figure; public profile; vivid; graphic; figurative",
            "es": "imagen; figura; semblanza; perfil público; gráfico; vívido; elocuente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "external appearance, artistic persona, or corporate/public reputational image",
                "definition_es": "imagen pública, figura artística, semblanza moral o prestigio corporativo",
                "example_phrase": "树立良好形象 (establish a good public image)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "vivid, graphic, concrete, and visually expressive in language or metaphor",
                "definition_es": "gráfico, vívido, plástico y expresivo al ilustrar conceptos con metáforas",
                "example_phrase": "比喻非常形象 (the metaphor is extremely vivid)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老师用切苹果的分数比喻深入浅出，十分形象地解释了抽象的数学原理，让同学们豁然开朗。",
                "pinyin": "Lǎoshī yòng qiē píngguǒ de fēnshù bǐyù shēnrù-qiǎnchū, shífēn xíngxiàng de jiěshì le chōuxiàng de shùxué yuánlǐ, ràng tóngxuémen huòrán-kāilǎng.",
                "en": "Using sliced apples to illustrate fractions, the teacher explained abstract principles vividly, enlightening the students.",
                "es": "El maestro explicó principios matemáticos abstractos mediante un elocuente símil con manzanas cortadas, iluminando a los alumnos."
            },
            {
                "id": "#2",
                "hanzi": "在现代读者心中，鲁迅先生往往被塑造成金刚怒目的斗士形象，但研读其日常书信，才能触摸到一个有血有肉的完整鲁迅。",
                "pinyin": "Zài xiàndài dúzhě xīnzhōng, Lǔ Xùn xiānsheng wǎngwǎng bèi sùzào chéng jīngāng-nùmù de dòushì xíngxiàng, dàn yándú qí rìcháng shūxìn, cáinéng chùmō dào yí ge yǒuxuè-yǒuròu de wánzhěng Lǔ Xùn.",
                "en": "To modern readers, Lu Xun is often cast as an uncompromising warrior; yet reading his letters reveals a complete, flesh-and-blood human being.",
                "es": "Los lectores suelen imaginar a Lu Xun como un combatiente de ceño adusto; mas al leer su correspondencia se descubre a un ser entrañable de carne y hueso."
            }
        ],
        "collocations": [
            {"hanzi": "树立形象", "en": "establish an image"},
            {"hanzi": "企业形象", "en": "corporate image/branding"},
            {"hanzi": "形象生动", "en": "vivid and graphic"},
            {"hanzi": "形象大使", "en": "brand/image ambassador"},
            {"hanzi": "文学形象", "en": "literary character/figure"},
            {"hanzi": "形象思维", "en": "thinking in images / visual thinking"}
        ],
        "idioms": [
            {"hanzi": "绘声绘色", "pinyin": "huì shēng huì sè", "meaning_en": "describe vividly in vibrant sound and color"},
            {"hanzi": "栩栩如生", "pinyin": "xǔ xǔ rú shēng", "meaning_en": "vivid as if alive; lifelike"},
            {"hanzi": "顶天立地", "pinyin": "dǐng tiān lì dì", "meaning_en": "stand upright between heaven and earth; heroic stature"},
            {"hanzi": "深入人心", "pinyin": "shēn rù rén xīn", "meaning_en": "strike deep roots in the hearts of the people"}
        ],
        "character_decomposition": [
            {
                "character": "形",
                "pinyin": "xíng",
                "meaning_en": "form; shape; appearance; body",
                "meaning_es": "forma; figura; cuerpo; aspecto",
                "radical": "彡",
                "radical_meaning_en": "hair / pattern",
                "meaning_component": "彡 (hair/artistic brushstrokes)",
                "sound_component": "开 (frame / phonetic harmony)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where elegant brushstrokes 彡 trace out the outer shape of an entity.",
                "visual_mnemonic_story_en": "Fine brushstrokes (彡) define the physical form and visible silhouette (形) of a living figure.",
                "visual_mnemonic_story_es": "Trazos de pincel (彡) dibujan la figura externa y la silueta visible (形) de un ser.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MTHH",
                "traditional": ""
            },
            {
                "character": "象",
                "pinyin": "xiàng",
                "meaning_en": "elephant; image; phenomenon; resemble",
                "meaning_es": "elefante; imagen; fenómeno; asemejarse",
                "radical": "豕",
                "radical_meaning_en": "pig / beast",
                "meaning_component": "象 (ancient oracle bone pictogram of an elephant)",
                "sound_component": "象 (xiàng)",
                "stroke_count": 11,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of an elephant with long trunk, large ears, and stout body; extended to the concept of form, mental image, and phenomenon.",
                "visual_mnemonic_story_en": "An elephant with curved trunk and stout body outlines a grand iconic mental image (象).",
                "visual_mnemonic_story_es": "Un elefante de larga trompa y cuerpo robusto perfila una imagen icónica y palpable (象).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NAHO",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Combine physical form (形) with the vivid iconic presence of the elephant (象) to build a powerful image (形象).",
            "composite_memory_hook_es": "Aúna la forma física (形) con la figura elocuente del elefante (象) para forjar una imagen vívida (形象).",
            "cultural_and_cognitive_roots": "According to Han Feizi, ancient Chinese rarely saw living elephants, so they imagined their shape by studying elephant bones (见其骨而象之); thus 'xiàng' became the root for mental images, symbols, and metaphors.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone: 'xíng xiàng' (35-51). Syllable 'xíng' glides upward, followed by a crisp descending drop on 'xiàng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "刑", "pinyin": "xíng", "meaning_en": "punishment", "distinction_note": "Has knife radical 刂 on right instead of 彡 in 形"},
                {"character": "免", "pinyin": "miǎn", "meaning_en": "exempt; avoid", "distinction_note": "Lacks the top snout and tusks structure of 象"},
                {"character": "像", "pinyin": "xiàng", "meaning_en": "resemble; statue", "distinction_note": "Has person radical 亻 on left of 象"},
                {"character": "豫", "pinyin": "yù", "meaning_en": "hesitate; Henan", "distinction_note": "Has 予 on left side of 象"}
            ],
            "etymological_cognates": [
                {"character": "相", "pinyin": "xiàng", "gloss_en": "appearance; mutual look"},
                {"character": "状", "pinyin": "zhuàng", "gloss_en": "shape; state; appearance"},
                {"character": "影", "pinyin": "yǐng", "gloss_en": "shadow; reflection; cinema"},
                {"character": "态", "pinyin": "tài", "gloss_en": "bearing; posture; state"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "形象 denotes public reputational image, artistic fictional character, or functions as an adjective meaning vivid and graphic.",
            "contrasts": [
                {"id": "1", "compared_word": "形象 vs. 现象", "pinyin": "xiànxiàng", "analysis": "现象 refers to objective natural or societal occurrences and manifestations ('自然现象'), while 形象 refers to personal reputational persona or vivid metaphor."},
                {"id": "2", "compared_word": "形象 vs. 印象", "pinyin": "yìnxiàng", "analysis": "印象 is the subjective impression left in someone's memory ('第一印象'), whereas 形象 is the objective persona projected outwards."},
                {"id": "3", "compared_word": "形象 vs. 生动", "pinyin": "shēngdòng", "analysis": "生动 emphasizes dynamic lifelikeness and animated charm, while 形象 as an adjective emphasizes clear, graphic metaphorical representation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "一个人的外在形象，是其内在涵养与精神风貌的直观投射。得体的谈吐、沉稳的举止与真诚的眼神，往往胜过一切华丽的名牌包装。保持干净大方的个人形象，不仅是对他人的基本尊重，更是对自己人格尊严的郑重守护。",
                "pinyin": "Yí ge rén de wàizài xíngxiàng, shì qí nèizài hányǎng yǔ jīngshén fēngmào de zhíguān tóushè. Détǐ de tántǔ, chénwěn de jǔzhǐ yǔ zhēnchéng de yǎnshén, wǎngwǎng shèngguò yíqiè huálì de míngpái bāozhuāng. Bǎochí gānjìng-dàfang de gèrén xíngxiàng, bùjǐn shì duì tārén de jīběn zūnzhòng, gèng shì duì zìjǐ réngé zūnyán de zhèngzhòng shǒuhù.",
                "en": "Personal image is a direct reflection of inner culture. Proper speech, steady posture, and sincere eyes outweigh luxury packaging. Maintaining a clean, dignified image respects others and solemnly guards one's own dignity.",
                "es": "La imagen exterior proyecta el cultivo interior y la compostura. El hablar mesurado, el porte firme y la mirada limpia superan a las marcas de lujo. Guardar una traza pulcra y cabal honra al prójimo y protege la propia dignidad."
            },
            {
                "id": "#2",
                "hanzi": "中国国家形象的全球传播正在从宏大叙事转向具象生动的人文表达。纪录片与影视出海团队通过聚焦当代普通中国人的奋斗打拼与温情日常，将古老东方的深厚底蕴生动具象化。这种真实接地气的文化形象，有效增进了全球民心相通。",
                "pinyin": "Zhōngguó guójiā xíngxiàng de quánqiú chuánbō zhèngzài cóng hóngdà xùshì zhuǎnxiàng jùxiàng shēngdòng de rénwén biǎodá. Jìlùpiàn yǔ yǐngshì chūhǎi tuánduì tōngguò jùjiāo dāngdài pǔtōng Zhōngguórén de fèndòu dǎpīn yǔ wēnqíng rìcháng, jiāng gǔlǎo dōngfāng de shēnhòu dǐyùn shēngdòng jùxiànghuà. Zhè zhǒng zhēnshí jiēdìqì de wénhuà xíngxiàng, yǒuxiào zēngjìn le quánqiú mínxīn-xiāngtōng.",
                "en": "Global communication of national image is shifting from grand narratives to human stories. Documentaries focusing on ordinary lives embody eastern heritage concretely. This grounded cultural image fosters international mutual understanding.",
                "es": "La proyección internacional de la imagen de China evoluciona hacia historias humanas y vivas. Al mostrar la brega cotidiana de ciudadanos corrientes, se visibiliza el arraigo oriental. Esa imagen franca y humana tiende puentes entre las gentes."
            }
        ]
    }
]

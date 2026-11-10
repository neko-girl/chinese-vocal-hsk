# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 拍
    {
        "id": "21",
        "hanzi": "拍",
        "pinyin": "pāi",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to clap; to pat; to swat; to photograph; to shoot (film)",
            "es": "aplaudir; palmear; golpear suavemente; fotografiar; filmar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to clap, pat, slap, or strike lightly with the palm or an implement",
                "definition_es": "palmear, aplaudir o golpear suavemente con la palma de la mano o una pala",
                "example_phrase": "拍手欢迎 (clap hands in welcome)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to take a photograph, shoot film, or record video with a camera",
                "definition_es": "tomar una fotografía o rodar una escena cinematográfica",
                "example_phrase": "拍照留念 (take a photo as a souvenir)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "摄影师蹲在跑道旁，抓住运动员跃起过杆的瞬间连续拍下了数十张照片。",
                "pinyin": "Shèyǐngshī dūn zài pǎodào páng, zhuāzhù yùndòngyuán yuèqǐ guò gān de shùnjiān liánxù pāixià le shùshí zhāng zhàopiàn.",
                "en": "Squatting beside the track, the photographer seized the moment the athlete vaulted over the bar, snapping dozens of photos.",
                "es": "Acuclillado junto a la pista, el fotógrafo aprovechó el instante en que el atleta saltaba el listón para disparar decenas de fotos."
            },
            {
                "id": "#2",
                "hanzi": "看到舞台上精彩的杂技表演，全场观众忍不住激动地起立拍手喝彩。",
                "pinyin": "Kàndào wǔtái shàng jīngcǎi de zájì biǎoyǎn, quánchǎng guānzhòng rěnbuzhù jīdòng de qǐlì pāishǒu hècǎi.",
                "en": "Seeing the magnificent acrobatic performance on stage, the entire audience couldn't help standing up excitedly to clap and cheer.",
                "es": "Ante la magnífica acrobacia sobre el escenario, todo el auditorio se puso en pie emocionado para aplaudir y ovacionar."
            }
        ],
        "collocations": [
            {"hanzi": "拍照", "en": "take photographs"},
            {"hanzi": "拍电影", "en": "film a movie"},
            {"hanzi": "拍手", "en": "clap hands / applaud"},
            {"hanzi": "拍马屁", "en": "flatter / brown-nose"},
            {"hanzi": "拍打", "en": "pat; slap gently"},
            {"hanzi": "节拍", "en": "musical beat / rhythm"}
        ],
        "idioms": [
            {"hanzi": "拍手称快", "pinyin": "pāi shǒu chēng kuài", "meaning_en": "clap hands and shout with satisfaction; express delight"},
            {"hanzi": "拍案叫绝", "pinyin": "pāi àn jiào jué", "meaning_en": "slap the table in amazement and admiration"},
            {"hanzi": "一拍即合", "pinyin": "yì pāi jí hé", "meaning_en": "hit it off right away; click immediately"},
            {"hanzi": "拍案而起", "pinyin": "pāi àn ér qǐ", "meaning_en": "strike the table and rise up in indignation"}
        ],
        "character_decomposition": [
            {
                "character": "拍",
                "pinyin": "pāi",
                "meaning_en": "clap; pat; shoot photo; racket",
                "meaning_es": "palmear; aplaudir; fotografiar; raqueta",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand action)",
                "sound_component": "白 (bái, clear / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with 白 (clear/flat); striking down with an open flat palm, extended to shutter clicks.",
                "visual_mnemonic_story_en": "An open hand (扌) turns its pale palm (白) outward to clap and snap (拍).",
                "visual_mnemonic_story_es": "Una mano abierta (扌) muestra su blanca palma (白) para palmear y disparar la foto (拍).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QHA",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A flat hand (扌) pats smoothly (pāi, 拍) or clicks the camera shutter.",
            "composite_memory_hook_es": "La mano abierta (扌) golpea suave o acciona el obturador (pāi, 拍).",
            "cultural_and_cognitive_roots": "From the physical clapping of hands to rhythmic musical beats (乐拍), modernizing in the 20th century to optical photography (拍摄).",
            "tone_sandhi_and_pitch_modulation": "High flat level tone: 'pāi' (55). Articulate with crisp level pitch 55 like a quick handclap."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "怕", "pinyin": "pà", "meaning_en": "fear; afraid", "distinction_note": "Has heart radical 忄 on left instead of hand 扌 in 拍"},
                {"character": "迫", "pinyin": "pò", "meaning_en": "compel; urgent", "distinction_note": "Has movement radical 辶 with 白 inside"},
                {"character": "伯", "pinyin": "bó", "meaning_en": "uncle; elder brother", "distinction_note": "Has person radical 亻 on left"},
                {"character": "柏", "pinyin": "bǎi", "meaning_en": "cypress tree", "distinction_note": "Has wood radical 木 on left"}
            ],
            "etymological_cognates": [
                {"character": "击", "pinyin": "jī", "gloss_en": "strike; hit firmly"},
                {"character": "掌", "pinyin": "zhǎng", "gloss_en": "palm of hand"},
                {"character": "打", "pinyin": "dǎ", "gloss_en": "hit; strike with hand"},
                {"character": "摄", "pinyin": "shè", "gloss_en": "capture image; shoot photo"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "拍 involves striking lightly with a flat surface or capturing photos/videos via camera shutter.",
            "contrasts": [
                {"id": "1", "compared_word": "拍 vs. 打", "pinyin": "dǎ", "analysis": "打 denotes forceful hitting or striking with a fist or weapon, whereas 拍 is a light pat with an open flat palm."},
                {"id": "2", "compared_word": "拍 vs. 摄", "pinyin": "shè", "analysis": "摄 is a formal literary term for optical absorption and filming (摄影, 摄制), while 拍 is everyday conversational (拍照, 拍片)."},
                {"id": "3", "compared_word": "拍 vs. 敲", "pinyin": "qiāo", "analysis": "敲 implies knocking or tapping repeatedly with knuckles or a mallet on a hard surface, unlike flat-palmed 拍."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "金秋十月天高气爽，漫山遍野的红叶如诗如画。许多摄影爱好者纷纷背起沉重的相机三脚架，赶在清晨第一缕阳光照耀山谷的时刻，抢拍薄雾缭绕间层林尽染的绝美自然秋色。",
                "pinyin": "Jīnqiū shíyuè tiāngāo-qìshuǎng, mànshān-biànyě de hóngyè rúshī-rúhuà. Xǔduō shèyǐng àihàozhě fēnfēn bēiqǐ chénzhòng de xiàngjī sānjiǎojià, gǎnzài qīngchén dì-yī lǚ yángguāng zhàoyào shāngǔ de shíkè, qiǎngpāi bówù liáorào jiān cénglín-jìnrǎn de juéměi zìrán qiūsè.",
                "en": "In pleasant October autumn, crimson leaves carpet hillsides. Photography enthusiasts carrying heavy tripods rush to capture the ethereal beauty of mist-clad forests bathed in morning dawn.",
                "es": "En el apacible otoño de octubre, el follaje carmesí viste los cerros. Entusiastas provistos de trípodes madrugan para captar la bruma dorada por los primeros rayos solares sobre el bosque otoñal."
            },
            {
                "id": "#2",
                "hanzi": "在早期电影拍摄试验中，爱德华·迈布里奇在跑道边排列了数十台照相机。当奔马飞驰而过扯断细线时，相机的快门被瞬间触发，连续拍下了一组定格马蹄腾空的珍贵照片，开创了活动影像技术的新纪元。",
                "pinyin": "Zài zǎoqī diànyǐng pāishè shíyàn zhōng, Àidéhuá Màibùlǐqí zài pǎodào biān páiliè le shùshí tái zhàoxiàngjī. Dāng bēnmǎ fēichí ér guò chěduàn xìxiàn shí, xiàngjī de kuàimén bèi shùnjiān chùfā, liánxù pāixià le yì zǔ dìnggé mǎtí téngkōng de zhēnguì zhàopiàn, kāichuàng le huódòng yǐngxiàng jìshù de xīn jìyuán.",
                "en": "In early cinematographic experiments, Muybridge arranged cameras along the track. As the galloping horse tripped tripwires, shutters fired in sequence, capturing hooves in mid-air and ushering in cinema.",
                "es": "En pioneros experimentos cinematográficos, Muybridge alineó cámaras junto a la pista. El galope del caballo rompió los hilos activando los obturadores, captando cascos suspendidos e inaugurando el cine."
            }
        ]
    },

    # 22 差距
    {
        "id": "22",
        "hanzi": "差距",
        "pinyin": "chā jù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "gap; disparity; difference; divergence",
            "es": "brecha; disparidad; diferencia; distancia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the distance, difference, or disparity between two entities in level, ability, scale, or quality",
                "definition_es": "distancia, desnivel o desemejanza entre dos entidades en cuanto a nivel, capacidad o calidad",
                "example_phrase": "缩小贫富差距 (narrow the wealth gap)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "虽然我国在一些前沿科技领域取得了突破，但与国际顶尖水平相比仍存在明显差距。",
                "pinyin": "Suīrán wǒguó zài yìxiē qiányán kējì lǐngyù qǔdé le tūpò, dàn yǔ guójì dǐngjiān shuǐpíng xiāngbǐ réng cúnzài míngxiǎn chājù.",
                "en": "Although our country achieved breakthroughs in frontier tech, noticeable gaps remain compared with top global levels.",
                "es": "Pese a los avances nacionales en tecnologías punteras, aún persiste una brecha palpable frente a los estándares mundiales líderes."
            },
            {
                "id": "#2",
                "hanzi": "正视自身差距不仅不会让人消沉，反而能激发团队奋发图强的斗志与前进动力。",
                "pinyin": "Zhèngshì zìshēn chājù bùjǐn bú huì ràng rén xiāochén, fǎn'ér néng jīfā tuánduì fènfā-túqiáng de dòuzhì yǔ qiánjìn dònglì.",
                "en": "Facing one's own shortcomings doesn't cause despair; rather, it spurs a team's fighting spirit to forge ahead.",
                "es": "Afrontar la propia desventaja no induce al desánimo, sino que espolea la combatividad y el empeño del equipo para superarse."
            }
        ],
        "collocations": [
            {"hanzi": "缩小差距", "en": "narrow the gap"},
            {"hanzi": "拉开差距", "en": "widen the distance / pull ahead"},
            {"hanzi": "明显差距", "en": "clear disparity; noticeable gap"},
            {"hanzi": "贫富差距", "en": "wealth gap; income disparity"},
            {"hanzi": "技术差距", "en": "technological disparity"},
            {"hanzi": "存在差距", "en": "exist a gap/difference"}
        ],
        "idioms": [
            {"hanzi": "天壤之别", "pinyin": "tiān rǎng zhī bié", "meaning_en": "world of difference; difference between heaven and earth"},
            {"hanzi": "相去甚远", "pinyin": "xiāng qù shèn yuǎn", "meaning_en": "fall far short of; miles apart"},
            {"hanzi": "截然不同", "pinyin": "jié rán bù tóng", "meaning_en": "entirely different; starkly contrasting"},
            {"hanzi": "平分秋色", "pinyin": "píng fēn qiū sè", "meaning_en": "share honors equally; on equal footing"}
        ],
        "character_decomposition": [
            {
                "character": "差",
                "pinyin": "chā",
                "meaning_en": "difference; mistake; fall short",
                "meaning_es": "diferencia; error; faltar; discrepancia",
                "radical": "羊",
                "radical_meaning_en": "sheep / ram",
                "meaning_component": "羊 (horns uneven) + 工 (hand measuring)",
                "sound_component": "差 (chā)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Rubbing and threshing ears of grain with unequal lengths, producing divergence, difference, or disparity.",
                "visual_mnemonic_story_en": "Comparing two ears of grain shows they diverge unevenly, creating a visible difference (差).",
                "visual_mnemonic_story_es": "Al medir dos espigas de grano se aprecia su longitud dispar, originando una diferencia (差).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "TQM",
                "traditional": ""
            },
            {
                "character": "距",
                "pinyin": "jù",
                "meaning_en": "distance; spur; be apart from",
                "meaning_es": "distancia; espolón; distar de; separación",
                "radical": "足",
                "radical_meaning_en": "foot",
                "meaning_component": "足 (foot/stride)",
                "sound_component": "巨 (jù, carpenter square / huge / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Foot radical 足 paired with 巨 (carpenter square measuring span); measuring spatial distance paced out by footsteps.",
                "visual_mnemonic_story_en": "A foot (足) paces out strides measured by a ruler (巨) to establish distance (距).",
                "visual_mnemonic_story_es": "Un pie (足) mide pasos con una escuadra (巨) para fijar la distancia (距).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "RMSS",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An uneven difference (差) paced out across physical distance (距) constitutes a disparity or gap (差距).",
            "composite_memory_hook_es": "Una desigualdad de nivel (差) medida en distancia de pasos (距) conforma la brecha (差距).",
            "cultural_and_cognitive_roots": "Metrology pairing: 差 (disparity in quality or measure) combined with 距 (linear span between benchmarks).",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'chā jù' (55-51). Hold high pitch 55 on 'chā', then drop down to 51 on 'jù'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "着", "pinyin": "zhe", "meaning_en": "aspect particle; touch", "distinction_note": "Has 目 underneath 羊-like top instead of 工 in 差"},
                {"character": "羞", "pinyin": "xiū", "meaning_en": "shy; shame", "distinction_note": "Has 丑 underneath 羊"},
                {"character": "拒", "pinyin": "jù", "meaning_en": "refuse; reject", "distinction_note": "Has hand radical 扌 on left instead of foot 足 in 距"},
                {"character": "矩", "pinyin": "jǔ", "meaning_en": "carpenter square; rule", "distinction_note": "Has arrow radical 矢 on left"}
            ],
            "etymological_cognates": [
                {"character": "别", "pinyin": "bié", "gloss_en": "distinction; separate"},
                {"character": "异", "pinyin": "yì", "gloss_en": "different; abnormal"},
                {"character": "离", "pinyin": "lí", "gloss_en": "separate; distance apart"},
                {"character": "隔", "pinyin": "gé", "gloss_en": "partition; divide"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "差距 emphasizes the measurable developmental or statistical distance between two levels, standards, or entities.",
            "contrasts": [
                {"id": "1", "compared_word": "差距 vs. 差异", "pinyin": "chāyì", "analysis": "差异 denotes qualitative differences in characteristics or styles (cultural differences), while 差距 emphasizes quantitative disparity in level or quality."},
                {"id": "2", "compared_word": "差距 vs. 距离", "pinyin": "jùlí", "analysis": "距离 primarily designates physical spatial length between coordinates ('两地距离五公里'), while 差距 is comparative disparity."},
                {"id": "3", "compared_word": "差距 vs. 区别", "pinyin": "qūbié", "analysis": "区别 distinguishes features that make two things non-identical, whereas 差距 highlights who is ahead and who is lagging behind."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "推进城乡一体化协调发展的关键，在于有效缩小城乡基础设施与公共服务领域的差距。政府通过持续加大对乡村教育、医疗与交通电网的财政扶持力度，让广大农民群众切实享受到现代化建设带来的发展成果。",
                "pinyin": "Tuījìn chéng-xiāng yītǐhuà xiétiáo fāzhǎn de guānjiàn, zàiyú yǒuxiào suōxiǎo chéng-xiāng jīchǔ shèshī yǔ gōnggòng fúwù lǐngyù de chājù. Zhèngfǔ tōngguò chíxù jiàdà duì xiāngcūn jiàoyù, yīliáo yǔ jiāotōng diànwǎng de cáizhèng fúchí lìdù, ràng guǎngdà nóngmín qúnzhòng qièshí xiǎngshòudào xiàndàihuà jiànshè dàilái de fāzhǎn chéngguǒ.",
                "en": "The key to balanced urban-rural development lies in narrowing disparities in infrastructure and public services. Fiscal support for rural education, healthcare, and transit ensures farmers share in modernization fruits.",
                "es": "La clave de la integración urbano-rural radica en acortar la brecha de infraestructuras y servicios públicos. El apoyo fiscal a la enseñanza, sanidad y vías rurales permite al campesinado disfrutar del progreso moderno."
            },
            {
                "id": "#2",
                "hanzi": "在激烈的国际产业竞争中，企业必须时刻保持居安思危的忧患意识。只有清醒地看到自身在基础工业软件和原创专利上的差距，沉下心来加大研发投入攻坚克难，才能逐步打破垄断，实现产业链的自主可控。",
                "pinyin": "Zài jīliè de guójì chǎnyè jìngzhēng zhōng, qǐyè bìxū shíkè bǎochí jū'ān-sīwēi de yōuhuàn yìshí. Zhǐyào qīngxǐng de kàndào zìshēn zài jīchǔ gōngyè ruǎnjiàn hé yuánchuàng zhuānlì shàng de chājù, chénxiàxīnlái jiàdà yánfā tóurù gōngjiān-kènán, cáinéng zhúbù dǎpò lǒngduàn, shíxiàn chǎnyèliàn de zìzhǔ kěkòng.",
                "en": "Amidst fierce global competition, firms must maintain crisis awareness. Only by acknowledging gaps in foundational software and patents, and investing in R&D, can they break monopolies and secure autonomous supply chains.",
                "es": "Ante la enconada competencia internacional, las empresas deben vigilar riesgos latentes. Reconociendo su desventaja en patentes y redoblando la inversión en I+D, quebrarán monopolios afianzando cadenas de suministro."
            }
        ]
    },

    # 23 显示
    {
        "id": "23",
        "hanzi": "显示",
        "pinyin": "xiǎn shì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to show; to display; to demonstrate; to manifest",
            "es": "mostrar; exhibir; manifestar; reflejar; indicar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to clearly show, reveal, exhibit, or indicate qualities, data, or situations",
                "definition_es": "hacer patente, exteriorizar, desplegar o indicar con claridad cualidades, datos o realidades",
                "example_phrase": "显示出非凡的才能 (display extraordinary talent)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "最新发布的国家宏观经济统计数据显示，国内消费市场正在稳步回暖。",
                "pinyin": "Zuìxīn fābù de guójiā hóngguān jīngjì tǒngjì shùjù xiǎnshì, guónèi xiāofèi shìchǎng zhèngzài wěnbù huínuǎn.",
                "en": "The newly released national macroeconomic statistical data show that the domestic consumer market is steadily recovering.",
                "es": "Las últimas estadísticas macroeconómicas nacionales reflejan que el mercado de consumo interno se está recuperando de manera constante."
            },
            {
                "id": "#2",
                "hanzi": "面对极其复杂的突发局面，年轻的指挥员显示出了过人的沉着与决断力。",
                "pinyin": "Miànduì jíqí fùzá de tūfā júmiàn, niánqīng de zhǐhuīyuán xiǎnshì chū le guòrén de chénzhuó yǔ juéduànlì.",
                "en": "Confronted with an extremely complex emergency, the young commander displayed remarkable composure and decisiveness.",
                "es": "Ante una contingencia sumamente compleja, el joven comandante dio muestras de una serenidad y determinación extraordinarias."
            }
        ],
        "collocations": [
            {"hanzi": "显示屏", "en": "display screen / monitor"},
            {"hanzi": "数据显示", "en": "data indicate / show"},
            {"hanzi": "显示出", "en": "display; demonstrate; reveal"},
            {"hanzi": "显示器", "en": "visual display unit; monitor"},
            {"hanzi": "充分显示", "en": "fully demonstrate; clearly show"},
            {"hanzi": "结果显示", "en": "results show/indicate"}
        ],
        "idioms": [
            {"hanzi": "大显身手", "pinyin": "dà xiǎn shēn shǒu", "meaning_en": "fully display one's talents and capabilities"},
            {"hanzi": "显而易见", "pinyin": "xiǎn ér yì jiàn", "meaning_en": "obvious and easy to see; self-evident"},
            {"hanzi": "初露锋芒", "pinyin": "chū lù fēng máng", "meaning_en": "first display of talent and brilliance"},
            {"hanzi": "崭露头角", "pinyin": "zhǎn lù tóu jiǎo", "meaning_en": "stand out prominently; rise above others"}
        ],
        "character_decomposition": [
            {
                "character": "显",
                "pinyin": "xiǎn",
                "meaning_en": "prominent; apparent; show; manifest",
                "meaning_es": "evidente; patente; ostensible; mostrar",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun/sunlight) + 业 (silk hanging ornament)",
                "sound_component": "显 (xiǎn)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Sunlight 日 shining down on illuminated objects 业, making them vividly visible to the eye.",
                "visual_mnemonic_story_en": "Bright sunlight (日) illuminates fine details, making them clearly visible (显).",
                "visual_mnemonic_story_es": "El sol radiante (日) alumbra los menores detalles haciéndolos patentes a la vista (显).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ATC",
                "traditional": "顯"
            },
            {
                "character": "示",
                "pinyin": "shì",
                "meaning_en": "show; reveal; notify; altar tablet",
                "meaning_es": "mostrar; manifestar; señalar; altar",
                "radical": "示",
                "radical_meaning_en": "spirit / show",
                "meaning_component": "二 (heaven) + 𡭕 (sun, moon, stars showing signs)",
                "sound_component": "示 (shì)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of an ancestral sacrificial stone altar upon which omens and celestial signs are revealed.",
                "visual_mnemonic_story_en": "An altar (示) displays sacrificial offerings to indicate divine guidance and signs.",
                "visual_mnemonic_story_es": "Un ara sagrada (示) expone ofrendas para revelar las señales del cielo.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MMF",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Bright sunlight (显) illuminates an altar sign (示) to clearly display and manifest truths (显示).",
            "composite_memory_hook_es": "La luz solar (显) descubre la señal del altar (示) para mostrar de forma patente la verdad (显示).",
            "cultural_and_cognitive_roots": "Derived from ancient celestial divination: 显 (light revealing forms) paired with 示 (heavenly omens displayed to mankind).",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by falling tone: 'xiǎn shì' (214-51). Dip on 'xiǎn' then drop sharply and decisively on 'shì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "晃", "pinyin": "huàng", "meaning_en": "sway; dazzle", "distinction_note": "Has 光 underneath 日 instead of 业 in 显"},
                {"character": "是", "pinyin": "shì", "meaning_en": "to be; yes", "distinction_note": "Has 疋 underneath 日 instead of 业"},
                {"character": "宗", "pinyin": "zōng", "meaning_en": "ancestor; clan", "distinction_note": "Has roof radical 宀 atop 示"},
                {"character": "奈", "pinyin": "nài", "meaning_en": "how; cope with", "distinction_note": "Has 大 atop 示"}
            ],
            "etymological_cognates": [
                {"character": "明", "pinyin": "míng", "gloss_en": "bright; clear insight"},
                {"character": "见", "pinyin": "jiàn", "gloss_en": "perceive with eyes"},
                {"character": "露", "pinyin": "lù", "gloss_en": "expose to open air"},
                {"character": "表", "pinyin": "biǎo", "gloss_en": "external surface; display"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "显示 emphasizes bringing internal qualities or data into clear, objective visibility for observers.",
            "contrasts": [
                {"id": "1", "compared_word": "显示 vs. 表现", "pinyin": "biǎoxiàn", "analysis": "表现 focuses on human conduct, behavior, or attitude, while 显示 commonly introduces statistical data, signs, or screen readouts."},
                {"id": "2", "compared_word": "显示 vs. 表明", "pinyin": "biǎomíng", "analysis": "表明 focuses on clarifying a stance, viewpoint, or intention ('表明态度'), while 显示 demonstrates empirical phenomena."},
                {"id": "3", "compared_word": "显示 vs. 显露", "pinyin": "xiǎnlù", "analysis": "显露 implies that something previously hidden or buried becomes revealed to view, while 显示 is neutral presentation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "科研团队在实验室成功研制出新型柔性超高清显示屏。这种屏幕厚度仅如薄纸，能够任意折叠弯曲而不影响色彩饱和度。测试数据显示，其在超低温环境下依然能保持极高刷新率与卓越的显示性能。",
                "pinyin": "Kēyán tuánduì zài shíyànshì chénggōng yánzhì chū xīnxíng róuxìng chāogāoqīng xiǎnshìpíng. Zhè zhǒng píngmù hòudù jǐn rú báozhǐ, nénggòu rènyì zhédié wānqū ér bù yǐngxiǎng sècǎi bǎohédù. Cèshì shùjù xiǎnshì, qí zài chāodīwēn huánjìng xià yīrán néng bǎochí jí gāo shuāxīnlǜ yǔ zhuóyuè de xiǎnshì xìngnéng.",
                "en": "Scientists developed ultra-thin flexible ultra-HD display screens. Thin as paper, it bends freely without losing color saturation. Test data show it maintains high refresh rates even under deep cold.",
                "es": "Científicos desarrollaron una pantalla flexible ultra HD fina como papel. Se pliega libremente sin mermar la saturación cromática. Los datos demuestran que conserva un refresco óptimo incluso en frío extremo."
            },
            {
                "id": "#2",
                "hanzi": "在面对重大自然灾害救援时，全社会各界心往一处想、劲往一处使，争分夺秒抢救生命。无数志愿者挺身而出，展现出中华民族守望相助的大爱精神，充分显示了万众一心、众志成城的强大凝聚力与制度优势。",
                "pinyin": "Zài miànduì zhòngdà zìrán zāihài jiùyuán shí, quán shèhuì gèjiè xīn wǎng yí chù xiǎng, jìn wǎng yí chù shǐ, zhēngfēn-duómiǎo qiǎngjiù shēngmìng. Wúshù zhìyuànzhě tǐngshēn'érchū, zhǎnxiàn chū Zhōnghuá mínzú shǒuwàng-xiāngzhù de dà'ài jīngshén, chōngfèn xiǎnshì le wànzhòng-yìxīn, zhòngzhì-chéngchéng de qiángdà níngjùlì yǔ zhìdù yōushì.",
                "en": "During disaster rescues, society joins forces to save lives against the clock. Volunteers step forward, manifesting solidarity and demonstrating the immense cohesion and resilience of a united nation.",
                "es": "En labores de rescate ante catástrofes, la sociedad aúna voluntades contrarreloj. Los voluntarios socorren al prójimo desplegando solidaridad y reflejando una formidable cohesión y entereza comunitaria."
            }
        ]
    },

    # 24 意识
    {
        "id": "24",
        "hanzi": "意识",
        "pinyin": "yì shí",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to realize; to become aware; consciousness; awareness",
            "es": "darse cuenta; percatarse; conciencia; conocimiento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to realize, perceive, or become conscious of a fact, risk, or situation",
                "definition_es": "percatarse, tomar conciencia o darse cuenta de un hecho o peligro",
                "example_phrase": "意识到问题的严重性 (realize the gravity of the problem)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "mental awareness, consciousness, or perception of the external world",
                "definition_es": "facultad de la mente de percibir la realidad, estado de lucidez o sentido de alerta",
                "example_phrase": "增强环保意识 (strengthen environmental awareness)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "走出大门走了好一段路，他才突然意识到自己把家里的钥匙忘在客厅茶几上了。",
                "pinyin": "Zǒuchū dàmén zǒu le hǎo yí duàn lù, tā cái tūrán yìshí dào zìjǐ bǎ jiā lǐ de yàoshi wàng zài kètīng chájī shàng le.",
                "en": "After walking quite a distance outside, he suddenly realized he had left his house keys on the living room table.",
                "es": "Tras caminar un buen trecho al salir a la calle, se percató de repente de que había dejado las llaves de casa en la mesita del salón."
            },
            {
                "id": "#2",
                "hanzi": "在野外徒步探险活动中，每一位队员都必须具备高度的安全防范意识与团队协作精神。",
                "pinyin": "Zài yěwài túbù tànxiǎn huódòng zhōng, měi yí wèi duìyuán dōu bìxū jùbèi gāodù de ānquán fángfàn yìshí yǔ tuánduì xiézuò jīngshén.",
                "en": "During outdoor trekking expeditions, every team member must possess heightened safety awareness and team cooperation.",
                "es": "En expediciones senderistas al aire libre, cada miembro debe contar con una elevada conciencia preventiva y espíritu de equipo."
            }
        ],
        "collocations": [
            {"hanzi": "意识到", "en": "become aware of / realize"},
            {"hanzi": "环保意识", "en": "environmental awareness"},
            {"hanzi": "安全意识", "en": "safety awareness"},
            {"hanzi": "失去意识", "en": "lose consciousness / faint"},
            {"hanzi": "防范意识", "en": "precautionary awareness"},
            {"hanzi": "潜意识", "en": "subconscious mind"}
        ],
        "idioms": [
            {"hanzi": "潜移默化", "pinyin": "qián yí mò huà", "meaning_en": "exert a subtle, imperceptible influence over time"},
            {"hanzi": "恍然大悟", "pinyin": "huǎng rán dà wù", "meaning_en": "suddenly see the light; sudden dawn of realization"},
            {"hanzi": "知觉敏锐", "pinyin": "zhī jué mǐn ruì", "meaning_en": "keen sensory perception and alert awareness"},
            {"hanzi": "居安思危", "pinyin": "jū ān sī wēi", "meaning_en": "in peacetime think of danger; remain vigilant"}
        ],
        "character_decomposition": [
            {
                "character": "意",
                "pinyin": "yì",
                "meaning_en": "meaning; mind; intention; consciousness",
                "meaning_es": "significado; intención; mente; deseo",
                "radical": "心",
                "radical_meaning_en": "heart / mind",
                "meaning_component": "音 (inner voice) + 心 (heart/mind)",
                "sound_component": "意 (yì)",
                "stroke_count": 13,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "An internal voice 音 rising from deep within the human heart 心; denotes intention, thoughts, or consciousness.",
                "visual_mnemonic_story_en": "An inner voice (音) whispers deep inside the heart (心), creating conscious thought (意).",
                "visual_mnemonic_story_es": "Una voz interior (音) susurra en el hondón del corazón (心) forjando el pensamiento (意).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YTAIP",
                "traditional": ""
            },
            {
                "character": "识",
                "pinyin": "shí",
                "meaning_en": "know; recognize; knowledge; perception",
                "meaning_es": "conocer; distinguir; saber; conocimiento",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken words/thought expression)",
                "sound_component": "只 (zhǐ, weapon banner / marker / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Speech radical 讠 paired with an insignia marker 只; to recognize, discriminate, or record knowledge.",
                "visual_mnemonic_story_en": "Words (讠) label markers (只) so that the mind recognizes and identifies them (识).",
                "visual_mnemonic_story_es": "Las palabras (讠) nombran señales (只) para que el juicio las reconozca con lucidez (识).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IVRC",
                "traditional": "識"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When internal thoughts (意) recognize and identify external realities (识), conscious awareness awakes (意识).",
            "composite_memory_hook_es": "Cuando la mente interna (意) reconoce y discierne lo externo (识), brota la conciencia (意识).",
            "cultural_and_cognitive_roots": "Adopted in Buddhist epistemic philosophy (Vijñāna / 唯识宗) to translate sensory and cognitive awareness, later becoming the standard psychological term.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by rising second tone: 'yì shí' (51-35). Descend sharply on 'yì', then climb up clearly on 'shí'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "思", "pinyin": "sī", "meaning_en": "think; ponder", "distinction_note": "Has field 田 atop heart 心 instead of 音 in 意"},
                {"character": "息", "pinyin": "xī", "meaning_en": "breath; rest", "distinction_note": "Has nose 自 atop 心"},
                {"character": "织", "pinyin": "zhī", "meaning_en": "weave; knit", "distinction_note": "Has silk radical 纟 on left instead of 讠 in 识"},
                {"character": "炽", "pinyin": "chì", "meaning_en": "blazing; fierce fire", "distinction_note": "Has fire radical 火 on left"}
            ],
            "etymological_cognates": [
                {"character": "知", "pinyin": "zhī", "gloss_en": "know; be cognizant"},
                {"character": "觉", "pinyin": "jué", "gloss_en": "feel; awaken to sense"},
                {"character": "悟", "pinyin": "wù", "gloss_en": "apprehend; enlighten"},
                {"character": "想", "pinyin": "xiǎng", "gloss_en": "ponder; imagine in mind"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "意识 covers cognitive perception of reality (verb: to realize) as well as psychological consciousness (noun: awareness).",
            "contrasts": [
                {"id": "1", "compared_word": "意识 vs. 认识", "pinyin": "rènshi", "analysis": "认识 refers to knowing a person, understanding objective facts, or cognitive epistemics, while 意识 refers to spontaneous situational realization or philosophical consciousness."},
                {"id": "2", "compared_word": "意识 vs. 察觉", "pinyin": "chájué", "analysis": "察觉 emphasizes early sensory detection of subtle external clues ('察觉到危险'), whereas 意识 highlights internal mental awakening."},
                {"id": "3", "compared_word": "意识 vs. 思想", "pinyin": "sīxiǎng", "analysis": "思想 denotes a structured system of beliefs, ideology, or deep philosophies, while 意识 is basic vigilance or alertness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着全球气候变化加剧，越来越多的人开始深刻意识到保护地球生态的紧迫性。从日常生活中减少一次性塑料制品的使用，到低碳绿色出行，公众环保意识的觉醒正在汇聚成推动可持续发展的强大动力。",
                "pinyin": "Suízhe quánqiú qìhòu biànhuà jiājù, yuèláiyuè duō de rén kāishǐ shēnkè yìshí dào bǎohù Dìqiú shēngtài de jǐnpòxìng. Cóng rìcháng shēnghuó zhōng jiǎnshǎo yícìxìng sùliào zhìpǐn de shǐyòng, dào dītàn lǜsè chūxíng, gōngzhòng huánbǎo yìshí de juéxǐng zhèngzài huìjù chéng tuīdòng kěchíxù fāzhǎn de qiángdà dònglì.",
                "en": "As climate change intensifies, people realize the urgency of ecological protection. Reducing single-use plastics and adopting low-carbon travel reflect an awakening environmental consciousness driving sustainability.",
                "es": "Con el cambio climático, más ciudadanos toman conciencia de proteger la ecología. Reducir plásticos y adoptar transportes limpios refleja una conciencia ambiental colectiva que impulsa la sostenibilidad."
            },
            {
                "id": "#2",
                "hanzi": "当医生从手术室走出来并宣布伤者已经彻底恢复了清醒意识时，焦急守候在走廊里的家属们终于如释重负。经历了惊心动魄的重症抢救，这个脆弱的生命展现出了顽强的生机，奇迹般地战胜了死神。",
                "pinyin": "Dāng yīshēng cóng shǒushùshì zǒuchūlái bìng xuānbù shāngzhě yǐjīng chèdǐ huīfù le qīngxǐng yìshí shí, jiāojí shǒuhòu zài zǒuláng lǐ de jiāshǔmen zhōngyú rúshìzhòngfù. Jīnglì le jīngxīn-dòngpò de zhòngzhèng qiǎngjiù, zhè ge cuìruò de shēngmìng zhǎnxiàn chū le wánqiáng de shēngjī, qíjìbān de zhànshèng le sǐshén.",
                "en": "When the doctor announced the patient had regained full consciousness, the family in the corridor felt immense relief. After intensive emergency treatment, fragile life rallied tenaciously to overcome death miraculously.",
                "es": "Al anunciar el cirujano que el herido había recobrado la plena conciencia, la familia en vela suspiró aliviada. Tras una dramática reanimación, la frágil vida venció tenaz y milagrosamente a la muerte."
            }
        ]
    },

    # 25 艰苦
    {
        "id": "25",
        "hanzi": "艰苦",
        "pinyin": "jiān kǔ",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "arduous; grueling; difficult; tough; hard",
            "es": "arduo; difícil; penoso; riguroso; sacrificado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "arduous, strenuous, and beset by harsh material privations or grueling trials",
                "definition_es": "arduo, penoso y marcado por duras privaciones materiales o rigurosas pruebas",
                "example_phrase": "艰苦的环境 (harsh / grueling environment)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "地质勘探队员顶着烈日暴风雪在荒无人烟的高原扎营，工作环境异常艰苦。",
                "pinyin": "Dìzhì kāntàn duìyuán dǐngzhe lièrì bàofēngxuě zài huángwúrényān de gāoyuán zhāyíng, gōngzuò huánjìng yìcháng jiānkǔ.",
                "en": "Braving blazing sun and blizzards, geologists camp on unpopulated plateaus in an exceptionally grueling working environment.",
                "es": "Desafiando soles abrasadores y ventiscas, los geólogos acampan en mesetas desiertas bajo un entorno laboral sumamente penoso."
            },
            {
                "id": "#2",
                "hanzi": "历经数年艰苦卓绝的科研攻关，团队终于攻克了高端芯片材料的制造瓶颈。",
                "pinyin": "Lìjīng shù nián jiānkǔ-zhuójué de kēyán gōngguān, tuánduì zhōngyú gōngkè le gāoduān xīnpiàn cáiliào de zhìzào píngjǐng.",
                "en": "Through years of grueling scientific research, the team finally overcame manufacturing bottlenecks for high-end chip materials.",
                "es": "Tras años de arduo y tenaz esfuerzo investigador, el equipo superó el cuello de botella en materiales para chips punteros."
            }
        ],
        "collocations": [
            {"hanzi": "艰苦奋斗", "en": "struggle hard; work arduous hours"},
            {"hanzi": "艰苦朴素", "en": "plain and hardworking; simple living"},
            {"hanzi": "条件艰苦", "en": "harsh/grueling conditions"},
            {"hanzi": "艰苦岁月", "en": "hard and grueling years"},
            {"hanzi": "艰苦创业", "en": "start a business amidst hardships"},
            {"hanzi": "历尽艰苦", "en": "endure all kinds of hardships"}
        ],
        "idioms": [
            {"hanzi": "艰苦卓绝", "pinyin": "jiān kǔ zhuó jué", "meaning_en": "arduous and unyielding; showing peerless resilience"},
            {"hanzi": "自力更生", "pinyin": "zì lì gēng shēng", "meaning_en": "rely on one's own efforts; self-reliance"},
            {"hanzi": "茹苦含辛", "pinyin": "rú kǔ hán xīn", "meaning_en": "endure hardships and bitter sacrifices stoically"},
            {"hanzi": "坚忍不拔", "pinyin": "jiān rěn bù bá", "meaning_en": "firm and unyielding; persistent perseverance"}
        ],
        "character_decomposition": [
            {
                "character": "艰",
                "pinyin": "jiān",
                "meaning_en": "difficult; hard; arduous",
                "meaning_es": "difícil; arduo; penoso; espinoso",
                "radical": "又",
                "radical_meaning_en": "right hand",
                "meaning_component": "𡏳 (muddy cliff obstacle) + 又 (hand climbing)",
                "sound_component": "艮 (gèn, obstinate / phonetic carrier)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person climbing a rocky and muddy mountain cliff with bare hands 又; signifying arduous difficulty.",
                "visual_mnemonic_story_en": "Hands (又) grip slippery rocky cliffs as one labours over difficult obstacles (艰).",
                "visual_mnemonic_story_es": "Manos desnudas (又) trepan por escarpados riscos afrontando la dura dificultad (艰).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "EO",
                "traditional": "艱"
            },
            {
                "character": "苦",
                "pinyin": "kǔ",
                "meaning_en": "bitter; hardship; pain; toil",
                "meaning_es": "amargo; penoso; sufrimiento; fatiga",
                "radical": "艹",
                "radical_meaning_en": "grass / plant",
                "meaning_component": "艹 (bitter herb / sow-thistle)",
                "sound_component": "古 (gǔ, old / phonetic)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Grass radical 艹 combined with 古; originally bitter-tasting medicinal herbs, extended to bitter hardship and toilsome life.",
                "visual_mnemonic_story_en": "Tasting wild bitter weeds (艹) of old (古) reminds the tongue of hardship (苦).",
                "visual_mnemonic_story_es": "Masticar hierbas amargas (艹) ancestrales (古) evoca la aspereza de la fatiga (苦).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "TJR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Climbing steep cliffs (艰) while chewing bitter herbs (苦) epitomizes grueling hardship (艰苦).",
            "composite_memory_hook_es": "Escalar riscos escarpados (艰) probando hierbas amargas (苦) resume lo arduo y penoso (艰苦).",
            "cultural_and_cognitive_roots": "Central to traditional Chinese ethos (吃苦耐劳) and revolutionary history (延安艰苦奋斗精神); enduring material privation for high ideals.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by dipping tone: 'jiān kǔ' (55-214). Maintain steady pitch 55 on 'jiān', then dip low and rise on 'kǔ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "坚", "pinyin": "jiān", "meaning_en": "firm; hard; solid", "distinction_note": "Has earth radical 土 at bottom instead of 又 in 艰"},
                {"character": "若", "pinyin": "ruò", "meaning_en": "as if; like", "distinction_note": "Has 右 underneath 艹 instead of 古 in 苦"},
                {"character": "苗", "pinyin": "miáo", "meaning_en": "seedling; sprout", "distinction_note": "Has field 田 underneath 艹"},
                {"character": "苟", "pinyin": "gǒu", "meaning_en": "careless; illicit", "distinction_note": "Has 句 underneath 艹"}
            ],
            "etymological_cognates": [
                {"character": "难", "pinyin": "nán", "gloss_en": "difficult; disaster"},
                {"character": "辛", "pinyin": "xīn", "gloss_en": "pungent; toilsome"},
                {"character": "困", "pinyin": "kùn", "gloss_en": "trapped; distress"},
                {"character": "劳", "pinyin": "láo", "gloss_en": "labor; weary toil"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "艰苦 highlights harsh material conditions and physical privations demanding strenuous perseverance.",
            "contrasts": [
                {"id": "1", "compared_word": "艰苦 vs. 艰难", "pinyin": "jiānnán", "analysis": "艰难 emphasizes severe obstacles, impasses, and crises in progress ('行路艰难', '度过艰难时期'), while 艰苦 emphasizes harsh living or working environments ('艰苦朴素')."},
                {"id": "2", "compared_word": "艰苦 vs. 辛苦", "pinyin": "xīnkǔ", "analysis": "辛苦 denotes everyday physical fatigue and hard work ('你辛苦了'), while 艰苦 implies deep, austere privation and trials."},
                {"id": "3", "compared_word": "艰苦 vs. 痛苦", "pinyin": "tòngkǔ", "analysis": "痛苦 refers to acute emotional agony or severe physical pain, whereas 艰苦 describes objective rugged conditions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在塞罕坝林场建设初期，创业者们住着简陋的地窝子，喝着浑浊的雪水，在零下四十度的极寒天气中顶风冒雪植树造林。正是凭着这股艰苦创业的顽强毅力，他们终于将昔日飞沙走石的荒原变成了浩瀚林海。",
                "pinyin": "Zài Sàihǎnbà línchǎng jiànshè chūqī, chuàngyèzhěmen zhù zhe jiǎnlòu de dìwōzi, hē zhe húnzhuó de xuěshuǐ, zài língxià sìshí dù de jíhán tiānqì zhōng dǐngfēng-màoxuě zhíshù zàolín. Zhèngshì píngzhe zhè gǔ jiānkǔ-chuàngyè de wánqiáng yìlì, tāmen zhōngyú jiāng xīrì fēishā-zǒushí de huāngyuán biànchéng le hàohàn línhǎi.",
                "en": "Founders of Saihanba lived in earthen dugouts, drinking melted snow in minus 40-degree cold to plant trees. Through such grueling entrepreneurship, they transformed barren wastelands into a sea of green forests.",
                "es": "Los pioneros de Saihanba moraban en chozas de barro y bebían nieve derretida a 40 bajo cero para plantar árboles. Con perseverancia y sacrificio transformaron yermos desérticos en un océano boscoso."
            },
            {
                "id": "#2",
                "hanzi": "无论个人事业还是国家建设，艰苦奋斗的优良传统永不过时。物质条件的丰富改善，绝不意味着可以贪图安逸、丢弃拼搏斗志。唯有保持清醒头脑，在顺境中居安思危、迎难而上，才能行稳致远、铸就辉煌业绩。",
                "pinyin": "Wúlùn gèrén shìyè háishì guójiā jiànshè, jiānkǔ-fèndòu de yōuliáng chuántǒng yǒng bù guòshí. Wùzhì tiáojiàn de fēngfù gǎishàn, juébù yìwèizhe kěyǐ tāntú ānyì, diūqì pīnbó dòuzhì. Wéiyǒu bǎochí qīngxǐng tóunǎo, zài shùnjìng zhōng jū'ān-sīwēi, yíngnán'érshàng, cáinéng xíngwěn-zhìyuǎn, zhùjiù huīhuáng yèjì.",
                "en": "Whether in personal careers or national development, the virtue of arduous struggle never goes out of style. Improved living conditions should never lead to complacency; enduring trials ensures enduring success.",
                "es": "En la superación personal o el desarrollo patrio, la tradición del esfuerzo abnegado jamás caduca. La bonanza material no debe invitar a la holganza; afrontar retos con sobriedad garantiza logros perdurables."
            }
        ]
    },

    # 26 试验
    {
        "id": "26",
        "hanzi": "试验",
        "pinyin": "shì yàn",
        "part_of_speech": "Noun / Verb",
        "meanings_summary": {
            "en": "experiment; test; trial; to test; to experiment",
            "es": "experimento; ensayo; prueba; probar; ensayar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a scientific test, trial, or experiment carried out to discover, verify, or demonstrate something",
                "definition_es": "ensayo, prueba empírica o experimento científico realizado para comprobar o demostrar algo",
                "example_phrase": "科学试验 (scientific experiment)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to put to test, run trials on, or experimentally verify equipment or theories",
                "definition_es": "poner a prueba, ensayar o verificar experimentalmente equipos o teorías",
                "example_phrase": "试验新机器 (test a new machine)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了验证杂交水稻耐盐碱的特性，农科院专家在沿海滩涂进行了连续三年的田间试验。",
                "pinyin": "Wèile yànzhèng zájiāo shuǐdào nài yánjiǎn de tèxìng, Nóngkēyuàn zhuānjiā zài yánhǎi tāntú jìnxíng le liánxù sān nián de tiánjiān shìyàn.",
                "en": "To verify saline-alkali resistance of hybrid rice, agronomy experts carried out field trials on coastal mudflats for three years.",
                "es": "Para comprobar la tolerancia al salitre del arroz híbrido, agrónomos realizaron ensayos en marismas litorales durante tres años."
            },
            {
                "id": "#2",
                "hanzi": "新型客机在正式投入商业运营前，必须通过数千小时极其严苛的试飞试验与极端环境测试。",
                "pinyin": "Xīnxíng kèjī zài zhèngshì tóurù shāngyè yùnyíng qián, bìxū tōngguò shùqiān xiǎoshí jíqí yánkē de shìfēi shìyàn yǔ jíduān huánjìng cèshì.",
                "en": "Before commercial passenger flights, new airliners must pass thousands of hours of rigorous flight trials and extreme weather tests.",
                "es": "Antes de operar comercialmente, los nuevos aviones de pasajeros deben superar miles de horas de rigurosos vuelos de prueba."
            }
        ],
        "collocations": [
            {"hanzi": "临床试验", "en": "clinical trial"},
            {"hanzi": "试验田", "en": "experimental plot; testing ground"},
            {"hanzi": "试验品", "en": "test product; trial article"},
            {"hanzi": "科学试验", "en": "scientific experiment/trial"},
            {"hanzi": "试验阶段", "en": "experimental/trial phase"},
            {"hanzi": "模拟试验", "en": "simulation test; mock trial"}
        ],
        "idioms": [
            {"hanzi": "屡试不爽", "pinyin": "lǚ shì bù shuǎng", "meaning_en": "tested many times and never fails; foolproof"},
            {"hanzi": "实践检验", "pinyin": "shí jiàn jiǎn yàn", "meaning_en": "testing through actual practical experience"},
            {"hanzi": "身体力行", "pinyin": "shēn tǐ lì xíng", "meaning_en": "practice personally what one preaches"},
            {"hanzi": "切实验证", "pinyin": "qiè shí yàn zhèng", "meaning_en": "verify rigorously through facts"}
        ],
        "character_decomposition": [
            {
                "character": "试",
                "pinyin": "shì",
                "meaning_en": "try; test; experiment; exam",
                "meaning_es": "probar; ensayar; examen; intentar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (inquire with speech/questions)",
                "sound_component": "式 (shì, model/standard / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 tested against a set pattern or standard rule 式; to evaluate, assay, or try out.",
                "visual_mnemonic_story_en": "Measuring words (讠) against a standard template (式) tests (试) their validity.",
                "visual_mnemonic_story_es": "Confrontar palabras (讠) con una pauta patrón (式) sirve para probar (试) su exactitud.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVIP",
                "traditional": "試"
            },
            {
                "character": "验",
                "pinyin": "yàn",
                "meaning_en": "examine; check; verify; effective",
                "meaning_es": "verificar; comprobar; examinar; eficaz",
                "radical": "马",
                "radical_meaning_en": "horse",
                "meaning_component": "马 (examining physical traits of horses)",
                "sound_component": "佥 (qiān, all together / phonetic carrier)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Horse radical 马 paired with 佥 (thoroughly assembled); thoroughly checking a horse's teeth and gait to verify pedigree.",
                "visual_mnemonic_story_en": "Inspectors examine a fine horse (马) from head to hoof to verify (验) its strength.",
                "visual_mnemonic_story_es": "Un perito examina al corcel (马) de pies a cabeza para verificar (验) su brío y salud.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NMSOI",
                "traditional": "驗"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Trying out a model (试) and verifying results on a test subject (验) constitutes an experiment (试验).",
            "composite_memory_hook_es": "Probar un modelo patrón (试) y verificar resultados fehacientes (验) conforma el ensayo (试验).",
            "cultural_and_cognitive_roots": "Scientific methodology term coined in modern Chinese: 试 (tentative testing) + 验 (verifying concrete outcomes).",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'shì yàn' (51-51). Descend firmly on 'shì', then drop sharply again on 'yàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "拭", "pinyin": "shì", "meaning_en": "wipe away tears", "distinction_note": "Has hand radical 扌 on left instead of speech 讠 in 试"},
                {"character": "弑", "pinyin": "shì", "meaning_en": "slay one's sovereign", "distinction_note": "Has weapon 弋 component"},
                {"character": "脸", "pinyin": "liǎn", "meaning_en": "face", "distinction_note": "Has flesh radical 月 on left of 佥 instead of horse 马 in 验"},
                {"character": "险", "pinyin": "xiǎn", "meaning_en": "danger; hazard", "distinction_note": "Has hill radical 阝 on left"}
            ],
            "etymological_cognates": [
                {"character": "考", "pinyin": "kǎo", "gloss_en": "examine; scrutinize"},
                {"character": "查", "pinyin": "chá", "gloss_en": "inspect; investigate"},
                {"character": "测", "pinyin": "cè", "gloss_en": "fathom; measure water"},
                {"character": "核", "pinyin": "hé", "gloss_en": "audit; check seed/core"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "试验 focuses on exploratory practical trials conducted to develop, verify, or improve products and machines.",
            "contrasts": [
                {"id": "1", "compared_word": "试验 vs. 实验", "pinyin": "shíyàn", "analysis": "实验 emphasizes controlled scientific lab procedures to deduce natural laws ('物理实验', '化学实验'), while 试验 refers to practical performance trials of tools, crops, or prototypes."},
                {"id": "2", "compared_word": "试验 vs. 考试", "pinyin": "kǎoshì", "analysis": "考试 designates formal academic tests evaluating students' mastery, whereas 试验 tests things or machines."},
                {"id": "3", "compared_word": "试验 vs. 检验", "pinyin": "jiǎnyàn", "analysis": "检验 focuses on inspecting already manufactured goods to ensure they meet existing quality criteria, while 试验 is exploratory."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在航空航天领域，每一次新型发动机的研发都要经历数以千计的严苛试验。科研人员在超音速风洞中反复模拟极端气流与超高温环境，细致采集各项核心数据，为国之重器的安全升空打下坚实基础。",
                "pinyin": "Zài hángkōng-hángtiān lǐngyù, měi yí cì xīnxíng fādòngjī de yánfā dōuyào jīnglì shùyǐqiānzhì de yánkē shìyàn. Kēyán rényuán zài chāoyīnsù fēngdòng zhōng fǎnfù mónǐ jíduān qìliú yǔ chāogāowēn huánjìng, xìzhì cǎijí gèxiàng héxīn shùjù, wèi guózhīzhòngqì de ānquán shēngkōng dǎxià jiānshí jīchǔ.",
                "en": "In aerospace, developing each new engine undergoes thousands of severe trials. Researchers simulate extreme airflow in supersonic wind tunnels, collecting data to safeguard liftoffs.",
                "es": "En la ingeniería aeroespacial, el desarrollo de turbinas afronta miles de rigurosos ensayos. En túneles supersónicos se simulan corrientes y calor extremos reuniendo datos clave para el vuelo seguro."
            },
            {
                "id": "#2",
                "hanzi": "科学探索的道路往往伴随着无数次试验的失败与挫折。发明家爱迪生在寻找理想灯丝的过程中，试验了上千种耐热植物纤维与金属材料。正是在一次次看似没有希望的尝试中，才最终迎来了照亮黑暗的伟大突破。",
                "pinyin": "Kēxué tànsuǒ de dàolù wǎngwǎng bànsuí zhe wúshù cì shìyàn de shībài yǔ cuòzhé. Fāmíngjiā Àidíshēng zài xúnzhǎo lǐxiǎng dēngsī de guòchéng zhōng, shìyàn le shàngqiān zhǒng nàirè zhíwù xiānwéi yǔ jīnshǔ cáiliào. Zhèngshì zài yícìcì kànsì méiyǒu xīwàng de chángshì zhōng, cái zuìzhōng yínglái le zhàoliàng hēi'àn de wěidà tūpò.",
                "en": "Scientific exploration is paved with failures across countless trials. In search of the ideal filament, Edison tested thousands of materials. Persisting through unpromising attempts, he achieved light.",
                "es": "La senda científica está jalonada de tropiezos en incontables ensayos. Para hallar el filamento idóneo, Edison ensayó miles de fibras y metales, coronando una gesta que iluminó las tinieblas."
            }
        ]
    },

    # 27 逐渐
    {
        "id": "27",
        "hanzi": "逐渐",
        "pinyin": "zhú jiàn",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "gradually; by degrees; little by little",
            "es": "gradualmente; poco a poco; paulatinamente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "gradually, step by step, or progressively over the course of time",
                "definition_es": "poco a poco, paso a paso o progresivamente a lo largo del tiempo",
                "example_phrase": "天气逐渐转凉 (weather gradually turns cool)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "立秋过后，昼夜温差变大，北方大地的树叶逐渐从翠绿变为金黄。",
                "pinyin": "Lìqiū guòhòu, zhòuyè wēnchā biàndà, běifāng dàdì de shùyè zhújiàn cóng cuìlǜ biànwéi jīnhuáng.",
                "en": "After Start of Autumn, temperature swings widen and northern tree leaves gradually turn from jade green to gold.",
                "es": "Tras la llegada del otoño, el contraste térmico aumenta y el follaje norteño pasa paulatinamente del verde esmeralda al dorado."
            },
            {
                "id": "#2",
                "hanzi": "通过持之以恒的系统阅读与写作训练，他的汉语听说表达能力逐渐得到了显著提升。",
                "pinyin": "Tōngguò chízhīyǐhéng de xìtǒng yuèdú yǔ xiězuò xùnliàn, tā de Hànyǔ tīng-shuō biǎodá nénglì zhújiàn dédào le xiǎnzhù tíshēng.",
                "en": "Through persistent systematic reading and writing, his Chinese speaking and listening abilities gradually improved remarkably.",
                "es": "Mediante una perseverante práctica de lectura y redacción, su destreza oral en chino experimentó una mejora paulatina y notable."
            }
        ],
        "collocations": [
            {"hanzi": "逐渐增加", "en": "gradually increase"},
            {"hanzi": "逐渐减少", "en": "gradually decrease"},
            {"hanzi": "逐渐形成", "en": "gradually take shape"},
            {"hanzi": "逐渐适应", "en": "gradually adapt to"},
            {"hanzi": "逐渐恢复", "en": "gradually recover"},
            {"hanzi": "逐渐改变", "en": "gradually change"}
        ],
        "idioms": [
            {"hanzi": "循序渐进", "pinyin": "xún xù jiàn jìn", "meaning_en": "proceed step by step in an orderly progression"},
            {"hanzi": "水滴石穿", "pinyin": "shuǐ dī shí chuān", "meaning_en": "dripping water wears through stone; persistence pays"},
            {"hanzi": "日积月累", "pinyin": "rì jī yuè lěi", "meaning_en": "accumulate day by day and month by month"},
            {"hanzi": "防微杜渐", "pinyin": "fáng wēi dù jiàn", "meaning_en": "nip problems in the bud before they grow"}
        ],
        "character_decomposition": [
            {
                "character": "逐",
                "pinyin": "zhú",
                "meaning_en": "pursue; chase; one by one; successively",
                "meaning_es": "perseguir; ahuyentar; uno a uno; sucesivamente",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (stride/movement) + 豕 (pig/wild boar)",
                "sound_component": "逐 (zhú)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A foot 辶 hunting and chasing a wild boar 豕 step by step; signifies following successively one after another.",
                "visual_mnemonic_story_en": "A hunter pursues (辶) a wild boar (豕) step by step in orderly succession (逐).",
                "visual_mnemonic_story_es": "Un cazador sigue el rastro (辶) de un jabalí (豕) paso a paso en pos de la presa (逐).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YMBO",
                "traditional": ""
            },
            {
                "character": "渐",
                "pinyin": "jiàn",
                "meaning_en": "gradual; slowly; advance step by step",
                "meaning_es": "gradual; paulatino; avanzar poco a poco",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (soaking water flow)",
                "sound_component": "斩 (zhǎn, cleave / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 paired with 斩; water gently and steadily soaking through soil over time without rushing.",
                "visual_mnemonic_story_en": "Water drops (氵) slowly soak into earth step by step (渐) without rushing.",
                "visual_mnemonic_story_es": "El agua (氵) impregna la tierra paso a paso (渐) con calma silenciosa.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EKLJ",
                "traditional": "漸"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pursuing step by step (逐) as water slowly soaks through soil (渐) describes gradual progress (逐渐).",
            "composite_memory_hook_es": "Seguir un paso tras otro (逐) como el agua cala la tierra (渐) describe el avance paulatino (逐渐).",
            "cultural_and_cognitive_roots": "Derived from the I Ching hexagram Jian (渐卦: gradual mountain tree growth); emphasizes natural evolutionary tempo versus rash haste.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone: 'zhú jiàn' (35-51). Rise smoothly on 'zhú', then descend firmly on 'jiàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "遂", "pinyin": "suì", "meaning_en": "succeed; fulfill", "distinction_note": "Has 豕 inside 辶 like 逐 but has two extra upper strokes"},
                {"character": "家", "pinyin": "jiā", "meaning_en": "family; home", "distinction_note": "Has roof radical 宀 atop 豕 instead of movement 辶"},
                {"character": "惭", "pinyin": "cán", "meaning_en": "ashamed", "distinction_note": "Has heart radical 忄 on left of 斩 instead of water 氵 in 渐"},
                {"character": "崭", "pinyin": "zhǎn", "meaning_en": "towering; brand-new", "distinction_note": "Has mountain radical 山 on top of 斩"}
            ],
            "etymological_cognates": [
                {"character": "慢", "pinyin": "màn", "gloss_en": "slow; deliberate pace"},
                {"character": "进", "pinyin": "jìn", "gloss_en": "advance; proceed forward"},
                {"character": "步", "pinyin": "bù", "gloss_en": "step; pace of walking"},
                {"character": "徐", "pinyin": "xú", "gloss_en": "gently slow; leisurely"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "逐渐 focuses on incremental, developmental transitions across uninterrupted chronological timelines.",
            "contrasts": [
                {"id": "1", "compared_word": "逐渐 vs. 逐步", "pinyin": "zhúbù", "analysis": "逐步 emphasizes clear, discrete planned human steps ('逐步落实方案'), while 逐渐 highlights continuous, natural, or subtle progressive changes ('天色逐渐暗下来')."},
                {"id": "2", "compared_word": "逐渐 vs. 渐渐", "pinyin": "jiànjiàn", "analysis": "渐渐 is more colloquial and poetic, common in spoken narrative, whereas 逐渐 is standard across written prose and analytical reports."},
                {"id": "3", "compared_word": "逐渐 vs. 慢慢", "pinyin": "mànmàn", "analysis": "慢慢 emphasizes low velocity ('慢慢走'), while 逐渐 emphasizes chronological degree of change."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "早春二月，覆盖大地的积雪在和煦阳光下悄然融化，小溪解冻流淌出悦耳的叮咚乐声。向阳山坡上的嫩草逐渐探出绿茸茸的脑袋，枯槁了一整个冬天的森林正在逐渐苏醒，四处洋溢着盎然生机。",
                "pinyin": "Zǎochūn èryuè, fùgài dàdì de jīxuě zài héxù yángguāng xià qiǎorán rónghuà, xiǎoxī jiědòng liútǎng chū yuè'ěr de dīngdōng yuèshēng. Xiàngyáng shānpō shàng de nèncǎo zhújiàn tànchū lǜróngróng de nǎodài, kūgǎo le yí zhěng ge dōngtiān de sēnlín zhèngzài zhújiàn sùxǐng, sìchù yángyì zhe àngrán shēngjī.",
                "en": "In early spring, snow melts softly under gentle sun as brooks thaw into song. Tender grass gradually peeps out on sunny slopes; the forest that slumbered all winter is gradually awakening to life.",
                "es": "A comienzos de primavera, la nieve se funde al sol tibio y los arroyos entonan su murmullo. Brotes verdes asoman en las laderas soleadas; el bosque despierta paulatinamente rebosando vida."
            },
            {
                "id": "#2",
                "hanzi": "掌握一门外语从非一朝一夕之功。初学者往往因记不住单词而倍感焦虑，但只要每天坚持收听地道广播、积累经典表达，语感就会在潜移默化中逐渐建立，原本晦涩复杂的长难句最终也能轻松读懂。",
                "pinyin": "Zhǎngwò yì mén wàiyǔ cóng fēi yìzhāo-yīxī zhī gōng. Chūxuézhě wǎngwǎng yīn jìbuzhù dāncí ér bèigǎn jiāolǜ, dàn zhǐyào měitiān jiānchí shōutīng dìdao guǎngbō, jīlěi jīngdiǎn biǎodá, yǔgǎn jiù huì zài qiányí-mòhuà zhōng zhújiàn jiànlì, yuánběn huìsè fùzá de chángnánjù zuìzhōng yě néng qīngsōng dúdǒng.",
                "en": "Mastering a foreign language is never overnight work. Beginners fret over vocabulary, yet daily listening builds language intuition gradually, turning complex sentences into accessible reading.",
                "es": "Dominar una lengua extranjera no se logra de la noche a la mañana. La constancia diaria con la radio consolida paulatinamente la intuición lingüística, facilitando la comprensión de frases arduas."
            }
        ]
    },

    # 28 改进
    {
        "id": "28",
        "hanzi": "改进",
        "pinyin": "gǎi jìn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to improve; to modify; to make better; improvement",
            "es": "mejorar; perfeccionar; reformar; optimizar; mejora"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to change, refine, or upgrade methods, technologies, or tools to make them better and more efficient",
                "definition_es": "modificar, perfeccionar o actualizar métodos, técnicas o herramientas para elevar su eficacia",
                "example_phrase": "改进工作方法 (improve working methods)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "工程师团队根据用户反馈的意见，对手机操作系统的流畅度进行了深度改进。",
                "pinyin": "Gōngchéngshī tuánduì gēnjù yònghù fǎnkuì de yìjiàn, duì shǒujī cāozuò xìtǒng de liúchàngdù jìnxíng le shēndù gǎijìn.",
                "en": "Based on user feedback, the engineering team carried out deep improvements on the mobile OS smoothness.",
                "es": "Tomando en cuenta las sugerencias de los usuarios, los ingenieros perfeccionaron a fondo la fluidez del sistema operativo móvil."
            },
            {
                "id": "#2",
                "hanzi": "工厂引进了自动化流水线并大力改进生产工艺，不仅大幅削减了能耗，还显著提升了产量。",
                "pinyin": "Gōngchǎng yǐnjìn le zìdònghuà liúshuǐxiàn bìng dàlì gǎijìn shēngchǎn gōngyì, bùjǐn dàfú xuējiǎn le nénghào, hái xiǎnzhù tíshēng le chǎnliàng.",
                "en": "The plant introduced automated assembly lines and improved craftsmanship, slashing energy consumption and boosting output.",
                "es": "La fábrica introdujo líneas automatizadas y mejoró los procesos productivos, recortando el consumo energético y aumentando la producción."
            }
        ],
        "collocations": [
            {"hanzi": "改进工作", "en": "improve work"},
            {"hanzi": "改进技术", "en": "upgrade/improve technology"},
            {"hanzi": "改进方法", "en": "improve methods"},
            {"hanzi": "改进工艺", "en": "refine manufacturing craft"},
            {"hanzi": "大力改进", "en": "vigorously improve"},
            {"hanzi": "有待改进", "en": "leave room for improvement"}
        ],
        "idioms": [
            {"hanzi": "精益求精", "pinyin": "jīng yì qiú jīng", "meaning_en": "constantly strive for perfection; refine unceasingly"},
            {"hanzi": "推陈出新", "pinyin": "tuī chén chū xīn", "meaning_en": "weed through the old to bring forth the new"},
            {"hanzi": "革故鼎新", "pinyin": "gé gù dǐng xīn", "meaning_en": "discard the obsolete and establish the new"},
            {"hanzi": "改过自新", "pinyin": "gǎi guò zì xīn", "meaning_en": "turn over a new leaf; reform oneself"}
        ],
        "character_decomposition": [
            {
                "character": "改",
                "pinyin": "gǎi",
                "meaning_en": "change; alter; correct; transform",
                "meaning_es": "cambiar; corregir; modificar; reformar",
                "radical": "攵",
                "radical_meaning_en": "tap / action",
                "meaning_component": "己 (oneself) + 攵 (tapping hand correcting posture)",
                "sound_component": "改 (gǎi)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand holding a rod 攵 lightly tapping to correct oneself 己; signifies reforming flaws into proper form.",
                "visual_mnemonic_story_en": "A mentor taps a student lightly (攵) to correct posture, changing for the better (改).",
                "visual_mnemonic_story_es": "Una vara suave (攵) corrige la postura personal (己) para reformarla a mejor (改).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "SUOK",
                "traditional": ""
            },
            {
                "character": "进",
                "pinyin": "jìn",
                "meaning_en": "advance; enter; move forward; promote",
                "meaning_es": "avanzar; entrar; progresar; promover",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walk/movement) + 井 (phonetic / well-ordered grid)",
                "sound_component": "进 (jìn)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of a small bird hopping forward 佳 with a walking foot 辶; moving steadily ahead.",
                "visual_mnemonic_story_en": "Footsteps (辶) march steadily through the gate, moving forward (进).",
                "visual_mnemonic_story_es": "Pasos firmes (辶) cruzan el dintel avanzando resueltamente hacia adelante (进).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YTT",
                "traditional": "進"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Correcting flaws (改) to advance forward (进) constitutes an improvement (改进).",
            "composite_memory_hook_es": "Corregir defectos (改) para avanzar adelante (进) conduce a la mejora (改进).",
            "cultural_and_cognitive_roots": "Rooted in the Chinese philosophical tenet of constant self-renewal (日新又新); continuously rectifying flaws to promote progress.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by falling tone: 'gǎi jìn' (214-51). Dip on 'gǎi' then land decisively on falling 'jìn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "政", "pinyin": "zhèng", "meaning_en": "politics; government", "distinction_note": "Has 正 on left of 攵 instead of 己 in 改"},
                {"character": "攻", "pinyin": "gōng", "meaning_en": "attack; study", "distinction_note": "Has 工 on left of 攵"},
                {"character": "近", "pinyin": "jìn", "meaning_en": "near; close", "distinction_note": "Has 斤 inside 辶 instead of 井 in 进"},
                {"character": "送", "pinyin": "sòng", "meaning_en": "deliver; see off", "distinction_note": "Has 关 inside 辶"}
            ],
            "etymological_cognates": [
                {"character": "良", "pinyin": "liáng", "gloss_en": "good; fine quality"},
                {"character": "革", "pinyin": "gé", "gloss_en": "leather; reform skin"},
                {"character": "更", "pinyin": "gēng", "gloss_en": "change; renew watch"},
                {"character": "变", "pinyin": "biàn", "gloss_en": "alter; transform"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "改进 targets refining procedural methods, tools, workflows, or technologies to make them more effective.",
            "contrasts": [
                {"id": "1", "compared_word": "改进 vs. 改善", "pinyin": "gǎishàn", "analysis": "改善 usually collocates with conditions, livelihoods, or relationships ('改善生活', '改善关系'), while 改进 collocates with methods, techniques, and systems ('改进工艺', '改进作风')."},
                {"id": "2", "compared_word": "改进 vs. 改良", "pinyin": "gǎiliáng", "analysis": "改良 often refers to biological breeding or soil enhancement ('改良品种', '改良土壤'), whereas 改进 applies to tools and workflows."},
                {"id": "3", "compared_word": "改进 vs. 改革", "pinyin": "gǎigé", "analysis": "改革 implies large-scale institutional transformation of social or economic structures, while 改进 is operational refinement."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代精益制造理念中，持续改进被视为企业安身立命之本。一线工人和技术骨干紧密配合，不放过任何一个操作细节上的小缺陷，通过日积月累的技术微创新，使整条生产线的加工精度达到了行业领先水平。",
                "pinyin": "Zài xiàndài jīngyì zhìzào lǐniàn zhōng, chíxù gǎijìn bèi shìwéi qǐyè ānshēn-lìmìng zhī běn. Yīxiàn gōngrén yǔ jìshù gǔgàn jǐnmì pèihé, bú fàngguò rènhé yí ge cāozuò xìjié shàng de xiǎoquēxiàn, tōngguò rìjī-yuèlěi de jìshù wēichuàngxīn, shǐ zhěng tiáo shēngchǎnxiàn de jiāgōng jīngdù dádào le hángyè lǐngxiān shuǐpíng.",
                "en": "In lean manufacturing, continuous improvement is vital. Workers and technicians address minor flaws in operational details; through accumulated micro-innovations, the line's precision achieves industry leadership.",
                "es": "En la manufactura esbelta, la mejora continua es pilar esencial. Operarios y técnicos corrigen minucias operativas; con microinnovaciones diarias la precisión de la línea alcanza el liderazgo industrial."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的市场需求，互联网产品经理必须时刻根据用户体验反馈改进产品设计。从简化注册流程到优化界面交互，唯有以用户为中心不断迭代升级，才能在同质化严重的激烈竞争中立于不败之地。",
                "pinyin": "Miànduì shùnxī-wànbiàn de shìchǎng xūqiú, hùliánwǎng chǎnpǐn jīnglǐ bìxū shíkè gēnjù yònghù tǐyàn fǎnkuì gǎijìn chǎnpǐn shèjì. Cóng jiǎnhuà zhùcè liúchéng dào yōuhuà jièmiàn jiāohù, wéiyǒu yǐ yònghù wéi zhōngxīn bùduàn diédài shēngjí, cáinéng zài tóngzhìhuà yánzhòng de jīliè jìngzhēng zhōng lìyú-búbàizhīdì.",
                "en": "Facing fast-changing market needs, internet product managers continuously improve designs based on user feedback. From streamlining onboarding to UI interaction, iterating keeps products competitive.",
                "es": "Ante la demanda cambiante, los gestores de producto perfeccionan el diseño según las impresiones del usuario. Simplificar el registro y optimizar la interfaz asegura la competitividad del producto."
            }
        ]
    },

    # 29 成熟
    {
        "id": "29",
        "hanzi": "成熟",
        "pinyin": "chéng shú",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "mature; ripe; fully developed; seasoned",
            "es": "maduro; sazonado; desarrollado; prudente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "ripe and ready for harvesting (of crops and fruit)",
                "definition_es": "maduro y listo para cosechar (dicho de frutos y cosechas)",
                "example_phrase": "麦子成熟了 (the wheat has ripened)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "mature, fully developed, seasoned, and well-thought-out (of personality, conditions, or ideas)",
                "definition_es": "maduro, plenamente desarrollado, sensato y ponderado (de personas o condiciones)",
                "example_phrase": "时机已经成熟 (conditions are now ripe)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秋风吹过金色的原野，果园里沉甸甸的红苹果成熟了，散发出诱人的阵阵果香。",
                "pinyin": "Qiūfēng chuīguò jīnsè de yuányě, guǒyuán lǐ chéndiāndiān de hóng píngguǒ chéngshú le, sànfā chū yòurén de zhènzhèn guǒxiāng.",
                "en": "Autumn breezes sweep golden fields; in orchards, heavy red apples have ripened, exuding alluring fragrant scents.",
                "es": "La brisa otoñal peina campos dorados; en el huerto, las pesadas manzanas rojas han madurado desprendiendo un delicioso aroma."
            },
            {
                "id": "#2",
                "hanzi": "经过多年商海风浪的洗礼，他在处理复杂人际关系与商务谈判时显得愈发沉稳成熟。",
                "pinyin": "Jīngguò duōnián shānghǎi fēnglàng de xǐlǐ, tā zài chǔlǐ fùzá rénjì guānxì yǔ shāngwù tánpàn shí xiǎnde yùfā chénwěn chéngshú.",
                "en": "Seasoned by years of business storms, he appears increasingly composed and mature in negotiations.",
                "es": "Curtido por años de lances comerciales, se muestra cada vez más sosegado y maduro en negociaciones complejas."
            }
        ],
        "collocations": [
            {"hanzi": "时机成熟", "en": "ripe timing / opportune moment"},
            {"hanzi": "技术成熟", "en": "mature technology"},
            {"hanzi": "成熟稳重", "en": "mature and prudent"},
            {"hanzi": "果实成熟", "en": "fruit ripeness"},
            {"hanzi": "思想成熟", "en": "mature thinking"},
            {"hanzi": "趋于成熟", "en": "tend towards maturity"}
        ],
        "idioms": [
            {"hanzi": "瓜熟蒂落", "pinyin": "guā shú dì luò", "meaning_en": "when melon is ripe it falls off the stem; things succeed when conditions ripen"},
            {"hanzi": "水到渠成", "pinyin": "shuǐ dào qú chéng", "meaning_en": "water flows and a channel is formed; success comes naturally when ready"},
            {"hanzi": "深思熟虑", "pinyin": "shēn sī shú lǜ", "meaning_en": "mature deliberation; careful, thorough consideration"},
            {"hanzi": "半生不熟", "pinyin": "bàn shēng bù shú", "meaning_en": "half-cooked / half-baked; poorly mastered"}
        ],
        "character_decomposition": [
            {
                "character": "成",
                "pinyin": "chéng",
                "meaning_en": "complete; accomplish; succeed; become",
                "meaning_es": "completar; lograr; tener éxito; convertirse",
                "radical": "戈",
                "radical_meaning_en": "dagger-axe",
                "meaning_component": "戊 (halberd weapon) + 丁 (nail / strike firmly)",
                "sound_component": "成 (chéng)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of an axe 戊 striking down firmly to conclude peace or complete construction work.",
                "visual_mnemonic_story_en": "A weapon (戈) strikes a firm boundary mark, successfully completing the goal (成).",
                "visual_mnemonic_story_es": "Un arma de bronce (戈) fija el límite firme, consumando con éxito la meta (成).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IHS",
                "traditional": ""
            },
            {
                "character": "熟",
                "pinyin": "shú",
                "meaning_en": "cooked; ripe; familiar; skilled",
                "meaning_es": "cocido; maduro; familiar; diestro",
                "radical": "灬",
                "radical_meaning_en": "fire",
                "meaning_component": "灬 (fire boiling food) + 享 (offering in temple)",
                "sound_component": "孰 (shú, who/which / phonetic)",
                "stroke_count": 15,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Fire radical 灬 heating sacrificial offerings 孰 until fully cooked, soft, and fragrant.",
                "visual_mnemonic_story_en": "Cooking fire (灬) warms food until thoroughly tender and fully ripe (熟).",
                "visual_mnemonic_story_es": "Llamas de fuego (灬) cuecen la vianda hasta dejarla tierna y madura (熟).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YDOF",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When goals are accomplished (成) and grain is ripened over warmth (熟), full maturity is attained (成熟).",
            "composite_memory_hook_es": "Cuando la meta se cumple (成) y el fruto sazona con calor (熟), se alcanza la madurez (成熟).",
            "cultural_and_cognitive_roots": "Agricultural metaphor: crop ripening translated into human emotional poise, intellectual judgment, and institutional readiness.",
            "tone_sandhi_and_pitch_modulation": "Double rising second tones: 'chéng shú' (35-35). Rise smoothly from pitch 3 to 5 on 'chéng', then rise again clearly on 'shú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "城", "pinyin": "chéng", "meaning_en": "city; castle wall", "distinction_note": "Has earth radical 土 on left of 成"},
                {"character": "诚", "pinyin": "chéng", "meaning_en": "honest; sincere", "distinction_note": "Has speech radical 讠 on left of 成"},
                {"character": "孰", "pinyin": "shú", "meaning_en": "who; which", "distinction_note": "Lacks four fire dots 灬 underneath"},
                {"character": "热", "pinyin": "rè", "meaning_en": "hot; heat", "distinction_note": "Has 执 atop 灬 instead of 孰"}
            ],
            "etymological_cognates": [
                {"character": "练", "pinyin": "liàn", "gloss_en": "practiced; seasoned skill"},
                {"character": "满", "pinyin": "mǎn", "gloss_en": "full; completely replete"},
                {"character": "立", "pinyin": "lì", "gloss_en": "stand firm; establish"},
                {"character": "丰", "pinyin": "fēng", "gloss_en": "plentiful; bountiful yield"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "成熟 encompasses biological ripeness as well as human emotional, cognitive, and commercial readiness.",
            "contrasts": [
                {"id": "1", "compared_word": "成熟 vs. 老练", "pinyin": "lǎoliàn", "analysis": "老练 focuses specifically on being crafty, seasoned, and calculating through worldly experience, while 成熟 has a broader, positive tone of emotional balance and wisdom."},
                {"id": "2", "compared_word": "成熟 vs. 熟练", "pinyin": "shúliàn", "analysis": "熟练 describes technical dexterity and fast motor skill ('操作熟练'), while 成熟 describes inner character, timing, or fruit ripeness."},
                {"id": "3", "compared_word": "成熟 vs. 完善", "pinyin": "wánshàn", "analysis": "完善 describes systems, rules, or facilities that are comprehensive and without flaws, while 成熟 describes organic evolution to full readiness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "八月的江南水乡果实累累，果园里的葡萄藤上挂满了一串串紫晶般的葡萄。微风吹过，阳光透过茂密的绿叶洒在成熟的果实上，甘甜的果汁在薄薄的果皮下流淌，预示着又一个丰硕喜悦的丰收年景。",
                "pinyin": "Bāyuè de Jiāngnán shuǐxiāng guǒshí-lěilěi, guǒyuán lǐ de pútáoténg shàng guàmǎn le yíchuànchuàn zǐjīngbān de pútáo. Wēifēng chuīguò, yángguāng tòuguò màomì de lǜyè sǎ zài chéngshú de guǒshí shàng, gāntián de guǒzhī zài báobáo de guǒpí xià liútǎng, yùshì zhe yòu yí ge fēngshuò xǐyuè de fēngshōu niánjǐng.",
                "en": "In August southern wetlands, orchards abound with grape clusters like purple crystals. Sunbeams pierce leaves onto ripe fruit, sweet nectar flowing beneath thin skins, heralding a bountiful harvest.",
                "es": "En agosto, los huertos del sur rebosan racimos de uvas como cristales violáceos. El sol dora los frutos maduros y el jugo dulce bajo la fina piel vaticina una colosal y alegre cosecha."
            },
            {
                "id": "#2",
                "hanzi": "一个人真正的成熟，绝不是变得圆滑世故，而是看清生活的艰难本质后依然热爱生活。面对挫折时保持理智清醒，身处喧嚣时守住内心情操，以宽厚包容的心胸接纳差异，这才是经岁月淬炼出的生命高度。",
                "pinyin": "Yí ge rén zhēnzhèng de chéngshú, juébù shì biànde yuánhuá-shìgù, érshì kànqīng shēnghuó de jiānnán běnzhì hòu yīrán rè'ài shēnghuó. Miànduì cuòzhé shí bǎochí lǐzhì qīngxǐng, shēnchǔ xuānxiāo shí shǒuzhù nèixīn qíngcāo, yǐ kuānhòu bāoróng de xīnxxiōng jiēnà chāyì, zhè cáishì jīng suìyuè cuìliàn chū de shēngmìng gāodù.",
                "en": "True maturity is not cynical sophistication, but loving life after seeing its hardships. Staying rational in adversity, guarding integrity amidst noise, and embracing differences reflect seasoned wisdom.",
                "es": "La verdadera madurez no consiste en volverse taimado, sino en amar la vida tras conocer su aspereza. Guardar la serenidad ante reveses y cobijar empatía refleja la hondura que forja el tiempo."
            }
        ]
    },

    # 30 兄弟
    {
        "id": "30",
        "hanzi": "兄弟",
        "pinyin": "xiōng dì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "brothers; fraternal comrades; younger brother",
            "es": "hermanos; camaradas entrañables; hermano menor"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "brothers (elder and younger brothers collectively)",
                "definition_es": "hermanos (varones mayores y menores colectivamente)",
                "example_phrase": "他们是亲兄弟 (they are blood brothers)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "close male friends, comrades, or fraternal confederates",
                "definition_es": "camaradas, amigos entrañables o hermanos de causa",
                "example_phrase": "情同手足的兄弟 (brothers close as hands and feet)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这两兄弟从小志趣相投，大学毕业后携手创立了一家高新技术科技企业。",
                "pinyin": "Zhè liǎng xiōngdì cóngxiǎo zhìqù-xiāngtóu, dàxué bìyè hòu xiéshǒu chuànglì le yì jiā gāoxīnjìshù kējì qǐyè.",
                "en": "These two brothers shared identical interests from childhood; after college, they joined hands to found a high-tech firm.",
                "es": "Estos dos hermanos compartían aficiones desde la infancia; al graduarse de la universidad, fundaron juntos una firma de alta tecnología."
            },
            {
                "id": "#2",
                "hanzi": "当年在部队一起服役的战友们情同手足，几十年后聚会依然互称亲切的兄弟。",
                "pinyin": "Dāngnián zài bùduì yìqǐ fúyì de zhànyǒumen qíngtóngshǒuzú, jǐshí nián hòu jùhuì yīrán hùchēng qīnqiè de xiōngdì.",
                "en": "Comrades serving in the army were as close as hands and feet; reuniting decades later, they still affectionately call each other brothers.",
                "es": "Los compañeros de armas eran uña y carne en el ejército; décadas después, siguen llamándose entrañablemente hermanos."
            }
        ],
        "collocations": [
            {"hanzi": "亲兄弟", "en": "blood brothers"},
            {"hanzi": "兄弟情", "en": "brotherly bond / fraternity"},
            {"hanzi": "堂兄弟", "en": "paternal male cousins"},
            {"hanzi": "表兄弟", "en": "maternal/cross cousins"},
            {"hanzi": "兄弟俩", "en": "the two brothers"},
            {"hanzi": "结拜兄弟", "en": "sworn brothers"}
        ],
        "idioms": [
            {"hanzi": "情同手足", "pinyin": "qíng tóng shǒu zú", "meaning_en": "affectionate as hands and feet; close as brothers"},
            {"hanzi": "难兄难弟", "pinyin": "nàn xiōng nàn dì", "meaning_en": "fellow sufferers; brothers in tribulation"},
            {"hanzi": "情深义重", "pinyin": "qíng shēn yì zhòng", "meaning_en": "profound affection and weighty loyalty"},
            {"hanzi": "同舟共济", "pinyin": "tóng zhōu gòng jì", "meaning_en": "cross river in same boat; pull together in crisis"}
        ],
        "character_decomposition": [
            {
                "character": "兄",
                "pinyin": "xiōng",
                "meaning_en": "elder brother; senior male",
                "meaning_es": "hermano mayor; mayor",
                "radical": "儿",
                "radical_meaning_en": "human / legs",
                "meaning_component": "口 (mouth giving counsel) + 儿 (standing adult legs)",
                "sound_component": "兄 (xiōng)",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A standing person 儿 with an open mouth 口 praying to ancestors on behalf of younger siblings; the eldest brother.",
                "visual_mnemonic_story_en": "A tall person (儿) speaks with an elder voice (口) advising siblings as the elder brother (兄).",
                "visual_mnemonic_story_es": "Un hombre en pie (儿) alza la voz (口) para guiar a la familia como hermano mayor (兄).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RHU",
                "traditional": ""
            },
            {
                "character": "弟",
                "pinyin": "dì",
                "meaning_en": "younger brother; junior",
                "meaning_es": "hermano menor; joven; menor",
                "radical": "弓",
                "radical_meaning_en": "bow",
                "meaning_component": "弋 (wooden stake) + 弓 (leather cord wound around it)",
                "sound_component": "弟 (dì)",
                "stroke_count": 7,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A leather cord wound sequentially down around a wooden spindle; represents descending order of birth.",
                "visual_mnemonic_story_en": "Cord wraps step by step down a spool like birth order descending to the younger brother (弟).",
                "visual_mnemonic_story_es": "Una cuerda se enrolla sucesivamente hacia abajo simbolizando el orden del hermano menor (弟).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "CNLH",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Elder brother (兄) standing with younger brother (弟) bound in kinship forms brothers (兄弟).",
            "composite_memory_hook_es": "El hermano mayor (兄) y el hermano menor (弟) unidos en linaje forman los hermanos (兄弟).",
            "cultural_and_cognitive_roots": "Foundational pillar of Confucian familial ethics (悌道: fraternal piety); expanded through heroic literature (三国演义 桃园结义) into sworn brotherhood.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'xiōng dì' (55-51). Hold high pitch 55 on 'xiōng', then descend firmly on 'dì'. (Can neutralize to 'xiōngdi' in casual talk)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "况", "pinyin": "kuàng", "meaning_en": "condition; situation", "distinction_note": "Has water radical 冫 on left of 兄"},
                {"character": "党", "pinyin": "dǎng", "meaning_en": "political party", "distinction_note": "Has 尚-like top over 儿"},
                {"character": "第", "pinyin": "dì", "meaning_en": "ordinal prefix", "distinction_note": "Has bamboo radical 竹 on top of 弟"},
                {"character": "梯", "pinyin": "tī", "meaning_en": "ladder; stairs", "distinction_note": "Has wood radical 木 on left of 弟"}
            ],
            "etymological_cognates": [
                {"character": "友", "pinyin": "yǒu", "gloss_en": "two hands joined in friendship"},
                {"character": "朋", "pinyin": "péng", "gloss_en": "strings of cowries / friends"},
                {"character": "亲", "pinyin": "qīn", "gloss_en": "blood relative; close kin"},
                {"character": "侪", "pinyin": "chái", "gloss_en": "peers of same generation"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "兄弟 encompasses male sibling relationships as well as fraternal comrades united by deep loyalty.",
            "contrasts": [
                {"id": "1", "compared_word": "兄弟 vs. 朋友", "pinyin": "péngyou", "analysis": "朋友 is general for any social acquaintance or friendship, while 兄弟 implies deep, sworn, family-like loyalty and mutual devotion."},
                {"id": "2", "compared_word": "兄弟 vs. 弟兄", "pinyin": "dìxiong", "analysis": "弟兄 is often used in military or close gang contexts ('弟兄们冲啊'), while 兄弟 is standard for biological siblings and friends."},
                {"id": "3", "compared_word": "兄弟 vs. 同志", "pinyin": "tóngzhì", "analysis": "同志 emphasizes shared political ideals and revolutionary comradeship, whereas 兄弟 emphasizes personal emotional affinity."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统文化中历来崇尚“长幼有序、兄友弟恭”的家庭伦理美德。做兄长的要关爱呵护弟弟，做弟弟的要尊敬体恤兄长。兄弟之间齐心协力、和睦相处，家庭才能枝繁叶茂、兴旺发达。",
                "pinyin": "Zhōngguó chuántǒng wénhuà zhōng lìlái chóngshàng 'zhǎngyòu-yǒuxù, xiōngyǒu-dìgōng' de jiātíng lúnlǐ měidé. Zuò xiōngzhǎng de yào guān'ài hēhù dìdi, zuò dìdi de yào zūnjìng tǐxù xiōngzhǎng. Xiōngdì zhījiān qíxīn-xiélì, hémù xiāngchǔ, jiātíng cáinéng zhīfán-yèmào, xīngwàng fādá.",
                "en": "Traditional culture upholds fraternal harmony: elder brothers care for younger ones, while younger brothers respect seniors. When brothers unite cordially, the household prospers like leafy branches.",
                "es": "La cultura tradicional ensalza la concordia fraterna: el mayor protege y el menor venera. Cuando los hermanos aúnan voluntades en armonía, el hogar florece próspero y bien avenido."
            },
            {
                "id": "#2",
                "hanzi": "在法国电影先驱卢米埃尔兄弟的科研试验室里，兄弟俩分工明确、配合默契。他们共同发明了活动电影机，并于十九世纪末在巴黎大咖啡馆公开放映了第一部电影，携手开启了世界电影艺术的崭新时代。",
                "pinyin": "Zài Fǎguó diànyǐng xiānqū Lúmǐ'āi'ěr xiōngdì de kēyán shíyànshì lǐ, xiōngdì liǎ fēngōng míngquè, pèihé mòqì. Tāmen gòngtóng fāmíng le huódòng diànyǐngjī, bìng yú shíjiǔ shìjì mò zài Bālí dàkāfēiguǎn gōngkāi fàngyìng le dì-yī bù diànyǐng, xiéshǒu kāiqǐ le shìjiè diànyǐng yìshù de zhǎnxīn shídài.",
                "en": "In the Lumière brothers' workshop, the two worked in seamless harmony. Inventing the Cinématographe and premiering movies in late 19th-century Paris, they launched a glorious era of motion pictures.",
                "es": "En el laboratorio de los hermanos Lumière reinaba una armonía perfecta. Inventaron el cinematógrafo y proyectaron la primera película en París a fines del siglo XIX, inaugurando la era del cine."
            }
        ]
    }
]

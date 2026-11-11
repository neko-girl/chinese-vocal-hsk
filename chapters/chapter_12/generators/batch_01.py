# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 用户
    {
        "id": "1",
        "hanzi": "用户",
        "pinyin": "yòng hù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "user; consumer; subscriber; account holder",
            "es": "usuario; abonado; consumidor; cliente de servicios"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person, household, or organization that uses a service, product, telecommunications network, or software application",
                "definition_es": "persona, entidad o abonado que utiliza habitualmente un servicio, software o red de telecomunicaciones",
                "example_phrase": "注册用户 (registered user)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "微信凭借便捷的即时语音通信与朋友圈分享功能，在全球范围内吸引了数以亿计的活跃用户。",
                "pinyin": "Wēixìn píngjiè biànjié de jíshí yǔyīn tōngxìn yǔ péngyouquān fēnxiǎng gōngnéng, zài quánqiú fànwéi nèi xīyǐnle shùyǐyìjì de huóyuè yònghù.",
                "en": "Relying on convenient instant voice messaging and Moments sharing features, WeChat has attracted hundreds of millions of active users worldwide.",
                "es": "Gracias a la mensajería de voz instantánea y la función de Momentos, WeChat ha atraído a cientos de millones de usuarios activos en todo el mundo."
            },
            {
                "id": "#2",
                "hanzi": "互联网产品团队每周都会深入分析海外用户的操作反馈，以持续优化多语言界面体验。",
                "pinyin": "Hùliánwǎng chǎnpǐn tuánduì měizhōu dōuhuì shēnrù fēnxī hǎiwài yònghù de cāozuò fǎnkuì, yǐ chíxù yōuhuà duōyǔyán jièmiàn tǐyàn.",
                "en": "The Internet product team analyzes overseas users' operational feedback in depth every week to continuously optimize multilingual interface experience.",
                "es": "El equipo de desarrollo web analiza cada semana las valoraciones de los usuarios internacionales para optimizar la interfaz multilingüe."
            }
        ],
        "collocations": [
            {"hanzi": "活跃用户", "en": "active users"},
            {"hanzi": "海外用户", "en": "overseas users"},
            {"hanzi": "注册用户", "en": "registered users"},
            {"hanzi": "用户体验", "en": "user experience (UX)"},
            {"hanzi": "潜在用户", "en": "potential users"},
            {"hanzi": "用户反馈", "en": "user feedback"}
        ],
        "idioms": [
            {"hanzi": "家喻户晓", "pinyin": "jiā yù hù xiǎo", "meaning_en": "known to every household; widely known"},
            {"hanzi": "挨家挨户", "pinyin": "āi jiā āi hù", "meaning_en": "from door to door; every household"},
            {"hanzi": "门当户对", "pinyin": "mén dāng hù duì", "meaning_en": "well-matched in social and economic status"},
            {"hanzi": "物尽其用", "pinyin": "wù jìn qí yòng", "meaning_en": "make the best and fullest use of everything"}
        ],
        "character_decomposition": [
            {
                "character": "用",
                "pinyin": "yòng",
                "meaning_en": "use; employ; apply; utility",
                "meaning_es": "usar; emplear; aplicar; utilidad",
                "radical": "用",
                "radical_meaning_en": "use",
                "meaning_component": "Depiction of a divinatory shell/bucket utilized for ceremonial and practical tasks",
                "sound_component": "Self-phonetic yòng",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of an implement, framed container, or oracle shell being put into active functional service.",
                "visual_mnemonic_story_en": "A handy tool frame ready in hand to be put to active functional use (用).",
                "visual_mnemonic_story_es": "El armazón de una herramienta dispuesto para prestar utilidad inmediata (用).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BQI",
                "traditional": ""
            },
            {
                "character": "户",
                "pinyin": "hù",
                "meaning_en": "door; family; household; account",
                "meaning_es": "puerta de una hoja; hogar; familia; cuenta",
                "radical": "户",
                "radical_meaning_en": "door",
                "meaning_component": "Single wing of a wooden door hinged to a post",
                "sound_component": "Pictograph of single door leaf",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of a single wooden door flap (half of a double gate 門); extended to household and registered account.",
                "visual_mnemonic_story_en": "A single wooden door flap (户) swings open to welcome each registered household member.",
                "visual_mnemonic_story_es": "La hoja batiente de una puerta (户) que da paso a cada familia o titular abonado.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IS",
                "traditional": "戶"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "One who enters the doorway of a service (户) to actively use its tools (用) is a registered user (用户).",
            "composite_memory_hook_es": "Quien cruza el umbral (户) para servirse de un sistema (用) es un usuario o abonado (用户).",
            "cultural_and_cognitive_roots": "Derived from the ancient household registration system (户籍): each registered door (户) receiving state utilities and services.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'yòng hù' (51-51). Pronounce both with crisp falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "甩", "pinyin": "shuǎi", "meaning_en": "fling; swing", "distinction_note": "Bottom stroke hooks out sideways like an uncoiling whip, unlike 用"},
                {"character": "角", "pinyin": "jiǎo", "meaning_en": "horn; corner", "distinction_note": "Has slanted peak on top"},
                {"character": "尸", "pinyin": "shī", "meaning_en": "corpse", "distinction_note": "Lacks the top dot/slant stroke of 户"},
                {"character": "卢", "pinyin": "lú", "meaning_en": "surname Lu / vessel", "distinction_note": "Has bottom enclosure, unlike 户"}
            ],
            "etymological_cognates": [
                {"character": "客", "pinyin": "kè", "gloss_en": "guest; client"},
                {"character": "家", "pinyin": "jiā", "gloss_en": "family; household"},
                {"character": "民", "pinyin": "mín", "gloss_en": "people; citizen"},
                {"character": "人", "pinyin": "rén", "gloss_en": "human; person"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "用户 stresses the person or entity operating software, telecom, hardware, or subscribed digital accounts.",
            "contrasts": [
                {"id": "1", "compared_word": "用户 vs. 客户", "pinyin": "kèhù", "analysis": "客户 emphasizes business-to-business commercial purchasing clients who pay for goods ('大客户'), while 用户 emphasizes actual operational users of an app or tool."},
                {"id": "2", "compared_word": "用户 vs. 顾客", "pinyin": "gùkè", "analysis": "顾客 specifically denotes retail shoppers patronizing brick-and-mortar stores, restaurants, or supermarkets ('百货店顾客')."},
                {"id": "3", "compared_word": "用户 vs. 消费者", "pinyin": "xiāofèizhě", "analysis": "消费者 is a macroeconomic legal term for consumers spending money to consume goods, whereas 用户 focuses on utility/software usage."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在移动互联网时代，海量活跃用户是数字平台赖以生存和壮大的根基。软件开发商必须深入洞察不同国家用户的文化习惯与隐私顾虑，不断升级算法与界面交互，才能在全球化数字浪潮中赢得广大用户的长久信任。",
                "pinyin": "Zài yídòng hùliánwǎng shídài, hǎiliàng huóyuè yònghù shì shùzì píngtái làiyǐ shēngcún hé zhuàngdà de gēnjī. Ruǎnjiàn kāifāshāng bìxū shēnrù dòngchá bùtóng guójiā yònghù de wénhuà xíguàn yǔ yǐnsī gùlǜ, bùduàn shēngjí suànfǎ yǔ jièmiàn jiāohù, cáinéng zài quánqiúhuà shùzì làngcháo zhōng yíngdé guǎngdà yònghù de chángjiǔ xìnlài.",
                "en": "In the mobile internet era, vast active users are the cornerstone of digital platforms. Developers must discern cultural habits and privacy concerns across nations to continuously optimize interactions and win lasting user trust.",
                "es": "En la era del internet móvil, los usuarios activos son el pilar de las plataformas digitales. Las tecnológicas deben atender las costumbres culturales y la privacidad en cada país para ganar la confianza duradera de sus usuarios."
            },
            {
                "id": "#2",
                "hanzi": "为了有效提升海外用户的黏性，技术团队定期召开跨国视频会议，细致梳理每一条来自拉美和欧洲用户的测评意见。从精简注册验证流程到优化慢速网络下的语音通话质量，每一个细微功能的改善都体现出以用户需求为核心的创新理念。",
                "pinyin": "Wèile yǒuxiào tíshēng hǎiwài yònghù de niánxìng, jìshù tuánduì dìngqī zhāokāi kuàguó shìpín huìyì, xìzhì shūlǐ měi yī tiáo láizì Lāměi hé Ōuzhōu yònghù de cèpíng yìjiàn. Cóng jīngjiǎn zhùcè yànzhèng liúchéng dào yōuhuà mànsù wǎngluò xià de yǔyīn tōnghuà zhìliàng, měi yī gè xìwēi gōngnéng de gǎishàn dōu tǐxiàn chū yǐ yònghù xūqiú wéi héxīn de chuàngxīn lǐniàn.",
                "en": "To boost overseas user retention, technical teams hold international conferences to address feedback from Latin America and Europe. From streamlining registration to improving low-bandwidth calls, each update centers on user needs.",
                "es": "Para afianzar a los usuarios foráneos, el equipo técnico celebra reuniones periódicas analizando sugerencias de Latinoamérica y Europa. De agilizar el registro a optimizar llamadas con baja cobertura, cada ajuste prioriza al usuario."
            }
        ]
    },

    # 02 颠球
    {
        "id": "2",
        "hanzi": "颠球",
        "pinyin": "diān qiú",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to juggle a ball; bounce a ball continuously on one's foot/head",
            "es": "dar toques al balón; hacer jueguitos con la pelota; dominar el balón en el aire"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to bounce or juggle a ball repeatedly in the air using one's feet, thighs, chest, or head without letting it hit the ground (especially in soccer)",
                "definition_es": "dar toques consecutivos a una pelota en el aire con los pies, rodillas o cabeza sin dejarla caer al suelo",
                "example_phrase": "花式颠球 (freestyle football juggling)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在微信推广宣传片中，阿根廷足球明星梅西对着智能手机摄像头熟练地颠球，引发了海外球迷的狂热追捧。",
                "pinyin": "Zài Wēixìn tuīguǎng xuānchuánpiān zhōng, Āgēntíng zúqiú míngxīng Méixī duìzhe zhìnéng shǒujī shèxiàngtóu shúliàn de diānqiú, yǐnfāle hǎiwài qiúmí de kuángrè zhuīpěng.",
                "en": "In the WeChat promotional commercial, Argentine soccer star Messi skillfully juggled a ball toward the smartphone camera, triggering wild fan enthusiasm overseas.",
                "es": "En el anuncio promocional de WeChat, la estrella argentina Messi dio toques al balón ante la cámara del móvil, desatando el furor de los hinchas."
            },
            {
                "id": "#2",
                "hanzi": "小男孩每天放学后都在操场角落练习颠球，如今已经能够连续颠上一百多次而不落地。",
                "pinyin": "Xiǎonánhái měitiān fàngxué hòu dōu zài cǎochǎng jiǎoluò liànxí diānqiú, rújīn yǐjīng nénggòu liánxù diān shàng yībǎi duō cì ér bú luòdì.",
                "en": "The boy practices ball juggling in a playground corner every day after school; now he can juggle more than a hundred times without dropping the ball.",
                "es": "El niño entrena toques de balón en la cancha cada día al salir de clase; hoy ya consigue dar más de cien toques seguidos sin que toque el césped."
            }
        ],
        "collocations": [
            {"hanzi": "练习颠球", "en": "practice ball juggling"},
            {"hanzi": "熟练颠球", "en": "juggle a ball skillfully"},
            {"hanzi": "连续颠球", "en": "juggle continuously"},
            {"hanzi": "双脚颠球", "en": "juggle with both feet"},
            {"hanzi": "颠球技巧", "en": "ball juggling technique"},
            {"hanzi": "花式颠球", "en": "freestyle juggling"}
        ],
        "idioms": [
            {"hanzi": "颠扑不破", "pinyin": "diān pū bú pò", "meaning_en": "solid, irrefutable, and standing up to any test"},
            {"hanzi": "颠沛流离", "pinyin": "diān pèi liú lí", "meaning_en": "homeless and wandering; destitute in distress"},
            {"hanzi": "颠倒黑白", "pinyin": "diān dǎo hēi bái", "meaning_en": "turn black into white; invert right and wrong"},
            {"hanzi": "球场风云", "pinyin": "qiú chǎng fēng yún", "meaning_en": "ever-shifting fortunes on the ball field"}
        ],
        "character_decomposition": [
            {
                "character": "颠",
                "pinyin": "diān",
                "meaning_en": "crown of head; top; jolt; toss; bump",
                "meaning_es": "coronilla; cima; botar; sacudir; tambalearse",
                "radical": "页",
                "radical_meaning_en": "head / page",
                "meaning_component": "真 (genuine balance / erect posture) + 页 (human head / face)",
                "sound_component": "真 (zhēn / phonetic nuance diān)",
                "stroke_count": 16,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Crown of the head 页 bouncing up and down; by extension, tossing, jolting, or tapping something up into the air.",
                "visual_mnemonic_story_en": "The crown of a head (页) bobbing vertically while bouncing an object up and down (颠).",
                "visual_mnemonic_story_es": "La coronilla de la cabeza (页) cabeceando hacia arriba y abajo mientras bota un objeto (颠).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JCMBO",
                "traditional": "顛"
            },
            {
                "character": "球",
                "pinyin": "qiú",
                "meaning_en": "ball; sphere; globe; orb",
                "meaning_es": "pelota; balón; esfera; globo",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王/玉 (precious polished jade orb) + 求 (fur coat / seeking round form)",
                "sound_component": "求 (qiú, seek / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Jade radical 王 indicating a smooth polished spherical jade ball; later used for all sports balls and celestial globes.",
                "visual_mnemonic_story_en": "A gem of polished jade (王) carved into a perfect round ball to play with (球).",
                "visual_mnemonic_story_es": "Una gema de jade (王) pulida en esfera perfecta convertida en balón de juego (球).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MGIJE",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Tossing and jolting upward (颠) a round spherical ball (球) without letting it touch ground is ball juggling (颠球).",
            "composite_memory_hook_es": "Mantener botando en alto (颠) la pelota redonda (球) a toques rítmicos es dar toques al balón (颠球).",
            "cultural_and_cognitive_roots": "Relates to the ancient Chinese game of Cuju (蹴鞠), an imperial ball-bouncing ancestor of modern soccer practiced since the Han Dynasty.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by second tone: 'diān qiú' (55-35). Hold high ceiling 55, then glide up cleanly to 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "镇", "pinyin": "zhèn", "meaning_en": "town; suppress", "distinction_note": "Has metal radical 钅 on left instead of 页 in 颠"},
                {"character": "慎", "pinyin": "shèn", "meaning_en": "cautious; prudent", "distinction_note": "Has heart radical 忄 on left"},
                {"character": "救", "pinyin": "jiù", "meaning_en": "rescue; save", "distinction_note": "Has rap radical 攵 on right instead of jade 王 on left"},
                {"character": "求", "pinyin": "qiú", "meaning_en": "request; seek", "distinction_note": "Single character lacking jade radical 王"}
            ],
            "etymological_cognates": [
                {"character": "踢", "pinyin": "tī", "gloss_en": "kick"},
                {"character": "顶", "pinyin": "dǐng", "gloss_en": "head a ball; top"},
                {"character": "传", "pinyin": "chuán", "gloss_en": "pass the ball"},
                {"character": "射", "pinyin": "shè", "gloss_en": "shoot a goal"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "颠球 specifically means juggling or bouncing a ball continuously off one's feet, knees, or head in mid-air.",
            "contrasts": [
                {"id": "1", "compared_word": "颠球 vs. 运球", "pinyin": "yùnqiú", "analysis": "运球 refers to dribbling a ball across the ground or basketball court while advancing ('带球突破'), whereas 颠球 is juggling in the air without advancing."},
                {"id": "2", "compared_word": "颠球 vs. 踢球", "pinyin": "tīqiú", "analysis": "踢球 is the general term for playing soccer or kicking a football, while 颠球 is an individual technical ball-control drill."},
                {"id": "3", "compared_word": "颠球 vs. 垫球", "pinyin": "diànqiú", "analysis": "垫球 is a volleyball term for bumping the ball with forearms ('排球垫球'), while 颠球 predominantly applies to soccer ball juggling."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "颠球是足球运动员培养敏锐球感与身体协调性的必修基础功课。无论是世界顶级球星还是青训小将，每天都需要通过反复颠球来增强双脚对皮球旋转与弹跳力度的掌控感，为在激烈对抗中做出精妙停球打下扎实基石。",
                "pinyin": "Diānqiú shì zúqiú yùndòngyuán péiyǎng mǐnruì qiúgǎn yǔ shēntǐ xiétiáoxìng de bìxiū jīchǔ gōngkè. Wúlùn shì shìjiè dǐngjí qiúxīng háishì qīngxùn xiǎojiàng, měitiān dōu xūyào tōngguò fǎnfù diānqiú lái zēngqiáng shuāngjiǎo duì píqiú xuánzhuǎn yǔ tántiào lìdù de zhǎngkònggǎn, wèi zài jīliè duìkàng zhōng zuòchū jīngmiào tíngqiú dǎxià zhāshi jīshí.",
                "en": "Ball juggling is a mandatory fundamental for soccer players to hone sharp touch and bodily coordination. World-class stars and academy youths alike juggle daily to master ball spin and bounce, laying bedrock for exquisite ball control.",
                "es": "Dar toques al balón es un ejercicio imprescindible para futbolistas al pulir la sensibilidad del pie y la coordinación. Astros mundiales y canteranos dominan la pelota a toques cada día para controlar el bote y el efecto en el juego."
            },
            {
                "id": "#2",
                "hanzi": "在繁华都市的街头广场上，常能见到身怀绝技的街头花式足球高手。伴随着动感欢快的音乐节奏，他们不仅能用脚尖轻盈颠球，还能瞬间将球停在后颈或额头之上，精湛绝伦的颠球控球技巧引得围观市民阵阵喝彩。",
                "pinyin": "Zài fánhuá dūshì de jiētóu guǎngchǎng shàng, cháng néng jiàndào shēnhuái-juéjì de jiētóu huāshì zúqiú gāoshǒu. Bànsuízhe dònggǎn huānkuài de yīnyuè jiézòu, tāmen bùjǐn néng yòng jiǎojiān qīngyíng diānqiú, hái néng shùnjiān jiāng qiú tíng zài hòujǐng huò étóu zhīshàng, jīngzhàn juélún de diānqiú kòngqiú jìqiǎo yǐndé wéiguān shìmín zhènzhèn hècǎi.",
                "en": "In urban plazas, skilled freestyle football masters often perform. To upbeat music rhythms, they not only juggle lightly with toe tips, but freeze the ball on the back of neck or forehead, eliciting enthusiastic cheers from the crowd.",
                "es": "En las plazas céntricas es habitual ver a malabaristas del fútbol callejero. Al son de ritmos alegres, dan toques con la puntera y clavan el balón en la nuca o la frente, cosechando ovaciones con su portentoso control."
            }
        ]
    },

    # 03 明星
    {
        "id": "3",
        "hanzi": "明星",
        "pinyin": "míng xīng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "celebrity; star (movie, sports, entertainment); famous figure",
            "es": "estrella; celebridad; astro del deporte o espectáculo; figura famosa"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a widely famous and admired person in the performing arts, music, sports, or public life",
                "definition_es": "persona célebre y aclamada en el ámbito del espectáculo, el cine, el deporte o la vida pública",
                "example_phrase": "影视明星 (movie / TV star)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "腾讯公司重金签约国际足坛超级明星梅西作为微信的全球代言人，全面开启海外市场推广。",
                "pinyin": "Téngxùn gōngsī zhòngjīn qiānyuē guójì zútán chāojí míngxīng Méixī zuòwéi Wēixìn de quánqiú dàiyánrén, quánmiàn kāiqǐ hǎiwài shìchǎng tuīguǎng.",
                "en": "Tencent spent heavily to sign international football superstar Messi as WeChat's global brand ambassador, initiating worldwide market promotion.",
                "es": "Tencent invirtió cuantiosos fondos para fichar a la superestrella futbolística Messi como imagen global de WeChat, abriendo la campaña internacional."
            },
            {
                "id": "#2",
                "hanzi": "这位备受瞩目的青年体育明星不仅在奥运赛场上屡创佳绩，还热心投身于各项环保公益事业。",
                "pinyin": "Zhè wèi bèishòu zhǔmù de qīngnián tǐyù míngxīng bùjǐn zài Àoyùn sàichǎng shàng lǚ chuàng jiājì, hái rèxīn tóushēn yú gèxiàng huánbǎo gōngyì shìyè.",
                "en": "This high-profile young sports star not only repeatedly achieved excellence in the Olympic arena, but also enthusiastically dedicated himself to environmental charity.",
                "es": "Esta célebre promesa deportiva no solo cosechó laureles en los Juegos Olímpicos, sino que se involucró activamente en causas medioambientales."
            }
        ],
        "collocations": [
            {"hanzi": "超级明星", "en": "superstar"},
            {"hanzi": "体育明星", "en": "sports star"},
            {"hanzi": "影视明星", "en": "film and television star"},
            {"hanzi": "明星效应", "en": "celebrity effect / star power"},
            {"hanzi": "明星代言", "en": "celebrity endorsement"},
            {"hanzi": "当红明星", "en": "popular / current hot celebrity"}
        ],
        "idioms": [
            {"hanzi": "群星璀璨", "pinyin": "qún xīng cuǐ càn", "meaning_en": "brilliant cluster of bright stars; galaxy of talents"},
            {"hanzi": "明眸皓齿", "pinyin": "míng móu hào chǐ", "meaning_en": "bright eyes and gleaming white teeth; radiant beauty"},
            {"hanzi": "大红大紫", "pinyin": "dà hóng dà zǐ", "meaning_en": "extremely popular and widely successful in fame"},
            {"hanzi": "众星拱月", "pinyin": "zhòng xīng gǒng yuè", "meaning_en": "stars revolving around the moon; cluster around a respected center"}
        ],
        "character_decomposition": [
            {
                "character": "明",
                "pinyin": "míng",
                "meaning_en": "bright; clear; understand; brilliant",
                "meaning_es": "brillante; claro; luminoso; comprender",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun / solar brilliance) + 月 (moon / lunar clarity)",
                "sound_component": "Pictographic cosmic light",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Sun 日 and Moon 月 placed side by side, illuminating heaven and earth with celestial radiance and total clarity.",
                "visual_mnemonic_story_en": "The sun (日) and moon (月) shining together radiate supreme brightness (明).",
                "visual_mnemonic_story_es": "El sol (日) y la luna (月) brillando al unísono irradian una luz diáfana y deslumbrante (明).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "AB",
                "traditional": ""
            },
            {
                "character": "星",
                "pinyin": "xīng",
                "meaning_en": "star; heavenly body; spark; tiny dot",
                "meaning_es": "estrella; astro; chispa; punto brillante",
                "radical": "日",
                "radical_meaning_en": "sun / day",
                "meaning_component": "日 (celestial luminary) + 生 (sprout / birth of light)",
                "sound_component": "生 (shēng, born / phonetic xīng)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A celestial body 日 born 生 in the night sky; points of light glistening across the heavens.",
                "visual_mnemonic_story_en": "Bright solar sparks (日) born (生) across the dark night sky glitter as stars (星).",
                "visual_mnemonic_story_es": "Luces celestes (日) nacidas (生) en la bóveda nocturna titilan como estrellas (星).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "AHM",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A brilliant shining light (明) glittering high like a stellar luminary (星) in public life is a celebrity star (明星).",
            "composite_memory_hook_es": "La luminosidad deslumbrante (明) que brilla en lo alto cual astro del cielo (星) define a la estrella o celebridad (明星).",
            "cultural_and_cognitive_roots": "Originally denoted Venus the Morning Star (启明星). In modern media culture, extended to celebrated entertainment and athletic figures.",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by first tone: 'míng xīng' (35-55). Rise smoothly then sustain steady high pitch 55."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "朋", "pinyin": "péng", "meaning_en": "friend", "distinction_note": "Composed of two moons 月 月, lacking sun 日 in 明"},
                {"character": "萌", "pinyin": "méng", "meaning_en": "sprout; cute", "distinction_note": "Has grass radical 艹 on top of 明"},
                {"character": "醒", "pinyin": "xǐng", "meaning_en": "sober; wake up", "distinction_note": "Has wine vessel radical 酉 on left of 星"},
                {"character": "晨", "pinyin": "chén", "meaning_en": "morning; dawn", "distinction_note": "Has 辰 at bottom under 日 instead of 生 in 星"}
            ],
            "etymological_cognates": [
                {"character": "辰", "pinyin": "chén", "gloss_en": "celestial body; dragon sign"},
                {"character": "宿", "pinyin": "xiù", "gloss_en": "lunar constellation"},
                {"character": "曜", "pinyin": "yào", "gloss_en": "bright luminary; daylight"},
                {"character": "光", "pinyin": "guāng", "gloss_en": "light; glory"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "明星 specifically denotes widely celebrated performers, musicians, athletes, or public media idols.",
            "contrasts": [
                {"id": "1", "compared_word": "明星 vs. 名人", "pinyin": "míngrén", "analysis": "名人 encompasses prominent figures across politics, science, business, and literature, whereas 明星 concentrates on popular entertainment and sports icons."},
                {"id": "2", "compared_word": "明星 vs. 偶像", "pinyin": "ǒuxiàng", "analysis": "偶像 denotes an idol idolized passionately by fans for persona and looks, while 明星 highlights fame and star status in an industry."},
                {"id": "3", "compared_word": "明星 vs. 巨星", "pinyin": "jùxīng", "analysis": "巨星 is a superstar of legendary stature and historic cultural impact (e.g. Messi, Michael Jackson), far beyond a regular 明星."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在当今全球商业品牌竞争中，跨国企业常常借助体育明星的巨大声誉来迅速打开海外市场。足球明星那健康阳光的竞技形象与顽强拼搏的职业精神，能够跨越语言与文化的鸿沟，极大地增强全球年轻消费者对品牌的认同感。",
                "pinyin": "Zài dāngjīn quánqiú shāngyè pǐnpái jìngzhēng zhōng, kuàguó qǐyè chángcháng jièzhù tǐyù míngxīng de jùdà shēngyù lái xùnsù dǎkāi hǎiwài shìchǎng. Zúqiú míngxīng nà jiànkāng yángguāng de jìngjì xíngxiàng yǔ wánqiáng pīnbó de zhíyè jīngshén, nénggòu kuàyuè yǔyán yǔ wénhuà de hónggōu, jídà de zēngqiáng quánqiú niánqīng xiāofèizhě duì pǐnpái de rèntónggǎn.",
                "en": "In global brand competition, multinationals leverage sports stars' renown to unlock overseas markets. Athletes' energetic image and fighting spirit transcend language barriers, boosting brand loyalty among young consumers worldwide.",
                "es": "En la competencia de marcas globales, las multinacionales recurren al tirón de estrellas deportivas para abrir mercados. Su imagen enérgica y espíritu combativo salvan barreras culturales, afianzando la lealtad de la juventud mundial."
            },
            {
                "id": "#2",
                "hanzi": "随着自媒体与短视频平台的爆发式普及，聚光灯下的明星群体正面临着更为严格的社会公众审视。作为公众人物，明星不仅需要在专业演艺领域精益求精，更应在日常言行与社会公益中树立积极守法的优良榜样，传递文明向善的社会正能量。",
                "pinyin": "Suízhe zìméitǐ yǔ duǎnshìpín píngtái de bàofāshì pǔjí, jùguāngdēng xià de míngxīng qúntǐ zhèng miànlín zhe gèngwéi yángé de shèhuì gōngzhòng shěnshì. Zuòwéi gōngzhòng rénwù, míngxīng bùjǐn xūyào zài zhuānyè yǎnyì lǐngyù jīngyìqiújīng, gèng yīng zài rìcháng yánxíng yǔ shèhuì gōngyì zhōng shùlì jījí shǒufǎ de yōuliáng bǎngyàng, chuándì wénmíng xiàngshàn de shèhuì zhèngnéngliàng.",
                "en": "With the rise of social media and video apps, celebrities under the spotlight face stricter public scrutiny. As role models, they must hone their craft while setting positive moral examples in speech and charity.",
                "es": "Con el auge de las redes y vídeos cortos, las celebridades afrontan un escrutinio social más severo. Como figuras públicas, deben perfeccionar su arte y dar ejemplo de civismo y solidaridad en su conducta diaria."
            }
        ]
    },

    # 04 直播
    {
        "id": "4",
        "hanzi": "直播",
        "pinyin": "zhí bō",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to live broadcast; live stream; real-time webcast",
            "es": "transmitir en directo; retransmitir en vivo; emisión en vivo; directo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to transmit audio and video signals in real time without pre-recording or post-editing",
                "definition_es": "emitir señales de audio o vídeo en tiempo real sin grabación previa ni montaje posterior",
                "example_phrase": "现场直播 (live broadcast on site)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a live telecast, audio show, or internet streaming session conducted in real time",
                "definition_es": "programa audiovisual o sesión por internet difundida en riguroso directo",
                "example_phrase": "网络直播 (internet live streaming)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "亿万球迷通过手机客户端准时观看了世界杯决赛的全程高清网络直播，随时在聊天室分享喜悦。",
                "pinyin": "Yìwàn qiúmí tōngguò shǒujī kèhùduān zhǔnshí guānkànle Shìjièbēi juésài de quánchéng gāoqīng wǎngluò zhíbō, suíshí zài liáotiānshì fēnxiǎng xǐyuè.",
                "en": "Hundreds of millions of fans watched the HD live stream of the World Cup final on mobile apps, sharing excitement in chat rooms.",
                "es": "Cientos de millones de aficionados siguieron en directo de alta definición la final del Mundial por el móvil compartiendo su emoción en el chat."
            },
            {
                "id": "#2",
                "hanzi": "科技公司举行全球新品发布会时开启多平台同步直播，吸引了超过千万海外科技爱好者的在线参与。",
                "pinyin": "Kējì gōngsī jǔxíng quánqiú xīnpǐn fābùhuì shí kāiqǐ duō píngtái tóngbù zhíbō, xīyǐnle chāoguò qiānwàn hǎiwài kējì àihàozhě de zàixiàn cānyù.",
                "en": "When hosting its global product launch, the tech company streamed synchronously across multiple platforms, drawing tens of millions of overseas fans.",
                "es": "Al presentar su nuevo producto mundial, la tecnológica emitió en directo en múltiples plataformas, atrayendo a millones de entusiastas extranjeros."
            }
        ],
        "collocations": [
            {"hanzi": "网络直播", "en": "internet live streaming"},
            {"hanzi": "现场直播", "en": "live broadcast from site"},
            {"hanzi": "电视直播", "en": "live television telecast"},
            {"hanzi": "直播带货", "en": "live-stream shopping / e-commerce streaming"},
            {"hanzi": "开启直播", "en": "start a live stream"},
            {"hanzi": "同步直播", "en": "simulcast / synchronous live broadcast"}
        ],
        "idioms": [
            {"hanzi": "直抒胸臆", "pinyin": "zhí shū xiōng yì", "meaning_en": "express one's feelings candidly and directly"},
            {"hanzi": "名播四海", "pinyin": "míng bō sì hǎi", "meaning_en": "one's fame spreads across the four seas"},
            {"hanzi": "直截了当", "pinyin": "zhí jié liǎo dàng", "meaning_en": "direct and straightforward; blunt"},
            {"hanzi": "广播英名", "pinyin": "guǎng bō yīng míng", "meaning_en": "widely disseminate renowned glory"}
        ],
        "character_decomposition": [
            {
                "character": "直",
                "pinyin": "zhí",
                "meaning_en": "straight; direct; candid; directly",
                "meaning_es": "recto; directo; sincero; sin rodeos",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye looking straight ahead) + 十 (crosshairs / upright line)",
                "sound_component": "Archaic phonetic nuance",
                "stroke_count": 8,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "An eye 目 gazing along a plumb line without wavering; signifies straightness, immediacy, and directness.",
                "visual_mnemonic_story_en": "An open eye (目) fixed along a level plumb line looks straight and direct (直).",
                "visual_mnemonic_story_es": "El ojo (目) enfocado en línea perpendicular fija la mirada recta y directa sin desvíos (直).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JBM",
                "traditional": ""
            },
            {
                "character": "播",
                "pinyin": "bō",
                "meaning_en": "sow seeds; scatter; broadcast; disseminate",
                "meaning_es": "sembrar; esparcir; difundir; emitir",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand scattering seed) + 番 (sowing field partitions)",
                "sound_component": "番 (fān/bō, turn / phonetic)",
                "stroke_count": 15,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand 扌 scattering seeds across plowed field furrows 番; extended to transmitting signals widely over airwaves.",
                "visual_mnemonic_story_en": "A hand (扌) scattering grain seeds across wide farmland (番) broadcasts signals outward (播).",
                "visual_mnemonic_story_es": "Una mano (扌) que esparce semillas sobre campos de labranza (番) propaga ondas al aire (播).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QHDW",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Transmitting directly in real time (直) while broadcasting signals across the globe (播) is live broadcasting (直播).",
            "composite_memory_hook_es": "Emitir de forma directa e inmediata (直) esparciendo la señal al mundo (播) es transmitir en directo (直播).",
            "cultural_and_cognitive_roots": "Evolved from agricultural sowing (播种) to radio wave transmission (广播) and modern digital interactive live-streaming (网络直播).",
            "tone_sandhi_and_pitch_modulation": "Second tone followed by first tone: 'zhí bō' (35-55). Rise up with 35, then sustain flat high pitch 55."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "真", "pinyin": "zhēn", "meaning_en": "true; real", "distinction_note": "Has bottom feet 八-like strokes, unlike horizontal bar base of 直"},
                {"character": "值", "pinyin": "zhí", "meaning_en": "value; worth", "distinction_note": "Has person radical 亻 on left of 直"},
                {"character": "翻", "pinyin": "fān", "meaning_en": "turn over; translate", "distinction_note": "Has wings 羽 on right of 番 instead of hand 扌 on left"},
                {"character": "潘", "pinyin": "pān", "meaning_en": "surname Pan / water", "distinction_note": "Has water radical 氵 on left of 番"}
            ],
            "etymological_cognates": [
                {"character": "传", "pinyin": "chuán", "gloss_en": "transmit; disseminate"},
                {"character": "发", "pinyin": "fā", "gloss_en": "emit; launch"},
                {"character": "播", "pinyin": "bō", "gloss_en": "broadcast; sow"},
                {"character": "映", "pinyin": "yìng", "gloss_en": "reflect; project movie"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "直播 denotes real-time simultaneous broadcast without recorded delays or post-production montage.",
            "contrasts": [
                {"id": "1", "compared_word": "直播 vs. 转播", "pinyin": "zhuǎnbō", "analysis": "转播 emphasizes relaying or rebroadcasting a feed produced by another television station or satellite source, while 直播 is original real-time broadcasting."},
                {"id": "2", "compared_word": "直播 vs. 录播", "pinyin": "lùbō", "analysis": "录播 involves pre-recording, editing, and screening footage at a scheduled later time, the direct antonym of 直播."},
                {"id": "3", "compared_word": "直播 vs. 广播", "pinyin": "guǎngbō", "analysis": "广播 generally refers to radio broadcasting or public loudspeaker announcements, while 直播 emphasizes zero-latency live real-time coverage."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "得益于高速无线通信网络的全面覆盖，网络直播早已深入大众日常生活的方方面面。无论是大型国际体育赛事的实时战况，还是偏远乡村农产品的产地直销，直播技术拉近了人与人之间的时空距离，激发了数字经济的蓬勃活力。",
                "pinyin": "Déyì yú gāosù wúxiàn tōngxìn wǎngluò de quánmiàn fùgài, wǎngluò zhíbō zǎoyǐ shēnrù dàzhòng rìcháng shēnghuó de fāngfāng-miànmiàn. Wúlùn shì dàxíng guójì tǐyù sàishì de shíshí zhànkuàng, háishì piānyuǎn xiāngcūn nóngchǎnpǐn de chǎndì zhíxiāo, zhíbō jìshù lājìnle rén yǔ rén zhījiān de shíkōng jùlí, jīfāle shùzì jīngjì de péngbó huólì.",
                "en": "Benefiting from comprehensive high-speed mobile network coverage, live streaming has permeated daily life. From live sports events to farm produce sales in remote villages, streaming shortens spatial distance and invigorates digital commerce.",
                "es": "Gracias a la cobertura móvil de alta velocidad, las emisiones en directo forman parte de la vida cotidiana. De torneos deportivos a ventas agrícolas en aldeas, la retransmisión en vivo acorta distancias y dinamiza la economía digital."
            },
            {
                "id": "#2",
                "hanzi": "在线教育与学术交流领域同样深刻受益于高清直播技术的广泛应用。知名专家通过网络直播平台向全球不同时区的青年学者开展远程讲座，观众不仅能实时提问交流，还能通过互动弹幕即时探讨疑难问题，极大促进了优质教育资源的全球共享。",
                "pinyin": "Zàixiàn jiàoyù yǔ xuéshù jiāoliú lǐngyù tóngyàng shēnkè shòuyì yú gāoqīng zhíbō jìshù de guǎngfàn yìngyòng. Zhīmíng zhuānjiā tōngguò wǎngluò zhíbō píngtái xiàng quánqiú bùtóng shíqū de qīngnián xuézhě kāizhǎn yuǎnchéng jiǎngzuò, guānzhòng bùjǐn néng shíshí tíwèn jiāoliú, hái néng tōngguò hùdòng dànmù jíshí tàntǎo yínán wèntí, jídà cùjìnle yōuzhì jiàoyù zīyuán de quánqiú gòngxiǎng.",
                "en": "Online education and scholarship benefit profoundly from HD live streaming. Renowned scholars deliver lectures globally via streaming platforms, where audiences pose questions and debate in real-time, sharing quality educational resources.",
                "es": "La educación a distancia y el intercambio académico aprovechan la retransmisión en alta definición. Catedráticos imparten conferencias a diversas zonas horarias, donde el público interactúa en directo compartiendo recursos docentes de calidad."
            }
        ]
    },

    # 05 宝贝
    {
        "id": "5",
        "hanzi": "宝贝",
        "pinyin": "bǎo bèi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "baby; darling; cherished treasure; precious object",
            "es": "bebé; tesoro; cariño; joya preciada; persona o cosa idolatrada"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Colloquial",
                "definition_en": "term of endearment for a baby, beloved child, or romantic partner",
                "definition_es": "apelativo cariñoso para un bebé, niño pequeño o persona amada",
                "example_phrase": "可爱的宝贝 (adorable baby / darling)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a rare, valuable, or cherished object or treasure",
                "definition_es": "objeto de gran valor o joya preciosa atesorada con veneración",
                "example_phrase": "传家宝贝 (heirloom treasure)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在宣传广告中，梅西在手机这头逗着视频里啼哭的宝贝，温馨的亲情画面深深打动了海外观众。",
                "pinyin": "Zài xuānchuán guǎnggào zhōng, Méixī zài shǒujī zhètóu dòuzhe shìpín lǐ tíkū de bǎobèi, wēnxīn de qīnqíng huàmiàn shēndēn dǎdòngle hǎiwài guānzhòng.",
                "en": "In the commercial, Messi teased his crying baby over the phone video; this warm picture of family love deeply touched overseas audiences.",
                "es": "En el anuncio, Messi divertía a su bebé que lloraba al otro lado del móvil; una tierna escena familiar que conmovió a los televidentes."
            },
            {
                "id": "#2",
                "hanzi": "这块古老的怀表是祖父留下的传家宝贝，他始终小心翼翼地珍藏在首饰盒最深处。",
                "pinyin": "Zhè kuài gǔlǎo de huáibiǎo shì zǔfù liúxià de chuánjiā bǎobèi, tā shǐzhōng xiǎoxīn-yìyì de zhēncáng zài shǒushìhé zuì shēnchù.",
                "en": "This antique pocket watch is an heirloom treasure left by his grandfather, which he always cautiously cherishes deep in his jewelry box.",
                "es": "Este reloj de bolsillo antiguo es una joya familiar legada por su abuelo, conservada con sumo celo en el joyero."
            }
        ],
        "collocations": [
            {"hanzi": "心爱宝贝", "en": "beloved treasure / darling"},
            {"hanzi": "可爱的宝贝", "en": "cute baby; darling"},
            {"hanzi": "无价宝贝", "en": "priceless treasure"},
            {"hanzi": "宝贝儿子", "en": "darling son"},
            {"hanzi": "传家宝贝", "en": "family heirloom"},
            {"hanzi": "淘到宝贝", "en": "hunt down a rare treasure"}
        ],
        "idioms": [
            {"hanzi": "如获至宝", "pinyin": "rú huò zhì bǎo", "meaning_en": "as if finding a priceless treasure; overjoyed"},
            {"hanzi": "奇珍异宝", "pinyin": "qí zhēn yì bǎo", "meaning_en": "rare and extraordinary treasures"},
            {"hanzi": "物华天宝", "pinyin": "wù huá tiān bǎo", "meaning_en": "land rich in natural wealth and glories of heaven"},
            {"hanzi": "视若珍宝", "pinyin": "shì ruò zhēn bǎo", "meaning_en": "cherish and prize something like precious jewels"}
        ],
        "character_decomposition": [
            {
                "character": "宝",
                "pinyin": "bǎo",
                "meaning_en": "treasure; precious; jewel; cherish",
                "meaning_es": "tesoro; precioso; joya; atesorar",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (safe shelter/house) + 玉 (jade stone jewels)",
                "sound_component": "Historical phonetic nuance in 寶",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A house 宀 safely housing precious polished jade 玉 inside; represents priceless valuables and cherished jewels.",
                "visual_mnemonic_story_en": "Safely guarded under a house roof (宀), precious jade (玉) sparkles as treasure (宝).",
                "visual_mnemonic_story_es": "A buen recaudo bajo el techo del hogar (宀), el jade resplandeciente (玉) brilla como tesoro (宝).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "JMI",
                "traditional": "寶"
            },
            {
                "character": "贝",
                "pinyin": "bèi",
                "meaning_en": "cowrie shell; currency; wealth",
                "meaning_es": "concha marina; caurí; moneda antigua; riqueza",
                "radical": "贝",
                "radical_meaning_en": "shell",
                "meaning_component": "Cowrie seashell used as ancient primordial currency",
                "sound_component": "Pictograph of prized seashell bèi",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Pictograph of a bivalve cowrie seashell, the earliest currency of the Shang Dynasty; signifies wealth and valuable things.",
                "visual_mnemonic_story_en": "A rare shiny cowrie shell (贝) prized since ancient times as money and treasure.",
                "visual_mnemonic_story_es": "Una reluciente concha de caurí (贝), divisa ancestral símbolo de gran fortuna.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BO",
                "traditional": "貝"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Sheltered jade jewels (宝) paired with golden cowrie seashells (贝) constitute a precious treasure or darling baby (宝贝).",
            "composite_memory_hook_es": "El jade familiar bien resguardado (宝) junto a valiosas conchas (贝) conforma un tesoro o querido bebé (宝贝).",
            "cultural_and_cognitive_roots": "Cowries (贝) were China's earliest legal tender. Loving parents naturally regard their offspring as jewels more precious than silver and jade.",
            "tone_sandhi_and_pitch_modulation": "Third tone followed by fourth tone: 'bǎo bèi' (214-51). In familial speech ('我的小宝贝'), 'bèi' is often pronounced as a gentle neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "字", "pinyin": "zì", "meaning_en": "character; word", "distinction_note": "Has child 子 under 宀 instead of jade 玉 in 宝"},
                {"character": "宗", "pinyin": "zōng", "meaning_en": "ancestor; sect", "distinction_note": "Has altar 示 under 宀"},
                {"character": "见", "pinyin": "jiàn", "meaning_en": "see", "distinction_note": "Top stroke has an open window-eye, with legs, unlike 贝"},
                {"character": "页", "pinyin": "yè", "meaning_en": "page; head", "distinction_note": "Has top horizontal stroke 一 over 贝-like frame"}
            ],
            "etymological_cognates": [
                {"character": "珍", "pinyin": "zhēn", "gloss_en": "precious; treasure"},
                {"character": "珠", "pinyin": "zhū", "gloss_en": "pearl; bead"},
                {"character": "玉", "pinyin": "yù", "gloss_en": "jade stone"},
                {"character": "金", "pinyin": "jīn", "gloss_en": "gold; metal"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "宝贝 is used affectionately for darling babies, loved ones, or cherished irreplaceable personal possessions.",
            "contrasts": [
                {"id": "1", "compared_word": "宝贝 vs. 宝物", "pinyin": "bǎowù", "analysis": "宝物 refers strictly to historical relics, antique art, or magical treasures in stories ('洞穴中的宝物'), and cannot be used as an affectionate term for children."},
                {"id": "2", "compared_word": "宝贝 vs. 孩子", "pinyin": "háizi", "analysis": "孩子 is an objective neutral term for children or offspring, whereas 宝贝 conveys intense emotional fondness and parental pampering."},
                {"id": "3", "compared_word": "宝贝 vs. 珍品", "pinyin": "zhēnpǐn", "analysis": "珍品 denotes museum-grade rare collector items or high-end luxuries, whereas 宝贝 can be intimate, familial, and warm."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "婴儿清脆纯净的笑声往往是整个家庭最温馨的治愈良药。每当年轻父母劳累一天回到家中，看到摇篮里熟睡的可爱宝贝，所有疲惫与烦恼都会在刹那间烟消云散，心中满溢着为人父母的幸福与责任。",
                "pinyin": "Yīng'ér qīngcuì chúnjìng de xiàoshēng wǎngwǎng shì zhěnggè jiātíng zuì wēnxīn de zhìyù liángyào. Měidāng niánqīng fùmǔ láolèi yītiān huídào jiāzhōng, kàndào yáolán lǐ shúshuì de kě'ài bǎobèi, suǒyǒu píbèi yǔ fánnǎo dōuhuì zài chànà jiān yānxiāo-yúnsàn, xīnzhōng mǎnyì zhe wéirén fùmǔ de xìngfú yǔ zérèn.",
                "en": "An infant's pure laughter is often the most soothing medicine for a family. When exhausted young parents return home and see their sweet darling sleeping in the cradle, fatigue vanishes instantly, replaced by parental joy and duty.",
                "es": "La risa cantarina de un bebé es el mejor bálsamo en el hogar. Al volver del trabajo y ver al dulce angelito dormido en su cuna, el cansancio se esfuma de golpe, colmando el corazón de dicha y ternura paternal."
            },
            {
                "id": "#2",
                "hanzi": "民间收藏家老王对古代陶瓷情有独钟，走遍大江南北寻访流散在民间的艺术瑰宝。他将自己历经数十载淘来的这几件宋代青瓷视若性命，逢人便如数家珍地夸赞这些传世宝贝，字里行间流露出对中华传统工匠精神的无限崇敬。",
                "pinyin": "Mínjiān shǒucángjiā Lǎo Wáng duì gǔdài táocí qíngyǒudúzhōng, zǒubiàn dàjiāng-nánběi xúnfǎng liúsàn zài mínjiān de yìshù guībǎo. Tā jiāng zìjǐ lìjīng shùshí zǎi táolái de zhè jǐ jiàn Sòngdài qīngcí shì ruò xìngmìng, féng rén biàn rúshǔjiāzhēn de kuāzàn zhèxiē chuánshì bǎobèi, zìlǐ-xíngjiān liúlù chū duì Zhōnghuá chuántǒng gōngjiàng jīngshén de wúxiàn chóngjìng.",
                "en": "Folk collector Lao Wang has a passion for ancient ceramics, traveling nationwide to seek dispersed gems. Prized Song celadons collected over decades are cherished like life itself, praised to guests with profound respect for Chinese craft.",
                "es": "El coleccionista Lao Wang siente pasión por la cerámica clásica y ha recorrido el país en busca de tesoros. Valora como oro en paño sus celadones de la dinastía Song, alabándolos con devoción ante quienes admiran el arte tradicional."
            }
        ]
    },

    # 06 逗
    {
        "id": "6",
        "hanzi": "逗",
        "pinyin": "dòu",
        "part_of_speech": "Verb / Adjective",
        "meanings_summary": {
            "en": "to tease; amuse; provoke laughter; funny; amusing",
            "es": "hacer gracia; bromear; provocar risa; gracioso; chistoso; entretener"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to tease, play with, or playfully provoke a child or pet to bring forth laughter or amusement",
                "definition_es": "bromear con un niño o animal con ademanes cariñosos para hacerle sonreír o jugar",
                "example_phrase": "逗孩子笑 (tease a child to laugh)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Colloquial",
                "definition_en": "funny, comical, amusing, or witty",
                "definition_es": "divertido, cómico, ocurrente o gracioso",
                "example_phrase": "这人真逗 (this person is really funny / amusing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "足球巨星在微信视频广告中一边娴熟颠球一边逗孩子开心的场景，极具生活情趣。",
                "pinyin": "Zúqiú jùxīng zài Wēixìn shìpín guǎnggào zhōng yībiān xiánshú diānqiú yībiān dòu háizi kāixīn de chǎngjǐng, jíjù shēnghuó qíngqù.",
                "en": "The football superstar juggling a ball while teasing a child to make them happy in the WeChat ad was brimming with endearing warmth.",
                "es": "La escena del astro del fútbol dando toques al balón mientras hacía reír a un niño en el anuncio de WeChat derrochaba ternura."
            },
            {
                "id": "#2",
                "hanzi": "台上相声演员惟妙惟肖的滑稽模仿把全场观众逗得捧腹大笑，剧场里充满了快活的掌声。",
                "pinyin": "Tái shàng xiàngsheng yǎnyuán wéimiào-wéixiào de huájī mófǎng bǎ quánchǎng guānzhòng dòu de pěngfù-dàxiào, jùchǎng lǐ chōngmǎnle kuàihuo de zhǎngshēng.",
                "en": "The comic performer's lifelike mimicry on stage amused the entire audience into roaring laughter, filling the theater with merry clapping.",
                "es": "La cómica imitación del humorista sobre las tablas hizo desternillarse de risa al público, inundando la sala de aplausos alegres."
            }
        ],
        "collocations": [
            {"hanzi": "逗乐", "en": "amuse; evoke laughter"},
            {"hanzi": "逗笑", "en": "make somebody laugh"},
            {"hanzi": "逗孩子", "en": "play with / tease a child playfully"},
            {"hanzi": "逗小猫", "en": "tease / play with a kitten"},
            {"hanzi": "真逗", "en": "really funny; comical"},
            {"hanzi": "逗趣", "en": "funny; delight in jokes"}
        ],
        "idioms": [
            {"hanzi": "逗人喜爱", "pinyin": "dòu rén xǐ ài", "meaning_en": "endearing and lovely; appealing to everyone"},
            {"hanzi": "捧腹大笑", "pinyin": "pěng fù dà xiào", "meaning_en": "hold one's sides with uncontrollable laughter"},
            {"hanzi": "诙谐幽默", "pinyin": "huī xié yōu mò", "meaning_en": "humorous, witty, and playfully funny"},
            {"hanzi": "妙趣横生", "pinyin": "miào qù héng shēng", "meaning_en": "overflowing with delightful wit and fun"}
        ],
        "character_decomposition": [
            {
                "character": "逗",
                "pinyin": "dòu",
                "meaning_en": "tease; play; stay; funny; comma",
                "meaning_es": "bromear; provocar risa; detenerse; coma; gracioso",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (movement/action) + 豆 (ancient sacrificial vessel / bean)",
                "sound_component": "豆 (dòu, bean / phonetic carrier)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Movement radical 辶 combined with 豆; originally lingering or halting on a path, evolved to making playful gestures to entice laughter.",
                "visual_mnemonic_story_en": "Stopping on a stroll (辶) offering a sweet bean snack (豆) to tease a smile out of a puppy (逗).",
                "visual_mnemonic_story_es": "Hacer un alto en el camino (辶) tentando con un granito (豆) para hacer sonreír al chiquillo (逗).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YMRT",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pausing on your path (辶) with sweet playful gestures (豆) to amuse and tease (逗) a laughing child.",
            "composite_memory_hook_es": "Detener el paso (辶) ofreciendo juegos y chanzas (豆) para hacer reír con gracia (逗).",
            "cultural_and_cognitive_roots": "In classical literature, 逗 meant 'linger' or 'punctuation pause' (句逗). In vernacular Beijing Mandarin, it blossomed into the lively verb for comical amusement.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'dòu' (51). Crisp, energetic falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "豆", "pinyin": "dòu", "meaning_en": "bean; pea", "distinction_note": "Lacks the movement radical 辶 surrounding it in 逗"},
                {"character": "通", "pinyin": "tōng", "meaning_en": "connect; pass", "distinction_note": "Has 甬 inside 辶 instead of 豆 in 逗"},
                {"character": "透", "pinyin": "tòu", "meaning_en": "penetrate; clear", "distinction_note": "Has 秀 inside 辶"},
                {"character": "选", "pinyin": "xuǎn", "meaning_en": "choose", "distinction_note": "Has 先 inside 辶"}
            ],
            "etymological_cognates": [
                {"character": "戏", "pinyin": "xì", "gloss_en": "play; drama"},
                {"character": "玩", "pinyin": "wán", "gloss_en": "play with; amuse"},
                {"character": "弄", "pinyin": "nòng", "gloss_en": "handle; play with"},
                {"character": "耍", "pinyin": "shuǎ", "gloss_en": "frolic; brandish"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "逗 emphasizes lighthearted playful teasing or provoking benign laughter and entertainment.",
            "contrasts": [
                {"id": "1", "compared_word": "逗 vs. 戏弄", "pinyin": "xìnòng", "analysis": "戏弄 carries malicious prankish mockery or making a fool of someone, whereas 逗 is affectionate, benign, and warm."},
                {"id": "2", "compared_word": "逗 vs. 开玩笑", "pinyin": "kāiwánxiào", "analysis": "开玩笑 refers to making verbal jokes or harmless kidding, whereas 逗 includes physical gestures, facial expressions, and animal/baby teasing."},
                {"id": "3", "compared_word": "逗 vs. 取笑", "pinyin": "qǔxiào", "analysis": "取笑 means ridiculing someone's shortcomings to laugh at them, while 逗 is cheerful entertainment."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "午后温暖的阳台上，小女孩拿着一根逗猫棒不停地上下晃动，逗引着毛茸茸的波斯猫在木地板上翻滚扑腾。看着猫咪憨态可掬的滑稽动作，全家人都被逗得笑逐颜开，屋子里洋溢着浓郁温馨的家庭幸福气息。",
                "pinyin": "Wǔhòu wēnnuǎn de yángtái shàng, xiǎonǚhái názhe yī gēn dòumāobàng bùtíng de shàngxià huàngdòng, dòuyǐn zhe máorōngrōng de Bōsīmāo zài mùdìbǎn shàng fāngǔn pūteng. Kànzhe māomī hāntài-kějū de huájī dòngzuò, quánjiā rén dōu bèi dòu de xiàozhúyánkāi, wūzi lǐ yángyì zhe nóngyù wēnxīn de jiātíng xìngfú qìxī.",
                "en": "On the sunlit balcony, a girl waved a cat-teaser wand up and down, enticing a Persian cat to tumble on the wooden floor. Watching the kitty's comical antics, the family was amused into beaming smiles, basking in cozy household joy.",
                "es": "En la soleada terraza, la niña ondeaba un plumero haciendo jugar al gato persa, que rodaba por la tarima. Ante las cómicas piruetas del felino, todos estallaron en risas inundando la casa de calidez hogareña."
            },
            {
                "id": "#2",
                "hanzi": "北方传统相声艺术之所以历经百年沧桑仍深受欢迎，其核心魅力正在于演员高超的逗乐技巧。逗哏演员与捧哏搭档默契配合，凭借幽默诙谐的语言包袱与夸张传神的面部表情，总能出其不意地将现场观众逗得前仰后合。",
                "pinyin": "Běifāng chuántǒng xiàngsheng yìshù zhīsuǒyǐ lìjīng bǎinián cāngsāng réng shēnshòu huānyíng, qí héxīn mèilì zhèng zàiyú yǎnyuán gāochāo de dòulè jìqiǎo. Dòugén yǎnyuán yǔ pěnggén dādàng mòqì pèihé, píngjiè yōumò huīxié de yǔyán bāofu yǔ kuāzhāng chuánshén de miànbù biǎoqíng, zǒng néng chūqíbùyì de jiāng xiànchǎng guānzhòng dòu de qiányǎng-hòuhé.",
                "en": "Traditional crosstalk remains celebrated because of masters' comedic artistry. Comedians coordinate seamlessly, delivering witty punchlines and expressive miming that surprise and amuse spectators into helpless laughter.",
                "es": "La comedia tradicional crosstalk sigue cautivando por la maestría de sus cómicos. Los dos actores se compenetran con remates ingeniosos y gesticulaciones que arrancan carcajadas incontenibles entre el público."
            }
        ]
    },

    # 07 宣传
    {
        "id": "7",
        "hanzi": "宣传",
        "pinyin": "xuān chuán",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to publicize; propagate; promote; advertising; publicity",
            "es": "publicitar; difundir; promover; propaganda; divulgación; campaña publicitaria"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to disseminate information, concepts, policies, or brand values to the public to convince, attract, or educate them",
                "definition_es": "dar a conocer al público doctrinas, políticas, productos o marcas para persuadir o informar",
                "example_phrase": "宣传新政策 (publicize new policies)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "publicity materials, promotional drives, or advertising campaigns aimed at widespread audience reach",
                "definition_es": "campaña publicitaria, difusión mediática o conjunto de materiales divulgativos",
                "example_phrase": "宣传手册 (promotional brochure)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了在欧美和东南亚市场迅速打响知名度，微信策划了一系列极具视觉冲击力的国际宣传广告。",
                "pinyin": "Wèile zài Ōu-Měi hé Dōngnányà shìchǎng xùnsù dǎxiǎng zhīmíngdù, Wēixìn cèhuàle yī xìliè jíjù shìjué chōngjīlì de guójì xuānchuán guǎnggào.",
                "en": "To quickly build brand awareness in Western and Southeast Asian markets, WeChat planned a series of visually striking international promotional ads.",
                "es": "Para ganar notoriedad en Europa, América y el Sudeste Asiático, WeChat diseñó una serie de anuncios promocionales de gran impacto visual."
            },
            {
                "id": "#2",
                "hanzi": "社区志愿者走上街头向居民发放垃圾分类宣传手册，耐心讲解低碳环保的绿色生活理念。",
                "pinyin": "Shèqū zhìyuànzhě zǒushàng jiētóu xiàng jūmín fāfàng lājī fēnlèi xuānchuán shǒucè, nàixīn jiǎngjiě dītàn huánbǎo de lǜsè shēnghuó lǐniàn.",
                "en": "Community volunteers took to the streets to distribute garbage-sorting brochures to residents, patiently explaining green low-carbon living concepts.",
                "es": "Voluntarios comunitarios salieron a la calle para repartir folletos divulgativos sobre reciclaje, explicando pautas para un estilo de vida sostenible."
            }
        ],
        "collocations": [
            {"hanzi": "宣传活动", "en": "publicity campaign / promotional event"},
            {"hanzi": "大力宣传", "en": "vigorously promote / publicize widely"},
            {"hanzi": "宣传手册", "en": "promotional brochure / flyer"},
            {"hanzi": "宣传海报", "en": "promotional poster"},
            {"hanzi": "加大宣传", "en": "step up publicity"},
            {"hanzi": "宣传效果", "en": "publicity effect"}
        ],
        "idioms": [
            {"hanzi": "广而告之", "pinyin": "guǎng ér gào zhī", "meaning_en": "broadcast to all; advertise widely"},
            {"hanzi": "名扬四海", "pinyin": "míng yáng sì hǎi", "meaning_en": "fame resonates across the four seas"},
            {"hanzi": "大张旗鼓", "pinyin": "dà zhāng qí gǔ", "meaning_en": "with great fanfare and flying banners"},
            {"hanzi": "宣宾夺主", "pinyin": "xuān bīn duó zhǔ", "meaning_en": "minor guest eclipses the principal host"}
        ],
        "character_decomposition": [
            {
                "character": "宣",
                "pinyin": "xuān",
                "meaning_en": "proclaim; declare; announce; spread",
                "meaning_es": "proclamar; declarar; publicar; promulgar",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (imperial palace hall) + 亘 (soaring circular heaven / broad span)",
                "sound_component": "亘 (xuān/gèn, broad span)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "An imperial palace 宀 where imperial edicts are pronounced outward across all quarters 亘; solemn announcement.",
                "visual_mnemonic_story_en": "From high inside the palace pavilion (宀), the herald proclaims decrees broadly (宣).",
                "visual_mnemonic_story_es": "Desde el palacio imperial (宀), el pregonero proclama solemnemente a los cuatro vientos (宣).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JMAM",
                "traditional": ""
            },
            {
                "character": "传",
                "pinyin": "chuán",
                "meaning_en": "pass on; spread; convey; transmit",
                "meaning_es": "transmitir; difundir; pasar; propagar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / messenger) + 专 (spinning spindle / focused transmission)",
                "sound_component": "专 (zhuān / carrier phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A courier person 亻 traveling between relay posts to convey news and messages uninterruptedly like spun thread 专.",
                "visual_mnemonic_story_en": "A diligent messenger (亻) bearing single-minded focus (专) transmits announcements (传).",
                "visual_mnemonic_story_es": "Un emisario (亻) que viaja consagrado (专) a propagar las noticias por todo el reino (传).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OQNI",
                "traditional": "傳"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Proclaiming openly from the palace (宣) and having messengers pass the word widely (传) is publicizing and promoting (宣传).",
            "composite_memory_hook_es": "Proclamar edictos en público (宣) y hacer que los emisarios los difundan (传) es publicitar y divulgar (宣传).",
            "cultural_and_cognitive_roots": "From the ancient imperial office of the Grand Herald (宣谕使) tasked with broadcasting imperial laws and moral codes to the populace.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by second tone: 'xuān chuán' (55-35). Hold high pitch 55, then glide cleanly up to 35."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "宙", "pinyin": "zhòu", "meaning_en": "universe; time", "distinction_note": "Has 由 under 宀 instead of 亘 in 宣"},
                {"character": "室", "pinyin": "shì", "meaning_en": "room; chamber", "distinction_note": "Has 至 under 宀"},
                {"character": "专", "pinyin": "zhuān", "meaning_en": "specialized", "distinction_note": "Lacks person radical 亻 on left of 传"},
                {"character": "转", "pinyin": "zhuǎn", "meaning_en": "turn; shift", "distinction_note": "Has vehicle radical 车 on left of 专"}
            ],
            "etymological_cognates": [
                {"character": "告", "pinyin": "gào", "gloss_en": "tell; inform"},
                {"character": "布", "pinyin": "bù", "gloss_en": "declare; spread out"},
                {"character": "扬", "pinyin": "yáng", "gloss_en": "raise; praise; scatter"},
                {"character": "播", "pinyin": "bō", "gloss_en": "broadcast; disperse"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "宣传 involves planned, organized campaigns to broadcast policies, ideas, or products to mold public opinion or boost sales.",
            "contrasts": [
                {"id": "1", "compared_word": "宣传 vs. 推广", "pinyin": "tuīguǎng", "analysis": "宣传 stresses message dissemination and mental awareness through media/ads, whereas 推广 focuses on concrete adoption, operational deployment, and market penetration."},
                {"id": "2", "compared_word": "宣传 vs. 广告", "pinyin": "guǎnggào", "analysis": "广告 refers specifically to commercial advertising spots and paid media placements, while 宣传 can encompass non-commercial social/political advocacy."},
                {"id": "3", "compared_word": "宣传 vs. 传达", "pinyin": "chuándá", "analysis": "传达 denotes conveying internal directives, superior orders, or specific information to subordinates within an organization ('传达上级指示')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在新技术与新模式层出不穷的商业环境中，卓越的品牌宣传策略能够显著缩短新产品被大众市场接纳的周期。市场营销团队通过精准投放多维度多语种宣传物料，将核心科技亮点转化为消费者通俗易懂的生动故事。",
                "pinyin": "Zài xīnjìshù yǔ xīnmóshì céngchū-bùqióng de shāngyè huánjìng zhōng, zhuóyuè de pǐnpái xuānchuán cèlüè nénggòu xiǎnzhù suōduǎn xīn chǎnpǐn bèi dàzhòng shìchǎng jiēnà de zhōuqī. Shìchǎng yíngxiāo tuánduì tōngguò jīngzhǔn tóufàng duōwéidù duōyǔyán xuānchuán wùliào, jiāng héxīn kējì liàngdiǎn zhuǎnhuà wéi xiāofèizhě tōngsú-yìdǒng de shēngdòng gùshi.",
                "en": "Amid rapid technological evolution, exceptional promotional strategies shorten adoption cycles for new products. Marketing teams place multilingual materials strategically, translating tech highlights into compelling stories for consumers.",
                "es": "En un mercado de constante cambio técnico, una promoción brillante agiliza la adopción de productos novedosos. Los equipos de mercadotecnia lanzan contenidos en varias lenguas traduciendo avances técnicos en relatos atractivos."
            },
            {
                "id": "#2",
                "hanzi": "公共卫生部门在传染病高发季节之前，便深入各大学校与企事业单位开展防疫知识科普宣传。通过制作生动有趣的动画短片与分发图文并茂的宣传折页，不仅提高了广大居民的自我防护意识，更为构建坚实的群体免疫屏障奠定了群众基础。",
                "pinyin": "Gōnggòng wèishēng bùmén zài chuánrǎnbìng gāofā jìjié zhīqián, biàn shēnrù gè dà xuéxiào yǔ qǐshìyè dānwèi kāizhǎn fángyì zhīshi kēpǔ xuānchuán. Tōngguò zhìzuò shēngdòng yǒuqù de dònghuà duǎnpiàn yǔ fēnfā túwén-bìngmào de xuānchuán zhéyè, bùjǐn tígāole guǎngdà jūmín de zìwǒ fánghù yìshí, gèng wèi gòujiàn jiānshí de qúntǐ miǎnyì píngzhàng diàndìngle qúnzhòng jīchǔ.",
                "en": "Before seasonal contagion peaks, public health agencies conduct preventive publicity in schools and enterprises. By producing animated shorts and distributing brochures, they enhance self-protection awareness and build collective health defenses.",
                "es": "Sanidad Pública emprende campañas divulgativas en colegios y empresas antes de la temporada epidémica. Mediante vídeos animados y folletos ilustrados, fomentan la prevención individual apuntalando la inmunidad colectiva."
            }
        ]
    },

    # 08 手笔
    {
        "id": "8",
        "hanzi": "手笔",
        "pinyin": "shǒu bǐ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "style of handling affairs; bold financial move; master stroke; original manuscript",
            "es": "estilo magnánimo de obrar; despliegue audaz; golpe maestro; autógrafo; pluma"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the scale, boldness, generosity, or impressive style shown in executing an endeavor or commercial venture",
                "definition_es": "magnitud, audacia o generosidad con la que se acomete un proyecto, gasto o negocio",
                "example_phrase": "大手笔投资 (large-scale investment / bold financial move)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Formal",
                "definition_en": "an original piece of calligraphy, painting, or literary work executed by a renowned master's own hand",
                "definition_es": "manuscrito, cuadro o caligrafía original salido del propio puño y letra de un maestro",
                "example_phrase": "名家手笔 (the hand of a celebrated master)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "花费数千万美元签下全球最贵足球巨星并制作世界级广告，堪称中国互联网企业出海的大手笔。",
                "pinyin": "Huāfèi shùqiānwàn měiyuán qiānxià quánqiú zuì guì zúqiú jùxīng bìng zhìzuò shìjièjí guǎnggào, kānchēng Zhōngguó hùliánwǎng qǐyè chūhǎi de dàshǒubǐ.",
                "en": "Spending tens of millions of dollars to sign the world's highest-paid soccer superstar and produce ads was hailed as a magnificent bold stroke for Chinese tech expansion.",
                "es": "Invertir decenas de millones de dólares en fichar al futbolista más cotizado y rodar anuncios mundiales fue un despliegue grandioso del software chino."
            },
            {
                "id": "#2",
                "hanzi": "这座气势磅礴的国家大剧院建筑出自国际知名设计大师的手笔，线条流畅且极具未来感。",
                "pinyin": "Zhè zuò qìshì pángbó de guójiā dàjùyuàn jiànzhù chūzì guójì zhīmíng shèjì dàshī de shǒubǐ, xiàntiáo liúchàng qiě jíjù wèiláigǎn.",
                "en": "This majestic National Grand Theatre building came from the hand of an internationally renowned master architect, boasting flowing futuristic lines.",
                "es": "El monumental Gran Teatro Nacional salió de la pluma de un prestigioso arquitecto internacional, con líneas fluidas de aire vanguardista."
            }
        ],
        "collocations": [
            {"hanzi": "大手笔", "en": "grand gesture; bold scale; huge investment"},
            {"hanzi": "名家手笔", "en": "master's hand; work of a celebrated master"},
            {"hanzi": "惊人手笔", "en": "astonishingly bold move"},
            {"hanzi": "出自手笔", "en": "from the hand of..."},
            {"hanzi": "挥霍手笔", "en": "lavish spending style"},
            {"hanzi": "大师手笔", "en": "hand of a great master"}
        ],
        "idioms": [
            {"hanzi": "神来之笔", "pinyin": "shén lái zhī bǐ", "meaning_en": "a stroke of inspired genius; exquisite artistic touch"},
            {"hanzi": "妙笔生花", "pinyin": "miào bǐ shēng huā", "meaning_en": "gifted pen blossoming into brilliant literary works"},
            {"hanzi": "大手大脚", "pinyin": "dà shǒu dà jiǎo", "meaning_en": "wasteful, extravagant, and loose with money"},
            {"hanzi": "行家手笔", "pinyin": "háng jiā shǒu bǐ", "meaning_en": "the skilled craftsmanship of an expert professional"}
        ],
        "character_decomposition": [
            {
                "character": "手",
                "pinyin": "shǒu",
                "meaning_en": "hand; skill; person engaged in a craft",
                "meaning_es": "mano; destreza; operario; artesano",
                "radical": "手",
                "radical_meaning_en": "hand",
                "meaning_component": "Pictograph of an outstretched human hand with five fingers",
                "sound_component": "Pictograph of hand",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of an open human hand showing palm lines and five outstretched fingers; agency, skill, and personal execution.",
                "visual_mnemonic_story_en": "An outstretched hand (手) ready to grasp tools and execute grand bold deeds.",
                "visual_mnemonic_story_es": "Una mano abierta (手) que blande instrumentos para ejecutar obras con destreza.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "Q",
                "traditional": ""
            },
            {
                "character": "笔",
                "pinyin": "bǐ",
                "meaning_en": "writing brush; pen; stroke of brush; write",
                "meaning_es": "pincel; pluma; trazo caligráfico; escribir",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo brush shaft) + 毛 (animal hair brush tip)",
                "sound_component": "Historical phonetic nuance in 筆",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A writing instrument made from a slender bamboo shaft 竹 tufted with animal hair 毛; the traditional Chinese writing brush.",
                "visual_mnemonic_story_en": "Slender bamboo (竹) tipped with soft animal hair (毛) forms a writing brush (笔).",
                "visual_mnemonic_story_es": "Una caña de bambú (竹) con pelo fino en la punta (毛) da cuerpo al pincel de escribir (笔).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "HHU",
                "traditional": "筆"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A master's capable hand (手) wielding the ink brush (笔) with magnificent flourish represents a bold move or master stroke (手笔).",
            "composite_memory_hook_es": "La mano diestra (手) blandiendo el pincel (笔) con audacia majestuosa representa un despliegue grandioso o golpe maestro (手笔).",
            "cultural_and_cognitive_roots": "Originates from literary and artistic patronage: an emperor or wealthy patron deploying immense gold to commission grand poems and scrolls from famous brushes (名家手笔).",
            "tone_sandhi_and_pitch_modulation": "Two third tones in succession: 'shǒu bǐ' transforms via tone sandhi into (35-214). Pronounce 'shóu bǐ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "毛", "pinyin": "máo", "meaning_en": "hair; fur", "distinction_note": "Bottom stroke curves rightwards with a hook, unlike 手"},
                {"character": "乎", "pinyin": "hū", "meaning_en": "particle; at", "distinction_note": "Has a slanted hook and dots at top, unlike 手"},
                {"character": "竿", "pinyin": "gān", "meaning_en": "pole; rod", "distinction_note": "Has 干 under bamboo 竹 instead of 毛 in 笔"},
                {"character": "笛", "pinyin": "dí", "meaning_en": "flute", "distinction_note": "Has 由 under bamboo 竹"}
            ],
            "etymological_cognates": [
                {"character": "作", "pinyin": "zuò", "gloss_en": "make; compose; masterpiece"},
                {"character": "画", "pinyin": "huà", "gloss_en": "paint; drawing"},
                {"character": "划", "pinyin": "huà", "gloss_en": "plan; divide"},
                {"character": "构", "pinyin": "gòu", "gloss_en": "construct; conceive"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "手笔 denotes the boldness of scale and generous artistic or financial vision behind a venture or creative masterpiece.",
            "contrasts": [
                {"id": "1", "compared_word": "手笔 vs. 作风", "pinyin": "zuòfēng", "analysis": "作风 refers to habitual ethical conduct, workplace discipline, or political style ('艰苦朴素的作风'), whereas 手笔 evaluates the grandeur and daring scale of action."},
                {"id": "2", "compared_word": "手笔 vs. 举措", "pinyin": "jǔcuò", "analysis": "举措 refers to specific policy measures or strategic steps taken by governments or firms ('重大改革举措'), while 手笔 is evaluative and rhetorical."},
                {"id": "3", "compared_word": "手笔 vs. 魄力", "pinyin": "pòlì", "analysis": "魄力 denotes internal psychological courage and daring decisiveness of a person ('有魄力的领导'), while 手笔 describes the concrete scale and manifestation of work."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在推动数字经济与实体产业深度融合的进程中，该科技集团斥资数千亿元设立前沿基础科学实验室，展现出极具前瞻性的大手笔。这种不计短期成本、深耕底层核心算法与芯片研发的雄心，赢得了国际科技界的高度赞誉。",
                "pinyin": "Zài tuīdòng shùzì jīngjì yǔ shítǐ chǎnyè shēndù rónghé de jìnchéng zhōng, gāi kējì jítuán chìzī shùqiān yì yuán shèlì qiányán jīchǔ kēxué shíyànshì, zhǎnxiàn chū jíjù qiánzhānxìng de dàshǒubǐ. Zhèzhǒng bújì duǎnqī chéngběn, shēngēng dǐcéng héxīn suànfǎ yǔ xīnpiàn yánfā de xióngxīn, yíngdéle guójì kējìjiè de gāodù zànyù.",
                "en": "In merging the digital and real economies, the tech group invested hundreds of billions in foundational science labs, showing visionary boldness. This ambition to pioneer core algorithms regardless of short-term costs won global praise.",
                "es": "Para fundir la economía digital y la industria real, el consorcio invirtió cientos de miles de millones en laboratorios científicos, en un despliegue visionario. Esta apuesta por algoritmos y microchips cosechó elogios mundiales."
            },
            {
                "id": "#2",
                "hanzi": "漫步在苏州古典园林之中，游客无不惊叹于叠山理水之间所透露出的大师手笔。叠石高低错落、亭台曲径通幽，哪怕是窗框对准的一枝疏竹，都构成了宛若水墨画卷的精妙框景，处处流露出中国古典造园艺术的非凡神韵。",
                "pinyin": "Mànbù zài Sūzhōu gǔdiǎn yuánlín zhīzhōng, yóukè wúbù jīngtàn yú diéshān-lǐshuǐ zhījiān suǒ tòulù chū de dàshī shǒubǐ. Diéshí gāodī-cuòluò, tíngtái qūjìng-tōngyōu, nǎpà shì chuāngkuàng duìzhǔn de yī zhī shūzhú, dōu gòuchéngle wǎnrù shuǐmò huàjuàn de jīngmiào kuàngjǐng, chùchù liúlù chū Zhōngguó gǔdiǎn zàoyuán yìshù de fēifán shényùn.",
                "en": "Strolling through classical Suzhou gardens, visitors marvel at the masterly hand revealed in rocking and water layouts. Terraced stones, pavilions, and single bamboo branches framed in windows capture the timeless spirit of Chinese landscape art.",
                "es": "Al pasear por los jardines de Suzhou, los visitantes admiran la pluma magistral que dispuso rocallas y estanques. Pabellones y senderos serpenteantes enmarcan ramas de bambú evocando lienzos de aguada de inigualable belleza."
            }
        ]
    },

    # 09 推广
    {
        "id": "9",
        "hanzi": "推广",
        "pinyin": "tuī guǎng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to popularize; spread; promote; expand the adoption of",
            "es": "popularizar; generalizar; difundir; promover; extender el uso de"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to spread, expand, and popularize a method, technology, product, or experience so that it becomes widely adopted across broader areas",
                "definition_es": "difundir y extender el empleo o conocimiento de una técnica, experiencia, producto o idea para que se generalice ampliamente",
                "example_phrase": "推广新技术 (popularize / spread new technology)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "微信团队通过与多国本地知名电信运营商展开深度合作，在海外市场全力推广其移动社交平台。",
                "pinyin": "Wēixìn tuánduì tōngguò yǔ duō guó běndì zhīmíng diànxìn yùnyíngshāng zhǎnkāi shēndù hézuò, zài hǎiwài shìchǎng quánlì tuīguǎng qí yídòng shèjiāo píngtái.",
                "en": "Through deep cooperation with prominent local telecom carriers in multiple countries, the WeChat team fully promoted its mobile social platform overseas.",
                "es": "Colaborando estrechamente con operadoras de telecomunicaciones de varios países, el equipo de WeChat promocionó su red social móvil en el exterior."
            },
            {
                "id": "#2",
                "hanzi": "农业科技专家在西部干旱地区大力推广节水滴灌技术，帮助当地农民大幅提升了粮食产量。",
                "pinyin": "Nóngyè kējì zhuānjiā zài xībù gānhàn dìqū dàlì tuīguǎng jiéshuǐ dīguàn jìshù, bāngzhù dāngdì nóngmín dàfú tíshēngle liángshi chǎnliàng.",
                "en": "Agricultural science experts vigorously popularized water-saving drip irrigation in arid western regions, helping local farmers boost grain yields.",
                "es": "Expertos agrónomos promovieron el riego por goteo en zonas áridas del oeste, ayudando a los agricultores a elevar sustancialmente sus cosechas."
            }
        ],
        "collocations": [
            {"hanzi": "大力推广", "en": "vigorously promote / popularize"},
            {"hanzi": "推广应用", "en": "popularize the application of"},
            {"hanzi": "市场推广", "en": "market promotion / marketing"},
            {"hanzi": "推广经验", "en": "disseminate experience"},
            {"hanzi": "广泛推广", "en": "widely popularize"},
            {"hanzi": "推广普通话", "en": "popularize Putonghua (Standard Mandarin)"}
        ],
        "idioms": [
            {"hanzi": "推陈出新", "pinyin": "tuī chén chū xīn", "meaning_en": "weed through the old to bring forth the new"},
            {"hanzi": "广种薄收", "pinyin": "guǎng zhòng bó shōu", "meaning_en": "sow widely but reap meagerly"},
            {"hanzi": "推波助澜", "pinyin": "tuī bō zhù lán", "meaning_en": "push the waves and add to the billows; instigate"},
            {"hanzi": "广结良缘", "pinyin": "guǎng jié liáng yuán", "meaning_en": "form widespread ties of goodwill"}
        ],
        "character_decomposition": [
            {
                "character": "推",
                "pinyin": "tuī",
                "meaning_en": "push; shove; advance; elect; postpone",
                "meaning_es": "empujar; impulsar; promover; postergar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand pushing forward) + 隹 (short-tailed bird moving ahead)",
                "sound_component": "隹 (zhuī, bird / phonetic nuance)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand 扌 pushing a bird 隹 forward to make it take flight; represents exerting force to propel, promote, or recommend.",
                "visual_mnemonic_story_en": "A hand (扌) gently pushing a bird (隹) to take wing into the open air pushes forward (推).",
                "visual_mnemonic_story_es": "Una mano (扌) que impulsa suavemente a un ave (隹) a alzar el vuelo propulsa y empuja (推).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QOG",
                "traditional": ""
            },
            {
                "character": "广",
                "pinyin": "guǎng",
                "meaning_en": "wide; broad; vast; spread out",
                "meaning_es": "amplio; ancho; vasto; extender; difundir",
                "radical": "广",
                "radical_meaning_en": "shelter / hall open on side",
                "meaning_component": "A spacious hillside building or hall with wide open sides",
                "sound_component": "Archaic phonetic guǎng",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A wide sheltered building built against a cliff face with an open unobstructed expanse; denotes breadth, width, and spaciousness.",
                "visual_mnemonic_story_en": "A vast mountain pavilion roof (广) sheltering an expansive open ground.",
                "visual_mnemonic_story_es": "El alero de un vasto pabellón de montaña (广) que cubre una explanada sin límites.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "I",
                "traditional": "廣"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pushing an innovation with one's hand (推) across a vast and wide open realm (广) is popularizing and promoting it (推广).",
            "composite_memory_hook_es": "Empujar e impulsar con la mano (推) a lo largo de un vasto territorio (广) es difundir y popularizar (推广).",
            "cultural_and_cognitive_roots": "Used historically in agronomic treatises (如《齐民要术》): taking successful cultivation experiments in one village and pushing them wide (推广) across all prefectures.",
            "tone_sandhi_and_pitch_modulation": "First tone followed by third tone: 'tuī guǎng' (55-214). High level 55 followed by full dipping third tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "准", "pinyin": "zhǔn", "meaning_en": "standard; accurate", "distinction_note": "Has water 冫 on left of 隹 instead of hand 扌 in 推"},
                {"character": "堆", "pinyin": "duī", "meaning_en": "pile; heap", "distinction_note": "Has earth radical 土 on left of 隹"},
                {"character": "厂", "pinyin": "chǎng", "meaning_en": "factory; mill", "distinction_note": "Lacks the top dot stroke of 广"},
                {"character": "矿", "pinyin": "kuàng", "meaning_en": "mine; ore", "distinction_note": "Has stone radical 石 on left of 广"}
            ],
            "etymological_cognates": [
                {"character": "扩", "pinyin": "kuò", "gloss_en": "expand; enlarge"},
                {"character": "延", "pinyin": "yán", "gloss_en": "extend; prolong"},
                {"character": "展", "pinyin": "zhǎn", "gloss_en": "unfold; display"},
                {"character": "宣", "pinyin": "xuān", "gloss_en": "proclaim; spread"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "推广 emphasizes expanding the practical application, usage base, or territory of a product, technology, or successful method.",
            "contrasts": [
                {"id": "1", "compared_word": "推广 vs. 宣传", "pinyin": "xuānchuán", "analysis": "宣传 focuses on informational publicity and perceptual persuasion, while 推广 focuses on actual user adoption, distribution, and operational implementation."},
                {"id": "2", "compared_word": "推广 vs. 普及", "pinyin": "pǔjí", "analysis": "普及 describes the resulting state of something becoming ubiquitous and universally known among the masses, while 推广 is the active process to achieve it."},
                {"id": "3", "compared_word": "推广 vs. 拓宽", "pinyin": "tuòkuān", "analysis": "拓宽 applies to physically widening roads or abstractly broadening channels/horizons ('拓宽思路'), whereas 推广 refers to spreading methods and products."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "随着全球对绿色低碳理念的普遍重视，新能源汽车的推广普及工作在世界各大都市全面提速。各地政府通过完善公共充电桩基础设施、出台购车补贴与税收优惠政策，有力推动了绿色出行方式走进寻常百姓家。",
                "pinyin": "Suízhe quánqiú duì lǜsè dītàn lǐniàn de pǔbiàn zhòngshì, xīnnéngyuán qìchē de tuīguǎng pǔjí gōngzuò zài shìjiè gè dà dūshì quánmiàn tísù. Gèdì zhèngfǔ tōngguò wánshàn gōnggòng chōngdiànzhuāng jīchǔ shèshī, chūtái gòuchē bǔtiē yǔ shuìshōu yōuhuì zhèngcè, yǒulì tuīdòngle lǜsè chūxíng fāngshì zǒujìn xúncháng bǎixìng jiā.",
                "en": "With global emphasis on low-carbon ideals, promotion of new energy vehicles has accelerated worldwide. Governments expand charging piles and offer tax credits, propelling green commuting into everyday households.",
                "es": "Con el énfasis en la sostenibilidad, la promoción de vehículos eléctricos se acelera en las urbes. Al instalar puntos de carga y conceder exenciones fiscales, los gobiernos acercan el transporte ecológico a la ciudadanía."
            },
            {
                "id": "#2",
                "hanzi": "中国在脱贫攻坚与乡村振兴中总结出的一系列行之有效的发展模式，正通过联合国南南合作机制向广大发展中国家积极推广。从菌草种植到杂交水稻选育，这些因地制宜的农业技术为全球消除饥饿与贫困贡献了东方智慧。",
                "pinyin": "Zhōngguó zài tuōpín-gōngjiān yǔ xiāngcūn zhènxīng zhōng zǒngjié chū de yī xìliè xíngzhī-yǒuxiào de fāzhǎn móshì, zhèng tōngguò Liánhéguó Nán-Nán hézuò jīzhì xiàng guǎngdà fāzhǎnzhōng guójiā jījí tuīguǎng. Cóng jùncǎo zhòngzhí dào zájiāo shuǐdào xuǎnyù, zhèxiē yīndì-zhìyí de nóngyè jìshù wèi quánqiú xiāochú jī'è yǔ pínkùn gòngxiànle dōngfāng zhìhuì.",
                "en": "Effective rural revitalisation models developed in China are actively promoted to developing countries through UN South-South cooperation. From Juncao cultivation to hybrid rice, these adaptive technologies offer wisdom in ending hunger.",
                "es": "Los modelos de desarrollo rural cosechados en China se promueven activamente en países en desarrollo mediante la ONU. Del cultivo de hierba Juncao al arroz híbrido, estas técnicas agrícolas aportan sabiduría contra el hambre."
            }
        ]
    },

    # 10 注册
    {
        "id": "10",
        "hanzi": "注册",
        "pinyin": "zhù cè",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to register; enroll; sign up; incorporate (company, trademark, user account)",
            "es": "inscribirse; matricularse; registrarse; dar de alta; registrar (empresa o marca)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to formally enter one's name, credentials, or corporate details into an official record, university registry, or software user database",
                "definition_es": "inscribir formalmente el nombre, datos personales o mercantiles en un registro oficial, matrícula escolar o cuenta virtual",
                "example_phrase": "注册新账号 (register a new account)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "新用户只需在智能手机上输入手机号码并完成短信验证，就能在半分钟内轻松完成微信账号注册。",
                "pinyin": "Xīn yònghù zhǐxū zài zhìnéng shǒujī shàng shūrù shǒujī hàomǎ bìng wánchéng duǎnxìn yànzhèng, jiù néng zài bàn fēnzhōng nèi qīngsōng wánchéng Wēixìn zhànghào zhùcè.",
                "en": "New users need only enter their phone number on a smartphone and complete SMS verification to easily finish WeChat account registration in half a minute.",
                "es": "A un nuevo usuario le basta con introducir su número móvil y verificar el SMS para completar el registro de su cuenta de WeChat en medio minuto."
            },
            {
                "id": "#2",
                "hanzi": "为了保护自主研发的核心技术，初创公司第一时间向国家知识产权局提交了相关商标与专利的注册申请。",
                "pinyin": "Wèile bǎohù zìzhǔ yánfā de héxīn jìshù, chūchuàng gōngsī dì-yī shíjiān xiàng guójiā zhīshi chǎnquánjú tíjiāole xiāngguān shāngbiāo yǔ zhuānlì de zhùcè shēnqǐng.",
                "en": "To protect core independently-developed technologies, the startup immediately submitted registration applications for relevant trademarks and patents to the IP office.",
                "es": "Para proteger su tecnología patentada, la empresa emergente presentó de inmediato la solicitud de registro de marcas y patentes ante la oficina oficial."
            }
        ],
        "collocations": [
            {"hanzi": "注册用户", "en": "registered user"},
            {"hanzi": "注册账号", "en": "register an account"},
            {"hanzi": "注册资本", "en": "registered capital"},
            {"hanzi": "注册商标", "en": "registered trademark"},
            {"hanzi": "完成注册", "en": "complete registration"},
            {"hanzi": "注册手续", "en": "registration formalities / procedures"}
        ],
        "idioms": [
            {"hanzi": "名册在案", "pinyin": "míng cè zài àn", "meaning_en": "name entered on the official record or registry"},
            {"hanzi": "金榜题名", "pinyin": "jīn bǎng tí míng", "meaning_en": "one's name listed on the golden board of imperial exam successes"},
            {"hanzi": "著于竹帛", "pinyin": "zhù yú zhú bó", "meaning_en": "inscribed on bamboo slips and silk; recorded in history"},
            {"hanzi": "千秋留名", "pinyin": "qiān qiū liú míng", "meaning_en": "leave a glorious name down through thousands of autumns"}
        ],
        "character_decomposition": [
            {
                "character": "注",
                "pinyin": "zhù",
                "meaning_en": "pour into; record; concentrate; annotate",
                "meaning_es": "verter; anotar; registrar; concentrar; inyectar",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water poured continuously) + 主 (flame / lamp core / master)",
                "sound_component": "主 (zhǔ, master / phonetic zhù)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water 氵 flowing steadily into a vessel; extended to pouring attention, injecting funds, or entering records into registers.",
                "visual_mnemonic_story_en": "Streams of ink water (氵) poured by a master (主) onto paper to record names into a registry (注).",
                "visual_mnemonic_story_es": "Gotas de tinta (氵) que el titular (主) vierte sobre el pliego para asentar una partida (注).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EYG",
                "traditional": ""
            },
            {
                "character": "册",
                "pinyin": "cè",
                "meaning_en": "book; volume; booklet; bound ledger",
                "meaning_es": "libro; tomo; registro encuadernado; censo",
                "radical": "丿",
                "radical_meaning_en": "slash",
                "meaning_component": "Pictograph of bamboo slips strung together with leather thongs into an accordion roll",
                "sound_component": "Pictographic bound bamboo book cè",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A pictograph of ancient bamboo slips tied together side by side with cords; an archival volume, roster, or book.",
                "visual_mnemonic_story_en": "Slender bamboo strips linked side by side with leather strings form an ancient registry volume (册).",
                "visual_mnemonic_story_es": "Tablillas de bambú enlazadas con correas formando un códice o libro de registro (册).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BT",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pouring one's verified credentials (注) into the official bound ledger volume (册) is completing registration (注册).",
            "composite_memory_hook_es": "Anotar con tinta (注) el nombre en el libro encuadernado o censo (册) es inscribirse o registrarse (注册).",
            "cultural_and_cognitive_roots": "From the ancient imperial census roster (黄册) where each household's taxes and land parcels were recorded into binding books (册).",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'zhù cè' (51-51). Pronounce both syllables with firm, crisp falling pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "住", "pinyin": "zhù", "meaning_en": "reside; live", "distinction_note": "Has person radical 亻 on left of 主 instead of water 氵 in 注"},
                {"character": "往", "pinyin": "wǎng", "meaning_en": "go; toward", "distinction_note": "Has step radical 彳 on left of 主"},
                {"character": "珊", "pinyin": "shān", "meaning_en": "coral", "distinction_note": "Has jade radical 王 on left of 册"},
                {"character": "删", "pinyin": "shān", "meaning_en": "delete; edit", "distinction_note": "Has knife radical 刂 on right of 册"}
            ],
            "etymological_cognates": [
                {"character": "登", "pinyin": "dēng", "gloss_en": "ascend; record on roster"},
                {"character": "记", "pinyin": "jì", "gloss_en": "record; remember"},
                {"character": "录", "pinyin": "lù", "gloss_en": "record; register"},
                {"character": "籍", "pinyin": "jí", "gloss_en": "census register; record"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "注册 refers specifically to formal administrative, legal, academic, or digital entry into an authorized registry or system.",
            "contrasts": [
                {"id": "1", "compared_word": "注册 vs. 登记", "pinyin": "dēngjì", "analysis": "登记 is a broader term for writing down names or information (e.g. hotel check-in 住宿登记, visitor logs 来访登记), while 注册 often confers official membership, corporate legal standing, or an online account."},
                {"id": "2", "compared_word": "注册 vs. 报名", "pinyin": "bàomíng", "analysis": "报名 specifically denotes signing up for an exam, competition, or event ('报名参赛'), whereas 注册 is matriculating or setting up an account."},
                {"id": "3", "compared_word": "注册 vs. 备案", "pinyin": "bèi'àn", "analysis": "备案 means filing documents with authorities for future record without necessarily needing prior approval ('网站备案'), while 注册 establishes formal standing."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "每年九月初秋时节，各大高校校园里随处可见充满朝气的大一新生。新生们手持录取通知书在各个学院报到点有序办理入学注册手续，领取属于自己的学生证与校园卡，满怀憧憬地翻开人生崭新的大学篇章。",
                "pinyin": "Měinián jiǔyuè chūqiū shíjié, gè dà gāoxiào xiàoyuán lǐ suíchù kějiàn chōngmǎn zhāoqì de dàyī xīnshēng. Xīnshēngmen shǒuchí lùqǔ tōngzhīshū zài gègè xuéyuàn bàodào diǎn yǒuxù bànlǐ rùxué zhùcè shǒuxù, lǐngqǔ shǔyú zìjǐ de xuéshēngzhèng yǔ xiàoyuánkǎ, mǎnhuái chōngjǐng de fānkāi rénshēng zhǎnxīn de dàxué piānzhāng.",
                "en": "In early September, university campuses are filled with vibrant freshmen. Holding acceptance letters, new students orderly complete matriculation registration at faculties, receiving student IDs to begin a new college chapter.",
                "es": "A principios de septiembre, los campus universitarios bullen de novatos ilusionados. Con la carta de admisión en mano, formalizan la matrícula en sus facultades y recogen el carné estudiantil abriendo una nueva etapa vital."
            },
            {
                "id": "#2",
                "hanzi": "在推动数字政务转型的背景下，政府部门大幅简化了新设企业的营业执照注册流程。如今创业者只需登录统一政务服务平台在线填报电子材料，不到一个工作日便能顺利拿到电子营业执照，极大地激发了全社会的创新创业活力。",
                "pinyin": "Zài tuīdòng shùzì zhèngwù zhuǎnxíng de bèijǐng xià, zhèngfǔ bùmén dàfú jiǎnhuàle xīnsè qǐyè de yíngyè zhízhào zhùcè liúchéng. Rújīn chuàngyèzhě zhǐxū dēnglù tǒngyī zhèngwù fúwù píngtái zàixiàn tiánbào diànzǐ cáiliào, búdào yī gè gōngzuòrì biàn néng shùnlì nádào diànzǐ yíngyè zhízhào, jídà de jīfāle quán shèhuì de chuàngxīn chuàngyè huólì.",
                "en": "Amid digital administration reforms, governments have drastically streamlined business license registration. Today, entrepreneurs fill out electronic forms online to obtain e-licenses in less than one business day, spurring entrepreneurship.",
                "es": "En plena digitalización administrativa, las autoridades han simplificado el registro mercantil. Los emprendedores completan formularios en línea obteniendo su licencia electrónica en menos de un día hábil, impulsando la iniciativa empresarial."
            }
        ]
    }
]

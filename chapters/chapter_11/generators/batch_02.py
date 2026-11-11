# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 现代
    {
        "id": "11",
        "hanzi": "现代",
        "pinyin": "xiàn dài",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "modern times; the contemporary era; modern; contemporary",
            "es": "época moderna; era contemporánea; moderno; actual"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the historical period of current or recent times",
                "definition_es": "período histórico actual o reciente; la época contemporánea",
                "example_phrase": "现代社会 (modern society)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "belonging to or characteristic of present or recent times; up-to-date",
                "definition_es": "perteneciente o relativo a la época presente; avanzado y actual",
                "example_phrase": "现代化的设施 (modernized facilities)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "高速发展的高新科技正在以惊人的速度深刻重塑着现代人们的日常生活方式。",
                "pinyin": "Gāosù fāzhǎn de gāoxīnkējì zhèngzài yǐ jīngrén de sùdù shēnkè chóngsù zhe xiàndài rénmen de rìcháng shēnghuó fāngshì.",
                "en": "Rapidly advancing high technology is deeply reshaping the everyday lifestyles of modern people at an astonishing pace.",
                "es": "El veloz desarrollo de la alta tecnología está remodelando profundamente y a ritmo vertiginoso el modo de vida de las personas de hoy."
            },
            {
                "id": "#2",
                "hanzi": "这座新建的国际机场航站楼设计前卫，配备了世界顶尖水准的现代化智能值机系统。",
                "pinyin": "Zhè zuò xīnjiàn de guójì jīchǎng hángzhànlóu shèjì qiánwèi, pèibèi le shìjiè dǐngjiān shuǐzhǔn de xiàndàihuà zhìnéng zhíjī xìtǒng.",
                "en": "The newly built international airport terminal boasts avant-garde design and is equipped with world-class modernized smart check-in systems.",
                "es": "La nueva terminal del aeropuerto internacional luce un diseño vanguardista y cuenta con sistemas de facturación inteligentes de última generación."
            }
        ],
        "collocations": [
            {"hanzi": "现代社会", "en": "modern society"},
            {"hanzi": "现代化", "en": "modernization; modernize"},
            {"hanzi": "现代科学", "en": "modern science"},
            {"hanzi": "现代生活", "en": "modern life"},
            {"hanzi": "现代艺术", "en": "modern/contemporary art"},
            {"hanzi": "现代汉语", "en": "Modern Chinese (Putonghua)"}
        ],
        "idioms": [
            {"hanzi": "与时俱进", "pinyin": "yǔ shí jù jìn", "meaning_en": "advance with the times; keep abreast of developments"},
            {"hanzi": "日新月异", "pinyin": "rì xīn yuè yì", "meaning_en": "change and progress with each passing day"},
            {"hanzi": "古为今用", "pinyin": "gǔ wéi jīn yòng", "meaning_en": "make the ancient serve the present"},
            {"hanzi": "革故鼎新", "pinyin": "gé gù dǐng xīn", "meaning_en": "cast off the old and embrace the new"}
        ],
        "character_decomposition": [
            {
                "character": "现",
                "pinyin": "xiàn",
                "meaning_en": "appear; present; current; now",
                "meaning_es": "aparecer; presente; actual; ahora",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王 (fine jade emerging) + 见 (observing eye seeing clearly)",
                "sound_component": "见 (jiàn / phonetic origin)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Carving raw jade stone 王 until its inner luster becomes visible to the eye 见; denotes appearing, manifesting, or the present moment.",
                "visual_mnemonic_story_en": "A lapidary polishes jade (王) until its brilliant luster appears (现) before our eyes (见).",
                "visual_mnemonic_story_es": "Un artesano pule el jade (王) hasta que su brillo resplandece patente (现) a la vista (见).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MGBU",
                "traditional": "現"
            },
            {
                "character": "代",
                "pinyin": "dài",
                "meaning_en": "generation; era; substitute; replace",
                "meaning_es": "generación; era; época; sustituir",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person) + 弋 (stake marking boundary/shift)",
                "sound_component": "弋 (yì, stake / phonetic)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 standing guard at a post marked by a stake 弋 until replaced by the next sentinel; represents generations, eras, and substitution.",
                "visual_mnemonic_story_en": "A guard (亻) takes over the post marked by a stake (弋), handing duties down from generation to generation (代).",
                "visual_mnemonic_story_es": "Un centinela (亻) releva la guardia junto a la estaca (弋) transmitiendo el relevo generacional (代).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OIP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The era (代) manifesting in the living present (现) is the modern era (现代).",
            "composite_memory_hook_es": "La época o relevo (代) que se manifiesta en el presente vivo (现) es la era moderna (现代).",
            "cultural_and_cognitive_roots": "Historiographical era triad: 古代 (ancient times), 近代 (modern era from late Qing/Opium War to May Fourth), 现代 (contemporary era).",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'xiàn dài' (51-51). Descend sharply on 'xiàn', then land with a firm snap on 'dài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; compass", "distinction_note": "Has 夫 on left of 见 instead of jade 王 in 现"},
                {"character": "视", "pinyin": "shì", "meaning_en": "look; inspect", "distinction_note": "Has altar 礻 on left of 见"},
                {"character": "伐", "pinyin": "fá", "meaning_en": "cut down; attack", "distinction_note": "Has dagger-axe 戈 on right of 亻 instead of 弋 in 代"},
                {"character": "化", "pinyin": "huà", "meaning_en": "transform", "distinction_note": "Has 匕 on right of 亻"}
            ],
            "etymological_cognates": [
                {"character": "今", "pinyin": "jīn", "gloss_en": "present time; now"},
                {"character": "世", "pinyin": "shì", "gloss_en": "generation of thirty years; world"},
                {"character": "纪", "pinyin": "jì", "gloss_en": "silk thread era; century"},
                {"character": "新", "pinyin": "xīn", "gloss_en": "new; fresh timber"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "现代 denotes the present historical era (spanning roughly from the 20th century to the present day).",
            "contrasts": [
                {"id": "1", "compared_word": "现代 vs. 当代", "pinyin": "dāngdài", "analysis": "当代 specifically denotes the immediate current living generation (post-1949 or current decades), while 现代 broadly spans the 20th century forward."},
                {"id": "2", "compared_word": "现代 vs. 近代", "pinyin": "jìndài", "analysis": "近代 in Chinese historiography designates the era from the 1840 Opium War to 1919 May Fourth Movement, strictly distinct from 现代."},
                {"id": "3", "compared_word": "现代 vs. 目前", "pinyin": "mùqián", "analysis": "目前 is a short-term temporal adverb meaning 'at present / currently' ('目前没有问题'), whereas 现代 is macroscopic historical time."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "步入现代社会，都市生活节奏日益加快，琳琅满目的智能手机与移动网络极大地便利了人们的衣食住行。然而伴随信息爆炸与全天候连接，现代人也面临着前所未有的心理压力、数字焦虑与睡眠剥夺挑战。",
                "pinyin": "Bùrù xiàndài shèhuì, dūshì shēnghuó jiézòu rìyì jiākuài, línláng-mǎnmù de zhìnéng shǒujī yǔ yídòng wǎngluò jídà de biànlì le rénmen de yī-shí-zhù-xíng. Rán'ér bànsuí xìnxī bàozhà yǔ quántiānhòu liánjiē, xiàndàirén yě miànlín zhe qiánsuǒwèijiàn de xīnlǐ yālì, shùzì jiāolǜ yǔ shuìmián bōduó tiǎozhàn.",
                "en": "Entering modern society, urban tempos accelerate as smartphones and mobile networks streamline life. Yet alongside information explosions and perpetual connectivity, modern people face unprecedented mental stress and sleep deprivation.",
                "es": "En la sociedad moderna el ritmo urbano se acelera con móviles y redes telemáticas. Empero, la hiperconexión acarrea tensiones inéditas, ansiedad digital y privación del descanso reparador."
            },
            {
                "id": "#2",
                "hanzi": "中国式现代化既有各国现代化的共同特征，更有基于自己国情的鲜明中国特色。它是人口规模巨大的现代化，是全体人民共同富裕的现代化，是物质文明和精神文明相协调的现代化，为人类探索更好社会制度贡献了中国智慧。",
                "pinyin": "Zhōngguóshì xiàndàihuà jì yǒu gèguó xiàndàihuà de gòngtóng tèzhēng, gèng yǒu jīyú zìjǐ guóqíng de xiānmíng Zhōngguó tèsè. Tā shì rénkǒu guīmó jùdà de xiàndàihuà, shì quántǐ rénmín gòngtóng fùyù de xiàndàihuà, shì wùzhì wénmíng hé jīngshén wénmíng xiāng xiétiáo de xiàndàihuà, wèi rénlèi tànsuǒ gèng hǎo shèhuì zhìdù gòngxiàn le Zhōngguó zhìhuì.",
                "en": "Chinese modernization shares universal traits while rooted in national conditions: massive population scale, common prosperity, and harmony between material and cultural progress, contributing wisdom to human institutions.",
                "es": "La modernización china combina rasgos universales y peculiaridades propias: escala demográfica ingente, prosperidad compartida y armonía material y espiritual, enriqueciendo la gobernanza global."
            }
        ]
    },

    # 12 享受
    {
        "id": "12",
        "hanzi": "享受",
        "pinyin": "xiǎng shòu",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to enjoy; to savor; enjoyment; treat; benefit",
            "es": "disfrutar; gozar de; deleitarse; disfrute; goce"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to take pleasure in, savor, or benefit from pleasant conditions, treatment, or sensations",
                "definition_es": "gozar, deleitarse o beneficiarse de condiciones gratas, delicias o derechos",
                "example_phrase": "享受生活 (enjoy life)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "pleasure, gratification, or luxurious satisfaction derived from experience",
                "definition_es": "deleite, fruición, bienestar o placer derivado de una vivencia",
                "example_phrase": "是一种精神享受 (is a spiritual treat)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "周末的午后，他喜欢泡上一壶芬芳的乌龙茶，静静地享受阳光洒满窗台的惬意时光。",
                "pinyin": "Zhōumò de wǔhòu, tā xǐhuan pào shàng yì hú fēnfāng de wūlóngchá, jìngjìng de xiǎngshòu yángguāng sǎmǎn chuāngtái de qièyì shíguāng.",
                "en": "On weekend afternoons, he loves brewing a fragrant pot of Oolong tea, quietly savoring the cozy hours of sunlight bathing the windowsill.",
                "es": "Los fines de semana por la tarde le complace preparar una tetera de aromático té Oolong, disfrutando de la agradable luz sobre el alféizar."
            },
            {
                "id": "#2",
                "hanzi": "聆听这位享誉世界的钢琴大师演奏古典协奏曲，对在场的所有乐迷而言无疑是一场无与伦比的艺术享受。",
                "pinyin": "Língtīng zhè wèi xiǎngyù-shìjiè de gāngqín dàshī yǎnzòu gǔdiǎn xiézòuqǔ, duì zàichǎng de suǒyǒu yuèmí éryán wúyí shì yì chǎng wúyǔlúnbǐ de yìshù xiǎngshòu.",
                "en": "Listening to the world-renowned pianist perform classical concertos was undoubtedly an incomparable artistic treat for all music lovers.",
                "es": "Escuchar al célebre virtuoso interpretar conciertos clásicos al piano constituyó un deleite estético incomparable para todos los melómanos."
            }
        ],
        "collocations": [
            {"hanzi": "享受生活", "en": "enjoy life"},
            {"hanzi": "物质享受", "en": "material comfort/enjoyment"},
            {"hanzi": "精神享受", "en": "spiritual/aesthetic enjoyment"},
            {"hanzi": "享受待遇", "en": "enjoy benefits / receive entitlements"},
            {"hanzi": "享受美食", "en": "savor delicacies"},
            {"hanzi": "尽情享受", "en": "enjoy to the fullest"}
        ],
        "idioms": [
            {"hanzi": "乐在其中", "pinyin": "lè zài qí zhōng", "meaning_en": "find joy in it; derive great pleasure from an activity"},
            {"hanzi": "怡然自得", "pinyin": "yí rán zì dé", "meaning_en": "contented and serene; peaceful self-satisfaction"},
            {"hanzi": "养尊处优", "pinyin": "yǎng zūn chǔ yōu", "meaning_en": "live in luxury and comfort; coddled lifestyle"},
            {"hanzi": "其乐无穷", "pinyin": "qí lè wú qióng", "meaning_en": "boundless joy and endless amusement"}
        ],
        "character_decomposition": [
            {
                "character": "享",
                "pinyin": "xiǎng",
                "meaning_en": "enjoy; benefit; sacrificial banquet",
                "meaning_es": "disfrutar; gozar; banquete de ofrenda",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "高 (lofty ancestral temple roof) + 子 (offspring presenting feast)",
                "sound_component": "享 (xiǎng)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "An ancestral temple lid 亠 where offspring 子 present aromatic sacrificial banquets for spirits to partake; denotes enjoying feast and favor.",
                "visual_mnemonic_story_en": "Under a decorated roof (亠), filial children (子) present fine food to enjoy together (享).",
                "visual_mnemonic_story_es": "Bajo el alero del templo (亠), los vástagos (子) ofrecen un manjar exquisito para disfrutarlo (享).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "YRND",
                "traditional": ""
            },
            {
                "character": "受",
                "pinyin": "shòu",
                "meaning_en": "receive; accept; endure; suffer",
                "meaning_es": "recibir; aceptar; soportar; experimentar",
                "radical": "又",
                "radical_meaning_en": "hand",
                "meaning_component": "爪 (hand from above giving) + 又 (hand from below receiving)",
                "sound_component": "舟 (zhōu, boat / vessel in between)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A hand from above 爪 passing a vessel into an eager hand below 又; denotes receiving, accepting, and experiencing sensations.",
                "visual_mnemonic_story_en": "Two hands pass and receive (受) a generous gift vessel smoothly.",
                "visual_mnemonic_story_es": "Una mano superior entrega y otra inferior acoge (受) una copa con deleite.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BBME",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Feasting on temple delicacies (享) and receiving them gratefully with open hands (受) means to enjoy (享受).",
            "composite_memory_hook_es": "Participar del banquete grato (享) recibiéndolo con ambas manos (受) es disfrutar a fondo (享受).",
            "cultural_and_cognitive_roots": "Derived from classical sacrificial communion (享通: spiritual reception); shifted in modern vernacular to hedonistic or aesthetic pleasures.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by falling fourth tone: 'xiǎng shòu' (214-51). Dip deeply on 'xiǎng', then drop down firmly on 'shòu'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "亨", "pinyin": "hēng", "meaning_en": "prosperous; smooth", "distinction_note": "Lacks the central horizontal stroke of 子 in 享"},
                {"character": "孝", "pinyin": "xiào", "meaning_en": "filial piety", "distinction_note": "Has 老-top atop 子 instead of 亠 and 口"},
                {"character": "爱", "pinyin": "ài", "meaning_en": "love", "distinction_note": "Has friend 友 at bottom instead of 又 in 受"},
                {"character": "妥", "pinyin": "tuǒ", "meaning_en": "proper; settled", "distinction_note": "Has woman 女 at bottom instead of 又"}
            ],
            "etymological_cognates": [
                {"character": "乐", "pinyin": "lè", "gloss_en": "joy; cheerful music"},
                {"character": "悦", "pinyin": "yuè", "gloss_en": "pleased in heart"},
                {"character": "欣", "pinyin": "xīn", "gloss_en": "joyous laughter"},
                {"character": "怡", "pinyin": "yí", "gloss_en": "serene harmony of mind"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "享受 emphasizes deep, comfortable sensory, psychological, or material gratification.",
            "contrasts": [
                {"id": "1", "compared_word": "享受 vs. 贪图", "pinyin": "tāntú", "analysis": "贪图 has a negative connotation of coveting comfort or illicit gain ('贪图安逸', '贪图小便宜'), while 享受 is neutral or positive."},
                {"id": "2", "compared_word": "享受 vs. 忍受", "pinyin": "rěnshòu", "analysis": "忍受 means enduring pain or unpleasant hardship ('忍受痛苦'), the polar emotional opposite of pleasant 享受."},
                {"id": "3", "compared_word": "享受 vs. 欣赏", "pinyin": "xīnshǎng", "analysis": "欣赏 emphasizes intellectual and aesthetic appraisal of art or talent ('欣赏画作', '欣赏才华'), while 享受 is holistic sensory delight."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "忙碌的工作之余，我们要学会放慢脚步，用心去感知生活中的点滴美好。不必追求奢华的物质铺张，清晨的一缕暖阳、窗台的一抹花香、与家人围坐的一顿热饭，都是值得我们细细品味与感念的无上享受。",
                "pinyin": "Mánglù de gōngzuò zhīyú, wǒmen yào xuéhuì fàngmàn jiǎobù, yòngxīn qù gǎnzhī shēnghuó zhōng de diǎndī měihǎo. Búbì zhuīqiú shēhuá de wùzhì pūzhāng, qīngchén de yì lǚ nuǎnyáng, chuāngtái de yì mǒ huāxiāng, yǔ jiārén wéizuò de yí dùn rèfàn, dōu shì zhíde wǒmen xìxì pǐnwèi yǔ gǎnniàn de wúshàng xiǎngshòu.",
                "en": "Amid busy work, we should learn to slow our steps to perceive life's simple joys. Luxuries are unneeded; morning sun, floral scents, and a warm meal with family are supreme delights worthy of savoring.",
                "es": "Entre el ajetreo laboral conviene pausar el paso y saborear la belleza menuda. Sin ostentaciones superfluas, el sol matinal, el aroma de una flor y una cena en familia son un goce inestimable para el alma."
            },
            {
                "id": "#2",
                "hanzi": "现代社会保障体系的建立与健全，让越来越多的劳动者在年老退休后能够切实享受到国家发展带来的民生红利。按时足额发放的养老金与普惠性医疗保障，为千万老年人安享幸福尊严的晚年生活提供了坚实后盾。",
                "pinyin": "Xiàndài shèhuì bǎozhàng tǐxì de jiànlì yǔ jiànquán, ràng yuèláiyuè duō de láodòngzhě zài niánlǎo tuìxiū hòu nénggòu qièshí xiǎngshòudào guójiā fāzhǎn dàilái de mínshēng hónglì. Ànshí zú'é fāfàng de yǎnglǎojīn yǔ pǔhuìxìng yīliáo bǎozhàng, wèi qiānwàn lǎoniánrén ānxiǎng xìngfú zūnyán de wǎnnián shēnghuó tígōng le jiānshí hòudùn.",
                "en": "The modern social safety net ensures retirees enjoy the fruits of national development. Timely pensions and universal healthcare provide firm backing for millions of seniors to enjoy dignified twilight years.",
                "es": "La red de protección social moderna permite a los jubilados gozar de las conquistas del progreso. Pensiones dignas y cobertura médica universal garantizan una vejez plácida y honrosa a millones de ancianos."
            }
        ]
    },

    # 13 用途
    {
        "id": "13",
        "hanzi": "用途",
        "pinyin": "yòng tú",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "use; purpose; practical application; function",
            "es": "uso; utilidad; aplicación práctica; finalidad"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the practical application, utility, or specific purpose for which something is used",
                "definition_es": "aplicación práctica, destino o finalidad a que sirve un objeto o recurso",
                "example_phrase": "用途广泛 (has a wide range of uses)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "竹子在我国南方民间用途极其广泛，不仅可以制作坚韧耐用的家具，还能用来造纸和编织工艺品。",
                "pinyin": "Zhúzi zài wǒguó nánfāng mínjiān yòngtú jíqí guǎngfàn, bùjǐn kěyǐ zhìzuò jiānrèn nàiyòng de jiājù, hái néng yònglái zàozhǐ hé biānzhī gōngyìpǐn.",
                "en": "Bamboo has an exceptionally wide range of uses in southern Chinese folk life, crafting sturdy furniture as well as papermaking and weaving.",
                "es": "El bambú tiene incontables usos en el sur de China: no solo sirve para fabricar muebles robustos, sino también para papel y cestería."
            },
            {
                "id": "#2",
                "hanzi": "财务制度明确严格规定，任何专项扶贫资金都必须专款专用，严禁挪作他用或改变资金用途。",
                "pinyin": "Cáiwù zhìdù míngquè yángé guīdìng, rènhé zhuānxiàng fúpín zījīn dōu bìxū zhuānkuǎn-zhuānyòng, yánjìn nuózuò tāyòng huò gǎibiàn zījīn yòngtú.",
                "en": "Financial regulations strictly stipulate that special poverty-alleviation funds must be ear-marked, barring diversion or altered purposes.",
                "es": "La normativa fiscal estipula que los fondos de ayuda deben destinarse a su fin exclusivo, prohibiendo desviar su uso o aplicación."
            }
        ],
        "collocations": [
            {"hanzi": "用途广泛", "en": "widely used; versatile utility"},
            {"hanzi": "实际用途", "en": "practical use/purpose"},
            {"hanzi": "资金用途", "en": "allocation / use of funds"},
            {"hanzi": "军事用途", "en": "military applications"},
            {"hanzi": "改变用途", "en": "change the purpose/use"},
            {"hanzi": "说明用途", "en": "explain the purpose"}
        ],
        "idioms": [
            {"hanzi": "大材小用", "pinyin": "dà cái xiǎo yòng", "meaning_en": "put fine timber to petty use; waste great talents on menial jobs"},
            {"hanzi": "物尽其用", "pinyin": "wù jìn qí yòng", "meaning_en": "make the best and fullest use of all resources"},
            {"hanzi": "学以致用", "pinyin": "xué yǐ zhì yòng", "meaning_en": "study in order to apply in practice"},
            {"hanzi": "别有用意", "pinyin": "bié yǒu yòng yì", "meaning_en": "have ulterior motives; have special hidden purpose"}
        ],
        "character_decomposition": [
            {
                "character": "用",
                "pinyin": "yòng",
                "meaning_en": "use; employ; apply; utility",
                "meaning_es": "usar; emplear; utilizar; utilidad",
                "radical": "用",
                "radical_meaning_en": "use",
                "meaning_component": "卜 (divination oracle bone) + 中 (centering target hit)",
                "sound_component": "用 (yòng)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of a bronze tripod vessel or divination bone hitting the target 中; signifies effectiveness, application, and using tools.",
                "visual_mnemonic_story_en": "A wooden tool is grabbed firmly by its frame to use (用) it for daily tasks.",
                "visual_mnemonic_story_es": "Un útil resistente se empuña por el bastidor para usarlo (用) en la labor cotidiana.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BQ",
                "traditional": ""
            },
            {
                "character": "途",
                "pinyin": "tú",
                "meaning_en": "way; route; road; path",
                "meaning_es": "camino; ruta; vía; sendero",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walk/movement) + 余 (thatched hut shelter along path)",
                "sound_component": "余 (yú, surplus / phonetic)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Footsteps 辶 traveling along a highway lined with post huts 余; denotes routes, paths, destinations, or avenues of development.",
                "visual_mnemonic_story_en": "Footsteps (辶) follow a well-trodden route past roadside huts (余), marking the path (途).",
                "visual_mnemonic_story_es": "Pasos firmes (辶) transitan la calzada junto a ventas camineras (余) siguiendo la ruta (途).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YOMD",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The path or avenue (途) along which a tool is put to use (用) is its purpose or application (用途).",
            "composite_memory_hook_es": "El camino o vía (途) por donde se aplica un útil (用) define su destino y uso (用途).",
            "cultural_and_cognitive_roots": "Utilitarian philosophy (体用之道: essence and utility); 途 maps out the functional trajectory through which matter serves human needs.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by rising second tone: 'yòng tú' (51-35). Drop sharply on 'yòng', then climb smoothly on 'tú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "甩", "pinyin": "shuǎi", "meaning_en": "fling; swing", "distinction_note": "Tail curves to right at bottom instead of central vertical stroke of 用"},
                {"character": "角", "pinyin": "jiǎo", "meaning_en": "horn; angle", "distinction_note": "Has ⺈ on top of enclosure"},
                {"character": "除", "pinyin": "chú", "meaning_en": "eliminate; divide", "distinction_note": "Has hill radical 阝 on left of 余 instead of 辶 in 途"},
                {"character": "叙", "pinyin": "xù", "meaning_en": "narrate", "distinction_note": "Has 又 on right of 余"}
            ],
            "etymological_cognates": [
                {"character": "功", "pinyin": "gōng", "gloss_en": "merit; functional work"},
                {"character": "效", "pinyin": "xiào", "gloss_en": "efficacy; imitate result"},
                {"character": "路", "pinyin": "lù", "gloss_en": "road; route of journey"},
                {"character": "径", "pinyin": "jìng", "gloss_en": "narrow path; diameter"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "用途 emphasizes the practical objective purpose or utilitarian domain an object is applied to.",
            "contrasts": [
                {"id": "1", "compared_word": "用途 vs. 功能", "pinyin": "gōngnéng", "analysis": "功能 refers to the inherent technical capability or feature of a device ('手机拍照功能'), while 用途 refers to what human purpose it serves in practice ('用途是防盗')."},
                {"id": "2", "compared_word": "用途 vs. 作用", "pinyin": "zuòyòng", "analysis": "作用 focuses on the effect, positive impact, or influence exerted on another object ('起到关键作用'), while 用途 is the intended application."},
                {"id": "3", "compared_word": "用途 vs. 目的", "pinyin": "mùdì", "analysis": "目的 refers to a person's conscious goal or target ('达到目的'), whereas 用途 applies to inanimate tools, funds, or materials."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "石墨烯作为一种颠覆性的新型纳米碳素材料，凭借其超轻薄、超强韧性与卓越的导电导热性能，拥有极其广泛的工业用途。无论是应用于下一代超快充电电池，还是航空航天防热涂层，都展现出巨大的应用前景。",
                "pinyin": "Shímòxī zuòwéi yì zhǒng diānfùxìng de xīnxíng nàmǐ tànsù cáiliào, píngjiè qí chāoqīngbáo, chāoqiáng rènxìng yǔ zhuóyuè de dǎodiàn dǎorè xìngnéng, yǒngyǒu jíqí guǎngfàn de gōngyè yòngtú. Wúlùn shì yìngyòng yú xià yí dài chāokuài chōngdiàn diànchí, háishì hángkōng-hángtiān fángrè túcéng, dōu zhǎnxiàn chū jùdà de yìngyòng qiánjǐng.",
                "en": "As a disruptive nanomaterial, graphene possesses wide industrial uses due to ultra-thinness, strength, and conductivity. From fast-charging batteries to aerospace coatings, it shows immense application prospects.",
                "es": "Como nanomaterial disruptivo, el grafeno ofrece incontables aplicaciones por su ligereza, dureza y conductividad. Desde baterías ultrarrápidas hasta revestimientos aeroespaciales, promete una revolución técnica."
            },
            {
                "id": "#2",
                "hanzi": "科研人员在野外考察时发现了一种具有特殊荧光特性的深海植物。经过实验室深入分析，专家们不仅证实了其作为生物传感器的新奇用途，更为开发无毒无害的新型医学造影试剂开辟了一条富有前景的创新技术路径。",
                "pinyin": "Kēyán rényuán zài yěwài kǎochá shí fāxiàn le yì zhǒng jùyǒu tèshū yíngguāng tèxìng de shēnhǎi zhíwù. Jīngguò shíyànshì shēnrù fēnxī, zhuānjiāmen bùjǐn zhèngshí le qí zuòwéi shēngwù chuángǎnqì de xīnqí yòngtú, gèng wèi kāifā wúdú-wúhài de xīnxíng yīxué zàoyǐng shìjì kāipì le yì tiáo fùyǒu qiánjǐng de chuàngxīn jìshù lùjìng.",
                "en": "Researchers on field surveys discovered a deep-sea plant with fluorescent properties. Laboratory analysis confirmed its novel use as a biosensor, opening paths to develop non-toxic medical imaging agents.",
                "es": "Exploradores hallaron una planta abisal de fluorescencia singular. Análisis de laboratorio demostraron su insólito uso como biosensor, abriendo una prometedora vía para agentes de contraste médico inocuos."
            }
        ]
    },

    # 14 实验
    {
        "id": "14",
        "hanzi": "实验",
        "pinyin": "shí yàn",
        "part_of_speech": "Noun / Verb",
        "meanings_summary": {
            "en": "experiment; scientific test; to experiment; to test",
            "es": "experimento; ensayo científico; experimentar; probar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a controlled scientific test or trial conducted in a laboratory to prove hypotheses or uncover natural laws",
                "definition_es": "operación científica controlada realizada en laboratorio para comprobar hipótesis o descubrir leyes",
                "example_phrase": "物理实验 (physics experiment)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to conduct controlled experiments in order to test theories or explore phenomena",
                "definition_es": "realizar ensayos o pruebas sistemáticas para contrastar un principio",
                "example_phrase": "在实验室反复实验 (experiment repeatedly in lab)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "化学老师在通风橱前为全班同学演示了浓硫酸与铜片在加热条件下发生反应的对比实验。",
                "pinyin": "Huàxué lǎoshī zài tōngfēngchú qián wèi quánbān tóngxué yǎnshì le nóngliúsuān yǔ tóngpiàn zài jiārè tiáojiàn xià fāshēng fǎnyìng de duìbǐ shíyàn.",
                "en": "The chemistry teacher demonstrated a comparative experiment under the fume hood showing reactions between concentrated sulfuric acid and copper under heat.",
                "es": "El profesor de química realizó ante los alumnos una prueba comparativa en la campana extractora con ácido sulfúrico concentrado y cobre al calor."
            },
            {
                "id": "#2",
                "hanzi": "科研攻关团队经过上万次失败的实验摸索，终于成功合成了具有超导性能的全新结晶化合物。",
                "pinyin": "Kēyán gōngguān tuánduì jīngguò shàngwàn cì shībài de shíyàn mōsuǒ, zhōngyú chénggōng héchéng le jùyǒu chāodǎo xìngnéng de quánxīn jiéjīng huàhéwù.",
                "en": "After exploring through tens of thousands of failed experiments, the research team finally synthesized a new crystalline compound with superconducting properties.",
                "es": "Tras tantear en decenas de miles de experimentos fallidos, el equipo de investigación sintetizó con éxito un compuesto superconductor inédito."
            }
        ],
        "collocations": [
            {"hanzi": "实验室", "en": "laboratory / research lab"},
            {"hanzi": "做实验", "en": "conduct/run an experiment"},
            {"hanzi": "科学实验", "en": "scientific experiment"},
            {"hanzi": "对比实验", "en": "comparative/control experiment"},
            {"hanzi": "实验结果", "en": "experimental results"},
            {"hanzi": "实验数据", "en": "experimental data"}
        ],
        "idioms": [
            {"hanzi": "真凭实据", "pinyin": "zhēn píng shí jù", "meaning_en": "ironclad, irrefutable evidence and solid facts"},
            {"hanzi": "按图索骥", "pinyin": "àn tú suǒ jì", "meaning_en": "seek a thoroughbred according to picture; follow instructions mechanically"},
            {"hanzi": "实事求是", "pinyin": "shí shì qiú shì", "meaning_en": "seek truth from facts; be practical and realistic"},
            {"hanzi": "身体力行", "pinyin": "shēn tǐ lì xíng", "meaning_en": "practice personally what one preaches"}
        ],
        "character_decomposition": [
            {
                "character": "实",
                "pinyin": "shí",
                "meaning_en": "solid; real; true; fruit; honest",
                "meaning_es": "sólido; real; verdadero; fruto; lleno",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (house roof) + 头/贯 (strings of cowrie currency filling home)",
                "sound_component": "实 (shí)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A house 宀 fully packed with stringed cowrie riches 贯; signifies substance, reality, truth, and solid fulfillment.",
                "visual_mnemonic_story_en": "A house (宀) packed solid with real treasures embodies truth and reality (实).",
                "visual_mnemonic_story_es": "Una casa (宀) colmada de riquezas tangibles personifica lo sólido y veraz (实).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "JND",
                "traditional": "實"
            },
            {
                "character": "验",
                "pinyin": "yàn",
                "meaning_en": "examine; check; verify; test",
                "meaning_es": "examinar; comprobar; verificar; eficaz",
                "radical": "马",
                "radical_meaning_en": "horse",
                "meaning_component": "马 (horse inspected for pedigree) + 佥 (all together / assembled)",
                "sound_component": "佥 (qiān, all / phonetic carrier)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Horse radical 马 paired with 佥 (assembled traits); thoroughly inspecting an equine to verify health, age, and pedigree.",
                "visual_mnemonic_story_en": "A breeder examines a horse (马) thoroughly to verify (验) its authentic pedigree.",
                "visual_mnemonic_story_es": "Un perito examina al corcel (马) de pies a cabeza para verificar (验) su brío y salud.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NMSOI",
                "traditional": "驗"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Using solid tangible physical facts (实) to verify hypotheses (验) defines a laboratory experiment (实验).",
            "composite_memory_hook_es": "Usar hechos tangibles y sólidos (实) para verificar principios (验) define el experimento científico (实验).",
            "cultural_and_cognitive_roots": "Scientific epistemology (实事求是); imported modernly as the standard translation for empirical experimental science (empiricism).",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by falling fourth tone: 'shí yàn' (35-51). Rise smoothly on 'shí', then drop down sharply and decisively on 'yàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "买", "pinyin": "mǎi", "meaning_en": "buy; purchase", "distinction_note": "Has 头 underneath 乛 instead of 宀 in 实"},
                {"character": "卖", "pinyin": "mài", "meaning_en": "sell", "distinction_note": "Has 十 on top of 头"},
                {"character": "脸", "pinyin": "liǎn", "meaning_en": "face", "distinction_note": "Has flesh radical 月 on left of 佥 instead of horse 马 in 验"},
                {"character": "险", "pinyin": "xiǎn", "meaning_en": "danger", "distinction_note": "Has hill radical 阝 on left"}
            ],
            "etymological_cognates": [
                {"character": "测", "pinyin": "cè", "gloss_en": "measure water depth; gauge"},
                {"character": "试", "pinyin": "shì", "gloss_en": "test against model template"},
                {"character": "证", "pinyin": "zhèng", "gloss_en": "prove with words; testify"},
                {"character": "查", "pinyin": "chá", "gloss_en": "inspect trees; investigate"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "实验 highlights controlled laboratory testing to uncover natural laws or verify scientific hypotheses.",
            "contrasts": [
                {"id": "1", "compared_word": "实验 vs. 试验", "pinyin": "shìyàn", "analysis": "实验 emphasizes rigorous laboratory verification of scientific natural laws ('物理实验'), while 试验 refers to practical field trials of prototypes or seed crops ('田间试验')."},
                {"id": "2", "compared_word": "实验 vs. 实践", "pinyin": "shíjiàn", "analysis": "实践 denotes broad philosophical human social activity and real-world implementation, while 实验 is a specialized scientific method."},
                {"id": "3", "compared_word": "实验 vs. 化验", "pinyin": "huàyàn", "analysis": "化验 specifically denotes laboratory chemical analysis of blood, urine, or soil samples ('抽血化验'), a subset of scientific tests."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在空间站微重力环境下，中国航天员顺利完成了多项具有国际前沿水准的空间生命科学实验。研究人员通过实时下传的高清实验数据，细致观测植物根系与哺乳动物骨细胞在太空微重力状态下的发育演化规律。",
                "pinyin": "Zài kōngjiānzhàn wēizhònglì huánjìng xià, Zhōngguó hángtiānyuán shùnlì wánchéng le duō xiàng jùyǒu guójì qiányán shuǐzhǔn de kōngjiān shēngmìng kēxué shíyàn. Yánjiū rényuán tōngguò shíshí xiàchuán de gāoqīng shíyàn shùjù, xìzhì guāncè zhíwù gēnxì yǔ shǔlèi dòngwù gǔxìbāo zài tàikōng wēizhònglì zhuàngtài xià de fāyù yǎnhuà guīlǜ.",
                "en": "In space station microgravity, Chinese astronauts completed frontier life science experiments. Researchers used real-time high-definition data to observe plant roots and bone cell development in space.",
                "es": "En microgravedad en la estación espacial, los astronautas chinos culminaron experimentos punteros de biología cósmica. Con datos en tiempo real observaron raíces y células óseas bajo ingravidez."
            },
            {
                "id": "#2",
                "hanzi": "现代医学的每一次巨大进步，都深深植根于严谨科学的临床对照实验。从新型抗癌靶向药物的分阶段人体试验，到大数据双盲对照评估，唯有经过确凿真实的实验证据检验，创新疗法才能获准走向临床挽救生命。",
                "pinyin": "Xiàndài yīxué de měi yí cì jùdà jìnbù, dōu shēnsēn zhígēn yú yánjǐn kēxué de línchuáng duìbǐ shíyàn. Cóng xīnxíng kàng'ái bǎxiàng yàowù de fēnjiēduàn réntǐ shìyàn, dào dàshùjù shuāngmáng duìbǐ pínggū, wéiyǒu jīngguò quèzáo zhēnshí de shíyàn zhèngjù jiǎnyàn, chuàngxīn liáofǎ cáinéng huòzhǔn zǒuxiàng línchuáng wǎnjiù shēngmìng.",
                "en": "Every progress in modern medicine is rooted in rigorous controlled clinical experiments. From phased trials of targeted drugs to double-blind assessments, only verified therapies reach clinics to save lives.",
                "es": "Los avances de la medicina moderna descansan en rigurosos ensayos clínicos de control. Desde pruebas farmacológicas hasta análisis a doble ciego, solo la evidencia experimental fidedigna avala tratamientos que salvan vidas."
            }
        ]
    },

    # 15 铃
    {
        "id": "15",
        "hanzi": "铃",
        "pinyin": "líng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "bell; chime; ring; buzzer",
            "es": "campana; campanilla; timbre; cascabel"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a hollow metallic acoustic device with a clapper that rings when struck, or an electrical buzzer",
                "definition_es": "dispositivo acústico metálico hueco con badajo que tintinea al agitarse, o timbre eléctrico",
                "example_phrase": "按门铃 (press the doorbell)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清脆悦耳的下课铃声刚刚响起，安静的教学楼走廊里瞬间充满了欢声笑语。",
                "pinyin": "Qīngcuì yuè'ěr de xiàkè língshēng gānggāng xiǎngqǐ, ānjìng de jiàoxuélóu zǒuláng lǐ shùnjiān chōngmǎn le huānshēng-xiàoyǔ.",
                "en": "Just as the crisp, melodious end-of-class bell rang, quiet hallways erupted into cheers and laughter in an instant.",
                "es": "Apenas sonó el timbre alegre de fin de clase, los silenciosos pasillos se llenaron al instante de risas y algarabía."
            },
            {
                "id": "#2",
                "hanzi": "小猫咪的脖子上系着一枚精致小巧的金色小铜铃，走起路来发出叮叮当当的声响。",
                "pinyin": "Xiǎomāomī de bózi shàng jì zhe yì méi jīngzhì xiǎoqiǎo de jīnsè xiǎotónglíng, zǒu qǐ lù lai fāchū dīngdīng-dāngdāng de shēngxiǎng.",
                "en": "The kitten had an exquisite golden brass bell tied to its neck, making tinkling sounds as it trotted along.",
                "es": "El gatito llevaba atado al cuello un primoroso cascabel de latón dorado que tintineaba con gracia a cada paso."
            }
        ],
        "collocations": [
            {"hanzi": "门铃", "en": "doorbell"},
            {"hanzi": "铃声", "en": "ringtone; bell chime"},
            {"hanzi": "闹铃", "en": "alarm chime"},
            {"hanzi": "车铃", "en": "bicycle bell"},
            {"hanzi": "铜铃", "en": "bronze bell"},
            {"hanzi": "摇铃", "en": "handbell / ring bell"}
        ],
        "idioms": [
            {"hanzi": "掩耳盗铃", "pinyin": "yǎn ěr dào líng", "meaning_en": "cover one's ears while stealing a bell; deceive oneself"},
            {"hanzi": "解铃系铃", "pinyin": "jiě líng xì líng", "meaning_en": "whoever tied the bell must untie it; solve what one caused"},
            {"hanzi": "顺手牵羊", "pinyin": "shùn shǒu qiān yáng", "meaning_en": "lead away sheep in passing; steal opportunistically"},
            {"hanzi": "铜铃大眼", "pinyin": "tóng líng dà yǎn", "meaning_en": "eyes as wide and round as bronze bells"}
        ],
        "character_decomposition": [
            {
                "character": "铃",
                "pinyin": "líng",
                "meaning_en": "bell; chime; ring; small rattle",
                "meaning_es": "campana; timbre; cascabel; campanilla",
                "radical": "钅",
                "radical_meaning_en": "metal / gold",
                "meaning_component": "钅 (cast bronze/brass metal) + 令 (order / command)",
                "sound_component": "令 (lìng, command / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Metal radical 钅 paired with 令 (issuing commands); small cast bronze bells rung by heralds to assemble people for public orders.",
                "visual_mnemonic_story_en": "A small bell of metal (钅) rings to issue authoritative commands (令) to listeners (铃).",
                "visual_mnemonic_story_es": "Una campanilla de metal (钅) tañe para promulgar bandos y órdenes (令) a la vecindad (铃).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "COEI",
                "traditional": "鈴"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A metal object (钅) that rings to command attention (令) is a bell (铃).",
            "composite_memory_hook_es": "Una pieza metálica (钅) que tañe dando la voz de orden (令) es el timbre o cascabel (铃).",
            "cultural_and_cognitive_roots": "Bronze bell culture; ancient carriages had chariot bells (銮铃) to announce imperial convoys, transforming into modern school bells and electronic ringtones.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone: 'líng' (35). Sweep upward cleanly from pitch 3 to high pitch 5 like a crisp bell chime."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "领", "pinyin": "lǐng", "meaning_en": "collar; lead", "distinction_note": "Has page/head radical 页 on right of 令 instead of 钅 in 铃"},
                {"character": "冷", "pinyin": "lěng", "meaning_en": "cold", "distinction_note": "Has ice radical 冫 on left of 令"},
                {"character": "钟", "pinyin": "zhōng", "meaning_en": "clock; large bell", "distinction_note": "Has 中 on right of 钅 instead of 令"},
                {"character": "钢", "pinyin": "gāng", "meaning_en": "steel", "distinction_note": "Has 冈 on right of 钅"}
            ],
            "etymological_cognates": [
                {"character": "铎", "pinyin": "duó", "gloss_en": "large handbell with wooden clapper"},
                {"character": "磬", "pinyin": "qìng", "gloss_en": "sonorous chime stone"},
                {"character": "钲", "pinyin": "zhēng", "gloss_en": "army gong used to halt soldiers"},
                {"character": "叮", "pinyin": "dīng", "gloss_en": "tinkling metallic sound"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "铃 designates small acoustic bells, chimes, or electronic buzzers, distinct from colossal temple bells.",
            "contrasts": [
                {"id": "1", "compared_word": "铃 vs. 钟", "pinyin": "zhōng", "analysis": "钟 refers to large hanging bronze bells or timepiece clocks, while 铃 refers to small handheld bells, door buzzers, or bicycle bells."},
                {"id": "2", "compared_word": "铃 vs. 锣", "pinyin": "luó", "analysis": "锣 is a flat bronze gong struck with a mallet, producing a flat resonant clash rather than tinkling 铃."},
                {"id": "3", "compared_word": "铃 vs. 哨", "pinyin": "shào", "analysis": "哨 is a blown whistle producing high-pitched acoustic air vibrations, not struck metal."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫步在风光旖旎的江南水乡古镇，微风吹拂屋檐，悬挂在古刹飞檐四角的铜质风铃随风摇曳，发出一阵阵空灵悠扬的叮当铃声。那纯净清脆的回响洗涤着旅人的浮躁尘心，令人仿佛置身于物我两忘的世外桃源。",
                "pinyin": "Mànbù zài fēngguāng-yǐnǐ de Jiāngnán shuǐxiāng gǔzhèn, wēifēng chuīfú wūyán, xuánguà zài gǔchà fēiyán sì jiǎo de tóngzhì fēnglíng suífēng yáoyè, fāchū yízhènzhèn kōnglíng yōuyáng de dīngdāng língshēng. Nà chúnjìng qīngcuì de huíxiǎng xǐdí zhe lǚrén de fúzào chénxīn, lìngrén fǎngfú zhìshēn yú wù-wǒ-liǎngwàng de shìwàitáoyuán.",
                "en": "Strolling through an ancient southern wetland town, breezes caress eaves where brass wind chimes sway, chiming melodiously. That crisp echo washes away travelers' restless thoughts, transporting minds into tranquil seclusion.",
                "es": "Paseando por una villa fluvial del sur, la brisa mece los carillones de bronce colgados de los aleros del templo, emitiendo un tintineo místico que sosiega el espíritu del caminante en un remanso de paz."
            },
            {
                "id": "#2",
                "hanzi": "古代成语“掩耳盗铃”生动讽刺了自欺欺人的愚蠢行为。春秋时期有人偷盗大钟，因钟体太重难以搬运便妄图用锤子敲碎，又害怕发出响亮铃声被他人发觉，竟自作聪明地用棉花捂住自己的耳朵，最终落得人赃俱获的下场。",
                "pinyin": "Gǔdài chéngyǔ 'yǎn'ěr-dàolíng' shēngdòng fěngcì le zìqī-qīrén de yúchǔn xíngwéi. Chūnqiū shíqī yǒurén tōudào dàzhōng, yīn zhōngtǐ tài zhòng nányǐ bānyùn biàn wàngtú yòng chuízi qiāosuì, yòu hàipà fāchū xiǎngliàng língshēng bèi tārén fājué, jìng zìzuò-cōngmíng de yòng miánhuā wǔzhù zìjǐ de ěrduo, zuìzhōng luòdé rénzāng-jùhuò de xiàchǎng.",
                "en": "The idiom 'cover one's ears to steal a bell' mocks self-deceit. A thief broke a bell with a hammer, but fearing its ring, stuffed his own ears with cotton, getting caught red-handed in foolish delusion.",
                "es": "La locución 'taparse los oídos para robar el cascabel' censura el autoengaño necio. Un ladrón quiso quebrar una campana para llevarse el bronce; temiendo el tañido se tapó los oídos cayendo preso en flagrante ridículo."
            }
        ]
    },

    # 16 所
    {
        "id": "16",
        "hanzi": "所",
        "pinyin": "suǒ",
        "part_of_speech": "Particle / Measure Word / Noun",
        "meanings_summary": {
            "en": "structural particle (that which / receiver of action); measure word for buildings; place",
            "es": "partícula estructural (lo que / aquello que); clasificador de edificios; lugar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Particle",
                "register": "Standard",
                "definition_en": "particle placed before a transitive verb to form a nominal phrase representing the object or receiver of the action",
                "definition_es": "partícula antepuesta al verbo que nominaliza la acción señalando al objeto paciente ('lo que')",
                "example_phrase": "所见所闻 / 他所说的 (what is seen and heard / what he said)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Measure Word",
                "register": "Standard",
                "definition_en": "measure word used for houses, schools, hospitals, and institutional establishments",
                "definition_es": "clasificador numeral empleado para escuelas, hospitales, institutos o edificios",
                "example_phrase": "一所大学 / 一所医院 (a university / a hospital)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "正如古人所说，“读万卷书，行万里路”，唯有将理论求知与社会实践紧密结合，才能增长才干。",
                "pinyin": "Zhèngrú gǔrén suǒ shuō, 'dú wànjuǎn shū, xíng wànlǐ lù', wéiyǒu jiāng lǐlùn qiúzhī yǔ shèhuì shíjiàn jǐnmì jiéhé, cáinéng zēngzhǎng cáigàn.",
                "en": "Just as the ancients said, 'read ten thousand books and travel ten thousand miles'; only by linking theory with practice can ability flourish.",
                "es": "Tal como decían los antiguos: 'leer diez mil tomos y recorrer diez mil leguas'; solo aunando teoría y práctica crece el talento."
            },
            {
                "id": "#2",
                "hanzi": "经过多年的持续建设，这所位于西北偏远山区的小学拥有了明亮宽敞的多媒体网络教室。",
                "pinyin": "Jīngguò duōnián de chíxù jiànshè, zhè suǒ wèiyú xīběi piānyuǎn shānqū de xiǎoxué yǒngyǒu le míngliàng kuānchǎng de duōméitǐ wǎngluò jiàoshì.",
                "en": "Through years of sustained construction, this primary school located in remote northwestern mountains gained bright, multimedia classrooms.",
                "es": "Tras años de mejoras sostenidas, esta escuela de la serranía noroccidental cuenta ya con aulas multimedia luminosas y conectadas."
            }
        ],
        "collocations": [
            {"hanzi": "一所学校", "en": "a school"},
            {"hanzi": "一所医院", "en": "a hospital"},
            {"hanzi": "所见所闻", "en": "what one sees and hears"},
            {"hanzi": "所谓", "en": "so-called; what is meant by"},
            {"hanzi": "所有人", "en": "everyone; owner"},
            {"hanzi": "无所畏惧", "en": "fearless; afraid of nothing"}
        ],
        "idioms": [
            {"hanzi": "各得其所", "pinyin": "gè dé qí suǒ", "meaning_en": "each is in their proper place; everyone is well-accommodated"},
            {"hanzi": "无所适从", "pinyin": "wú suǒ shì cóng", "meaning_en": "at a loss what to follow; not knowing which way to turn"},
            {"hanzi": "无所作为", "pinyin": "wú suǒ zuò wéi", "meaning_en": "accomplish nothing; passive and ineffective"},
            {"hanzi": "无所不能", "pinyin": "wú suǒ bù néng", "meaning_en": "omnipotent; capable of doing anything"}
        ],
        "character_decomposition": [
            {
                "character": "所",
                "pinyin": "suǒ",
                "meaning_en": "place; that which; structural particle; classifier for houses",
                "meaning_es": "lugar; lo que; partícula estructural; clasificador de edificios",
                "radical": "户",
                "radical_meaning_en": "door",
                "meaning_component": "户 (single-leaf doorway / household) + 斤 (carpenter axe)",
                "sound_component": "斤 (jīn, axe / sound of chopping)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A carpenter's axe 斤 hewing wood beside a doorway 户 to clear building timber; originally sound of chopping wood, generalized to a building site or place.",
                "visual_mnemonic_story_en": "An axe (斤) shapes building timber beside a wooden door (户) to build an establishment (所).",
                "visual_mnemonic_story_es": "Un hacha (斤) desbasta maderos junto a la puerta (户) para alzar un edificio (所).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "HSHML",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An axe (斤) at the door (户) establishes a physical place, or tags 'that which' (suǒ, 所).",
            "composite_memory_hook_es": "El hacha (斤) ante la puerta (户) levanta un recinto y marca 'aquello que' (suǒ, 所).",
            "cultural_and_cognitive_roots": "Classical Chinese grammatical marker (所字结构): prefixing 所 to transitive verbs nominalizes action, creating literary relative clauses ('所学', '所作').",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'suǒ' (214). Dip down to pitch 2 then rise lightly to 4."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "斤", "pinyin": "jīn", "meaning_en": "half kilogram; axe", "distinction_note": "Single character lacking door radical 户 on left of 所"},
                {"character": "斥", "pinyin": "chì", "meaning_en": "reproach; scold", "distinction_note": "Has extra dot at upper right of 斤"},
                {"character": "房", "pinyin": "fáng", "meaning_en": "room; house", "distinction_note": "Has 方 underneath 户 instead of 斤 in 所"},
                {"character": "启", "pinyin": "qǐ", "meaning_en": "open; start", "distinction_note": "Has 口 underneath 户"}
            ],
            "etymological_cognates": [
                {"character": "处", "pinyin": "chù", "gloss_en": "place; location"},
                {"character": "地", "pinyin": "dì", "gloss_en": "earth; ground territory"},
                {"character": "方", "pinyin": "fāng", "gloss_en": "square; direction; place"},
                {"character": "居", "pinyin": "jū", "gloss_en": "dwell; reside under roof"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "所 functions syntactically as a nominalizing verbal prefix ('所+V') or classifier for institutions.",
            "contrasts": [
                {"id": "1", "compared_word": "所 vs. 处", "pinyin": "chù", "analysis": "处 is primarily a noun designating a physical geographic spot or administrative bureau ('到处', '教务处'), while 所 has rich grammatical nominalizing particle roles."},
                {"id": "2", "compared_word": "所 vs. 家", "pinyin": "jiā", "analysis": "家 is the classifier for commercial companies, restaurants, and shops ('一家公司'), while 所 counts schools and hospitals ('一所学校')."},
                {"id": "3", "compared_word": "所 vs. 个", "pinyin": "gè", "analysis": "个 is a generic classifier, while 所 conveys institutional formality when counting establishments."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代先哲老子在《道德经》中曾深刻指出，“知人者智，自知者明。胜人者有力，自胜者强。”先贤所阐发的辩证哲理历经数千年历史淘洗，依然在今天闪耀着穿越时空的智慧光芒，指引着人们修身克己。",
                "pinyin": "Zhōngguó gǔdài xiānzhé Lǎozǐ zài Dàodéjīng zhōng céng shēnkè zhǐchū, 'zhīrén zhě zhì, zìzhī zhě míng. Shèngrén zhě yǒulì, zìshèng zhě qiáng.' Xiānxián suǒ chǎnfā de biànzhèng zhélǐ lìjīng shùqiān nián lìshǐ táoxǐ, yīrán zài jīntiān shǎnyào zhe chuānyuè shíkōng de zhìhuì guāngmáng, zhǐyǐn zhe rénmen xiūshēn-kèjǐ.",
                "en": "In the Tao Te Ching, Laozi observed that knowing others is intelligence, while self-knowledge is true enlightenment. The dialectical wisdom expounded by sages shines timelessly across millennia, guiding self-cultivation.",
                "es": "Lao Tse afirmó en el Tao Te King que conocer a los demás es sabiduría, mas conocerse a sí mismo es iluminación. Aquello que dilucidaron los antiguos sabios alumbra la conciencia moral con fulgor eterno."
            },
            {
                "id": "#2",
                "hanzi": "百年大计，教育为本。近十年来，国家财政性教育经费持续向农村中西部倾斜，新建改建了数以万计标准化乡村中小学校。在这每一所现代化的校园里，偏远山区的孩子们都能通过宽带互联网共享全国名校的优质名师网络课程。",
                "pinyin": "Bǎinián dàjì, jiàoyù wéiběn. Jìn shí nián lái, guójiā cáizhèngxìng jiàoyù jīngfèi chíxù xiàng nóngcūn qīngxié, xīnjiàn gǎijiàn le shùyǐwànjì biāozhǔnhuà xiāngcūn zhōng-xiǎoxué. Zài zhè měi yì suǒ xiàndàihuà de xiàoyuán lǐ, piānyuǎn shānqū de háizimen dōunéng tōngguò kuāndài hùliánwǎng gòngxiǎng quánguó míngxiào de yōuzhì míngshī wǎngluò kèchéng.",
                "en": "Education is foundational to a nation's destiny. Over the past decade, public funding built tens of thousands of rural schools. In each modernized school, rural children access courses from top teachers via internet.",
                "es": "La enseñanza es cimiento de la nación. La inversión pública ha levantado decenas de miles de escuelas rurales en el interior. En cada una de estas escuelas los escolares acceden a lecciones magistrales por red."
            }
        ]
    },

    # 17 状态
    {
        "id": "17",
        "hanzi": "状态",
        "pinyin": "zhuàng tài",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "state; condition; status; situation",
            "es": "estado; condición; situación; disposición"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the current physical, mental, biological, or operational mode and condition of a person or system",
                "definition_es": "modo de estar físico, anímico, biológico u operativo en que se halla una persona, sistema o materia",
                "example_phrase": "处于良好状态 (be in good condition)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "大赛开始前，教练通过科学的心理疏导帮助运动员迅速调整到了最佳竞技状态。",
                "pinyin": "Dàsài kāishǐ qián, jiàoliàn tōngguò kēxué de xīnlǐ shūdǎo bāngzhù yùndòngyuán xùnsù tiáozhěng dào le zuìjiā jìngjì zhuàngtài.",
                "en": "Before the tournament began, the coach helped athletes adjust rapidly into peak competitive condition through psychological counseling.",
                "es": "Antes del certamen, el entrenador ayudó a los atletas a alcanzar su estado competitivo óptimo mediante asesoramiento psicológico."
            },
            {
                "id": "#2",
                "hanzi": "经过长途连续飞行，飞机发动机各项监测参数均显示正常，整机处于完全适航状态。",
                "pinyin": "Jīngguò chángtú liánxù fēixíng, fēijī fādòngjī gèxiàng jiāncè cānshù jūn xiǎnshì zhèngcháng, zhěngjī chǔyú wánquán shìháng zhuàngtài.",
                "en": "After long-distance continuous flight, all aircraft engine monitoring parameters read normal, the plane remaining in airworthy condition.",
                "es": "Tras un vuelo prolongado sin escalas, los parámetros de las turbinas marcaron normalidad hallándose el aparato en perfecto estado de vuelo."
            }
        ],
        "collocations": [
            {"hanzi": "心理状态", "en": "psychological state / mindset"},
            {"hanzi": "精神状态", "en": "mental state; spiritual vigor"},
            {"hanzi": "处于状态", "en": "in a state of"},
            {"hanzi": "调整状态", "en": "adjust one's state/mindset"},
            {"hanzi": "工作状态", "en": "working state / operational mode"},
            {"hanzi": "最佳状态", "en": "peak condition / best state"}
        ],
        "idioms": [
            {"hanzi": "渐入佳境", "pinyin": "jiàn rù jiā jìng", "meaning_en": "gradually enter a pleasant condition; steadily improve"},
            {"hanzi": "浑然一体", "pinyin": "hún rán yì tǐ", "meaning_en": "integrated into an organic whole; seamless harmony"},
            {"hanzi": "如入梦境", "pinyin": "rú rù mèng jìng", "meaning_en": "as if entering a dreamland; entranced state"},
            {"hanzi": "安之若素", "pinyin": "ān zhī ruò sù", "meaning_en": "bear hardships with tranquil composure as if habitual"}
        ],
        "character_decomposition": [
            {
                "character": "状",
                "pinyin": "zhuàng",
                "meaning_en": "form; shape; state; certificate; describe",
                "meaning_es": "forma; aspecto; estado; acta; describir",
                "radical": "犬",
                "radical_meaning_en": "dog",
                "meaning_component": "丬 (wooden bed split) + 犬 (hound dog form)",
                "sound_component": "状 (zhuàng)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hound dog 犬 lying against a split wooden bed board 丬; picturing the posture, visible outline, or condition of creatures.",
                "visual_mnemonic_story_en": "A dog (犬) rests beside a bed plank (丬), showing its physical form and posture (状).",
                "visual_mnemonic_story_es": "Un lebrel (犬) reposa junto a un tablón de lecho (丬) mostrando su aspecto y postura (状).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LMID",
                "traditional": ""
            },
            {
                "character": "态",
                "pinyin": "tài",
                "meaning_en": "manner; appearance; voice; posture; state",
                "meaning_es": "ademán; porte; actitud; postura; estado",
                "radical": "心",
                "radical_meaning_en": "heart / mind",
                "meaning_component": "太 (grand / excessive) + 心 (heart/mind posture)",
                "sound_component": "太 (tài, great / phonetic)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Grand appearance 太 guided by internal mental dispositions of the heart 心; denotes external demeanor, attitude, or physical phase.",
                "visual_mnemonic_story_en": "A grand demeanor (太) guided by feelings inside the heart (心) shapes posture (态).",
                "visual_mnemonic_story_es": "Un porte altivo (太) regido por los impulsos del corazón (心) define la actitud y estado (态).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "KIP",
                "traditional": "態"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Physical posture (状) combined with internal mental disposition (态) establishes a comprehensive state (状态).",
            "composite_memory_hook_es": "La postura exterior (状) combinada con la disposición interna (态) configura el estado (状态).",
            "cultural_and_cognitive_roots": "Physics, psychology, and cybernetics calque: 状 (visible morphological configuration) paired with 态 (internal phase/state of matter: 固态, 液态, 气态).",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'zhuàng tài' (51-51). Descend sharply on 'zhuàng', then strike down firmly on 'tài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "壮", "pinyin": "zhuàng", "meaning_en": "strong; robust", "distinction_note": "Has 士 on right instead of hound dog 犬 in 状"},
                {"character": "伏", "pinyin": "fú", "meaning_en": "prostrate; bend down", "distinction_note": "Has person radical 亻 on left of 犬"},
                {"character": "怂", "pinyin": "sǒng", "meaning_en": "timid; instigate", "distinction_note": "Has 从 atop 心 instead of 太 in 态"},
                {"character": "思", "pinyin": "sī", "meaning_en": "think; ponder", "distinction_note": "Has field 田 atop 心"}
            ],
            "etymological_cognates": [
                {"character": "形", "pinyin": "xíng", "gloss_en": "shape; physical form"},
                {"character": "况", "pinyin": "kuàng", "gloss_en": "condition; compare water"},
                {"character": "势", "pinyin": "shì", "gloss_en": "momentum; physical force"},
                {"character": "相", "pinyin": "xiàng", "gloss_en": "appearance; posture"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "状态 designates the immediate operational mode, health condition, or psychological state of a person, machine, or matter.",
            "contrasts": [
                {"id": "1", "compared_word": "状态 vs. 情况", "pinyin": "qíngkuàng", "analysis": "情况 refers to external situational facts, circumstances, and developments ('了解具体情况'), while 状态 refers to the internal condition or functioning mode of a subject ('身体状态')."},
                {"id": "2", "compared_word": "状态 vs. 态度", "pinyin": "tàidù", "analysis": "态度 denotes subjective human attitude, stance, or behavioral disposition toward others ('工作态度认真'), while 状态 is objective condition."},
                {"id": "3", "compared_word": "状态 vs. 形式", "pinyin": "xíngshì", "analysis": "形式 refers to external aesthetic structure, genre, or format ('表现形式'), whereas 状态 is operational condition."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代高压职场环境中，保持良好的心理健康状态是战胜困难与实现自我突破的关键。当感到焦虑烦躁时，主动停下手中繁重的事务做深呼吸，适度散步放空大脑，有助于迅速摆脱精神内耗，重回专注高效的工作状态。",
                "pinyin": "Zài xiàndài gāoyā zhíchǎng huánjìng xià, bǎochí liánghǎo de xīnlǐ jiànkāng zhuàngtài shì zhànshèng kùnnán yǔ shíxiàn zìwǒ tūpò de guānjiàn. Dāng gǎndào jiāolǜ fánzào shí, zhǔdòng tíngxià shǒuzhōng fánzhòng de shìwù zuò shēnhūxī, shìdù sànbù fàngkōng dànǎo, yǒuzhùyú xùnsù bǎituō jīngshén nèihào, chónghuí zhuānzhù gāoxiào de gōngzuò zhuàngtài.",
                "en": "In high-pressure workplaces, maintaining good mental state is key to overcoming obstacles. When feeling anxious, pausing for deep breaths and a stroll clears the mind, shedding friction to regain productive focus.",
                "es": "En la vorágine laboral, guardar un estado anímico equilibrado es clave para superar escollos. Ante la zozobra, respirar hondo y pasear oxigena la mente, disipando el estrés para rendir con lucidez."
            },
            {
                "id": "#2",
                "hanzi": "高铁列车在以每小时三百五十公里飞驰时，车体各部传感器实时采集受电弓、轴承与制动系统的运行状态数据。车载中央电脑利用智能算法对机车运行状态进行毫秒级高频诊断，确保列车始终处于绝对安全运行状态。",
                "pinyin": "Gāotiě lièchē zài yǐ měi xiǎoshí sānbǎi wǔshí gōnglǐ fēichí shí, chētǐ gèbù chuángǎnqì shíshí cǎijí shòudiàngōng, zhóuchéng yǔ zhìdòng xìtǒng de yùnxíng zhuàngtài shùjù. Chēzài zhōngyāng diànnǎo lìyòng zhìnéng suànfǎ duì jīchē yùnxíng zhuàngtài jìnxíng háomiǎojí gāopín zhěnduàn, quèbǎo lièchē shǐzhōng chǔyú juéduì ānquán yùnxíng zhuàngtài.",
                "en": "As bullet trains race at 350 km/h, sensors collect operational data on pantographs, bearings, and brakes. Computers diagnose running states at millisecond speeds, ensuring absolute safety throughout journeys.",
                "es": "A 350 km/h, sensores del tren bala monitorizan pantógrafos, cojinetes y frenos en tiempo real. Ordenadores a bordo diagnostican el estado del convoy al milisegundo garantizando un viaje enteramente seguro."
            }
        ]
    },

    # 18 清醒
    {
        "id": "18",
        "hanzi": "清醒",
        "pinyin": "qīng xǐng",
        "part_of_speech": "Adjective / Verb",
        "meanings_summary": {
            "en": "clear-headed; sober; awake; to regain consciousness; to sober up",
            "es": "lúcido; sobrio; despierto; despejado; recobrar el conocimiento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "clear-headed, sober, alert, and rationally aware (not drunk, asleep, or confused)",
                "definition_es": "despierto, despejado, sereno y con pleno uso de las facultades racionales",
                "example_phrase": "头脑清醒 (clear-headed)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to regain consciousness after fainting, coma, or intoxication",
                "definition_es": "volver en sí, despejarse o recobrar el sentido tras desmayo o embriaguez",
                "example_phrase": "病人已经清醒过来 (the patient has regained consciousness)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "面对突如其来的巨大利益诱惑与外界吹捧，保持清醒的头脑是做出明智判断的底线。",
                "pinyin": "Miànduì tūrúqílái de jùdà lìyì yòuhuò yǔ wàijiè chuīpěng, bǎochí qīngxǐng de tóunǎo shì zuòchū míngzhì pànduàn de dǐxiàn.",
                "en": "Confronted with sudden temptations of huge profit and outside flattery, keeping a clear head is the bottom line for making wise decisions.",
                "es": "Ante la tentación de pingües ganancias y halagos desmedidos, mantener la mente despejada es premisa ineludible para obrar con juicio."
            },
            {
                "id": "#2",
                "hanzi": "在重症监护室医护人员连续两天的精心治疗下，陷入深度昏迷的伤者终于逐渐清醒了过来。",
                "pinyin": "Zài zhòngzhèng jiānhùshì yīhù rényuán liánxù liǎng tiān de jīngxīn zhìliáo xià, xiànrù shēndù hūnmí de shāngzhě zhōngyú zhújiàn qīngxǐng le guòlai.",
                "en": "Under two days of intensive care by ICU medical staff, the critically injured patient in a deep coma finally regained consciousness gradually.",
                "es": "Gracias a los minuciosos cuidados en la unidad de cuidados intensivos, el herido en coma profundo recobró paulatinamente el conocimiento."
            }
        ],
        "collocations": [
            {"hanzi": "头脑清醒", "en": "clear-headed; sober-minded"},
            {"hanzi": "清醒过来", "en": "regain consciousness / come round"},
            {"hanzi": "保持清醒", "en": "stay alert / remain sober"},
            {"hanzi": "十分清醒", "en": "fully awake / wide awake"},
            {"hanzi": "清醒认识", "en": "sober understanding / clear realization"},
            {"hanzi": "难以清醒", "en": "hard to sober up"}
        ],
        "idioms": [
            {"hanzi": "大梦初醒", "pinyin": "dà mèng chū xǐng", "meaning_en": "as if waking from a long dream; sudden awakening to reality"},
            {"hanzi": "神志清醒", "pinyin": "shén zhì qīng xǐng", "meaning_en": "fully conscious and alert; completely lucid"},
            {"hanzi": "如梦初醒", "pinyin": "rú mèng chū xǐng", "meaning_en": "wake up as from a dream; suddenly see the light"},
            {"hanzi": "从容不迫", "pinyin": "cóng róng bù pò", "meaning_en": "calm and unhurried; serene composure"}
        ],
        "character_decomposition": [
            {
                "character": "清",
                "pinyin": "qīng",
                "meaning_en": "clear; pure; clean; quiet; settle",
                "meaning_es": "claro; puro; limpio; transparente; saldar",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (clear spring water) + 青 (lush green / pure)",
                "sound_component": "青 (qīng, green/pure / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 combined with 青 (lush pure green); clear, limpid water without sediment, extended to mental clarity.",
                "visual_mnemonic_story_en": "Water (氵) as pure and tranquil as spring greenery (青) reflects crystal clarity (清).",
                "visual_mnemonic_story_es": "El agua (氵) tan pura y diáfana como el verdor primaveral (青) destila transparencia (清).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "EQMB",
                "traditional": ""
            },
            {
                "character": "醒",
                "pinyin": "xǐng",
                "meaning_en": "wake up; sober up; awaken; realize",
                "meaning_es": "despertar; despejarse; volver en sí; despabilar",
                "radical": "酉",
                "radical_meaning_en": "wine / vessel",
                "meaning_component": "酉 (fermenting wine vessel) + 星 (bright stars in morning sky)",
                "sound_component": "星 (xīng, stars / phonetic origin)",
                "stroke_count": 16,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Wine vessel 酉 dissipating intoxication as morning stars 星 shine; recovering sobriety and waking from slumber.",
                "visual_mnemonic_story_en": "Fumes from a wine jar (酉) clear away as bright morning stars (星) signal waking up (醒).",
                "visual_mnemonic_story_es": "Los vapores del jarro de vino (酉) se disipan cuando las estrellas matinales (星) despabilan al durmiente (醒).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "MWAHM",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Clear water (清) dispels wine fumes as dawn breaks (醒), making one clear-headed and awake (清醒).",
            "composite_memory_hook_es": "El agua cristalina (清) disipa los vapores del vino al romper el alba (醒), recobrando la lucidez (清醒).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese drinking culture and philosophical mindfulness (屈原: 众人皆醉我独醒: all the world is drunk, I alone am sober).",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by dipping third tone: 'qīng xǐng' (55-214). Maintain steady high pitch 55 on 'qīng', then dip and rise on 'xǐng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "晴", "pinyin": "qíng", "meaning_en": "sunny; clear", "distinction_note": "Has sun radical 日 on left of 青 instead of water 氵 in 清"},
                {"character": "请", "pinyin": "qǐng", "meaning_en": "please; invite", "distinction_note": "Has speech radical 讠 on left of 青"},
                {"character": "醉", "pinyin": "zuì", "meaning_en": "drunk; intoxicated", "distinction_note": "Has 卒 on right of 酉 instead of 星 in 醒"},
                {"character": "醋", "pinyin": "cù", "meaning_en": "vinegar", "distinction_note": "Has 昔 on right of 酉"}
            ],
            "etymological_cognates": [
                {"character": "觉", "pinyin": "jué", "gloss_en": "awaken to sense; feel"},
                {"character": "明", "pinyin": "míng", "gloss_en": "bright; lucid mind"},
                {"character": "悟", "pinyin": "wù", "gloss_en": "apprehend truth; enlighten"},
                {"character": "澈", "pinyin": "chè", "gloss_en": "limpid; penetrate through"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "清醒 emphasizes cognitive lucidity and rational wakefulness, free from intoxication, delirium, or illusion.",
            "contrasts": [
                {"id": "1", "compared_word": "清醒 vs. 醒来", "pinyin": "xǐnglái", "analysis": "醒来 focuses on the physical transitional action of opening eyes and leaving sleep ('从梦中醒来'), while 清醒 describes state of alertness or recovering from coma/drunkenness."},
                {"id": "2", "compared_word": "清醒 vs. 明白", "pinyin": "míngbai", "analysis": "明白 denotes intellectual understanding of a concept or fact ('我明白了'), whereas 清醒 is the physiological and psychological state of alertness."},
                {"id": "3", "compared_word": "清醒 vs. 镇静", "pinyin": "zhènjìng", "analysis": "镇静 emphasizes emotional calm and lack of agitation in panic ('保持镇静'), while 清醒 is intellectual lucidity."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古往今来，身处顺境高位时最难能可贵的便是保持内心的清醒与戒惧。战国楚国大诗人屈原曾慨叹“举世皆浊我独清，众人皆醉我独醒”。在名利喧嚣中守住本心，不为浮华所惑，方能行止有度、立身长远。",
                "pinyin": "Gǔwǎng-jīnlái, shēnchǔ shùnjìng gāowèi shí zuì nánnéng-kěguì de biànshì bǎochí nèixīn de qīngxǐng yǔ jièjù. Zhànguó Chǔguó dà shīrén Qū Yuán céng kǎitàn 'jǔshì jiē zhuó wǒ dú qīng, zhòngrén jiē zuì wǒ dú xǐng'. Zài mínglì xuānxiāo zhōng shǒuzhù běnxīn, bù wéi fúhuá suǒ huò, fāngnéng xíngzhǐ-yǒudù, lìshēn chángyuǎn.",
                "en": "Throughout history, staying lucid and vigilant in prosperity is rare. Poet Qu Yuan lamented, 'The whole world is turbid, I alone am pure; all are drunk, I alone am sober.' Staying grounded amidst fame leads to lasting integrity.",
                "es": "A lo largo de los siglos, guardar la lucidez y la prudencia en el éxito ha sido la más rara virtud. Como sentenció el poeta Qu Yuan: 'Ebrio está el mundo, solo yo velo lúcido'. Desoír los halagos vanos forja un carácter intachable."
            },
            {
                "id": "#2",
                "hanzi": "早晨被刺耳闹钟惊醒的人，常常会经历长达十数分钟的“睡眠惯性”状态。此时大脑皮层尚未彻底恢复清醒，血液循环与思维反应相对迟钝，若立即下床剧烈运动极易头晕目眩，应静坐片刻温和苏醒。",
                "pinyin": "Zǎochen bèi cì'ěr nàozhōng jīngxǐng de rén, chángcháng huì jīnglì chángdá shíshù fēnzhōng de 'shuìmián guànxìng' zhuàngtài. Cǐshí dànǎo pícéng shàngwèi chèdǐ huīfù qīngxǐng, xuèyè xúnhuán yǔ sīwéi fǎnyìng xiāngduì chídùn, ruò lìjí xiàchuáng jùliè yùndòng jíyì tóuyūn-mùxuàn, yīng jìngzuò piànkè wēnhé sùxǐng.",
                "en": "Those jolted awake by loud alarms often endure minutes of sleep inertia. The cerebral cortex has not regained full lucidity, blood flow is sluggish; jumping out of bed causes dizziness, so resting gently is best.",
                "es": "Quien despierta sobresaltado por el despertador padece minutos de inercia del sueño. La corteza cerebral aún no está despejada y la mente reacciona lenta; levantarse de golpe causa mareos, siendo prudente reposar un momento."
            }
        ]
    },

    # 19 呼吸
    {
        "id": "19",
        "hanzi": "呼吸",
        "pinyin": "hū xī",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to breathe; to respire; respiration; breath",
            "es": "respirar; respiración; aliento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to inhale oxygen and exhale carbon dioxide through respiratory organs",
                "definition_es": "inhalar oxígeno y exhalar dióxido de carbono a través de los órganos respiratorios",
                "example_phrase": "深呼吸 (take a deep breath)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the physiological process or sound of breathing; respiration",
                "definition_es": "el proceso fisiológico o sonido del aire al respirar; respiración",
                "example_phrase": "呼吸急促 (rapid and hurried breathing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清晨漫步在松柏苍翠的山间小路上，深深地呼吸着富含负氧离子的清新空气，顿觉心旷神怡。",
                "pinyin": "Qīngchén mànbù zài sōngbǎi cāngcuì de shānjiān xiǎolù shàng, shēnshēn de hūxī zhe fùhán fùyǎnglízǐ de qīngxīn kōngqì, dùnjué xīnkuàng-shényí.",
                "en": "Strolling on pine-lined mountain paths in the morning, breathing deeply the fresh air rich in negative oxygen ions brings instant serenity.",
                "es": "Paseando al amanecer por un sendero entre pinos y respirando hondo el aire puro del bosque, el espíritu se serena y regocija."
            },
            {
                "id": "#2",
                "hanzi": "医生仔细检查患者的胸腔起伏与脉搏跳动，发现其呼吸极其微弱，立刻组织团队展开紧急气管插管抢救。",
                "pinyin": "Yīshēng zǐxì jiǎnchá huànzhě de xiōngqiāng qǐfú yǔ màibó tiàodòng, fāxiàn qí hūxī jíqí wēiruò, lìkè zǔzhī tuánduì zhǎnkāi jǐnjí qìguǎn chāguǎn qiǎngjiù.",
                "en": "The doctor checked chest movements and pulse, finding the patient's breathing extremely faint, immediately organizing intubation rescue.",
                "es": "El médico comprobó el pulso y el tórax del paciente hallando su respiración sumamente débil, procediendo a una intubación traqueal de urgencia."
            }
        ],
        "collocations": [
            {"hanzi": "深呼吸", "en": "deep breath; take a deep breath"},
            {"hanzi": "呼吸困难", "en": "difficulty breathing; dyspnea"},
            {"hanzi": "呼吸系统", "en": "respiratory system"},
            {"hanzi": "屏住呼吸", "en": "hold one's breath"},
            {"hanzi": "呼吸急促", "en": "rapid breathing; shortness of breath"},
            {"hanzi": "人工呼吸", "en": "artificial respiration / CPR"}
        ],
        "idioms": [
            {"hanzi": "同呼吸共命运", "pinyin": "tóng hū xī gòng mìng yùn", "meaning_en": "breathe the same air and share the same destiny; united in fate"},
            {"hanzi": "屏气凝神", "pinyin": "bǐng qì níng shén", "meaning_en": "hold one's breath and concentrate with rapt attention"},
            {"hanzi": "气喘吁吁", "pinyin": "qì chuǎn xū xū", "meaning_en": "panting and out of breath after exertion"},
            {"hanzi": "苟延残喘", "pinyin": "gǒu yán cán chuǎn", "meaning_en": "barely manage to prolong lingering breath; scrape along"}
        ],
        "character_decomposition": [
            {
                "character": "呼",
                "pinyin": "hū",
                "meaning_en": "call; shout; exhale; breathe out",
                "meaning_es": "llamar; gritar; exhalar; expirar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (open mouth) + 乎 (sound of air sighing out)",
                "sound_component": "乎 (hū, sighing exhalation / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Open mouth 口 blowing air outward or sighing 乎; signifies exhalation, calling out, or shouting.",
                "visual_mnemonic_story_en": "An open mouth (口) exhales air smoothly outward into the wind (乎), breathing out (呼).",
                "visual_mnemonic_story_es": "Una boca abierta (口) exhala el aire hacia afuera en suave suspiro (乎), espirando (呼).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RHFD",
                "traditional": ""
            },
            {
                "character": "吸",
                "pinyin": "xī",
                "meaning_en": "inhale; breathe in; absorb; suck",
                "meaning_es": "inhalar; inspirar; absorber; chupar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth opening) + 及 (hand reaching and catching)",
                "sound_component": "及 (jí, reach / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Mouth 口 catching and drawing air into the body 及; represents inhalation, sucking, or absorption.",
                "visual_mnemonic_story_en": "A mouth (口) reaches inward to draw in (及) fresh air, inhaling deeply (吸).",
                "visual_mnemonic_story_es": "Una boca (口) atrae hacia adentro (及) el aire fresco, inspirando con hondura (吸).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RNHE",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Blowing air out (呼) and drawing air in (吸) forms the natural rhythm of respiration (呼吸).",
            "composite_memory_hook_es": "Expulsar el aire (呼) y tomar aire hacia adentro (吸) constituye el ciclo de la respiración (呼吸).",
            "cultural_and_cognitive_roots": "Daoist inner cultivation (吐纳之术: spitting out turbid air and inhaling fresh qi); breathing forms the vital conduit linking cosmos and human physiology.",
            "tone_sandhi_and_pitch_modulation": "Double level high first tones: 'hū xī' (55-55). Hold level high pitch 55 smoothly across both syllables like calm, steady breathing."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "乎", "pinyin": "hū", "meaning_en": "modal particle", "distinction_note": "Lacks the mouth radical 口 of 呼"},
                {"character": "呼", "pinyin": "hū", "meaning_en": "breathe out; call", "distinction_note": "Has mouth radical 口 on left"},
                {"character": "及", "pinyin": "jí", "meaning_en": "reach; and", "distinction_note": "Lacks mouth radical 口 of 吸"},
                {"character": "级", "pinyin": "jí", "meaning_en": "level; grade", "distinction_note": "Has silk radical 纟 on left of 及"}
            ],
            "etymological_cognates": [
                {"character": "气", "pinyin": "qì", "gloss_en": "vapor; vital air/energy"},
                {"character": "喘", "pinyin": "chuǎn", "gloss_en": "pant; gasp for breath"},
                {"character": "吸", "pinyin": "xī", "gloss_en": "inhale into mouth"},
                {"character": "吐", "pinyin": "tǔ", "gloss_en": "spit out; exhale"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "呼吸 is the comprehensive biological term for the complete cycle of inhaling and exhaling.",
            "contrasts": [
                {"id": "1", "compared_word": "呼吸 vs. 喘气", "pinyin": "chuǎnqì", "analysis": "喘气 specifically describes rapid, labored gasping for breath after exhausting physical exercise, while 呼吸 is regular calm respiration."},
                {"id": "2", "compared_word": "呼吸 vs. 叹气", "pinyin": "tànqì", "analysis": "叹气 refers to sighing out of sorrow, frustration, or relief ('唉声叹气'), not physiological gas exchange."},
                {"id": "3", "compared_word": "呼吸 vs. 气息", "pinyin": "qìxī", "analysis": "气息 refers to the faint stream of air from the nostrils/mouth or emotional atmosphere ('春天的气息'), while 呼吸 is the bodily process."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代瑜伽与冥想练习中，调整呼吸被视为平复思绪与连接身心的核心纽带。练习者通过放慢呼吸节奏、进行腹式深呼吸，能够有效激活体内副交感神经系统，促使紧绷的心率与血压平稳回落，带来深度的平静与放松。",
                "pinyin": "Zài xiàndài yújiā yǔ míngxiǎng liànxí zhōng, tiáozhěng hūxī bèi shìwéi píngfù sīxù yǔ liánjiē shēn-xīn de héxīn niǔdài. Liànxízhě tōngguò fàngmàn hūxī jiézòu, jìnxíng fùshì shēnhūxī, nénggòu yǒuxiào jīhuó tǐnèi fùjiāogǎn shénjīng xìtǒng, cùshǐ jǐnbēng de xīnlǜ yǔ xuèyā píngwěn huíluò, dàilái shēndù de píngjìng yǔ fàngsōng.",
                "en": "In yoga and meditation, regulating breath connects body and mind. Slowing breathing and using deep diaphragmatic breaths activates parasympathetic systems, lowering heart rates and blood pressure for deep relaxation.",
                "es": "En el yoga y la meditación, acompasar la respiración une cuerpo y mente. Una respiración abdominal pausada activa el sistema parasimpático, serenando el pulso y la tensión para un sosiego hondo."
            },
            {
                "id": "#2",
                "hanzi": "广袤繁茂的热带雨林被誉为“地球之肺”，全球数以百亿计的绿色植物通过光合作用日夜不停地进行着碳氧气体交换。大自然的每一次呼吸，不仅维系着大气层中氧气含量的动态平衡，更是守护所有生命延续的生命源泉。",
                "pinyin": "Guǎngmào fánmào de rèdài yǔlín bèi yùwéi 'Dìqiúzhīfèi', quánqiú shùyǐbǎiyìjì de lǜsè zhíwù tōngguò guānghé zuòyòng rìyè-bùtíng de jìnxíng zhe tàn-yǎng qìtǐ jiāohuàn. Dànzìrán de měi yí cì hūxī, bùjǐn wéixì zhe dàqìcéng zhōng yǎngqì hánliàng de dòngtài pínghéng, gèng shì shǒuhù suǒyǒu shēngmìng yánxù de shēngmìng yuánquán.",
                "en": "Rainforests are hailed as Earth's lungs, billions of green plants exchanging carbon and oxygen through photosynthesis day and night. Every breath of nature maintains oxygen balance, sustaining the fountain of life.",
                "es": "La selva amazónica es el pulmón de la Tierra; miles de millones de plantas fotosintetizan noche y día. Cada hálito de la naturaleza equilibra el oxígeno de la atmósfera custodiando la fuente misma de la vida."
            }
        ]
    },

    # 20 心理
    {
        "id": "20",
        "hanzi": "心理",
        "pinyin": "xīn lǐ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "psychology; mentality; mindset; psychological",
            "es": "psicología; mentalidad; psique; psicológico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the mental and emotional states, cognitive processes, or subjective mindset of an individual or group",
                "definition_es": "conjunto de procesos anímicos, cognitivos y afectivos que configuran la mente de un individuo o colectivo",
                "example_phrase": "心理健康 (mental health)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "面对重重学业考核与升学压力，学校设立了专门的心理咨询辅导室帮助学生排解心理焦虑。",
                "pinyin": "Miànduì chóngchóng xuéyè kǎohé yǔ shēngxué yālì, xuéxiào shèlì le zhuānmén de xīnlǐ zīxún fǔdǎoshì bāngzhù xuésheng páijiě xīnlǐ jiāolǜ.",
                "en": "Facing mounting academic exams and admission pressures, the school established a dedicated psychological counseling room to help students dispel anxiety.",
                "es": "Ante la presión de los exámenes y el ingreso escolar, el colegio habilitó un gabinete de orientación psicológica para canalizar la ansiedad del alumnado."
            },
            {
                "id": "#2",
                "hanzi": "资深谈判专家敏锐地洞察到了对方买家急于求成的焦躁心理，因势利导掌握了定价的主动权。",
                "pinyin": "Zīshēn tánpàn zhuānjiā mǐnruì de dòngchá dào le duìfāng mǎijiā jíyú-qiúchéng de jiāozào xīnlǐ, yīnshì-lìdǎo zhǎngwò le dìngjià de zhǔdòngquán.",
                "en": "The veteran negotiator keenly discerned the buyer's impatient psychology to close the deal, seizing the upper hand in pricing discussions.",
                "es": "El avezado negociador caló la impaciente psicología del comprador por cerrar el trato, tomando la iniciativa en las condiciones de precio."
            }
        ],
        "collocations": [
            {"hanzi": "心理健康", "en": "mental health; psychological wellbeing"},
            {"hanzi": "心理医生", "en": "psychiatrist; psychotherapist"},
            {"hanzi": "心理压力", "en": "psychological stress/pressure"},
            {"hanzi": "心理状态", "en": "psychological state / mindset"},
            {"hanzi": "心理学", "en": "psychology (discipline)"},
            {"hanzi": "心理准备", "en": "psychological readiness/preparation"}
        ],
        "idioms": [
            {"hanzi": "心照不宣", "pinyin": "xīn zhào bù xuān", "meaning_en": "understand each other tacitly without a word spoken"},
            {"hanzi": "心满意足", "pinyin": "xīn mǎn yì zú", "meaning_en": "fully satisfied and contented in heart"},
            {"hanzi": "居安思危", "pinyin": "jū ān sī wēi", "meaning_en": "in peace prepare for danger; mental vigilance"},
            {"hanzi": "忐忑不安", "pinyin": "tǎn tè bù ān", "meaning_en": "fidgety and restless; uneasy in mind"}
        ],
        "character_decomposition": [
            {
                "character": "心",
                "pinyin": "xīn",
                "meaning_en": "heart; mind; center; core",
                "meaning_es": "corazón; mente; centro; núcleo",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "心 (anatomical heart with pericardium chambers)",
                "sound_component": "心 (xīn)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of the human heart, depicting the muscular chambers and aorta; the seat of thoughts and feelings in ancient epistemology.",
                "visual_mnemonic_story_en": "The human heart (心) beats with chambers pumping blood and cradling feelings.",
                "visual_mnemonic_story_es": "El corazón (心) con sus ventrículos bombea sangre cobijando pensamientos y emociones.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "P",
                "traditional": ""
            },
            {
                "character": "理",
                "pinyin": "lǐ",
                "meaning_en": "reason; logic; veins in jade; manage; principle",
                "meaning_es": "razón; lógica; vetas del jade; gestionar; principio",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王 (fine jade stone) + 里 (orderly village grid lines)",
                "sound_component": "里 (lǐ, village / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Carving jade 王 along its natural internal grain and veins 里; signifies intrinsic principles, logic, reason, and orderly management.",
                "visual_mnemonic_story_en": "A master carves jade (王) following its natural inner vein lines (里) with logic and reason (理).",
                "visual_mnemonic_story_es": "El tallista pule el jade (王) siguiendo sus vetas naturales (里) con destreza y razón (理).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "MGWG",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The internal veins and rational principles (理) governing the human heart and mind (心) make up psychology (心理).",
            "composite_memory_hook_es": "Las vetas y principios lógicos (理) que rigen el corazón y la mente (心) componen la psicología (心理).",
            "cultural_and_cognitive_roots": "Song-Ming Neo-Confucian philosophy (心学与理学: Wang Yangming and Zhu Xi debates on 心 vs. 理); modern science fused them to translate Western psychology (心理学).",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by dipping third tone: 'xīn lǐ' (55-214). Maintain steady high pitch 55 on 'xīn', then dip down and rebound on 'lǐ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "必", "pinyin": "bì", "meaning_en": "must; surely", "distinction_note": "Has long slash stroke crossing through 心"},
                {"character": "息", "pinyin": "xī", "meaning_en": "breath; rest", "distinction_note": "Has 自 atop 心"},
                {"character": "埋", "pinyin": "mái", "meaning_en": "bury", "distinction_note": "Has earth radical 土 on left of 里 instead of jade 王 in 理"},
                {"character": "野", "pinyin": "yě", "meaning_en": "wild; field", "distinction_note": "Has 里 on left of 予"}
            ],
            "etymological_cognates": [
                {"character": "性", "pinyin": "xìng", "gloss_en": "human nature; character"},
                {"character": "情", "pinyin": "qíng", "gloss_en": "emotion; sentiment"},
                {"character": "念", "pinyin": "niàn", "gloss_en": "mindful thought; memory"},
                {"character": "志", "pinyin": "zhì", "gloss_en": "ambition; intent of heart"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "心理 encompasses the inner subjective emotional states, attitudes, and cognitive processes of individuals or groups.",
            "contrasts": [
                {"id": "1", "compared_word": "心理 vs. 生理", "pinyin": "shēnglǐ", "analysis": "生理 pertains to biological, anatomical bodily functions (hormones, digestion, heartbeat), while 心理 pertains to mental, cognitive, and emotional processes."},
                {"id": "2", "compared_word": "心理 vs. 心态", "pinyin": "xīntài", "analysis": "心态 specifically designates psychological attitude or emotional outlook ('保持平稳心态'), while 心理 covers the entire academic discipline and mental structure."},
                {"id": "3", "compared_word": "心理 vs. 思想", "pinyin": "sīxiǎng", "analysis": "思想 refers to political, philosophical, or ideological systems of belief ('哲学思想'), whereas 心理 refers to affective emotional states."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在现代竞争激烈的体育赛场上，顶尖运动员之间的技术差距往往微乎其微，最终决定胜负走向的关键往往在于心理素质的较量。面对逆境时能否顶住心理压力、保持沉着冷静，往往直接决定了冠军金牌的归属。",
                "pinyin": "Zài xiàndài jìngzhēng jīliè de tǐyù sàichǎng shàng, dǐngjiān yùndòngyuán zhījiān de jìshù chājù wǎngwǎng wēihūqíwēi, zuìzhōng juédìng shèngfù zǒuxiàng de guānjiàn wǎngwǎng zàiyú xīnlǐ sùzhì de jiàoliàng. Miànduì nìjìng shí néngfǒu dǐngzhù xīnlǐ yālì, bǎochí chénzhuó lěngjìng, wǎngwǎng zhíjiē juédìng le guànjūn jīnpái de guīshǔ.",
                "en": "In elite athletic competitions, technical gaps between champions are minuscule; victory is decided by psychological fortitude. Withstanding mental pressure in adversity and keeping cool determines gold medalists.",
                "es": "En la alta competición atlética, las diferencias técnicas son mínimas; el triunfo se decide en la solidez psicológica. Resistir la presión anímica en la adversidad con aplomo es lo que corona a los campeones."
            },
            {
                "id": "#2",
                "hanzi": "关注青少年心理健康已成为全社会的共识。家庭与学校应当摒弃“唯成绩论”的片面观念，营造包容温润的成长氛围，引导孩子正确看待挫折与失败。当孩子遭遇心理困惑时，多倾听、多肯定，筑牢守护心灵的阳光港湾。",
                "pinyin": "Guānzhù qīng-shàonián xīnlǐ jiànkāng yǐ chéngwéi quán shèhuì de gòngshí. Jiātíng yǔ xuéxiào yīngdāng bǐngqì 'wéi chéngjì lùn' de piànmiàn guānniàn, yíngzào bāoróng wēnrùn de chéngzhǎng fēnwéi, yǐndǎo háizi zhèngquè kàndài cuòzhé yǔ shībài. Dāng háizi zāoyù xīnlǐ kùnhuò shí, duō qīngtīng, duō kěndìng, zhùláo shǒuhù xīnlíng de yángguāng gǎngwān.",
                "en": "Attending to adolescent mental health is a societal consensus. Families and schools should abandon grading-only biases, building nurturing environments. Listening and encouraging children facing dilemmas builds a haven for their souls.",
                "es": "Atender la salud mental de la juventud es un deber social unánime. Hogares y escuelas deben desterrar el culto exclusivo a las notas, acogiendo con empatía para que los jóvenes encajen tropiezos y crezcan con ilusión."
            }
        ]
    }
]

from core.toon_builder import save_word

words_batch3 = [
    # 11 抱怨
    {
        "id": "11",
        "hanzi": "抱怨",
        "pinyin": "bào yuàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to complain; to grumble; to blame",
            "es": "quejarse; rezongar; lamentarse; culpar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to express dissatisfaction, resentment, or grievance about an unpleasant situation or person",
                "definition_es": "expresar descontento, resentimiento o reproche ante una situación adversa o persona",
                "example_phrase": "抱怨天气 (complain about the weather)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "遇到生活中的挫折时，一味抱怨外界环境并不能解决问题，积极调整心态才是走出困境的关键。",
                "pinyin": "Yùdào shēnghuó zhōng de cuòzhé shí, yíwèi bàoyuàn wàijiè huánjìng bìng bù néng jiějué wèntí, jījí tiáozhěng xīntài cái shì zǒuchū kùnjìng de guānjiàn.",
                "en": "When encountering setbacks in life, blindly complaining about external circumstances resolves nothing; proactively adjusting one's mindset is the key out of adversity.",
                "es": "Al afrontar reveses en la vida, quejarse ciegamente del entorno no resuelve nada; ajustar una actitud proactiva es la clave para superar las dificultades."
            },
            {
                "id": "#2",
                "hanzi": "在产品发布后的用户体验追踪调研中，不少消费者公开抱怨该款智能软件的操作界面复杂繁琐。",
                "pinyin": "Zài chǎnpǐn fābù hòu de yònghù tǐyàn zhuīzōng diàoyán zhōng, bùshǎo xiāofèizhě gōngkāi bàoyuàn gāi kuǎn zhìnéng ruǎnjiàn de cāozuò jièmiàn fùzá fánsuǒ.",
                "en": "In post-launch user experience tracking surveys, many consumers openly complained that the operating interface of the smart software was convoluted and cumbersome.",
                "es": "En las encuestas de seguimiento de experiencia de usuario tras el lanzamiento, numerosos consumidores se quejaron de que la interfaz del software resultaba confusa."
            }
        ],
        "collocations": [
            {"hanzi": "经常抱怨", "en": "constantly complain"},
            {"hanzi": "停止抱怨", "en": "stop complaining"},
            {"hanzi": "抱怨命运", "en": "complain about fate"},
            {"hanzi": "毫无抱怨", "en": "without any complaint"},
            {"hanzi": "引起抱怨", "en": "cause complaints / grumbling"},
            {"hanzi": "私下抱怨", "en": "grumble in private"}
        ],
        "idioms": [
            {"hanzi": "怨天尤人", "pinyin": "yuàn tiān yóu rén", "meaning_en": "blame heaven and other people; complain of fate"},
            {"hanzi": "满腹牢骚", "pinyin": "mǎn fù láo sāo", "meaning_en": "full of grievances and complaints"},
            {"hanzi": "以德报怨", "pinyin": "yǐ dé bào yuàn", "meaning_en": "repay injury with kindness"},
            {"hanzi": "任劳任怨", "pinyin": "rèn láo rèn yuàn", "meaning_en": "bear hardships and work without complaints"}
        ],
        "character_decomposition": [
            {
                "character": "抱",
                "pinyin": "bào",
                "meaning_en": "hold in arms; hug; cherish; harbor",
                "meaning_es": "abrazar; sostener en brazos; albergar",
                "radical": "手",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand, embracing or holding)",
                "sound_component": "包 (bāo, wrap/bundle)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining hand (扌) with wrapping package (包), describing folding arms around something or harboring sentiments in one's bosom.",
                "visual_mnemonic_story_en": "Hands (扌) wrap tightly around a heavy bundle (包), holding grudges close to the chest.",
                "visual_mnemonic_story_es": "Las manos (扌) envuelven con fuerza un fardo (包), reteniendo amarguras contra el pecho.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "QPU",
                "traditional": '""'
            },
            {
                "character": "怨",
                "pinyin": "yuàn",
                "meaning_en": "resent; blame; grievance; malice",
                "meaning_es": "resentimiento; rencor; agravio; quejarse",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "心 (heart, inner emotional distress)",
                "sound_component": "夗 (yuàn, bent/turned over in bed)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character of turning restlessly in bed (夗) over heartache (心), conveying brooding bitterness.",
                "visual_mnemonic_story_en": "Tossing restlessly at dusk (夗) because the heart (心) harbors unresolved grievances.",
                "visual_mnemonic_story_es": "Dar vueltas inquietas al anochecer (夗) porque el corazón (心) alberga rencores no resueltos.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NUP",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Harboring in your chest (抱) a wounded heart full of resentment (怨) spills outward as constant complaining.",
            "composite_memory_hook_es": "Abrazar en el pecho (抱) un corazón herido de resentimiento (怨) se desborda en quejas continuas.",
            "cultural_and_cognitive_roots": "Chinese psychological tradition distinguishes between verbal expression and internal brooding; 'bàoyuàn' literally describes carrying (抱) grievances (怨) in one's bosom, reflecting the Buddhist-Taoist observation that harboring resentment harms internal harmony.",
            "tone_sandhi_and_pitch_modulation": "51-51 pitch contour. Two consecutive 4th tones require crisp, assertive downward falls (51 to 51) without merging into flat tones."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "跑", "pinyin": "pǎo", "meaning_en": "run", "distinction_note": "Has foot radical 𧾷 on the left instead of hand 扌"},
                {"character": "饱", "pinyin": "bǎo", "meaning_en": "full; satisfied", "distinction_note": "Has food radical 饣 on the left instead of hand 扌"},
                {"character": "恕", "pinyin": "shù", "meaning_en": "forgive; pardon", "distinction_note": "Features 如 over 心 instead of 夗"},
                {"character": "怒", "pinyin": "nù", "meaning_en": "anger; furious", "distinction_note": "Features 奴 over 心 instead of 夗"}
            ],
            "etymological_cognates": [
                {"character": "包", "pinyin": "bāo", "gloss_en": "wrap; phonetic root of 抱"},
                {"character": "恨", "pinyin": "hèn", "gloss_en": "hate; remorse in the heart family"},
                {"character": "悔", "pinyin": "huǐ", "gloss_en": "regret; remorse"},
                {"character": "忧", "pinyin": "yōu", "gloss_en": "grief; worry"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "抱怨 focuses on venting vocal discontent or harboring chronic dissatisfaction toward unfavorable conditions or people.",
            "contrasts": [
                {"id": "1", "compared_word": "抱怨 vs. 埋怨", "pinyin": "mányuàn", "analysis": "埋怨 emphasizes finding fault with or blaming someone for minor blunders (often mild or implicit), whereas 抱怨 focuses on openly grumbling about hardship or poor conditions."},
                {"id": "2", "compared_word": "抱怨 vs. 批评", "pinyin": "pīpíng", "analysis": "批评 is constructive or formal critique aimed at evaluating faults or correcting behaviour, whereas 抱怨 is an emotional venting of dissatisfaction."},
                {"id": "3", "compared_word": "抱怨 vs. 控告", "pinyin": "kònggào", "analysis": "控告 is a formal legal term meaning to file criminal or legal charges, whereas 抱怨 is casual or emotional grumbling."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活就像一面镜子，你对它抱怨，它便回赠你阴霾；你对它微笑，它便报之以晴朗。无休止的抱怨如同一杯苦酒，不仅会腐蚀自己的心境，也会疏远身边的挚友。唯有放下抱怨，才能看清前路的花开。",
                "pinyin": "Shēnghuó jiù xiàng yí miàn jìngzi, nǐ duì tā bàoyuàn, tā biàn huízèng nǐ yīnmái; nǐ duì tā wēixiào, tā biàn bào zhī yǐ qínglǎng. Wúxiūzhǐ de bàoyuàn rútóng yì bēi kǔjiǔ, bùjǐn huì fǔshí zìjǐ de xīnjìng, yě huì shūyuǎn shēnbiān de zhìyǒu. Wéiyǒu fàngxià bàoyuàn, cáinǐng kànqīng qiánlù de huākāi.",
                "en": "Life is like a mirror: if you complain to it, it returns gloom; if you smile, it gives warmth. Ceaseless complaining is a bitter draught, eroding your mood and distancing friends. Only dropping complaints reveals the flowers ahead.",
                "es": "La vida es como un espejo: si te quejas ante ella, te devuelve sombras; si le sonríes, te brinda luz. Quejarse sin cesar es como un trago amargo que marchita el ánimo y aleja a los amigos. Dejar las quejas permite ver los senderos floridos."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业组织行为学中，员工无序的抱怨往往是内部管理沟通机制不畅的警示信号。卓越的管理者善于将消极抱怨转化为建设性反馈，通过构建开放的民主申诉通道，将潜在的团队怨气转化为流程革新的动力。",
                "pinyin": "Zài xiàndài qǐyè zǔzhī xíngwéixué zhōng, yuángōng wúxù de bàoyuàn wǎngwǎng shì nèibù guǎnlǐ gōutōng jīzhì bú chàng de jǐngshì xìnhào. Zhuóyuè de guǎnlǐzhě shànyú jiāng xiāojí bàoyuàn zhuǎnhuà wéi jiànshèxìng fǎnkuì, tōngguò gòujiàn kāifàng de mínzhǔ shēnsù tōngdào, jiāng qiánzài de tuánduì yuànqì zhuǎnhuà wéi liúchéng géxīn de dònglì.",
                "en": "In organizational behavior, disordered employee complaining serves as a red flag signaling obstructed internal communication. Astute managers convert complaints into constructive feedback, channeling latent team frustration into motivation for process innovation.",
                "es": "En el comportamiento organizativo moderno, las quejas continuas de los empleados advierten fallas de comunicación interna. Los líderes competentes transforman los descontentos en aportes constructivos, convirtiendo el malestar latente en motor de innovación."
            }
        ]
    },

    # 12 爱护
    {
        "id": "12",
        "hanzi": "爱护",
        "pinyin": "ài hù",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to care for; to cherish; to treasure; to take good care of",
            "es": "cuidar; proteger; mimar; valorar con esmero"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to cherish, protect, and care tenderly for people (subordinates/children) or public property",
                "definition_es": "cuidar con cariño y proteger a personas o cuidar esmeradamente bienes públicos",
                "example_phrase": "爱护公物 (take good care of public property)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "班主任老师不仅悉心指导我们的学业，更像父母一样在日常生活中爱护每一个学生的身体与心理健康。",
                "pinyin": "Bānzhǔrèn lǎoshī bùjǐn xīxīn zhǐdǎo wǒmen de xuéyè, gèng xiàng fùmǔ yíyàng zài rìcháng shēnghuó zhōng àihù měi yí gè xuéshēng de shēntǐ yǔ xīnlǐ jiànkāng.",
                "en": "Our homeroom teacher not only guides our academics with diligence, but also cares for every student's physical and mental health like a parent.",
                "es": "El tutor no solo orienta nuestros estudios con esmero, sino que cuida la salud física y emocional de cada alumno con afecto maternal."
            },
            {
                "id": "#2",
                "hanzi": "企业社会责任报告特别强调，所有员工在日常生产经营活动中都应自觉爱护厂区环境，严守生态保护红线。",
                "pinyin": "Qǐyè shèhuì zérèn bàogào tèbié qiángdiào, suǒyǒu yuángōng zài rìcháng shēngchǎn jīngyíng huó dòng zhōng dōu yīng zìjué àihù chǎngqū huánjìng, yánshǒu shēngtài bǎohù hóngxiàn.",
                "en": "The corporate social responsibility report specifically emphasized that all employees must take good care of the factory environment and respect ecological baselines.",
                "es": "El informe de responsabilidad social empresarial destacó que todos los empleados deben cuidar conscientemente las instalaciones y respetar las normas ecológicas."
            }
        ],
        "collocations": [
            {"hanzi": "爱护公物", "en": "take care of public property"},
            {"hanzi": "爱护环境", "en": "care for the environment"},
            {"hanzi": "爱护花草", "en": "protect flora and greenery"},
            {"hanzi": "倍加爱护", "en": "cherish with double care"},
            {"hanzi": "爱护儿童", "en": "care for and protect children"},
            {"hanzi": "爱护名誉", "en": "cherish one's reputation"}
        ],
        "idioms": [
            {"hanzi": "爱不释手", "pinyin": "ài bù shì shǒu", "meaning_en": "love something so much one cannot part with it"},
            {"hanzi": "爱憎分明", "pinyin": "ài zēng fēn míng", "meaning_en": "have a clear distinction between what to love and what to hate"},
            {"hanzi": "官官相护", "pinyin": "guān guān xiāng hù", "meaning_en": "bureaucrats shielding one another; mutual complicity"},
            {"hanzi": "自相庇护", "pinyin": "zì xiāng bì hù", "meaning_en": "shield each other mutually"}
        ],
        "character_decomposition": [
            {
                "character": "爱",
                "pinyin": "ài",
                "meaning_en": "love; affection; cherish",
                "meaning_es": "amor; afecto; apreciar",
                "radical": "爫",
                "radical_meaning_en": "claw / hand",
                "meaning_component": "爫 (caring hands)",
                "sound_component": "冖 (protective shelter) + 友 (friend)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Depicts tender hands (爫) stretching a shelter (冖) over a cherished companion (友).",
                "visual_mnemonic_story_en": "A protective canopy (冖) extends gentle hands (爫) over a beloved friend (友).",
                "visual_mnemonic_story_es": "Un techo protector (冖) extiende manos cariñosas (爫) para amparar al amigo querido (友).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BBE",
                "traditional": "愛"
            },
            {
                "character": "护",
                "pinyin": "hù",
                "meaning_en": "protect; guard; shield; shelter",
                "meaning_es": "proteger; cuidar; guardar; defender",
                "radical": "手",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand protecting/defending)",
                "sound_component": "户 (hù, household door)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining protective hand (扌) with home portal (户), conveying guarding the threshold.",
                "visual_mnemonic_story_en": "Hands (扌) stand guard at the entryway door (户) to protect those inside.",
                "visual_mnemonic_story_es": "Unas manos firmes (扌) guardan la puerta de casa (户) para proteger a la familia.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "QHS",
                "traditional": "護"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Pouring genuine love (爱) while extending hands to shield and protect (护) encapsulates caring deeply for someone or something.",
            "composite_memory_hook_es": "Brindar amor sincero (爱) extendiendo las manos para proteger (护) significa cuidar con devoción.",
            "cultural_and_cognitive_roots": "Derived from classical ethics of paternal benevolence and ecological stewardship ('仁民而爱物'); caring combines tender warmth with vigilant protective action.",
            "tone_sandhi_and_pitch_modulation": "51-51 pitch contour. Both syllables are sharp falling 4th tones; articulate each tone distinctly without swallowing the syllable finals."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "受", "pinyin": "shòu", "meaning_en": "receive; bear", "distinction_note": "Lacks the upper horizontal roof stroke; different top component from 爱"},
                {"character": "妥", "pinyin": "tuǒ", "meaning_en": "proper", "distinction_note": "Features 女 below 爫 instead of 友"},
                {"character": "炉", "pinyin": "lú", "meaning_en": "stove; furnace", "distinction_note": "Has fire radical 火 on the left instead of hand 扌"},
                {"character": "庐", "pinyin": "lú", "meaning_en": "thatched hut", "distinction_note": "Features 广 on the outside enclosing 户"}
            ],
            "etymological_cognates": [
                {"character": "保", "pinyin": "bǎo", "gloss_en": "protect; preserve"},
                {"character": "卫", "pinyin": "wèi", "gloss_en": "defend; guard"},
                {"character": "惜", "pinyin": "xī", "gloss_en": "cherish; feel tender regret"},
                {"character": "疼", "pinyin": "téng", "gloss_en": "love dearly; dote upon"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "爱护 conveys protective affection and conscientious care, used towards subordinates, youth, animals, or public objects.",
            "contrasts": [
                {"id": "1", "compared_word": "爱护 vs. 爱惜", "pinyin": "àixī", "analysis": "爱惜 focuses on not wasting or squandering scarce resources (e.g., 爱惜时间, 爱惜粮食), while 爱护 stresses protecting something fragile from damage or harm (e.g., 爱护公物, 爱护身体)."},
                {"id": "2", "compared_word": "爱护 vs. 保护", "pinyin": "bǎohù", "analysis": "保护 focuses on shielding against external threats, attacks, or environmental legal frameworks, whereas 爱护 adds a layer of emotional warmth, gentleness, and moral duty."},
                {"id": "3", "compared_word": "爱护 vs. 关心", "pinyin": "guānxīn", "analysis": "关心 denotes psychological solicitude and attentiveness to someone's welfare, whereas 爱护 emphasizes physical protection, stewardship, and preservation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "真正的爱护不是将幼苗置于温室中免受风雨，而是在它成长时给予坚定的庇护与守望。唯有懂得尊重自然的规律，悉心呵护弱小而不横加干涉，才能让生命在辽阔的天地间自由舒展，长成参天大树。",
                "pinyin": "Zhēnzhèng de àihù bú shì jiāng yòumiáo zhìyú wēnshì zhōng miǎnshòu fēngyǔ, érshì zài tā chéngzhǎng shí jǐyǔ jiāndìng de bìhù yǔ shǒuwàng. Wéiyǒu dǒngdé zūnzhòng zìrán de guīlǜ, xīxīn hēhù ruòxiǎo ér bù héngjiā gānshè, cáinǐng ràng shēngmìng zài liáokuò de tiāndì jiān zìyóu shūzhǎn, zhǎng chéng cāntiān dàshù.",
                "en": "True care does not mean locking seedlings in a greenhouse away from rain, but offering steady guardianship as they grow. Only by respecting nature's rhythm and tenderly protecting the young can life thrive freely into towering trees.",
                "es": "Cuidar de verdad no consiste en encerrar los brotes en un invernadero, sino en brindarles cobijo constante mientras crecen. Solo respetando la naturaleza y protegiendo a los frágiles sin asfixiarlos puede la vida florecer en árboles robustos."
            },
            {
                "id": "#2",
                "hanzi": "在现代公共文化遗产保护与城市更新的交汇点上，全社会爱护历史古迹的意识成为衡量城市文明的重要标尺。通过立法规范古建筑修缮标准，引导市民自发参与文物巡查，方能实现珍贵历史文脉的永续传承。",
                "pinyin": "Zài xiàndài gōnggòng wénhuà yíchǎn bǎohù yǔ chéngshì gēngxīn de jiāohuìdiǎn shàng, quán shèhuì àihù lìshǐ gǔjì de yìshí chéngwéi héngliáng chéngshì wénmíng de zhòngyào biāochǐ. Tōngguò lìfǎ guīfàn gǔ jiànzhù xiūshàn biāozhǔn, yǐndǎo shìmín zìfā cānyù wénwù xúnchá, fāng néng shíxiàn zhēnguì lìshǐ wénmài de yǒngxù chuánchéng.",
                "en": "At the crossroads of heritage preservation and urban renewal, societal care for historical relics measures urban civility. Regulating restoration standards and guiding citizens to monitor heritage ensure that precious cultural roots endure.",
                "es": "En la intersección entre patrimonio y renovación urbana, la conciencia social de cuidar los monumentos mide la madurez de una ciudad. Regular la restauración de edificios antiguos y fomentar la participación ciudadana preserva las raíces culturales."
            }
        ]
    },

    # 13 婚姻
    {
        "id": "13",
        "hanzi": "婚姻",
        "pinyin": "hūn yīn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "marriage; matrimony; marital relationship",
            "es": "matrimonio; unión conyugal; nupcias"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the legally or socially recognized union of two people as partners in a personal relationship",
                "definition_es": "unión legal y socialmente reconocida de dos personas como pareja conyugal",
                "example_phrase": "婚姻幸福 (happy marriage)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在长达数十年的婚姻旅程中，相互信任与包容是化解生活琐事争执、保持感情历久弥新的坚实基石。",
                "pinyin": "Zài chángdá shù shí nián de hūnyīn lǚchéng zhōng, xiānghù xìnrèn yǔ bāoróng shì huàjiě shēnghuó suǒshì zhēngzhí, bǎochí gǎnqíng lìjiǔmíxīn de jiānshí jīshí.",
                "en": "Across a decades-long marital journey, mutual trust and tolerance are the solid cornerstone resolving daily domestic squabbles and keeping affection fresh.",
                "es": "A lo largo de décadas de matrimonio, la confianza y la tolerancia mutuas son la piedra angular para resolver roces diarios y mantener vivo el amor."
            },
            {
                "id": "#2",
                "hanzi": "社会学学者通过跟踪调查指出，当代青年群体对婚姻制度的认知正从功能性结盟转向精神契合度优先。",
                "pinyin": "Shèhuìxué xuézhě tōngguò gēnzōng diàochá zhǐchū, dāngdài qīngnián qúntǐ duì hūnyīn zhìdù de rènzhī zhèng cóng gōngnéngxìng jiéméng zhuǎnxiàng jīngshén qìhédù yōuxiān.",
                "en": "Sociologists point out via longitudinal surveys that modern youth's perception of marriage is shifting from functional alliance toward spiritual compatibility.",
                "es": "A través de estudios sociológicos, se observa que los jóvenes conciben el matrimonio no como una alianza utilitaria, sino como una afinidad espiritual prioritaria."
            }
        ],
        "collocations": [
            {"hanzi": "婚姻家庭", "en": "marriage and family"},
            {"hanzi": "美满婚姻", "en": "happy / blessed marriage"},
            {"hanzi": "婚姻法", "en": "marriage law"},
            {"hanzi": "走进婚姻", "en": "enter into marriage"},
            {"hanzi": "婚姻危机", "en": "marital crisis"},
            {"hanzi": "包办婚姻", "en": "arranged marriage"}
        ],
        "idioms": [
            {"hanzi": "男婚女嫁", "pinyin": "nán hūn nǚ jià", "meaning_en": "men and women marrying; getting married as a normal part of life"},
            {"hanzi": "千里姻缘", "pinyin": "qiān lǐ yīn yuán", "meaning_en": "romantic affinity bringing people together from a thousand miles apart"},
            {"hanzi": "秦晋之好", "pinyin": "qín jìn zhī hǎo", "meaning_en": "match between two families; firm matrimonial alliance"},
            {"hanzi": "结为连理", "pinyin": "jié wéi lián lǐ", "meaning_en": "join together as intertwining branches; tie the knot"}
        ],
        "character_decomposition": [
            {
                "character": "婚",
                "pinyin": "hūn",
                "meaning_en": "marry; wedding; bridegroom taking bride",
                "meaning_es": "casarse; matrimonio; desposar",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman / bride)",
                "sound_component": "昏 (hūn, dusk/evening wedding rites)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Depicts taking a woman (女) as wife at dusk (昏), the auspicious time for ancient matrimonial rituals.",
                "visual_mnemonic_story_en": "At twilight dusk (昏), the carriage arrives to welcome the bride (女) into her new home.",
                "visual_mnemonic_story_es": "Al caer el crepúsculo (昏), el carruaje llega para recibir a la novia (女) en su nuevo hogar.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VHPA",
                "traditional": '""'
            },
            {
                "character": "姻",
                "pinyin": "yīn",
                "meaning_en": "marriage affinity; in-law relationship",
                "meaning_es": "afinidad matrimonial; lazo por matrimonio",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman, forming kinship ties)",
                "sound_component": "因 (yīn, origin/basis)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing woman (女) with cause/foundation (因), denoting family ties forged through marriage.",
                "visual_mnemonic_story_en": "A woman (女) becomes the source and reason (因) uniting two completely separate families.",
                "visual_mnemonic_story_es": "Una mujer (女) se convierte en el motivo y la causa (因) que entrelaza a dos familias.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VWK",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Taking a bride at twilight dusk (婚) establishes the lifelong family affinity (姻) of sacred marriage.",
            "composite_memory_hook_es": "Celebrar las nupcias al crepúsculo (婚) crea el lazo de afinidad eterna (姻) en el matrimonio.",
            "cultural_and_cognitive_roots": "Both characters bear the woman radical (女); ancient Chinese matrimony merged the bridegroom's home welcoming at dusk ('hūn') with the alliance between two lineages ('yīn'). Thus, 婚姻 represents both emotional bonding and institutional kinship.",
            "tone_sandhi_and_pitch_modulation": "55-55 pitch contour. Both syllables are high level 1st tones (55); maintain an even, sustained pitch without dragging."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "昏", "pinyin": "hūn", "meaning_en": "dusk; faint", "distinction_note": "Lacks the left woman radical 女"},
                {"character": "荤", "pinyin": "hūn", "meaning_en": "meat; pungent food", "distinction_note": "Features grass radical 艹 on top of 军"},
                {"character": "咽", "pinyin": "yān / yàn", "meaning_en": "throat; swallow", "distinction_note": "Has mouth radical 口 on the left instead of 女"},
                {"character": "烟", "pinyin": "yān", "meaning_en": "smoke; cigarette", "distinction_note": "Has fire radical 火 on the left instead of 女"}
            ],
            "etymological_cognates": [
                {"character": "嫁", "pinyin": "jià", "gloss_en": "marry off a daughter"},
                {"character": "娶", "pinyin": "qǔ", "gloss_en": "marry a woman as wife"},
                {"character": "妻", "pinyin": "qī", "gloss_en": "wife in the 女 radical network"},
                {"character": "妇", "pinyin": "fù", "gloss_en": "married woman; matron"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "婚姻 specifically designates the formal institution, legal contract, and marital status of being husband and wife.",
            "contrasts": [
                {"id": "1", "compared_word": "婚姻 vs. 婚礼", "pinyin": "hūnlǐ", "analysis": "婚礼 is the one-time ceremonial wedding celebration or nuptial service, whereas 婚姻 refers to the ongoing institution, contract, and relationship."},
                {"id": "2", "compared_word": "婚姻 vs. 感情", "pinyin": "gǎnqíng", "analysis": "感情 refers to subjective emotional feelings or affection between any persons, whereas 婚姻 is a socially ratified and legalized status."},
                {"id": "3", "compared_word": "婚姻 vs. 恋爱", "pinyin": "liàn'ài", "analysis": "恋爱 denotes romantic courtship and dating before or without marriage, whereas 婚姻 entails civil rights and legal obligations."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "美满的婚姻绝非一劳永逸的誓言，而是两个人共同构筑的避风港。当最初的激情随岁月沉淀，唯有彼此的真诚与体谅，才能在日复一日的平淡琐碎中抵御风雨，让婚姻成为灵魂深处最温暖的依靠。",
                "pinyin": "Měimǎn de hūnyīn jué fēi yíláoyǒngyì de shìyán, érshì liǎng gè rén gòngtóng gòuzhù de bìfēnggǎng. Dāng zuìchū de jīqíng suí suìyuè chéndiàn, wéiyǒu bǐcǐ de zhēnchéng yǔ tǐliàng, cáinǐng zài rìfùyírì de píngdàn suǒsuì zhōng dǐyù fēngyǔ, ràng hūnyīn chéngwéi línghún shēnchù zuì wēnnuǎn de yīkào.",
                "en": "A fulfilling marriage is no one-and-done vow, but a shared haven built by two people. When initial passion settles with years, only sincerity and mutual understanding weather life's storms, making marriage the warmest anchor of the soul.",
                "es": "Un matrimonio pleno no es un juramento estático, sino un refugio edificado entre dos. Cuando la pasión juvenil madura con los años, solo la sinceridad y la comprensión mutua resisten las tormentas, convirtiendo la unión en el ancla más cálida del alma."
            },
            {
                "id": "#2",
                "hanzi": "从法理学视角审视，现代婚姻制度兼具人身伦理属性与重大财产法效力。民法典婚姻家庭编通过完善婚前财产登记与夫妻共同债务认定标准，为保护弱势配偶权益与维护交易安全提供了坚实的制度保障。",
                "pinyin": "Cóng fǎlǐxué shìjiǎo shěnshì, xiàndài hūnyīn zhìdù jiānjù rénshēn lúnlǐ shǔxìng yǔ zhòngdà cáichǎnfǎ xiàolì. Mínfǎdiǎn hūnyīn jiātíng biān tōngguò wánshàn hūnqián cáichǎn dēngjì yǔ fūqī gòngtóng zhàiwù rèndìng biāozhǔn, wèi bǎohù ruòshì pèi'ǒu quányì yǔ wéihù jiāoyì ānquán tígōng le jiānshí de zhìdù bǎozhàng.",
                "en": "From a legal perspective, modern marriage embodies ethical personal relations and significant property rights. The Civil Code protects vulnerable spouses and preserves transaction security through refined premarital asset registration and joint debt standards.",
                "es": "Desde la jurisprudencia, el matrimonio moderno conjuga lazos éticos personales con efectos patrimoniales. El Código Civil protege a los cónyuges vulnerables y garantiza la seguridad jurídica regulando el patrimonio prematrimonial y las deudas comunes."
            }
        ]
    },

    # 14 吵架
    {
        "id": "14",
        "hanzi": "吵架",
        "pinyin": "chǎo jià",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to quarrel; to have a row; to bicker; verbal dispute",
            "es": "pelear; discutir; reñir; tener una discusión acalorada"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Colloquial",
                "definition_en": "to engage in an angry, loud verbal altercation or dispute with someone",
                "definition_es": "sostener una riña o disputa verbal acalorada y en voz alta con alguien",
                "example_phrase": "跟邻居吵架 (quarrel with a neighbor)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "昨天下午因为对周末出游计划意见不合，我和同桌大声吵架，但今天早上我们又笑着和好了。",
                "pinyin": "Zuótiān xiàwǔ yīnwèi duì zhōumò chūyóu jìhuà yìjiàn bù hé, wǒ hé tóngzhuō dàshēng chǎojià, dàn jīntiān zǎoshang wǒmen yòu xiào zhe héhǎo le.",
                "en": "Yesterday afternoon, having differing opinions on weekend outing plans, my deskmate and I had a loud quarrel, but this morning we laughed and reconciled.",
                "es": "Ayer por la tarde, por no ponernos de acuerdo sobre el paseo del fin de semana, mi compañero y yo tuvimos una fuerte discusión, pero esta mañana nos reconciliamos con una sonrisa."
            },
            {
                "id": "#2",
                "hanzi": "人际沟通培训讲师指出，团队成员在方案研讨中就事论事的激烈争论是正常的，但绝不能演化为情绪化的人身攻击与吵架。",
                "pinyin": "Rénjì gōutōng péixùn jiǎngshī zhǐchū, tuánduì chéngyuán zài fāng'àn yántǎo zhōng jiùshìlùnshì de jīliè zhēnglùn shì zhèngcháng de, dàn jué bù néng yǎnhuà wéi qíngxùhuà de rénshēng gōngjī yǔ chǎojià.",
                "en": "The interpersonal communication trainer noted that spirited, objective debate over proposals among team members is healthy, but it must never degenerate into personal bickering.",
                "es": "El instructor de comunicación interpersonal señaló que el debate técnico apasionado es productivo, pero nunca debe degenerar en ataques personales ni discusiones destructivas."
            }
        ],
        "collocations": [
            {"hanzi": "激烈吵架", "en": "quarrel fiercely"},
            {"hanzi": "大吵一架", "en": "have a big row"},
            {"hanzi": "频繁吵架", "en": "quarrel frequently"},
            {"hanzi": "夫妻吵架", "en": "spouses bickering"},
            {"hanzi": "当街吵架", "en": "quarrel in the public street"},
            {"hanzi": "吵架闹别扭", "en": "squabble and give the cold shoulder"}
        ],
        "idioms": [
            {"hanzi": "吵吵闹闹", "pinyin": "chāo chao nào nào", "meaning_en": "noisy and turbulent; constantly squabbling"},
            {"hanzi": "鸡犬不宁", "pinyin": "jī quǎn bù níng", "meaning_en": "even fowls and dogs are disturbed; utterly tumultuous"},
            {"hanzi": "唇枪舌剑", "pinyin": "chún qiāng shé jiàn", "meaning_en": "lips as spears and tongues as swords; fierce war of words"},
            {"hanzi": "各执一词", "pinyin": "gè zhí yì cí", "meaning_en": "each sticks to their own version of the story"}
        ],
        "character_decomposition": [
            {
                "character": "吵",
                "pinyin": "chǎo",
                "meaning_en": "make noise; quarrel; clamor; noisy",
                "meaning_es": "hacer ruido; pelear; discutir; ruidoso",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth, making vocal racket)",
                "sound_component": "少 (shǎo, phonetic match)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing loud mouth (口) with 少 (shǎo), describing noisy verbal squabbling.",
                "visual_mnemonic_story_en": "Opening a loud mouth (口) with small (少) self-restraint creates clamor.",
                "visual_mnemonic_story_es": "Abrir una boca (口) ruidosa con poca (少) prudencia provoca escándalo y disputas.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RFH",
                "traditional": '""'
            },
            {
                "character": "架",
                "pinyin": "jià",
                "meaning_en": "frame; rack; support; fight/brawl",
                "meaning_es": "estante; armazón; pelear; riña",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden timber frame)",
                "sound_component": "加 (jiā, add/impose phonetics)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Depicts assembling wooden timbers (木) by adding (加) them together; extended colloquially to clashing or throwing hands/words in a fight (打架/吵架).",
                "visual_mnemonic_story_en": "Putting together added force (加) over timber stakes (木) builds a fighting posture.",
                "visual_mnemonic_story_es": "Aplicar fuerza adicional (加) sobre estacas de madera (木) levanta una postura de pelea.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "KRD",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Loud, clamoring mouths (吵) locking into a rigid verbal confrontation frame (架) sparks a bitter quarrel.",
            "composite_memory_hook_es": "Bocas ruidosas (吵) que chocan en un forcejeo violento (架) dan lugar a una acalorada pelea verbal.",
            "cultural_and_cognitive_roots": "Chinese vernacular uses 'jià' (frame/scaffolding) metaphorically to describe squaring off in conflict; pairing it with vocal racket ('chǎo') designates verbal fights, contrasting with physical blows ('dǎjià').",
            "tone_sandhi_and_pitch_modulation": "214-51 contour. The 3rd tone of chǎo is pronounced as a half-3rd tone (21 low pitch) when immediately preceding the 4th tone of jià (51)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "抄", "pinyin": "chāo", "meaning_en": "copy; plagiarize", "distinction_note": "Has hand radical 扌 on the left instead of mouth 口"},
                {"character": "秒", "pinyin": "miǎo", "meaning_en": "second (time)", "distinction_note": "Has grain radical 禾 on the left instead of mouth 口"},
                {"character": "驾", "pinyin": "jià", "meaning_en": "drive; harness", "distinction_note": "Features horse radical 马 at the bottom instead of wood 木"},
                {"character": "贺", "pinyin": "hè", "meaning_en": "congratulate", "distinction_note": "Features shell radical 贝 at the bottom instead of wood 木"}
            ],
            "etymological_cognates": [
                {"character": "闹", "pinyin": "nào", "gloss_en": "noisy; make a scene"},
                {"character": "争", "pinyin": "zhēng", "gloss_en": "contend; dispute"},
                {"character": "吵", "pinyin": "chǎo", "gloss_en": "noisy; root morpheme"},
                {"character": "打", "pinyin": "dǎ", "gloss_en": "strike; partner morpheme in 打架"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "吵架 refers specifically to loud, angry, emotional verbal quarreling or bickering between individuals.",
            "contrasts": [
                {"id": "1", "compared_word": "吵架 vs. 争论", "pinyin": "zhēnglùn", "analysis": "争论 refers to intellectual, academic, or professional argumentation where parties debate reasons objectively, whereas 吵架 is emotional venting and shouting."},
                {"id": "2", "compared_word": "吵架 vs. 打架", "pinyin": "dǎjià", "analysis": "吵架 is strictly verbal warfare, whereas 打架 involves physical violence, punching, or brawling."},
                {"id": "3", "compared_word": "吵架 vs. 发生争执", "pinyin": "fāshēng zhēngzhí", "analysis": "发生争执 is a formal, written-register description for experiencing disagreement, while 吵架 is everyday spoken Chinese for shouting matches."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "人与人之间的相处难免会有摩擦，但无休止的吵架只会消耗彼此的情感。真正成熟的沟通，是在情绪翻涌时懂得克制退让，用倾听代替指责。化解矛盾需要的不是争辩输赢，而是理解对方的委屈。",
                "pinyin": "Rén yǔ rén zhījiān de xiāngchǔ nánmiǎn huì yǒu mócā, dàn wúxiūzhǐ de chǎojià zhǐ huì xiāohào bǐcǐ de qínggǎn. Zhēnzhèng chéngshú de gōutōng, shì zài qíngxù fānyǒng shí dǒngdé kèzhì tuìràng, yòng qīngtīng dàitì zhǐzé. Huàjiě máodùn xūyào de bú shì zhēngbiàn shūyíng, érshì lǐjiě duìfāng de wěiqu.",
                "en": "Friction is inevitable among people, but endless quarreling merely drains mutual affection. Mature communication means practicing restraint when emotions surge and listening rather than blaming. Resolving conflict requires understanding, not winning arguments.",
                "es": "Los roces en el trato humano son inevitables, pero pelear sin cesar agota el cariño mutuo. La madurez consiste en contenerse cuando las emociones hierven y escuchar en vez de acusar. Resolver discordias exige comprender los sentimientos del otro."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业团队协作中，将人际吵架与业务研讨严格区分，是保障项目平稳推进的关键组织规则。健康的团队文化鼓励针对技术难点各抒己见，但严禁将业务分歧异化为人身攻击与非理性情绪宣泄。",
                "pinyin": "Zài xiàndài qǐyè tuánduì xiézuò zhōng, jiāng rénjì chǎojià yǔ yèwù yántǎo yángé qūfēn, shì bǎozhàng xiàngmù píngwěn tuījìn de guānjiàn zǔzhī guīzé. Jiànkāng de tuánduì wénhuà gǔlì zhēnduì jìshù nándiǎn gèshūjǐjiàn, dàn yánjìn jiāng yèwù fēnqí yìhuà wéi rénshēng gōngjī yǔ fēilǐxìng qíngxù xuānxiè.",
                "en": "In modern corporate teamwork, strictly demarcating interpersonal bickering from technical deliberation is vital for project advancement. Healthy cultures encourage diverse views on technical hurdles while banning personal attacks and emotional outbursts.",
                "es": "En la colaboración empresarial moderna, separar los altercados personales del debate técnico asegura el avance del proyecto. Una cultura sólida fomenta el debate de ideas pero prohíbe que las discrepancias degeneren en ataques personales."
            }
        ]
    },

    # 15 相敬如宾
    {
        "id": "15",
        "hanzi": "相敬如宾",
        "pinyin": "xiāng jìng rú bīn",
        "part_of_speech": "Idiom",
        "meanings_summary": {
            "en": "(of husband and wife) to respect each other like honored guests; mutual respect in marriage",
            "es": "(entre cónyuges) respetarse mutuamente como huéspedes de honor; respeto conyugal ejemplar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Idiom",
                "register": "Literary",
                "definition_en": "married couples treating each other with the profound courtesy, decorum, and deference due to an honored guest",
                "definition_es": "tratarse los cónyuges con la consideración, reverencia y cortesía debidas a un huésped de honor",
                "example_phrase": "夫妻相敬如宾 (husband and wife respect each other like guests)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这对学者夫妇相伴走过半个世纪的风雨，在日常生活中始终相敬如宾，被后辈学者传为佳话。",
                "pinyin": "Zhè duì xuézhě fūfù xiāngbàn zǒuguò bàn gè shìjì de fēngyǔ, zài rìcháng shēnghuó zhōng shǐzhōng xiāngjìngrúbīn, bèi hòubèi xuézhě chuán wéi jiāhuà.",
                "en": "This scholar couple walked through half a century of trials together, always respecting each other like honored guests in daily life, hailed by younger scholars as an exemplary union.",
                "es": "Este matrimonio de académicos compartió medio siglo de vicisitudes tratándose siempre con mutuo respeto ejemplar, admirados por las nuevas generaciones."
            },
            {
                "id": "#2",
                "hanzi": "中国传统家风研究专家指出，“相敬如宾”不仅是一种婚姻处世哲学，更是维护古代家族制度秩序稳定的伦理基石。",
                "pinyin": "Zhōngguó chuántǒng jiāfēng yánjiū zhuānjiā zhǐchū, “xiāngjìngrúbīn” bùjǐn shì yì zhǒng hūnyīn chǔshì zhéxué, gèng shì wéihù gǔdài jiāzú zhìdù zhìxù wěndìng de lúnlǐ jīshí.",
                "en": "Experts on traditional Chinese family values note that 'respecting each other like guests' is not merely a philosophy of marriage, but an ethical cornerstone ensuring family stability.",
                "es": "Especialistas en tradiciones familiares chinas señalan que respetarse como huéspedes en el matrimonio constituye la base ética de la armonía y estabilidad del hogar."
            }
        ],
        "collocations": [
            {"hanzi": "夫妻相敬如宾", "en": "husband and wife respect each other like guests"},
            {"hanzi": "相敬如宾数十年", "en": "respect each other like guests for decades"},
            {"hanzi": "始终相敬如宾", "en": "remain courteous and respectful like guests throughout"},
            {"hanzi": "相敬如宾的生活", "en": "a life of mutual marital courtesy"},
            {"hanzi": "相敬如宾的相处模式", "en": "a relationship dynamic of mutual deference"},
            {"hanzi": "做到了相敬如宾", "en": "achieved mutual deference in marriage"}
        ],
        "idioms": [
            {"hanzi": "举案齐眉", "pinyin": "jǔ àn qí méi", "meaning_en": "lift the food tray to eyebrow level; exemplary spousal respect and harmony"},
            {"hanzi": "琴瑟和鸣", "pinyin": "qín sè hé míng", "meaning_en": "harmony of zither and lute; blissful marital accord"},
            {"hanzi": "夫唱妇随", "pinyin": "fū chàng fù suí", "meaning_en": "husband and wife in happy harmony"},
            {"hanzi": "白头偕老", "pinyin": "bái tóu xié lǎo", "meaning_en": "live together until white hair; grow old together"}
        ],
        "character_decomposition": [
            {
                "character": "相",
                "pinyin": "xiāng",
                "meaning_en": "mutually; each other",
                "meaning_es": "mutuamente; el uno al otro",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye looking) + 木 (tree/target observed)",
                "sound_component": "木 (phonetic association)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Depicts an eye (目) carefully examining a tree (木), extended to mutually gazing and interacting.",
                "visual_mnemonic_story_en": "An eye (目) looks across at a slender tree (木), symbolizing mutual observation.",
                "visual_mnemonic_story_es": "Un ojo (目) contempla un árbol (木), reflejando una interacción y mirada mutua.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DUB",
                "traditional": '""'
            },
            {
                "character": "敬",
                "pinyin": "jìng",
                "meaning_en": "respect; honor; revere",
                "meaning_es": "respetar; venerar; honrar",
                "radical": "攵",
                "radical_meaning_en": "strike / action",
                "meaning_component": "攵 (disciplined action)",
                "sound_component": "苟 (jìng, alert posture)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Depicts adopting an alert, humble stance (苟) under self-discipline (攵), denoting reverence.",
                "visual_mnemonic_story_en": "Under self-discipline (攵), one bows attentively with profound respect (敬).",
                "visual_mnemonic_story_es": "Con autocontrol sereno (攵), uno se inclina mostrando respeto y reverencia.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "TKOK",
                "traditional": '""'
            },
            {
                "character": "如",
                "pinyin": "rú",
                "meaning_en": "as if; like; similar to",
                "meaning_es": "como; al igual que; semejante a",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman / harmony)",
                "sound_component": "口 (mouth)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram of speech (口) complying harmoniously with instruction (女), signifying 'like' or 'accordance'.",
                "visual_mnemonic_story_en": "Speaking from the mouth (口) with the graceful compliance of a lady (女) makes actions resemble words.",
                "visual_mnemonic_story_es": "Expresarse desde la boca (口) con elegancia (女) asegura que todo transcurra conforme a lo debido.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "VR",
                "traditional": '""'
            },
            {
                "character": "宾",
                "pinyin": "bīn",
                "meaning_en": "guest; visitor; receive with honor",
                "meaning_es": "huésped; invitado de honor",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (hall/mansion welcoming guests)",
                "sound_component": "兵 / 贝 (bīn, precious gift exchange)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Depicts a guest welcomed under the roof (宀) presented with gifts of cowrie shells (贝).",
                "visual_mnemonic_story_en": "Under the mansion roof (宀), gifts are exchanged to honor the arriving guest (宾).",
                "visual_mnemonic_story_es": "Bajo el techo señorial (宀), se ofrecen presentes para agasajar al huésped de honor (宾).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JOMC",
                "traditional": "賓"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Treating each other (相) with solemn reverence (敬) just as (如) one honors an esteemed guest (宾) defines matrimonial decorum.",
            "composite_memory_hook_es": "Tratarse mutuamente (相) con profundo respeto (敬) igual que (如) a un huésped distinguido (宾) define la virtud matrimonial.",
            "cultural_and_cognitive_roots": "Originating in the Spring and Autumn Annals (左传·僖公三十三年), when Xi Que and his wife were observed weeding fields together with mutual courtesy like honoring an imperial guest. It became the highest traditional ideal of marital decorum without excessive casualness.",
            "tone_sandhi_and_pitch_modulation": "55-51-35-55 pitch pattern. Articulate four balanced syllables with distinct high level (55), falling (51), rising (35), and high level (55) contours."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "警", "pinyin": "jǐng", "meaning_en": "warn; police", "distinction_note": "Features 言 (speech) at the bottom instead of 攵 alone"},
                {"character": "惊", "pinyin": "jīng", "meaning_en": "startle; surprise", "distinction_note": "Has heart radical 忄 on the left with 京"},
                {"character": "滨", "pinyin": "bīn", "meaning_en": "shore; coast", "distinction_note": "Has water radical 氵 on the left side of 宾"},
                {"character": "摈", "pinyin": "bìn", "meaning_en": "discard; reject", "distinction_note": "Has hand radical 扌 on the left side of 宾"}
            ],
            "etymological_cognates": [
                {"character": "礼", "pinyin": "lǐ", "gloss_en": "ritual propriety; decorum"},
                {"character": "客", "pinyin": "kè", "gloss_en": "guest; visitor under the roof radical"},
                {"character": "待", "pinyin": "dài", "gloss_en": "treat; receive guests"},
                {"character": "尊", "pinyin": "zūn", "gloss_en": "revere; honor with wine vessel"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "相敬如宾 specifically characterizes married couples treating one another with dignified courtesy, mutual deference, and unflagging decorum.",
            "contrasts": [
                {"id": "1", "compared_word": "相敬如宾 vs. 举案齐眉", "pinyin": "jǔ'ànqíméi", "analysis": "Both describe marital respect, but 举案齐眉 historically highlighted the wife's dutiful deference to the husband, whereas 相敬如宾 emphasizes symmetrical, mutual respect between both partners."},
                {"id": "2", "compared_word": "相敬如宾 vs. 恩爱如初", "pinyin": "ēn'àirúchū", "analysis": "恩爱如初 emphasizes the undiminished emotional passion and affection of early romance, while 相敬如宾 emphasizes polite restraint, decorum, and mutual reverence."},
                {"id": "3", "compared_word": "相敬如宾 vs. 亲密无间", "pinyin": "qīnmìwújiàn", "analysis": "亲密无间 denotes boundless casual intimacy without formalities, whereas 相敬如宾 maintains a respectful, courteous boundary to avoid domestic contempt."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古人将相敬如宾视为夫妻相处的最高境界。爱情最初由激情点燃，但要在数十年的柴米油盐中免于厌倦，唯有以礼相待。将伴侣视作尊贵的宾客，言语有度，举止有礼，才能让婚姻在岁月流转中沉淀出温润的优雅。",
                "pinyin": "Zhōngguó gǔrén jiāng xiāngjìngrúbīn shìwéi fūqī xiāngchǔ de zuìgāo jìngjiè. Àiqíng zuìchū yóu jīqíng diǎnrán, dàn yào zài shù shí nián de cháimǐyóuyán zhōng miǎnyú yànjuàn, wéiyǒu yǐ lǐ xiāng dài. Jiāng bànlǚ shìzuò zūnguì de bīnkè, yányǔ yǒudù, jǔzhǐ yǒulǐ, cáinǐng ràng hūnyīn zài suìyuè liúzhuǎn zhōng chéndiàn chū wēnrùn de yōuyǎ.",
                "en": "Ancient Chinese regarded mutual respect like guests as the summit of matrimony. Passion kindles love, but avoiding domestic weariness over decades requires courtesy. Treating your partner as an honored guest allows marriage to distill gentle elegance over time.",
                "es": "Los antiguos concebían el respeto mutuo como la cúspide conyugal. La pasión enciende el amor, pero para sortear el tedio cotidiano durante décadas se precisa cortesía. Considerar al cónyuge como un huésped de honor destila una serena elegancia matrimonial."
            },
            {
                "id": "#2",
                "hanzi": "在现代文化语境中，相敬如宾这一传统成语常被赋予关于婚姻边界感的新内涵。现代家庭咨询顾问指出，过度亲昵往往容易模糊彼此的心理界限，引发不必要的控制欲。保持如宾客般的相互尊重与独立空间，是构建健康伙伴式婚姻的重要法则。",
                "pinyin": "Zài xiàndài wénhuà yǔjìng zhōng, xiāngjìngrúbīn zhè yì chuántǒng chéngyǔ cháng bèi fùyǔ guānyú hūnyīn biānjiègǎn de xīn nèihán. Xiàndài jiātíng zīxún gùwèn zhǐchū, guòdù qīnnì wǎngwǎng róngyì móhu bǐcǐ de xīnlǐ jièxiàn, yǐnfā búbìyào de kòngzhìyù. Bǎochí rú bīnkè bān de xiānghù zūnzhòng yǔ dúlì kōngjiān, shì gòujiàn jiànkāng huǒbànshì hūnyīn de zhòngyào fǎzé.",
                "en": "In contemporary contexts, respecting each other like guests gains new meaning around marital psychological boundaries. Counselors note that unchecked familiarity blurs boundaries and fuels possessiveness. Preserving courteous space is a vital rule for healthy partnership marriage.",
                "es": "En la psicología contemporánea, respetarse como huéspedes cobra nuevo sentido sobre los límites personales en la pareja. La excesiva confianza borra las fronteras afectivas y alienta el afán de control. Mantener un espacio de respeto mutuo forja una convivencia sana y equilibrada."
            }
        ]
    }
]

if __name__ == '__main__':
    for w in words_batch3:
        save_word(w)

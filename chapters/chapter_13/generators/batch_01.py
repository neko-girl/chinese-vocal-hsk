# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 锯子
    {
        "id": "1",
        "hanzi": "锯子",
        "pinyin": "jù zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "saw (tool); hand saw",
            "es": "sierra; serrucho"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a cutting tool consisting of a toothed blade operated by hand or machine",
                "definition_es": "herramienta para cortar madera u otros materiales compuesta por una hoja dentada",
                "example_phrase": "一把锋利的锯子 (a sharp hand saw)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老木匠熟练地拿起锯子，顺着墨线几下就把坚硬的红木板整齐地锯开了。",
                "pinyin": "Lǎo mùjiang shúliàn de ná qǐ jùzi, shùnzhe mòxiàn jǐ xià jiù bǎ jiānyìng de hóngmù bǎn zhěngqí de jù kāi le.",
                "en": "The veteran carpenter skillfully picked up the saw and neatly cut through the hard mahogany board along the marked ink line in just a few strokes.",
                "es": "El viejo carpintero tomó con destreza la sierra y, siguiendo la línea de tinta, cortó con pulcritud la dura tabla de caoba en pocos pases."
            },
            {
                "id": "#2",
                "hanzi": "在现代建筑工地上，传统的简易锯子已经被高效精准的电动切割机所取代。",
                "pinyin": "Zài xiàndài jiànzhù gōngdì shang, chuántǒng de jiǎnyì jùzi yǐjīng bèi gāoxiào jīngzhǔn de diàndòng qiēgējī suǒ qǔdài.",
                "en": "On modern construction sites, traditional simple saws have largely been replaced by highly efficient and precise electric cutting machines.",
                "es": "En las obras de construcción modernas, las sierras manuales tradicionales han sido sustituidas por cortadoras eléctricas de gran eficiencia y precisión."
            }
        ],
        "collocations": [
            {"hanzi": "用锯子锯断", "en": "saw through with a saw"},
            {"hanzi": "一把锯子", "en": "a saw (classifier 把)"},
            {"hanzi": "木工锯子", "en": "woodworking saw"},
            {"hanzi": "钢锯子", "en": "hacksaw"},
            {"hanzi": "拉锯子", "en": "pull a saw back and forth"},
            {"hanzi": "锋利的锯子", "en": "sharp saw"}
        ],
        "idioms": [
            {"hanzi": "锯齿齿", "pinyin": "jù chǐ chǐ", "meaning_en": "jagged like saw teeth; serrated"},
            {"hanzi": "笨口拙舌", "pinyin": "bèn kǒu zhuō shé", "meaning_en": "clumsy in speech; tongue-tied like a stuck saw"},
            {"hanzi": "斧锯齐下", "pinyin": "fǔ jù qí xià", "meaning_en": "axes and saws striking together; forceful radical overhaul"},
            {"hanzi": "刻舟求剑", "pinyin": "kè zhōu qiú jiàn", "meaning_en": "notching boat to find fallen sword; rigid outdated methods"}
        ],
        "character_decomposition": [
            {
                "character": "锯",
                "pinyin": "jù",
                "meaning_en": "saw; to saw; cut with a saw",
                "meaning_es": "sierra; serrar; cortar con sierra",
                "radical": "钅",
                "radical_meaning_en": "metal / gold",
                "meaning_component": "钅 (metal blade)",
                "sound_component": "居 (jū / phonetic)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Metal radical 钅 paired with 居; legend says Lu Ban observed serrated grass leaves cutting fingers and invented the iron saw blade.",
                "visual_mnemonic_story_en": "Lu Ban forged a strip of sharp metal (钅) with serrated teeth to slice wood where timber settled (居).",
                "visual_mnemonic_story_es": "Lu Ban forjó una hoja de metal (钅) con dientes afilados para cortar maderos donde se asentaban (居).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OPRJR",
                "traditional": "鋸"
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; child; son",
                "meaning_es": "sufijo sustantivo; hijo; crío",
                "radical": "子",
                "radical_meaning_en": "child / son",
                "meaning_component": "pictograph of swaddled infant",
                "sound_component": "子 (zǐ)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph depicting an infant with outstretched arms, serving here as a productive nominal suffix.",
                "visual_mnemonic_story_en": "An infant waving little arms (子), attached here to tool names to form common nouns.",
                "visual_mnemonic_story_es": "Un bebé con brazos abiertos (子), añadido a nombres de herramientas como sufijo nominal.",
                "tone_mnemonic_anchor": "neutral",
                "cangjie": "ND",
                "traditional": "子"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A toothed metal (钅) blade attached to a wooden handle forms a trusty saw (锯子).",
            "composite_memory_hook_es": "Una hoja metálica (钅) dentada convertida en herramienta básica constituye una sierra (锯子).",
            "cultural_and_cognitive_roots": "Attributed to master craftsman Lu Ban in the Warring States period, inspired by jagged mountain weeds cutting skin.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by neutral tone: 'jù zi' (51-neutral). Sharp descending drop on 'jù' followed by light, unstressed 'zi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "锯", "pinyin": "jù", "meaning_en": "saw", "distinction_note": "Contains metal radical 钅 with 居"},
                {"character": "据", "pinyin": "jù", "meaning_en": "according to; seize", "distinction_note": "Contains hand radical 扌 instead of 钅"},
                {"character": "剧", "pinyin": "jù", "meaning_en": "theatrical drama; acute", "distinction_note": "Contains knife radical 刂 on the right"},
                {"character": "裾", "pinyin": "jū", "meaning_en": "hem of garment", "distinction_note": "Contains clothing radical 衤 on the left"}
            ],
            "etymological_cognates": [
                {"character": "斧", "pinyin": "fǔ", "gloss_en": "axe; hatchet"},
                {"character": "刨", "pinyin": "bào", "gloss_en": "plane (carpentry tool)"},
                {"character": "凿", "pinyin": "záo", "gloss_en": "chisel; bore"},
                {"character": "铲", "pinyin": "chǎn", "gloss_en": "shovel; trowel"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "锯子 specifically denotes a serrated pull-or-push toothed sawing tool, unlike impact or slicing blades.",
            "contrasts": [
                {"id": 1, "compared_word": "锯子 vs. 斧头", "pinyin": "fǔtou", "analysis": "斧头 splits heavy lumber using downward chopping impact force, whereas 锯子 cuts linearly using repetitive back-and-forth friction."},
                {"id": 2, "compared_word": "锯子 vs. 刀子", "pinyin": "dāozi", "analysis": "刀子 has a continuous smooth cutting edge suited for carving, whereas 锯子 has serrated teeth for abrading hard timber."},
                {"id": 3, "compared_word": "锯子 vs. 剪刀", "pinyin": "jiǎndāo", "analysis": "剪刀 works through double-blade shearing of flexible fabrics or thin sheets, while 锯子 removes dust Kerf from rigid materials."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "相传古代工匠鲁班在陡峭的山上采集木料时，手指不慎被一种边缘带齿的野草割破。他深受启发，经过反复摸索试验，用铁片打制出带有密密麻麻细齿的锯子，大幅提高了伐木与建筑的作业效率。",
                "pinyin": "Xiāngchuán gǔdài gōngjiàng Lǔ Bān zài dǒuqiào de shān shang cǎijí mùliào shí, shǒuzhǐ búshèn bèi yī zhǒng biānyuán dài chǐ de yěcǎo gēpò. Tā shēn shòu qǐfā, jīngguò fǎnfù mōsuǒ shìyàn, yòng tiěpiàn dǎzhì chū dài yǒu mìmimámá xìchǐ de jùzi, dàfú tígāo le fámù yǔ jiànzhù de zuòyè xiàolǜ.",
                "en": "Legend tells that when ancient master craftsman Lu Ban was cutting timber on a steep mountain, his finger was cut by wild serrated grass. Deeply inspired, he hammered iron into toothed saws, dramatically boosting carpentry productivity.",
                "es": "Cuenta la leyenda que el célebre artesano Lu Ban, cortando madera en el monte, se hirió con una hierba de bordes dentados. Inspirado por ello, forjó sierras de hierro dentadas, elevando enormemente la eficiencia constructiva."
            },
            {
                "id": "#2",
                "hanzi": "在早期篮球运动刚刚创立的阶段，人们直接把盛装桃子的竹筐钉在体育馆两端的栏杆上。每次投篮得分之后，工作人员都必须搬来高高的梯子爬上去把球取出，比赛过程因此变得断断续续。直到有人找来锯子直接锯开筐底，才彻底化繁为简。",
                "pinyin": "Zài zǎoqī lánqiú yùndòng gānggāng chuànglì de jiēduàn, rénmen zhíjiē bǎ chéngzhuāng táozi de zhúkuāng dīng zài tǐyùguǎn liǎngduān de lángān shang. Měicì tóulán défēn zhīhòu, gōngzuò rényuán dōu bìxū bān lái gāogāo de tīzi pá shàngqu bǎ qiú qǔchū, bǐsài guòchéng yīncǐ biàn de duànduàn-xùxù. Zhídào yǒurén zhǎolái jùzi zhíjiē jù kāi kuāngdǐ, cái chèdǐ huà fán wéi jiǎn.",
                "en": "During the early beginnings of basketball, peach baskets were nailed onto gymnasium railings. Every time a basket was made, staff had to haul tall ladders to retrieve the ball, interrupting the game. Only when someone brought a saw to cut off the bottom did the solution simplify.",
                "es": "En los albores del baloncesto, se clavaban cestas de melocotón en las barandillas. Tras cada canasta, un auxiliar debía trepar a una escalera para extraer el balón, cortando el ritmo. Bastó usar una sierra para cortar el fondo y simplificarlo todo."
            }
        ]
    },

    # 02 筐
    {
        "id": "2",
        "hanzi": "筐",
        "pinyin": "kuāng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "basket (open woven container)",
            "es": "cesta; canasta; cesto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a container woven from split bamboo, wicker, or rattan used for carrying produce or objects",
                "definition_es": "recipiente tejido de tiras de bambú, mimbre o caña para transportar productos u objetos",
                "example_phrase": "装满新鲜果子的竹筐 (a bamboo basket filled with fresh fruit)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "果农们天不亮就挑着沉甸甸的竹筐赶往集市，筐里装满了刚采摘下来的水蜜桃。",
                "pinyin": "Guǒnóngmen tiān bú liàng jiù tiāo zhe chéndiāndiān de zhúkuāng gǎnwǎng jíshì, kuāng lǐ zhuāngmǎn le gāng cǎizhāi xiàlái de shuǐmìtáo.",
                "en": "Before daybreak, fruit farmers carried heavy bamboo baskets on shoulder poles to the market, the baskets filled with freshly picked juicy peaches.",
                "es": "Antes del amanecer, los fruticultores cargaban pesadas cestas de bambú camino al mercado, colmadas de melocotones recién cosechados."
            },
            {
                "id": "#2",
                "hanzi": "最初发明篮球时，奈史密斯博士把两只装桃子的圆筐挂在墙头作为球门。",
                "pinyin": "Zuìchū fāmíng lánqiú shí, Nàishǐmīsī bóshì bǎ liǎng zhī zhuāng táozi de yuánkuāng guà zài qiángtóu zuòwéi qiúmén.",
                "en": "When basketball was first invented, Dr. Naismith hung two round peach baskets on the walls to serve as goals.",
                "es": "Al inventar el baloncesto, el doctor Naismith colgó dos cestas redondas de melocotones en la pared a modo de metas."
            }
        ],
        "collocations": [
            {"hanzi": "竹筐", "en": "bamboo basket"},
            {"hanzi": "一个筐", "en": "a basket (classifier 个)"},
            {"hanzi": "筐底", "en": "bottom of a basket"},
            {"hanzi": "菜筐", "en": "vegetable basket"},
            {"hanzi": "果筐", "en": "fruit basket"},
            {"hanzi": "装筐", "en": "pack into a basket"}
        ],
        "idioms": [
            {"hanzi": "一筐倾尽", "pinyin": "yī kuāng qīng jìn", "meaning_en": "pour out an entire basket; give all one's resources"},
            {"hanzi": "竹篮打水", "pinyin": "zhú lán dǎ shuǐ", "meaning_en": "drawing water with a bamboo basket; all in vain"},
            {"hanzi": "同舟共济", "pinyin": "tóng zhōu gòng jì", "meaning_en": "cross the river in the same boat; cooperate in adversity"},
            {"hanzi": "满载而归", "pinyin": "mǎn zài ér guī", "meaning_en": "return with a full load; come back richly rewarded"}
        ],
        "character_decomposition": [
            {
                "character": "筐",
                "pinyin": "kuāng",
                "meaning_en": "basket",
                "meaning_es": "cesta; canasto",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo weave)",
                "sound_component": "匡 (kuāng / frame; phonetic)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Bamboo radical 竹 on top over frame 匡; traditionally woven with interlocking bamboo splits inside a rectangular or round frame.",
                "visual_mnemonic_story_en": "Strips of flexible bamboo (竹) woven inside a sturdy wooden frame (匡) create a spacious farm basket (筐).",
                "visual_mnemonic_story_es": "Tiras de bambú (竹) entrelazadas en un bastidor resistente (匡) conforman una espaciosa canasta (筐).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "HSMG",
                "traditional": "筐"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Bamboo (竹) strips woven into a protective rectangular frame (匡) become a carrying basket (筐).",
            "composite_memory_hook_es": "Tiras de bambú (竹) entretejidas sobre un armazón (匡) forman una práctica cesta de carga (筐).",
            "cultural_and_cognitive_roots": "Essential harvest container throughout Chinese agrarian history, woven from resilient southern bamboo.",
            "tone_sandhi_and_pitch_modulation": "High flat level tone: 'kuāng' (55). Maintain a sustained, resonant high-pitch ring without dropping."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "筐", "pinyin": "kuāng", "meaning_en": "basket", "distinction_note": "Has bamboo radical 竹 on top"},
                {"character": "匡", "pinyin": "kuāng", "meaning_en": "frame; rectify", "distinction_note": "Base character without bamboo radical"},
                {"character": "框", "pinyin": "kuàng", "meaning_en": "frame; casement", "distinction_note": "Has tree/wood radical 木 on the left"},
                {"character": "眶", "pinyin": "kuàng", "meaning_en": "eye socket", "distinction_note": "Has eye radical 目 on the left"}
            ],
            "etymological_cognates": [
                {"character": "篮", "pinyin": "lán", "gloss_en": "basket with handle"},
                {"character": "篓", "pinyin": "lǒu", "gloss_en": "tall wicker hamper"},
                {"character": "箱", "pinyin": "xiāng", "gloss_en": "box; chest"},
                {"character": "笼", "pinyin": "lóng", "gloss_en": "cage; steamer basket"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "筐 is typically a wide, lidless basket woven of bamboo or wicker, primarily used for coarse farm produce.",
            "contrasts": [
                {"id": 1, "compared_word": "筐 vs. 篮子", "pinyin": "lánzi", "analysis": "篮子 usually has an arching handle for carrying personal purchases, whereas 筐 is larger and carried with shoulder poles."},
                {"id": 2, "compared_word": "筐 vs. 箱子", "pinyin": "xiāngzi", "analysis": "箱子 denotes a rigid rectangular trunk or box with walls and a closing lid, unlike the open breathable weave of 筐."},
                {"id": 3, "compared_word": "筐 vs. 桶", "pinyin": "tǒng", "analysis": "桶 is a watertight wooden or plastic bucket for liquids, whereas 筐 has a porous woven mesh unfit for liquids."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "深秋时节的山村果园里，红彤彤的苹果压弯了枝头。乡亲们手脚麻利地将采摘下来的鲜果整齐码放进竹筐中，欢声笑语伴随着丰收的喜悦，在漫山遍野的清脆鸟鸣声中久久回荡。",
                "pinyin": "Shēnqiū shíjié de shāncūn guǒyuán lǐ, hóngtóngtóng de píngguǒ yāwān le zhītóu. Xiāngqīnmen shǒujiǎo málì de jiāng cǎizhāi xiàlái de xiānguǒ zhěngqí mǎfàng jìn zhúkuāng zhōng, huānshēng-xiàoyǔ bànsuí zhe fēngshōu de xǐyuè, zài mànshān-biànyě de qīngcuì niǎomíng shēng zhōng jiǔjiǔ huídàng.",
                "en": "In late autumn mountain orchards, crimson apples bent the branches. Villagers swiftly arranged freshly gathered fruit into bamboo baskets, their laughter and harvest joy echoing alongside crisp birdsong across the hills.",
                "es": "En los huertos serranos a finales de otoño, las manzanas doblaban las ramas. Con presteza, los lugareños acomodaban la fruta en cestas de bambú, resonando sus risas y júbilo por doquier entre trinos campestres."
            },
            {
                "id": "#2",
                "hanzi": "当年在马萨诸塞州的春田学院，体育教师由于缺乏室内器械，便就地取材把两个盛桃的竹筐固定在离地十英尺的高处。这个不起眼的果筐，不仅成为了现代篮球运动的摇篮，也见证了体育规则在实践中的不断创新与完善。",
                "pinyin": "Dāngnián zài Mǎsàzhūsuāi zhōu de Chūntián xuéyuàn, tǐyù jiàoshī yóuyú quēfá shìnèi qìxiè, biàn jiùdì-qǔcái bǎ liǎng ge chéng táo de zhúkuāng gùdìng zài lí dì shí yīngchǐ de gāochù. Zhè ge bùqǐyǎn de guǒkuāng, bùjǐn chéngwéi le xiàndài lánqiú yùndòng de yáolán, yě jiànzhèng le tǐyù guīzé zài shíjiàn zhōng de búduàn chuàngxīn yǔ wánshàn.",
                "en": "Back then at Springfield College in Massachusetts, a gym teacher lacking indoor equipment attached two peach baskets ten feet off the ground. That humble basket not only cradled modern basketball but witnessed sports rules constantly evolving through practice.",
                "es": "En el Springfield College de Massachusetts, un profesor sin material colgó dos cestas de melocotón a diez pies de altura. Esa humilde cesta fue la cuna del baloncesto moderno y testigo de la evolución de sus reglas."
            }
        ]
    },

    # 03 训练
    {
        "id": "3",
        "hanzi": "训练",
        "pinyin": "xùn liàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to train; to drill; training",
            "es": "entrenar; adiestrar; entrenamiento; adiestramiento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to instruct and exercise repeatedly to acquire physical skills or professional discipline",
                "definition_es": "instruir y ejercitar metódicamente para adquirir habilidades físicas o disciplina profesional",
                "example_phrase": "严格训练队员 (strictly train team members)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "systematic physical or mental instruction and practice",
                "definition_es": "serie de ejercicios sistemáticos de preparación física o técnica",
                "example_phrase": "高强度的体能训练 (high-intensity physical conditioning)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了在下个月的校际运动会上夺冠，长跑队队员们每天清晨都坚持进行五公里耐力训练。",
                "pinyin": "Wèile zài xià ge yuè de xiàojì yùndònghuì shang duóguàn, chángpǎoduì duìyuánmen měitiān qīngchén dōu jiānchí jìnxíng wǔ gōnglǐ nàilì xùnliàn.",
                "en": "To win the championship at next month's interschool athletic meet, the long-distance runners persisted in five-kilometer endurance training every dawn.",
                "es": "Para alzarse con el título en el torneo interescolar del mes próximo, los fondistas realizaban cada alba un entrenamiento de resistencia de cinco kilómetros."
            },
            {
                "id": "#2",
                "hanzi": "新员工入职之后必须接受为期三周的系统技能培训与职业素养考核。",
                "pinyin": "Xīn yuángōng rùzhí zhīhòu bìxū jiēshòu wéiqī sān zhōu de xìtǒng jìnéng péixùn yǔ zhíyè sùyǎng kǎohé.",
                "en": "After joining, new employees must undergo three weeks of systematic technical training and professional competency assessments.",
                "es": "Tras incorporarse, los nuevos empleados deben completar tres semanas de capacitación técnica sistemática y evaluación de competencias profesionales."
            }
        ],
        "collocations": [
            {"hanzi": "严格训练", "en": "strict training / drill"},
            {"hanzi": "军事训练", "en": "military training"},
            {"hanzi": "体能训练", "en": "physical fitness conditioning"},
            {"hanzi": "训练有素", "en": "well-trained; seasoned"},
            {"hanzi": "训练基地", "en": "training camp / base"},
            {"hanzi": "接受训练", "en": "undergo training"}
        ],
        "idioms": [
            {"hanzi": "训练有素", "pinyin": "xùn liàn yǒu sù", "meaning_en": "well-drilled; rigorously prepared through long training"},
            {"hanzi": "熟能生巧", "pinyin": "shú néng shēng qiǎo", "meaning_en": "practice makes perfect; skill comes from practice"},
            {"hanzi": "厉兵秣马", "pinyin": "lì bīng mò mǎ", "meaning_en": "whet weapons and feed horses; prepare intensively for battle"},
            {"hanzi": "刻苦耐劳", "pinyin": "kè kǔ nài láo", "meaning_en": "endure hardships through tireless persevering effort"}
        ],
        "character_decomposition": [
            {
                "character": "训",
                "pinyin": "xùn",
                "meaning_en": "teach; instruct; admonish",
                "meaning_es": "instruir; amaestrar; adoctrinar",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken instruction)",
                "sound_component": "川 (chuān / flow; phonetic)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Speech radical 讠 with river stream 川; originally guiding words to flow smoothly into understanding like smooth waterways.",
                "visual_mnemonic_story_en": "Spoken instructions (讠) flow continuously like a river (川) into learners' minds to train their conduct (训).",
                "visual_mnemonic_story_es": "Las palabras didácticas (讠) fluyen como un río (川) hacia la mente del aprendiz guiando su conducta (训).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVLL",
                "traditional": "訓"
            },
            {
                "character": "练",
                "pinyin": "liàn",
                "meaning_en": "practice; drill; refine",
                "meaning_es": "practicar; ejercitar; curtir",
                "radical": "纟",
                "radical_meaning_en": "silk thread",
                "meaning_component": "纟 (raw silk threads)",
                "sound_component": "东 / 练 (phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk radical 纟 beside 练; originally boiling and beating raw coarse silk repeatedly to make it white and supple.",
                "visual_mnemonic_story_en": "Rough silk fibers (纟) washed and boiled repeatedly under the eastern sun until perfected through practice (练).",
                "visual_mnemonic_story_es": "Hebras de seda (纟) lavadas y hervidas una y otra vez bajo el sol oriental hasta purificarse mediante la práctica (练).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMDF",
                "traditional": "練"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Guiding words (训) combined with repetitive silk-like conditioning (练) produce thorough mastery (训练).",
            "composite_memory_hook_es": "La instrucción verbal (训) combinada con el pulido repetitivo como seda (练) forja el verdadero adiestramiento (训练).",
            "cultural_and_cognitive_roots": "Derives from ancient martial drills and silk purification metaphors where raw fiber is transformed into strong fabric.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'xùn liàn' (51-51). Execute two decisive down-slopes without rushing."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "训", "pinyin": "xùn", "meaning_en": "train; instruct", "distinction_note": "Speech radical 讠 with 川"},
                {"character": "圳", "pinyin": "zhèn", "meaning_en": "furrow; ditch", "distinction_note": "Earth radical 土 with 川 (e.g. 深圳)"},
                {"character": "练", "pinyin": "liàn", "meaning_en": "practice", "distinction_note": "Silk radical 纟 on the left"},
                {"character": "炼", "pinyin": "liàn", "meaning_en": "smelt metals; refine", "distinction_note": "Fire radical 火 on the left"}
            ],
            "etymological_cognates": [
                {"character": "演", "pinyin": "yǎn", "gloss_en": "drill; perform; evolve"},
                {"character": "习", "pinyin": "xí", "gloss_en": "practice; flap wings"},
                {"character": "操", "pinyin": "cāo", "gloss_en": "operate; drill"},
                {"character": "修", "pinyin": "xiū", "gloss_en": "cultivate; mend"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "训练 emphasizes systematic physical, behavioral, or tactical drill to achieve peak execution under pressure.",
            "contrasts": [
                {"id": 1, "compared_word": "训练 vs. 练习", "pinyin": "liànxí", "analysis": "练习 refers to general self-study practice exercises, whereas 训练 entails structured external coaching and discipline."},
                {"id": 2, "compared_word": "训练 vs. 培养", "pinyin": "péiyǎng", "analysis": "培养 focuses on long-term nurturing of character, habits, or talent over years, while 训练 targets specific motor and tactical drills."},
                {"id": 3, "compared_word": "训练 vs. 锻炼", "pinyin": "duànliàn", "analysis": "锻炼 denotes personal health fitness workout or undergoing hardship, whereas 训练 targets specific competitive standards."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "寒冬腊月里的训练基地格外安静，队员们却早已汗流浃背。教练一遍又一遍地拆解战术动作，纠正每一个细小的传球失误。正是在这种千百次枯燥重复的刻苦训练中，队伍培养出了默契与坚不可摧的团队意志。",
                "pinyin": "Hándōng-làyuè lǐ de xùnliàn jīdì géwài ānjìng, duìyuánmen què zǎoyǐ hànliújiābèi. Jiàoliàn yí biàn yòu yí biàn de chāijiě zhànshù dòngzuò, jiūzhèng měi yí ge xìxiǎo de chuánqiú shīwù. Zhèng shì zài zhè zhǒng qiānbǎicì kūzào chóngfù de kèkǔ xùnliàn zhōng, duìwù péiyǎng chū le mòqì yǔ jiānbùkěcuī de tuánduì yìzhì.",
                "en": "The training base was quiet in the bitter winter, yet the players were already drenched in sweat. The coach dismantled tactical movements repeatedly, correcting small passing errors. Through this grueling repetition, the team forged chemistry and indomitable will.",
                "es": "La base deportiva permanecía en silencio en el crudo invierno, mas los jugadores sudaban a mares. El entrenador desgranaba las tácticas corrigiendo cada pase. En esa ardua repetición, el equipo forjó compenetración y temple inquebrantable."
            },
            {
                "id": "#2",
                "hanzi": "当年奈史密斯发明篮球运动的初衷，正是为了在漫长寒冷的冬季为学生提供一种无需面对面激烈冲撞的室内体能训练方式。然而随着时代发展，现代篮球训练对运动员的速度、爆发力及战术素养提出了更为严苛的综合要求。",
                "pinyin": "Dāngnián Nàishǐmīsī fāmíng lánqiú yùndòng de chūzhōng, zhèng shì wèile zài màncháng hánlěng de dōngjì wèi xuésheng tígōng yī zhǒng wúxū miànduìmiàn jīliè chōngzhuàng de shìnèi tǐnéng xùnliàn fāngshì. Rán'ér suízhe shídài fāzhǎn, xiàndài lánqiú xùnliàn duì yùndòngyuán de sùdù, bàofālì jí zhànshù sùyǎng tíchū le gèng wéi yánkē de zōnghé yāoqiú.",
                "en": "Naismith's original intention was to provide students with an indoor conditioning method free from violent collisions during harsh winters. As eras shifted, modern basketball training has raised demanding standards for speed, explosive power, and tactical prowess.",
                "es": "Naismith concibió el baloncesto para dotar a los alumnos de entrenamiento bajo techo sin colisiones bruscas durante el crudo invierno. No obstante, el entrenamiento actual exige una velocidad, potencia explosiva y lectura táctica superlativas."
            }
        ]
    },

    # 04 缺乏
    {
        "id": "4",
        "hanzi": "缺乏",
        "pinyin": "quē fá",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to lack; to be deficient in; shortage",
            "es": "carecer de; faltar; escasear; deficiencia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to not have enough of something necessary (resources, experience, vitality, or confidence)",
                "definition_es": "no disponer de la cantidad suficiente de algo indispensable o valioso",
                "example_phrase": "缺乏实际经验 (lack practical experience)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "由于长期缺乏户外运动和充足的阳光照射，不少办公室白领出现了亚健康症状。",
                "pinyin": "Yóuyú chángqī quēfá hùwài yùndòng hé chōngzú de yángguāng zhàoshè, bùshǎo bàngōngshì báilǐng chūxiàn le yàjiànkāng zhèngzhuàng.",
                "en": "Due to a prolonged lack of outdoor exercise and sufficient sunshine, many office white-collar workers exhibit sub-health symptoms.",
                "es": "Debido a una prolongada carencia de ejercicio al aire libre y luz solar, muchos oficinistas manifiestan síntomas de fatiga crónica."
            },
            {
                "id": "#2",
                "hanzi": "这家初创公司在技术研发上极具前瞻性，但在海外市场开拓方面依然严重缺乏专业人才。",
                "pinyin": "Zhè jiā chūchuàng gōngsī zài jìshù yánfā shang jí jù qiánzhānxìng, dàn zài hǎiwài shìchǎng kāituò fāngmiàn yīrán yánzhòng quēfá zhuānyè réncái.",
                "en": "This startup is visionary in technology R&D, but still severely lacks experienced professionals in overseas market expansion.",
                "es": "Esta empresa emergente es visionaria en desarrollo técnico, pero aún acusa una grave falta de profesionales para expandirse al extranjero."
            }
        ],
        "collocations": [
            {"hanzi": "缺乏经验", "en": "lack experience"},
            {"hanzi": "缺乏资金", "en": "lack financial funds"},
            {"hanzi": "缺乏信心", "en": "lack confidence"},
            {"hanzi": "缺乏证据", "en": "lack evidence"},
            {"hanzi": "严重缺乏", "en": "severely lack"},
            {"hanzi": "缺乏耐心", "en": "lack patience"}
        ],
        "idioms": [
            {"hanzi": "捉襟见肘", "pinyin": "zhuō jīn jiàn zhǒu", "meaning_en": "pull up sleeves and reveal elbows; severely strapped for resources"},
            {"hanzi": "缺衣少食", "pinyin": "quē yī shǎo shí", "meaning_en": "short of food and clothing; living in dire poverty"},
            {"hanzi": "供不应求", "pinyin": "gōng bù yìng qiú", "meaning_en": "supply falls short of demand; acute shortages"},
            {"hanzi": "短斤少两", "pinyin": "duǎn jīn shǎo liǎng", "meaning_en": "give short weight; lack fair measure"}
        ],
        "character_decomposition": [
            {
                "character": "缺",
                "pinyin": "quē",
                "meaning_en": "deficient; gap; lack",
                "meaning_es": "falta; defecto; hendidura",
                "radical": "缶",
                "radical_meaning_en": "earthenware pot",
                "meaning_component": "缶 (earthen jar with chipped rim)",
                "sound_component": "夬 (guài / break off; phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Pottery jar radical 缶 beside 夬 (archery glove/breach); an earthenware jar missing a chip on its rim, denoting an incomplete defect.",
                "visual_mnemonic_story_en": "A clay pottery jar (缶) chipped and cracked at the rim (夬) shows an obvious gap or deficiency (缺).",
                "visual_mnemonic_story_es": "Una vasija de arcilla (缶) desportillada en su borde (夬) muestra una hendidura o carencia (缺).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OUDK",
                "traditional": "缺"
            },
            {
                "character": "乏",
                "pinyin": "fá",
                "meaning_en": "short of; tired; depleted",
                "meaning_es": "carente; exhausto; falto",
                "radical": "丿",
                "radical_meaning_en": "slash",
                "meaning_component": "distorted inverted pictograph of 正 (straight foot)",
                "sound_component": "乏 (fá)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Inversion of 正 (walking upright); walking in reverse or limping from exhaustion, depleted of strength and provisions.",
                "visual_mnemonic_story_en": "Footsteps wavering backward due to sheer exhaustion, signaling that vital energy has run out (乏).",
                "visual_mnemonic_story_es": "Pasos tambaleantes que retroceden por agotamiento, señal de que las provisiones se han vaciado (乏).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HINO",
                "traditional": "乏"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When a chipped pottery bowl (缺) runs out of provisions, you suffer from a total lack (缺乏).",
            "composite_memory_hook_es": "Cuando una vasija desportillada (缺) agota sus víveres, se padece una total escasez (缺乏).",
            "cultural_and_cognitive_roots": "Derived from ancient grain storage metaphors where cracked vessels leak grain, resulting in impoverishment.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by rising tone: 'quē fá' (55-35). Hold a clean high pitch on 'quē', then soar upward on 'fá'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "缺", "pinyin": "quē", "meaning_en": "lack; gap", "distinction_note": "Contains pottery radical 缶 on the left"},
                {"character": "决", "pinyin": "jué", "meaning_en": "decide; determine", "distinction_note": "Contains ice/water radical 冫 with 夬"},
                {"character": "乏", "pinyin": "fá", "meaning_en": "lacking; weary", "distinction_note": "4 strokes starting with slanted撇 and horizontal line"},
                {"character": "之", "pinyin": "zhī", "meaning_en": "possessive particle; go", "distinction_note": "Top dot 丶 instead of slanted horizontal hook"}
            ],
            "etymological_cognates": [
                {"character": "少", "pinyin": "shǎo", "gloss_en": "few; little"},
                {"character": "短", "pinyin": "duǎn", "gloss_en": "short; deficient"},
                {"character": "贫", "pinyin": "pín", "gloss_en": "poor; destitute"},
                {"character": "耗", "pinyin": "hào", "gloss_en": "consume; deplete"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "缺乏 denotes the absence or insufficiency of intangible qualities or vital resources needed for success.",
            "contrasts": [
                {"id": 1, "compared_word": "缺乏 vs. 缺少", "pinyin": "quēshǎo", "analysis": "缺少 is often used for countable items or people (缺少两人), while 缺乏 applies to abstract qualities (缺乏经验, 缺乏耐心)."},
                {"id": 2, "compared_word": "缺乏 vs. 贫乏", "pinyin": "pínfá", "analysis": "贫乏 implies utter cultural, spiritual, or linguistic poverty (语言贫乏), while 缺乏 simply means falling below necessary quota."},
                {"id": 3, "compared_word": "缺乏 vs. 损失", "pinyin": "sǔnshī", "analysis": "损失 denotes tangible damage or loss of what was already possessed, while 缺乏 describes non-existence of resources."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "年轻人在职业规划初期往往缺乏对行业全貌的清醒认识，容易在盲目跟风中迷失方向。唯有多向经验丰富的行业前辈请教，踏踏实实深入一线岗位磨练，才能有效弥补知识结构的短板与实战能力的匮乏。",
                "pinyin": "Niánqīngrén zài zhíyè guīhuà chūqī wǎngwǎng quēfá duì hángyè quánmào de qīngxǐng rènshi, róngyì zài mángmù gēnfēng zhōng míshī fāngxiàng. Wéi yǒu duō xiàng jīngyàn fēngfù de hángyè qiánbèi qǐngjiào, tātā-shíshí shēnrù yīxiàn gǎngwèi móliàn, cái néng yǒuxiào míbǔ zhīshi jiégòu de duǎnbǎn yǔ shízhàn nénglì de kuìfá.",
                "en": "Young people often lack clear insight into their industries early in their careers, easily drifting with trends. Only by consulting veterans and gaining solid frontline experience can they remedy blind spots in their knowledge.",
                "es": "Los jóvenes carecen a menudo de una visión lúcida de su profesión al inicio, perdiéndose en modas. Sólo consultando a veteranos y fogueándose en el terreno compensarán las lagunas de su formación práctica."
            },
            {
                "id": "#2",
                "hanzi": "当年奈史密斯发明篮球运动时，学校正缺乏专门的室内器械与活动经费。然而物质条件的缺乏并没有阻碍创新的诞生，反倒逼迫他跳出思维惯性，用两只极为廉价的竹筐巧妙设计出风靡全球的体育项目。",
                "pinyin": "Dāngnián Nàishǐmīsī fāmíng lánqiú yùndòng shí, xuéxiào zhèng quēfá zhuānmén de shìnèi qìxiè yǔ huódòng jīngfèi. Rán'ér wùzhì tiáojiàn de quēfá bìng méiyǒu zǔ'ài chuàngxīn de dànshēng, fǎndào bīpò tā tiào chū sīwéi guànxìng, yòng liǎng zhī jíwéi liánjià de zhúkuāng qiǎomiào shèjì chū fēngmí quánqiú de tǐyù xiàngmù.",
                "en": "When Naismith invented basketball, the school lacked indoor apparatus and athletic funding. Yet this material scarcity never stifled innovation; instead, it prompted him to break mental ruts and use two cheap peach baskets to birth a worldwide sport.",
                "es": "Cuando Naismith ideó el baloncesto, la escuela carecía de equipamiento y fondos. Lejos de frenar la creatividad, tal escasez le forzó a quebrar la rutina, concibiendo con dos canastas baratas un deporte universal."
            }
        ]
    },

    # 05 项目
    {
        "id": "5",
        "hanzi": "项目",
        "pinyin": "xiàng mù",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "project; program; sports event; item",
            "es": "proyecto; programa; disciplina deportiva; rubro"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a planned endeavor undertaking a specific objective within defined scope and budget",
                "definition_es": "empresa o trabajo planificado con objetivos, plazos y recursos específicos",
                "example_phrase": "负责一个重大科研项目 (lead a major scientific research project)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a specific category in sports competitions or itemized list",
                "definition_es": "prueba o modalidad deportiva en competiciones",
                "example_phrase": "奥运会田径比赛项目 (track and field events in the Olympics)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过两年的刻苦攻关，研发团队终于提前完成了这座现代化跨海大桥的总体设计项目。",
                "pinyin": "Jīngguò liǎng nián de kèkǔ gōngguān, yánfā tuánduì zhōngyú tíqián wánchéng le zhè zuò xiàndàihuà kuàhǎi dàqiáo de zǒngtǐ shèjì xiàngmù.",
                "en": "After two years of hard research, the R&D team finally completed the overarching design project for this modern sea-crossing bridge ahead of schedule.",
                "es": "Tras dos años de intensa labor, el equipo completó antes del plazo previsto el proyecto de diseño integral del moderno puente marítimo."
            },
            {
                "id": "#2",
                "hanzi": "篮球在十九世纪末作为一项全新的体育项目诞生，如今已成为全球参与人数最多的运动之一。",
                "pinyin": "Lánqiú zài shíjiǔ shìjì mò zuòwéi yī xiàng quánxīn de tǐyù xiàngmù dànshēng, rújīn yǐ chéngwéi quánqiú cānyù rénshù zuì duō de yùndòng zhī yī.",
                "en": "Basketball was born in the late 19th century as a brand-new sporting event, and has now become one of the most widely played sports in the world.",
                "es": "Nacido a finales del siglo XIX como una disciplina deportiva inédita, el baloncesto es hoy uno de los deportes más practicados del planeta."
            }
        ],
        "collocations": [
            {"hanzi": "重大项目", "en": "major project"},
            {"hanzi": "体育项目", "en": "sporting event / discipline"},
            {"hanzi": "项目经理", "en": "project manager"},
            {"hanzi": "启动项目", "en": "launch a project"},
            {"hanzi": "投资项目", "en": "investment project"},
            {"hanzi": "项目进展", "en": "project progress"}
        ],
        "idioms": [
            {"hanzi": "立竿见影", "pinyin": "lì gān jiàn yǐng", "meaning_en": "set up pole and see shadow; yield instantaneous results"},
            {"hanzi": "开宗明义", "pinyin": "kāi zōng míng yì", "meaning_en": "state the main purpose right at the beginning"},
            {"hanzi": "各具特色", "pinyin": "gè jù tè sè", "meaning_en": "each having its own distinct characteristics"},
            {"hanzi": "纲举目张", "pinyin": "gāng jǔ mù zhāng", "meaning_en": "lift main rope and mesh spreads; organize systematically"}
        ],
        "character_decomposition": [
            {
                "character": "项",
                "pinyin": "xiàng",
                "meaning_en": "nape of neck; item; clause; sum",
                "meaning_es": "nuca; rubro; artículo; proyecto",
                "radical": "工",
                "radical_meaning_en": "work / craft",
                "meaning_component": "工 (artisan work) + 页 (head/neck pictograph)",
                "sound_component": "工 (gōng / phonetic connection)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Craft 工 beside head 页; originally the nape of the neck, extended metaphorically to individual bullet items on an official register.",
                "visual_mnemonic_story_en": "A clerk bowing his neck (页) over artisan blueprints (工), recording every distinct project clause (项).",
                "visual_mnemonic_story_es": "Un escriba inclinando la nuca (页) sobre los planos de obra (工), detallando cada rubro del proyecto (项).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MOMBO",
                "traditional": "項"
            },
            {
                "character": "目",
                "pinyin": "mù",
                "meaning_en": "eye; item; catalog; index",
                "meaning_es": "ojo; índice; epígrafe; categoría",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "pictograph of human eye and pupil",
                "sound_component": "目 (mù)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph of an eyeball and eyelids turned vertically; extended to lines of sight and catalog entries.",
                "visual_mnemonic_story_en": "An observant eye (目) looking straight ahead, reviewing catalog items one by one.",
                "visual_mnemonic_story_es": "Un ojo atento (目) mirando de frente, catalogando cada apartado en la lista.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BU",
                "traditional": "目"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Items checked off under the supervisor's neck (项) and watchful eyes (目) form a completed project (项目).",
            "composite_memory_hook_es": "Los rubros revisados bajo la nuca (项) y la atenta mirada (目) constituyen un proyecto culminado (项目).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese cataloging where '项' and '目' formed tabular ledger columns for bureaucratic supervision.",
            "tone_sandhi_and_pitch_modulation": "Two falling fourth tones: 'xiàng mù' (51-51). Deliver both syllables with crisp, distinct downward force."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "项", "pinyin": "xiàng", "meaning_en": "project; neck", "distinction_note": "Has 工 on left and 页 on right"},
                {"character": "顶", "pinyin": "dǐng", "meaning_en": "top; peak; withstand", "distinction_note": "Has 丁 on left instead of 工"},
                {"character": "目", "pinyin": "mù", "meaning_en": "eye; catalog", "distinction_note": "Vertical rectangle with two horizontal strokes inside"},
                {"character": "日", "pinyin": "rì", "meaning_en": "sun; day", "distinction_note": "Has only one horizontal stroke inside"}
            ],
            "etymological_cognates": [
                {"character": "案", "pinyin": "àn", "gloss_en": "case; record; plan"},
                {"character": "划", "pinyin": "huà", "gloss_en": "plan; divide"},
                {"character": "程", "pinyin": "chéng", "gloss_en": "journey; program"},
                {"character": "款", "pinyin": "kuǎn", "gloss_en": "clause; fund"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "项目 designates an organized undertaking or a specific event category in sports or enterprise.",
            "contrasts": [
                {"id": 1, "compared_word": "项目 vs. 计划", "pinyin": "jìhuà", "analysis": "计划 refers to the forward-looking plan or schedule, whereas 项目 is the concrete endeavor encompassing funding, team, and deliverables."},
                {"id": 2, "compared_word": "项目 vs. 方案", "pinyin": "fāng'àn", "analysis": "方案 is a proposed blueprint or problem-solving strategy, while 项目 is the overarching entity being implemented."},
                {"id": 3, "compared_word": "项目 vs. 任务", "pinyin": "rènwu", "analysis": "任务 is a specific delegated assignment or task, whereas 项目 is broader and composed of hundreds of individual tasks."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "大型跨国工程项目的成败，往往取决于项目经理对风险控制与多团队协同沟通的掌控能力。在错综复杂的施工过程中，任何一个关键节点的延误都可能导致连锁反应，甚至给整体工期带来不可挽回的巨大经济损失。",
                "pinyin": "Dàxíng kuàguó gōngchéng xiàngmù de chéngbài, wǎngwǎng qǔjué yú xiàngmù jīnglǐ duì fēngxiǎn kòngzhì yǔ duō tuánduì xiétóng gōutōng de zhǎngkòng nénglì. Zài cuòzōng-fùzá de shīgōng guòchéng zhōng, rènhé yí ge guānjiàn jiédiǎn de yánwù dōu kěnéng dǎozhì liánsuǒ fǎnyìng, shènzhì gěi zhěngtǐ gōngqī dài lái bùkě wǎnhuí de jùdà jīngjì sǔnshī.",
                "en": "The success of mega multinational engineering projects hinges on project managers' grasp of risk control and cross-team communication. In intricate workflows, any delay in key milestones can trigger domino reactions and huge economic losses.",
                "es": "El éxito de grandes proyectos de ingeniería depende del control de riesgos y la coordinación de equipos. En obras complejas, el retraso en un hito clave desencadena efectos dominó que conllevan cuantiosas pérdidas económicas."
            },
            {
                "id": "#2",
                "hanzi": "篮球最初只是作为冬季避免学生受寒的室内辅助项目，谁料在短短数十年间，它便凭借极高的观赏性与竞技魅力迅速风靡五大洲。如今，它不仅是奥运会最引人瞩目的核心比赛项目，更催生了产值数十亿美元的全球体育产业链。",
                "pinyin": "Lánqiú zuìchū zhǐshì zuòwéi dōngjì bìmiǎn xuésheng shòuhán de shìnèi fǔzhù xiàngmù, shuí liào zài duǎnduǎn shùshí nián jiān, tā biàn píngjiè jí gāo de guānshǎngxìng yǔ jìngjì mèilì xùnsù fēngmí wǔ dàzhōu. Rújīn, tā bùjǐn shì Àoyùnhuì zuì yǐnrén zhǔmù de héxīn bǐsài xiàngmù, gèng cuīshēng le chǎnzhí shùshí yì měiyuán de quánqiú tǐyù chǎnyèliàn.",
                "en": "Basketball was originally an auxiliary indoor program to protect students from the winter chill. Yet within decades, its athletic allure captivated five continents. Today, it is not only an Olympic cornerstone but drives a multibillion-dollar global sports empire.",
                "es": "El baloncesto nació como una disciplina bajo techo contra el frío invernal. En pocas décadas, su espectacularidad conquistó el mundo. Hoy es una prueba olímpica cumbre que impulsa un sector comercial multimillonario."
            }
        ]
    },

    # 06 桃
    {
        "id": "6",
        "hanzi": "桃",
        "pinyin": "táo",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "peach (fruit or tree)",
            "es": "melocotón; durazno"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a round, juicy, sweet fruit with soft downy skin and a rough furrowed stone; also the peach tree",
                "definition_es": "fruta redonda de pulpa jugosa, piel aterciopelada y hueso rugoso; también el árbol melocotonero",
                "example_phrase": "鲜嫩多汁的蜜桃 (tender and juicy honey peach)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每年七八月份正是蜜桃成熟的黄金季节，满树沉甸甸的粉红果实散发出诱人的甜香。",
                "pinyin": "Měinián qī-bā yuèfèn zhèng shì mìtáo chéngshú de huángjīn jìjié, mǎn shù chéndiāndiān de fěnhóng guǒshí sànfā chū yòurén de tiánxiāng.",
                "en": "Every July and August marks the peak season for honey peaches, when trees bowed under pink fruits give off enticing sweet fragrances.",
                "es": "Julio y agosto marcan el apogeo de los melocotones; los árboles cargados de frutos rosados despiden un dulce aroma tentador."
            },
            {
                "id": "#2",
                "hanzi": "在我国传统文化中，桃子因其吉祥寓意常被用作庆祝老人大寿的贺礼寿桃。",
                "pinyin": "Zài wǒguó chuántǒng wénhuà zhōng, táozi yīn qí jíxiáng yùyì cháng bèi yòng zuò qìngzhù lǎorén dàshòu de hèlǐ shòutáo.",
                "en": "In traditional Chinese culture, peaches symbolize longevity and are frequently given as congratulatory longevity peaches on seniors' birthdays.",
                "es": "En la cultura china, el melocotón simboliza longevidad y se ofrenda tradicionalmente en banquetes de cumpleaños de ancianos."
            }
        ],
        "collocations": [
            {"hanzi": "水蜜桃", "en": "honey peach"},
            {"hanzi": "寿桃", "en": "longevity peach (confectionery/fruit)"},
            {"hanzi": "桃树", "en": "peach tree"},
            {"hanzi": "桃花", "en": "peach blossom"},
            {"hanzi": "桃子", "en": "peach (common noun)"},
            {"hanzi": "核桃", "en": "walnut"}
        ],
        "idioms": [
            {"hanzi": "世外桃源", "pinyin": "shì wài táo yuán", "meaning_en": "the Peach Blossom Spring; a hidden haven of peace"},
            {"hanzi": "投桃报李", "pinyin": "tóu táo bào lǐ", "meaning_en": "give a peach and get a plum in return; exchange mutual courtesies"},
            {"hanzi": "桃李满天下", "pinyin": "táo lǐ mǎn tiān xià", "meaning_en": "peaches and plums across the land; distinguished students everywhere"},
            {"hanzi": "人面桃花", "pinyin": "rén miàn táo huā", "meaning_en": "a fair lady's face like peach blossoms; nostalgia for past beauty"}
        ],
        "character_decomposition": [
            {
                "character": "桃",
                "pinyin": "táo",
                "meaning_en": "peach",
                "meaning_es": "melocotón; durazno",
                "radical": "木",
                "radical_meaning_en": "tree / wood",
                "meaning_component": "木 (fruit tree / wood)",
                "sound_component": "兆 (zhào / split; omen; phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tree radical 木 beside 兆 (cracking turtle plastron); the fruit of the peach tree with its deeply cleft stone, highly esteemed for warding off evil.",
                "visual_mnemonic_story_en": "A fruitful tree (木) bearing sacred fruits with omen-like cleft pits (兆): the blessed peach (桃).",
                "visual_mnemonic_story_es": "Un árbol frutal (木) cuyos frutos tienen un hueso hendido con presagio propicio (兆): el melocotón (桃).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "DLMO",
                "traditional": "桃"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A sacred fruit tree (木) bearing auspicious omen-marked pits (兆) gives sweet peaches (桃).",
            "composite_memory_hook_es": "Un árbol (木) cuyos frutos encierran un hueso de buen agüero (兆) es el melocotonero (桃).",
            "cultural_and_cognitive_roots": "Revered in Daoist myth as the Queen Mother's divine fruit of immortality (蟠桃), representing longevity and warding against evil spirits.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone: 'táo' (35). Rise cleanly from mid-pitch to high, smooth and resonant."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "桃", "pinyin": "táo", "meaning_en": "peach", "distinction_note": "Tree radical 木 on left"},
                {"character": "挑", "pinyin": "tiāo", "meaning_en": "pick; carry on pole", "distinction_note": "Hand radical 扌 on left"},
                {"character": "逃", "pinyin": "táo", "meaning_en": "flee; escape", "distinction_note": "Movement radical 辶 at the bottom"},
                {"character": "眺", "pinyin": "tiào", "meaning_en": "look far into distance", "distinction_note": "Eye radical 目 on left"}
            ],
            "etymological_cognates": [
                {"character": "李", "pinyin": "lǐ", "gloss_en": "plum"},
                {"character": "杏", "pinyin": "xìng", "gloss_en": "apricot"},
                {"character": "梨", "pinyin": "lí", "gloss_en": "pear"},
                {"character": "枣", "pinyin": "zǎo", "gloss_en": "jujube / date"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "桃 refers specifically to the peach tree or its downy sweet stone fruit, rich in longevity symbolism.",
            "contrasts": [
                {"id": 1, "compared_word": "桃 vs. 李", "pinyin": "lǐ", "analysis": "桃 is larger with downy skin and furrowed stone, whereas 李 (plum) has smooth skin and is more tart."},
                {"id": 2, "compared_word": "桃 vs. 杏", "pinyin": "xìng", "analysis": "杏 (apricot) is smaller with orange-golden flesh, while 桃 has pink-tinged juicy flesh."},
                {"id": 3, "compared_word": "桃 vs. 苹果", "pinyin": "píngguǒ", "analysis": "苹果 has a crisp interior core with multiple seeds, while 桃 possesses a single hard woody central stone."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代文人常将桃树视为超脱尘俗的象征，陶渊明笔下的《桃花源记》便描绘了一个没有赋税徭役、民风淳朴安详的理想国度。千百年来，那一树树芬芳灿烂的桃花，寄托了中国人对安宁生活的无限憧憬。",
                "pinyin": "Zhōngguó gǔdài wénrén cháng jiāng táoshù shìwéi chāotuō chénsú de xiàngzhēng, Táo Yuānmíng bǐxià de Táo Huā Yuán Jì biàn miáohuì le yí ge méiyǒu fùshuì yáoyì, mínfēng chúnpǔ ānxiáng de lǐxiǎng guódù. Qiānbǎinián lái, nà yí shùshù fēnfāng cànlàn de táohuā, jìtuō le Zhōngguórén duì ānníng shēnghuó de wúxiàn chōngjǐng.",
                "en": "Ancient Chinese scholars revered peach trees as symbols of transcending vulgarity; Tao Yuanming's Peach Blossom Spring depicted a tranquil haven free from taxes. For centuries, radiant peach blossoms embodied enduring yearnings for peace.",
                "es": "Los literatos chinos veían en el melocotonero un símbolo utópico; Tao Yuanming retrató en su célebre fábula un remanso sin tributos ni discordias. Esas flores encarnaron el anhelo secular de una existencia sosegada."
            },
            {
                "id": "#2",
                "hanzi": "篮球运动在起步之初，所使用的球筐正是从当地果农手中找来的两个装桃子的竹筐。谁也没有料到，这个本用来盛放鲜桃的简陋农具，竟然在无意间成就了一项世界级的伟大体育发明，并在百年时光中持续带给全人类无尽的欢乐。",
                "pinyin": "Lánqiú yùndòng zài qǐbù zhī chū, suǒ shǐyòng de qiúkuāng zhèng shì cóng dāngdì guǒnóng shǒuzhōng zhǎolái de liǎng ge zhuāng táozi de zhúkuāng. Shuí yě méiyǒu liàodào, zhè ge běn yònglái chéngfàng xiāntáo de jiǎnlòu nóngjù, jìngrán zài wúyì jiān chéngjiù le yí xiàng shìjièjí de wěidà tǐyù fāmíng, bìng zài bǎinián shíguāng zhōng chíxù dài gěi quán rénlèi wújìn de huānlè.",
                "en": "At its inception, basketball used two peach baskets sourced from local orchardists. No one anticipated that these humble farm containers, meant for sweet fruit, would serendipitously birth a legendary sport that has brought boundless joy to mankind for over a century.",
                "es": "En sus inicios, el baloncesto empleó dos cestas de melocotón cedidas por campesinos. Nadie previó que un apero rural para cargar fruta alumbraría un invento deportivo monumental, brindando dicha a millones durante más de un siglo."
            }
        ]
    },

    # 07 装
    {
        "id": "7",
        "hanzi": "装",
        "pinyin": "zhuāng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to load; pack; hold; install; pretend; outfit",
            "es": "cargar; empacar; contener; instalar; fingir; vestimenta"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to put things into a container; pack or load goods",
                "definition_es": "meter o colocar objetos dentro de un recipiente o medio de transporte",
                "example_phrase": "把行李装进后备箱 (pack luggage into the car trunk)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to assemble, fit, or install equipment",
                "definition_es": "fijar, acoplar o montar un mecanismo o dispositivo",
                "example_phrase": "在墙上装空调 (install an air conditioner on the wall)"
            },
            {
                "sense_number": "3",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to pretend; feign; disguise oneself",
                "definition_es": "aparentar o disimular un estado o sentimiento que no es real",
                "example_phrase": "装作不知情 (pretend not to know)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "出发去机场前，她把所有重要证件和笔记本电脑都仔细地装进了随身背包里。",
                "pinyin": "Chūfā qù jīchǎng qián, tā bǎ suǒyǒu zhòngyào zhèngjiàn hé bǐjìběn diànnǎo dōu zǐxì de zhuāng jìn le suíshēn bēibāo lǐ.",
                "en": "Before setting off for the airport, she carefully packed all her vital documents and laptop into her carry-on backpack.",
                "es": "Antes de salir hacia el aeropuerto, guardó minuciosamente en su mochila todos los documentos esenciales y el portátil."
            },
            {
                "id": "#2",
                "hanzi": "技术工人正在实验室内给新型机器人安装高精度的激光雷达传感器。",
                "pinyin": "Jìshù gōngrén zhèng zài shíyànshì nèi gěi xīnxíng jīqìrén ānzhuāng gāo jīngdù de jīguāng léidá chuángǎnqì.",
                "en": "Technicians in the laboratory are currently installing high-precision LiDAR sensors onto the prototype robot.",
                "es": "Los técnicos montaban en el laboratorio sensores láser de alta precisión en el nuevo prototipo robótico."
            }
        ],
        "collocations": [
            {"hanzi": "装满", "en": "filled up with; pack full"},
            {"hanzi": "安装", "en": "install; assemble"},
            {"hanzi": "包装", "en": "package; wrap"},
            {"hanzi": "装车", "en": "load onto a vehicle"},
            {"hanzi": "伪装", "en": "disguise; camouflage"},
            {"hanzi": "装模作样", "en": "put on an act; affect airs"}
        ],
        "idioms": [
            {"hanzi": "装模作样", "pinyin": "zhuāng mú zuò yàng", "meaning_en": "put on an act; behave with affectation"},
            {"hanzi": "装聋作哑", "pinyin": "zhuāng lóng zuò yǎ", "meaning_en": "pretend to be deaf and mute; play dumb"},
            {"hanzi": "乔装打扮", "pinyin": "qiáo zhuāng dǎ bàn", "meaning_en": "disguise oneself in elaborate clothes"},
            {"hanzi": "满载而归", "pinyin": "mǎn zài ér guī", "meaning_en": "return fully loaded with riches"}
        ],
        "character_decomposition": [
            {
                "character": "装",
                "pinyin": "zhuāng",
                "meaning_en": "load; pack; attire; install",
                "meaning_es": "cargar; vestir; montar; fingir",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (garments / outer cover)",
                "sound_component": "壮 (zhuàng / sturdy; phonetic)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Sturdy 壮 on top over clothing 衣; packing oneself into robust travel attire, later expanded to packing goods and installing fixtures.",
                "visual_mnemonic_story_en": "A sturdy warrior (壮) donning protective travel clothes (衣) and packing his provisions (装).",
                "visual_mnemonic_story_es": "Un recio soldado (壮) vistiéndose con atuendos resistentes (衣) y cargando sus vituallas (装).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VGHO",
                "traditional": "裝"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A sturdy warrior (壮) dressing in heavy clothing (衣) packs supplies and installs gear (装).",
            "composite_memory_hook_es": "Un guerrero fuerte (壮) poniéndose ropa (衣) para empacar y montar su equipo de viaje (装).",
            "cultural_and_cognitive_roots": "Began as preparing baggage and outfitting oneself for distant expeditions along trade routes.",
            "tone_sandhi_and_pitch_modulation": "Level high tone: 'zhuāng' (55). Pronounce with sustained high vocal pitch without fading."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "装", "pinyin": "zhuāng", "meaning_en": "pack; install; pretend", "distinction_note": "Has clothing radical 衣 at bottom"},
                {"character": "妆", "pinyin": "zhuāng", "meaning_en": "makeup; cosmetics", "distinction_note": "Has woman radical 女 beside 丬"},
                {"character": "壮", "pinyin": "zhuàng", "meaning_en": "sturdy; strong", "distinction_note": "Upper part without the 衣 base"},
                {"character": "袋", "pinyin": "dài", "meaning_en": "bag; sack", "distinction_note": "Has 代 on top over 衣"}
            ],
            "etymological_cognates": [
                {"character": "载", "pinyin": "zài", "gloss_en": "load; carry onboard"},
                {"character": "盛", "pinyin": "chéng", "gloss_en": "hold in vessel; ladle"},
                {"character": "填", "pinyin": "tián", "gloss_en": "fill; stuff"},
                {"character": "配", "pinyin": "pèi", "gloss_en": "mate; equip; configure"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "装 covers both placing contents into a container and mounting/fixing parts onto a frame.",
            "contrasts": [
                {"id": 1, "compared_word": "装 vs. 盛", "pinyin": "chéng", "analysis": "盛 specifically refers to ladling or holding food/liquids in open bowls (盛饭, 盛汤), while 装 applies broadly to packing luggage or freight."},
                {"id": 2, "compared_word": "装 vs. 载", "pinyin": "zài", "analysis": "载 focuses on transportation vehicles bearing payload weight (载重, 载客), while 装 emphasizes the manual packing action."},
                {"id": 3, "compared_word": "装 vs. 假装", "pinyin": "jiǎzhuāng", "analysis": "假装 exclusively denotes psychological pretense, whereas 装 has rich mechanical and physical cargo meanings."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "母亲总觉得出门在外的游子照顾不好自己。每次临别前，她都会把亲手腌制的小菜和厚实的防寒衣物，一层一层结结实实地装满整个行李箱。那沉甸甸的分量里，装载着道不尽的挂念与深情。",
                "pinyin": "Mǔqīn zǒng juéde chūmén zàiwài de yóuzǐ zhàogù bù hǎo zìjǐ. Měicì línbié qián, tā dōu huì bǎ qīnshǒu yānzhì de xiǎocài hé hòushi de fánghán yīwù, yì céng yì céng jiējiē-shíshí de zhuāngmǎn zhěnggè xínglǐxiāng. Nà chéndiāndiān de fènliàng lǐ, zhuāngzài zhe dào bú jìn de guàniàn yǔ shēnqíng.",
                "en": "Mother always worried her traveling child could not care for himself. Before departures, she packed homemade preserves and heavy winter coats tightly into his suitcase. Within that heavy load lay inexhaustible maternal tenderness.",
                "es": "La madre temía que su hijo pasara privaciones lejos de casa. Antes de cada despedida, empacaba en la maleta viandas caseras y ropa de abrigo. En aquel equipaje repleto viajaba un cariño maternal incondicional."
            },
            {
                "id": "#2",
                "hanzi": "在奈史密斯发明篮球之初，工人们把两只用来装桃子的竹筐安装在阳台栏杆下方。然而每次球投进筐里后，都需要人专门踩着梯子把球取出来。为了解决这个麻烦，人们后来才锯掉筐底，实现了篮球顺畅下落的连贯比赛节奏。",
                "pinyin": "Zài Nàishǐmīsī fāmíng lánqiú zhī chū, gōngrénmen bǎ liǎng zhī yònglái zhuāng táozi de zhúkuāng ānzhuāng zài yángtái lángān xiàfāng. Rán'ér měicì qiú tóu jìn kuāng lǐ hòu, dōu xūyào rén zhuānmén cǎi zhe tīzi bǎ qiú qǔ chūlái. Wèile jiějué zhè ge máfan, rénmen hòulái cái jù diào kuāngdǐ, shíxiàn le lánqiú shùnchàng xiàluò de liánguàn bǐsài jiézòu.",
                "en": "At basketball's birth, workers mounted two baskets once used to hold peaches beneath the gallery railing. But after each goal, someone had to climb a ladder to extract the ball. To solve this hassle, they later sawed off the basket bottoms to let the ball drop through freely.",
                "es": "En los orígenes del baloncesto, se instalaron canastas de melocotones bajo la galería. Mas tras cada canasta, se requería trepar a una escalera para sacar el balón. Para agilizar el juego, se serruchó el fondo, permitiendo un flujo continuo."
            }
        ]
    },

    # 08 启发
    {
        "id": "8",
        "hanzi": "启发",
        "pinyin": "qǐ fā",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to enlighten; to inspire; inspiration",
            "es": "inspirar; iluminar; suscitar; inspiración"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to stimulate someone to think and discover truth or creative solutions on their own",
                "definition_es": "estimular la reflexión en alguien para que descubra soluciones o ideas por sí mismo",
                "example_phrase": "受到大自然奇妙现象的启发 (inspired by wondrous natural phenomena)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "insight or creative spark obtained from an observation or event",
                "definition_es": "chispa de comprensión o idea súbita provocada por un suceso",
                "example_phrase": "这番话给了我很大启发 (these remarks gave me great inspiration)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在课堂讨论中，老师没有直接给出标准答案，而是通过层层设问来启发学生独立思考。",
                "pinyin": "Zài kètáng tǎolùn zhōng, lǎoshī méiyǒu zhíjiē gěi chū biāozhǔn dá'àn, érshì tōngguò céngcéng shèwèn lái qǐfā xuésheng dúlì sīkǎo.",
                "en": "During class discussions, the teacher never handed out standard answers, instead asking probing questions to inspire students to think independently.",
                "es": "Durante el debate en clase, el profesor no dio respuestas hechas, sino que formuló preguntas para estimular el criterio independiente de los alumnos."
            },
            {
                "id": "#2",
                "hanzi": "仿生科学家从荷叶不沾泥水的自洁原理中受到启发，成功研发出了革命性的防水防油纳米涂层。",
                "pinyin": "Fǎngshēng kēxuéjiā cóng héyè bù zhān níshuǐ de zìjié yuánlǐ zhōng shòudào qǐfā, chénggōng yánfā chū le gémìngxìng de fángshuǐ fángyóu nàmǐ túcéng.",
                "en": "Biomimetic scientists drew inspiration from the lotus leaf's self-cleaning property, developing revolutionary waterproof and oleophobic nano-coatings.",
                "es": "Científicos biomiméticos se inspiraron en la flor de loto para crear un revolucionario nanorrevestimiento impermeable y repelente de aceites."
            }
        ],
        "collocations": [
            {"hanzi": "深受启发", "en": "deeply inspired"},
            {"hanzi": "启发式教学", "en": "heuristic / elicitation teaching"},
            {"hanzi": "受到启发", "en": "receive inspiration"},
            {"hanzi": "启发思维", "en": "stimulate thinking"},
            {"hanzi": "给予启发", "en": "provide inspiration"},
            {"hanzi": "灵感启发", "en": "spark of inspiration"}
        ],
        "idioms": [
            {"hanzi": "举一反三", "pinyin": "jǔ yī fǎn sān", "meaning_en": "infer three things from one fact; learn by analogy"},
            {"hanzi": "触类旁通", "pinyin": "chù lèi páng tōng", "meaning_en": "comprehend an entire category by understanding one instance"},
            {"hanzi": "恍然大悟", "pinyin": "huǎng rán dà wù", "meaning_en": "suddenly see the light; sudden dawn of comprehension"},
            {"hanzi": "茅塞顿开", "pinyin": "máo sè dùn kāi", "meaning_en": "thickets of doubt suddenly cleared; suddenly enlightened"}
        ],
        "character_decomposition": [
            {
                "character": "启",
                "pinyin": "qǐ",
                "meaning_en": "open; enlighten; initiate",
                "meaning_es": "abrir; alumbrar; iniciar",
                "radical": "户",
                "radical_meaning_en": "single door",
                "meaning_component": "户 (single door leaflet) + 口 (mouth speaking)",
                "sound_component": "启 (qǐ)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Single leaf door 户 over mouth 口; opening the door and speaking words of wisdom to illuminate the uninitiated.",
                "visual_mnemonic_story_en": "Unlocking a closed doorway (户) with enlightening words (口) to awaken the mind (启).",
                "visual_mnemonic_story_es": "Abrir una puerta trancada (户) mediante palabras elocuentes (口) para despejar la mente (启).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ISR",
                "traditional": "啟"
            },
            {
                "character": "发",
                "pinyin": "fā",
                "meaning_en": "send out; expand; develop",
                "meaning_es": "lanzar; manifestar; florecer",
                "radical": "又",
                "radical_meaning_en": "right hand",
                "meaning_component": "pictograph of releasing an arrow from a drawn bow",
                "sound_component": "发 (fā)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A drawn bow releasing an arrow; metaphorically emitting, manifesting, and spurring forward development.",
                "visual_mnemonic_story_en": "Releasing an arrow from a drawn bow, sparking rapid outward flight and expansion (发).",
                "visual_mnemonic_story_es": "Soltar una flecha tensada en el arco que vuela rauda hacia el blanco manifestándose (发).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "IVE",
                "traditional": "發"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Unlocking the mental doorway (启) lets creative insight burst forth like a flying arrow (发) to inspire (启发).",
            "composite_memory_hook_es": "Abrir la puerta de la mente (启) permite que la inspiración brote como una flecha en vuelo (发) para iluminar (启发).",
            "cultural_and_cognitive_roots": "Derived from Confucius in the Analects: '不愤不启，不悱不发' (I do not enlighten someone who is not eager to know).",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by high level tone: 'qǐ fā' (214-55). Dip down deeply on 'qǐ' before ascending to a sustained high 'fā'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "启", "pinyin": "qǐ", "meaning_en": "open; enlighten", "distinction_note": "Single door 户 on top over 口"},
                {"character": "扇", "pinyin": "shān", "meaning_en": "fan; flap wings", "distinction_note": "Has 羽 (feathers) inside 户"},
                {"character": "房", "pinyin": "fáng", "meaning_en": "room; house", "distinction_note": "Has 方 inside 户"},
                {"character": "发", "pinyin": "fā", "meaning_en": "emit; hair", "distinction_note": "5 strokes with upper crossing slant"}
            ],
            "etymological_cognates": [
                {"character": "迪", "pinyin": "dí", "gloss_en": "enlighten; guide"},
                {"character": "示", "pinyin": "shì", "gloss_en": "show; reveal"},
                {"character": "诱", "pinyin": "yòu", "gloss_en": "induce; entice"},
                {"character": "导", "pinyin": "dǎo", "gloss_en": "lead; instruct"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "启发 centers on unlocking latent human understanding by giving subtle hints rather than spoon-feeding.",
            "contrasts": [
                {"id": 1, "compared_word": "启发 vs. 启示", "pinyin": "qǐshì", "analysis": "启发 is primarily a verb or internal cognitive spark, while 启示 is usually a noun denoting profound religious or philosophical revelation."},
                {"id": 2, "compared_word": "启发 vs. 鼓励", "pinyin": "gǔlì", "analysis": "鼓励 focuses on boosting morale, emotional courage, and motivation, whereas 启发 triggers intellectual problem-solving."},
                {"id": 3, "compared_word": "启发 vs. 指导", "pinyin": "zhǐdǎo", "analysis": "指导 provides explicit directions and step-by-step instructions, whereas 启发 gently steers one to discover answers independently."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "孔子曾说‘不愤不启，不悱不发’，强调教育应当注重时机与意愿。真正优秀的导师从不生硬灌输现成结论，而是善于捕捉求知者心智困顿的节点适度点拨，从而启发他们自己去勘破迷局、领悟人生真谛。",
                "pinyin": "Kǒngzǐ céng shuō 'bú fèn bù qǐ, bú fěi bù fā', qiángdiào jiàoyù yīngdāng zhùzhòng shíjī yǔ yìyuàn. Zhēnzhèng yōuxiù de dǎoshī cóngbù shēngyìng guànshū xiànchéng jiélùn, érshì shànyú bǔzhuō qiúzhīzhě xīnjié kùndùn de jiédiǎn shìdù diǎnbō, cóng'ér qǐfā tāmen zìjǐ qù kānpò míjú, lǐngwù rénshēng zhēndì.",
                "en": "Confucius famously asserted that teaching requires receptivity. Great mentors never force-feed conclusions; they identify moments of doubt to drop subtle hints, inspiring seekers to unravel perplexities and grasp life's truths.",
                "es": "Confucio sostenía que la enseñanza requiere receptividad. Un buen mentor jamás impone conclusiones; detecta las dudas del aprendiz y aporta pistas sutiles, incitándole a disipar enigmas y asimilar la verdad."
            },
            {
                "id": "#2",
                "hanzi": "面对工人们每次投篮后不得不反复搬梯子取球的繁琐困扰，一个在场边玩耍的小男孩好奇地问：‘为什么不把筐底直接剪开呢？’这句看似天真无邪的童言，却如同当头棒喝瞬间启发了在场的大人，彻底打破了思维的桎梏。",
                "pinyin": "Miànduì gōngrénmen měicì tóulán hòu bùdébù fǎnfù bān tīzi qǔ qiú de fánsuǒ kùnrǎo, yí ge zài chǎngbiān wánshuǎ de xiǎo nánhái hàoqí de wèn: 'Wèishénme bù bǎ kuāngdǐ zhíjiē jiǎn kāi ne?' Zhè jù kànsì tiānzhēn-wúxié de tóngyán, què rútóng dāngtóu-bànghè shùnjiān qǐfā le zàichǎng de dàren, chèdǐ dǎpò le sīwéi de zhìgù.",
                "en": "Faced with the nuisance of fetching ladders after every scored basket, a boy playing courtside innocently asked: 'Why not just cut open the basket bottom?' This naive remark struck the adults like a lightning bolt, inspiring them to shatter rigid mindsets.",
                "es": "Ante el tedio de subir a una escalera tras cada canasta, un niño preguntó: '¿Por qué no recortan el fondo?' Aquella ingenua observación iluminó a los adultos, quebrando de golpe sus prejuicios mentales."
            }
        ]
    },

    # 09 安装
    {
        "id": "9",
        "hanzi": "安装",
        "pinyin": "ān zhuāng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to install; to set up; to mount",
            "es": "instalar; montar; ensamblar; armar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to place equipment, machinery, fixtures, or software into position and connect ready for use",
                "definition_es": "fijar y conectar maquinaria, aparatos o programas informáticos dejándolos listos para su uso",
                "example_phrase": "安装净水器 (install a water purifier)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "装修师傅仅用半天时间，就将全套现代化的智能厨卫设施安装调试完毕了。",
                "pinyin": "Zhuāngxiū shīfu jǐn yòng bàntiān shíjiān, jiù jiāng quántào xiàndàihuà de zhìnéng chúwèi shèshī ānzhuāng tiáoshì wánbì le.",
                "en": "In merely half a day, the technician finished installing and tuning the complete suite of modern smart kitchen and bathroom facilities.",
                "es": "El técnico tardó apenas media jornada en montar y verificar todo el equipamiento inteligente de la cocina y el baño."
            },
            {
                "id": "#2",
                "hanzi": "为了保证办公网络环境的数据安全，企业要求所有员工的电脑必须统一定期安装最新的安全补丁。",
                "pinyin": "Wèile bǎozhèng bàngōng wǎngluò huánjìng de shùjù ānquán, qǐyè yāoqiú suǒyǒu yuángōng de diànnǎo bìxū tǒngyī dìngqī ānzhuāng zuìxīn de ānquán bǔdīng.",
                "en": "To guarantee data security across office networks, the enterprise requires all employees' computers to regularly install the latest security patches.",
                "es": "Para garantizar la seguridad en la red corporativa, la empresa exige instalar con regularidad los últimos parches de seguridad en los equipos."
            }
        ],
        "collocations": [
            {"hanzi": "安装调试", "en": "install and calibrate"},
            {"hanzi": "安装软件", "en": "install software"},
            {"hanzi": "上门安装", "en": "on-site installation service"},
            {"hanzi": "安装设备", "en": "install equipment"},
            {"hanzi": "免费安装", "en": "free installation"},
            {"hanzi": "重新安装", "en": "reinstall"}
        ],
        "idioms": [
            {"hanzi": "安居乐业", "pinyin": "ān jū lè yè", "meaning_en": "live in peace and work with contentment"},
            {"hanzi": "转危为安", "pinyin": "zhuǎn wēi wéi ān", "meaning_en": "turn peril into safety; avert danger"},
            {"hanzi": "乔装打扮", "pinyin": "qiáo zhuāng dǎ bàn", "meaning_en": "disguise oneself carefully"},
            {"hanzi": "安营扎寨", "pinyin": "ān yíng zhā zhài", "meaning_en": "pitch camps and build fortifications; settle down"}
        ],
        "character_decomposition": [
            {
                "character": "安",
                "pinyin": "ān",
                "meaning_en": "safe; secure; quiet; settle",
                "meaning_es": "seguro; tranquilo; asentar",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (roof / sheltered home) + 女 (woman peacefully at home)",
                "sound_component": "安 (ān)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A woman 女 sitting safely under a solid roof 宀; ancient symbol of security, calmness, and proper positioning.",
                "visual_mnemonic_story_en": "A woman (女) seated peacefully beneath a warm roof (宀) embodies safety and settling into place (安).",
                "visual_mnemonic_story_es": "Una mujer (女) descansando a salvo bajo un hogar seguro (宀) evoca estabilidad y sosiego (安).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JV",
                "traditional": "安"
            },
            {
                "character": "装",
                "pinyin": "zhuāng",
                "meaning_en": "fit; mount; outfit; load",
                "meaning_es": "montar; vestir; empacar",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (cover / outfit) + 壮 (sturdy support)",
                "sound_component": "壮 (zhuàng)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Clothing 衣 affixed upon sturdy 壮 frame; mounting and fitting items securely into place.",
                "visual_mnemonic_story_en": "Fastening sturdy fixtures (壮) dressed in protective casing (衣) to complete an installation (装).",
                "visual_mnemonic_story_es": "Fijar piezas robustas (壮) protegidas por carcasas (衣) para ultimar un ensamblaje (装).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VGHO",
                "traditional": "裝"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Carefully settling parts into secure shelter (安) and fastening the fixtures (装) achieves proper installation (安装).",
            "composite_memory_hook_es": "Asentar piezas con seguridad (安) ajustando los componentes (装) da como resultado una instalación perfecta (安装).",
            "cultural_and_cognitive_roots": "Evolved from domestic carpentry to modern mechanical engineering and software configuration.",
            "tone_sandhi_and_pitch_modulation": "Two high level tones: 'ān zhuāng' (55-55). Pronounce with sustained, even pitch across both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "安", "pinyin": "ān", "meaning_en": "peace; install", "distinction_note": "Roof 宀 over 女"},
                {"character": "按", "pinyin": "àn", "meaning_en": "press; according to", "distinction_note": "Hand radical 扌 on left of 安"},
                {"character": "案", "pinyin": "àn", "meaning_en": "table; case; record", "distinction_note": "Wood radical 木 underneath 安"},
                {"character": "装", "pinyin": "zhuāng", "meaning_en": "install; pack", "distinction_note": "Has 衣 at bottom"}
            ],
            "etymological_cognates": [
                {"character": "配", "pinyin": "pèi", "gloss_en": "match; allocate; equip"},
                {"character": "设", "pinyin": "shè", "gloss_en": "establish; setup"},
                {"character": "置", "pinyin": "zhì", "gloss_en": "place; install"},
                {"character": "架", "pinyin": "jià", "gloss_en": "frame; erect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "安装 specifically denotes assembling, mounting, or configuring physical fixtures or software.",
            "contrasts": [
                {"id": 1, "compared_word": "安装 vs. 组装", "pinyin": "zǔzhuāng", "analysis": "组装 focuses on assembling dispersed components into a finished product, while 安装 emphasizes mounting the finished unit onto a wall or system."},
                {"id": 2, "compared_word": "安装 vs. 安置", "pinyin": "ānzhì", "analysis": "安置 means settling people, refugees, or furniture into living spaces, while 安装 deals with technical equipment or software."},
                {"id": 3, "compared_word": "安装 vs. 修理", "pinyin": "xiūlǐ", "analysis": "修理 means repairing broken machinery, whereas 安装 is putting brand-new machinery into place initially."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "智能家居工程师在施工现场一丝不苟地对中央空调与全屋温控系统进行安装。他仔细核对线路图纸，严格排查每处管道接口，以确保这套复杂的自动化设施在未来的日常运转中能够长期保持零故障与高能效。",
                "pinyin": "Zhìnéng jiājū gōngchéngshī zài shīgōng xiànchǎng yìsī-bùgǒu de duì zhōngyāng kōngtiáo yǔ quánwū wēnkòng xìtǒng jìnxíng ānzhuāng. Tā zǐxì héduì xiànlù túzhǐ, yángé páichá měi chù guǎndào jiēkǒu, yǐ quèbǎo zhè tào fùzá de zìdònghuà shèshī zài wèilái de rìcháng yùnzhuǎn zhōng nénggòu chángqī bǎochí líng gùzhàng yǔ gāo néngxiào.",
                "en": "The smart home engineer meticulously installed the central air conditioning and whole-house climate control systems on site. He verified wiring schematics and checked pipe joints to ensure the complex automation ran smoothly.",
                "es": "El técnico de domótica instalaba minuciosamente el climatizador central en la vivienda. Cotejó planos e inspeccionó empalmes para garantizar que el complejo sistema funcionara sin fallos y con óptima eficiencia energética."
            },
            {
                "id": "#2",
                "hanzi": "当年奈史密斯发明篮球时，指派学校校工将两只盛桃竹筐安装在室内体育馆两头的栏杆上。谁也没有预料到，这项当时临时起意、极为粗糙的体育设施安装，竟在往后的岁月里演变为一个在全球拥有数以亿计忠实球迷的传奇运动。",
                "pinyin": "Dāngnián Nàishǐmīsī fāmíng lánqiú shí, zhǐpài xuéxiào xiàogōng jiāng liǎng zhī chéng táo zhúkuāng ānzhuāng zài shìnèi tǐyùguǎn liǎngtóu de lángān shang. Shuí yě méiyǒu yùliào dào, zhè xiàng dāngshí línshí-qǐyì, jíwéi cūcāo de tǐyù shèshī ānzhuāng, jìng zài wǎnghòu de suìyuè lǐ yǎnbiàn wéi yí ge zài quánqiú yǒngyǒu shù yǐ yì jì zhōngshí qiúmí de chuánqí yùndòng.",
                "en": "When Naismith created basketball, he instructed the custodian to mount two peach baskets onto railings at each end of the gym. No one dreamed that this impromptu installation would grow into a legendary sport with hundreds of millions of devotees.",
                "es": "Naismith mandó clavar dos cestas de melocotón en las barandillas del gimnasio escolar. Nadie imaginó que aquel tosco montaje improvisado acabaría convirtiéndose en un deporte legendario con cientos de millones de seguidores."
            }
        ]
    },

    # 10 栏杆
    {
        "id": "10",
        "hanzi": "栏杆",
        "pinyin": "lán gān",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "railing; balustrade; banister; barrier",
            "es": "barandilla; pasamanos; baranda; valla"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a barrier made of horizontal rails and vertical posts preventing falls along stairs, balconies, or bridges",
                "definition_es": "armazón compuesto de barras o balaustres que sirve de protección en balcones, escaleras o puentes",
                "example_phrase": "倚在阳台栏杆上看日落 (lean against the balcony railing watching the sunset)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "景区在临崖栈道的陡峭外侧安装了坚固的不锈钢防护栏杆，以确保游客观景时的绝对安全。",
                "pinyin": "Jǐngqū zài lín yá zhàndào de dǒuqiào wàicè ānzhuāng le jiāngù de búxiùgāng fánghù lángān, yǐ quèbǎo yóukè guānjǐng shí de juéduì ānquán.",
                "en": "The scenic park installed sturdy stainless steel guard railings along the steep cliffside walkways to guarantee the safety of sightseeing visitors.",
                "es": "El parque natural colocó firmes barandillas de acero inoxidable al borde del precipicio para salvaguardar a los turistas mientras contemplan las vistas."
            },
            {
                "id": "#2",
                "hanzi": "小男孩调皮地想翻越马路中央的隔离栏杆，被路口执勤的交通警察及时吹哨制止了。",
                "pinyin": "Xiǎo nánhái tiáopí de xiǎng fānyuè mǎlù zhōngyāng de gélí lángān, bèi lùkǒu zhíqín de jiāotōng jǐngchá jíshí chuīshào zhìzhǐ le.",
                "en": "The mischievous little boy tried to climb over the median barrier railing, but the traffic officer on duty whistled to stop him immediately.",
                "es": "El travieso chiquillo intentó saltar la valla que divide la calzada, pero el agente de tráfico le pitó al instante frenando su imprudencia."
            }
        ],
        "collocations": [
            {"hanzi": "扶着栏杆", "en": "hold onto the railing"},
            {"hanzi": "防护栏杆", "en": "protective barrier / guardrail"},
            {"hanzi": "阳台栏杆", "en": "balcony balustrade"},
            {"hanzi": "楼梯栏杆", "en": "staircase banister"},
            {"hanzi": "跨过栏杆", "en": "step over the railing"},
            {"hanzi": "雕花栏杆", "en": "carved marble/wood balustrade"}
        ],
        "idioms": [
            {"hanzi": "栏杆拍遍", "pinyin": "lán gān pāi biàn", "meaning_en": "strike railings repeatedly in patriotic grief or surging emotion"},
            {"hanzi": "雕栏玉砌", "pinyin": "diāo lán yù qì", "meaning_en": "carved balustrades and jade steps; opulent imperial palaces"},
            {"hanzi": "闭门造车", "pinyin": "bì mén zào chē", "meaning_en": "build cart behind closed doors; divorce theory from reality"},
            {"hanzi": "倚窗远眺", "pinyin": "yǐ chuāng yuǎn tiào", "meaning_en": "lean on windowsill gazing into distant horizon"}
        ],
        "character_decomposition": [
            {
                "character": "栏",
                "pinyin": "lán",
                "meaning_en": "railing; pen; column in newspaper",
                "meaning_es": "baranda; corral; columna",
                "radical": "木",
                "radical_meaning_en": "tree / wood",
                "meaning_component": "木 (wooden post)",
                "sound_component": "兰 (lán / orchid; phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tree radical 木 with phonetic 兰; a wooden pen or protective fence to keep livestock safe and delineate boundaries.",
                "visual_mnemonic_story_en": "Wooden posts (木) arranged gracefully like fragrant orchids (兰) to form a barrier fence (栏).",
                "visual_mnemonic_story_es": "Maderos alineados (木) con la pulcritud de orquídeas (兰) formando una cerca protectora (栏).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "DAMM",
                "traditional": "欄"
            },
            {
                "character": "杆",
                "pinyin": "gān",
                "meaning_en": "pole; rod; shaft",
                "meaning_es": "poste; pértiga; vara",
                "radical": "木",
                "radical_meaning_en": "tree / wood",
                "meaning_component": "木 (wooden timber)",
                "sound_component": "干 (gān / shield; trunk; phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Tree radical 木 beside 干; a tall straight wooden pole used as an upright post or flag staff.",
                "visual_mnemonic_story_en": "A straight wooden tree trunk (木) standing upright like a sturdy shield post (干) to make a pole (杆).",
                "visual_mnemonic_story_es": "El tronco recto de un árbol (木) erigido como un poste defensivo (干) formando una pértiga (杆).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "DMJ",
                "traditional": "桿"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Wooden boundary fences (栏) supported by upright posts (杆) create a protective railing (栏杆).",
            "composite_memory_hook_es": "Tablas protectoras de madera (栏) sostenidas por postes verticales (杆) componen una barandilla (栏杆).",
            "cultural_and_cognitive_roots": "Focal motif in Chinese classical poetry (辛弃疾 '把吴钩看了，栏杆拍遍') expressing patriotic yearning when leaning over grand vistas.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone followed by level high tone: 'lán gān' (35-55). Ascend smoothly on 'lán', then keep a sustained high level pitch on 'gān'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "栏", "pinyin": "lán", "meaning_en": "railing; pen", "distinction_note": "Tree radical 木 with 兰 on right"},
                {"character": "拦", "pinyin": "lán", "meaning_en": "block; stop; intercept", "distinction_note": "Hand radical 扌 on left instead of 木"},
                {"character": "杆", "pinyin": "gān", "meaning_en": "pole; shaft", "distinction_note": "Tree radical 木 with 干 on right"},
                {"character": "竿", "pinyin": "gān", "meaning_en": "bamboo rod/pole", "distinction_note": "Bamboo radical 竹 on top"}
            ],
            "etymological_cognates": [
                {"character": "栅", "pinyin": "zhà", "gloss_en": "palisade; railings"},
                {"character": "篱", "pinyin": "lí", "gloss_en": "bamboo fence; hedge"},
                {"character": "柱", "pinyin": "zhù", "gloss_en": "pillar; column"},
                {"character": "墙", "pinyin": "qiáng", "gloss_en": "wall; barrier"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "栏杆 refers strictly to a slotted waist-high safety barrier along balconies, bridges, or stairs.",
            "contrasts": [
                {"id": 1, "compared_word": "栏杆 vs. 扶手", "pinyin": "fúshǒu", "analysis": "扶手 is specifically the top grip rail grasped by hands for balance, while 栏杆 includes the whole assembly of vertical balusters and uprights."},
                {"id": 2, "compared_word": "栏杆 vs. 栅栏", "pinyin": "zhàlan", "analysis": "栅栏 denotes ground-level outdoor fencing around gardens or pastures, whereas 栏杆 is mounted on elevated balconies, staircases, and bridges."},
                {"id": 3, "compared_word": "栏杆 vs. 围墙", "pinyin": "wéiqiáng", "analysis": "围墙 is a solid brick or stone masonry enclosure blocking vision and passage, whereas 栏杆 is a see-through safety rail."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "暮色苍茫时分，诗人独自倚靠在江南古桥那饱经风霜的汉白玉栏杆旁。水面上微波荡漾，渔火点点，微凉的晚风吹拂着青衫，那一排雕琢精美的石桥栏杆，默默见证着岁月的流逝与人世间的聚散悲欢。",
                "pinyin": "Mùsè cāngmáng shífēn, shīrén dúzì yǐkào zài Jiāngnán gǔqiáo nà bǎojīng-fēngshuāng de hànbáiyù lángān páng. Shuǐmiàn shang wēibō dàngyàng, yúhuǒ diǎndiǎn, wēiliáng de wǎnfēng chuīfú zhe qīngshān, nà yì pái diāozhuó jīngměi de shíqiáo lángān, mòmò jiànzhèng zhe suìyuè de liúshì yǔ rénshìjiān de jùsàn bēihuān.",
                "en": "At twilight, the poet leaned alone against weathered white marble railings on an ancient Jiangnan bridge. Ripples shimmered with fishing fires as evening breezes ruffled his robes; the carved railings stood silent witness to passing eras and earthly sorrow.",
                "es": "Al caer el crepúsculo, el poeta se apoyaba en la barandilla de mármol del viejo puente fluvial. Ondulaban las aguas con destellos de barcas mientras la brisa acariciaba su túnica; los balaustres esculpidos contemplaban en silencio el paso inexorable del tiempo."
            },
            {
                "id": "#2",
                "hanzi": "体育馆二楼环形看台下方的木质栏杆，原本只是为了防止观众失足跌落的防护设施。而奈史密斯别出心裁地将两只桃筐固定在距离地面三米多高的栏杆边沿，无意间确立了百年来篮球运动篮筐的标准垂直高度。",
                "pinyin": "Tǐyùguǎn èrlóu huánxíng kàntái xiàfāng de mùzhì lángān, yuánběn zhǐshì wèile fángzhǐ guānzhòng shīzú diēluò de fánghù shèshī. Ér Nàishǐmīsī biéchūxīncái de jiāng liǎng zhī táokuāng gùdìng zài jùlí dìmbiàn sān mǐ duō gāo de lángān biānyán, wúyì jiān quèlì le bǎinián lái lánqiú yùndòng lánkuāng de biāozhǔn chuízhí gāodù.",
                "en": "The wooden railings beneath the second-floor gymnasium balcony were originally mere safety barriers against falls. Yet Naismith ingeniously nailed two peach baskets onto those railings ten feet up, inadvertently establishing the universal rim height for basketball.",
                "es": "La barandilla del graderío en el gimnasio sólo buscaba evitar caídas. Sin embargo, Naismith fijó allí dos cestas a más de tres metros de altura, fijando sin proponérselo la cota reglamentaria del aro que perdura hasta nuestros días."
            }
        ]
    }
]

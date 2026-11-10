# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 表现
    {
        "id": "1",
        "hanzi": "表现",
        "pinyin": "biǎo xiàn",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to show; to manifest; to display; expression; performance; conduct",
            "es": "manifestar; mostrar; expresar; rendimiento; conducta; comportamiento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to show or manifest internal qualities, thoughts, or emotions through external words or actions",
                "definition_es": "manifestar o mostrar cualidades, ideas o sentimientos a través de actos o palabras",
                "example_phrase": "表现出色 (perform exceptionally well)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "conduct, behavioral manifestation, or work performance",
                "definition_es": "conducta, comportamiento o rendimiento laboral observable",
                "example_phrase": "工作表现良好 (good work performance)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "小李在面试中表现得从容自信，对主考官提出的专业问题对答如流，赢得了高度评价。",
                "pinyin": "Xiǎo Lǐ zài miànshì zhōng biǎoxiàn de cóngróng zìxìn, duì zhǔkǎoguān tíchū de zhuānyè wèntí duìdá-rúliú, yíngdé le gāodù píngjià.",
                "en": "Xiao Li performed calmly and confidently in the interview, answering professional questions fluently and winning high praise.",
                "es": "Xiao Li se desenvolvió con serenidad y aplomo durante la entrevista, respondiendo con soltura las preguntas profesionales."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在文学创作中表现出深刻的现实关怀，而在日常宴请朋友时则表现得热情随和，毫无大家架子。",
                "pinyin": "Lǔ Xùn zài wénxué chuàngzuò zhōng biǎoxiàn chū shēnkè de xiànshí guānhuái, ér zài rìcháng yànqǐng péngyou shí zé biǎoxiàn de rèqíng suíhe, háowú dàjiā jiàzi.",
                "en": "Lu Xun displayed profound social concern in writing, yet showed warm approachability when hosting friends in daily life.",
                "es": "Lu Xun mostró una profunda preocupación social en sus obras, mientras que al convidar amigos se mostraba cálido y accesible."
            }
        ],
        "collocations": [
            {"hanzi": "良好表现", "en": "good performance"},
            {"hanzi": "具体表现", "en": "concrete manifestation"},
            {"hanzi": "表现突出", "en": "outstanding performance"},
            {"hanzi": "表现出", "en": "display; exhibit"},
            {"hanzi": "临床表现", "en": "clinical manifestation"},
            {"hanzi": "表现形式", "en": "form of expression"}
        ],
        "idioms": [
            {"hanzi": "各抒己见", "pinyin": "gè shū jǐ jiàn", "meaning_en": "everyone expresses their own personal views"},
            {"hanzi": "直抒胸臆", "pinyin": "zhí shū xiōng yì", "meaning_en": "express one's inner feelings candidly"},
            {"hanzi": "表里如一", "pinyin": "biǎo lǐ rú yī", "meaning_en": "external appearance and internal character are identical; sincere"},
            {"hanzi": "显山露水", "pinyin": "xiǎn shān lù shuǐ", "meaning_en": "show off one's abilities or wealth visibly"}
        ],
        "character_decomposition": [
            {
                "character": "表",
                "pinyin": "biǎo",
                "meaning_en": "surface; exterior; watch; show",
                "meaning_es": "superficie; exterior; reloj; manifestar",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (garment, outer fur robe)",
                "sound_component": "毛 (máo, fur / phonetic harmony)",
                "stroke_count": 8,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideogram showing an outer fur garment worn outside, symbolizing the outer surface or visible manifestation.",
                "visual_mnemonic_story_en": "An ornate outer fur coat (衣) worn on the exterior displays one's status openly (表).",
                "visual_mnemonic_story_es": "Un abrigo de pieles (衣) llevado en el exterior exhibe la compostura hacia afuera (表).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "QMV",
                "traditional": ""
            },
            {
                "character": "现",
                "pinyin": "xiàn",
                "meaning_en": "appear; reveal; present; current",
                "meaning_es": "aparecer; manifestar; actual; presente",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王 (jade luster)",
                "sound_component": "见 (jiàn, see / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where jade luster 王 is revealed to the eye 见, meaning to shine forth or appear.",
                "visual_mnemonic_story_en": "A cut jade stone (王) is held up so onlookers can see (见) its brilliance shine into view (现).",
                "visual_mnemonic_story_es": "Una gema de jade (王) se alza para que todos la vean (见) resplandecer ante la mirada (现).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MGBUU",
                "traditional": "現"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Turn your outer garment (表) outward to let your true qualities appear (现) in full view (表现).",
            "composite_memory_hook_es": "Gira tu prenda exterior (表) para dejar que tus talentos aparezcan (现) a plena luz (表现).",
            "cultural_and_cognitive_roots": "Derived from the ancient distinction between the inner self (里) and the observable outer conduct (表); 'biǎoxiàn' reflects how internal virtue is made tangible to the external world.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by falling tone: 'biǎo xiàn' (214-51). Syllable 'biǎo' dips low before dropping sharply into 4th tone 'xiàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; compass", "distinction_note": "Left side has 夫 instead of 王 in 现"},
                {"character": "视", "pinyin": "shì", "meaning_en": "look at; vision", "distinction_note": "Left side has radical 礻 instead of 王"},
                {"character": "袁", "pinyin": "yuán", "meaning_en": "surname Yuan", "distinction_note": "Middle has 口 structure, unlike 表"},
                {"character": "哀", "pinyin": "āi", "meaning_en": "sorrow; grief", "distinction_note": "Middle has 口 between top and bottom clothing strokes"}
            ],
            "etymological_cognates": [
                {"character": "见", "pinyin": "jiàn", "gloss_en": "see; perceive visually"},
                {"character": "视", "pinyin": "shì", "gloss_en": "look; examine carefully"},
                {"character": "览", "pinyin": "lǎn", "gloss_en": "survey; read through"},
                {"character": "显", "pinyin": "xiǎn", "gloss_en": "prominent; manifest"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "表现 emphasizes the visible manifestation or behavioral output of internal qualities, thoughts, or abilities.",
            "contrasts": [
                {"id": "1", "compared_word": "表现 vs. 表明", "pinyin": "biǎomíng", "analysis": "表现 focuses on observable behavior or conduct over time, while 表明 emphasizes making a clear intellectual statement or signaling a conclusive fact."},
                {"id": "2", "compared_word": "表现 vs. 表达", "pinyin": "biǎodá", "analysis": "表现 pertains to general behavioral and performance display, whereas 表达 is restricted to communicating thoughts, feelings, or ideas through language and art."},
                {"id": "3", "compared_word": "表现 vs. 显示", "pinyin": "xiǎnshì", "analysis": "表现 suggests subjective effort or spontaneous human performance, while 显示 denotes objective display of data, indicators, or evident results."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "一个人真正的教养，往往在不经意的微小细节中表现得淋漓尽致。无论是在餐桌上礼貌地夹菜，还是在拥挤的电梯里耐心等待，这些无声的表现都是心灵深处最真实的映照。懂得体贴他人，才是最高贵的风度。",
                "pinyin": "Yí ge rén zhēnzhèng de jiàoyǎng, wǎngwǎng zài bùjīngyì de wēixiǎo xìjié zhōng biǎoxiàn de línlí-jìnzhì. Wúlùn shì zài cānzhuō shàng lǐmào de jiācài, háishì zài yōngjǐ de diàntī lǐ nàixīn děngdài, zhèxiē wúshēng de biǎoxiàn dōu shì xīnlíng shēnchù zuì zhēnshí de yìngzhào. Dǒngdé tǐtiē tārén, cáishì zuì gāoguì de fēngdù.",
                "en": "True cultivation is often manifested most thoroughly in small careless details. Whether politely taking food at table or waiting patiently in an elevator, these silent expressions reflect the inner heart. Thoughtfulness is the noblest elegance.",
                "es": "La verdadera educación se manifiesta en los detalles más espontáneos. Ya sea sirviéndose con cortesía a la mesa o esperando con paciencia en el ascensor, estas muestras silenciosas revelan el alma. Considerar a los demás es la máxima distinción."
            },
            {
                "id": "#2",
                "hanzi": "现代企业考核机制越来越注重员工的全面表现。管理者不仅关注个人销售业绩的突出成果，更考量团队协作中的沟通表现与危机应对能力。科学的评估体系通过多维度反馈，全面反映员工在岗位上的真实综合素质。",
                "pinyin": "Xiàndài qǐyè kǎohé jīzhì yuèláiyuè zhùzhòng yuángōng de quánmiàn biǎoxiàn. Guǎnlǐzhě bùjǐn guānzhù gèrén xiāoshòu yèjì de tūchū chéngguǒ, gèng kǎoliáng tuánduì xiézuò zhōng de gōutōng biǎoxiàn yǔ wēijī yìngduì nénglì. Kēxué de pínggù tǐxì tōngguò duō wéidù fǎnkuì, quánmiàn fǎnyìng yuángōng zài gǎngwèi shàng de zhēnshí zōnghé sùzhì.",
                "en": "Modern appraisal systems increasingly focus on comprehensive employee performance. Managers review not only notable sales achievements, but collaborative communication and crisis management. Multi-dimensional feedback objectively gauges overall competence.",
                "es": "La evaluación corporativa moderna prioriza el desempeño integral del empleado. Los directivos analizan no solo los logros en ventas, sino la cooperación grupal y la resolución de imprevistos. Este sistema multidimensional refleja las competencias laborales."
            }
        ]
    },

    # 02 突出
    {
        "id": "2",
        "hanzi": "突出",
        "pinyin": "tū chū",
        "part_of_speech": "Adjective / Verb",
        "meanings_summary": {
            "en": "prominent; outstanding; striking; conspicuous; to stand out; to highlight",
            "es": "destacado; sobresaliente; prominente; resaltar; poner de relieve; descollar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "clearly prominent, striking, or exceeding the average standard",
                "definition_es": "claramente prominente, sobresaliente o superior a la media",
                "example_phrase": "成绩突出 (outstanding achievement)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to highlight, emphasize, or project physically outward",
                "definition_es": "hacer resaltar, dar prominencia o proyectarse físicamente hacia afuera",
                "example_phrase": "突出重点 (highlight the focal point)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "他在数学竞赛中取得了突出的成绩，不仅获得了金牌，还得到了名校的录取邀请函。",
                "pinyin": "Tā zài shùxué jìngsài zhōng qǔdé le tūchū de chéngjì, bùjǐn huòdé le jīnpái, hái dédào le míngxiào de lùqǔ yāoqǐnghán.",
                "en": "He achieved outstanding results in the mathematics competition, winning not only a gold medal but an admission invitation from a prestigious school.",
                "es": "Alcanzó resultados sobresalientes en la olimpiada de matemáticas, ganando no solo el oro sino la admisión a una célebre universidad."
            },
            {
                "id": "#2",
                "hanzi": "这份研究报告着重突出了近代都市变迁对传统民俗的影响，具有很强的学术说服力与前瞻性。",
                "pinyin": "Zhè fèn yánjiū bàogào zhuózhòng tūchū le jìndài dūshì biànqiān duì chuántǒng mínsú de yǐngxiǎng, jùyǒu hěn qiáng de xuéshù shuōfúlì yǔ qiánzhānxìng.",
                "en": "This research report emphatically highlighted the impact of modern urban transition on folk customs, possessing scholarly rigor and foresight.",
                "es": "Este informe de investigación destacó con firmeza el impacto de la modernización urbana sobre el folclore, con gran rigor y visión académica."
            }
        ],
        "collocations": [
            {"hanzi": "成绩突出", "en": "outstanding achievement"},
            {"hanzi": "突出贡献", "en": "prominent contribution"},
            {"hanzi": "突出特点", "en": "striking feature"},
            {"hanzi": "突出重点", "en": "highlight the key points"},
            {"hanzi": "突出矛盾", "en": "accentuate contradictions"},
            {"hanzi": "地位突出", "en": "prominent position"}
        ],
        "idioms": [
            {"hanzi": "出类拔萃", "pinyin": "chū lèi bá cuì", "meaning_en": "stand out above one's peers; distinguished"},
            {"hanzi": "突飞猛进", "pinyin": "tū fēi měng jìn", "meaning_en": "advance by leaps and bounds; rapid progress"},
            {"hanzi": "拔地倚天", "pinyin": "bá dì yǐ tiān", "meaning_en": "rise steeply from the ground into the sky; towering"},
            {"hanzi": "锋芒毕露", "pinyin": "fēng máng bì lù", "meaning_en": "display one's edge or brilliance fully"}
        ],
        "character_decomposition": [
            {
                "character": "突",
                "pinyin": "tū",
                "meaning_en": "dash forward; abrupt; sudden; protrude",
                "meaning_es": "lanzarse; repentino; brusco; sobresalir",
                "radical": "穴",
                "radical_meaning_en": "cave",
                "meaning_component": "穴 (cave / hole)",
                "sound_component": "犬 (quǎn, dog rushing out)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient pictogram showing a hound 犬 suddenly darting out from a cave opening 穴, meaning abrupt emergence.",
                "visual_mnemonic_story_en": "A hound (犬) suddenly bursts out of a hidden burrow (穴), startling passersby with its sudden dash (突).",
                "visual_mnemonic_story_es": "Un sabueso (犬) sale disparado de golpe desde su cueva (穴), sorprendiendo con su brusca salida (突).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JCIK",
                "traditional": ""
            },
            {
                "character": "出",
                "pinyin": "chū",
                "meaning_en": "go out; come forth; produce; issue",
                "meaning_es": "salir; brotar; producir; emitir",
                "radical": "凵",
                "radical_meaning_en": "open container",
                "meaning_component": "凵 (hollow container/ground)",
                "sound_component": "屮 (chè, plant sprouting)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideogram showing a foot or plant sprout leaving an enclosed hollow, denoting outward progression.",
                "visual_mnemonic_story_en": "Two fresh leaves sprout upward out of a hollow recess in the ground, bursting out (出) toward the sun.",
                "visual_mnemonic_story_es": "Dos brotes tiernos germinan hacia arriba saliendo del hoyo (出) en busca del sol.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "UU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A spirited hound dashes out (突) and emerges outward (出), standing conspicuously prominent (突出).",
            "composite_memory_hook_es": "El sabueso se lanza repentinamente (突) y sale hacia afuera (出), destacando de modo sobresaliente (突出).",
            "cultural_and_cognitive_roots": "Originating from the imagery of an animal surging from an enclosure; extended metaphorically to any person or deed that rises above an otherwise uniform baseline.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by level high tone: 'tū chū' (55-55). Maintain a stable high plateau pitch throughout both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "究", "pinyin": "jiū", "meaning_en": "investigate; study", "distinction_note": "Has 九 below radical 穴 instead of 犬"},
                {"character": "空", "pinyin": "kōng", "meaning_en": "empty; sky", "distinction_note": "Has 工 below radical 穴 instead of 犬"},
                {"character": "击", "pinyin": "jī", "meaning_en": "strike; hit", "distinction_note": "Shares two tier vertical design, but lacks center crossing"},
                {"character": "山", "pinyin": "shān", "meaning_en": "mountain", "distinction_note": "Has three peaks on one base, unlike stacked 出"}
            ],
            "etymological_cognates": [
                {"character": "窜", "pinyin": "cuàn", "gloss_en": "scurry; flee in panic from holes"},
                {"character": "穿", "pinyin": "chuān", "gloss_en": "pierce; pass through caves"},
                {"character": "窝", "pinyin": "wō", "gloss_en": "nest; hollow den"},
                {"character": "入", "pinyin": "rù", "gloss_en": "enter; direct antonym of 出"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "突出 emphasizes exceeding normal standards or drawing distinct visual or conceptual focus.",
            "contrasts": [
                {"id": "1", "compared_word": "突出 vs. 显著", "pinyin": "xiǎnzhù", "analysis": "突出 highlights that a feature or achievement rises sharply above peers, while 显著 denotes that an effect or change is obvious and plainly discernible."},
                {"id": "2", "compared_word": "突出 vs. 优异", "pinyin": "yōuyì", "analysis": "突出 can describe either positive achievements or glaring problems, whereas 优异 is strictly reserved for praiseworthy and exceptional talent or grades."},
                {"id": "3", "compared_word": "突出 vs. 强调", "pinyin": "qiángdiào", "analysis": "突出 can function as both an adjective (prominent) and a verb (highlight), whereas 强调 is solely a verb meaning to stress or underline in speech or policy."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "优秀的艺术作品往往具有突出的个性风格。无论是画作中浓墨重彩的强烈对比，还是诗篇中真挚奔放的情感流淌，都能够从平庸的作品中脱颖而出。唯有保持本色，才能在岁月的长河中留下难以磨灭的印记。",
                "pinyin": "Yōuxiù de yìshù zuòpǐn wǎngwǎng jùyǒu tūchū de gèxìng fēnggé. Wúlùn shì huàzuò zhōng nóngmò-zhòngcǎi de qiángliè duìbǐ, háishì shīpiān zhōng zhēnzhì bēnfàng de qínggǎn liútǎng, dōu nénggòu cóng píngyōng de zuòpǐn zhōng tuōyǐng-érchū. Wéiyǒu bǎochí běnsè, cáinéng zài suìyuè de chánghé zhōng liúxià nányǐ mómì de yìnjì.",
                "en": "Masterpieces always possess outstanding unique character. Be it the stark contrast of thick ink or the earnest flow of poetic emotion, they stand out sharply from mediocrity. Only by keeping one's true colors can lasting marks be made.",
                "es": "Las grandes obras de arte poseen una personalidad sobresaliente. Ya sea mediante intensos contrastes cromáticos o versos de emoción sincera, despuntan por encima de lo común. Solo siendo fiel a la propia voz se deja una huella imperecedera."
            },
            {
                "id": "#2",
                "hanzi": "在产业转型升级的关键时期，技术创新的地位愈发突出。研发机构通过攻关核心算法与精密部件，解决了产业链上的突出问题。实践证明，谁在基础科学上拥有突出的原创能力，谁就能在国际竞争中抢占战略制高点。",
                "pinyin": "Zài chǎnyè zhuǎnxíng shēngjí de guānjiàn shíqī, jìshù chuàngxīn de dìwèi yùfā tūchū. Yánfā jīgòu tōngguò gōngguān héxīn suànfǎ yǔ jīngmì bùjiàn, jiějué le chǎnyèliàn shàng de tūchū wèntí. Shíjiàn zhèngmíng, shéi zài jīchǔ kēxué shàng yǒngyǒu tūchū de yuánchuàng nénglì, shéi jiù néng zài guójì jìngzhēng zhōng qiǎngzhàn zhànlüè zhìgāodiǎn.",
                "en": "In industrial transformation, technological innovation holds an ever more prominent place. Solving key bottlenecks in algorithms and parts has resolved prominent supply chain issues, proving foundational research commands strategic heights.",
                "es": "En la reconversión industrial, la innovación tecnológica adquiere un peso sobresaliente. Al resolver nudos críticos en algoritmos y componentes, se solventaron fallas notorias. La vanguardia científica otorga una ventaja decisiva."
            }
        ]
    },

    # 03 文学家
    {
        "id": "3",
        "hanzi": "文学家",
        "pinyin": "wén xué jiā",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "writer; man of letters; literary figure; author of renown",
            "es": "escritor; literato; hombre de letras; autor consagrado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a renowned specialist or author with significant achievements in literary creation or research",
                "definition_es": "persona consagrada a la creación o estudio de la literatura con obras de reconocido prestigio",
                "example_phrase": "杰出的文学家 (distinguished man of letters)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "鲁迅是中国近代著名的文学家和思想家，他的小说深刻解剖了旧社会的积弊与国民劣根性。",
                "pinyin": "Lǔ Xùn shì Zhōngguó jìndài zhùmíng de wénxuéjiā hé sīxiǎngjiā, tā de xiǎoshuō shēnkè jiěpōu le jiù shèhuì de jībì yǔ guómín liègènxìng.",
                "en": "Lu Xun was a celebrated modern Chinese writer and thinker; his fiction incisively dissected old societal ills and deep-seated mentalities.",
                "es": "Lu Xun fue un célebre literato y pensador chino moderno; sus relatos diseccionaron con lucidez los males de la antigua sociedad."
            },
            {
                "id": "#2",
                "hanzi": "真正伟大的文学家不仅用生花妙笔描摹世间百态，更通过作品启迪民众的灵魂与良知。",
                "pinyin": "Zhēnzhèng wěidà de wénxuéjiā bùjǐn yòng shēnghuā-miàobǐ miáomó shìjiān bǎitài, gèng tōngguò zuòpǐn qǐdí mínzhòng de línghún yǔ liángzhī.",
                "en": "Truly great literary authors not only depict human life with masterful pens, but enlighten the souls and consciences of the public through their works.",
                "es": "Los grandes hombres de letras no solo retratan la condición humana con maestría, sino que iluminan el alma y la conciencia colectiva."
            }
        ],
        "collocations": [
            {"hanzi": "著名文学家", "en": "famous man of letters"},
            {"hanzi": "近代文学家", "en": "modern literary writer"},
            {"hanzi": "伟大文学家", "en": "great literary master"},
            {"hanzi": "杰出文学家", "en": "distinguished writer"},
            {"hanzi": "文学家的故居", "en": "former residence of a literary figure"},
            {"hanzi": "青年文学家", "en": "young author"}
        ],
        "idioms": [
            {"hanzi": "文质彬彬", "pinyin": "wén zhì bīn bīn", "meaning_en": "refined in manner and gentle in speech"},
            {"hanzi": "才高八斗", "pinyin": "cái gāo bā dǒu", "meaning_en": "endowed with immense literary talent"},
            {"hanzi": "著作等身", "pinyin": "zhù zuò děng shēn", "meaning_en": "one's written works pile as high as one's height; prolific author"},
            {"hanzi": "自成一家", "pinyin": "zì chéng yì jiā", "meaning_en": "develop a unique, standalone school of thought or style"}
        ],
        "character_decomposition": [
            {
                "character": "文",
                "pinyin": "wén",
                "meaning_en": "culture; script; literature; gentle",
                "meaning_es": "cultura; escritura; literatura; refinado",
                "radical": "文",
                "radical_meaning_en": "pattern/script",
                "meaning_component": "文 (ritual body pattern / script)",
                "sound_component": "文 (wén)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram depicting patterned ritual chest tattoos, which later evolved into culture, literature, and writing.",
                "visual_mnemonic_story_en": "Ancient scholars drew elegant patterned characters on silk, establishing the bedrock of human literature (文).",
                "visual_mnemonic_story_es": "Los antiguos trazaron armoniosos caracteres sobre seda, fundando la civilización de las letras (文).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YK",
                "traditional": ""
            },
            {
                "character": "学",
                "pinyin": "xué",
                "meaning_en": "study; learn; scholarship; school",
                "meaning_es": "estudiar; aprender; saber; escuela",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (child under school roof)",
                "sound_component": "爻 (yáo, counting tallies)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient ideogram showing two hands guiding counting tallies above a child 子 in a roofed schoolroom.",
                "visual_mnemonic_story_en": "A child (子) sits beneath the roof, enthusiastically mastering books of learning and scholarship (学).",
                "visual_mnemonic_story_es": "Un niño (子) sentado bajo el tejado escolar adquiere con tesón el tesoro del saber (学).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "FBD",
                "traditional": "學"
            },
            {
                "character": "家",
                "pinyin": "jiā",
                "meaning_en": "family; home; master; specialist",
                "meaning_es": "familia; hogar; maestro; especialista",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (roof/house)",
                "sound_component": "豕 (shǐ, domestic pig / prosperity)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient pictogram showing a domestic pig 豕 sheltered beneath a solid roof 宀, signifying settled family life, extended to masters of a craft.",
                "visual_mnemonic_story_en": "Under a safe shelter roof (宀), precious domestic assets (豕) establish a settled home and an expert lineage (家).",
                "visual_mnemonic_story_es": "Bajo el techo (宀), criar cerdos (豕) representaba prosperidad familiar y la consolidación de un maestro (家).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JMO",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A master (家) who has mastered cultural script (文) and deep learning (学) becomes a true literary author (文学家).",
            "composite_memory_hook_es": "El maestro (家) que domina las bellas letras (文) y el saber profundo (学) se consagra como literato (文学家).",
            "cultural_and_cognitive_roots": "Suffix -jiā (家) historically designated prestigious intellectual schools (e.g., 儒家, 墨家) and recognized guild masters; appended to 'wénxué' it dignifies authorial authority.",
            "tone_sandhi_and_pitch_modulation": "Rising, rising, high: 'wén xué jiā' (35-35-55). Two smooth upward glides transitioning into a steady high tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "字", "pinyin": "zì", "meaning_en": "character; word", "distinction_note": "Has 宀 over 子, but lacks the upper three strokes of 学"},
                {"character": "冢", "pinyin": "zhǒng", "meaning_en": "mound; tomb", "distinction_note": "Has extra dot and slant stroke inside radical 冖"},
                {"character": "父", "pinyin": "fù", "meaning_en": "father", "distinction_note": "Has crossing diagonal strokes distinct from 文"},
                {"character": "豪", "pinyin": "háo", "meaning_en": "grand; heroic", "distinction_note": "Has top radical 亠 and 口 over 豕, distinct from 家"}
            ],
            "etymological_cognates": [
                {"character": "教", "pinyin": "jiào", "gloss_en": "teach; instruct students"},
                {"character": "考", "pinyin": "kǎo", "gloss_en": "examine; investigate scholarship"},
                {"character": "儒", "pinyin": "rú", "gloss_en": "Confucian scholar; literatus"},
                {"character": "宅", "pinyin": "zhái", "gloss_en": "residence; family manor"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "文学家 refers to recognized, accomplished figures in literature whose works have enduring aesthetic and cultural standing.",
            "contrasts": [
                {"id": "1", "compared_word": "文学家 vs. 作家", "pinyin": "zuòjiā", "analysis": "作家 is a common professional term for anyone who writes fiction or books, whereas 文学家 carries solemn cultural prestige denoting a historic literary master."},
                {"id": "2", "compared_word": "文学家 vs. 学者", "pinyin": "xuézhě", "analysis": "文学家 primarily creates imaginative literary prose, poetry, and drama, while 学者 conducts academic analysis, historical research, and theoretical critique."},
                {"id": "3", "compared_word": "文学家 vs. 文人", "pinyin": "wénrén", "analysis": "文人 describes the broad traditional socio-cultural class of educated intellectuals with artistic taste, while 文学家 denotes specific master-level authors."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在老北京青砖灰瓦的胡同深处，一代代文学家留下了浓墨重彩的文化印记。他们伏案疾书，用敏锐的文字记录下时代的悲欢离合。推开斑驳的朱红院门，庭院里的古槐似乎仍在轻声吟诵着昔日大师写下的不朽篇章。",
                "pinyin": "Zài lǎo Běijīng qīngzhuān-huīwǎ de hútòng shēnchù, yídàidài wénxuéjiā liúxià le nóngmò-zhòngcǎi de wénhuà yìnjì. Tāmen fú'àn-jíshū, yòng mǐnruì de wénzì jìlù xià shídài de bēihuān-líhé. Tuīkāi bānbó de zhūhóng yuànmén, tíngyuàn lǐ de gǔhuái sìhū réng zài qīngshēng yínsòng zhe xīrì dàshī xièxià de bùxiǔ piānzhāng.",
                "en": "In the alleys of old Beijing, generations of literary masters left vibrant cultural imprints. Leaning over desks, they recorded joys and sorrows of eras. Creaking open vermilion gates, ancient trees still whisper enduring lines.",
                "es": "En los callejones de Pekín, sucesivas generaciones de literatos forjaron un legado imborrable. En sus escritorios plasmaron las vicisitudes de su era. Al abrir los portones de madera, las viejas acacias parecen susurrar aquellos textos inmortales."
            },
            {
                "id": "#2",
                "hanzi": "中国近代文学家的作品不仅推动了白话文运动的蓬勃普及，更为民族精神的觉醒注入了强劲动力。从《呐喊》到《彷徨》，鲁迅等文学先驱以笔为戈，深刻审视民族历史命运，奠定了现代人文思想的精神基石。",
                "pinyin": "Zhōngguó jìndài wénxuéjiā de zuòpǐn bùjǐn tuīdòng le báihuàwén yùndòng de péngbó pǔjí, gèng wèi mínzú jīngshén de juéxǐng zhùrù le qiángjìn dònglì. Cóng 《Nàhǎn》 dào 《Pánghuáng》, Lǔ Xùn děng wénxué xiānqū yǐ bǐ wéi gē, shēnkè shěnshì mínzú lìshǐ mìngyùn, diàndìng le xiàndài rénwén sīxiǎng de jīngshén jīshí.",
                "en": "Works of modern Chinese writers spurred the vernacular language movement and invigorated national awakening. From 'Call to Arms' to 'Wandering', literary pioneers scrutinized history with their pens, laying humanistic cornerstones.",
                "es": "Las creaciones de los literatos modernos impulsaron el uso de la lengua vernácula y el renacer nacional. Con obras como 'Gritos', pioneros como Lu Xun empuñaron la pluma para reflexionar sobre el destino del país, cimentando el humanismo."
            }
        ]
    },

    # 04 算
    {
        "id": "4",
        "hanzi": "算",
        "pinyin": "suàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to count; to calculate; to regard as; to pass as; at last; finally",
            "es": "contar; calcular; considerar; calificar como; al fin; por fin"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to calculate, compute arithmetic figures, or plan strategically",
                "definition_es": "calcular, computar cifras aritméticas o planificar",
                "example_phrase": "算一笔账 (calculate the accounts)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to consider, count as, or pass muster as meeting a certain criterion",
                "definition_es": "considerar, tener por o calificar como alguien o algo que cumple un criterio",
                "example_phrase": "算是个行家 (considered an expert)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经过反复核算，这笔家庭开支总算达到了收支平衡，让父母松了一大口气。",
                "pinyin": "Jīngguò fǎnfù hésuàn, zhè bǐ jiātíng kāizhī zǒngsuàn dádào le shōuzhī pínghéng, ràng fùmǔ sōng le yí dà kǒuqì.",
                "en": "After repeated recalculations, these household expenses finally balanced out, allowing the parents to breathe a sigh of relief.",
                "es": "Tras repetidos cálculos, los gastos domésticos al fin quedaron equilibrados, lo que brindó un hondo alivio a los padres."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅先生对各大菜系的烹饪技法了如指掌，在饮食文化上绝对算得上是一位地道的行家。",
                "pinyin": "Lǔ Xùn xiānsheng duì gèdà càixì de pēngrèn jìfǎ liǎorú-zhǐzhǎng, zài yǐnshí wénhuà shàng juéduì suàndeshàng shì yí wèi dìdao de hángjia.",
                "en": "Mr. Lu Xun was intimately familiar with culinary techniques across regional cuisines; he can certainly be regarded as an authentic connoisseur.",
                "es": "El señor Lu Xun conocía las técnicas de las cocinas regionales al dedillo; en cultura gastronómica califica como un auténtico entendido."
            }
        ],
        "collocations": [
            {"hanzi": "算得上", "en": "can be counted as; pass as"},
            {"hanzi": "总算", "en": "at long last; finally"},
            {"hanzi": "说了算", "en": "have the final say"},
            {"hanzi": "算账", "en": "settle accounts; calculate costs"},
            {"hanzi": "算是", "en": "can be considered; at least is"},
            {"hanzi": "划算", "en": "worthwhile; cost-effective"}
        ],
        "idioms": [
            {"hanzi": "精打细算", "pinyin": "jīng dǎ xì suàn", "meaning_en": "meticulous planning and careful budgeting"},
            {"hanzi": "心怀叵测", "pinyin": "xīn huái pǒ cè", "meaning_en": "harbor unpredictable, malicious schemes"},
            {"hanzi": "满打满算", "pinyin": "mǎn dǎ mǎn suàn", "meaning_en": "at the very most; counting generously"},
            {"hanzi": "失算", "pinyin": "shī suàn", "meaning_en": "miscalculation; bad judgment"}
        ],
        "character_decomposition": [
            {
                "character": "算",
                "pinyin": "suàn",
                "meaning_en": "calculate; reckon; consider; plan",
                "meaning_es": "calcular; computar; considerar; planear",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo counting tallies / rods)",
                "sound_component": "目 (mù, eye inspecting tallies) + 廾 (two hands)",
                "stroke_count": 14,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient ideogram showing two hands 廾 arranging bamboo counting rods 竹 while the eye 目 inspects the calculation.",
                "visual_mnemonic_story_en": "Two hands manipulate bamboo counting sticks (竹) under watchful eyes (目) to calculate precise tallies (算).",
                "visual_mnemonic_story_es": "Dos manos ordenan varillas de bambú (竹) bajo la atenta mirada (目) para calcular con exactitud (算).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HBUC",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Align bamboo calculating rods (竹) under observant eyes (目) to calculate and count someone as qualified (算).",
            "composite_memory_hook_es": "Alinea las varas de cálculo (竹) ante los ojos (目) para computar y calificar a alguien de experto (算).",
            "cultural_and_cognitive_roots": "Derived from ancient Chinese rod calculus (筹算); moving counting rods led to the metaphor of cognitive estimation, strategic reckoning, and legal qualification.",
            "tone_sandhi_and_pitch_modulation": "Sharp falling tone: 'suàn' (51). Deliver with a crisp descending strike without drawling."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "鼻", "pinyin": "bí", "meaning_en": "nose", "distinction_note": "Has 自 at the top instead of 竹"},
                {"character": "笄", "pinyin": "jī", "meaning_en": "hairpin", "distinction_note": "Has 开 below 竹 instead of the complex lower matrix of 算"},
                {"character": "符", "pinyin": "fú", "meaning_en": "symbol; tally", "distinction_note": "Has 付 below radical 竹"},
                {"character": "等", "pinyin": "děng", "meaning_en": "wait; equal", "distinction_note": "Has 寺 below radical 竹 instead of 目 and 廾"}
            ],
            "etymological_cognates": [
                {"character": "筹", "pinyin": "chóu", "gloss_en": "counting tally; chip; plan"},
                {"character": "简", "pinyin": "jiǎn", "gloss_en": "bamboo slip; concise letter"},
                {"character": "计", "pinyin": "jì", "gloss_en": "count; plan; strategy"},
                {"character": "数", "pinyin": "shǔ", "gloss_en": "count numbers sequentially"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "算 denotes either cognitive/mathematical calculation or subjectively evaluating someone as meeting an informal classification.",
            "contrasts": [
                {"id": "1", "compared_word": "算 vs. 计算", "pinyin": "jìsuàn", "analysis": "算 is widely used colloquially for both arithmetic and qualitative judgment ('算是'), whereas 计算 is a formal verb restricted to mathematical or technical computation."},
                {"id": "2", "compared_word": "算 vs. 认为", "pinyin": "rènwéi", "analysis": "算 indicates an objective or grudging concession of qualification ('勉强算'), while 认为 expresses an explicit conscious belief or argument."},
                {"id": "3", "compared_word": "算 vs. 打算", "pinyin": "dǎsuàn", "analysis": "算 alone can mean finally or counting as, whereas 打算 specifically functions as an intention or future plan ('to intend to')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫漫人生路，究竟怎样才算不虚此行？有人耗尽心力计算名利的得失，到头来却身心俱疲；有人寄情山水淡泊明志，反倒在宁静中收获了丰盈的喜乐。唯有遵从本心，珍惜当下的每一寸光阴，生命才算真正活得通透坦然。",
                "pinyin": "Mànmàn rénshēng lù, jiūjìng zènyàng cái suàn bùxū-cǐxíng? Yǒurén hàojìn xīnlì jìsuàn mínglì de déshī, dàotóulái què shēnxīn-jùpí; yǒurén jìqíng-shānshuǐ dànbó-míngzhì, fǎndào zài níngjìng zhōng shōuhuò le fēngyíng de xǐlè. Wéiyǒu zūncóng běnxīn, zhēnxī dāngxià de měi yí cùn guāngyīn, shēngmìng cái suàn zhēnzhèng huó de tōngtòu tǎnrán.",
                "en": "On life's long path, what counts as living without regret? Some exhaust themselves calculating fame and profit, ending in fatigue; others love nature and find joy. Only following one's heart and treasuring the present makes life genuinely fulfilled.",
                "es": "¿Qué se considera vivir plenamente? Algunos agotan sus fuerzas calculando ganancias mundanas, quedando extenuados; otros prefieren la calma natural y hallan paz. Solo viviendo según la propia conciencia el camino cuenta como auténtico."
            },
            {
                "id": "#2",
                "hanzi": "民国时期的文人日记，算得上是一部鲜活生动的微观社会史。学者们统计鲁迅日记中记载的数百次宴请记录，细致测算当年的物价水准与文人收入构成。这些详实账目为研究近代知识分子的日常生活，提供了极具学术价值的实证依据。",
                "pinyin": "Mínguó shíqī de wénrén rìjì, suàndeshàng shì yí bù xiānhuó shēngdòng de wēiguān shèhuìshǐ. Xuézhěmen tǒngjì Lǔ Xùn rìjì zhōng jìzǎi de shùbǎi cì yànqǐng jìlù, xìzhì cèsuàn dāngnián de wùjià shuǐzhǔn yǔ wénrén shōurù gòuchéng. Zhèxiē xiángshí zhàngmù wèi yánjiū jìndài zhīshifènzǐ de rìcháng shēnghuó, tígōng le jí jù xuéshù jiàzhí de shídzhèng yījù.",
                "en": "Diaries of the Republican era pass as vivid micro-histories. Scholars analyze Lu Xun's hundreds of dining entries, calculating price levels and intellectual income, yielding empirical evidence for modern social research.",
                "es": "Los diarios de la época republicana califican como una viva microhistoria. Los investigadores compilan los banquetes anotados por Lu Xun para calcular el coste de vida y los honorarios, aportando datos de gran valor historiográfico."
            }
        ]
    },

    # 05 地道
    {
        "id": "5",
        "hanzi": "地道",
        "pinyin": "dì dao",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "authentic; genuine; typical; pure; up to standard; honest",
            "es": "auténtico; genuino; castizo; típico; intachable; cabal"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "authentic, pure, or conforming perfectly to traditional native origins and flavors",
                "definition_es": "auténtico, puro o que responde con fidelidad al sabor y estilo tradicional de origen",
                "example_phrase": "地道的北京烤鸭 (authentic Beijing roast duck)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Colloquial",
                "definition_en": "honest, fair-minded, or morally upright in character and business dealings",
                "definition_es": "honesto, cabal, intachable o leal en el trato personal",
                "example_phrase": "为人很地道 (very upright and honest person)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这位外国留学生在北京生活了十年，不仅能说一口地道的京腔，连待人接物的规矩都十分讲究。",
                "pinyin": "Zhè wèi wàiguó liúxuéshēng zài Běijīng shēnghuó le shí nián, bùjǐn néng shuō yì kǒu dìdao de jīngqiāng, lián dàirén-jiēwù de guīju dōu shífēn jiǎngjiu.",
                "en": "This foreign student has lived in Beijing for ten years; he speaks authentic local slang and is deeply mindful of etiquette.",
                "es": "Este estudiante extranjero lleva diez años en Pekín; no solo habla un acento pekinés auténtico, sino que cuida todas las costumbres."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在北京定居期间，常去宣武门外的老字号饭馆，品尝地道的北方炸酱面与绍兴故乡的传统黄酒。",
                "pinyin": "Lǔ Xùn zài Běijīng dìngjū qījiān, cháng qù Xuānwǔmén wài de lǎozìhào fànguǎn, pǐncháng dìdao de běifāng zhàjiàngmiàn yǔ Shàoxīng gùxiāng de chuántǒng huángjiǔ.",
                "en": "While residing in Beijing, Lu Xun frequented heritage restaurants to savor authentic northern Zhajiang noodles and Shaoxing rice wine.",
                "es": "Durante su estancia en Pekín, Lu Xun frecuentaba mesones tradicionales para degustar auténticos fideos norteños y vino añejo de Shaoxing."
            }
        ],
        "collocations": [
            {"hanzi": "地道的口音", "en": "authentic accent"},
            {"hanzi": "地道的美食", "en": "authentic delicacy"},
            {"hanzi": "地道普通话", "en": "standard, authentic Mandarin"},
            {"hanzi": "为人地道", "en": "morally upright and honest person"},
            {"hanzi": "做工地下/地道", "en": "exquisite and genuine craftsmanship"},
            {"hanzi": "地道特产", "en": "authentic local specialty"}
        ],
        "idioms": [
            {"hanzi": "原汁原味", "pinyin": "yuán zhī yuán wèi", "meaning_en": "original flavor and aroma; completely authentic"},
            {"hanzi": "名副其实", "pinyin": "míng fù qí shí", "meaning_en": "worthy of the name; genuine reality matching the title"},
            {"hanzi": "货真价实", "pinyin": "huò zhēn jià shí", "meaning_en": "genuine goods at a fair price; authentic through and through"},
            {"hanzi": "言传身教", "pinyin": "yán chuán shēn jiào", "meaning_en": "teach by both word and genuine personal example"}
        ],
        "character_decomposition": [
            {
                "character": "地",
                "pinyin": "dì",
                "meaning_en": "earth; soil; place; land; ground",
                "meaning_es": "tierra; suelo; lugar; territorio",
                "radical": "土",
                "radical_meaning_en": "earth",
                "meaning_component": "土 (soil/land)",
                "sound_component": "也 (yě, phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where earth radical 土 represents the soil of the terrain and 也 acts as the phonetic harmony.",
                "visual_mnemonic_story_en": "Mounds of fertile soil (土) extend across the vast landscape (也) creating stable ground (地).",
                "visual_mnemonic_story_es": "Montículos de tierra fértil (土) se extienden por el terreno (也) formando suelo firme (地).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GPD",
                "traditional": ""
            },
            {
                "character": "道",
                "pinyin": "dào",
                "meaning_en": "road; way; doctrine; say; direction",
                "meaning_es": "camino; vía; doctrina; decir; dirección",
                "radical": "辶",
                "radical_meaning_en": "walk",
                "meaning_component": "辶 (motion along a road)",
                "sound_component": "首 (shǒu, head / direction)",
                "stroke_count": 12,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Ideogram showing an eye and head 首 leading the body along a path 辶, meaning walking in the correct rightful direction.",
                "visual_mnemonic_story_en": "Keeping your head (首) forward as you walk along the path (辶) ensures you follow the true proper way (道).",
                "visual_mnemonic_story_es": "Caminar con la cabeza (首) erguida a lo largo de la senda (辶) conduce por la vía correcta (道).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YTBU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Only what grows directly from native soil (地) along the proper path (道) is truly authentic (地道).",
            "composite_memory_hook_es": "Solo lo que brota del suelo natal (地) siguiendo la debida senda (道) resulta auténtico (地道).",
            "cultural_and_cognitive_roots": "Originally rooted in the traditional concept of 'dìdao yàocái' (authentic herbs native to specific terroirs); extended to language, culinary flavors, and honest personal character.",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by neutral tone: 'dì dao' (51-2). Articulate 'dì' firmly on pitch 51, and drop 'dao' softly into a low neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "池", "pinyin": "chí", "meaning_en": "pool; pond", "distinction_note": "Has water radical 氵 instead of 土"},
                {"character": "驰", "pinyin": "chí", "meaning_en": "gallop; speed", "distinction_note": "Has horse radical 马 instead of 土"},
                {"character": "导", "pinyin": "dǎo", "meaning_en": "guide; direct", "distinction_note": "Has 寸 at bottom instead of walking radical 辶"},
                {"character": "通", "pinyin": "tōng", "meaning_en": "pass through; open", "distinction_note": "Has 甬 inside 辶 instead of 首"}
            ],
            "etymological_cognates": [
                {"character": "基", "pinyin": "jī", "gloss_en": "foundation; soil base"},
                {"character": "垠", "pinyin": "yín", "gloss_en": "boundary; border of land"},
                {"character": "途", "pinyin": "tú", "gloss_en": "route; journey on foot"},
                {"character": "径", "pinyin": "jìng", "gloss_en": "direct path; shortcut"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "地道 specifically emphasizes genuine local provenance, traditional craftsmanship, or uncorrupted pure native style.",
            "contrasts": [
                {"id": "1", "compared_word": "地道 vs. 正宗", "pinyin": "zhèngzōng", "analysis": "正宗 highlights authoritative lineage and orthodox recipes ('正宗传人'), while 地道 focuses on unadulterated native flavor, accent, or honest conduct."},
                {"id": "2", "compared_word": "地道 vs. 真正", "pinyin": "zhēnzhèng", "analysis": "真正 denotes that an object is real rather than fake in an ontological sense, whereas 地道 denotes high quality conformity to cultural tradition."},
                {"id": "3", "compared_word": "地道 vs. 纯正", "pinyin": "chúnzhèng", "analysis": "纯正 stresses freedom from adulteration or ideological taint, while 地道 carries a rich, colloquial, grassroots flavor of regional life."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "寻味一座城市最地道的人间烟火，往往不需要流连于豪华饭店。清晨拐进胡同深处的小吃铺，一碗热气腾腾的豆汁，配上金黄酥脆的焦圈，那浓郁而朴实的乡土滋味，才是老街坊心中无可替代的真地道。",
                "pinyin": "Xúnwèi yí zuò chéngshì zuì dìdao de rénjiān yānhuǒ, wǎngwǎng bù xūyào liúlián yú háohuá fàndiàn. Qīngchén guǎijìn hútòng shēnchù de xiǎochīpù, yì wǎn rèqì-téngténg de dòuzhī, pèishàng jīnhuáng sūcuì de jiāojuān, nà nóngyù ér pǔshí de xiāngtǔ zīwèi, cáishì lǎo jiēfang xīnzhōng wúkě-tìdài de zhēn dìdao.",
                "en": "Seeking a city's authentic pulse rarely requires luxury dining. Turning into an alley stall for steaming fermented milk with crisp rings, that earthy local flavor is the irreplaceable genuine article cherished by longtime residents.",
                "es": "Para saborear lo más castizo de una ciudad no hace falta acudir al lujo. Basta doblar la esquina hacia un puesto matutino en el callejón: un tazón humeante con buñuelos dorados brinda ese entrañable sabor que los vecinos veneran."
            },
            {
                "id": "#2",
                "hanzi": "语言学习的最高境界在于掌握地道的文化语境。单纯背诵语法规则和词汇表，往往难以摆脱生硬的母语负迁移。唯有多听多练，积极融入本土社交场域，才能在潜移默化中说出一口流利地道、符合母语者习惯的中文。",
                "pinyin": "Yǔyán xuéxí de zuìgāo jìngjiè zàiyú zhǎngwò dìdao de wénhuà yǔjìng. Dānchún bèisòng yǔfǎ guīzé hé cíhuìbiǎo, wǎngwǎng nányǐ bǎituō shēngyìng de mǔyǔ fùqiānyí. Wéiyǒu duō tīng duō liàn, jījí róngrù běntǔ shèjiāo chǎngyù, cáinéng zài qiányí-mòhuà zhōng shuōchū yì kǒu liúlì dìdao, fúhé mǔyǔzhě xíguàn de Zhōngwén.",
                "en": "The pinnacle of language learning lies in mastering authentic cultural context. Rote memorization cannot shake off mother-tongue interference. Only by immersion can one naturally speak fluent, authentic Chinese matching native habits.",
                "es": "La cima del aprendizaje de idiomas estriba en dominar el contexto cultural genuino. Memorizar reglas gramaticales suele generar calcos rígidos. Solo practicando e integrándose en el entorno social se logra hablar con naturalidad castiza."
            }
        ]
    },

    # 06 行家
    {
        "id": "6",
        "hanzi": "行家",
        "pinyin": "háng jia",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "expert; connoisseur; professional; insider",
            "es": "experto; perito; entendido; conocedor; profesional"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person thoroughly skilled, experienced, and knowledgeable in a specific trade, art, or field",
                "definition_es": "persona muy versada, ducha y experimentada en determinado oficio, arte o disciplina",
                "example_phrase": "内行是行家 (an insider is an expert)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "李师傅在古董玉石行业摸爬滚打了几十年，只要上手一摸，行家一出手便知真假。",
                "pinyin": "Lǐ shīfu zài gǔdǒng yùshí hángyè mōpá-gǔndǎ le jǐshí nián, zhǐyào shàngshǒu yì mō, hángjia yì chūshǒu biàn zhī zhēnjiǎ.",
                "en": "Master Li has worked in antiques and jades for decades; with a single touch, the expert immediately discerns the real from fake.",
                "es": "El maestro Li lleva décadas en el gremio de las antigüedades; apenas palpa una pieza, el entendido distingue lo falso de lo legítimo."
            },
            {
                "id": "#2",
                "hanzi": "在朋友眼中，鲁迅不仅文章写得极具锋芒，在品鉴各大名菜和选购点心上更是一位极具眼光的行家。",
                "pinyin": "Zài péngyou yǎnzhōng, Lǔ Xùn bùjǐn wénzhāng xiě de jí jù fēngmáng, zài pǐnjiàn gèdà míngcài hé xuǎngòu diǎnxin shàng gèng shì yí wèi jí jù yǎnguāng de hángjia.",
                "en": "To his friends, Lu Xun not only wrote incisive essays, but was a discerning connoisseur when sampling famous dishes and pastries.",
                "es": "A ojos de sus amigos, Lu Xun no solo escribía prosa mordaz, sino que al catar delicias y comprar repostería era un consumado experto."
            }
        ],
        "collocations": [
            {"hanzi": "真正的行家", "en": "true connoisseur"},
            {"hanzi": "行业行家", "en": "industry expert"},
            {"hanzi": "行家指点", "en": "guidance from an expert"},
            {"hanzi": "美食行家", "en": "gourmet connoisseur"},
            {"hanzi": "古玩行家", "en": "antique expert"},
            {"hanzi": "行家一出手", "en": "as soon as the expert takes action"}
        ],
        "idioms": [
            {"hanzi": "行家里手", "pinyin": "háng jiā lǐ shǒu", "meaning_en": "master of one's trade; seasoned expert"},
            {"hanzi": "驾轻就熟", "pinyin": "jià qīng jiù shú", "meaning_en": "handle an easy task with familiar ease"},
            {"hanzi": "游刃有余", "pinyin": "yóu rèn yǒu yú", "meaning_en": "handle with skill and room to spare; effortless mastery"},
            {"hanzi": "庖丁解牛", "pinyin": "páo dīng jiě niú", "meaning_en": "dissect an ox with consummate technical artistry"}
        ],
        "character_decomposition": [
            {
                "character": "行",
                "pinyin": "háng",
                "meaning_en": "line; trade; profession; business firm",
                "meaning_es": "fila; gremio; oficio; profesión; negocio",
                "radical": "行",
                "radical_meaning_en": "go / crossroads",
                "meaning_component": "彳 (step / left road junction)",
                "sound_component": "亍 (chù, right road junction)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram of a four-way road crossroads; extended to shops lined along roads, and hence lines of business.",
                "visual_mnemonic_story_en": "Rows of shops line the busy four-way street intersection (行), forming professional trade guilds (行).",
                "visual_mnemonic_story_es": "Hileras de tiendas flanquean el cruce de caminos (行), conformando los gremios profesionales (行).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HONN",
                "traditional": ""
            },
            {
                "character": "家",
                "pinyin": "jia",
                "meaning_en": "specialist; person skilled in a craft",
                "meaning_es": "especialista; maestro de un quehacer",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (household/lineage)",
                "sound_component": "豕 (shǐ, pig / domestic wealth)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Denotes an accomplished practitioner belonging to an established school or master's lineage.",
                "visual_mnemonic_story_en": "Inside the master's studio house (宀), a seasoned expert (家) trains disciples in the craft.",
                "visual_mnemonic_story_es": "Bajo el techo del taller (宀), el maestro (家) guía a los aprendices en el dominio del oficio.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "JMO",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A master (家) who has mastered every street and guild of the trade (行) is a true expert (行家).",
            "composite_memory_hook_es": "El maestro (家) que conoce al dedillo los secretos del gremio (行) es un verdadero perito (行家).",
            "cultural_and_cognitive_roots": "In imperial Chinese cities, artisans and merchants formed trade associations called 'háng' (行) along designated streets; an acknowledged master within the guild was titled 'hángjia'.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by neutral/level tone: 'háng jia' (35-2 or 35-55). Syllable 'háng' rises cleanly, and 'jia' is lightened in colloquial speech."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "待", "pinyin": "dài", "meaning_en": "wait; treat", "distinction_note": "Has 彳 on left, but 寺 on right instead of 亍"},
                {"character": "街", "pinyin": "jiē", "meaning_en": "street", "distinction_note": "Has 圭 inserted in the center of 行"},
                {"character": "律", "pinyin": "lǜ", "meaning_en": "law; rhythm", "distinction_note": "Has 聿 on right instead of 亍"},
                {"character": "徒", "pinyin": "tú", "meaning_en": "disciple; apprentice", "distinction_note": "Has 走 on right; direct semantic counterpart to 行家"}
            ],
            "etymological_cognates": [
                {"character": "术", "pinyin": "shù", "gloss_en": "art; skill; technique along roads"},
                {"character": "途", "pinyin": "tú", "gloss_en": "path; career avenue"},
                {"character": "业", "pinyin": "yè", "gloss_en": "enterprise; occupational line"},
                {"character": "匠", "pinyin": "jiàng", "gloss_en": "craftsman; master artisan"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "行家 emphasizes practical savvy, trade secrets, and acute connoisseurship gained through long hands-on immersion.",
            "contrasts": [
                {"id": "1", "compared_word": "行家 vs. 专家", "pinyin": "zhuānjiā", "analysis": "专家 emphasizes institutional academic credentials and formal scientific theory, whereas 行家 highlights practical trade experience, discerning taste, and street wisdom."},
                {"id": "2", "compared_word": "行家 vs. 内行", "pinyin": "nèiháng", "analysis": "内行 is frequently used as an adjective meaning knowledgeable or competent (vs. 外行), while 行家 is primarily a noun denoting the expert person."},
                {"id": "3", "compared_word": "行家 vs. 高手", "pinyin": "gāoshǒu", "analysis": "高手 emphasizes exceptional physical skill or competitive prowess, whereas 行家 stresses analytical discernment, connoisseurship, and appraisal."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "品茶论道最讲究心境与眼力。真正的行家端起茶盏，先观汤色之澄澈，再嗅香气之幽微，最后轻啜一口品味回甘的层次。外行看热闹，内行看门道，那种只可意会不可言传的韵味，只有久经熏陶的行家方能心领神会。",
                "pinyin": "Pǐnchá lùndào zuì jiǎngjiu xīnjìng yǔ yǎnlì. Zhēnzhèng de hángjia duānqǐ cházhǎn, xiān guān tāngsè zhī chéngchè, zài xiù xiāngqì zhī yōuwēi, zuìhòu qīngchuò yì kǒu pǐnwèi huígān de céngcì. Wàiháng kàn rènào, nèiháng kàn méndào, nà zhǒng zhǐ kě yìhuì bù kě yánchuán de yùnwèi, zhǐyǒu jiǔjīng-xūntáo de hángjia fāng néng xīnlǐng-shénhuì.",
                "en": "Tasting tea demands tranquility and sharp eyes. An expert lifts the cup to inspect clarity, smell subtle aromas, and sip for multi-layered sweetness. While novices watch the surface, true connoisseurs grasp subtle depths intuitively.",
                "es": "Catar té requiere serenidad y ojo clínico. El entendido toma la taza, observa la nitidez del licor, inhala el aroma y da un sorbo para saborear el dulzor de fondo. Quien no sabe mira de lejos; solo el experto versado capta la sutil armonía."
            },
            {
                "id": "#2",
                "hanzi": "在快速更迭的数字经济浪潮中，各行各业都渴求兼具前沿视野与实操经验的行家。优秀的顾问能够一针见血地指出商业模式的漏洞，并提出行之有效的优化方案。正是这些行家的深度参与，有力护航了初创企业的稳健发展。",
                "pinyin": "Zài kuàisù gēngdié de shùzì jīngjì làngcháo zhōng, gèháng-gèyè dōu kěqiú jiānjù qiányán shìyě yǔ shícāo jīngyàn de hángjia. Yōuxiù de gùwèn nénggòu yìzhēn-jiànxiě de zhǐchū shāngyè móshì de lòudòng, bìng tíchū xíngzhī-yǒuxiào de yōuhuà fāng'àn. Zhèng shì zhèxiē hángjia de shēndù cānyù, yǒulì hùháng le chūchuàng qǐyè de wěnjiàn fāzhǎn.",
                "en": "Amid digital economic waves, industries seek seasoned professionals combining vision with operational savvy. Outstanding advisors pinpoint business flaws and propose viable solutions, safeguarding startup growth through deep involvement.",
                "es": "En la veloz economía digital, los sectores demandan peritos con visión y pericia práctica. Los consultores brillantes detectan fallas al vuelo y ofrecen soluciones viables. Su decisiva aportación afianza el crecimiento de las nuevas empresas."
            }
        ]
    },

    # 07 亲自
    {
        "id": "7",
        "hanzi": "亲自",
        "pinyin": "qīn zì",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "personally; in person; oneself (without proxy)",
            "es": "personalmente; en persona; por sí mismo (sin intermediarios)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "doing an action in person oneself, rather than delegating it to subordinates or agents",
                "definition_es": "realizar una acción en persona uno mismo, sin delegarla en terceros o subordinados",
                "example_phrase": "亲自主持会议 (personally chair the meeting)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "为了表达对远道而来客人的诚意，总经理亲自驾车前往机场迎接，令客户深受感动。",
                "pinyin": "Wèile biǎodá duì yuǎndào-érlái kèrén de chéngyì, zǒngjīnglǐ qīnzì jiàchē qiánwǎng jīchǎng yíngjiē, lìng kèhù shēnshòu gǎndòng.",
                "en": "To express sincere hospitality to guests traveling from afar, the general manager personally drove to the airport to welcome them, deeply touching the clients.",
                "es": "Para mostrar sincera cortesía a los huéspedes que venían de lejos, el director general condujo él mismo hasta el aeropuerto a recibirlos."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅不仅爱吃会吃，周末闲暇时还常常亲自下厨掌勺，为前来做客的年轻朋友们烹制家乡美味。",
                "pinyin": "Lǔ Xùn bùjǐn àichī huìchī, zhòumò xiánxiá shí hái chángcháng qīnzì xiàchú zhǎngsháo, wèi qiánlái zuòkè de niánqīng péngyoumen pēngzhì jiāxiāng měiwèi.",
                "en": "Lu Xun not only enjoyed fine cuisine, but frequently cooked in person on weekends, preparing hometown delicacies for visiting young friends.",
                "es": "Lu Xun no solo disfrutaba de la gastronomía, sino que en sus fines de semana solía meterse en persona a la cocina para agasajar a sus amigos."
            }
        ],
        "collocations": [
            {"hanzi": "亲自出席", "en": "attend in person"},
            {"hanzi": "亲自参与", "en": "participate personally"},
            {"hanzi": "亲自下厨", "en": "cook in person in the kitchen"},
            {"hanzi": "亲自过问", "en": "inquire into personally"},
            {"hanzi": "亲自体验", "en": "experience firsthand"},
            {"hanzi": "亲自带队", "en": "lead the team in person"}
        ],
        "idioms": [
            {"hanzi": "身体力行", "pinyin": "shēn tǐ lì xíng", "meaning_en": "practice what one preaches; carry out personally"},
            {"hanzi": "事必躬亲", "pinyin": "shì bì gōng qīn", "meaning_en": "attend to everything personally; take care of all details oneself"},
            {"hanzi": "微服私访", "pinyin": "wēi fú sī fǎng", "meaning_en": "travel incognito to investigate conditions firsthand"},
            {"hanzi": "耳闻目睹", "pinyin": "ěr wén mù dǔ", "meaning_en": "hear with one's ears and see with one's own eyes"}
        ],
        "character_decomposition": [
            {
                "character": "亲",
                "pinyin": "qīn",
                "meaning_en": "close; parent; intimate; in person; kiss",
                "meaning_es": "pariente; íntimo; en persona; besar",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "立 (stand on feet) + 木 (tree/parent)",
                "sound_component": "见 (jiàn, see / present in traditional 親)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Traditional 親 shows standing 立 atop wood 木 to look out 见 affectionately for returning loved ones.",
                "visual_mnemonic_story_en": "A loving parent stands tall (立) on the threshold waiting to greet loved ones intimately in person (亲).",
                "visual_mnemonic_story_es": "Un progenitor devoto se pone en pie (立) para aguardar con afecto la llegada del ser querido (亲).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YKD",
                "traditional": "親"
            },
            {
                "character": "自",
                "pinyin": "zì",
                "meaning_en": "self; oneself; from; origin",
                "meaning_es": "uno mismo; propio; desde; origen",
                "radical": "自",
                "radical_meaning_en": "nose / self",
                "meaning_component": "自 (pictogram of the human nose)",
                "sound_component": "自 (zì)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictogram of the human nose; in Chinese gesture, pointing to one's nose signifies 'myself'.",
                "visual_mnemonic_story_en": "A person points directly to their nose (自) to indicate: 'I did this completely by myself!'",
                "visual_mnemonic_story_es": "Alguien se señala la nariz (自) con el dedo índice para recalcar: '¡Lo hice yo mismo!'",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HBU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Step forward with close care (亲) and point to yourself (自) to do the vital job in person (亲自).",
            "composite_memory_hook_es": "Acércate con afecto (亲) y señálate a ti mismo (自) para realizar la tarea en persona (亲自).",
            "cultural_and_cognitive_roots": "In high-context Chinese culture, doing something 'qīnzì' (rather than sending an assistant) demonstrates extraordinary respect, humility, or utmost importance.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'qīn zì' (55-51). Articulate 'qīn' with a high pitch, dropping crisply into 4th tone 'zì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "白", "pinyin": "bái", "meaning_en": "white", "distinction_note": "Lacks the extra horizontal stroke inside 自"},
                {"character": "目", "pinyin": "mù", "meaning_en": "eye", "distinction_note": "Lacks the top diagonal dot stroke that 自 possesses"},
                {"character": "辛", "pinyin": "xīn", "meaning_en": "toilsome; bitter", "distinction_note": "Has 十 at bottom instead of the lower strokes of 亲"},
                {"character": "新", "pinyin": "xīn", "meaning_en": "new; fresh", "distinction_note": "Has axe radical 斤 on the right side of 亲"}
            ],
            "etymological_cognates": [
                {"character": "躬", "pinyin": "gōng", "gloss_en": "body; bow personally"},
                {"character": "己", "pinyin": "jǐ", "gloss_en": "oneself; private self"},
                {"character": "吾", "pinyin": "wú", "gloss_en": "I; myself"},
                {"character": "近", "pinyin": "jìn", "gloss_en": "near; intimate closeness"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "亲自 emphasizes the non-delegation of duty, underscoring that a principal figure acted without proxies.",
            "contrasts": [
                {"id": "1", "compared_word": "亲自 vs. 自己", "pinyin": "zìjǐ", "analysis": "自己 is a reflexive pronoun ('myself / himself'), while 亲自 is an adverb strictly modifying verbs to stress that an authoritative person did not delegate the action."},
                {"id": "2", "compared_word": "亲自 vs. 亲身", "pinyin": "qīnshēn", "analysis": "亲自 modifies proactive actions taken by someone ('亲自接待'), whereas 亲身 typically modifies passive experiences undergone ('亲身经历')."},
                {"id": "3", "compared_word": "亲自 vs. 亲自/亲手", "pinyin": "qīnshǒu", "analysis": "亲手 emphasizes physical manipulation with one's own hands ('亲手做蛋糕'), while 亲自 covers broader leadership, attendance, or decision-making."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "真正的温暖不是金钱的馈赠，而是亲自陪伴与倾听的诚意。当朋友遭遇人生低谷时，再多的客套短信也比不上亲自登门探望，握住对方冰冷的手送上一句鼓励。躬身而行的温度，胜过世间一切虚华的繁文缛节。",
                "pinyin": "Zhēnzhèng de wēnduǎn bú shì jīnqián de kuìzèng, ér shì qīnzì péibàn yǔ qīngtīng de chéngyì. Dāng péngyou zāoyù rénshēng dīgǔ shí, zài duō de kètào duǎnxìn yě bǐbúshàng qīnzì dēngmén tànwàng, wòzhù duìfāng bīnglěng de shǒu sòngshàng yí jù gǔlì. Gōngshēn-érxíng de wēndù, shèngguò shìjiān yíqiè xūhuá de fánwén-rùjié.",
                "en": "True warmth is not gifts of money, but the sincerity of personally accompanying and listening. When a friend hits rock bottom, polite texts pale beside visiting in person and clasping their hand. Personal presence outweighs empty etiquette.",
                "es": "La calidez genuina no emana del dinero, sino de la cercanía al acompañar y escuchar. Cuando un amigo toca fondo, ningún mensaje formal iguala una visita en persona para estrechar su mano. La presencia sincera vale más que vanas cortesías."
            },
            {
                "id": "#2",
                "hanzi": "卓越的领导力不仅体现在高瞻远瞩的战略决策，更体现在关键时刻亲自靠前指挥的务实作风。抗洪抢险与重大科研攻关一线，指挥官亲自带队深入最艰苦的现场，极大鼓舞了全员士气，为化解危机赢得了宝贵先机。",
                "pinyin": "Zhuóyuè de lǐngdǎolì bùjǐn tǐxiàn zài gāozhān-yuǎnzhǔ de zhànlüè juécè, gèng tǐxiàn zài guānjiàn shíkè qīnzì kàoqián zhǐhuī de wùshí zuòfēng. Kànghóng-qiǎngxiǎn yǔ zhòngdà kēyán gōngguān yíxiàn, zhǐhuīguān qīnzì dàiduì shēnrù zuì jiānkǔ de xiànchǎng, jídà gǔwǔ le quányuán shìqì, wèi huàjiě wēijī yíngdé le bǎoguì xiānjī.",
                "en": "Outstanding leadership is shown not only in foresight, but in taking charge in person at critical moments. Leading teams to frontlines of floods or research breakthroughs inspires morale, winning precious ground in resolving crises.",
                "es": "El liderazgo insigne se refleja tanto en la visión de futuro como en asumir el mando en persona durante momentos decisivos. Cuando los mandos guían al equipo sobre el terreno, levantan la moral y toman la delantera ante las dificultades."
            }
        ]
    },

    # 08 见解
    {
        "id": "8",
        "hanzi": "见解",
        "pinyin": "jiàn jiě",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "opinion; view; insight; perspective; interpretation",
            "es": "opinión; punto de vista; criterio; apreciación; juicio"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a thoughtful, reasoned understanding or insightful perspective on a problem, theory, or art",
                "definition_es": "comprensión meditada, criterio fundado o juicio crítico sobre una materia, arte o teoría",
                "example_phrase": "独到的见解 (original and insightful perspective)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在学术研讨会上，这位年轻博士对传统文化在当代的传播提出了许多独到的见解，引起了与会专家的热烈讨论。",
                "pinyin": "Zài xuéshù yántǎohuì shàng, zhè wèi niánqīng bóshì duì chuántǒng wénhuà zài dāngdài de chuánbō tíchū le xǔduō dúdào de jiànjiě, yǐnqǐ le yùhuì zhuānjiā de rèliè tǎolùn.",
                "en": "At the symposium, this young doctoral graduate proposed many original insights into contemporary transmission of traditional culture, sparking lively discussion.",
                "es": "En el simposio, el joven doctor expuso criterios muy originales sobre la divulgación de las tradiciones, generando un vivo debate entre los expertos."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅对文学评论与社会批判有着极为深刻的见解，往往几句话就能切中要害，揭示问题的本质所在。",
                "pinyin": "Lǔ Xùn duì wénxué pínglùn yǔ shèhuì pīpàn yǒuzhe jíwéi shēnkè de jiànjiě, wǎngwǎng jǐ jù huà jiù néng qièzhòng-yàohài, jiēshì wèntí de běnzhì suǒzài.",
                "en": "Lu Xun possessed profound insights into literary criticism and social commentary, often striking the core of issues in just a few sentences.",
                "es": "Lu Xun poseía un criterio perspicaz sobre la crítica literaria y social; con pocas frases daba en el clavo, revelando la entraña del dilema."
            }
        ],
        "collocations": [
            {"hanzi": "独到见解", "en": "original insight"},
            {"hanzi": "深刻见解", "en": "profound view/insight"},
            {"hanzi": "发表见解", "en": "express one's views"},
            {"hanzi": "精辟见解", "en": "incisive and brilliant insight"},
            {"hanzi": "专业见解", "en": "professional perspective"},
            {"hanzi": "个人见解", "en": "personal opinion"}
        ],
        "idioms": [
            {"hanzi": "真知灼见", "pinyin": "zhēn zhī zhuó jiàn", "meaning_en": "penetrating insight; real and profound knowledge"},
            {"hanzi": "仁者见仁", "pinyin": "rén zhě jiàn rén", "meaning_en": "the benevolent sees benevolence; different views according to character"},
            {"hanzi": "高瞻远瞩", "pinyin": "gāo zhān yuǎn zhǔ", "meaning_en": "stand high and gaze far; broad, farsighted perspective"},
            {"hanzi": "各执一词", "pinyin": "gè zhí yì cí", "meaning_en": "each clings stubbornly to their own opinion"}
        ],
        "character_decomposition": [
            {
                "character": "见",
                "pinyin": "jiàn",
                "meaning_en": "see; view; observe; meet",
                "meaning_es": "ver; percibir; opinión; encontrarse",
                "radical": "见",
                "radical_meaning_en": "see",
                "meaning_component": "目 (eye) + 儿 (legs of an observer)",
                "sound_component": "见 (jiàn)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram showing an exaggerated human eye 目 mounted upon a walking person 儿, meaning conscious sight and observation.",
                "visual_mnemonic_story_en": "An open eye (目) looking out across the landscape allows a thinker to observe (见) and reflect on reality.",
                "visual_mnemonic_story_es": "Un ojo atento (目) escruta el entorno permitiendo al observador ver (见) y reflexionar.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BHU",
                "traditional": "見"
            },
            {
                "character": "解",
                "pinyin": "jiě",
                "meaning_en": "dissect; untie; solve; understand; explain",
                "meaning_es": "desatar; desmembrar; resolver; comprender",
                "radical": "角",
                "radical_meaning_en": "horn",
                "meaning_component": "角 (horn) + 刀 (knife/dissect) + 牛 (ox)",
                "sound_component": "刀 (dāo, cut)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient ideogram showing using a sharp knife 刀 to cut the horns 角 from an ox 牛, meaning analytical dissection and intellectual understanding.",
                "visual_mnemonic_story_en": "A knife (刀) carefully cuts apart the horns (角) of an ox (牛) to dissect, untie, and understand (解) the anatomy.",
                "visual_mnemonic_story_es": "El cuchillo (刀) separa con destreza las astas (角) del buey (牛), simbolizando la disección y el entendimiento (解).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "NBHNQ",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Observe with clear sight (见) and analytically dissect the details (解) to form a brilliant insight (见解).",
            "composite_memory_hook_es": "Observa con mirada clara (见) y desmenuza con precisión (解) para forjar un criterio lúcido (见解).",
            "cultural_and_cognitive_roots": "Combining visual perception (见) with logical dissection (解); implies that true opinion is not baseless gossip, but an analyzed deconstruction of empirical facts.",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by dipping tone: 'jiàn jiě' (51-214). Sharp drop on 'jiàn', followed by a full undulating 3rd tone on 'jiě'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "贝", "pinyin": "bèi", "meaning_en": "shell; money", "distinction_note": "Bottom legs 儿 are closed into two short dots 八"},
                {"character": "触", "pinyin": "chù", "meaning_en": "touch; strike", "distinction_note": "Has 虫 on the right side of 角 instead of 刀 and 牛"},
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; regulation", "distinction_note": "Has 见 on right, but 夫 on left instead of standalone 见"},
                {"character": "现", "pinyin": "xiàn", "meaning_en": "appear; present", "distinction_note": "Has jade radical 王 on the left"}
            ],
            "etymological_cognates": [
                {"character": "观", "pinyin": "guān", "gloss_en": "view; perspective; observe"},
                {"character": "觉", "pinyin": "jué", "gloss_en": "perceive; awaken; feel"},
                {"character": "析", "pinyin": "xī", "gloss_en": "analyze; split wood cleanly"},
                {"character": "释", "pinyin": "shì", "gloss_en": "explain; unloose; liberate"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "见解 denotes an intellectual, analytical judgment formed through rational synthesis and deep expertise.",
            "contrasts": [
                {"id": "1", "compared_word": "见解 vs. 意见", "pinyin": "yìjiàn", "analysis": "见解 refers to scholarly or philosophical insights and assessments, while 意见 often denotes practical suggestions, complaints, or divergent disagreements."},
                {"id": "2", "compared_word": "见解 vs. 看法", "pinyin": "kànfǎ", "analysis": "看法 is an everyday, general term for any personal impression or opinion, whereas 见解 implies greater analytical depth and formal reasoning."},
                {"id": "3", "compared_word": "见解 vs. 观点", "pinyin": "guāndiǎn", "analysis": "观点 emphasizes one's fundamental ideological stance or angle of observation, while 见解 emphasizes the reasoned conclusions drawn."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "读书的真谛不仅在于汲取既成知识，更在于培养独立思考的见解。不盲从权威，不随波逐流，在经典与现实的碰撞中叩问真理。唯有经过理性淘洗的思想，才能沉淀为属于自己的精神坐标，照亮前行之路。",
                "pinyin": "Dúshū de zhēndì bùjǐn zàiyú jíqǔ jìchéng zhīshi, gèng zàiyú péiyǎng dúlì-sīkǎo de jiànjiě. Bù mángcóng quánwēi, bù suíbō-zhúliú, zài jīngdiǎn yǔ xiànshí de pèngzhuàng zhōng kòuwèn zhēnlǐ. Wéiyǒu jīngguò lǐxìng táoxǐ de sīxiǎng, cáinéng chéndiàn wéi shǔyú zìjǐ de jīngshén zuòbiāo, zhàoliàng qiánxíng zhī lù.",
                "en": "The essence of reading lies not just in absorbing knowledge, but cultivating independent insights. Questioning truth without blind obedience to authority turns reasoned thoughts into inner spiritual coordinates that light one's path forward.",
                "es": "El valor de la lectura radica en forjar un juicio propio e independiente. Quien no se somete a dogmas ni sigue modas interroga la verdad. Solo el pensamiento decantado por la razón se transforma en una brújula que orienta los pasos."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的全球宏观局势，智库学者必须保持敏锐的洞察力。通过多源大数据的交叉印证，专家们在能源安全与产业布局上发表了一系列富有远见的专业见解，为国家制定中长期发展战略提供了强有力的智力支撑。",
                "pinyin": "Miànduì shùnxī-wànbiàn de quánqiú hóngguān júshì, zhìkù xuézhě bìxū bǎochí mǐnruì de dòngchálì. Tōngguò duōyuán dàshùjù de jiāochā yìnzhèng, zhuānjiāmen zài néngyuán ānquán yǔ chǎnyè bùjú shàng fābiǎo le yíxìliè fùyǒu yuǎnjiàn de zhuānyè jiànjiě, wèi guójiā zhìdìng zhōng-chángqī fāzhǎn zhànlüè tígōng le qiángyǒulì de zhìlì zhīchēng.",
                "en": "Facing fast-shifting global trends, think-tank scholars must maintain sharp insight. Cross-verifying big data, experts have published visionary perspectives on energy security and industrial layout, providing robust intellectual support for national strategy.",
                "es": "Ante la volátil coyuntura mundial, los analistas deben afinar la mirada. Cruzando macrodatos fiables, los expertos han formulado dictámenes de gran alcance sobre seguridad energética e industria, brindando sólido respaldo estratégico."
            }
        ]
    },

    # 09 近代
    {
        "id": "9",
        "hanzi": "近代",
        "pinyin": "jìn dài",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "modern times (in Chinese historiography: 1840-1919/1949); recent history",
            "es": "época moderna; era contemporánea temprana; historia reciente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "historical era typically defined in China as spanning from the Opium War (1840) to the May Fourth Movement (1919) or the mid-20th century",
                "definition_es": "período histórico que en China comprende desde la Guerra del Opio (1840) hasta el Movimiento del Cuatro de Mayo (1919) o mediados del siglo XX",
                "example_phrase": "近代历史 (modern history)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "近代中国经历了波澜壮阔的社会变革，传统的儒家伦理与西方的现代科学思想在此激烈碰撞交融。",
                "pinyin": "Jìndài Zhōngguó jīnglì le bōlán-zhuàngkuò de shèhuì biàngé, chuántǒng de Rújiā lúnlǐ yǔ xīfāng de xiàndài kēxué sīxiǎng zài cǐ jīliè pèngzhuàng jiāoróng.",
                "en": "Modern China experienced tumultuous social changes, where traditional Confucian ethics and Western scientific thought clashed and converged violently.",
                "es": "La China moderna vivió convulsas transformaciones sociales, en las que la ética confuciana colisionó y se entrelazó con la ciencia occidental."
            },
            {
                "id": "#2",
                "hanzi": "研究近代文人的饮食文化与日常手账，能让我们以更加鲜活真实的视角重返百年前的市井生活。",
                "pinyin": "Yánjiū jìndài wénrén de yǐnshí wénhuà yǔ rìcháng shǒuzhàng, néng ràng wǒmen yǐ gèngjiā xiānhuó zhēnshí de shìjiǎo chóngfǎn bǎi nián qián de shìjǐng shēnghuó.",
                "en": "Studying the dining culture and daily journals of modern literary figures allows us to revisit century-old urban life with vivid authenticity.",
                "es": "Estudiar los hábitos culinarios y dietarios de los literatos de la era moderna nos permite asomarnos con viveza a la vida urbana de hace un siglo."
            }
        ],
        "collocations": [
            {"hanzi": "近代历史", "en": "modern history"},
            {"hanzi": "近代科学", "en": "modern science"},
            {"hanzi": "近代中国", "en": "modern China"},
            {"hanzi": "近代思想", "en": "modern thought/ideology"},
            {"hanzi": "近代以来", "en": "since the advent of modern times"},
            {"hanzi": "近代文学", "en": "modern literature"}
        ],
        "idioms": [
            {"hanzi": "继往开来", "pinyin": "jì wǎng kāi lái", "meaning_en": "carry forward past heritage and blaze new trails into the future"},
            {"hanzi": "改弦易辙", "pinyin": "gǎi xián yì zhé", "meaning_en": "change one's course or policy drastically"},
            {"hanzi": "与时俱进", "pinyin": "yǔ shí jù jìn", "meaning_en": "advance in lockstep with the times; keep pace with progress"},
            {"hanzi": "推陈出新", "pinyin": "tuī chén chū xīn", "meaning_en": "weed out the obsolete to bring forth the fresh and new"}
        ],
        "character_decomposition": [
            {
                "character": "近",
                "pinyin": "jìn",
                "meaning_en": "near; close; recent; approach",
                "meaning_es": "cerca; próximo; reciente; aproximarse",
                "radical": "辶",
                "radical_meaning_en": "walk",
                "meaning_component": "辶 (movement on a path)",
                "sound_component": "斤 (jīn, axe / phonetic harmony)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Phono-semantic character where motion along a road 辶 approaches a destination close at hand.",
                "visual_mnemonic_story_en": "Walking along the path (辶) with an axe (斤) in hand brings you within close, recent reach (近).",
                "visual_mnemonic_story_es": "Avanzar por la senda (辶) con un hacha (斤) sitúa al viajero a poca distancia (近).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YHML",
                "traditional": ""
            },
            {
                "character": "代",
                "pinyin": "dài",
                "meaning_en": "era; generation; replace; substitute",
                "meaning_es": "era; época; generación; reemplazar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person / generational succession)",
                "sound_component": "弋 (yì, arrow peg / marker)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing one person 亻 taking the post marked by 弋, signifying generational replacement and successive historical eras.",
                "visual_mnemonic_story_en": "One person (亻) steps up to stake (弋) their place, succeeding the previous generation in the era (代).",
                "visual_mnemonic_story_es": "Un individuo (亻) toma el relevo en la estaca (弋), sucediendo a la generación anterior en la época (代).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OIP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The era (代) closest to our present memory (近) is the modern era (近代).",
            "composite_memory_hook_es": "La época (代) más cercana a nuestro presente (近) constituye la era moderna (近代).",
            "cultural_and_cognitive_roots": "Chinese historiography divides epochs into Ancient (古代, pre-1840), Modern (近代, 1840-1919/1949), and Contemporary (现代/当代, post-1949/1919); 'jìn' marks proximity to the present.",
            "tone_sandhi_and_pitch_modulation": "Two falling tones: 'jìn dài' (51-51). Articulate both syllables with firm, crisp descending contours."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "进", "pinyin": "jìn", "meaning_en": "advance; enter", "distinction_note": "Has 井 inside 辶 instead of 斤"},
                {"character": "远", "pinyin": "yuǎn", "meaning_en": "far; distant", "distinction_note": "Has 元 inside 辶; direct antonym of 近"},
                {"character": "伐", "pinyin": "fá", "meaning_en": "cut down; attack", "distinction_note": "Has 戈 on right instead of 弋"},
                {"character": "仕", "pinyin": "shì", "meaning_en": "official; serve", "distinction_note": "Has 士 on right instead of 弋"}
            ],
            "etymological_cognates": [
                {"character": "世", "pinyin": "shì", "gloss_en": "generation; epoch; thirty years"},
                {"character": "纪", "pinyin": "jì", "gloss_en": "record; century; discipline"},
                {"character": "年", "pinyin": "nián", "gloss_en": "year; seasonal harvest cycle"},
                {"character": "临", "pinyin": "lín", "gloss_en": "approach; overlook from nearby"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "近代 specifically refers to the transitional modern historical era preceding contemporary times.",
            "contrasts": [
                {"id": "1", "compared_word": "近代 vs. 现代", "pinyin": "xiàndài", "analysis": "In Chinese historiography, 近代 denotes the period starting from 1840, whereas 现代 denotes the contemporary era starting with the May Fourth Movement (1919) or PRC founding."},
                {"id": "2", "compared_word": "近代 vs. 当代", "pinyin": "dāngdài", "analysis": "近代 is a concluded historical epoch, while 当代 strictly denotes the immediate present ongoing period in which we currently live."},
                {"id": "3", "compared_word": "近代 vs. 古代", "pinyin": "gǔdài", "analysis": "古代 refers to antiquity and imperial dynasties prior to the 1840 Opium War, while 近代 marks the threshold of industrial modernization."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫步在近代留下的红砖洋房与石库门里弄之间，斑驳的铁艺栏杆静静诉说着往昔的风云际会。那些从旧时代突围而出的思想先驱，正是在这些逼仄的亭子间里挑灯夜战，为民族的觉醒点亮了最早的黎明微光。",
                "pinyin": "Mànbù zài jìndài liúxià de hóngzhuān yángfáng yǔ shíkùmén lǐnòng zhījiān, bānbó de tiěyì lángān jìngjìng sùshuō zhe wǎngxī de fēngyún-jìhuì. Nàxiē cóng jiù shídài tūwéi-érchū de sīxiǎng xiānqū, zhèng shì zài zhèxiē bīzè de tíngzǐjiān lǐ tiǎodēng-yèzhàn, wèi mínzú de juéxǐng diǎnliàng le zuìzǎo de límíng wēiguāng.",
                "en": "Strolling between modern red-brick villas and lane alleys, mottled railings whisper tales of historical turbulence. In cramped garrets, pioneers broke from old constraints and burnt midnight oil, kindling the dawn of national awakening.",
                "es": "Paseando entre casonas de ladrillo rojo y callejones antiguos, las rejas oxidadas susurran memorias de cambio. Fue en estos estrechos desvanes donde los pioneros del pensamiento velaron armas, encendiendo la aurora del renacer popular."
            },
            {
                "id": "#2",
                "hanzi": "中国近代工业化探索走过了一条极其曲折艰难的道路。从晚清洋务运动创办军工制造，到民国初期民族资本在轻工纺织业的艰难崛起，近代先辈们实业报国的顽强求索，为今日门类完备的现代工业体系奠定了坚实雏形。",
                "pinyin": "Zhōngguó jìndài gōngyèhuà tànsuǒ zǒuguò le yì tiáo jíqí qūzhé jiānnán de dàolù. Cóng wǎn-Qīng Yángwù Yùndòng chuàngbàn jūngōng zhìzào, dào Mínguó chūqí mínzú zīběn zài qīnggōng fǎngzhīyè de jiānnán juéqǐ, jìndài xiānbèimen shíyè-bàoguó de wánqiáng qiúsuǒ, wèi jīnrì ménlèi-wánbèi de xiàndài gōngyè tǐxì diàndìng le jiānshí chúxíng.",
                "en": "China's modern industrialization walked a tortuous path. From late Qing defense arsenals to Republican textile mills, modern predecessors' tenacity in building domestic enterprise laid the solid embryonic foundation for today's industry.",
                "es": "La industrialización de la China moderna recorrió un sendero arduo. Desde las factorías de defensa en la dinastía Qing hasta el auge textil republicano, la entrega de aquellos precursores forjó los cimientos del actual tejido fabril."
            }
        ]
    },

    # 10 时尚
    {
        "id": "10",
        "hanzi": "时尚",
        "pinyin": "shí shàng",
        "part_of_speech": "Noun / Adjective",
        "meanings_summary": {
            "en": "fashion; vogue; trend; trendy; fashionable; stylish",
            "es": "moda; tendencia; boga; moderno; elegante; a la moda"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "prevailing social customs, artistic trends, or clothing styles fashionable in a given period",
                "definition_es": "usos, costumbres, estilos de vestir o tendencias artísticas en boga durante una época",
                "example_phrase": "引领时代时尚 (lead the fashion of the era)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "conforming to current popular taste; stylish and fashionable",
                "definition_es": "adaptado al gusto en boga; moderno y con estilo",
                "example_phrase": "设计非常时尚 (very fashionable design)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这家文创店将传统剪纸工艺融入时尚背包设计，吸引了大量年轻消费者的青睐。",
                "pinyin": "Zhè jiā wénchuàng diàn jiāng chuántǒng jiǎnzhǐ gōngyì róngrù shíshàng bēibāo shèjì, xīyǐn le dàliàng niánqīng xiāofèizhě de qīnglài.",
                "en": "This cultural shop integrated paper-cutting into stylish backpack designs, attracting many young consumers.",
                "es": "Esta tienda fusionó el recortado de papel con mochilas modernas, cautivando la atención de los jóvenes compradores."
            },
            {
                "id": "#2",
                "hanzi": "在近代北京与上海，穿西装、喝咖啡、下西餐厅渐渐成为文人圈子里极具标志性的生活时尚。",
                "pinyin": "Zài jìndài Běijīng yǔ Shànghǎi, chuān xīzhuāng, hē kāfēi, xià xīcāntīng jiànjiàn chéngwéi wénrén quānzi lǐ jí jù biāozhìxìng de shēnghuó shíshàng.",
                "en": "In modern Beijing and Shanghai, wearing suits, drinking coffee, and patronizing Western diners became iconic lifestyle trends among literati.",
                "es": "En el Pekín y Shanghái de la modernidad, vestir traje occidental, tomar café y frecuentar mesones foráneos devino una moda emblemática."
            }
        ],
        "collocations": [
            {"hanzi": "时尚潮流", "en": "fashion trend"},
            {"hanzi": "追赶时尚", "en": "pursue fashion/trends"},
            {"hanzi": "时尚元素", "en": "fashionable elements"},
            {"hanzi": "生活时尚", "en": "lifestyle fashion"},
            {"hanzi": "时尚前沿", "en": "forefront of fashion"},
            {"hanzi": "引领时尚", "en": "lead fashion"}
        ],
        "idioms": [
            {"hanzi": "风靡一时", "pinyin": "fēng mǐ yì shí", "meaning_en": "sweep like the wind; be all the rage for a time"},
            {"hanzi": "蔚然成风", "pinyin": "wèi rán chéng fēng", "meaning_en": "grow into a widespread custom or prevailing practice"},
            {"hanzi": "独领风骚", "pinyin": "dú lǐng fēng sāo", "meaning_en": "take the lead in literary style; dominate the trend"},
            {"hanzi": "标新立异", "pinyin": "biāo xīn lì yì", "meaning_en": "innovate distinctively; show uniqueness"}
        ],
        "character_decomposition": [
            {
                "character": "时",
                "pinyin": "shí",
                "meaning_en": "time; era; season; hour; current",
                "meaning_es": "tiempo; era; sazón; hora; oportuno",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun marking time)",
                "sound_component": "寸 (cùn, measurement / hand)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where solar passage 日 measured by inches 寸 represents time and seasonal changes.",
                "visual_mnemonic_story_en": "Measuring the sun's (日) shadow inch by inch (寸) tracks the precious passage of time (时).",
                "visual_mnemonic_story_es": "Medir pulgada a pulgada (寸) la sombra del sol (日) marca el paso del tiempo oportuno (时).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "ADI",
                "traditional": "時"
            },
            {
                "character": "尚",
                "pinyin": "shàng",
                "meaning_en": "esteem; value; still; yet; upward",
                "meaning_es": "estimar; valorar; aún; hacia arriba",
                "radical": "小",
                "radical_meaning_en": "small / top",
                "meaning_component": "八 (diverge upward)",
                "sound_component": "向 (xiàng, window / orientation)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient ideogram showing upward movement toward an opening, extended to esteeming or holding in high regard.",
                "visual_mnemonic_story_en": "Rising above small (小) trifles to point toward the high open window (向) shows what is valued and esteemed (尚).",
                "visual_mnemonic_story_es": "Elevarse sobre lo menudo (小) hacia el ventanal alto (向) simboliza lo que se valora y estima (尚).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FBR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "What is esteemed (尚) in the current season of time (时) becomes the reigning fashion (时尚).",
            "composite_memory_hook_es": "Lo que más se estima (尚) en el tiempo presente (时) marca la pauta de la moda (时尚).",
            "cultural_and_cognitive_roots": "Derived from classical phrases like 'fēngshàng' (风尚) and 'shíshì' (时事); represents the social psychology of collective zeitgeist and aesthetic adoration.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone: 'shí shàng' (35-51). Syllable 'shí' rises steadily from mid to high, followed by a crisp downward drop on 'shàng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "村", "pinyin": "cūn", "meaning_en": "village", "distinction_note": "Has tree radical 木 on left instead of 日"},
                {"character": "堂", "pinyin": "táng", "meaning_en": "hall; room", "distinction_note": "Has earth radical 土 at bottom instead of 口"},
                {"character": "常", "pinyin": "cháng", "meaning_en": "often; common", "distinction_note": "Has cloth radical 巾 at bottom instead of 口"},
                {"character": "党", "pinyin": "dǎng", "meaning_en": "party; faction", "distinction_note": "Has 儿 at bottom instead of 口"}
            ],
            "etymological_cognates": [
                {"character": "崇", "pinyin": "chóng", "gloss_en": "lofty; revere mountains; esteem"},
                {"character": "尊", "pinyin": "zūn", "gloss_en": "respect; honor with wine"},
                {"character": "潮", "pinyin": "cháo", "gloss_en": "ocean tide; trend of the era"},
                {"character": "流", "pinyin": "liú", "gloss_en": "flow; stream; mainstream style"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "时尚 refers to the contemporary aesthetic, behavioral, or consumerist trend embraced by society.",
            "contrasts": [
                {"id": "1", "compared_word": "时尚 vs. 时髦", "pinyin": "shímáo", "analysis": "时髦 is a more colloquial loanword-style term focusing narrowly on trendy clothing or makeup, while 时尚 has a broader cultural, artistic, and lifestyle scope."},
                {"id": "2", "compared_word": "时尚 vs. 潮流", "pinyin": "cháoliú", "analysis": "潮流 denotes the broader, powerful historical or macroeconomic tide of change ('时代潮流'), while 时尚 focuses on lifestyle taste and aesthetic design."},
                {"id": "3", "compared_word": "时尚 vs. 流行", "pinyin": "liúxíng", "analysis": "流行 simply means widely circulating or statistically popular, whereas 时尚 carries an inherent connotation of chic elegance, novelty, and prestige."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "时尚如同一阵拂面而过的春风，不断更迭着城市的容颜。然而盲目跟风者往往在追赶中迷失自我，唯有将外在的审美与内在的气质相契合，才能孕育出历久弥新的优雅。真正的时尚从不喧哗，它是一种从容不迫的生活态度。",
                "pinyin": "Shíshàng rútóng yí zhèn fúmiàn-érguò de chūnfēng, bùduàn gēngdié zhe chéngshì de róngyán. Rán'ér mángmù gēnfēng zhě wǎngwǎng zài zhuīgǎn zhōng míshī zìwǒ, wéiyǒu jiāng wàizài de shěnmǐ yǔ nèizài de qìzhì xiàng qìhé, cáinéng yùnyù chū lìjiǔ-míxīn de yōuyǎ. Zhēnzhèng de shíshàng cóng bù xuānhuá, tā shì yì zhǒng cóngróng-bùpò de shēnghuó tàidù.",
                "en": "Fashion is like a passing spring breeze, renewing the city's face. Yet blind trend followers lose themselves; only uniting outer aesthetics with inner grace breeds timeless elegance. True style never shouts—it is calm composure.",
                "es": "La moda es como una brisa primaveral que renueva el rostro de la urbe. Quien la sigue a ciegas se extravía; solo al aunar el buen gusto exterior con el temple interno florece la elegancia perdurable. La auténtica distinción no alardea: es serenidad."
            },
            {
                "id": "#2",
                "hanzi": "近年来，东方美学在国际设计舞台上掀起了一股强劲的中国时尚风潮。设计师们从故宫典藏与传统刺绣中汲取灵感，将古老东方的水墨留白与现代极简剪裁巧妙交融。这种跨越时空的创新表达，向世界展现了中华文化的现代活力。",
                "pinyin": "Jìnniánlái, dōngfāng měixué zài guójì shèjì wǔtái shàng xiānqǐ le yì gǔ qiángjìn de Zhōngguó shíshàng fēngcháo. Shèjìshīmen cóng Gùgōng diǎncáng yǔ chuántǒng cìxiù zhōng jíqǔ línggǎn, jiāng gǔlǎo dōngfāng de shuǐmò liúbái yǔ xiàndài jíjiǎn jiǎncái qiǎomiào jiāoróng. Zhè zhǒng kuàyuè shíkōng de chuàngxīn biǎodá, xiàng shìjiè zhǎnxiàn le Zhōnghuá wénhuà de xiàndài huólì.",
                "en": "In recent years, oriental aesthetics has sparked a vibrant Chinese fashion wave on international stages. Designers draw inspiration from Forbidden City archives and embroidery, fusing ink-wash space with modern minimalism to showcase cultural vitality.",
                "es": "La estética oriental ha desatado una pujante corriente de diseño en las pasarelas del orbe. Los creadores beben de los bordados y el arte imperial para fusionar la tinta china con el corte moderno, mostrando al mundo la lozanía de su cultura."
            }
        ]
    }
]

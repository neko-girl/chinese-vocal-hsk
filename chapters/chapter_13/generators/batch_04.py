# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 瞧
    {
        "id": "31",
        "hanzi": "瞧",
        "pinyin": "qiáo",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to look; see; glance at",
            "es": "mirar; ver; echar un vistazo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Colloquial",
                "definition_en": "to look at, glance, or observe with the eyes, predominantly used in colloquial spoken Chinese",
                "definition_es": "mirar u observar con atención; muy habitual en el lenguaje coloquial",
                "example_phrase": "你快瞧瞧那是什么 (take a look quickly at what that is)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "你快到窗前瞧瞧，昨晚的一场大雪把整个小区的树木都裹上了一层银白色的厚霜。",
                "pinyin": "Nǐ kuài dào chuāngqián qiáoqiao, zuówǎn de yì chǎng dàxuě bǎ zhěnggè xiǎoqū de shùmù dōu guǒ shàng le yì céng yínbáisè de hòushuāng.",
                "en": "Quick, come to the window and take a look; last night's heavy snowfall wrapped all trees in the neighborhood in thick silver frost.",
                "es": "Ven corriendo a la ventana a echar un vistazo; la copiosa nevada de anoche envolvió los árboles de la barriada en una gruesa escarcha plateada."
            },
            {
                "id": "#2",
                "hanzi": "他总爱戴着有色眼镜瞧人，这种傲慢偏见的处世态度让身边的很多同事都敬而远之。",
                "pinyin": "Tā zǒng ài dài zhe yǒusè yǎnjìng qiáo rén, zhè zhǒng àomàn piānjiàn de chǔshì tàidù ràng shēnbiān de hěnduō tóngshì dōu jìng'éryuǎnzhī.",
                "en": "He always looks at people through tinted glasses; this arrogant and prejudiced attitude causes many colleagues around him to keep their distance.",
                "es": "Siempre mira a los demás con prejuicios; esa actitud altanera y despectiva hace que sus compañeros de trabajo prefieran guardar las distancias."
            }
        ],
        "collocations": [
            {"hanzi": "瞧一瞧", "en": "have a look; take a glance"},
            {"hanzi": "瞧不起", "en": "look down upon; despise"},
            {"hanzi": "瞧得起", "en": "think highly of; respect"},
            {"hanzi": "瞧见", "en": "catch sight of; see"},
            {"hanzi": "瞧病", "en": "see a doctor (colloquial)"},
            {"hanzi": "走着瞧", "en": "wait and see (warning/slang)"}
        ],
        "idioms": [
            {"hanzi": "另眼相看", "pinyin": "lìng yǎn xiāng kàn", "meaning_en": "view in a new and favorable light; treat with special respect"},
            {"hanzi": "刮目相看", "pinyin": "guā mù xiāng kàn", "meaning_en": "rub eyes and look with new respect"},
            {"hanzi": "冷眼旁观", "pinyin": "lěng yǎn páng guān", "meaning_en": "look on coldly from the sidelines; detached spectator"},
            {"hanzi": "虎视眈眈", "pinyin": "hǔ shì dān dān", "meaning_en": "glare like a tiger eyeing its prey covetously"}
        ],
        "character_decomposition": [
            {
                "character": "瞧",
                "pinyin": "qiáo",
                "meaning_en": "look; glance; see",
                "meaning_es": "mirar; ver",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye / gaze) + 焦 (scorched / intense longing)",
                "sound_component": "焦 (jiāo / phonetic association)",
                "stroke_count": 17,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Eye radical 目 beside 焦 (scorched bird over fire); focusing one's eyes with burning intensity to discern something.",
                "visual_mnemonic_story_en": "Keen eyes (目) focusing through scorched embers (焦) to catch a sharp glance of the truth (瞧).",
                "visual_mnemonic_story_es": "Ojos atentos (目) que atisban entre ascuas (焦) para divisar con claridad lo que ocurre (瞧).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BUPOG",
                "traditional": "瞧"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Directing your attentive eyes (目) with sharp focus (焦) allows you to take a close look (瞧).",
            "composite_memory_hook_es": "Fijar la mirada (目) con ardiente interés (焦) te permite echar un buen vistazo (瞧).",
            "cultural_and_cognitive_roots": "Expressive northern Mandarin colloquialism for looking, common in vernacular novels and Beijing dialogue.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone: 'qiáo' (35). Soar upward smoothly with bright colloquial inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "瞧", "pinyin": "qiáo", "meaning_en": "look; see", "distinction_note": "Eye radical 目 on left with 焦"},
                {"character": "焦", "pinyin": "jiāo", "meaning_en": "burnt; anxious", "distinction_note": "Without the eye radical on left"},
                {"character": "樵", "pinyin": "qiáo", "meaning_en": "woodcutter; gather firewood", "distinction_note": "Tree radical 木 on left of 焦"},
                {"character": "礁", "pinyin": "jiāo", "meaning_en": "reef; submerged rock", "distinction_note": "Stone radical 石 on left of 焦"}
            ],
            "etymological_cognates": [
                {"character": "看", "pinyin": "kàn", "gloss_en": "look; watch"},
                {"character": "望", "pinyin": "wàng", "gloss_en": "gaze into distance; hope"},
                {"character": "睹", "pinyin": "dǔ", "gloss_en": "witness; observe"},
                {"character": "瞻", "pinyin": "zhān", "gloss_en": "look forward; inspect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "瞧 is an informal, colloquial synonym of 看, often implying a spontaneous glance or evaluation.",
            "contrasts": [
                {"id": 1, "compared_word": "瞧 vs. 看", "pinyin": "kàn", "analysis": "看 is neutral and universally used across spoken and written Chinese, while 瞧 is vivid northern colloquial speech."},
                {"id": 2, "compared_word": "瞧 vs. 望", "pinyin": "wàng", "analysis": "望 denotes gazing far into the distant horizon or up at stars, whereas 瞧 focuses on nearby objects or people."},
                {"id": 3, "compared_word": "瞧 vs. 瞅", "pinyin": "chǒu", "analysis": "瞅 is strongly regional (Northeastern vernacular), while 瞧 is standard colloquial northern Mandarin."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "母亲常拉着客人的手亲切地说：‘快进屋瞧瞧，院子里的老茶花开得正艳呢。’那些在岁月风雨中悄然绽放的花瓣红艳似火，映照着小院的宁静祥和，也温暖着每一个远道而来寻访乡愁的游子。",
                "pinyin": "Mǔqīn cháng lā zhe kèrén de shǒu qīnqiè de shuō: 'Kuài jìn wū qiáoqiao, yuànzi lǐ de lǎo cháhuā kāi de zhèng yàn ne.' Nàxiē zài suìyuè fēngyǔ zhōng qiǎorán zhànfàng de huābàn hóngyàn-sìhuǒ, yìngzhào zhe xiǎoyuàn de níngjìng xiánghé, yě wēnnuǎn zhe měi yí ge yuǎndào'érlái xúnfǎng xiāngchóu de yóuzǐ.",
                "en": "Mother warmly took guests' hands: 'Come inside and take a look; the old camellias are blooming splendidly.' Blossoms glowing like fire mirrored the tranquil yard, comforting nostalgic travelers from afar.",
                "es": "La madre tomaba afectuosamente la mano del visitante: 'Pasad a ver qué floridas están las camelias del patio'. Sus pétalos ardientes como fuego acariciaban la paz del hogar, confortando a los viajeros."
            },
            {
                "id": "#2",
                "hanzi": "当年路过球场的小男孩好奇地停下脚步，歪着头仔细瞧着那两个挂在高处的桃筐，忍不住随口说了句：‘你们瞧，把筐底直接锯掉不就全解决了吗？’这句看似天真的大实话，瞬间点醒了全场工匠。",
                "pinyin": "Dāngnián lùguò qiúchǎng de xiǎo nánhái hàoqí de tíngxià jiǎobù, wāi zhe tóu zǐxì qiáo zhe nà liǎng ge guà zài gāochù de táokuāng, rěnbùzhù suíkǒu shuō le jù: 'Nǐmen qiáo, bǎ kuāngdǐ zhíjiē jù diào bù jiù quán jiějué le ma?' Zhè jù kànsì tiānzhēn de dà shíhuà, shùnjiān diǎnxǐng le quánchǎng gōngjiàng.",
                "en": "The boy passing the court paused curiously, tilting his head to look at the elevated baskets, blurted: 'Look, wouldn't sawing off the bottoms solve everything?' That candid remark instantly woke all the workmen.",
                "es": "El niño que pasaba se detuvo con curiosidad, contempló las canastas en lo alto y soltó: 'Miren, ¿acaso no se arregla cortando el fondo?' Aquella obviedad inocente iluminó de golpe a todos los presentes."
            }
        ]
    },

    # 32 困扰
    {
        "id": "32",
        "hanzi": "困扰",
        "pinyin": "kùn rǎo",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to perplex; trouble; haunt; distress; dilemma",
            "es": "atormentar; agobiar; desconcertar; quebradero de cabeza"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to cause someone persistent worry, difficulty, or psychological perplexity",
                "definition_es": "inquietar o causar desazón mental continua ante un problema difícil de resolver",
                "example_phrase": "深受失眠问题的困扰 (deeply troubled by insomnia problems)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a nagging difficulty, dilemma, or source of perplexity",
                "definition_es": "motivo de honda preocupación o dilema persistente",
                "example_phrase": "摆脱长期的生活困扰 (shake off long-term troubles of life)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "连续数周的高强度加班和日益严苛的业绩考核，让这位年轻的项目总监饱受焦虑和失眠的困扰。",
                "pinyin": "Liánxù shù zhōu de gāo qiángdù jiābān hé rìyì yánkē de yèjì kǎohé, ràng zhè wèi niánqīng de xiàngmù zǒngjiān bǎoshòu jiāolǜ hé shīmián de kùnrǎo.",
                "en": "Weeks of intense overtime and increasingly harsh performance metrics left the young project director deeply troubled by anxiety and insomnia.",
                "es": "Semanas consecutivas de horas extras y exigentes evaluaciones de rendimiento dejaron al joven director de proyectos agobiado por el insomnio y la ansiedad."
            },
            {
                "id": "#2",
                "hanzi": "长期困扰该地区经济发展的交通瓶颈问题，终于在新建的高速公路通车后得到了根本性缓解。",
                "pinyin": "Chángqī kùnrǎo gāi dìqū jīngjì fāzhǎn de jiāotōng píngjǐng wèntí, zhōngyú zài xīnjiàn de gāosù gōnglù tōngchē hòu dédào le gēnběnxìng huǎnjiě.",
                "en": "The transportation bottleneck that had long troubled regional economic development was fundamentally alleviated once the new expressway opened.",
                "es": "El cuello de botella logístico que atormentaba el desarrollo económico comarcal se resolvió con la inauguración de la nueva autovía."
            }
        ],
        "collocations": [
            {"hanzi": "深受困扰", "en": "deeply troubled / harassed"},
            {"hanzi": "摆脱困扰", "en": "cast off troubles / perplexities"},
            {"hanzi": "解决困扰", "en": "resolve a nagging difficulty"},
            {"hanzi": "带来困扰", "en": "bring distress or trouble"},
            {"hanzi": "长期困扰", "en": "long-term dilemma / trouble"},
            {"hanzi": "精神困扰", "en": "mental / psychological distress"}
        ],
        "idioms": [
            {"hanzi": "焦头烂额", "pinyin": "jiāo tóu làn é", "meaning_en": "scorched head and battered forehead; overwhelmed with distress"},
            {"hanzi": "心烦意乱", "pinyin": "xīn fán yì luàn", "meaning_en": "agitated and confused; perturbed in mind"},
            {"hanzi": "不知所措", "pinyin": "bù zhī suǒ cuò", "meaning_en": "at one's wits' end; not knowing what to do"},
            {"hanzi": "忧心忡忡", "pinyin": "yōu xīn chōng chōng", "meaning_en": "laden with heavy anxieties and care"}
        ],
        "character_decomposition": [
            {
                "character": "困",
                "pinyin": "kùn",
                "meaning_en": "trapped; surrounded; hard-pressed",
                "meaning_es": "acorralado; sitiado; fatigado",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (enclosing perimeter) + 木 (tree / timber)",
                "sound_component": "困 (kùn)",
                "stroke_count": 7,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "A tree 木 trapped tightly within an enclosure 囗; unable to grow or spread roots, symbolizing being trapped in dire straits.",
                "visual_mnemonic_story_en": "A leafy tree (木) confined inside a cramped stone wall (囗), stunted and trapped in distress (困).",
                "visual_mnemonic_story_es": "Un árbol (木) enclaustrado dentro de cuatro muros (囗), asfixiado y atrapado en apuros (困).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "WDI",
                "traditional": "困"
            },
            {
                "character": "扰",
                "pinyin": "rǎo",
                "meaning_en": "disturb; trouble; harass; agitate",
                "meaning_es": "molestar; perturbar; desasosegar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (restless hand) + 尤 (outstanding / faulty)",
                "sound_component": "尤 (yóu / phonetic association)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 beside 尤; restless hands stirring up trouble, creating irritation and emotional agitation.",
                "visual_mnemonic_story_en": "A meddling hand (扌) stirring up trouble (尤) to disturb domestic peace (扰).",
                "visual_mnemonic_story_es": "Una mano inquieta (扌) que agita y remueve discordias (尤) turbando la paz (扰).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "QIKU",
                "traditional": "擾"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Being trapped like a walled-in tree (困) while agitated by meddling hands (扰) produces deep distress (困扰).",
            "composite_memory_hook_es": "Estar acorralado sin salida (困) mientras te inquietan agitaciones ajenas (扰) genera hondo agobio (困扰).",
            "cultural_and_cognitive_roots": "Blends spatial confinement (困) with psychic agitation (扰) into an evocative compound for modern dilemmas.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by dipping third tone: 'kùn rǎo' (51-214). Drop decisively on 'kùn', then dip low and scoop upward on 'rǎo'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "困", "pinyin": "kùn", "meaning_en": "trapped; sleepy", "distinction_note": "Tree 木 inside enclosure 囗"},
                {"character": "因", "pinyin": "yīn", "meaning_en": "cause; reason", "distinction_note": "Big 大 inside enclosure 囗"},
                {"character": "扰", "pinyin": "rǎo", "meaning_en": "disturb", "distinction_note": "Hand radical 扌 on left with 尤"},
                {"character": "拢", "pinyin": "lǒng", "meaning_en": "gather; draw together", "distinction_note": "Hand radical 扌 on left with 龙"}
            ],
            "etymological_cognates": [
                {"character": "烦", "pinyin": "fán", "gloss_en": "vexed; troublesome"},
                {"character": "恼", "pinyin": "nǎo", "gloss_en": "irritated; angry"},
                {"character": "缠", "pinyin": "chán", "gloss_en": "entangle; pester"},
                {"character": "乱", "pinyin": "luàn", "gloss_en": "chaos; disorder"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "困扰 denotes persistent psychological vexation or chronic technical dilemmas requiring resolution.",
            "contrasts": [
                {"id": 1, "compared_word": "困扰 vs. 骚扰", "pinyin": "sāorǎo", "analysis": "骚扰 involves malicious, intrusive harassment from external predators or spam, whereas 困扰 is an ongoing internal mental distress or technical bottleneck."},
                {"id": 2, "compared_word": "困扰 vs. 打扰", "pinyin": "dǎrǎo", "analysis": "打扰 is a polite colloquial term for interrupting someone temporarily (打扰一下), without deep existential anguish."},
                {"id": 3, "compared_word": "困扰 vs. 障碍", "pinyin": "zhàng'ài", "analysis": "障碍 refers to concrete tangible physical or policy barriers, while 困扰 is cognitive distress."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "很多职场人在面对海量碎片化信息与无休止的即时通讯时，常常深陷注意力涣散与精神焦虑的困扰。若想重获心灵的宁静与工作的高效，就必须勇于自我设限，学会定期给大脑做‘断舍离’的清理减负。",
                "pinyin": "Hěnduō zhíchǎngrén zài miànduì hǎiliàng suìpiànhuà xìnxī yǔ wúxiūzhǐ de jíshí tōngxùn shí, chángcháng shēnxiàn zhùyìlì huànsàn yǔ jīngshén jiāolǜ de kùnrǎo. Ruò xiǎng chónghuò xīnlíng de níngjìng yǔ gōngzuò de gāoxiào, jiù bìxū yǒngyú zìwǒ shèxiàn, xuéhuì dìngqī gěi dànǎo zuò 'duànshělí' de qīnglǐ jiǎnfù.",
                "en": "Faced with fragmented info and endless instant chats, professionals suffer from distraction and anxiety. To regain mental peace and work efficiency, one must dare to set boundaries and declutter the brain regularly.",
                "es": "Ante la avalancha de mensajes instantáneos, muchos profesionales padecen dispersión y agobio. Para recobrar la calma y rendir con eficacia, urge fijar límites y depurar la sobrecarga mental."
            },
            {
                "id": "#2",
                "hanzi": "在篮球运动诞生最初的那段岁月里，每次投篮进球后的强制取球停顿，曾是让所有人焦头烂额的巨大困扰。大家习惯性地在‘如何更省力地把球取出来’的固有逻辑里打转，直到锯开筐底的直截了当，才彻底粉碎了这一旷日持久的困扰。",
                "pinyin": "Zài lánqiú yùndòng dànshēng zuìchū de nà duàn suìyuè lǐ, měicì tóulán jìnqiú hòu de qiángzhì qǔ qiú tíngdùn, céng shì ràng suǒyǒurén jiāotóu-làn'é de jùdà kùnrǎo. Dàjiā xíguànxìng de zài 'rúhé gèng shěnglì de bǎ qiú qǔ chūlái' de gùyǒu luóji lǐ dǎzhuàn, zhídào jù kāi kuāngdǐ de zhíjié-liǎodàng, cái chèdǐ fěnsuì le zhè yí kuàngrì-jiǔchí de kùnrǎo.",
                "en": "In basketball's nascent days, retrieving balls after scores was a persistent headache. People circled round the premise of 'how to extract balls with less effort', until sawing off the bottoms shattered this chronic dilemma.",
                "es": "En la infancia del baloncesto, recuperar el balón tras encestar fue un agobio constante. Todos cavilaban sobre cómo extraerlo con menos esfuerzo, hasta que una sierra abrió la base extirpando el quebradero de cabeza."
            }
        ]
    },

    # 33 思维
    {
        "id": "33",
        "hanzi": "思维",
        "pinyin": "sī wéi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "thinking; thought; cognitive mindset; mental logic",
            "es": "pensamiento; modo de pensar; lógica mental; intelecto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the cognitive process of reflecting, reasoning, and conceptualizing using the human mind",
                "definition_es": "proceso intelectivo y cognitivo de razonar, abstraer y concebir ideas en la mente",
                "example_phrase": "逻辑思维能力 (logical thinking ability)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "数学奥林匹克竞赛不仅考核基础公式的计算速度，更着重考察参赛选手严密的抽象逻辑思维能力。",
                "pinyin": "Shùxué Àolínpǐkè jìngsài bùjǐn kǎohé jīchǔ gōngshì de jìsuàn sùdù, gèng zhuózhòng kǎochá cānsài xuǎnshǒu yánmì de chōuxiàng luóji sīwéi nénglì.",
                "en": "Math Olympiad competitions test not only speed in calculating basic formulas, but focus primarily on competitors' rigorous abstract logical thinking skills.",
                "es": "Las Olimpiadas de Matemáticas no sólo evalúan el cálculo de fórmulas, sino el rigor y agudeza del pensamiento lógico abstracto de los participantes."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的技术革命，领导者必须主动打破原有的思维定式，以更加开放包容的心态拥抱未知。",
                "pinyin": "Miànduì shùnxī-wànbiàn de jìshù gémìng, lǐngdǎozhě bìxū zhǔdòng dǎpò yuányǒu de sīwéi dìngshì, yǐ gèngjiā kāifàng bāoróng de xīntài yōngbào wèizhī.",
                "en": "Confronted by rapid technological upheaval, leaders must proactively shatter existing cognitive mindsets and embrace the unknown with an open heart.",
                "es": "Ante la vertiginosa revolución tecnológica, los líderes deben quebrar sus esquemas mentales preconcebidos y acoger lo ignoto con amplitud de miras."
            }
        ],
        "collocations": [
            {"hanzi": "思维定式", "en": "fixed mindset / mental rut"},
            {"hanzi": "逻辑思维", "en": "logical thinking"},
            {"hanzi": "创新思维", "en": "innovative thinking"},
            {"hanzi": "思维能力", "en": "thinking ability / intellect"},
            {"hanzi": "思维模式", "en": "thought pattern / paradigm"},
            {"hanzi": "批判性思维", "en": "critical thinking"}
        ],
        "idioms": [
            {"hanzi": "深谋远虑", "pinyin": "shēn móu yuǎn lǜ", "meaning_en": "plan deeply and foresee distantly; farsighted strategy"},
            {"hanzi": "墨守成规", "pinyin": "mò shǒu chéng guī", "meaning_en": "stick stubbornly to obsolete conventions"},
            {"hanzi": "见微知著", "pinyin": "jiàn wēi zhī zhù", "meaning_en": "discern future macro trends from minute signs"},
            {"hanzi": "运筹帷幄", "pinyin": "yùn chóu wéi wò", "meaning_en": "devise strategies within military tents; mastermind victories"}
        ],
        "character_decomposition": [
            {
                "character": "思",
                "pinyin": "sī",
                "meaning_en": "think; consider; deliberate; miss",
                "meaning_es": "pensar; reflexionar; meditar",
                "radical": "心",
                "radical_meaning_en": "heart",
                "meaning_component": "囟 / 田 (brain cranium fontanelle) + 心 (heart consciousness)",
                "sound_component": "思 (sī)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Brain cranium 田 (囟) atop heart 心; in classical Chinese philosophy, the heart and brain collaborate as seat of cognition and contemplation.",
                "visual_mnemonic_story_en": "The brain (田) and the feeling heart (心) harmonizing in quiet reflection (思).",
                "visual_mnemonic_story_es": "El cerebro pensante (田) y el corazón sensible (心) concertados en profunda meditación (思).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "WP",
                "traditional": "思"
            },
            {
                "character": "维",
                "pinyin": "wéi",
                "meaning_en": "tie; maintain; dimension",
                "meaning_es": "atar; preservar; dimensión",
                "radical": "纟",
                "radical_meaning_en": "silk thread",
                "meaning_component": "纟 (binding cords) + 隹 (bird with short tail)",
                "sound_component": "隹 (zhuī / phonetic association)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Silk radical 纟 tethering short-tailed bird 隹; tying corners and cords together, extended to mental fabric, dimensions, and maintenance.",
                "visual_mnemonic_story_en": "Strong silk cords (纟) tying the corner poles of a tent firmly in multi-dimensional balance (维).",
                "visual_mnemonic_story_es": "Fuertes cuerdas de seda (纟) tensando los amarres de una tienda en armonía tridimensional (维).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "VFOV",
                "traditional": "維"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The heart-brain pondering (思) woven into a structured mental framework (维) forms cognitive thinking (思维).",
            "composite_memory_hook_es": "El juicio reflexivo (思) enhebrado en una red conceptual sólida (维) da lugar al pensamiento (思维).",
            "cultural_and_cognitive_roots": "Represents the intellectual lattice of human reasoning, balancing philosophical insight with practical problem-solving.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by rising second tone: 'sī wéi' (55-35). Hold 'sī' high, then soar gracefully on 'wéi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "思", "pinyin": "sī", "meaning_en": "think; ponder", "distinction_note": "Field 田 over heart 心"},
                {"character": "恩", "pinyin": "ēn", "meaning_en": "grace; kindness", "distinction_note": "Cause 因 over heart 心"},
                {"character": "维", "pinyin": "wéi", "meaning_en": "maintain; tie", "distinction_note": "Silk radical 纟 on left with 隹"},
                {"character": "谁", "pinyin": "shuí", "meaning_en": "who", "distinction_note": "Speech radical 讠 on left with 隹"}
            ],
            "etymological_cognates": [
                {"character": "考", "pinyin": "kǎo", "gloss_en": "examine; ponder"},
                {"character": "虑", "pinyin": "lǜ", "gloss_en": "consider; deliberate"},
                {"character": "想", "pinyin": "xiǎng", "gloss_en": "think; yearn"},
                {"character": "念", "pinyin": "niàn", "gloss_en": "recollect; idea"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "思维 denotes higher-order cognitive faculties, mental paradigms, and structured logical deduction.",
            "contrasts": [
                {"id": 1, "compared_word": "思维 vs. 思想", "pinyin": "sīxiǎng", "analysis": "思想 denotes overarching ideological beliefs, philosophical outlooks, or political doctrine, while 思维 refers to cognitive logic and problem-solving patterns."},
                {"id": 2, "compared_word": "思维 vs. 想法", "pinyin": "xiǎngfǎ", "analysis": "想法 refers to a specific concrete opinion, notion, or idea on a matter, whereas 思维 is the cognitive apparatus producing ideas."},
                {"id": 3, "compared_word": "思维 vs. 情绪", "pinyin": "qíngxù", "analysis": "情绪 encompasses physiological affective moods and feelings, directly contrasting with rational 思维."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "哲学家笛卡尔曾留下‘我思故我在’的千古名言，揭示了理性思维是确证个体自我存在与认识宇宙的根本基石。人类唯有保持持续反省与独立深邃的理性思维，才能在纷繁复杂的世俗尘嚣中擦亮双眼，不被盲从的群体偏见所裹挟。",
                "pinyin": "Zhéxuéjiā Díkǎ'ěr céng liúxià 'wǒ sī gù wǒ zài' de qiāngǔ míngyán, jiēshì le lǐxìng sīwéi shì quèzhèng gètǐ zìwǒ cúnzài yǔ rènzhī yǔzhòu de gēnběn jīshí. Rénlèi wéiyǒu bǎochí chíxù fǎnxǐng yǔ dúlì shēnxuì de lǐxìng sīwéi, cái néng zài fēnfán-fùzá de shìsú chénxiāo zhōng cāliàng shuāngyǎn, bù bèi mángcóng de qúntǐ piānjiàn suǒ guǒxié.",
                "en": "Descartes coined 'I think, therefore I am', proving rational thought is the bedrock confirming existence. Only by nurturing deep reflective thinking can humanity see clearly amid worldly distractions, resisting herd bias.",
                "es": "Descartes proclamó 'pienso, luego existo', situando el raciocinio como cimiento del ser. Sólo cultivando un criterio lúcido y reflexivo preservará el ser humano su discernimiento ante el ruido gregario."
            },
            {
                "id": "#2",
                "hanzi": "篮球发展史上的‘筐底革命’，本质上是一场颠覆性的思维突破。工匠们最初被‘筐必定有底’的传统经验死死框住，一心只想研制复杂的取球器械。直到有人跳出思维定势，人们才恍然大悟：去掉无用的底子，才是最高明的思维解法。",
                "pinyin": "Lánqiú fāzhǎnshǐ shang de 'kuāngdǐ gémìng', běnzhì shang shì yì chǎng diānfùxìng de sīwéi tūpò. Gōngjiàngmen zuìchū bèi 'kuāng bìdìng yǒu dǐ' de chuántǒng jīngyàn sǐsǐ kuàng zhù, yìxīn zhǐ xiǎng yánzhì fùzá de qǔ qiú qìxiè. Zhídào yǒurén tiào chū sīwéi dìngshì, rénmen cái huǎngrán-dàwù: qùdiào wúyòng de dǐzi, cái shì zuì gāomíng de sīwéi jiěfǎ.",
                "en": "The basket revolution in basketball history was at heart a paradigm shift. Craftsmen were trapped by the assumption that 'baskets must have bottoms', scheming complex gizmos. Breaking that mental rut revealed the truth: removing the bottom was the ultimate solution.",
                "es": "La revolución del fondo de la canasta fue un audaz salto cognitivo. Los conserjes creían a ciegas que 'toda cesta debe tener fondo', discurriendo artificios. Romper ese esquema demostró que eliminar lo sobrante era la solución genial."
            }
        ]
    },

    # 34 呆
    {
        "id": "34",
        "hanzi": "呆",
        "pinyin": "dāi",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "dull; foolish; blank; to stay; dawdle",
            "es": "atontado; boquiabierto; torpe; quedarse; permanecer"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "dull-witted, sluggish, or staring blankly with an immobile expression",
                "definition_es": "quedarse pasmado, atónito o con la mirada perdida sin reaccionar",
                "example_phrase": "吓得目瞪口呆 (scared stiff and dumbfounded)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Colloquial",
                "definition_en": "to stay, linger, or remain in a place without moving",
                "definition_es": "permanecer o quedarse en un sitio durante un tiempo",
                "example_phrase": "在老家呆了两个星期 (stayed in hometown for two weeks)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "听到突如其来的失业噩耗，他整个人顿时呆立在原地，脑子里一片空白不知该如何是好。",
                "pinyin": "Tīngdào tūrúqílái de shīyè èhào, tā zhěngrén dùnshí dāi lì zài yuándì, nǎozǐ lǐ yípiàn kòngbái bùzhī gāi rúhé shì hǎo.",
                "en": "Hearing the abrupt catastrophic news of his layoff, he stood blankly rooted to the spot, his mind an utter void not knowing what to do.",
                "es": "Al enterarse del repentino despido, se quedó paralizado en el sitio boquiabierto, con la mente en blanco y sin saber cómo reaccionar."
            },
            {
                "id": "#2",
                "hanzi": "周末他哪儿也不想去，就喜欢一个人静静地呆在飘着书香的书房里喝茶看书。",
                "pinyin": "Zhōumò tā nǎr yě bù xiǎng qù, jiù xǐhuan yí ge rén jìngjìng de dāi zài piāozhe shūxiāng de shūfáng lǐ hēchá kànshū.",
                "en": "On weekends he had no wish to go anywhere, preferring to stay quietly alone in his book-scented study drinking tea and reading.",
                "es": "Los fines de semana no le apetece salir; prefiere quedarse plácidamente en el estudio disfrutando de la lectura y un té aromático."
            }
        ],
        "collocations": [
            {"hanzi": "目瞪口呆", "en": "dumbfounded; flabbergasted"},
            {"hanzi": "发呆", "en": "stare blankly; day-dream"},
            {"hanzi": "呆滞", "en": "dull; sluggish; stagnant"},
            {"hanzi": "呆板", "en": "inflexible; wooden; rigid"},
            {"hanzi": "呆在家里", "en": "stay at home"},
            {"hanzi": "看呆了", "en": "watch in stunned bewilderment"}
        ],
        "idioms": [
            {"hanzi": "目瞪口呆", "pinyin": "mù dèng kǒu dāi", "meaning_en": "stare wide-eyed and open-mouthed; struck dumb with shock"},
            {"hanzi": "呆若木鸡", "pinyin": "dāi ruò mù jī", "meaning_en": "transfixed like a wooden cock; motionless with shock or mastery"},
            {"hanzi": "大智若愚", "pinyin": "dà zhì ruò yú", "meaning_en": "supreme wisdom seems like foolishness; profound depth"},
            {"hanzi": "死板教条", "pinyin": "sǐ bǎn jiào tiáo", "meaning_en": "dogmatic and rigid in thinking"}
        ],
        "character_decomposition": [
            {
                "character": "呆",
                "pinyin": "dāi",
                "meaning_en": "dull; foolish; blank; stay",
                "meaning_es": "bobo; pasmado; quedarse",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (open mouth) + 木 (wooden post / immobile tree)",
                "sound_component": "呆 (dāi)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Open mouth 口 resting stiffly on top of wooden post 木; standing frozen with mouth agape like a wooden statue.",
                "visual_mnemonic_story_en": "Standing stiff as a wooden tree (木) with mouth gaping wide open (口) in stunned silence (呆).",
                "visual_mnemonic_story_es": "Quedarse inmóvil como un madero seco (木) con la boca abierta (口) atónito de asombro (呆).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RD",
                "traditional": "呆"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Having your mouth open (口) while frozen like a wooden stump (木) makes you look blank and stunned (呆).",
            "composite_memory_hook_es": "Tener la boca abierta (口) petrificado como un poste de madera (木) te deja boquiabierto (呆).",
            "cultural_and_cognitive_roots": "Derives from Zhuangzi's fable of the fighting cock (呆若木鸡) which appears motionless and dull but possesses unbeatable calm.",
            "tone_sandhi_and_pitch_modulation": "Level high tone: 'dāi' (55). Sustain an even high tone without dropping in pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "呆", "pinyin": "dāi", "meaning_en": "dull; blank; stay", "distinction_note": "Mouth 口 on top over wood 木"},
                {"character": "杏", "pinyin": "xìng", "meaning_en": "apricot", "distinction_note": "Wood 木 on top over mouth 口"},
                {"character": "困", "pinyin": "kùn", "meaning_en": "trapped; surrounded", "distinction_note": "Wood 木 inside enclosure 囗"},
                {"character": "保", "pinyin": "bǎo", "meaning_en": "protect; preserve", "distinction_note": "Person radical 亻 on left of 呆"}
            ],
            "etymological_cognates": [
                {"character": "傻", "pinyin": "shǎ", "gloss_en": "foolish; silly"},
                {"character": "痴", "pinyin": "chī", "gloss_en": "infatuated; foolish"},
                {"character": "滞", "pinyin": "zhì", "gloss_en": "stagnant; sluggish"},
                {"character": "钝", "pinyin": "dùn", "gloss_en": "blunt; slow-witted"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "呆 indicates temporary mental blankness, frozen immobility, or colloquially lingering in a location.",
            "contrasts": [
                {"id": 1, "compared_word": "呆 vs. 傻", "pinyin": "shǎ", "analysis": "傻 describes innate silliness, naivety, or lack of intelligence, whereas 呆 emphasizes staring blankly or standing frozen in shock."},
                {"id": 2, "compared_word": "呆 vs. 留", "pinyin": "liú", "analysis": "留 is formal for staying or detaining (留步, 留学), while 呆 is informal colloquial for hanging around (呆在家里)."},
                {"id": 3, "compared_word": "呆 vs. 愣", "pinyin": "lèng", "analysis": "愣 stresses sudden momentary bewilderment or rash impulsiveness (发愣, 愣头青), while 呆 can be prolonged dullness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "庄子曾借斗鸡寓言阐述‘呆若木鸡’的至高境界。真正顶级的斗鸡既不鸣叫炫耀，也不张牙舞爪，而是如木雕般凝神静气、沉稳呆立，却能令一切对手望而生畏、落荒而逃。这体现了超越浮躁的大智与沉敛。",
                "pinyin": "Zhuāngzǐ céng jiè dòujī yùyán chǎnshù 'dāiruò-mùjī' de zhìgāo jìngjiè. Zhēnzhèng dǐngjí de dòujī jì bù míngjiào xuànyào, yě bù zhāngyá-wǔzhǎo, érshì rú mùdiāo bān nǐngshén-jìngqì, chénwěn dāi lì, què néng lìng yíqiè duìshǒu wàng'ér-shēngwèi, luòhuāng'értáo. Zhè tǐxiàn le chāoyuè fúzào de dàzhì yǔ chénliǎn.",
                "en": "Zhuangzi used the gamecock fable to illustrate the supreme state of 'calm like a wooden rooster'. The finest rooster neither crows nor struts, standing immobile like a wood carving, yet terrifies rivals into flight, exuding calm depth.",
                "es": "Zhuangzi ilustró con el gallo de pelea la cumbre del sosiego impávido. El mejor gallo no cacarea ni aletea; permanece plantado como talla de madera y su aplomo espanta a los rivales, encarnando la serenidad suprema."
            },
            {
                "id": "#2",
                "hanzi": "当年在篮球场上，当小男孩说出锯掉筐底的瞬间，满场的大人们全惊呆了。工人们面面相觑地呆立了数秒，随后爆发出一阵如释重负的会心大笑。那一刻的目瞪口呆，正是思维冲破传统牢笼时不可避免的心智激荡。",
                "pinyin": "Dāngnián zài lánqiúchǎng shang, dāng xiǎo nánhái shuōchū jù diào kuāngdǐ de shùnjiān, mǎn chǎng de dàrenmen quán jīng dāi le. Gōngrénmen miànmiàn-xiāngqù de dāi lì le shù miǎo, suíhòu bàofā chū yí zhèn rúshì-zhòngfù de huìxīn dàxiào. Nà yí kè de mùdèng-kǒudāi, zhèng shì sīwéi chōngpò chuántǒng láolóng shí bùkě-bìmiǎn de xīnjiào jīdàng.",
                "en": "When the boy suggested sawing off the bottom, the adults on the court were struck dumb. Workers stood staring blankly for seconds before bursting into relieved laughter. That stunned moment captured the shock of minds bursting free from ruts.",
                "es": "Al proponer el chiquillo recortar el fondo, los adultos se quedaron boquiabiertos. Se miraron atónitos unos instantes antes de romper en risas de alivio. Ese instante de pasmo reflejó el despertar de la mente rompiendo viejas ataduras."
            }
        ]
    },

    # 35 造成
    {
        "id": "35",
        "hanzi": "造成",
        "pinyin": "zào chéng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to cause; bring about; give rise to (usually negative results)",
            "es": "causar; provocar; ocasionar; dar lugar a"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to cause, bring about, or result in an unfavorable, problematic, or harmful consequence",
                "definition_es": "ocasionar, producir o desembocar en una consecuencia perjudicial, dañina o indeseable",
                "example_phrase": "造成不可挽回的重大损失 (cause irreversible major losses)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "由于施工方在深基坑作业中违规操作，导致地下自来水主管道破裂，给周边居民供水造成了极大不便。",
                "pinyin": "Yóuyú shīgōngfāng zài shēn jīkēng zuòyè zhōng wéiguī cāozuò, dǎozhì dìxià zìláishuǐ zhǔguǎndào pòliè, gěi zhōubiān jūmín gōngshuǐ zàochéng le jídà búbiàn.",
                "en": "Due to irregular drilling in deep foundation pits by contractors, the underground water main ruptured, causing severe inconvenience to surrounding residents' water supply.",
                "es": "Debido a una maniobra antirreglamentaria en las obras, se rompió la tubería principal subterránea, causando graves molestias al suministro vecinal."
            },
            {
                "id": "#2",
                "hanzi": "如果不能及时疏导青少年的负面情绪，长期的心理压抑将对其身心健康造成深远的负面影响。",
                "pinyin": "Rúguǒ bùnéng jíshí shūdǎo qīng-shàonián de fùmiàn qíngxù, chángqī de xīnlǐ yāyì jiāng duì qí shēnxīn jiànkāng zàochéng shēnyuǎn de fùmiàn yǐngxiǎng.",
                "en": "If adolescents' negative emotions are not channeled in time, prolonged psychological distress will cause profound adverse effects on their well-being.",
                "es": "Si no se encauzan a tiempo las emociones negativas en adolescentes, la represión psicológica prolongada causará hondos perjuicios a su salud mental."
            }
        ],
        "collocations": [
            {"hanzi": "造成损失", "en": "cause financial loss / damage"},
            {"hanzi": "造成严重后果", "en": "cause grave consequences"},
            {"hanzi": "造成不良影响", "en": "cause adverse impact"},
            {"hanzi": "造成伤亡", "en": "cause casualties"},
            {"hanzi": "造成拥堵", "en": "cause traffic congestion"},
            {"hanzi": "造成误解", "en": "cause misunderstanding"}
        ],
        "idioms": [
            {"hanzi": "祸从口出", "pinyin": "huò cóng kǒu chū", "meaning_en": "disaster comes from careless mouth; loose lips sink ships"},
            {"hanzi": "遗祸无穷", "pinyin": "yí huò wú qióng", "meaning_en": "bequeath endless disasters; cause endless trouble"},
            {"hanzi": "木已成舟", "pinyin": "mù yǐ chéng zhōu", "meaning_en": "the timber has been carved into a boat; what is done cannot be undone"},
            {"hanzi": "后患无穷", "pinyin": "hòu huàn wú qióng", "meaning_en": "breed unending future troubles"}
        ],
        "character_decomposition": [
            {
                "character": "造",
                "pinyin": "zào",
                "meaning_en": "create; build; fabricate; cause",
                "meaning_es": "crear; construir; fabricar; causar",
                "radical": "辶",
                "radical_meaning_en": "movement",
                "meaning_component": "辶 (advance on path) + 告 (announce / sacrifice bull)",
                "sound_component": "告 (gào / phonetic)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Advancing on the road 辶 toward sacrifice altars to make prayers 告; extended to manufacturing, constructing, and generating outcomes.",
                "visual_mnemonic_story_en": "Advancing along a road (辶) while making an official announcement (告) to create a new institution (造).",
                "visual_mnemonic_story_es": "Avanzar por un camino (辶) proclamando decretos (告) para fundar una nueva obra (造).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YHGR",
                "traditional": "造"
            },
            {
                "character": "成",
                "pinyin": "chéng",
                "meaning_en": "become; complete; achieve; succeed",
                "meaning_es": "convertirse; completar; lograr",
                "radical": "戈",
                "radical_meaning_en": "halberd / spear",
                "meaning_component": "戈 (weapon) + 𢦏 (firm foundation wall)",
                "sound_component": "成 (chéng)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A spear 戈 defending a newly completed fortified wall settlement; accomplishing construction and reaching fruition.",
                "visual_mnemonic_story_en": "Planting a protective spear (戈) upon the completed stone battlements: full accomplishment (成).",
                "visual_mnemonic_story_es": "Clavar una lanza (戈) sobre las almenas concluidas de la muralla: obra culminada (成).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IHSH",
                "traditional": "成"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Actions actively built and engineered (造) that settle into a lasting result (成) bring about a consequence (造成).",
            "composite_memory_hook_es": "Actos fraguados con afán (造) que cuajan en un resultado consumado (成) ocasionan una consecuencia (造成).",
            "cultural_and_cognitive_roots": "Semantic preference: unlike neutral '产生' or positive '促成', '造成' predominantly introduces negative, regrettable outcomes.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone followed by rising second tone: 'zào chéng' (51-35). Drive down forcefully on 'zào', then rise on 'chéng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "造", "pinyin": "zào", "meaning_en": "create; cause", "distinction_note": "Movement radical 辶 with 告"},
                {"character": "选", "pinyin": "xuǎn", "meaning_en": "choose; select", "distinction_note": "Movement radical 辶 with 先"},
                {"character": "成", "pinyin": "chéng", "meaning_en": "become; complete", "distinction_note": "6 strokes including slanted hook and 戈 axe"},
                {"character": "戍", "pinyin": "shù", "meaning_en": "garrison frontier", "distinction_note": "Has a dot inside the corner"}
            ],
            "etymological_cognates": [
                {"character": "致", "pinyin": "zhì", "gloss_en": "cause; lead to"},
                {"character": "致", "pinyin": "zhì", "gloss_en": "incur; deliver"},
                {"character": "引", "pinyin": "yǐn", "gloss_en": "lead to; trigger"},
                {"character": "酿", "pinyin": "niàng", "gloss_en": "ferment; brew crisis"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "造成 is a causal verb almost exclusively paired with undesirable, negative, or harmful nouns.",
            "contrasts": [
                {"id": 1, "compared_word": "造成 vs. 导致", "pinyin": "dǎozhì", "analysis": "导致 can be followed by a full explanatory clause or verb phrase (导致比赛中断), whereas 造成 is strictly paired with a noun object (造成恶劣影响)."},
                {"id": 2, "compared_word": "造成 vs. 产生", "pinyin": "chǎnshēng", "analysis": "产生 is completely neutral and can introduce positive breakthroughs (产生灵感, 产生效益), unlike the negative bias of 造成."},
                {"id": 3, "compared_word": "造成 vs. 引起", "pinyin": "yǐnqǐ", "analysis": "引起 means to attract or arouse notice, discussion, or reaction (引起广泛关注), without necessarily implying catastrophic damage."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "盲目砍伐原始森林不仅破坏了珍稀野生动物的天然栖息家园，更诱发了严重的水土流失与频繁的山体滑坡，给流域下游居民的生命财产安全造成了巨大威胁。人与自然唯有和谐共生，方能守住绿水青山的美好家园。",
                "pinyin": "Mángmù kǎnfá yuánshǐ sēnlín bùjǐn pòhuài le zhēnxī yěshēng dòngwù de tiānrán qīxī jiāyuán, gèng yòufā le yánzhòng de shuǐtǔ liúshī yǔ pínfán de shāntǐ huápō, gěi liùyù xiàyóu jūmín de shēngmìng cáichǎn ānquán zàochéng le jùdà wēixié. Rén yǔ zìrán wéiyǒu héxié gòngshēng, fāng néng shǒuzhù lǜshuǐ-qīngshān de měihǎo jiāyuán.",
                "en": "Deforesting virgin timber not only ravages wildlife habitats, but induces severe soil erosion and landslides, posing grave hazards to downstream communities. Only by living in harmony with nature can humanity safeguard its home.",
                "es": "La tala indiscriminada devasta los hábitats silvestres y desata deslaves, causando graves estragos en las poblaciones ribereñas. Sólo conviviendo en armonía con la naturaleza preservaremos la belleza de nuestra tierra."
            },
            {
                "id": "#2",
                "hanzi": "当年在篮球运动起步阶段，那个未经改造的带底果筐给整场赛事造成了极大的节奏阻碍。每次投篮得分都迫使比赛停摆，频繁的停滞给观众的观赛体验造成了严重破坏。直到有人果断锯掉筐底，才从根源上消除了这个造成混乱的症结。",
                "pinyin": "Dāngnián zài lánqiú yùndòng qǐbù jiēduàn, nà ge wèijīng gǎizào de dàidǐ guǒkuāng gěi zhěngchǎng sàishì zàochéng le jídà de jiézòu zǔ'ài. Měicì tóulán défēn dōu pòshǐ bǐsài tíngbǎi, pínfán de tíngzhì gěi guānzhòng de guānsài tǐyàn zàochéng le yánzhòng pòhuài. Zhídào yǒurén guǒduàn jù diào kuāngdǐ, cái cóng gēnyuán shang xiāochú le zhè ge zàochéng hùnluàn de zhèngjié.",
                "en": "At basketball's inception, unadapted closed baskets caused enormous rhythmic bottlenecks. Scores halted play, ruining the spectator experience. Only when someone sawed off the bottoms was this root cause of disruption eliminated for good.",
                "es": "En los inicios del baloncesto, las cestas ciegas causaron grandes parones en el juego. Cada canasta congelaba el partido, arruinando la emoción del público. Al serrar el fondo, se erradicó de raíz la causa de tanto trastorno."
            }
        ]
    },

    # 36 仿佛
    {
        "id": "36",
        "hanzi": "仿佛",
        "pinyin": "fǎng fú",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "as if; to seem; like; resemblance",
            "es": "como si; parecer; semejante a; tal parece"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Literary",
                "definition_en": "seeming as if; resembling in appearance, impression, or feeling",
                "definition_es": "da la impresión de que; como si; de manera muy semejante o ilusoria",
                "example_phrase": "仿佛回到了快乐的童年时代 (as if returning to happy childhood days)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "微风吹拂过宁静的湖面，层层荡漾的粼粼波光仿佛无数碎银在月色下欢快跳跃。",
                "pinyin": "Wēifēng chuīfú guò níngjìng de húmiàn, céngcéng dàngyàng de línlín bōguāng fǎngfú wúshù suìyín zài yuèyè xià huānkuài tiàoyuè.",
                "en": "Gentle breezes swept across the peaceful lake; rippling glimmering wavelets looked as if countless shards of broken silver were dancing under the moonlight.",
                "es": "La brisa rozaba el lago plácido; los reflejos centelleantes en las ondas parecían trozos de plata viva danzando bajo la luna."
            },
            {
                "id": "#2",
                "hanzi": "听着老艺人悠扬婉转的古筝弹奏，台下观众仿佛置身于烟雨蒙蒙的江南古镇水巷之中。",
                "pinyin": "Tīng zhe lǎo yìrén yōuyáng wǎnzhuǎn de gǔzhēng tánzòu, táixià guānzhòng fǎngfú zhìshēn yú yānyǔ-méngméng de Jiāngnán gǔzhèn shuǐxiàng zhīzhōng.",
                "en": "Listening to the veteran artist's melodious guzheng performance, the audience felt as if they were transported into misty water lanes of Jiangnan canal towns.",
                "es": "Al escuchar las notas cadenciosas del laúd tradicional, el público creyó hallarse inmerso entre los canales neblinosos de las villas ribereñas del sur."
            }
        ],
        "collocations": [
            {"hanzi": "仿佛是", "en": "seeming as if it were"},
            {"hanzi": "仿佛置身于", "en": "as if placed in the midst of"},
            {"hanzi": "仿佛看到了", "en": "as if having seen"},
            {"hanzi": "仿佛在说", "en": "as if saying"},
            {"hanzi": "仿佛回到了", "en": "as if having returned to"},
            {"hanzi": "神态仿佛", "en": "bearing strikingly resembles"}
        ],
        "idioms": [
            {"hanzi": "如梦初醒", "pinyin": "rú mèng chū xǐng", "meaning_en": "as if waking from a dream; sudden awakening"},
            {"hanzi": "若即若离", "pinyin": "ruò jí ruò lí", "meaning_en": "seeming both close and distant; keeping at arm's length"},
            {"hanzi": "宛若天仙", "pinyin": "wǎn ruò tiān xiān", "meaning_en": "graceful and lovely as a celestial fairy"},
            {"hanzi": "栩栩如生", "pinyin": "xǔ xǔ rú shēng", "meaning_en": "lifelike as if alive; vivid artistic realism"}
        ],
        "character_decomposition": [
            {
                "character": "仿",
                "pinyin": "fǎng",
                "meaning_en": "imitate; like; resemble",
                "meaning_es": "imitar; parecerse; semejante",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person model) + 方 (square / directions)",
                "sound_component": "方 (fāng / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 aligning oneself to standard squares 方; copying models, imitating form, or bearing close likeness.",
                "visual_mnemonic_story_en": "An artist (亻) copying lines precisely along a carpenter's square pattern (方) to replicate an image (仿).",
                "visual_mnemonic_story_es": "Un dibujante (亻) guiándose por una escuadra (方) para calcar una figura con exactitud (仿).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "OYS",
                "traditional": "倣"
            },
            {
                "character": "佛",
                "pinyin": "fú",
                "meaning_en": "resemble; like (fú); Buddha (fó)",
                "meaning_es": "asemejarse; parecer (fú); Buda (fó)",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person) + 弗 (bent bows / negative bound)",
                "sound_component": "弗 (fú / phonetic)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Person radical 亻 with 弗; phonetic borrowing meaning hazy resemblance; pronounced fú in compound '仿佛'.",
                "visual_mnemonic_story_en": "A figure (亻) seen faintly through mist like a bending willow bow (弗), appearing as if in a dream (佛).",
                "visual_mnemonic_story_es": "Una silueta humana (亻) divisada entre brumas (弗), que parece casi una ilusión vaporosa (佛).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "OLLN",
                "traditional": "彿"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A figure imitating form (仿) glimpsed faintly through misty silhouettes (佛) appears as if real (仿佛).",
            "composite_memory_hook_es": "Una figura que imita un modelo (仿) divisada entre brumas tenues (佛) se asemeja a una ilusión (仿佛).",
            "cultural_and_cognitive_roots": "Classical evocative literary conjunction prevalent in poetry and prose (e.g. 朱自清《荷塘月色》) for sensory similes.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by rising second tone: 'fǎng fú' (214-35). Note second-tone reading 'fú' (not 'fó')."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "仿", "pinyin": "fǎng", "meaning_en": "resemble; imitate", "distinction_note": "Person radical 亻 on left with 方"},
                {"character": "伤", "pinyin": "shāng", "meaning_en": "wound; injure", "distinction_note": "Has 𠂉 and 力 inside"},
                {"character": "佛", "pinyin": "fú/fó", "meaning_en": "resemble; Buddha", "distinction_note": "Person radical 亻 on left with 弗"},
                {"character": "拂", "pinyin": "fú", "meaning_en": "brush off; whisk", "distinction_note": "Hand radical 扌 on left of 弗"}
            ],
            "etymological_cognates": [
                {"character": "宛", "pinyin": "wǎn", "gloss_en": "as if; winding"},
                {"character": "似", "pinyin": "sì", "gloss_en": "resemble; like"},
                {"character": "像", "pinyin": "xiàng", "gloss_en": "resemble; picture"},
                {"character": "若", "pinyin": "ruò", "gloss_en": "seem like; if"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "仿佛 is a literary connective establishing poetic similes or subjective dreamlike impressions.",
            "contrasts": [
                {"id": 1, "compared_word": "仿佛 vs. 好像", "pinyin": "hǎoxiàng", "analysis": "好像 is neutral and ubiquitous in everyday conversation, while 仿佛 carries poetic elegance and literary flavor."},
                {"id": 2, "compared_word": "仿佛 vs. 似乎", "pinyin": "sìhū", "analysis": "似乎 conveys logical conjecture or mild uncertainty about facts (他似乎不知道), whereas 仿佛 introduces imaginative figurative similes."},
                {"id": 3, "compared_word": "仿佛 vs. 犹如", "pinyin": "yóurú", "analysis": "犹如 is an explicit literary simile marker directly equating two concrete nouns, while 仿佛 can function adverbially across full narrative clauses."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫步在雨后苍翠欲滴的幽静竹林中，泥土的清芬混合着竹叶的幽香沁人心脾。偶尔几声婉转清脆的鸟鸣穿透林间薄雾，让人心旷神怡，仿佛步入了一幅遗世独立的古代水墨写意长卷。",
                "pinyin": "Mànbù zài yǔhòu cāngcuì-yùdī de yōujìng zhúlín zhōng, nítǔ de qīngfēn hùnhé zhe zhúyè de yōuxiāng qìnrénxīnpí. Ǒu'ěr jǐ shēng wǎnzhuǎn qīngcuì de niǎomíng chuāntòu línjiān báowù, ràng rén xīnkuàng-shényí, fǎngfú bùrù le yì fú yíshì-dúlì de gǔdài shuǐmò xièyì chángjuàn.",
                "en": "Strolling in verdant bamboo groves after rain, the scent of damp earth and bamboo fragrance was intoxicating. Crisp birdsong pierced thin mists; one felt as though stepping straight into an ancient timeless ink wash scroll.",
                "es": "Pasear entre bambúes tras la lluvia embriagaba con aroma a tierra húmeda y hojas frescas. Los trinos rompían la neblina; parecía como si uno se adentrara en un cuadro tradicional de tinta china al margen del mundo."
            },
            {
                "id": "#2",
                "hanzi": "当工人们终于挥动锯子将桃筐底部锯开的那一刹那，在场的所有人仿佛卸下了一幅沉重不堪的枷锁。篮球在投中后顺滑地穿筐而落，场馆内爆发出雷鸣般的喝彩，现代篮球运动仿佛在这一声落地中重获新生。",
                "pinyin": "Dāng gōngrénmen zhōngyú huīdòng jùzi jiāng táokuāng dǐbù jù kāi de nà yí chànà, zàichǎng de suǒyǒurén fǎngfú xièxià le yì fú chénzhòng-bùkān de jiāsuǒ. Lánqiú zài tóu zhòng hòu shùnhuá de chuān kuāng ér luò, chǎngguǎn nèi bàofā chū léimíng bān de hècǎi, xiàndài lánqiú yùndòng fǎngfú zài zhè yì shēng luòdì zhōng chónghuò xīnshēng.",
                "en": "The moment workmen sawed open the basket bottoms, everyone present felt as if a heavy shackle had been lifted. Balls dropped through smoothly; thunderous cheers erupted, as if modern basketball was reborn in that bounce.",
                "es": "En el instante en que la sierra cercenó el fondo de la cesta, todos sintieron como si se liberaran de un pesado yugo. La bola cayó limpia entre ovaciones atronadoras; el baloncesto moderno parecía renacer con aquel bote."
            }
        ]
    },

    # 37 阻碍
    {
        "id": "37",
        "hanzi": "阻碍",
        "pinyin": "zǔ 'ài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to hinder; obstruct; impede; obstacle; barrier",
            "es": "obstaculizar; entorpecer; estorbar; traba; obstáculo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to block, hinder, or make difficult the progress, movement, or development of something",
                "definition_es": "dificultar o impedir el paso, avance o desarrollo de algo o alguien",
                "example_phrase": "阻碍社会经济的健康发展 (hinder healthy socioeconomic development)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a hindrance, obstacle, or impeding condition",
                "definition_es": "cosa que entorpece o estorba la consecución de un fin",
                "example_phrase": "扫清前行道路上的一切阻碍 (sweep away all obstacles on the path ahead)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "地方保护主义和各种隐形市场壁垒，严重阻碍了全国统一大市场的建立与生产要素的自由流动。",
                "pinyin": "Dìfāng bǎohù zhǔyì hé gèzhǒng yǐnxíng shìchǎng bìlěi, yánzhòng zǔ'ài le quánguó tǒngyī dà shìchǎng de jiànlì yǔ shēngchǎn yàosù de zìyóu liúdòng.",
                "en": "Local protectionism and invisible market barriers severely hinder the formation of a unified national market and the free flow of production factors.",
                "es": "El proteccionismo local y las trabas invisibles obstaculizan gravemente la articulación de un mercado nacional y la libre circulación productiva."
            },
            {
                "id": "#2",
                "hanzi": "坚强的探险家从未被大自然险恶的崇山峻岭所吓倒，所有的严寒险阻都化为了砥砺坚强意志的宝贵财富。",
                "pinyin": "Jiānqiáng de tànxiǎnjiā cóngwèi bèi zìrán xiǎn'è de chóngshān-jùnlǐng suǒ xiàdǎo, suǒyǒu de yánhán xiǎnzǔ dōu huàwéi le dǐlì jiānqiáng yìzhì de bǎoguì cáifù.",
                "en": "The intrepid explorer was never daunted by towering perilous peaks; every frost and hindrance became precious assets forging unbreakable resolve.",
                "es": "El intrépido explorador no se arredró ante los abruptos riscos; el frío y los obstáculos se convirtieron en temple para su inquebrantable voluntad."
            }
        ],
        "collocations": [
            {"hanzi": "清除阻碍", "en": "eliminate / remove obstacles"},
            {"hanzi": "阻碍发展", "en": "hinder development"},
            {"hanzi": "造成阻碍", "en": "create an obstacle / hindrance"},
            {"hanzi": "重大阻碍", "en": "major roadblock / obstacle"},
            {"hanzi": "阻碍交通", "en": "obstruct traffic"},
            {"hanzi": "破除阻碍", "en": "break through impediments"}
        ],
        "idioms": [
            {"hanzi": "排除万难", "pinyin": "pái chú wàn nán", "meaning_en": "surmount all ten thousand difficulties; overcome all obstacles"},
            {"hanzi": "披荆斩棘", "pinyin": "pī jīng zhǎn jí", "meaning_en": "hack through brambles and thistles; pioneer through hardships"},
            {"hanzi": "艰难险阻", "pinyin": "jiān nán xiǎn zǔ", "meaning_en": "perilous obstacles and hardships along a journey"},
            {"hanzi": "畅通无阻", "pinyin": "chàng tōng wú zǔ", "meaning_en": "completely unimpeded; open passage without obstacle"}
        ],
        "character_decomposition": [
            {
                "character": "阻",
                "pinyin": "zǔ",
                "meaning_en": "hinder; block; steep mound",
                "meaning_es": "frenar; obstruir; loma empinada",
                "radical": "阝",
                "radical_meaning_en": "mound / hill",
                "meaning_component": "阝 (steep mountain cliff) + 且 (sacrificial stand / altar)",
                "sound_component": "且 (qiě / phonetic association)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Mound/hill radical 阝 beside 且; a sheer mountain terrace obstructing travellers' road, requiring arduous detours.",
                "visual_mnemonic_story_en": "A steep hill cliff (阝) blocking the mountain pass (且), hindering travelers' advance (阻).",
                "visual_mnemonic_story_es": "Un risco escarpado (阝) cerrando el paso del sendero (且), frenando a los caminantes (阻).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "NLBM",
                "traditional": "阻"
            },
            {
                "character": "碍",
                "pinyin": "ài",
                "meaning_en": "hinder; obstruct; impede",
                "meaning_es": "estorbar; entorpecer",
                "radical": "石",
                "radical_meaning_en": "stone / rock",
                "meaning_component": "石 (heavy boulder) + 旦 (rising sun blocked)",
                "sound_component": "得 / 碍 (phonetic)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Stone radical 石 beside 碍; a massive boulder blocking the roadway, impeding travel and sight lines.",
                "visual_mnemonic_story_en": "A giant boulder (石) rolled into the middle of the road at dawn (旦), creating an obstacle (碍).",
                "visual_mnemonic_story_es": "Una enorme roca (石) atravesada al despuntar el día (旦), estorbando el camino (碍).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MRAPM",
                "traditional": "礙"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Steep mountain cliffs (阻) and giant fallen boulders (碍) combine to form a formidable hindrance (阻碍).",
            "composite_memory_hook_es": "Riscos empinados (阻) y peñascos caídos en la senda (碍) se conjugan en un gran obstáculo (阻碍).",
            "cultural_and_cognitive_roots": "Derived from classical geographic hazards (险阻) where cliffs and boulders tested perseverance and road-building ingenuity.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone followed by falling fourth tone: 'zǔ 'ài' (214-51). Dip low on 'zǔ', then drop decisively on 'ài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "阻", "pinyin": "zǔ", "meaning_en": "block; hinder", "distinction_note": "Mound radical 阝 on left with 且"},
                {"character": "租", "pinyin": "zū", "meaning_en": "rent; lease", "distinction_note": "Grain radical 禾 on left of 且"},
                {"character": "碍", "pinyin": "ài", "meaning_en": "hinder; obstacle", "distinction_note": "Stone radical 石 on left"},
                {"character": "得", "pinyin": "dé", "meaning_en": "obtain; get", "distinction_note": "Step radical 彳 on left"}
            ],
            "etymological_cognates": [
                {"character": "障", "pinyin": "zhàng", "gloss_en": "screen; barrier"},
                {"character": "塞", "pinyin": "sè", "gloss_en": "cork; choke; obstruct"},
                {"character": "拦", "pinyin": "lán", "gloss_en": "block; intercept"},
                {"character": "抑", "pinyin": "yì", "gloss_en": "restrain; suppress"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "阻碍 can be either a verb meaning to impede progress or a noun denoting the obstacle itself.",
            "contrasts": [
                {"id": 1, "compared_word": "阻碍 vs. 妨碍", "pinyin": "fáng'ài", "analysis": "妨碍 specifically means causing momentary inconvenience or annoyance to others (妨碍别人休息), while 阻碍 implies major systemic blockages to progress."},
                {"id": 2, "compared_word": "阻碍 vs. 阻止", "pinyin": "zǔzhǐ", "analysis": "阻止 means stopping someone from carrying out an action entirely (阻止他犯错), while 阻碍 slows or impairs progress without necessarily halting it."},
                {"id": 3, "compared_word": "阻碍 vs. 挫折", "pinyin": "cuòzhé", "analysis": "挫折 refers to emotional setbacks or defeats experienced after failure, whereas 阻碍 is the external hurdle."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "改革开放四十多年来的恢弘历程昭示我们，任何社会制度的发展都不可能一帆风顺。唯有敢于直面利益固化的藩篱，敢于破除阻碍创新活力的体制机制障碍，国家才能在风云变幻的国际竞争中勇立潮头、行稳致远。",
                "pinyin": "Gǎigé-kāifàng sìshí duō nián lái de huīhóng lìchéng zhāoshì wǒmen, rènhé shèhuì zhìdù de fāzhǎn dōu bùkěnéng yīfān-fēngshùn. Wéiyǒu gǎnyú zhímiàn lìyì gùhuà de fānlí, gǎnyú pòchú zǔ'ài chuàngxīn huólì de tǐzhì jīzhì zhàng'ài, guójiā cái néng zài fēngyún-biànhuàn de guójì jìngzhēng zhōng yǒnglì-cháotóu, xíngwěn-zhìyuǎn.",
                "en": "Decades of reform reveal that no social development enjoys smooth sailing. Only by confronting entrenchment and dismantling institutional roadblocks hindering innovation can a nation ride cresting waves and advance steadily.",
                "es": "Décadas de reforma demuestran que ningún progreso es coser y cantar. Sólo afrontando los intereses creados y derribando las trabas burocráticas que frenan la innovación, podrá una nación liderar el porvenir con paso firme."
            },
            {
                "id": "#2",
                "hanzi": "在人生的漫长赛道上，真正阻碍我们前进步伐的，往往不是外界环境的严苛艰难，而是我们头脑中固步自封的‘思维筐底’。学会用一把锋利的智慧之锯果断锯掉心理上的筐底与局限，所有的阻碍都将化为通向成功的崭新坦途。",
                "pinyin": "Zài rénshēng de màncháng sàidào shang, zhēnzhèng zǔ'ài wǒmen qiánjìn bùfá de, wǎngwǎng búshì wàijiè huánjìng de yánkē jiānnán, érshì wǒmen tóunǎo zhōng gùbù-zìfēng de 'sīwéi kuāngdǐ'. Xuéhuì yòng yì bǎ fēnglì de zhìhuì zhī jù guǒduàn jù diào xīnlǐ shang de kuāngdǐ yǔ júxiàn, suǒyǒu de zǔ'ài dōu jiāng huàwéi tōngxiàng chénggōng de zhǎnxīn tǎntú.",
                "en": "On life's long track, what truly hinders our stride is seldom external harshness, but the rigid mental bottoms of our own assumptions. Learn to saw away psychological limitations with wisdom's blade, and every obstacle will transform into an open avenue to triumph.",
                "es": "En la carrera de la vida, lo que de verdad frena el paso no son los rigores del entorno, sino los fondos ciegos de nuestra mente. Aprender a serrar con sabiduría esos límites psicológicos transformará cualquier tropiezo en una senda despejada hacia el éxito."
            }
        ]
    }
]

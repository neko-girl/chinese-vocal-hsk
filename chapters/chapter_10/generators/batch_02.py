# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 说服
    {
        "id": "11",
        "hanzi": "说服",
        "pinyin": "shuō fú",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to persuade; to convince; to talk someone round",
            "es": "persuadir; convencer; hacer cambiar de opinión"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to use logical reasoning, evidence, or emotional appeal to win someone over",
                "definition_es": "utilizar razonamientos lógicos, pruebas o persuasión para hacer que alguien acepte un punto de vista",
                "example_phrase": "说服大家接受方案 (persuade everyone to accept the proposal)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "他摆事实、讲道理，终于说服了持反对意见的客户签下合作协议。",
                "pinyin": "Tā bǎi shìshí, jiǎng dàolǐ, zhōngyú shuōfú le chí fǎnduì yìjiàn de kèhù qiānxià hézuò xiéyì.",
                "en": "Presenting facts and reasoning, he finally persuaded the opposing client to sign the agreement.",
                "es": "Exponiendo hechos y razonando, finalmente convenció al cliente reticente para que firmara el acuerdo."
            },
            {
                "id": "#2",
                "hanzi": "这篇科学研究论文数据详实严谨，论证层层递进，具有极强的说服力。",
                "pinyin": "Zhè piān kēxué yánjiū lùnwén shùjù xiángshí yánjǐn, lùnzhèng céngcéng-dìjìn, jùyǒu jí qiáng de shuōfúlì.",
                "en": "This scientific paper is rigorous with data and builds logically step by step, possessing immense persuasive power.",
                "es": "Esta tesis científica aporta datos minuciosos y una argumentación gradual dotada de un enorme poder de convicción."
            }
        ],
        "collocations": [
            {"hanzi": "说服力", "en": "persuasive power; cogency"},
            {"hanzi": "耐心说服", "en": "persuade patiently"},
            {"hanzi": "试图说服", "en": "attempt to convince"},
            {"hanzi": "说服别人", "en": "convince others"},
            {"hanzi": "极具说服力", "en": "highly persuasive"},
            {"hanzi": "说服教育", "en": "educate through persuasion"}
        ],
        "idioms": [
            {"hanzi": "心服口服", "pinyin": "xīn fú kǒu fú", "meaning_en": "convinced in heart and word; completely convinced"},
            {"hanzi": "理屈词穷", "pinyin": "lǐ qū cí qióng", "meaning_en": "run out of arguments when reason is lacking"},
            {"hanzi": "苦口婆心", "pinyin": "kǔ kǒu pó xīn", "meaning_en": "persuade earnestly and kindly with good intentions"},
            {"hanzi": "循循善诱", "pinyin": "xún xún shàn yòu", "meaning_en": "guide systematically and persuasively step by step"}
        ],
        "character_decomposition": [
            {
                "character": "说",
                "pinyin": "shuō",
                "meaning_en": "speak; talk; explain; theory",
                "meaning_es": "hablar; decir; explicar; teoría",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken words/speech)",
                "sound_component": "兑 (duì, articulate/exchange / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 paired with 兑 (open mouth speaking pleasantly), signifying articulating thoughts clearly to others.",
                "visual_mnemonic_story_en": "Words (讠) flow joyfully from an open mouth (兑) in clear speech (说).",
                "visual_mnemonic_story_es": "Palabras (讠) brotan con agrado de una boca abierta (兑) en discurso fluido (说).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "IVCR",
                "traditional": "說"
            },
            {
                "character": "服",
                "pinyin": "fú",
                "meaning_en": "clothes; obey; submit; convince; serve",
                "meaning_es": "ropa; obedecer; someterse; convencerse; servir",
                "radical": "月",
                "radical_meaning_en": "flesh / boat",
                "meaning_component": "月/舟 (boat or person) + 卩 (kneeling person)",
                "sound_component": "又 (yòu, hand / action)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand 又 pressing a kneeling figure 卩 to submit, evolving from physical subjugation to voluntary mental assent and obedience.",
                "visual_mnemonic_story_en": "A hand gently touches a kneeling person until they yield willingly in heart (服).",
                "visual_mnemonic_story_es": "Una mano posada sobre quien se arrodilla hasta que asiente de buen grado (服).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BSSE",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Using reasoned speech (说) until the listener willingly assents in their heart (服) yields persuasion (说服).",
            "composite_memory_hook_es": "Emplear la palabra razonada (说) hasta que el oyente asiente de corazón (服) logra convencerlo (说服).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese diplomacy and rhetoric (战国策); ancient strategists (纵横家) perfected the art of persuasion without resorting to warfare.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by rising tone: 'shuō fú' (55-35). Hold high pitch 55 on 'shuō', then rise smoothly from 3 to 5 on 'fú'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "悦", "pinyin": "yuè", "meaning_en": "pleased; delighted", "distinction_note": "Has heart radical 忄 on left instead of speech 讠 in 说"},
                {"character": "朋", "pinyin": "péng", "meaning_en": "friend", "distinction_note": "Consists of two 月 characters side by side"},
                {"character": "报", "pinyin": "bào", "meaning_en": "report; newspaper", "distinction_note": "Has hand radical 扌 on left instead of 月 in 服"},
                {"character": "蜕", "pinyin": "tuì", "meaning_en": "slough off; molt", "distinction_note": "Has insect radical 虫 on left instead of 讠"}
            ],
            "etymological_cognates": [
                {"character": "劝", "pinyin": "quàn", "gloss_en": "advise; urge with words"},
                {"character": "导", "pinyin": "dǎo", "gloss_en": "guide; lead with hand"},
                {"character": "信", "pinyin": "xìn", "gloss_en": "trust; sincere speech"},
                {"character": "从", "pinyin": "cóng", "gloss_en": "follow; agree with"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "说服 focuses on successfully achieving psychological agreement, whereas 劝告 is merely giving advice regardless of whether it is accepted.",
            "contrasts": [
                {"id": "1", "compared_word": "说服 vs. 劝说", "pinyin": "quànshuō", "analysis": "劝说 highlights the ongoing communicative effort to advise, while 说服 marks the successful conclusion of having won someone over."},
                {"id": "2", "compared_word": "说服 vs. 强迫", "pinyin": "qiǎngpò", "analysis": "强迫 compels compliance through threat or coercion, whereas 说服 relies on rational conviction and voluntary choice."},
                {"id": "3", "compared_word": "说服 vs. 开导", "pinyin": "kāidǎo", "analysis": "开导 focuses on soothing emotional distress or mental gloom, while 说服 focuses on winning agreement in matters of opinion."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在商业谈判中，单凭华丽的言辞很难真正说服精明的投资人。唯有拿出详实客观的市场调研数据、清晰可行的盈利模式以及强大的执行团队，才能彻底打消顾虑，赢得真诚认可与资金支持。",
                "pinyin": "Zài shāngyè tánpàn zhōng, dānpíng huálì de yáncí hěn nán zhēnzhèng shuōfú jīngmíng de tóuzīrén. Wéiyǒu náchū xiángshí kèguān de shìchǎng diàoyán shùjù, qīngxī kěxíng de yínglì móshì yǐjí qiángdà de zhíxíng tuánduì, cáinéng chèdǐ dǎxiāo gùlǜ, yíngdé zhēnchéng rènkě yǔ zījīn zhīchí.",
                "en": "In business negotiations, flowery rhetoric alone rarely convinces shrewd investors. Only objective market data, clear profit models, and strong execution can dispel doubts and secure authentic backing.",
                "es": "En negociaciones comerciales, la retórica hueca apenas convence a inversores sagaces. Solo datos objetivos de mercado, modelos viables y equipos solventes disipan dudas y conquistan respaldo financiero."
            },
            {
                "id": "#2",
                "hanzi": "面对固执己见的朋友，粗暴指责往往适得其反，激起防御心理。真正高超的说服艺术，在于设身处地倾听对方关切，巧妙引导其换位思考，让对方在自主权衡中得出合乎逻辑的明智结论。",
                "pinyin": "Miànduì gùzhí jǐjiàn de péngyou, cūbào zhǐzé wǎngwǎng shìdéqífǎn, jīqǐ fángyù xīnlǐ. Zhēnzhèng gāochāo de shuōfú yìshù, zàiyú shèshēnchǔdì qīngtīng duìfāng guānqiè, qiǎomiào yǐndǎo qí huànwèi sīkǎo, ràng duìfāng zài zìzhǔ quánhéng zhōng déchū héhū luóji de míngzhì jiélùn.",
                "en": "Confronting stubborn friends with blunt reproach often backfires into defensiveness. True persuasive skill lies in empathetic listening and guiding them to weigh perspectives autonomously toward wise conclusions.",
                "es": "Ante amigos testarudos, la censura tajante desata actitudes defensivas. La verdadera maestría persuasiva consiste en escuchar con empatía y guiar con tacto para que sopesen opciones y alcancen conclusiones sensatas."
            }
        ]
    },

    # 12 摄影师
    {
        "id": "12",
        "hanzi": "摄影师",
        "pinyin": "shè yǐng shī",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "photographer; cinematographer; cameraman",
            "es": "fotógrafo; camarógrafo; operador de cámara"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a professional who operates cameras to take still photographs or film motion pictures",
                "definition_es": "profesional que opera cámaras para tomar fotografías fijas o rodar películas",
                "example_phrase": "专业摄影师 (professional photographer)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "野生动物摄影师在茫茫雪原耐心地潜伏了三天，终于拍摄到雪豹奔跑的珍贵瞬间。",
                "pinyin": "Yěshēng dòngwù shèyǐngshī zài mángmáng xuěyuán nàixīn de qiánfú le sān tiān, zhōngyú pāishè dào xuěbào bēnpǎo de zhēnguì shùnjiān.",
                "en": "The wildlife photographer staked out the snowy plateau for three days, finally filming the precious moment of a snow leopard sprinting.",
                "es": "El fotógrafo de fauna silvestre acechó tres días en la estepa nevada, captando al fin el instante irrepetible de un leopardo de las nieves corriendo."
            },
            {
                "id": "#2",
                "hanzi": "这位年轻的摄影师凭借独特的光影构图，斩获了国际摄影大赛金奖。",
                "pinyin": "Zhè wèi niánqīng de shèyǐngshī píngjiè dútè de guāngyǐng gòutú, zhǎnhuò le guójì shèyǐng dàsài jīnjiǎng.",
                "en": "With his unique lighting and composition, this young photographer won the gold prize at the international photography competition.",
                "es": "Este joven fotógrafo cosechó el premio de oro en el certamen internacional gracias a su original composición de luces y sombras."
            }
        ],
        "collocations": [
            {"hanzi": "专业摄影师", "en": "professional photographer"},
            {"hanzi": "野生动物摄影师", "en": "wildlife photographer"},
            {"hanzi": "首席摄影师", "en": "chief cinematographer/photographer"},
            {"hanzi": "特约摄影师", "en": "contributing photographer"},
            {"hanzi": "婚礼摄影师", "en": "wedding photographer"},
            {"hanzi": "签约摄影师", "en": "contracted photographer"}
        ],
        "idioms": [
            {"hanzi": "惟妙惟肖", "pinyin": "wéi miào wéi xiào", "meaning_en": "remarkably lifelike and vivid"},
            {"hanzi": "跃然纸上", "pinyin": "yuè rán zhǐ shàng", "meaning_en": "leap off the page; vividly presented"},
            {"hanzi": "捕捉瞬间", "pinyin": "bǔ zhuō shùn jiān", "meaning_en": "capture fleeting, critical moments"},
            {"hanzi": "匠心独运", "pinyin": "jiàng xīn dú yùn", "meaning_en": "exquisite artistic craftsmanship and originality"}
        ],
        "character_decomposition": [
            {
                "character": "摄",
                "pinyin": "shè",
                "meaning_en": "absorb; capture; take photo; act for",
                "meaning_es": "absorber; captar; fotografiar; asumir",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand action)",
                "sound_component": "聑 (dié/shè, multiple ears / phonetic)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with three ears 聑; originally gathering sounds and sights by hand, extended to photo-recording.",
                "visual_mnemonic_story_en": "A hand (扌) captures sights and sounds from listening ears (聑) through a camera lens (摄).",
                "visual_mnemonic_story_es": "Una mano (扌) recoge imágenes y susurros de oídos atentos (聑) a través de una lente (摄).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "QSJJ",
                "traditional": "攝"
            },
            {
                "character": "影",
                "pinyin": "yǐng",
                "meaning_en": "shadow; image; film; reflection",
                "meaning_es": "sombra; imagen; película; reflejo",
                "radical": "彡",
                "radical_meaning_en": "bristle / pattern",
                "meaning_component": "彡 (rays/patterns of light and shade)",
                "sound_component": "景 (jǐng, scenery/sunshine / phonetic)",
                "stroke_count": 15,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Sunlight over a pavilion 景 casting decorative shadow streaks 彡; represents shadow, image, or movie.",
                "visual_mnemonic_story_en": "Sun shining on bright scenery (景) casts delicate shadow rays (彡) creating photographic imagery (影).",
                "visual_mnemonic_story_es": "El sol sobre el paisaje (景) proyecta haces de sombra (彡) engendrando la imagen fotográfica (影).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "AFHHH",
                "traditional": ""
            },
            {
                "character": "师",
                "pinyin": "shī",
                "meaning_en": "teacher; master; specialist; division",
                "meaning_es": "maestro; especialista; profesor; división",
                "radical": "巾",
                "radical_meaning_en": "cloth / banner",
                "meaning_component": "巾 (military camp banner)",
                "sound_component": "𠂤 (duī, mound / multitude)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A commander's banner 巾 leading an assembled host 𠂤; evolved to denote certified masters and professionals.",
                "visual_mnemonic_story_en": "Under a guild banner (巾), a qualified master (师) leads and teaches with expertise.",
                "visual_mnemonic_story_es": "Bajo el estandarte gremial (巾), un maestro profesional (师) guía con pericia consumada.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "LMLB",
                "traditional": "師"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "One who captures (摄) light and shadows (影) with masterly skill (师) is a photographer (摄影师).",
            "composite_memory_hook_es": "Quien captura (摄) sombras y luces (影) con destreza de maestro (师) es un fotógrafo (摄影师).",
            "cultural_and_cognitive_roots": "Compound created in late Qing to translate optical photography; 摄影 (capturing shadows) reflects the poetic Chinese perception of camera optics.",
            "tone_sandhi_and_pitch_modulation": "Falling tone, dipping tone, level high tone: 'shè yǐng shī' (51-214-55). Strike down on 'shè', swoop low on 'yǐng', float high on 'shī'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "慑", "pinyin": "shè", "meaning_en": "fear; intimidate", "distinction_note": "Has heart radical 忄 on left instead of hand 扌 in 摄"},
                {"character": "帅", "pinyin": "shuài", "meaning_en": "handsome; commander", "distinction_note": "Has 丿 on left instead of 刂 in 师"},
                {"character": "聂", "pinyin": "niè", "meaning_en": "whisper; surname", "distinction_note": "Has three ears 耳 without hand radical 扌"},
                {"character": "彭", "pinyin": "péng", "meaning_en": "drum sound; surname", "distinction_note": "Has 壴 on left instead of 景 before 彡"}
            ],
            "etymological_cognates": [
                {"character": "照", "pinyin": "zhào", "gloss_en": "illuminate; take snapshot"},
                {"character": "相", "pinyin": "xiàng", "gloss_en": "appearance; portrait photograph"},
                {"character": "镜", "pinyin": "jìng", "gloss_en": "mirror; optical lens"},
                {"character": "景", "pinyin": "jǐng", "gloss_en": "scenery; optical vista"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "摄影师 highlights artistic mastery of lighting, framing, and lenses, distinct from moving camera operators or directors.",
            "contrasts": [
                {"id": "1", "compared_word": "摄影师 vs. 摄像师", "pinyin": "shèxiàngshī", "analysis": "摄影师 commonly focuses on still photography or cinema optics, while 摄像师 primarily operates video cameras for television and live broadcasts."},
                {"id": "2", "compared_word": "摄影师 vs. 导演", "pinyin": "dǎoyǎn", "analysis": "导演 directs overall dramatic narrative and acting, while 摄影师 realizes visual compositions on camera."},
                {"id": "3", "compared_word": "摄影师 vs. 照相师傅", "pinyin": "zhàoxiàng shīfu", "analysis": "照相师傅 is a traditional colloquial term for ID studio technicians, lacking the creative artistic prestige of 摄影师."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "一名优秀的纪实摄影师，不仅需要精湛的技术，更需要敏锐的人文洞察力。他们穿梭在喧嚣街巷与偏僻乡村，用镜头定格普通人的喜怒哀乐，记录时代变迁中最动人的脉搏与记忆。",
                "pinyin": "Yì míng yōuxiù de jìshí shèyǐngshī, bùjǐn xūyào jīngzhàn de jìshù, gèng xūyào mǐnruì de rénwén dòngchálì. Tāmen chuānsuō zài xuānxiāo jiēxiàng yǔ piānpì xiāngcūn, yòng jìngtóu dìnggé pǔtōngrén de xǐnù'ǎilè, jìlù shídài biànqiān zhōng zuì dòngrén de màibó yǔ jìyì.",
                "en": "An outstanding documentary photographer requires superb technique and humanistic insight. Moving between bustling alleys and quiet hamlets, their lens captures human emotions, recording the poignant pulse of history.",
                "es": "Un fotógrafo documental sobresaliente precisa pericia técnica y hondura humanística. Recorriendo callejones bulliciosos y aldeas remotas, su lente inmortaliza emociones cotidianas retratando el palpitar de una época."
            },
            {
                "id": "#2",
                "hanzi": "电影摄影师被称为“用光作画的诗人”。在剧组拍摄现场，摄影师与导演紧密配合，根据剧情发展精准调配光影明暗、机位运动与色调冷暖，赋予原本平淡的场景深邃的戏剧张力与视觉美感。",
                "pinyin": "Diànyǐng shèyǐngshī bèi chēngwéi 'yòng guāng zuòhuà de shīrén'. Zài jùzǔ pāishè xiànchǎng, shèyǐngshī yǔ dǎoyǎn jǐnmì pèihé, gēnjù jùqíng fāzhǎn jīngzhǔn tiáopèi guāngyǐng míng'àn, jīwèi yùndòng yǔ sèdiào lěngnuǎn, fùyǔ yuánběn píngdàn de chǎngjǐng shēnsù de xìjù zhānglì yǔ shìjué měigǎn.",
                "en": "Cinematographers are called poets painting with light. On set, they collaborate with directors, calibrating shadows, camera movement, and color warmth to infuse ordinary scenes with dramatic tension and beauty.",
                "es": "A los directores de fotografía se les llama poetas de la luz. En el rodaje colaboran con el director modulando sombras, encuadres y temperatura de color para dotar a las escenas de tensión dramática y belleza visual."
            }
        ]
    },

    # 13 毕竟
    {
        "id": "13",
        "hanzi": "毕竟",
        "pinyin": "bì jìng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "after all; when all is said and done; in the final analysis",
            "es": "después de todo; al fin y al cabo; en definitiva"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "used to emphasize a fundamental, inescapable truth or decisive explanatory factor",
                "definition_es": "empleado para recalcar una verdad ineludible, factor decisivo o realidad concluyente",
                "example_phrase": "毕竟是小孩子 (after all, he is just a child)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "他刚参加工作不到两个月，缺乏实战经验，毕竟还是个新手，我们应该多加包容。",
                "pinyin": "Tā gāng cānjiā gōngzuò bú dào liǎng ge yuè, quēfá shízhàn jīngyàn, bìjìng háishì ge xīnshǒu, wǒmen yīnggāi duōjiā bāoróng.",
                "en": "Having worked for under two months, he lacks field experience; after all, he is a beginner, so we should be forgiving.",
                "es": "Lleva menos de dos meses en el puesto y carece de tablas; al fin y al cabo es principiante, por lo que conviene ser tolerantes."
            },
            {
                "id": "#2",
                "hanzi": "理论设想无论多么完美，毕竟需要放到实践中去检验其真实可行性。",
                "pinyin": "Lǐlùn shèxiǎng wúlùn duōme wánměi, bìjìng xūyào fàng dào shíjiàn zhōng qù jiǎnyàn qí zhēnshí kěxíngxìng.",
                "en": "No matter how perfect theoretical assumptions are, in the end they must be verified in practical application.",
                "es": "Por impecable que parezca el planteamiento teórico, después de todo es preciso contrastarlo en la práctica real."
            }
        ],
        "collocations": [
            {"hanzi": "毕竟还是", "en": "after all still is"},
            {"hanzi": "毕竟不同", "en": "after all different"},
            {"hanzi": "毕竟有限", "en": "ultimately limited"},
            {"hanzi": "毕竟年轻", "en": "young after all"},
            {"hanzi": "这毕竟说明", "en": "this after all proves"},
            {"hanzi": "毕竟是事实", "en": "after all a reality"}
        ],
        "idioms": [
            {"hanzi": "归根到底", "pinyin": "guī gēn dào dǐ", "meaning_en": "fundamentally speaking; in the final analysis"},
            {"hanzi": "水落石出", "pinyin": "shuǐ luò shí chū", "meaning_en": "the water recedes and rocks appear; truth comes to light"},
            {"hanzi": "终成正果", "pinyin": "zhōng chéng zhèng guǒ", "meaning_en": "reach fruition after prolonged striving"},
            {"hanzi": "不可否认", "pinyin": "bù kě fǒu rèn", "meaning_en": "undeniable; cannot be contested"}
        ],
        "character_decomposition": [
            {
                "character": "毕",
                "pinyin": "bì",
                "meaning_en": "finish; complete; entirely; graduate",
                "meaning_es": "terminar; concluir; graduarse; totalmente",
                "radical": "十",
                "radical_meaning_en": "ten",
                "meaning_component": "比 (close/paired) + 十 (full completeness)",
                "sound_component": "毕 (bì)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Originally a hunting net on a handle for netting small birds; extended to total capture and final completion (毕业).",
                "visual_mnemonic_story_en": "A net scoops up every last target, bringing total completion (毕) to the hunt.",
                "visual_mnemonic_story_es": "Una red atrapa la última pieza, consumando la faena con pleno remate (毕).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "PPU",
                "traditional": "畢"
            },
            {
                "character": "竟",
                "pinyin": "jìng",
                "meaning_en": "unexpectedly; finally; finish; go so far as to",
                "meaning_es": "al final; inesperadamente; concluir; llegar al extremo de",
                "radical": "立",
                "radical_meaning_en": "stand",
                "meaning_component": "音 (music piece playing through)",
                "sound_component": "儿 (human reaching the limit)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A musical performance 音 reaching its final chord or closing measure; signifying termination, limit, or ultimately.",
                "visual_mnemonic_story_en": "A piece of music (音) plays its very last note, reaching its ultimate end (竟).",
                "visual_mnemonic_story_es": "Una melodía (音) desgrana su última nota sonora hasta concluir por fin (竟).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YTQU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Reaching the end of the net (毕) and the final musical note (竟), one realizes the bottom line truth after all (毕竟).",
            "composite_memory_hook_es": "Llegando al remate de la red (毕) y al acorde final (竟), se comprende la verdad concluyente al fin y al cabo (毕竟).",
            "cultural_and_cognitive_roots": "Classical compound pairing two words of terminus (毕 finish + 竟 conclude) to yield a philosophical realization of ultimate realities.",
            "tone_sandhi_and_pitch_modulation": "Double falling fourth tones: 'bì jìng' (51-51). Descend sharply on 'bì', then strike down again decisively on 'jìng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "华", "pinyin": "huá", "meaning_en": "splendid; flower; China", "distinction_note": "Has 化 atop 十 instead of 比 in 毕"},
                {"character": "竞", "pinyin": "jìng", "meaning_en": "compete; contest", "distinction_note": "Has two 立 components and two 儿 components (竞争)"},
                {"character": "境", "pinyin": "jìng", "meaning_en": "border; territory; state", "distinction_note": "Has earth radical 土 on left of 竟"},
                {"character": "算", "pinyin": "suàn", "meaning_en": "calculate; reckon", "distinction_note": "Has bamboo radical 竹 on top instead of 比"}
            ],
            "etymological_cognates": [
                {"character": "终", "pinyin": "zhōng", "gloss_en": "end; terminal knot"},
                {"character": "底", "pinyin": "dǐ", "gloss_en": "bottom; underlying foundation"},
                {"character": "竟", "pinyin": "jìng", "gloss_en": "finish musical composition"},
                {"character": "极", "pinyin": "jí", "gloss_en": "utmost; extremity"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "毕竟 underlines an unavoidable root reason or fundamental factor explaining an outcome.",
            "contrasts": [
                {"id": "1", "compared_word": "毕竟 vs. 究竟", "pinyin": "jiūjìng", "analysis": "究竟 is used in questions to interrogate reality deeply ('你究竟去不去？'), while 毕竟 provides explanatory reasons in declarative statements."},
                {"id": "2", "compared_word": "毕竟 vs. 到底", "pinyin": "dàodǐ", "analysis": "到底 can express persistence over time ('坚持到底'), whereas 毕竟 strictly serves as an explanatory causal connector."},
                {"id": "3", "compared_word": "毕竟 vs. 终究", "pinyin": "zhōngjiū", "analysis": "终究 emphasizes inevitable eventual fate over long timeframes, while 毕竟 explains why something is justifiable."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "虽然人工智能翻译软件日新月异，但在捕捉文学作品细腻情感与文化潜台词方面，算法毕竟难以彻底替代人类译者的艺术直觉。文字深处的温度与灵魂，终究源于真实的心灵共鸣。",
                "pinyin": "Suīrán réngōng zhìnéng fānyì ruǎnjiàn rìxīnyuèyì, dàn zài bǔzhuō wénxué zuòpǐn xìnì qínggǎn yǔ wénhuà qiántáicí fāngmiàn, suànfǎ bìjìng nán yǐ chèdǐ tìdài rénlèi yìzhě de yìshù zhíjué. Wénzì shēnchù de wēndù yǔ línghún, zhōngjiū yuányú zhēnshí de xīnlíng gòngmíng.",
                "en": "Though AI translation evolves quickly, algorithms after all can hardly replace a human translator's artistic intuition for literary nuances. Verbal warmth stems from authentic human resonance.",
                "es": "Aunque la traducción automática avanza rauda, después de todo los algoritmos no sustituyen la intuición estética humana ante matices líricos. El calor del texto mana de la empatía vivencial."
            },
            {
                "id": "#2",
                "hanzi": "年轻人初入职场难免眼高手低、遭遇挫折，但前辈们应当给予足够的耐心与宽容。他们毕竟缺乏阅历积累，只要肯虚心钻研、勇于担当，经过数年摸爬滚打，定能成为独当一面的骨干力量。",
                "pinyin": "Niánqīngrén chūrù zhíchǎng nánmiǎn yǎngāoshǒudī, zāoyù cuòzhé, dàn qiánbèimen yīngdāng jǐyǔ zúgòu de nàixīn yǔ kuānróng. Tāmen bìjìng quēfá yuèlì jīlěi, zhǐyào kěn xūxīn zuānyán, yǒngyú dāndāng, jīngguò shùnián mōpágǔndǎ, dìng néng chéngwéi dúdāng-yímiàn de gǔgàn lìliàng.",
                "en": "Novices starting careers inevitably stumble, but seniors should offer patience. After all, they lack accumulated experience; with humility and dedication, they will grow into pillars of strength.",
                "es": "Los novatos tropiezan inevitablemente al debutar en el trabajo, pero los veteranos deben mostrar paciencia. Carecen de bagaje después de todo; con humildad y coraje madurarán hasta ser puntales decisivos."
            }
        ]
    },

    # 14 操场
    {
        "id": "14",
        "hanzi": "操场",
        "pinyin": "cāo chǎng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "playground; sports field; athletic ground",
            "es": "patio de recreo; pista de atletismo; campo de deportes"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an outdoor open ground or track in schools or institutions for physical exercise and sports",
                "definition_es": "terreno exterior o pista deportiva escolar o institucional para ejercicios físicos y deportes",
                "example_phrase": "在操场跑步 (run on the sports field)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "放学后，操场上聚集了许多热爱运动的学生，打篮球和踢足球的声音此起彼伏。",
                "pinyin": "Fàngxué hòu, cāochǎng shàng jùjí le xǔduō rè'ài yùndòng de xuésheng, dǎ lánqiú hé tī zúqiú de shēngyīn cǐqǐ-bǐfú.",
                "en": "After school, sports-loving students gathered on the playground, basketball and football shouts rising continuously.",
                "es": "Al concluir las clases, los alumnos se congregan en el patio escolar, sucediéndose los ecos del baloncesto y el fútbol."
            },
            {
                "id": "#2",
                "hanzi": "学校为了保障学生安全，对操场的塑胶跑道和草坪进行了全面翻新。",
                "pinyin": "Xuéxiào wèile bǎozhàng xuésheng ānquán, duì cāochǎng de sùjiāo pǎodào hé cǎopíng jìnxíng le quánmiàn fānxīn.",
                "en": "To guarantee student safety, the school carried out a comprehensive renovation of the sports field's track and lawn.",
                "es": "Para garantizar la seguridad del alumnado, la escuela renovó íntegramente la pista sintética y el césped del campo deportivo."
            }
        ],
        "collocations": [
            {"hanzi": "学校操场", "en": "school sports ground"},
            {"hanzi": "塑胶操场", "en": "synthetic turf/track playground"},
            {"hanzi": "环形操场", "en": "circular athletic track"},
            {"hanzi": "跑操场", "en": "run laps on the playground"},
            {"hanzi": "操场集合", "en": "assemble on the sports ground"},
            {"hanzi": "操场跑道", "en": "playground running track"}
        ],
        "idioms": [
            {"hanzi": "生龙活虎", "pinyin": "shēng lóng huó hǔ", "meaning_en": "full of vigor and vitality; spirited as dragons and tigers"},
            {"hanzi": "欢声笑语", "pinyin": "huān shēng xiào yǔ", "meaning_en": "bursts of happy laughter and cheerful voices"},
            {"hanzi": "你追我赶", "pinyin": "nǐ zhuī wǒ gǎn", "meaning_en": "compete keenly with each other neck and neck"},
            {"hanzi": "龙腾虎跃", "pinyin": "lóng téng hǔ yuè", "meaning_en": "bounding with dynamic vitality and boundless energy"}
        ],
        "character_decomposition": [
            {
                "character": "操",
                "pinyin": "cāo",
                "meaning_en": "grasp; hold; drill; exercise",
                "meaning_es": "agarrar; sostener; ejercitarse; maniobrar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand action)",
                "sound_component": "喿 (zào, chirping birds on trees / phonetic)",
                "stroke_count": 16,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with 喿; holding tools firmly and directing physical drilling (体操).",
                "visual_mnemonic_story_en": "Hands (扌) move vigorously in unison during morning physical exercises (操).",
                "visual_mnemonic_story_es": "Las manos (扌) se mueven enérgica y coordinadamente en la tabla gimnástica (操).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QRRD",
                "traditional": ""
            },
            {
                "character": "场",
                "pinyin": "chǎng",
                "meaning_en": "open ground; threshing floor; scene",
                "meaning_es": "campo; terreno llano; escena; explanada",
                "radical": "土",
                "radical_meaning_en": "earth / ground",
                "meaning_component": "土 (soil/ground)",
                "sound_component": "𠃓 (yáng, spreading light / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Earth radical 土 plus spreading sunlight; an open flat ground cleared for threshing or gatherings.",
                "visual_mnemonic_story_en": "Level ground (土) basking under open sunlight makes an expansive field (场).",
                "visual_mnemonic_story_es": "Suelo llano (土) expuesto al sol abierto que conforma una ancha explanada (场).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "GNSH",
                "traditional": "場"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An open level ground (场) where students drill and exercise (操) is the school playground (操场).",
            "composite_memory_hook_es": "Una ancha explanada (场) donde se ejecutan ejercicios y gimnasia (操) es el patio escolar (操场).",
            "cultural_and_cognitive_roots": "Evolved from military drill grounds (操练场地) into universal modern school physical education grounds since the late Qing educational reforms.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by dipping tone: 'cāo chǎng' (55-214). Maintain steady pitch 55 on 'cāo', then dip and rise on 'chǎng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "燥", "pinyin": "zào", "meaning_en": "dry; parched", "distinction_note": "Has fire radical 火 on left instead of hand 扌 in 操"},
                {"character": "澡", "pinyin": "zǎo", "meaning_en": "bathe; wash", "distinction_note": "Has water radical 氵 on left instead of 扌"},
                {"character": "扬", "pinyin": "yáng", "meaning_en": "raise; hoist", "distinction_note": "Has hand radical 扌 on left instead of earth 土 in 场"},
                {"character": "汤", "pinyin": "tāng", "meaning_en": "soup; broth", "distinction_note": "Has water radical 氵 on left of 𠃓"}
            ],
            "etymological_cognates": [
                {"character": "坪", "pinyin": "píng", "gloss_en": "level ground; lawn"},
                {"character": "坛", "pinyin": "tán", "gloss_en": "altar; raised earthen platform"},
                {"character": "苑", "pinyin": "yuàn", "gloss_en": "garden grounds; park"},
                {"character": "园", "pinyin": "yuán", "gloss_en": "enclosed garden field"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "操场 emphasizes school or military outdoor grounds equipped with running tracks for calisthenics and games.",
            "contrasts": [
                {"id": "1", "compared_word": "操场 vs. 体育场", "pinyin": "tǐyùchǎng", "analysis": "体育场 refers to a grand public stadium with spectator stands, while 操场 is the everyday outdoor yard of a school."},
                {"id": "2", "compared_word": "操场 vs. 广场", "pinyin": "guǎngchǎng", "analysis": "广场 is an urban paved public square for civic assemblies and leisure, not student physical education."},
                {"id": "3", "compared_word": "操场 vs. 球场", "pinyin": "qiúchǎng", "analysis": "球场 specifically designates a specialized ball court (basketball court, tennis court), while 操场 covers the general athletic ground."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "金色的夕阳洒在校园的操场上，将奔跑少年的影子拉得长长的。微风拂过红绿相间的跑道，带来泥土与青草的气息。这里不仅见证了青春的拼搏与汗水，也承载着无数纯真难忘的友谊。",
                "pinyin": "Jīnsè de xīyáng sǎ zài xiàoyuán de cāochǎng shàng, jiāng bēnpǎo shàonián de yǐngzi lā de chángcháng de. Wēifēng fúguò hónglǜ xiāngjiàn de pǎodào, dàilái nítǔ yǔ qīngcǎo de qìxī. Zhèlǐ bùjǐn jiànzhèng le qīngchūn de pīnbó yǔ hànshuǐ, yě chéngzài zhe wúshù chúnzhēn nánwàng de yǒuyì.",
                "en": "Golden sunset bathes the campus sports field, elongating runners' shadows. Breezes bring scents of turf and earth, witnessing youth's sweat and carrying pure friendships.",
                "es": "La puesta de sol baña el patio escolar alargando las sombras juveniles. La brisa trae aroma a tierra y hierba, atestiguando el tesón y cobijando amistades entrañables."
            },
            {
                "id": "#2",
                "hanzi": "每逢清晨集合铃声响起，全校师生便整齐划一地汇聚在操场中央做广播体操。口令声与进行曲交织回荡在蓝天下，整齐的队列和蓬勃的朝气，让整座宁静的校园瞬间焕发出无限生机与活力。",
                "pinyin": "Měiféng qīngchén jíhé língshēng xiǎngqǐ, quánxiào shīshēng biàn zhěngqí huàyī de huìjù zài cāochǎng zhōngyāng zuò guǎngbō tǐcāo. Kǒulìngshēng yǔ jìnxíngqǔ jiāozhī huídàng zài lántiān xià, zhěngqí de duìliè hé péngbó de zhāoqì, ràng zhěng zuò níngjìng de xiàoyuán shùnjiān huànfā chū wúxiàn shēngjī yǔ huólì.",
                "en": "When the morning bell rings, students assemble neatly across the sports field for calisthenics. Commands and music echo under blue skies, instantly filling the quiet campus with vitality.",
                "es": "Al sonar la campana matutina, el alumnado se forma en el patio para la gimnasia rítmica. Voces de mando y marchas resuenan bajo el cielo azul infundiendo dinamismo a todo el recinto."
            }
        ]
    },

    # 15 洞
    {
        "id": "15",
        "hanzi": "洞",
        "pinyin": "dòng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "hole; cave; cavity; aperture",
            "es": "agujero; hoyo; cueva; cavidad; orificio"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a hollow place, opening, perforation, or natural cavern in a solid body or the earth",
                "definition_es": "espacio hueco, abertura, perforación o caverna natural en la roca o tierra",
                "example_phrase": "山洞 / 衣服破了个洞 (mountain cave / hole in clothes)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "调皮的小老鼠一看到黑猫走过来，立刻敏捷地钻进了墙角深处的石洞里。",
                "pinyin": "Tiáopí de xiǎolǎoshǔ yí kàndào hēimāo zǒuguòlai, lìkè mǐnjié de zuānjìn le qiángjiǎo shēnchù de shídòng lǐ.",
                "en": "Seeing the black cat approach, the mischievous mouse darted into a stone hole deep in the wall corner.",
                "es": "Al ver aproximarse al gato negro, el ratoncillo se escabulló veloz hacia el agujero de piedra en el rincón."
            },
            {
                "id": "#2",
                "hanzi": "老工人顺着木板仔细检查，发现这块木料中间竟然被虫子蛀出了好几个小洞。",
                "pinyin": "Lǎo gōngrén shùnzhe mùbǎn zǐxì jiǎnchá, fāxiàn zhè kuài mùliào zhōngjiān jìngrán bèi chóngzi zhùchū le hǎojǐ ge xiǎodòng.",
                "en": "Inspecting the plank, the veteran worker found insects had bored several small holes right through the wood.",
                "es": "Inspeccionando el tablón, el veterano operario descubrió que los insectos habían horadado varios agujeros diminutos en la madera."
            }
        ],
        "collocations": [
            {"hanzi": "山洞", "en": "mountain cave"},
            {"hanzi": "漏洞", "en": "loophole; security flaw"},
            {"hanzi": "挖洞", "en": "dig a hole"},
            {"hanzi": "打洞", "en": "drill / bore holes"},
            {"hanzi": "地洞", "en": "underground burrow"},
            {"hanzi": "黑洞", "en": "astronomical black hole"}
        ],
        "idioms": [
            {"hanzi": "别有洞天", "pinyin": "bié yǒu dòng tiān", "meaning_en": "a wonderful hidden new world or paradise"},
            {"hanzi": "洞察秋毫", "pinyin": "dòng chá qiū háo", "meaning_en": "perceive the minutest detail with razor-sharp insight"},
            {"hanzi": "无底深洞", "pinyin": "wú dǐ shēn dòng", "meaning_en": "bottomless pit; unfillable chasm"},
            {"hanzi": "钻洞而逃", "pinyin": "zuān dòng ér táo", "meaning_en": "crawl through a hole to escape"}
        ],
        "character_decomposition": [
            {
                "character": "洞",
                "pinyin": "dòng",
                "meaning_en": "hole; cave; cavity; penetrate through",
                "meaning_es": "agujero; cueva; cavidad; penetrar a fondo",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water flowing straight through)",
                "sound_component": "同 (tóng, tunnel / concurrence / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water radical 氵 paired with 同 (together/through); rushing subterranean streams boring straight through rocks to create caves.",
                "visual_mnemonic_story_en": "Water (氵) carves a smooth tunnel (同) straight through rock, creating a cavernous hole (洞).",
                "visual_mnemonic_story_es": "El agua (氵) horada un túnel continuo (同) en la roca viva, modelando una cueva (洞).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EBMR",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Water (氵) flowing through rock forms a deep opening or cave (洞).",
            "composite_memory_hook_es": "El agua (氵) que perfora la peña abre un hoyo o profunda cueva (洞).",
            "cultural_and_cognitive_roots": "Taoist cosmology reveres sacred grottos (洞天福地) as secluded gateways to immortality and primordial nature.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone: 'dòng' (51). Drop sharply like a heavy rock plummeting into a deep underground cavern."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "铜", "pinyin": "tóng", "meaning_en": "copper; bronze", "distinction_note": "Has metal radical 钅 on left instead of water 氵 in 洞"},
                {"character": "桐", "pinyin": "tóng", "meaning_en": "paulownia tree", "distinction_note": "Has tree radical 木 on left instead of 氵"},
                {"character": "筒", "pinyin": "tǒng", "meaning_en": "cylinder; tube", "distinction_note": "Has bamboo radical 竹 on top instead of 氵"},
                {"character": "侗", "pinyin": "dòng", "meaning_en": "Dong ethnic group; naive", "distinction_note": "Has person radical 亻 on left"}
            ],
            "etymological_cognates": [
                {"character": "穴", "pinyin": "xué", "gloss_en": "burrow; cave dwelling"},
                {"character": "坑", "pinyin": "kēng", "gloss_en": "earthen pit; depression"},
                {"character": "孔", "pinyin": "kǒng", "gloss_en": "aperture; small pore"},
                {"character": "窟", "pinyin": "kū", "gloss_en": "cavernous grotto; den"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "洞 denotes a hollow opening, cavity, or passage, ranging from punctures in cloth to karst caves.",
            "contrasts": [
                {"id": "1", "compared_word": "洞 vs. 穴", "pinyin": "xué", "analysis": "穴 is used in scientific or anatomical contexts (acupuncture point 穴位, animal burrow 巢穴), while 洞 is the general term for holes and caves."},
                {"id": "2", "compared_word": "洞 vs. 坑", "pinyin": "kēng", "analysis": "坑 refers to a shallow depression or pit dug in the earth, whereas 洞 refers to a deep cavern or penetrating aperture."},
                {"id": "3", "compared_word": "洞 vs. 窟", "pinyin": "kū", "analysis": "窟 denotes grottos with Buddhist carvings (石窟) or illicit dens, while 洞 is neutral and natural."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在群山环抱的幽深峡谷中，隐藏着一个巨大的喀斯特溶洞。岩壁上的石笋历经数万年水滴的洗礼，千姿百态。洞内溪流淙淙、清凉宜人，微弱的手电光束照亮了沉睡千万年的地下奇观。",
                "pinyin": "Zài qúnshān huánbào de yōushēn xiágǔ zhōng, yǐncáng zhe yí ge jùdà de kāsītè róngdòng. Yánbì shàng de shísǔn lìjīng shùwàn nián shuǐdī de xǐlǐ, qiānzībǎitài. Dòngnèi xīliú cóngcóng, qīngliáng yírén, wēiruò de shǒudiàn guāngshù zhàoliàng le chénsù qiānwàn nián de dìxià qíguān.",
                "en": "In a deep canyon surrounded by mountains lies a colossal karst cave. Stalagmites washed over millennia present diverse forms. Streams keep the cavern cool as flashlights illuminate ancient wonders.",
                "es": "En un hondo cañón entre montañas yace oculta una inmensa gruta cárstica. Estalagmitas milenarias adoptan caprichosas formas. El rumor del arroyo interior refresca el ambiente mientras las linternas alumbran maravillas subterráneas."
            },
            {
                "id": "#2",
                "hanzi": "信息安全工程师在系统代码中发现了一个隐秘的逻辑漏洞。这个看似微小的系统破洞，极易被黑客利用进行恶意渗透与窃取核心数据库。团队通宵达旦地紧急编写补丁程序，彻底封堵了安全隐患。",
                "pinyin": "Xìnxī ānquán gōngchéngshī zài xìtǒng dàimǎ zhōng fāxiàn le yí ge yǐnmì de luóji lòudòng. Zhè ge kànsì wēixiǎo de xìtǒng pòdòng, jíyì bèi hēikè lìyòng jìnxíng èyì shèntòu yǔ qièqǔ héxīn shùjùkù. Tuánduì tōngxiāo-dádàn de jǐnjí biānxǐe bǔdīng chéngxù, chèdǐ fēngdǔ le ānquán yǐnhuàn.",
                "en": "Security engineers discovered a covert logic vulnerability in code. This seemingly tiny system hole could easily be exploited by hackers to steal databases. The team coded patches overnight to plug risks.",
                "es": "Ingenieros de ciberseguridad hallaron una sutil brecha lógica en el código. Este minúsculo orificio permitía a atacantes infiltrarse en bases de datos. El equipo programó parches de urgencia para neutralizar la amenaza."
            }
        ]
    },

    # 16 插
    {
        "id": "16",
        "hanzi": "插",
        "pinyin": "chā",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to insert; to stick in; to pierce; to interpose",
            "es": "insertar; enchufar; clavar; meter; intercalar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to insert, stick, or pierce an object into an opening, gap, or soil",
                "definition_es": "introducir, clavar o embutir un objeto alargado en una abertura o superficie",
                "example_phrase": "插上电源插头 (plug in the electrical cord)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "姐姐买来了一束芬芳的白百合，小心翼翼地插进精致的青花瓷花瓶中。",
                "pinyin": "Jiějie mǎilai le yí shù fēnfāng de bái bǎihé, xiǎoxīnyìyì de chājìn jīngzhì de qīnghuācí huāpíng zhōng.",
                "en": "My sister bought fragrant white lilies and carefully inserted them into an exquisite porcelain vase.",
                "es": "Mi hermana compró un aromático ramo de azucenas y las colocó con esmero en un fino jarrón de porcelana."
            },
            {
                "id": "#2",
                "hanzi": "在严肃的讨论过程中随意插话打断别人，是一种极不礼貌的社交行为。",
                "pinyin": "Zài yánsù de tǎolùn guòchéng zhōng suíyì chāhuà dǎduàn biérén, shì yì zhǒng jí bù lǐmào de shèjiāo xíngwéi.",
                "en": "Casually interjecting and interrupting others during a serious discussion is extremely impolite social etiquette.",
                "es": "Interrumpir a otros interpelando sin permiso durante una deliberación seria resulta una falta de consideración social."
            }
        ],
        "collocations": [
            {"hanzi": "插头", "en": "electrical plug"},
            {"hanzi": "插座", "en": "power socket/outlet"},
            {"hanzi": "插花", "en": "flower arrangement; ikebana"},
            {"hanzi": "插嘴", "en": "butt in; interrupt talking"},
            {"hanzi": "插队", "en": "jump the queue / cut in line"},
            {"hanzi": "插图", "en": "book illustration"}
        ],
        "idioms": [
            {"hanzi": "插翅难逃", "pinyin": "chā chì nán táo", "meaning_en": "unable to escape even if given wings"},
            {"hanzi": "倒打一耙", "pinyin": "dào dǎ yì pá", "meaning_en": "make a bogus counter-accusation"},
            {"hanzi": "安插亲信", "pinyin": "ān chā qīn xìn", "meaning_en": "plant cronies in strategic positions"},
            {"hanzi": "旁敲侧击", "pinyin": "páng qiāo cè jī", "meaning_en": "drop indirect hints and insinuations"}
        ],
        "character_decomposition": [
            {
                "character": "插",
                "pinyin": "chā",
                "meaning_en": "insert; pierce; stick in; interpose",
                "meaning_es": "insertar; clavar; intercalar; meter",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand manipulation)",
                "sound_component": "臿 (chā, pestle pounding in mortar / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with 臿 (pestle pounding grain into mortar); motion of sticking or thrusting downward.",
                "visual_mnemonic_story_en": "A hand (扌) guides a pestle-like prong (臿) firmly into its slot (插).",
                "visual_mnemonic_story_es": "Una mano (扌) encaja una espiga (臿) firmemente en su ranura (插).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QHJL",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A hand (扌) plunges a rod down like a pestle (臿) to insert it securely (插).",
            "composite_memory_hook_es": "La mano (扌) clava un vástago como mano de mortero (臿) para insertarlo con firmeza (插).",
            "cultural_and_cognitive_roots": "Agricultural roots dating to Neolithic rice cultivation (插秧: inserting rice shoots into wet mud), expanding to modern electrical prongs.",
            "tone_sandhi_and_pitch_modulation": "High flat level tone: 'chā' (55). Hold clear high pitch 55 steadily without dipping."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "播", "pinyin": "bō", "meaning_en": "broadcast; sow seed", "distinction_note": "Has 番 on right of 扌 instead of 臿 in 插"},
                {"character": "捶", "pinyin": "chuí", "meaning_en": "beat; thump with fist", "distinction_note": "Has 垂 on right of 扌"},
                {"character": "碴", "pinyin": "chā", "meaning_en": "glass fragment; fault", "distinction_note": "Has stone radical 石 on left instead of hand 扌"},
                {"character": "茬", "pinyin": "chá", "meaning_en": "crop stubble; round", "distinction_note": "Has grass radical 艹 on top instead of 扌"}
            ],
            "etymological_cognates": [
                {"character": "刺", "pinyin": "cì", "gloss_en": "thorn; prick with sharp tip"},
                {"character": "入", "pinyin": "rù", "gloss_en": "enter; go inside"},
                {"character": "嵌", "pinyin": "qiàn", "gloss_en": "inlay flush into surface"},
                {"character": "穿", "pinyin": "chuān", "gloss_en": "pierce through; thread into"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "插 involves sliding or embedding an elongated object into an opening, gap, or soft medium.",
            "contrasts": [
                {"id": "1", "compared_word": "插 vs. 扎", "pinyin": "zhā", "analysis": "扎 emphasizes puncturing a surface with a needle or needle-point causing a wound, while 插 slides into pre-existing openings or soft soil."},
                {"id": "2", "compared_word": "插 vs. 塞", "pinyin": "sāi", "analysis": "塞 implies stuffing or jamming something tightly to plug a gap, while 插 implies a smooth linear insertion."},
                {"id": "3", "compared_word": "插 vs. 嵌", "pinyin": "qiàn", "analysis": "嵌 implies embedding flush into a groove or mosaic, whereas 插 leaves parts sticking out."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "暮春时节江南水乡春雨绵绵，农夫们卷起裤脚挽起衣袖，走入波光粼粼的水田中辛勤插秧。一株株翠绿柔嫩的秧苗被整齐地插入松软的泥土里，不一会儿，原本空旷的水面便泛起了一片生机勃勃的新绿。",
                "pinyin": "Mùchūn shíjié Jiāngnán shuǐxiāng chūnyǔ miánmián, nóngfūmen juǎnqǐ kùjiǎo wǎnqǐ yīxiù, zǒurù bōguāng-línlín de shuǐtián zhōng xīnqín chāyāng. Yìzhūzhū cuìlǜ róunèn de yāngmiáo bèi zhěngqí de chārù sōngruǎn de nítǔ lǐ, bù yíhuìr, yuánběn kōngkuàng de shuǐmiàn biàn fànqǐ le yí piàn shēngjī-bóbó de xīnlǜ.",
                "en": "In late spring southern wetlands, farmers transplant rice in glistening paddies. Tender green shoots are inserted neatly into mud, soon carpeting watery fields in vibrant green.",
                "es": "A fines de primavera, labriegos trasplantan arroz bajo mansa llovizna. Tallos verdes son insertados en el fango blando tiñendo el espejo de agua de un lozano manto esperanzador."
            },
            {
                "id": "#2",
                "hanzi": "日常使用各类家用电器时，必须严格遵守电气安全规范。潮湿的手绝对不能触碰插头，插入插座时也应动作平稳、严禁蛮力拉扯电线。只有养成良好的用电习惯，才能有效避免因接触不良而发生短路险情。",
                "pinyin": "Rìcháng shǐyòng gèlèi jiāyòng diànqì shí, bìxū yángé zūnshǒu diànqì ānquán guīfàn. Cháoshī de shǒu juéduì bù néng chùpèng chātóu, chārù chāzuò shí yě yīng dòngzuò píngwěn, yánjìn mánlì lāchě diànxiàn. Zhǐyào yǎngchéng liánghǎo de yòngdiàn xíguàn, cáinéng yǒuxiào bìmiǎn yīn jiēchù bùliáng ér fāshēng duǎnlù xiǎnqíng.",
                "en": "When using appliances, adhering to electrical safety is vital. Never touch plugs with wet hands; insert them smoothly into outlets without yanking cords to avoid short-circuit risks.",
                "es": "Al manipular electrodomésticos, acatar las normas de seguridad eléctrica es indispensable. Jamás toques enchufes húmedos; insértalos suavemente en la toma para evitar cortocircuitos."
            }
        ]
    },

    # 17 棍
    {
        "id": "17",
        "hanzi": "棍",
        "pinyin": "gùn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "stick; rod; truncheon; staff",
            "es": "palo; vara; bastón; garrote; porra"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a piece of solid wood, metal, or rigid material shaped into a straight cylindrical rod",
                "definition_es": "pieza cilíndrica y alargada de madera, metal u otro material resistente",
                "example_phrase": "木棍 / 警棍 (wooden stick / police baton)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "爷爷喜欢在山间小路上散步，手里总是拄着一根结实坚韧的竹棍作为拐杖。",
                "pinyin": "Yéye xǐhuan zài shānjiān xiǎolù shàng sànbù, shǒu lǐ zǒngshì zhǔ zhe yì gēn jiēshi jiānrèn de zhúgùn zuòwéi guǎizhàng.",
                "en": "Grandfather loves walking along mountain paths, always leaning on a sturdy bamboo stick as a cane.",
                "es": "Al abuelo le encanta pasear por senderos serranos, apoyándose siempre en una vara de bambú a modo de bastón."
            },
            {
                "id": "#2",
                "hanzi": "教练向武术学员们耐心传授少林棍法的防守与进攻技巧，动作刚劲有力。",
                "pinyin": "Jiàoliàn xiàng wǔshù xuéyuánmen nàixīn chuánshòu Shàolín gùnfǎ de fángshǒu yǔ jìngōng jìqiǎo, dòngzuò gāngjìng yǒulì.",
                "en": "The coach patiently instructed martial arts students in offensive and defensive Shaolin staff techniques.",
                "es": "El instructor transmitió pacientemente las técnicas de ataque y defensa con palo Shaolin, ejecutando movimientos vigorosos."
            }
        ],
        "collocations": [
            {"hanzi": "木棍", "en": "wooden stick"},
            {"hanzi": "铁棍", "en": "iron rod"},
            {"hanzi": "警棍", "en": "police baton"},
            {"hanzi": "棍棒", "en": "sticks and clubs"},
            {"hanzi": "手杖棍", "en": "walking stick"},
            {"hanzi": "指挥棍", "en": "baton / conducting stick"}
        ],
        "idioms": [
            {"hanzi": "当头棒喝", "pinyin": "dāng tóu bàng hè", "meaning_en": "sharp blow and loud shout; blunt awakening"},
            {"hanzi": "光棍一条", "pinyin": "guāng gùn yì tiáo", "meaning_en": "bachelor with no family ties; single person"},
            {"hanzi": "敲闷棍", "pinyin": "qiāo mèn gùn", "meaning_en": "strike someone secretly from behind; sneak attack"},
            {"hanzi": "弄巧成拙", "pinyin": "nòng qiǎo chéng zhuō", "meaning_en": "try to be clever only to blunder clumsily"}
        ],
        "character_decomposition": [
            {
                "character": "棍",
                "pinyin": "gùn",
                "meaning_en": "stick; rod; staff; scoundrel",
                "meaning_es": "palo; vara; bastón; bribón",
                "radical": "木",
                "radical_meaning_en": "wood / tree",
                "meaning_component": "木 (wooden timber)",
                "sound_component": "昆 (kūn, together / descendant / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Wood radical 木 combined with 昆 (together/multitude); a stripped wooden rod or staff shaped for utility.",
                "visual_mnemonic_story_en": "Carved straight from timber (木), a uniform rod (昆) becomes a sturdy walking staff (棍).",
                "visual_mnemonic_story_es": "Labrado en dura madera (木), un cilindro uniforme (昆) se convierte en bastón de apoyo (棍).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "DAMP",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Timber (木) trimmed into a solid straight piece (昆) forms a handheld stick (棍).",
            "composite_memory_hook_es": "La madera (木) alisada en tramo recto (昆) forma una vara o palo consistente (棍).",
            "cultural_and_cognitive_roots": "Revered as the ancestor of all weapons (百兵之祖) in Chinese martial arts due to its simplicity and versatility in combat.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone: 'gùn' (51). Descend sharply and firmly like a heavy wooden staff striking the earth."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "混", "pinyin": "hùn", "meaning_en": "mix; muddle along", "distinction_note": "Has water radical 氵 on left instead of wood 木 in 棍"},
                {"character": "辊", "pinyin": "gǔn", "meaning_en": "roller; revolve", "distinction_note": "Has vehicle radical 车 on left of 昆"},
                {"character": "琨", "pinyin": "kūn", "meaning_en": "fine jade", "distinction_note": "Has jade radical 王 on left of 昆"},
                {"character": "溷", "pinyin": "hùn", "meaning_en": "turbid; latrine", "distinction_note": "Has enclosure 囗 enclosing 豕"}
            ],
            "etymological_cognates": [
                {"character": "棒", "pinyin": "bàng", "gloss_en": "club; heavy wooden bat"},
                {"character": "杖", "pinyin": "zhàng", "gloss_en": "cane; dignified staff"},
                {"character": "杆", "pinyin": "gān", "gloss_en": "pole; vertical upright mast"},
                {"character": "枝", "pinyin": "zhī", "gloss_en": "branch; slender twig"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "棍 denotes a cylindrical, unbladed rod of uniform thickness, distinct from pointed canes or thick bats.",
            "contrasts": [
                {"id": "1", "compared_word": "棍 vs. 杖", "pinyin": "zhàng", "analysis": "杖 is dignified and ritualistic (拐杖 walking cane, 权杖 scepter), while 棍 is utilitarian for rough rods."},
                {"id": "2", "compared_word": "棍 vs. 棒", "pinyin": "bàng", "analysis": "棒 denotes a heavier, thicker club or bat (棒球棒, 木棒), while 棍 has uniform slender diameter."},
                {"id": "3", "compared_word": "棍 vs. 杆", "pinyin": "gān", "analysis": "杆 designates tall vertical posts or poles (旗杆 flagpole, 电线杆 utility pole), while 棍 is handheld."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在传统中国武术中，棍被称为“百兵之祖”。练棍讲究身法灵活、棍随身转。挥舞之时如疾风扫落叶，密不透风。武术练习者通过持之以恒地挥棍磨砺臂力与协调性，涵养坚毅不屈的武德与沉稳气度。",
                "pinyin": "Zài chuántǒng Zhōngguó wǔshù zhōng, gùn bèi chēngwéi 'bǎibīngzhīzǔ'. Liàn gùn jiǎngjiu shēnfǎ línghuó, gùn suí shēn zhuǎn. Huīwǔ zhīshí rú jífēng sǎoluòyè, mìbùtòufēng. Wǔshù liànxízhě tōngguò chízhīyǐhéng de huīgùn mólì bìlì yǔ xiétiáoxìng, hányǎng jiānyì-bùqū de wǔdé yǔ chénwěn qìdù.",
                "en": "In martial arts, the staff is called ancestor of all weapons. Practice requires agile footwork, sweeping like winds to temper arm strength, resilience, and inner composure.",
                "es": "En las artes marciales chinas, el bastón es progenitor de las armas. Su manejo exige agilidad y cadencia armónica, templando la fuerza física, la entereza moral y el temple."
            },
            {
                "id": "#2",
                "hanzi": "野外科考队员在茂密的热带雨林中穿行时，每个人手中都会随身携带一根探路木棍。这根看似普通的木棍，不仅能在陡峭湿滑的泥泞山路上借力支撑身体平衡，更能在拨开荆棘杂草时提前惊走潜伏的毒蛇与昆虫。",
                "pinyin": "Yěwài kěkǎoduìyuán zài màomì de rèdài yǔlín zhōng chuānxíng shí, měi ge rén shǒu zhōng dōuhuì suíshēn xiédài yì gēn tànlù mùgùn. Zhè gēn kànsì pǔtōng de mùgùn, bùjǐn néng zài dǒuqiào shīhuá de nínìng shānlù shàng jièlì zhīchēng shēntǐ pínghéng, gèng néng zài bōkāi jīngjí zácǎo shí tíqián jīngzǒu qiánfú de dúshé yǔ kūnchóng.",
                "en": "Trekking in rainforests, expeditions carry walking sticks. This wooden rod supports balance on slippery slopes and rustles thorny brush to scare away lurking snakes.",
                "es": "Al explorar selvas tropicales, los científicos portan una vara de madera para tantear el sendero. Asegura el equilibrio en pendientes y bate matorrales ahuyentando víboras."
            }
        ]
    },

    # 18 系
    {
        "id": "18",
        "hanzi": "系",
        "pinyin": "jì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to tie; to fasten; to bind; to buckle",
            "es": "atar; amarrar; abrochar; ceñir; anudar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to tie, bind, knot, or fasten with a cord, rope, strap, or belt (pronounced jì)",
                "definition_es": "atar, anudar, abrochar o sujetar mediante cuerda, lazo, correa o cinturón (leído jì)",
                "example_phrase": "系鞋带 / 系安全带 (tie shoelaces / fasten seatbelt)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "登机入座后，乘务员微笑着提醒每一位旅客系好座椅上的安全带。",
                "pinyin": "Dēngjī rùzuò hòu, chéngwùyuán wēixiào zhe tíxǐng měi yí wèi lǚkè jìhǎo zuòyǐ shàng de ānquándài.",
                "en": "After boarding, the flight attendant reminded passengers to fasten their seatbelts.",
                "es": "Tras acomodarse en el avión, la azafata recordó a los pasajeros abrocharse los cinturones de seguridad."
            },
            {
                "id": "#2",
                "hanzi": "他在木棍上牢牢系了一条细线，用它制作了一副简单耐用的简易捕鱼工具。",
                "pinyin": "Tā zài mùgùn shàng láoláo jì le yì tiáo xìxiàn, yòng tā zhìzuò le yí fù jiǎndān nàiyòng de jiǎnyì bǔyú gōngjù.",
                "en": "He tied a thin line firmly onto the wooden stick, making a simple improvised fishing rig.",
                "es": "Ató firmemente un sedal a la vara de madera, fabricando un útil de pesca casero, sencillo y resistente."
            }
        ],
        "collocations": [
            {"hanzi": "系好", "en": "fasten securely"},
            {"hanzi": "系鞋带", "en": "tie shoelaces"},
            {"hanzi": "系安全带", "en": "buckle seatbelt"},
            {"hanzi": "系上围裙", "en": "put on / tie apron"},
            {"hanzi": "系红领巾", "en": "tie red scarf"},
            {"hanzi": "系紧绳子", "en": "tighten rope knot"}
        ],
        "idioms": [
            {"hanzi": "解铃系铃", "pinyin": "jiě líng xì líng", "meaning_en": "let whoever tied the bell untie it; solve what one caused"},
            {"hanzi": "心系祖国", "pinyin": "xīn xì zǔ guó", "meaning_en": "heart inextricably tied to one's homeland"},
            {"hanzi": "千钧一发", "pinyin": "qiān jūn yí fà", "meaning_en": "suspended by a single hair; extremely critical moment"},
            {"hanzi": "命系一线", "pinyin": "mìng xì yí xiàn", "meaning_en": "one's life hanging by a single slender thread"}
        ],
        "character_decomposition": [
            {
                "character": "系",
                "pinyin": "jì",
                "meaning_en": "tie; fasten; knot; bind",
                "meaning_es": "atar; anudar; amarrar; abrochar",
                "radical": "糸",
                "radical_meaning_en": "silk / thread",
                "meaning_component": "糸 (silk filaments/threads)",
                "sound_component": "丿 (hand reaching to attach)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of silk skeins connected together with a binding tie; phonetic split between colloquial jì (fasten) and formal xì (system).",
                "visual_mnemonic_story_en": "Silk threads (糸) are held by a hand and tied into a firm knot (系).",
                "visual_mnemonic_story_es": "Hebras de seda (糸) sujetadas por una mano para anudarlas con firmeza (系).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HVI",
                "traditional": "繫"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Hold silk threads (糸) and snap them down tight into a knot (jì, 系).",
            "composite_memory_hook_es": "Toma hebras de seda (糸) y ciérralas en un nudo firme (jì, 系).",
            "cultural_and_cognitive_roots": "Textile knotting culture in ancient China; before writing, knots (结绳记事) recorded treaties and obligations, giving '系' deep cultural resonance.",
            "tone_sandhi_and_pitch_modulation": "Falling fourth tone: 'jì' (51). Snap down sharply and firmly like locking a seatbelt buckle into place."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "素", "pinyin": "sù", "meaning_en": "plain; vegetarian; element", "distinction_note": "Has 𡗗 on top instead of 丿 in 系"},
                {"character": "絮", "pinyin": "xù", "meaning_en": "cotton wadding; chatter", "distinction_note": "Has 如 on top of 糸"},
                {"character": "索", "pinyin": "suǒ", "meaning_en": "rope; search; demand", "distinction_note": "Has 十 and 冖 atop 糸"},
                {"character": "累", "pinyin": "lèi", "meaning_en": "tired; accumulate", "distinction_note": "Has field 田 on top of 糸"}
            ],
            "etymological_cognates": [
                {"character": "结", "pinyin": "jié", "gloss_en": "knot; tie into bundle"},
                {"character": "绑", "pinyin": "bǎng", "gloss_en": "bind; tie person to post"},
                {"character": "扣", "pinyin": "kòu", "gloss_en": "button; buckle clasp"},
                {"character": "缚", "pinyin": "fù", "gloss_en": "bind; tie tightly with cords"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "系 (jì) emphasizes binding or fastening with flexible cords, straps, or ribbons.",
            "contrasts": [
                {"id": "1", "compared_word": "系 (jì) vs. 捆", "pinyin": "kǔn", "analysis": "捆 refers to bundling up bulky cargo tightly with thick ropes, whereas 系 is tying a neat knot or fastening a strap/belt."},
                {"id": "2", "compared_word": "系 (jì) vs. 绑", "pinyin": "bǎng", "analysis": "绑 involves binding someone or something securely to immobilize it, while 系 fastens garments and accessories."},
                {"id": "3", "compared_word": "系 (jì) vs. 扣", "pinyin": "kòu", "analysis": "扣 focuses on snapping buttons or clasps together, whereas 系 uses cordage and knotting."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在驾驶汽车出行时，上车后第一件事就是规范地系好安全带。这条看似普通的尼龙带子，是发生突发碰撞时保护驾乘人员生命安全的关键屏障。系牢的是安全带，守护的是每一个家庭的团圆与平安。",
                "pinyin": "Zài jiàshǐ qìchē chūxíng shí, shàngchē hòu dì-yī jiàn shì jiùshì guīfàn de jìhǎo ānquándài. Zhè tiáo kànsì pǔtōng de nílóng dàizi, shì fāshēng tūfā pèngzhuàng shí bǎohù jiàchéng rényuán shēngmìng ānquán de guānjiàn píngzhàng. Jìláo de shì ānquándài, shǒuhù de shì měi yí ge jiātíng de tuányuán yǔ píng'ān.",
                "en": "When driving, buckling the seatbelt properly is the first step. This nylon belt is a vital barrier protecting lives during collisions, safeguarding family peace.",
                "es": "Al subir a un coche, abrocharse el cinturón de seguridad es el primer paso. Esta banda de nailon salvaguarda vidas en colisiones custodiando la paz familiar."
            },
            {
                "id": "#2",
                "hanzi": "秋风渐凉，母亲细心地为即将远行求学的儿子整理行装，并在毛衣领口系上了一条亲手织就的羊毛围巾。那温暖整齐的结扣，紧紧系着长辈对游子道不尽的牵挂与叮咛，无论走多远都能感受到家的温存。",
                "pinyin": "Qiūfēng jiàn liáng, mǔqīn xìxīn de wèi jíjiāng yuǎnxíng qiúxué de érzi zhěnglǐ xíngzhuang, bìng zài máoyī lǐngkǒu jì shàng le yì tiáo qīnshǒu zhījiù de yángmáo wéijīn. Nà wēnnuǎn zhěngqí de jiékòu, jǐnjǐn jì zhe zhǎngbèi duì yóuzǐ dào bù jìn de qiānguà yǔ dīngníng, wúlùn zǒu duō yuǎn dōunéng gǎnshòudào jiā de wēncún.",
                "en": "As autumn cools, mother packs for her son studying afar, tying a hand-knit woolen scarf at his sweater collar. That neat knot ties elders' boundless yearnings to him wherever he journeys.",
                "es": "Con el fresco otoñal, una madre prepara el equipaje de su hijo anudándole al cuello una bufanda tejida a mano. Ese nudo ata el cariño familiar arropándolo en la distancia."
            }
        ]
    },

    # 19 匹
    {
        "id": "19",
        "hanzi": "匹",
        "pinyin": "pǐ",
        "part_of_speech": "Measure Word",
        "meanings_summary": {
            "en": "measure word for horses or cloth bolts; match; equal",
            "es": "clasificador para caballos o piezas de tela; rival; igual"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Measure Word",
                "register": "Standard",
                "definition_en": "measure word used for horses, mules, or bolts of woven cloth",
                "definition_es": "clasificador numeral empleado para caballos, mulas o piezas de tela",
                "example_phrase": "一匹骏马 / 两匹布 (a spirited horse / two bolts of cloth)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "广阔无垠的蒙古大草原上，一匹黑色的骏马正迎着晨曦自由自在地飞驰奔跑。",
                "pinyin": "Guǎngkuò-wúyín de Měnggǔ dàcǎoyuán shàng, yì pǐ hēisè de jùnmǎ zhèng yíngzhe chénxī zìyóuzìzài de fēichí bēnpǎo.",
                "en": "On the boundless Mongolian steppe, a black steed galloped freely into the morning dawn.",
                "es": "En la inmensa estepa mongola, un brioso caballo negro galopaba a sus anchas de cara al alba."
            },
            {
                "id": "#2",
                "hanzi": "在这场马拉松长跑决赛中，这位名不见经传的年轻小将成为一匹爆冷的黑马，夺得冠军。",
                "pinyin": "Zài zhè chǎng mǎlāsōng chángpǎo juésài zhōng, zhè wèi míngbùjiànjīngzhuàn de niánqīng xiǎojiàng chéngwéi yì pǐ bàolěng de hēimǎ, duódé guànjūn.",
                "en": "In the marathon final, this little-known young athlete emerged as a dark horse upset, winning the championship.",
                "es": "En la final de maratón, este desconocido joven atleta se convirtió en un caballo negro revelación alzándose con el título."
            }
        ],
        "collocations": [
            {"hanzi": "一匹马", "en": "a horse"},
            {"hanzi": "一匹骏马", "en": "a fine spirited horse"},
            {"hanzi": "一匹黑马", "en": "a dark horse (surprise winner)"},
            {"hanzi": "一匹布", "en": "a bolt of cloth"},
            {"hanzi": "单枪匹马", "en": "single-handed; all alone"},
            {"hanzi": "匹配", "en": "to match / pair up"}
        ],
        "idioms": [
            {"hanzi": "单枪匹马", "pinyin": "dān qiāng pǐ mǎ", "meaning_en": "single-handed; completely on one's own"},
            {"hanzi": "匹夫有责", "pinyin": "pǐ fū yǒu zé", "meaning_en": "every ordinary citizen shares responsibility for the nation"},
            {"hanzi": "天下无匹", "pinyin": "tiān xià wú pǐ", "meaning_en": "matchless in the world; peerless"},
            {"hanzi": "势均力敌", "pinyin": "shì jūn lì dí", "meaning_en": "evenly matched in strength"}
        ],
        "character_decomposition": [
            {
                "character": "匹",
                "pinyin": "pǐ",
                "meaning_en": "measure word for horses/cloth; equal; match",
                "meaning_es": "clasificador para caballos/tela; semejante; rival",
                "radical": "匚",
                "radical_meaning_en": "box / enclosure",
                "meaning_component": "匚 (container/measured enclosure)",
                "sound_component": "儿 (legs / phonetic carrier)",
                "stroke_count": 4,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Enclosure 匚 holding measured rolls of silk; ancient textile counting unit later applied to equines.",
                "visual_mnemonic_story_en": "A measure box (匚) neatly rolls up a bolt of silk cloth (匹).",
                "visual_mnemonic_story_es": "Un cajón de medida (匚) enrolla con pulcritud una pieza de seda (匹).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "SU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Count horses and fine silk bolts within the standard measure box (匹).",
            "composite_memory_hook_es": "Cuenta corceles y piezas de tela fina con el clasificador patrón (匹).",
            "cultural_and_cognitive_roots": "Silk trading on the Northern frontier: an equine war horse was valued at exactly one bolt of standard silk (匹), permanently bridging the classifier.",
            "tone_sandhi_and_pitch_modulation": "Dipping third tone: 'pǐ' (214). Dip down low to pitch 2 and rebound lightly up to 4."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "四", "pinyin": "sì", "meaning_en": "four", "distinction_note": "Has enclosed box 囗 with 儿 inside instead of 匚 open on right in 匹"},
                {"character": "西", "pinyin": "xī", "meaning_en": "west", "distinction_note": "Has top stroke 一 over enclosure"},
                {"character": "巨", "pinyin": "jù", "meaning_en": "huge; gigantic", "distinction_note": "Has internal horizontal and vertical hook strokes inside 匚"},
                {"character": "臣", "pinyin": "chén", "meaning_en": "official; minister", "distinction_note": "Pictogram of downcast eye in vertical frame"}
            ],
            "etymological_cognates": [
                {"character": "配", "pinyin": "pèi", "gloss_en": "match; pair together"},
                {"character": "头", "pinyin": "tóu", "gloss_en": "classifier for cattle and pigs"},
                {"character": "卷", "pinyin": "juǎn", "gloss_en": "roll of paper or fabric"},
                {"character": "双", "pinyin": "shuāng", "gloss_en": "pair; couple"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "匹 is the dedicated classifier for horses, mules, and fabric bolts, conveying stature and vigor.",
            "contrasts": [
                {"id": "1", "compared_word": "匹 vs. 头", "pinyin": "tóu", "analysis": "头 is the classifier for cattle, pigs, and donkeys ('一头牛', '一头猪'), while horses strictly take 匹 ('一匹马')."},
                {"id": "2", "compared_word": "匹 vs. 只", "pinyin": "zhī", "analysis": "只 is the classifier for birds, sheep, and small pets, inappropriate for noble horses in standard Chinese."},
                {"id": "3", "compared_word": "匹 vs. 卷", "pinyin": "juǎn", "analysis": "卷 counts modern rolled carpets and paper, whereas 匹 traditionally counts whole woven fabric bolts ('两匹布')."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古丝绸之路上，商人牵着满载丝绸的骆驼商队西行，用一匹匹细腻柔软的中国绫罗绸缎，换回西域良马。一匹匹神骏的汗血宝马穿行在大漠黄沙间，见证了东西方文明跨越千山万水的繁荣交融。",
                "pinyin": "Gǔ Sīchóuzhīlù shàng, shāngrén qiānzhe mǎnzài sīchóu de luòtuo shāngduì xīxíng, yòng yì pǐ pǐ xìnì róuruǎn de Zhōngguó língluó-chóuduàn, huànhuí Xīyù liángmǎ. Yì pǐ pǐ shénjùn de hànxiě bǎomǎ chuānxíng zài dàmò huángshā jiān, jiànzhèng le dōng-xīfāng wénmíng kuàyuè qiānshān-wànshuǐ de fánróng jiāoróng.",
                "en": "On the Silk Road, merchants traded bolts of silk for western steeds. Noble horses trotting through desert sands witnessed the prosperous fusion of civilizations.",
                "es": "En la Ruta de la Seda, caravanas trocaban piezas de seda por corceles occidentales. Caballos trotando entre arenas desérticas atestiguaron la fructífera comunión de civilizaciones."
            },
            {
                "id": "#2",
                "hanzi": "在现代科技竞技赛场上，只要敢打敢拼，任何籍籍无名的初创企业都有可能凭借颠覆性创新脱颖而出，成为震撼行业的“独角兽黑马”。这匹黑马的诞生，不仅打破了既有市场格局，更激发了全社会的创新活力。",
                "pinyin": "Zài xiàndài kējì jìngjì sàichǎng shàng, zhǐyào gǎndǎ-gǎnpīn, rènhé jíjímíngbù de chūchuàng qǐyè dōuyǒu kěnéng píngjiè diānfùxìng chuàngxīn tuōyǐng'érchū, chéngwéi zhènhàn hángyè de 'dújiǎoshòu hēimǎ'. Zhè pǐ hēimǎ de dànshēng, bùjǐn dǎpò le jìyǒu shìchǎng géjú, gèng jīfā le quán shèhuì de chuàngxīn huólì.",
                "en": "In tech arenas, an obscure startup pioneering disruption can emerge as an industry-shaking dark horse unicorn. Its birth shatters market setups and inspires innovation.",
                "es": "En la arena tecnológica, una empresa emergente resuelta puede irrumpir como caballo negro unicornio gracias a una innovación disruptiva, sacudiendo el mercado con dinamismo creador."
            }
        ]
    },

    # 20 拦
    {
        "id": "20",
        "hanzi": "拦",
        "pinyin": "lán",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to block; to stop; to bar; to intercept",
            "es": "bloquear; detener; atajar; interceptar; impedir el paso"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to obstruct, block, or hold back someone or something from proceeding forward",
                "definition_es": "obstruir el paso, atajar o detener a alguien o algo en su trayectoria",
                "example_phrase": "拦住去路 (block the way / obstruct the path)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "暴雨导致山体滑坡，倒塌的大树和泥石横在路中，拦住了所有过往车辆的去路。",
                "pinyin": "Bàoyǔ dǎozhì shāntǐ huápō, dǎotā de dàshù hé níshí héng zài lù zhōng, lánzhù le suǒyǒu guòwǎng chēliàng de qùlù.",
                "en": "Torrential rain triggered landslides; fallen trees and rocks blocked the road, barring all passing vehicles.",
                "es": "La tromba provocó un desprendimiento; árboles caídos y lodo cortaron la calzada, bloqueando el paso a todos los vehículos."
            },
            {
                "id": "#2",
                "hanzi": "他刚想冲动地冲出门去理论，被身旁冷静的好友一把拦了下来。",
                "pinyin": "Tā gāng xiǎng chōngdòng de chōng chū mén qù lǐlùn, bèi shēnpáng lěngjìng de hǎoyǒu yì bǎ lán le xiàlai.",
                "en": "Just as he impulsively bolted out to argue, his calm friend beside him held him back.",
                "es": "Justo cuando pretendía salir airado a pedir explicaciones, su sereno amigo lo retuvo de inmediato sujetándolo del brazo."
            }
        ],
        "collocations": [
            {"hanzi": "拦住", "en": "block / hold back"},
            {"hanzi": "拦车", "en": "hail or stop a vehicle"},
            {"hanzi": "阻拦", "en": "obstruct / deter"},
            {"hanzi": "拦截", "en": "intercept"},
            {"hanzi": "拦路虎", "en": "stumbling block; road obstacle"},
            {"hanzi": "拦网", "en": "block at the net (sports)"}
        ],
        "idioms": [
            {"hanzi": "拦路打劫", "pinyin": "lán lù dǎ jié", "meaning_en": "highway robbery; rob along roads"},
            {"hanzi": "势不可挡", "pinyin": "shì bù kě dǎng", "meaning_en": "unstoppable; irresistible force"},
            {"hanzi": "无可阻挡", "pinyin": "wú kě zǔ dǎng", "meaning_en": "incapable of being held back"},
            {"hanzi": "挡箭牌", "pinyin": "dǎng jiàn pái", "meaning_en": "shield; pretext / scapegoat"}
        ],
        "character_decomposition": [
            {
                "character": "拦",
                "pinyin": "lán",
                "meaning_en": "block; stop; bar; obstruct",
                "meaning_es": "bloquear; atajar; parar; impedir paso",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand action)",
                "sound_component": "兰 (lán, orchid / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Hand radical 扌 combined with 兰 (lán phonetic); hand reaching out horizontally to halt movement.",
                "visual_mnemonic_story_en": "A firm hand (扌) reaches out across the road to bar (拦) anyone from passing.",
                "visual_mnemonic_story_es": "Una mano extendida (扌) corta el paso en el camino para atajar (拦) el avance.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "QTFM",
                "traditional": "攔"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A hand (扌) reaches out horizontally (lán) to block the way (拦).",
            "composite_memory_hook_es": "La mano extendida (扌) corta el paso (lán) deteniendo la marcha (拦).",
            "cultural_and_cognitive_roots": "Derived from the physical barrier of wooden railing fences (栏), evolving a hand radical (扌) to express active manual interception.",
            "tone_sandhi_and_pitch_modulation": "Rising second tone: 'lán' (35). Sweep upward smoothly from mid pitch 3 to high 5."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "栏", "pinyin": "lán", "meaning_en": "fence; railing; column", "distinction_note": "Has wood radical 木 on left instead of hand 扌 in 拦"},
                {"character": "烂", "pinyin": "làn", "meaning_en": "rotten; worn out", "distinction_note": "Has fire radical 火 on left"},
                {"character": "滥", "pinyin": "làn", "meaning_en": "overflow; excessive", "distinction_note": "Has water radical 氵 on left"},
                {"character": "览", "pinyin": "lǎn", "meaning_en": "look at; view", "distinction_note": "Has see radical 见 at bottom"}
            ],
            "etymological_cognates": [
                {"character": "挡", "pinyin": "dǎng", "gloss_en": "ward off; shield against"},
                {"character": "阻", "pinyin": "zǔ", "gloss_en": "hinder; impede progression"},
                {"character": "截", "pinyin": "jié", "gloss_en": "cut off; intercept midway"},
                {"character": "遏", "pinyin": "è", "gloss_en": "halt; suppress advance"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "拦 focuses on stepping in front of someone or something in motion to physically halt their path.",
            "contrasts": [
                {"id": "1", "compared_word": "拦 vs. 挡", "pinyin": "dǎng", "analysis": "挡 emphasizes shielding against wind, rain, or blows (挡风, 挡雨), while 拦 specifically halts forward motion."},
                {"id": "2", "compared_word": "拦 vs. 阻", "pinyin": "zǔ", "analysis": "阻 is more formal and abstract, denoting setting up obstacles or deterrents (阻止, 阻碍), while 拦 is concrete manual action."},
                {"id": "3", "compared_word": "拦 vs. 截", "pinyin": "jié", "analysis": "截 emphasizes cutting off or intercepting midway (截断, 截获), while 拦 is holding back."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "深山巡护员老张在林区巡查时，敏锐地察觉到前方灌木丛有异动。他毫不犹豫地跨前一步，大声喝止并伸手拦住了一名企图偷运珍稀中草药的可疑人员，成功保护了国家重点自然保护区的生态安全。",
                "pinyin": "Shēnshān xúnhùyuán Lǎo Zhāng zài línqū xúnchá shí, mǐnruì de cháchuédào qiánfāng guānmùcóng yǒu yìdòng. Tā háobùyóuyù de kuàqián yíbù, dàshēng hèzhǐ bìng shēnshǒu lánzhù le yì míng qǐtú tōuyùn zhēnxī zhōngcǎoyào de kěyí rényuán, chénggōng bǎohù le guójiā zhòngdiǎn zìrán bǎohùqū de shēngtài ānquán.",
                "en": "Patrolling the deep forest, Ranger Lao Zhang noticed rustling in bushes. Stepping forward, he shouted and stretched his arm to bar a suspect smuggling rare herbs, protecting the reserve.",
                "es": "Patrullando la espesura, el guardabosques notó movimientos sospechosos. Dio un paso al frente y extendió el brazo reteniendo a un infractor que traficaba hierbas medicinales, salvaguardando la reserva."
            },
            {
                "id": "#2",
                "hanzi": "科研攻关道路上从没有一帆风顺的坦途，各种始料不及的技术壁垒就像一只只凶猛的“拦路虎”，横亘在团队面前。然而，年轻的科学家们毫不气馁，迎难而上日夜攻坚，终于踢开绊脚石，迎来了核心突破。",
                "pinyin": "Kēyán gōngguān dàolù shàng cóng méiyǒu yīfānfēngshùn de tǎntú, gèzhǒng shǐliàobùjí de jìshù bìlěi jiù xiàng yìzhīzhī xiōngměng de 'lánlùhǔ', hénggèn zài tuánduì miànqián. Rán'ér, niánqīng de kēxuéjiāmen háobù qìněi, yíngnán'érshàng rìyè gōngjiān, zhōngyú tīkāi bànjiǎoshí, yínglái le héxīn tūpò.",
                "en": "The path of scientific innovation is never smooth; unexpected barriers stand like fierce roadblocks. Yet young scientists press forward tirelessly, kicking away stumbling blocks to achieve breakthroughs.",
                "es": "La senda investigadora jamás es un camino llano; barreras técnicas inesperadas se alzan como fieros escollos ante el equipo. Los jóvenes científicos perseveran superando tropiezos hasta coronar un hito decisivo."
            }
        ]
    }
]

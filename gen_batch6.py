from builder import save_word

words_batch6 = [
    # 26 脑袋
    {
        "id": "26",
        "hanzi": "脑袋",
        "pinyin": "nǎo dai",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "head; skull; brains; mental capacity",
            "es": "cabeza; cráneo; seso; inteligencia; mente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the human physical head or cranium containing the brain",
                "definition_es": "la cabeza física humana que aloja el cerebro",
                "example_phrase": "摸摸脑袋 (scratch or touch one's head)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Colloquial",
                "definition_en": "intellect, mental wits, or cleverness",
                "definition_es": "inteligencia, seso o agudeza mental",
                "example_phrase": "很有商业脑袋 (have a great head for business)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "小弟弟做错了数学算术题，有些害羞地挠了挠毛茸茸的小脑袋，逗得全家人都哈哈大笑。",
                "pinyin": "Xiǎo dìdi zuòcuò le shùxué suànshù tí, yǒuxiē hàixiū de náo le náo máorōngrōng de xiǎo nǎodai, dòu de quánjiā rén dōu hāhā dàxiào.",
                "en": "Having made a mistake on his math arithmetic problem, my little brother shyly scratched his fluffy little head, making the whole family burst into laughter.",
                "es": "Al equivocarse en la cuenta de matemáticas, mi hermanito se rascó la cabecita con timidez, haciendo reír a toda la familia a carcajadas."
            },
            {
                "id": "#2",
                "hanzi": "现代神经认知科学与类脑计算研究发现，人类脑袋在处理高维度模糊信息时表现出的超低能耗与高容错性，为下一代神经形态芯片提供了重要启发。",
                "pinyin": "Xiàndài shénjīng rènzhī kēxué yǔ lèi nǎo jìsuàn yánjiū fāxiàn, rénlèi nǎodai zài chǔlǐ gāo wéidù móhu xìnxī shí biǎoxiàn chū de chāodī nénghào yǔ gāo róngcuòxìng, wèi xià yí dài shénjīng xíngtài xīnpiàn tígōng le zhòngyào qǐfā.",
                "en": "Neurocognitive science and brain-inspired computing have revealed that the ultra-low energy consumption and high fault tolerance of human brains in processing complex fuzzy data inspire neuromorphic chips.",
                "es": "La neurociencia cognitiva ha descubierto que el bajo consumo energético y la tolerancia a fallos del cerebro humano al procesar datos complejos inspiran el diseño de chips neuromórficos."
            }
        ],
        "collocations": [
            {"hanzi": "摸摸脑袋", "en": "pat or rub one's head"},
            {"hanzi": "歪着脑袋", "en": "cock one's head to one side"},
            {"hanzi": "脑袋灵活", "en": "quick-witted / sharp head"},
            {"hanzi": "拍脑袋决定", "en": "make a knee-jerk decision off the top of one's head"},
            {"hanzi": "脑袋发懵", "en": "one's head is dazed / befuddled"},
            {"hanzi": "摇晃脑袋", "en": "shake one's head"}
        ],
        "idioms": [
            {"hanzi": "头晕脑胀", "pinyin": "tóu yūn nǎo zhàng", "meaning_en": "dizzy and light-headed; head swelling with fatigue"},
            {"hanzi": "呆头呆脑", "pinyin": "dāi tóu dāi nǎo", "meaning_en": "slow-witted and wooden-headed; mutton-headed"},
            {"hanzi": "探头探脑", "pinyin": "tàn tóu tàn nǎo", "meaning_en": "pop one's head in and peer around slyly"},
            {"hanzi": "没头没脑", "pinyin": "méi tóu méi nǎo", "meaning_en": "without head or tail; completely senseless and abrupt"}
        ],
        "character_decomposition": [
            {
                "character": "脑",
                "pinyin": "nǎo",
                "meaning_en": "brain; cranium; intellect",
                "meaning_es": "cerebro; seso; entendimiento",
                "radical": "肉",
                "radical_meaning_en": "meat / flesh",
                "meaning_component": "月/肉 (flesh/body organ)",
                "sound_component": "囟 / 凶 (xìn, fontanelle of skull)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Depicts bodily tissue (月) housed under the cranial fontanelle (囟/凶) with hair fibers, representing the physical brain.",
                "visual_mnemonic_story_en": "The vital organ of flesh (月) protected inside the skull (凶/匕) powers thoughts and wits.",
                "visual_mnemonic_story_es": "El órgano vital de carne (月) resguardado dentro del cráneo (凶/匕) impulsa las ideas y la lucidez.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "BYUK",
                "traditional": "腦"
            },
            {
                "character": "袋",
                "pinyin": "dai",
                "meaning_en": "pouch; bag; pocket; sack",
                "meaning_es": "bolsa; saco; faltriquera",
                "radical": "衣",
                "radical_meaning_en": "clothing",
                "meaning_component": "衣 (fabric garment/container)",
                "sound_component": "代 (dài, replacement/generation)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing garment (衣) with 代 (dài), denoting a fabric pouch sewn to hold precious contents.",
                "visual_mnemonic_story_en": "A pouch of cloth garment (衣) holds valuables across generations (代).",
                "visual_mnemonic_story_es": "Una bolsa de tela (衣) contiene objetos valiosos que pasan de una generación a otra (代).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OPYV",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The brain (脑) encased within the fleshly cranial pouch (袋) forms our head and mind (脑袋).",
            "composite_memory_hook_es": "El cerebro (脑) alojado dentro de la cavidad o saco craneal (袋) conforma nuestra cabeza y mente (脑袋).",
            "cultural_and_cognitive_roots": "Metaphorically visualizes the human cranium as a biological pouch ('dài') containing brains ('nǎo'); colloquial Chinese frequently uses 'nǎodai' to indicate practical wits ('商业脑袋') or impulsive decisions ('拍脑袋').",
            "tone_sandhi_and_pitch_modulation": "214-51 contour. In standard colloquial Mandarin, the second syllable is almost universally pronounced in a neutral tone (nǎodai / nǎodɑi)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "恼", "pinyin": "nǎo", "meaning_en": "annoyed; irritated", "distinction_note": "Features heart radical 忄 on the left instead of flesh 月"},
                {"character": "贷", "pinyin": "dài", "meaning_en": "loan; borrow", "distinction_note": "Features shell radical 贝 at the bottom instead of clothing 衣"},
                {"character": "装", "pinyin": "zhuāng", "meaning_en": "attire; load", "distinction_note": "Features 壮 on top instead of 代 above 衣"},
                {"character": "囊", "pinyin": "náng", "meaning_en": "pocket; bag", "distinction_note": "Much more complex radical structure for pouch"}
            ],
            "etymological_cognates": [
                {"character": "头", "pinyin": "tóu", "gloss_en": "head; chief"},
                {"character": "颅", "pinyin": "lú", "gloss_en": "skull; cranium"},
                {"character": "胞", "pinyin": "bāo", "gloss_en": "cell; uterine sac"},
                {"character": "肚", "pinyin": "dù", "gloss_en": "belly; stomach sac"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "脑袋 refers colloquially to the physical head and anatomical skull, or informally to a person's mental wits and ingenuity.",
            "contrasts": [
                {"id": "1", "compared_word": "脑袋 vs. 头部", "pinyin": "tóubù", "analysis": "头部 is a formal medical, scientific, and technical anatomical term, whereas 脑袋 is everyday, vivid spoken Chinese."},
                {"id": "2", "compared_word": "脑袋 vs. 头脑", "pinyin": "tóunǎo", "analysis": "头脑 refers primarily to cognitive reasoning, mental capacity, or organizational leadership (e.g., 清醒的头脑), while 脑袋 can refer literally to the physical head."},
                {"id": "3", "compared_word": "脑袋 vs. 脑海", "pinyin": "nǎohǎi", "analysis": "脑海 is a poetic/literary term denoting the subjective theatre of memory and consciousness (e.g., 浮现在脑海中), not physical anatomy."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "夕阳的余晖洒在静谧的村庄里，老爷爷戴着老花镜，一边看着报纸，一边轻轻抚摸着膝头孙子毛茸茸的小脑袋。屋檐下微风拂过，岁月安详得如同一幅水墨画。小小的脑袋里装满了对外头世界的奇思妙想。",
                "pinyin": "Xīyáng de yúhuī sǎ zài jìngmì de cūnzhuāng lǐ, lǎoyéye dài zhe lǎohuājìng, yìbiān kàn zhe bàozhǐ, yìbiān qīngqīng fǔmō zhe xītóu sūnzi máorōngrōng de xiǎo nǎodai. Wūyán xià wēifēng fúguò, suìyuè ānxiáng de rútóng yì fú shuǐmòhuà. Xiǎoxiǎo de nǎodai lǐ zhuāngmǎn le duì wàitóu shìjiè de qísīmiàoxiǎng.",
                "en": "Sunset glow bathed the tranquil village as grandfather read his paper while stroking the fluffy head of his grandson on his knee. Under the eaves breezes blew, peaceful as a wash painting. That little head was full of wonder for the world.",
                "es": "La luz del atardecer doraba la aldea tranquila mientras el abuelo leía acariciando la cabecita de su nieto en su regazo. La brisa bajo el alero evocaba una pintura apacible. Aquella cabecita rebosaba asombro por el mundo exterior."
            },
            {
                "id": "#2",
                "hanzi": "在智能网联汽车的研发试验中，碰撞假人脑袋加速度传感器是测定被动安全防护等级的关键指标。工程师通过精确计算碰撞瞬间假人脑袋承受的动能冲击峰值，不断优化安全气囊点爆算法与吸能转向柱结构。",
                "pinyin": "Zài zhìnéng wǎnglián qìchē de yánfā shìyàn zhōng, pèngzhuàng jiǎrén nǎodai jiāsùdù chuángǎnqì shì cèdìng bèidòng ānquán fánghù děngjí de guānjiàn zhǐbiāo. Gōngchéngshī tōngguò jīngquè jìsuàn pèngzhuàng shùnjiān jiǎrén nǎodai chéngshòu de dòngnéng chōngjī fēngzhí, bùduàn yōuhuà ānquán qìnáng diǎnbào suànfǎ yǔ xīnén zhuǎnxiàngzhù jiégòu.",
                "en": "In crash testing for intelligent vehicles, crash dummy head acceleration sensors are key indicators measuring passive protection. By calculating impact peaks on the head, engineers optimize airbag deployment algorithms and steering columns.",
                "es": "En los ensayos automovilísticos de seguridad, los sensores de aceleración en la cabeza de los maniquíes miden la protección pasiva. Calcular el impacto recibido en la cabeza permite perfeccionar los algoritmos de los airbags y columnas de dirección."
            }
        ]
    },

    # 27 女士
    {
        "id": "27",
        "hanzi": "女士",
        "pinyin": "nǚ shì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "lady; Madam; Ms.; gentlewoman",
            "es": "señora; señorita; dama; distinguida dama"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Formal",
                "definition_en": "polite, respectful term of address or reference for an adult woman regardless of marital status",
                "definition_es": "tratamiento cortés y respetuoso para una mujer adulta independiente de su estado civil",
                "example_phrase": "女士们，先生们 (ladies and gentlemen)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在盛大的国际慈善晚宴开始前，主持人面带微笑走向舞台中央，礼貌地说道：“各位女士，各位先生，欢迎大家莅临。”",
                "pinyin": "Zài shèngdà de guójì císhàn wǎnyàn kāishǐ qián, zhǔchírén miàn dài wēixiào zǒuxiàng wǔtái zhōngyāng, lǐmào de shuōdào: “Gèwèi nǚshì, gèwèi xiānsheng, huānyíng dàjiā lìlín.”",
                "en": "Before the grand international charity banquet commenced, the host walked to center stage with a smile and politely announced: 'Ladies and gentlemen, welcome.'",
                "es": "Antes de iniciar la gala benéfica internacional, el presentador se acercó al escenario con una sonrisa diciendo con cortesía: 'Damas y caballeros, bienvenidos a todos'."
            },
            {
                "id": "#2",
                "hanzi": "这位享有盛誉的杰出女科学家荣获国家最高科学技术奖，成为首位获此殊荣的当代女性学者，社会各界称赞她是科学界的卓越女士。",
                "pinyin": "Zhè wèi xiǎngyǒu shèngyù de jiéchū nǚ kēxuéjiā rónghuò guójiā zuìgāo kējì jiǎng, chéngwéi shǒuwèi huò cǐ shūróng de dāngdài nǚxìng xuézhě, shèhuì gèjiè chēngzàn tā shì kēxuéjiè de zhuóyuè nǚshì.",
                "en": "This renowned female scientist won the State Preeminent Science and Technology Award, hailed by society as an outstanding lady of the scientific community.",
                "es": "Esta destacada científica obtuvo el máximo galardón tecnológico nacional, siendo aclamada por la sociedad como una dama insigne de la comunidad científica."
            }
        ],
        "collocations": [
            {"hanzi": "女士们先生们", "en": "ladies and gentlemen"},
            {"hanzi": "年轻女士", "en": "young lady"},
            {"hanzi": "女士优先", "en": "ladies first"},
            {"hanzi": "尊敬的女士", "en": "distinguished / respected lady"},
            {"hanzi": "职业女士", "en": "career woman / professional lady"},
            {"hanzi": "女士专区", "en": "ladies' exclusive section"}
        ],
        "idioms": [
            {"hanzi": "巾帼英雄", "pinyin": "jīn guó yīng xióng", "meaning_en": "heroine; female hero of great renown"},
            {"hanzi": "温文尔雅", "pinyin": "wēn wén ěr yǎ", "meaning_en": "gentle, cultivated, and refined in manner"},
            {"hanzi": "贤妻良母", "pinyin": "xián qī liáng mǔ", "meaning_en": "a good wife and loving mother; model matriarch"},
            {"hanzi": "大家闺秀", "pinyin": "dà jiā guī xiù", "meaning_en": "lady of noble birth; well-bred daughter of an eminent family"}
        ],
        "character_decomposition": [
            {
                "character": "女",
                "pinyin": "nǚ",
                "meaning_en": "woman; female; daughter",
                "meaning_es": "mujer; femenino; hija",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (pictogram of kneeling graceful woman)",
                "sound_component": "女 (inherent female phoneme)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of a woman kneeling demurely with arms crossed over her lap in ancient decorum.",
                "visual_mnemonic_story_en": "A graceful figure (女) kneels serenely with crossed sleeves, embodying feminine grace.",
                "visual_mnemonic_story_es": "Una figura esbelta (女) se arrodilla con serenidad y brazos cruzados, personificando la elegancia femenina.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "V",
                "traditional": '""'
            },
            {
                "character": "士",
                "pinyin": "shì",
                "meaning_en": "scholar; gentleman; warrior; cultivated person",
                "meaning_es": "erudito; caballero; letrado; persona culta",
                "radical": "士",
                "radical_meaning_en": "scholar / warrior",
                "meaning_component": "十 (ten/beginning) + 一 (one/completion)",
                "sound_component": "士 (inherent scholar sound)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Depicts one who knows matters from one to ten (一至十), designating an educated gentleman or scholar-warrior.",
                "visual_mnemonic_story_en": "A scholar stands tall with shoulders broader than the base (士), mastering knowledge.",
                "visual_mnemonic_story_es": "Un letrado erguido con hombros anchos (士) domina el saber desde el inicio al fin.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "J",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A woman (女) endowed with the honor and wisdom of a scholar (士) is addressed as an esteemed lady (女士).",
            "composite_memory_hook_es": "Una mujer (女) investida con la distinción y cultura de un letrado (士) recibe el honroso título de dama (女士).",
            "cultural_and_cognitive_roots": "Historically, 'shì' designated the educated gentry class. In modern Chinese diplomacy and civil society, pairing 'nǚ' with 'shì' elevated female address to universal parity with 'xiānsheng' (先生), honoring female dignity without marital distinction.",
            "tone_sandhi_and_pitch_modulation": "214-51 contour. The dipping 3rd tone of nǚ is pronounced as a half-3rd tone (21 low) before the crisp falling 4th tone of shì (51)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "土", "pinyin": "tǔ", "meaning_en": "soil; earth", "distinction_note": "Bottom horizontal stroke is longer than the top stroke, whereas in 士 top stroke is longer"},
                {"character": "干", "pinyin": "gān", "meaning_en": "do; dry", "distinction_note": "Top stroke is horizontal and vertical stroke extends through top"},
                {"character": "子", "pinyin": "zǐ", "meaning_en": "child", "distinction_note": "Has a curved hook and horizontal stroke; distinct from 女"},
                {"character": "刃", "pinyin": "rèn", "meaning_en": "blade edge", "distinction_note": "Different structure entirely"}
            ],
            "etymological_cognates": [
                {"character": "妇", "pinyin": "fù", "gloss_en": "married woman; matron"},
                {"character": "娘", "pinyin": "niáng", "gloss_en": "mother; young woman"},
                {"character": "贤", "pinyin": "xián", "gloss_en": "virtuous; worthy person"},
                {"character": "儒", "pinyin": "rú", "gloss_en": "Confucian scholar"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "女士 is a neutral, polite, and respectful formal address for an adult woman regardless of marital status.",
            "contrasts": [
                {"id": "1", "compared_word": "女士 vs. 夫人", "pinyin": "fūrén", "analysis": "夫人 is a high-register diplomatic or ceremonial term specifically indicating someone's wife (Madam/First Lady), whereas 女士 applies generally to any woman."},
                {"id": "2", "compared_word": "女士 vs. 小姐", "pinyin": "xiǎojiě", "analysis": "小姐 traditionally means Miss/unmarried woman, but can carry ambiguous or service-industry connotations in certain mainland contexts; 女士 is universally safe and respectful."},
                {"id": "3", "compared_word": "女士 vs. 太太", "pinyin": "tàitai", "analysis": "太太 is a colloquial or domestic term referring specifically to a married woman/wife, whereas 女士 ignores marital status entirely."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "她是一位优雅而从容的女士，无论岁月如何在眼角留下细纹，她的眼神始终澄澈而坚定。她用温和的言语化解生活中的龃龉，用坚韧的脊梁扛起家庭的担当。这种由内而外散发的从容风度，正是当代女性最动人的风采。",
                "pinyin": "Tā shì yí wèi yōuyǎ ér cóngróng de nǚshì, wúlùn suìyuè rúhé zài yǎnjiǎo liúxià xìwén, tā de yǎnshén shǐzhōng chéngchè ér jiāndìng. Tā yòng wēnhé de yányǔ huàjiě shēnghuó zhōng de jǔyǔ, yòng jiānrèn de jǐliáng kángqǐ jiātíng de dāndāng. Zhè zhǒng yóunèijíwài sànfā de cóngróng fēngdù, zhèng shì dāngdài nǚxìng zuì dòngrén de fēngcǎi.",
                "en": "She was an elegant and serene lady; no matter the fine lines carved by time, her gaze remained limpid and firm. She dissolved disputes with gentle words and carried family duties with resilience, radiating true modern feminine grace.",
                "es": "Era una dama elegante y serena; por más huellas que dejaran los años, su mirada permanecía diáfana y firme. Suavizaba desavenencias con palabras amables y sostenía al hogar con firmeza, personificando la templanza contemporánea."
            },
            {
                "id": "#2",
                "hanzi": "在联合国妇女署推动的可持续发展论坛上，多位杰出女性领袖就提高女性科技工作者话语权发表专题演讲。代表们指出，为女性科研人员消除职业晋升隐形壁垒，助力每一位卓越女士施展才华，是推动全球科技公平创新的重要基石。",
                "pinyin": "Zài Liánhéguó Fùnǚshǔ tuīdòng de kěchíxù fāzhǎn lùntán shàng, duō wèi jiéchū nǚxìng lǐngxiù jiù tígāo nǚxìng kējì gōngzuòzhě huàyǔquán fābiǎo zhuāntí yǎnjiǎng. Dàibiǎo men zhǐchū, wèi nǚxìng kēyán rényuán xiāochú zhíyè jìnshēng yǐnxíng bìlěi, zhùlì měi yí wèi zhuóyuè nǚshì shīzhǎn cáihuá, shì tuīdòng quánqiú kējì gōngpíng chuàngxīn de zhòngyào jīshí.",
                "en": "At the UN Women forum, female leaders delivered speeches on elevating female scientists' voice. Delegates stressed that dismantling career barriers and empowering ladies to display their talents constitute a cornerstone for equitable global innovation.",
                "es": "En el foro de ONU Mujeres, varias líderes intervinieron para fortalecer la voz de las científicas. Señalaron que derribar techos de cristal y apoyar el talento de cada dama investigadora es indispensable para la innovación equitativa global."
            }
        ]
    },

    # 28 叙述
    {
        "id": "28",
        "hanzi": "叙述",
        "pinyin": "xù shù",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to narrate; to recount; to relate; narration",
            "es": "narrar; relatar; contar; exponer; narración"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to relate, recount, or describe events or a sequence of actions in oral or written form",
                "definition_es": "relatar o exponer acontecimientos y hechos de forma ordenada, oral o escrita",
                "example_phrase": "详细叙述事情经过 (recount in detail what happened)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在警方的案情询问室里，目击证人喝了一口热水平复情绪后，开始清晰地叙述案发当晚所见到的全部情景。",
                "pinyin": "Zài jǐngfāng de ànqíng xùnwènshì lǐ, mùjī zhèngrén hē le yì kǒu rèshuǐ píngfù qíngxù hòu, kāishǐ qīngxī de xùshù ànfā dāngwǎn suǒ jiàndào de quánbù qíngjǐng.",
                "en": "In the police interrogation room, after sipping warm water to calm his nerves, the eyewitness began to clearly recount everything seen on the night of the crime.",
                "es": "En la sala policial, tras calmarse con un sorbo de agua tibia, el testigo comenzó a relatar con claridad todo lo que presenció la noche del suceso."
            },
            {
                "id": "#2",
                "hanzi": "这部历史文献长卷以宏阔的叙事笔触，详尽叙述了近代工商业家族在时代巨变波澜中的创业艰辛与命运起伏。",
                "pinyin": "Zhè bù lìshǐ wénxiàn chángjuàn yǐ hóngkuò de xùshì bǐchù, xiángjìn xùshù le jìndài gōngshāngyè jiāzú zài shídài jùbiàn bōlán zhōng de chuàngyè jiānxīn yǔ mìngyùn qǐfú.",
                "en": "With an expansive narrative brush, this historical documentary volume recounts in detail the entrepreneurial hardships and vicissitudes of a modern industrial family.",
                "es": "Con una prosa narrativa monumental, este volumen histórico relata minuciosamente las vicisitudes y afanes de un clan empresarial frente a los grandes cambios de la época."
            }
        ],
        "collocations": [
            {"hanzi": "详细叙述", "en": "recount in detail"},
            {"hanzi": "简要叙述", "en": "briefly narrate / summarize"},
            {"hanzi": "叙述经过", "en": "recount the process / course of events"},
            {"hanzi": "叙述事实", "en": "narrate facts"},
            {"hanzi": "叙述手法", "en": "narrative technique / device"},
            {"hanzi": "按时间顺序叙述", "en": "narrate in chronological order"}
        ],
        "idioms": [
            {"hanzi": "娓娓道来", "pinyin": "wěi wěi dào lái", "meaning_en": "narrate ceaselessly and charmingly; talk in an engaging flow"},
            {"hanzi": "长话短说", "pinyin": "cháng huà duǎn shuō", "meaning_en": "make a long story short"},
            {"hanzi": "平铺直叙", "pinyin": "píng pū zhí xù", "meaning_en": "straightforward and dull narration; tell a story without dramatic flair"},
            {"hanzi": "借题发挥", "pinyin": "jiè tí fā huī", "meaning_en": "seize upon an incident or topic to air one's own views"}
        ],
        "character_decomposition": [
            {
                "character": "叙",
                "pinyin": "xù",
                "meaning_en": "narrate; recount; chat; arrange in order",
                "meaning_es": "narrar; relatar; conversar; ordenar",
                "radical": "又",
                "radical_meaning_en": "again / hand",
                "meaning_component": "余 (surplus/self) + 又 (hand making marks)",
                "sound_component": "余 (yú, phonetic harmony)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Anciently depicted arranging building materials or genealogical lines in order (余/又), extended to sequential narration.",
                "visual_mnemonic_story_en": "A hand (又) neatly arranges leftover history scrolls (余) in sequence to narrate the chronicle.",
                "visual_mnemonic_story_es": "Una mano (又) ordena rollos históricos (余) de manera secuencial para relatar la crónica.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "ODNE",
                "traditional": "敘"
            },
            {
                "character": "述",
                "pinyin": "shù",
                "meaning_en": "recount; state; transmit; follow",
                "meaning_es": "relatar; exponer; transmitir; seguir",
                "radical": "辵",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walk/follow a path)",
                "sound_component": "术 (shù, technique/path)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Depicts walking along a defined path (辶/术) transmitting ancient ancestral traditions without invention.",
                "visual_mnemonic_story_en": "Stepping along the road (辶) using refined art and technique (术) to relate truth.",
                "visual_mnemonic_story_es": "Caminar por la senda (辶) aplicando el arte de la elocuencia (术) para relatar la verdad.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YID",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Arranging facts in order (叙) and tracking their path step by step (述) delivers a thorough narration (叙述).",
            "composite_memory_hook_es": "Ordenar los hechos en secuencia (叙) y seguir su curso paso a paso (述) logra una narración acabada (叙述).",
            "cultural_and_cognitive_roots": "Derived from the ancient historiographical dictum of Confucius: '述而不作，信而好古' (transmit, don't innovate; trust and love antiquity). 'Xùshù' embodies objective, faithful chronological reporting without fictional distortion.",
            "tone_sandhi_and_pitch_modulation": "51-51 pitch contour. Two crisp 4th tones; maintain falling contours on both syllables without slurring into a flat cadence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "斜", "pinyin": "xié", "meaning_en": "slanting; tilted", "distinction_note": "Features 斗 on the right instead of 又"},
                {"character": "途", "pinyin": "tú", "meaning_en": "way; route", "distinction_note": "Features 余 inside 辶 rather than 术"},
                {"character": "术", "pinyin": "shù", "meaning_en": "technique; art", "distinction_note": "Lacks the movement radical 辶"},
                {"character": "述", "pinyin": "shù", "meaning_en": "recount", "distinction_note": "Headword character itself"}
            ],
            "etymological_cognates": [
                {"character": "说", "pinyin": "shuō", "gloss_en": "speak; tell"},
                {"character": "讲", "pinyin": "jiǎng", "gloss_en": "explain; lecture"},
                {"character": "记", "pinyin": "jì", "gloss_en": "record; remember"},
                {"character": "陈", "pinyin": "chén", "gloss_en": "lay out; state"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "叙述 focuses on sequentially setting forth the development of an event or story in an orderly, objective manner.",
            "contrasts": [
                {"id": "1", "compared_word": "叙述 vs. 描写", "pinyin": "miáoxiě", "analysis": "叙述 recounts chronological progression of events (what happened), whereas 描写 paints vivid sensory impressions, scenery, or facial expressions (how it looked)."},
                {"id": "2", "compared_word": "叙述 vs. 说明", "pinyin": "shuōmíng", "analysis": "说明 explains concepts, principles, rules, or instructions, whereas 叙述 chronicles temporal sequences of incidents."},
                {"id": "3", "compared_word": "叙述 vs. 议论", "pinyin": "yìlùn", "analysis": "议论 expresses viewpoints, arguments, and commentary, whereas 叙述 establishes narrative facts."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "文学的魅力往往在于如何叙述时光的流逝。优秀的作家不需要浮夸的辞藻，只需用沉静克制的语言，将普通人在命运沉浮中的欢笑与泪水娓娓道来。这种真实的叙述，往往比虚构的戏剧更能震撼心灵。",
                "pinyin": "Wénxué de mèilì wǎngwǎng zài yú rúhé xùshù shíguāng de liúshì. Yōuxiù de zuòjiā bù xūyào fúkuā de cízǎo, zhǐ xū yòng chénjìng kèzhì de yǔyán, jiāng pǔtōngrén zài mìngyùn chénfú zhōng de huānxiào yǔ lèishuǐ wěiwěidàolái. Zhè zhǒng zhēnshí de xùshù, wǎngwǎng bǐ xūgòu de xìjù gèng néng zhènhàn xīnlíng.",
                "en": "The charm of literature lies in how it recounts the passage of time. Master writers need no bombast; with serene language they relate ordinary people's joy and tears amid fate's tides. Such authentic narration touches souls deeply.",
                "es": "El encanto de la literatura radica en cómo relata el transcurso del tiempo. Los grandes autores no precisan artificios; con lenguaje sobrio desgranan las alegrías y llantos cotidianos. Esta narración auténtica conmueve el alma con hondura."
            },
            {
                "id": "#2",
                "hanzi": "在司法审判实践中，案件事实的客观叙述是法官准确适用法律裁判的前提。当事人陈述若出现逻辑断裂或自相矛盾，审判人员需通过多方举证质证，排除非理性情绪干扰，还原清晰可靠的案发事实链条。",
                "pinyin": "Zài sīfǎ shěnpàn shíjiàn zhōng, ànjiàn shìshí de kèguān xùshù shì fǎguān zhǔnquè shìyòng fǎlǜ cáipàn de qiántí. Dāngshìrén chénshù ruò chūxiàn luójí duànliè huò zìxiāngmáodùn, shěnpàn rényuán xū tōngguò duōfāng jǔzhèng zhìzhèng, páichú fēilǐxìng qíngxù gānrǎo, huányuán qīngxī kěkào de ànfā shìshí liàntiáo.",
                "en": "In judicial adjudication, objective narration of case facts is the prerequisite for accurate application of law. When testimonies show contradictions, judges cross-examine evidence to eliminate emotion and reconstruct facts.",
                "es": "En la práctica judicial, el relato objetivo de los hechos es el presupuesto indispensable para aplicar la ley con justicia. Si los testimonios incurren en contradicciones, los jueces contrastan pruebas para reconstruir la cadena fáctica verídica."
            }
        ]
    },

    # 29 居然
    {
        "id": "29",
        "hanzi": "居然",
        "pinyin": "jū rán",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "unexpectedly; to one's surprise; actually; go so far as to",
            "es": "inesperadamente; para sorpresa de uno; sorprendentemente; llegar al colmo de"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "expressing that something happened contrary to expectation, surprising the speaker",
                "definition_es": "expresa que un hecho ocurre en contra de lo esperado causando asombro",
                "example_phrase": "他居然考了第一名 (to everyone's surprise, he actually came in first)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "原本天气预报说今天全天都有大暴雨，没想到午后居然放晴了，天边甚至挂起了一道绚丽的彩虹。",
                "pinyin": "Yuánběn tiānqì yùbào shuō jīntiān quántiān dōu yǒu dà bàoyǔ, méi xiǎngdào wǔhòu jūrán fàngqíng le, tiānbiān shènzhì guàqǐ le yí dào xuànlì de cǎihóng.",
                "en": "The weather forecast had predicted heavy torrential downpours all day, but to our surprise it actually cleared up in the afternoon, with a gorgeous rainbow appearing.",
                "es": "El pronóstico del tiempo anunciaba tormentas todo el día, pero para sorpresa de todos, por la tarde escampó e incluso apareció un hermoso arcoíris."
            },
            {
                "id": "#2",
                "hanzi": "在完全没有外部战略投资扶持的艰难处境下，这家初创人工智能企业居然在短短两年内实现了关键芯片算法的量产突破。",
                "pinyin": "Zài wánquán méiyǒu wàibù zhànlüè tóuzī fúchí de jiānnán chǔjìng xià, zhè jiā chūchuàng réngōng zhìnéng qǐyè jūrán zài duǎnduǎn liǎng nián nèi shíxiàn le guānjiàn xīnpiàn suànfǎ de liàngchǎn tūpò.",
                "en": "In the arduous situation of lacking external venture capital, this AI startup unexpectedly achieved mass-production breakthroughs in key algorithms within two years.",
                "es": "En medio de una difícil situación sin inversión externa, esta empresa emergente de inteligencia artificial logró sorprendentemente avances clave de producción en dos años."
            }
        ],
        "collocations": [
            {"hanzi": "居然是他", "en": "unexpectedly, it was him"},
            {"hanzi": "居然做到了", "en": "actually managed to achieve it"},
            {"hanzi": "没想到居然", "en": "never expected that unexpectedly..."},
            {"hanzi": "居然会发生", "en": "could actually happen against all odds"},
            {"hanzi": "居然敢", "en": "actually have the nerve to"},
            {"hanzi": "居然不知道", "en": "actually did not even know"}
        ],
        "idioms": [
            {"hanzi": "意料之外", "pinyin": "yì liào zhī wài", "meaning_en": "beyond all expectations; completely surprising"},
            {"hanzi": "出人意料", "pinyin": "chū rén yì liào", "meaning_en": "exceeding people's expectations; surprise everyone"},
            {"hanzi": "安居乐业", "pinyin": "ān jū lè yè", "meaning_en": "live in peace and work happily"},
            {"hanzi": "理所当然", "pinyin": "lǐ suǒ dāng rán", "meaning_en": "take it as natural; matters following natural logic"}
        ],
        "character_decomposition": [
            {
                "character": "居",
                "pinyin": "jū",
                "meaning_en": "dwell; reside; occupy; sit still",
                "meaning_es": "residir; habitar; ocupar; estar sentado",
                "radical": "尸",
                "radical_meaning_en": "corpse / body posture",
                "meaning_component": "尸 (seated body posture)",
                "sound_component": "古 (gǔ, old/stable phonetics)",
                "stroke_count": 8,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Depicts a person resting in a settled seated position (尸) in an ancient dwelling (古), conveying resting firmly.",
                "visual_mnemonic_story_en": "A person rests settled inside a sheltered shelter (尸) atop ancient foundations (古).",
                "visual_mnemonic_story_es": "Una persona reposa instalada bajo techo (尸) sobre cimientos ancestrales (古).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "SJLR",
                "traditional": '""'
            },
            {
                "character": "然",
                "pinyin": "rán",
                "meaning_en": "so; like this; suffix forming adverbs",
                "meaning_es": "así; de este modo; sufijo adverbial",
                "radical": "灬",
                "radical_meaning_en": "fire",
                "meaning_component": "灬 (fire flames burning)",
                "sound_component": "肰 (rán, dog meat roasted)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Originally depicted roasting meat over fire (灬), borrowed phonetically as an adverbial suffix meaning 'in such a manner'.",
                "visual_mnemonic_story_en": "Flames of fire (灬) blaze brightly, demonstrating things happening visibly in this manner (然).",
                "visual_mnemonic_story_es": "Llamas de fuego (灬) arden vivas, mostrando con claridad que las cosas ocurren de este modo (然).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BKF",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Something quietly sitting in the background (居) turns out in this unexpected state (然) to everyone's amazement.",
            "composite_memory_hook_es": "Algo que permanecía en reposo aparente (居) se revela de este modo asombroso (然) para sorpresa de todos.",
            "cultural_and_cognitive_roots": "Originally conveyed 'sitting calmly in such a state' in classical prose; evolved by contrastive pragmatics to describe startling events where reality defies subjective expectation.",
            "tone_sandhi_and_pitch_modulation": "55-35 pitch contour. A high flat 1st tone (55) on jū steps cleanly down then rises smoothly with rán (35)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "据", "pinyin": "jù", "meaning_en": "according to; basis", "distinction_note": "Has hand radical 扌 on the left instead of 居 alone"},
                {"character": "剧", "pinyin": "jù", "meaning_en": "drama; fierce", "distinction_note": "Features knife radical 刂 on the right of 居"},
                {"character": "燃", "pinyin": "rán", "meaning_en": "burn; ignite", "distinction_note": "Has additional fire radical 火 on the left side of 然"},
                {"character": "烈", "pinyin": "liè", "meaning_en": "intense; fiery", "distinction_note": "Features 列 above 灬 instead of 肰"}
            ],
            "etymological_cognates": [
                {"character": "竟", "pinyin": "jìng", "gloss_en": "unexpectedly; in the end"},
                {"character": "竟", "pinyin": "jìng", "gloss_en": "synonym root marker"},
                {"character": "俄", "pinyin": "é", "gloss_en": "suddenly; unexpectedly"},
                {"character": "忽", "pinyin": "hū", "gloss_en": "suddenly; abruptly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "居然 emphasizes that an event occurred completely contrary to reasonable expectation, carrying surprise, marvel, or disbelief.",
            "contrasts": [
                {"id": "1", "compared_word": "居然 vs. 竟然", "pinyin": "jìngrán", "analysis": "Both indicate surprise, but 竟然 often carries stronger emotional tone (often indignation or severe shock), whereas 居然 can convey delightful pleasant surprise or neutral amazement."},
                {"id": "2", "compared_word": "居然 vs. 果然", "pinyin": "guǒrán", "analysis": "居然 is contrary to expectations (unexpected surprise), whereas 果然 indicates that reality exactly matches prior predictions (as expected)."},
                {"id": "3", "compared_word": "居然 vs. 突然", "pinyin": "tūrán", "analysis": "突然 describes rapid, unexpected temporal onset ('suddenly'), whereas 居然 highlights cognitive contrast with psychological expectations."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "命运常常在不经意间峰回路转。在经历了无数次被拒之门外的沮丧后，青年在几乎放弃希望的清晨，居然收到了国际顶尖学府全额奖学金的录取通知书。那一刻，曾经流过的所有泪水，都化作了不可思议的奇迹。",
                "pinyin": "Mìngyùn chángcháng zài bùjīngyì jiān fēnghuílùzhuǎn. Zài jīnglì le wúshù cì bèi jù zhī ménwài de jǔsàng hòu, qīngnián zài jīhū fàngqì xīwàng de qīngchén, jūrán shōudào le guójì dǐngjiān xuéfǔ quán'é jiǎngxuéjīn de lùqǔ tōngzhīshū. Nà yí kè, céngjīng liúguò de suǒyǒu lèishuǐ, dōu huàzuò le bùkěsīyì de qíjì.",
                "en": "Fate often takes unexpected turns when least anticipated. After experiencing endless rejections, on a morning when he nearly surrendered hope, the youth unexpectedly received a full-scholarship admission letter, turning tears into miracles.",
                "es": "El destino suele dar giros asombrosos en los momentos menos previstos. Tras innumerables rechazos, cuando casi se daba por vencido, el joven recibió para su sorpresa una carta de admisión con beca completa, trocando lágrimas en un milagro."
            },
            {
                "id": "#2",
                "hanzi": "在极度干旱贫瘠的戈壁深处，生态科考队员居然发现了一片生机勃勃的珍稀濒危灌木群落。依托深层地下水脉的微循环补给，这片绿洲在极端气候中顽强存续了数百年，为全球荒漠化治理研究提供了不可多得的生态样本。",
                "pinyin": "Zài jídù gānhàn pínjí de gēbì shēnchù, shēngtài kěkǎo duìyuán jūrán fāxiàn le yí piàn shēngjībóbó de zhēnxī bīnwēi guānmù qúnluò. Yītuō shēncéng dìxiàshuǐ mài de wēi xúnhuán bǔjǐ, zhè piàn lǜzhōu zài jíduān qìhòu zhōng wánqiáng cúnxù le shù bǎi nián, wèi quánqiú huāngmòhuà zhìlǐ yánjiū tígōng le bùkěduōdé de shēngtài yàngběn.",
                "en": "Deep in the arid Gobi, ecological researchers surprisingly discovered a thriving community of endangered shrubs. Sustained by deep aquifer micro-cycles, this oasis endured extreme climate for centuries, offering an invaluable sample for desertification studies.",
                "es": "En las profundidades del desierto árido, los ecólogos descubrieron sorprendentemente una comunidad viva de arbustos en peligro de extinción. Nutridos por corrientes subterráneas, este oasis pervivió siglos aportando un modelo clave contra la desertificación."
            }
        ]
    },

    # 30 催
    {
        "id": "30",
        "hanzi": "催",
        "pinyin": "cuī",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to urge; to hurry; to press; to hasten; to prompt",
            "es": "apurar; apremiar; apresurar; urgir; instar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to urge or press someone to act or finish something faster",
                "definition_es": "apremiar o instar a alguien a actuar o completar una tarea con prisa",
                "example_phrase": "催他快走 (urge him to hurry up)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to hasten, induce, or stimulate a natural or chemical process",
                "definition_es": "acelerar o inducir un proceso biológico o químico",
                "example_phrase": "催熟水果 (ripen fruits artificially)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "眼看校车马上就要到小区门口了，妈妈站在玄关一边帮弟弟整理书包，一边不停催他快点穿鞋。",
                "pinyin": "Yǎnkàn xiàochē mǎshàng jiù yào dào xiǎoqū ménkǒu le, māma zhàn zài xuánguān yìbiān bāng dìdi zhěnglǐ shūbāo, yìbiān bùtíng cuī tā kuài diǎn chuān xié.",
                "en": "Seeing that the school bus was arriving at the neighborhood gate, mother stood by the foyer helping brother pack his bag while constantly urging him to put on his shoes.",
                "es": "Al ver que el autobús escolar casi llegaba a la puerta, mamá ayudaba a mi hermano con la mochila en el recibidor mientras le apuraba sin parar para que se calzara."
            },
            {
                "id": "#2",
                "hanzi": "面对供应链核心零部件交货延期风险，项目总监亲自向主要供应商派出督导组，现场催促产能释放并紧盯交付节点。",
                "pinyin": "Miànduì gōngyìngliàn héxīn língbùjiàn jiāohuò yánqī fēngxiǎn, xiàngmù zǒngjiān qīnzì xiàng zhǔyào gōngyìngshāng pàichū dūdǎozǔ, xiànchǎng cuīcù chǎnnéng shìfàng bìng jǐndīng jiāofù jiédiǎn.",
                "en": "Facing delivery delay risks for critical supply chain parts, the project director dispatched a supervisor team to suppliers to urge capacity ramp-up and track delivery milestones.",
                "es": "Ante el riesgo de demora en componentes clave, el director del proyecto envió supervisores a los proveedores para apremiar la producción y asegurar los plazos."
            }
        ],
        "collocations": [
            {"hanzi": "催促进度", "en": "urge progress on a schedule"},
            {"hanzi": "催交作业", "en": "press to submit homework"},
            {"hanzi": "催款", "en": "press for payment of debts"},
            {"hanzi": "催眠", "en": "hypnotize; induce sleep"},
            {"hanzi": "催熟", "en": "accelerate ripening"},
            {"hanzi": "催人奋进", "en": "urge people onward to strive"}
        ],
        "idioms": [
            {"hanzi": "催人泪下", "pinyin": "cuī rén lèi xià", "meaning_en": "moving one to tears; poignant and tear-inducing"},
            {"hanzi": "羯鼓催花", "pinyin": "jié gǔ cuī huā", "meaning_en": "beating drums to hasten flower blossoms; eager impatience"},
            {"hanzi": "星夜兼程", "pinyin": "xīng yè jiān chéng", "meaning_en": "travel night and day by star light; hurry through journey"},
            {"hanzi": "雷厉风行", "pinyin": "léi lì fēng xíng", "meaning_en": "vigorously and swiftly as thunder and wind"}
        ],
        "character_decomposition": [
            {
                "character": "催",
                "pinyin": "cuī",
                "meaning_en": "urge; press; hurry; hasten",
                "meaning_es": "apurar; apremiar; apresurar; instar",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person prodding/urging)",
                "sound_component": "崔 (cuī, steep high mountain)",
                "stroke_count": 13,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing person (亻) with steep crag (崔), conveying pressing someone forward as if climbing a steep slope.",
                "visual_mnemonic_story_en": "A guide (亻) urgently prods climbers up a steep mountain crag (崔) before sunset.",
                "visual_mnemonic_story_es": "Un guía (亻) apremia a los montañistas para que asciendan el risco escarpado (崔) antes del anochecer.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OUOG",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A person (亻) pushing you up a towering, precipitous mountain (崔) embodies being hurried and urged forward (催).",
            "composite_memory_hook_es": "Una persona (亻) que te empuja a subir una montaña empinada (崔) representa estar siendo apurado y apremiado (催).",
            "cultural_and_cognitive_roots": "Associated in Chinese poetry with seasonal urgency ('春风催新绿', spring breezes prompt fresh green) as well as the urgency of official tax collectors or military drums driving soldiers into battle.",
            "tone_sandhi_and_pitch_modulation": "55 pitch contour. A high, steady 1st tone (55); keep the onset crisp and sustained without dipping."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "璀", "pinyin": "cuǐ", "meaning_en": "resplendent; luster of jade", "distinction_note": "Features jade radical 王 on the left instead of person 亻"},
                {"character": "摧", "pinyin": "cuī", "meaning_en": "destroy; break", "distinction_note": "Features hand radical 扌 on the left instead of person 亻"},
                {"character": "崔", "pinyin": "cuī", "meaning_en": "lofty mountain; surname", "distinction_note": "The phonetic stem without the left person radical 亻"},
                {"character": "维", "pinyin": "wéi", "meaning_en": "maintain; dimension", "distinction_note": "Has silk radical 纟 on the left instead of person 亻"}
            ],
            "etymological_cognates": [
                {"character": "赶", "pinyin": "gǎn", "gloss_en": "rush; hurry"},
                {"character": "督", "pinyin": "dū", "gloss_en": "supervise; urge forward"},
                {"character": "迫", "pinyin": "pò", "gloss_en": "compel; press"},
                {"character": "促", "pinyin": "cù", "gloss_en": "hasten; promote"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "催 focuses on verbally or operationally pressing someone to accelerate their pace and finish promptly.",
            "contrasts": [
                {"id": "1", "compared_word": "催 vs. 赶", "pinyin": "gǎn", "analysis": "赶 focuses on accelerating one's own physical movement to catch a vehicle or meet a deadline (e.g., 赶时间, 赶火车), whereas 催 is transitive, pressing another person to act faster."},
                {"id": "2", "compared_word": "催 vs. 促", "pinyin": "cù", "analysis": "促 is more formal/written, denoting facilitating or catalyzing broad trends (e.g., 促进, 督促), whereas 催 is direct spoken prompting (e.g., 催促, 别催了)."},
                {"id": "3", "compared_word": "催 vs. 逼", "pinyin": "bī", "analysis": "逼 implies coercive intimidation, cornering, or extortion without choice, whereas 催 is urging speed and timeliness."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活总是催促着人们匆匆赶路，早晨急促的闹钟，地铁里拥挤的脚步，都在无声地催促着我们向前奔跑。然而，偶尔放慢脚步，听听路边清脆的鸟鸣，看看花开的姿态，才能让疲惫的灵魂重新找回宁静的归宿。",
                "pinyin": "Shēnghuó zǒngshì cuīcù zhe rénmen cōngcōng gǎnlù, zǎochen jícù de nàozhōng, dìtiě lǐ yōngjǐ de jiǎobù, dōu zài wúshēng de cuīcù zhe wǒmen xiàngqián bēnpǎo. Rán'ér, ǒu'ěr fàngmàn jiǎobù, tīngting lùbiān qīngcuì de niǎomíng, kànkan huākāi de zītài, cáinǐng ràng píbèi de línghún chóngxīn zhǎohuí níngjìng de guīsù.",
                "en": "Life constantly urges people onward in haste: buzzing alarm clocks and rushed subway steps push us forward silently. Yet slowing down occasionally to hear birds chirping and view flowers allows weary souls to reclaim peaceful havens.",
                "es": "La vida nos apremia a correr deprisa: el despertador matutino y los pasos apresurados en el metro nos empujan en silencio. Sin embargo, frenar el paso para escuchar el canto de las aves y contemplar las flores devuelve la paz al alma fatigada."
            },
            {
                "id": "#2",
                "hanzi": "在现代敏捷项目开发流程中，项目经理通过看板系统实时监控研发瓶颈。当某一核心功能模块出现交付滞后风险时，项目组需及时组织跨部门资源会商，通过梳理阻塞节点替代盲目催促进度，以确保系统按期高质量交付。",
                "pinyin": "Zài xiàndài mǐnjié xiàngmù kāifā liúchéng zhōng, xiàngmù jīnglǐ tōngguò kànbǎn xìtǒng shíshí jiānkòng yánfā píngjǐng. Dāng mǒu yí héxīn gōngnéng mókuài chūxiàn jiāofù zhìhòu fēngxiǎn shí, xiàngmùzǔ xū jíshí zǔzhī kuà bùmén zīyuán huìshāng, tōngguò shūlǐ zǔsè jiédiǎn tìdài mángmù cuīcù jìndù, yǐ quèbǎo xìtǒng ànqī gāozhìliàng jiāofù.",
                "en": "In agile development workflows, project managers monitor bottlenecks via Kanban systems. When module delays arise, teams coordinate cross-functional resources to unblock bottlenecks rather than blindly rushing schedules, ensuring quality.",
                "es": "En el desarrollo ágil de proyectos, los directores supervisan cuellos de botella con tableros Kanban. Al surgir retrasos en módulos clave, se coordinan recursos para despejar trabas en vez de apremiar a ciegas, asegurando entregas de calidad."
            }
        ]
    }
]

if __name__ == '__main__':
    for w in words_batch6:
        save_word(w)

from core.toon_builder import save_word

words_batch7 = [
    # 31 等待
    {
        "id": "31",
        "hanzi": "等待",
        "pinyin": "děng dài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to wait for; to await; wait; expectation",
            "es": "esperar; aguardar; espera; expectativa"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to stay in a place or state expecting a person, event, or condition to occur",
                "definition_es": "permanecer a la espera de que ocurra una persona, acontecimiento o estado",
                "example_phrase": "耐心等待 (wait patiently)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在漫天飘雪的冬夜，母亲站在老屋檐下，搓着冰凉的双手，静静等待着远方归家的游子。",
                "pinyin": "Zài màntiān piāoxuě de dōngyè, mǔqīn zhàn zài lǎo wūyán xià, cuō zhe bīngliáng de shuāngshǒu, jìngjìng děngdài zhe yuǎnfāng guījiā de yóuzǐ.",
                "en": "On a winter night with snowflakes swirling through the sky, mother stood under the old eaves, rubbing cold hands, quietly waiting for her traveler returning home from afar.",
                "es": "En una noche invernal bajo la nieve, la madre aguardaba bajo el alero de la casa, frotándose las manos frías mientras esperaba al hijo que volvía del lejano hogar."
            },
            {
                "id": "#2",
                "hanzi": "经过长达八个月的临床试验数据审评，创新抗癌靶向药物研发团队终于拿到了国家药品监督管理局批准上市的决定，结束了漫长焦灼的等待。",
                "pinyin": "Jīngguò chángdá bā gè yuè de línchuáng shíyàn shùjù shěnpíng, chuàngxīn kàng'ái bǎxiàng yàowù yánfā tuánduì zhōngyú ná dào le Guójiā Yàopǐn Jiāndǔ Guǎnlǐjú pīzhǔn shàngshì de juédìng, jiéshù le màncháng jiāozhuó de děngdài.",
                "en": "After eight months of clinical trial data evaluation, the innovative targeted cancer drug R&D team finally received the marketing approval decision from the medical administration, ending their long and anxious wait.",
                "es": "Tras ocho meses de rigurosa evaluación de datos clínicos, el equipo del fármaco oncológico obtuvo por fin la autorización oficial de comercialización, concluyendo una prolongada y tensa espera."
            }
        ],
        "collocations": [
            {"hanzi": "耐心等待", "en": "wait patiently"},
            {"hanzi": "漫长等待", "en": "long wait"},
            {"hanzi": "焦急等待", "en": "wait anxiously"},
            {"hanzi": "等待时机", "en": "await an opportune moment"},
            {"hanzi": "等待结果", "en": "wait for the result"},
            {"hanzi": "静静等待", "en": "wait in quiet silence"}
        ],
        "idioms": [
            {"hanzi": "拭目以待", "pinyin": "shì mù yǐ dài", "meaning_en": "wipe one's eyes and wait; wait and see with high anticipation"},
            {"hanzi": "严阵以待", "pinyin": "yán zhèn yǐ dài", "meaning_en": "stand in battle array awaiting the enemy; ready for action"},
            {"hanzi": "守株待兔", "pinyin": "shǒu zhū dài tù", "meaning_en": "stand by a tree stump waiting for rabbits; wait idly for windfalls"},
            {"hanzi": "翘首以待", "pinyin": "qiáo shǒu yǐ dài", "meaning_en": "crane one's neck in eager anticipation"}
        ],
        "character_decomposition": [
            {
                "character": "等",
                "pinyin": "děng",
                "meaning_en": "wait; equal; rank; class",
                "meaning_es": "esperar; igual; rango; clase",
                "radical": "竹",
                "radical_meaning_en": "bamboo",
                "meaning_component": "竹 (bamboo slats for ranking/weighing)",
                "sound_component": "寺 (sì, temple/official court)",
                "stroke_count": 12,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing bamboo tallies (竹) with imperial office (寺), anciently denoting classifying equal ranks on tallies, extended to pausing/waiting.",
                "visual_mnemonic_story_en": "Bamboo measurement slips (竹) are stacked in the hall (寺) until records are verified.",
                "visual_mnemonic_story_es": "Varillas de bambú (竹) aguardan apiladas en el tribunal (寺) hasta certificar los registros.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "HGDI",
                "traditional": '""'
            },
            {
                "character": "待",
                "pinyin": "dài",
                "meaning_en": "wait; treat; stay; about to",
                "meaning_es": "esperar; aguardar; tratar; quedarse",
                "radical": "彳",
                "radical_meaning_en": "step / walk slowly",
                "meaning_component": "彳 (step pausing on road)",
                "sound_component": "寺 (sì, court/stopping point)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Depicts halting one's steps (彳) at an official post (寺) awaiting orders.",
                "visual_mnemonic_story_en": "Halting footsteps (彳) outside the sanctuary gate (寺) to wait patiently for arrival.",
                "visual_mnemonic_story_es": "Detener el paso (彳) ante el umbral (寺) para esperar pacientemente la llegada.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HOGDI",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Halting with bamboo tallies (等) and pausing your steps (待) to let time unfold creates patient waiting.",
            "composite_memory_hook_es": "Contar los días como varillas (等) y frenar el paso (待) para dar tiempo al tiempo constituye la serena espera.",
            "cultural_and_cognitive_roots": "Both characters share the courtly/temple root '寺' (sì); ancient Chinese view of waiting was not passive paralysis but disciplined temporal incubation ('待时而动', biding one's time until heaven's moment arrives).",
            "tone_sandhi_and_pitch_modulation": "214-51 contour. The 3rd tone of děng is pronounced as a half-3rd tone (21 low) before the crisp falling 4th tone of dài (51)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "持", "pinyin": "chí", "meaning_en": "hold; grasp", "distinction_note": "Features hand radical 扌 on the left instead of step 彳"},
                {"character": "特", "pinyin": "tè", "meaning_en": "special", "distinction_note": "Features ox radical 牛 on the left instead of step 彳"},
                {"character": "诗", "pinyin": "shī", "meaning_en": "poetry; verse", "distinction_note": "Features speech radical 讠 on the left with 寺"},
                {"character": "符", "pinyin": "fú", "meaning_en": "tally; symbol", "distinction_note": "Features bamboo radical 竹 over 付 instead of 寺"}
            ],
            "etymological_cognates": [
                {"character": "候", "pinyin": "hòu", "gloss_en": "wait; expect season"},
                {"character": "盼", "pinyin": "pàn", "gloss_en": "long for; look expectantly"},
                {"character": "停", "pinyin": "tíng", "gloss_en": "stop; halt steps"},
                {"character": "守", "pinyin": "shǒu", "gloss_en": "guard; keep watch"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "等待 denotes spending time in a steady state anticipation of an event, person, or result to materialize.",
            "contrasts": [
                {"id": "1", "compared_word": "等待 vs. 等候", "pinyin": "děnghòu", "analysis": "等候 is more specific to physical waiting in a dedicated area (e.g., 在候车室等候), whereas 等待 encompasses deep psychological and temporal anticipation (e.g., 等待时机, 等待奇迹)."},
                {"id": "2", "compared_word": "等待 vs. 期盼", "pinyin": "qīpàn", "analysis": "期盼 emphasizes strong yearning and subjective eagerness, whereas 等待 is an objective state of passing time."},
                {"id": "3", "compared_word": "等待 vs. 逗留", "pinyin": "dòuliú", "analysis": "逗留 means staying or lingering at a geographic destination during travel, unrelated to expecting future results."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生命中许多美好的事物，都值得我们耐心地等待。春天的花开，秋天的硕果，都需要经过风霜雨雪的漫长孕育。学会学会在浮躁的尘世中平静等待，不是消极怠工，而是在时光深处积蓄破土而出的蓬勃生机。",
                "pinyin": "Shēngmìng zhōng xǔduō měihǎo de shìwù, dōu zhídé wǒmen nàixīn de děngdài. Chūntiān de huākāi, qiūtiān de shuòguǒ, dōu xūyào jīngguò fēngshuāngyǔxuě de màncháng yùnyù. Xuéhuì zài fúzào de chénshì zhōng píngjìng děngdài, bú shì xiāojí dàigōng, érshì zài shíguāng shēnchù jīxù pòtǔ'érchū de péngbó shēngjī.",
                "en": "Many wonders of life are worth waiting for patiently. Spring flowers and autumn fruit demand long maturation through wind and frost. Learning to wait with serenity amidst turmoil is not passive surrender, but gathering vitality to burst forth.",
                "es": "Muchas maravillas de la vida merecen una paciente espera. Las flores primaverales y los frutos de otoño maduran tras largos fríos. Aprender a aguardar con serenidad no es pasividad, sino acumular la fuerza vital necesaria para brotar."
            },
            {
                "id": "#2",
                "hanzi": "在现代宏观经济资本运作与长周期产业投资领域，秉持耐心资本理念是穿越行业周期的关键。面对底层硬核技术的漫长研发周期，投资机构唯有经得起时间等待，摒弃短期投机套利冲动，才能分享战略产业自主创新的丰厚红利。",
                "pinyin": "Zài xiàndài hóngguān jīngjì zīběn yùnzuò yǔ chángzhōuqī chǎnyè tóuzī lǐngyù, bǐngchí nàixīn zīběn lǐniàn shì chuānyuè hángyè zhōuqī de guānjiàn. Miànduì dǐcéng yìnghé jìshù de màncháng yánfā zhōuqī, tóuzī jīgòu wéiyǒu jīngdéqǐ shíjiān děngdài, bìngqì duǎnqī tóujī tàolì chōngdòng, cáinǐng fēnxiǎng zhànlüè chǎnyè zìzhǔ chuàngxīn de fēnghòu hónglì.",
                "en": "In long-cycle industrial investment, patient capital philosophy is vital to traversing economic cycles. Facing lengthy R&D timelines for foundational technology, investors who endure the wait and reject speculation reap innovation dividends.",
                "es": "En la inversión industrial a largo plazo, el capital paciente permite atravesar los ciclos económicos. Frente a la prolongada gestación de las tecnologías de base, los inversores capaces de esperar sin especular cosechan los frutos de la innovación."
            }
        ]
    },

    # 32 蚊子
    {
        "id": "32",
        "hanzi": "蚊子",
        "pinyin": "wén zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "mosquito; biting gnat",
            "es": "mosquito; zancudo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a small slender dipteran insect with piercing mouthparts, the female of which bites and sucks blood",
                "definition_es": "insecto díptero pequeño de piezas bucales punzantes cuya hembra pica para succionar sangre",
                "example_phrase": "消灭蚊子 (eradicate mosquitoes)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "夏天夜里在院子里乘凉时，如果不点燃盘装蚊香或喷洒防蚊花露水，手臂上很容易被可恶的蚊子叮出好几个红肿的大包。",
                "pinyin": "Xiàtiān yèlǐ zài yuànzi lǐ chéngliáng shí, rúguǒ bù diǎnrán pánzhuāng wénxiāng huò pēnsǎ fángwén huālùshuǐ, shǒubì shàng hěn róngyì bèi kě'wù de wénzi dīng chū hǎojǐ gè hóngzhǒng de dàbāo.",
                "en": "When enjoying the cool evening in the courtyard during summer, unless one lights a mosquito coil or sprays repellent, arms easily get bitten by pesky mosquitoes into red swollen welts.",
                "es": "Al tomar el fresco nocturno en el patio durante el verano, si no se enciende repelente o espirales, los molestos mosquitos acaban acribillando los brazos de ronchas rojas."
            },
            {
                "id": "#2",
                "hanzi": "热带公共卫生疾病控制专家多次警告，伊蚊等特定种类的蚊子是登革热、疟疾和寨卡病毒等急性传染病跨区域扩散的关键媒介。",
                "pinyin": "Rèdài gōnggòng wèishēng jíbìng kòngzhì zhuānjiā duō cì jǐnggào, yīwén děng tèdìng zhǒnglèi de wénzi shì dēnggérè, nüèjí hé zhàikǎ bìngdú děng jíxìng chuánrǎnbìng kuà qūyù kuòsàn de guānjiàn méijiè.",
                "en": "Tropical public health disease control experts have repeatedly warned that specific mosquito species like Aedes are crucial vectors spreading acute infectious diseases such as dengue, malaria, and Zika.",
                "es": "Expertos en salud pública advierten de que ciertas especies de mosquitos como el Aedes son vectores biológicos clave en la propagación de enfermedades como el dengue, la malaria y el zika."
            }
        ],
        "collocations": [
            {"hanzi": "蚊子叮咬", "en": "mosquito bites"},
            {"hanzi": "驱赶蚊子", "en": "repel / drive away mosquitoes"},
            {"hanzi": "消灭蚊子", "en": "exterminate mosquitoes"},
            {"hanzi": "蚊子幼虫", "en": "mosquito larvae / wrigglers"},
            {"hanzi": "蚊子叫声", "en": "whining / buzzing of mosquitoes"},
            {"hanzi": "招蚊子", "en": "attract mosquitoes"}
        ],
        "idioms": [
            {"hanzi": "聚蚊成雷", "pinyin": "jù wén chéng léi", "meaning_en": "a swarm of mosquitoes buzzing like thunder; small slanders growing into formidable harm"},
            {"hanzi": "秋蚊见血", "pinyin": "qiū wén jiàn xiè", "meaning_en": "autumn mosquitoes thirsty for blood; fierce desperation before death"},
            {"hanzi": "蝇营狗苟", "pinyin": "yíng yíng gǒu gǒu", "meaning_en": "scurrying like flies and creeping like dogs; shamelessly chasing personal gain"},
            {"hanzi": "蛛丝马迹", "pinyin": "zhū sī mǎ jì", "meaning_en": "spider web and horse tracks; faint clues"}
        ],
        "character_decomposition": [
            {
                "character": "蚊",
                "pinyin": "wén",
                "meaning_en": "mosquito; gnat",
                "meaning_es": "mosquito; zancudo",
                "radical": "虫",
                "radical_meaning_en": "insect / bug",
                "meaning_component": "虫 (insect radical)",
                "sound_component": "文 (wén, pattern/humming vibration)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining insect (虫) with 文 (wén), imitating the fine high-pitched humming drone of mosquito wings.",
                "visual_mnemonic_story_en": "An annoying insect (虫) flies around writing invisible patterns in the air with a humming drone (文).",
                "visual_mnemonic_story_es": "Un insecto molesto (虫) traza dibujos invisibles en el aire con un zumbido agudo (文).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "LIYK",
                "traditional": '""'
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; child; son",
                "meaning_es": "sufijo nominal; niño; hijo",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (infant/nominal affix)",
                "sound_component": "子 (inherent phoneme)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Pictogram of an infant with outstretched arms, widely utilized in vernacular Chinese as a common nominalizing noun suffix.",
                "visual_mnemonic_story_en": "A small child (子) swaddled up, functioning as the ubiquitous Chinese noun particle.",
                "visual_mnemonic_story_es": "Un infante (子) envuelto en mantas, usado como el sufijo de sustantivo más común del idioma.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ND",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The humming insect (蚊) with the standard noun suffix (子) forms the pesky mosquito.",
            "composite_memory_hook_es": "El insecto zumbador (蚊) con el sufijo de sustantivo (子) forma la palabra mosquito.",
            "cultural_and_cognitive_roots": "Symbol of annoying, disruptive trifles in classical poetry; the idiom '聚蚊成雷' warns that tiny pests humming together can generate the roar of thunder, metaphor for the dangerous accumulation of minor slander.",
            "tone_sandhi_and_pitch_modulation": "35-214 contour. In everyday spoken Chinese, 子 is universally reduced to a light neutral tone: wénzi (35-neutral)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "纹", "pinyin": "wén", "meaning_en": "pattern; grain", "distinction_note": "Features silk radical 纟 on the left instead of insect 虫"},
                {"character": "蚊", "pinyin": "wén", "meaning_en": "mosquito", "distinction_note": "Headword character with insect radical 虫"},
                {"character": "蛇", "pinyin": "shé", "meaning_en": "snake", "distinction_note": "Right side is 它 rather than 文"},
                {"character": "蜂", "pinyin": "fēng", "meaning_en": "bee; wasp", "distinction_note": "Right side is 夆 rather than 文"}
            ],
            "etymological_cognates": [
                {"character": "蝇", "pinyin": "yíng", "gloss_en": "housefly in the 虫 radical system"},
                {"character": "蛾", "pinyin": "é", "gloss_en": "moth"},
                {"character": "蝉", "pinyin": "chán", "gloss_en": "cicada"},
                {"character": "蝶", "pinyin": "dié", "gloss_en": "butterfly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "蚊子 refers specifically and biologically to mosquitoes (Culicidae family) that suck blood and hum loudly.",
            "contrasts": [
                {"id": "1", "compared_word": "蚊子 vs. 苍蝇", "pinyin": "cāngying", "analysis": "蚊子 sucks blood with piercing mouthparts and makes a high-pitched hum at night, whereas 苍蝇 is a filth-feeding fly that spreads digestive pathogens during daytime."},
                {"id": "2", "compared_word": "蚊子 vs. 飞蛾", "pinyin": "fēi'é", "analysis": "飞蛾 is a nocturnal powdery moth attracted to flames, harmless to human skin, unlike blood-biting 蚊子."},
                {"id": "3", "compared_word": "蚊子 vs. 蜜蜂", "pinyin": "mìfēng", "analysis": "蜜蜂 is a beneficial honeybee that stings defensively when provoked, unlike parasitic mosquitoes that feed on human blood."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "童年的盛夏夜里，庭院中摇曳的蒲扇是抵挡蚊子最好的盾牌。微风吹散了白昼的暑气，耳边偶尔响起蚊子微弱的嗡嗡声，却很快在漫天繁星与阵阵蛙鸣中远去。那一缕艾草蚊香的清香，是故乡最悠长的夏夜记忆。",
                "pinyin": "Tóngnián de shèngxià yèlǐ, tíngyuàn zhōng yáoyè de púshàn shì dǐdǎng wénzi zuì hǎo de dùnpái. Wēifēng chuīsàn le báizhòu de shǔqì, ěrbiān ǒu'ěr xiǎngqǐ wénzi wēiruò de wēngwēng shēng, què hěn kuài zài màntiān fánxīng yǔ zhènzhèn wāmíng zhōng yuǎnqù. Nà yì lǚ àicǎo wénxiāng de qīngxiāng, shì gùxiāng zuì yōucháng de xiàyè jìyì.",
                "en": "On summer nights of childhood, swaying cattail fans were our best shield against mosquitoes. Breezes cooled the day's heat; faint buzzing in our ears soon receded into starlight and croaking frogs. The scent of mugwort incense is my deepest memory.",
                "es": "En las noches infantiles de verano, el abanico de paja era el mejor escudo contra los zancudos. La brisa disipaba el bochorno y el zumbido de los mosquitos se perdía entre estrellas y ranas. El aroma a incienso de artemisa es el recuerdo más dulce de mi tierra."
            },
            {
                "id": "#2",
                "hanzi": "在现代生物技术防蚊治理前沿，科研团队正在利用基因驱动技术对野生蚊子种群实施精准干预。通过向自然界释放不育雄蚊阻断虫媒交配链条，能够在不破坏食物链生态平衡的前提下，大幅压低登革热与黄热病在城市的暴发风险。",
                "pinyin": "Zài xiàndài shēngwù jìshù fángwén zhìlǐ qiányán, kēyán tuánduì zhèngzài lìyòng jīyīn qūdòng jìshù duì yěshēng wénzi zhǒngqún shíshī jīngzhǔn gānyù. Tōngguò xiàng zìránjiè shìfàng bùyù xióngwén zǔduàn chóngméi jiāopèi liàntiáo, nénggòu zài bù pòhuài shíwùliàn shēngtài pínghéng de qiántí xià, dàfú yādī dēnggérè yǔ huángrèbìng zài chéngshì de bàofā fēngxiǎn.",
                "en": "At the forefront of biotechnology mosquito control, scientists utilize gene drives to intervene in wild mosquito populations. Releasing sterile males disrupts reproduction, suppressing dengue and yellow fever risks without disrupting food chains.",
                "es": "En la biotecnología contra insectos transmisores, los científicos aplican impulsos genéticos a poblaciones silvestres de mosquitos. Liberar machos estériles corta la reproducción y reduce el riesgo de dengue y fiebre amarilla sin alterar el ecosistema."
            }
        ]
    },

    # 33 半夜
    {
        "id": "33",
        "hanzi": "半夜",
        "pinyin": "bàn yè",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "midnight; middle of the night; late at night",
            "es": "medianoche; altas horas de la noche; en plena noche"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the middle period of the night, around or after midnight",
                "definition_es": "el periodo central de la noche, alrededor o pasada la medianoche",
                "example_phrase": "半夜醒来 (wake up in the middle of the night)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "昨天半夜突然狂风大作，窗外电闪雷鸣，暴雨敲打着窗玻璃，把熟睡中的全家人都惊醒了。",
                "pinyin": "Zuótiān bànyè tūrán kuángfēng dàzuò, chuāngwài diànshǎnléimíng, bàoyǔ qiāodǎ zhe chuāngbōlí, bǎ shúshuì zhōng de quánjiā rén dōu jīngxǐng le.",
                "en": "Wild winds suddenly blew in the middle of the night yesterday with lightning and thunder, torrential rain hammering the windowpanes and startling the whole sleeping family awake.",
                "es": "Ayer a medianoche se desató un vendaval con truenos y relámpagos, y la lluvia torrencial azotó los cristales despertando a toda la familia de su sueño."
            },
            {
                "id": "#2",
                "hanzi": "由于系统服务器集群在半夜遭遇异常网络流量冲击，技术值班团队紧急响应，历经三小时通宵排查修复了核心链路。",
                "pinyin": "Yóuyú xìtǒng fúwùqì jíqún zài bànyè zāoyù yìcháng wǎngluò liúliàng chōngjī, jìshù zhíbān tuánduì jǐnjí xiǎngyìng, lìjīng sān xiǎoshí tōngxiāo páichá xiūfù le héxīn liànlù.",
                "en": "Because server clusters were hit by abnormal network traffic surges in the middle of the night, on-duty tech staff responded swiftly, troubleshooting overnight to restore links.",
                "es": "Debido a una sobrecarga de tráfico anómala en los servidores a medianoche, el equipo técnico de guardia actuó de urgencia reparando los enlaces críticos tras horas de desvelo."
            }
        ],
        "collocations": [
            {"hanzi": "半夜三更", "en": "in the dead of night / middle of the night"},
            {"hanzi": "深更半夜", "en": "deep in the dead of night"},
            {"hanzi": "半夜醒来", "en": "wake up in the middle of the night"},
            {"hanzi": "大半夜", "en": "late at night; wee hours"},
            {"hanzi": "半夜敲门", "en": "knock on the door at midnight"},
            {"hanzi": "半夜起床", "en": "get up in the middle of the night"}
        ],
        "idioms": [
            {"hanzi": "夜以继日", "pinyin": "yè yǐ jì rì", "meaning_en": "day and night without cease; working round the clock"},
            {"hanzi": "深更半夜", "pinyin": "shēn gēng bàn yè", "meaning_en": "the small hours of the morning; the dead of night"},
            {"hanzi": "半夜三更", "pinyin": "bàn yè sān gēng", "meaning_en": "the third watch of the night; in the deep of the night"},
            {"hanzi": "风雨交加", "pinyin": "fēng yǔ jiāo jiā", "meaning_en": "wind and rain accompanied by thunder; severe nighttime storm"}
        ],
        "character_decomposition": [
            {
                "character": "半",
                "pinyin": "bàn",
                "meaning_en": "half; semi-; partly",
                "meaning_es": "mitad; medio; a medias",
                "radical": "十",
                "radical_meaning_en": "ten",
                "meaning_component": "八 (divide in two) + 牛 (ox halved)",
                "sound_component": "半 (inherent phoneme)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Anciently depicted cleaving an ox (牛) down the middle into two symmetrical halves (八).",
                "visual_mnemonic_story_en": "A central stroke cuts directly down through an animal carcass (十/八) into two equal halves.",
                "visual_mnemonic_story_es": "Un trazo vertical divide en dos mitades exactas (十/八) el cuerpo para compartirlo a medias.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "FQ",
                "traditional": '""'
            },
            {
                "character": "夜",
                "pinyin": "yè",
                "meaning_en": "night; darkness; evening",
                "meaning_es": "noche; oscuridad; anochecer",
                "radical": "夕",
                "radical_meaning_en": "evening / sunset",
                "meaning_component": "夕 (crescent moon rising at evening)",
                "sound_component": "亦 (yì, phonetic match / arms sheltering)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Depicts a human standing under the evening moon (夕) sheltered by the canopy of darkness.",
                "visual_mnemonic_story_en": "Under the canopy of the roof (亠), the crescent moon (夕) shines through darkness of night.",
                "visual_mnemonic_story_es": "Bajo el manto del cielo (亠), la luna creciente (夕) alumbra la oscuridad de la noche.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YOKD",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Reaching the exact midpoint (半) of the dark night (夜) marks midnight (半夜).",
            "composite_memory_hook_es": "Llegar a la mitad exacta (半) de la noche oscura (夜) define la medianoche (半夜).",
            "cultural_and_cognitive_roots": "Linked to the ancient Chinese system of five night watches ('五更'); the third watch ('三更', 23:00 to 01:00) sits at the balance of Yin and Yang, designated colloquially as 'bànyè' (half of the night).",
            "tone_sandhi_and_pitch_modulation": "51-51 pitch contour. Two consecutive crisp falling 4th tones; articulate both syllables distinctly."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "伴", "pinyin": "bàn", "meaning_en": "companion; partner", "distinction_note": "Features person radical 亻 on the left instead of 半 alone"},
                {"character": "拌", "pinyin": "bàn", "meaning_en": "mix; stir", "distinction_note": "Features hand radical 扌 on the left instead of 半 alone"},
                {"character": "变", "pinyin": "biàn", "meaning_en": "change", "distinction_note": "Top component is 亦 with dots; bottom is 又"},
                {"character": "夕", "pinyin": "xī", "meaning_en": "evening; dusk", "distinction_note": "Radical component itself inside 夜"}
            ],
            "etymological_cognates": [
                {"character": "晚", "pinyin": "wǎn", "gloss_en": "evening; late"},
                {"character": "昏", "pinyin": "hūn", "gloss_en": "dusk; twilight"},
                {"character": "宵", "pinyin": "xiāo", "gloss_en": "night; night watch"},
                {"character": "暮", "pinyin": "mù", "gloss_en": "sunset; dusk"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "半夜 refers specifically to the middle of the night, around or after midnight, usually between 23:00 and 03:00.",
            "contrasts": [
                {"id": "1", "compared_word": "半夜 vs. 午夜", "pinyin": "wǔyè", "analysis": "午夜 is a formal, precise, or literary chronological point marking 24:00/00:00, whereas 半夜 is a broader colloquial time window describing the deep of the night."},
                {"id": "2", "compared_word": "半夜 vs. 晚上", "pinyin": "wǎnshang", "analysis": "晚上 covers the entire evening from sunset to bedtime (typically 18:00 to 22:00), while 半夜 begins after most people have fallen asleep."},
                {"id": "3", "compared_word": "半夜 vs. 黎明", "pinyin": "límíng", "analysis": "黎明 marks the crack of dawn right before sunrise, the direct temporal successor to the dead of night."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "整座城市在半夜陷入了深沉的沉睡，白日的喧嚣与车水马龙都悄然退去。窗外只有几颗清冷的寒星，静静俯瞰着静谧的街巷。在这样万籁俱寂的半夜，人的心境往往格外澄明，能听见心底最真实的声音。",
                "pinyin": "Zhěng zuò chéngshì zài bànyè xiànrù le shēnchén de chénshuì, báirì de xuānxiāo yǔ chēshuǐmǎlóng dōu qiǎorán tuìqù. Chuāngwài zhǐyǒu jǐ kē qīnglěng de hánxīng, jìngjìng fǔkàn zhe jìngmì de jiēxiàng. Zài zhèyàng wànlàijùjì de bànyè, rén de xīnjìng wǎngwǎng géwài chéngmíng, néng tīngjiàn xīndǐ zuì zhēnshí de shēngyīn.",
                "en": "The entire city sank into deep slumber at midnight; daylight clamor and traffic receded. Outside the window, cool stars silently overlooked quiet lanes. In such stillness, the mind becomes clear, hearing the truest voice within.",
                "es": "La ciudad entera se sumió en un sueño profundo a medianoche; el bullicio diurno y el tráfico desaparecieron. Por la ventana, frías estrellas contemplaban callejuelas en silencio. En esa quietud nocturna, el alma escucha sus anhelos más sinceros."
            },
            {
                "id": "#2",
                "hanzi": "在现代越洋跨国金融外汇交易中，许多投资机构的技术团队必须在半夜保持高强度值守。面对国际外汇市场与大宗商品由于突发地缘事件引发的剧烈波动，半夜的实时风险对冲操作往往直接关乎数十亿美元头寸的资产安全。",
                "pinyin": "Zài xiàndài yuèyáng kuàguó jīnróng wàihuì jiāoyì zhōng, xǔduō tóuzī jīgòu de jìshù tuánduì bìxū zài bànyè bǎochí gāoxiàngdù zhíshǒu. Miànduì guójì wàihuì shìchǎng yǔ dàzōng shāngpǐn yóuyú tūfā dìyuán shìjiàn yǐnfā de jùliè bōdòng, bànyè de shíshí fēngxiǎn duìchōng cāozuò wǎngwǎng zhíjiē guānhū shù shí yì měiyuán tóucùn de zīchǎn ānquán.",
                "en": "In transoceanic foreign exchange trading, investment teams must maintain vigilance in the middle of the night. Confronting extreme currency volatility sparked by geopolitical events, midnight hedging operations safeguard billions in institutional capital.",
                "es": "En las finanzas internacionales y el mercado de divisas, los analistas deben hacer guardia a medianoche. Ante la volatilidad extrema provocada por sucesos geopolíticos, las operaciones de cobertura en plena noche protegen carteras multimillonarias de activos."
            }
        ]
    },

    # 34 叮
    {
        "id": "34",
        "hanzi": "叮",
        "pinyin": "dīng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to bite; to sting (of insects); to prompt/exhort; tinkling sound",
            "es": "picar (un insecto); encargar con insistencia; tintinear"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to sting or bite with a proboscis or stinger (of mosquitoes, bees, insects)",
                "definition_es": "picar o morder con aguijón o probóscide (insectos, mosquitos)",
                "example_phrase": "被蚊子叮了一口 (bitten by a mosquito)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to exhort repeatedly, prompt, or urge with careful instructions",
                "definition_es": "encargar o advertir con insistencia y cuidado",
                "example_phrase": "叮嘱再三 (exhort repeatedly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "昨晚在湖边草丛里散步时，我的脖子不小心被蚊子叮了好几个包，又红又痒，十分难受。",
                "pinyin": "Zuówǎn zài húbiān cǎocóng lǐ sànbù shí, wǒ de bózi bù xiǎoxīn bèi wénzi dīng le hǎojǐ gè bāo, yòu hóng yòu yǎng, shífēn nánshòu.",
                "en": "When strolling in the grassy brush by the lake last night, my neck was accidentally bitten by mosquitoes into several welts, red, itchy, and uncomfortable.",
                "es": "Anoche, al pasear por el pasto junto al lago, los mosquitos me picaron varias veces en el cuello, dejándome ronchas rojas que picaban mucho."
            },
            {
                "id": "#2",
                "hanzi": "临行前往高原高寒边防哨所慰问前，后勤医疗总监特意反复叮嘱队员们务必随身携带抗高原反应与防叮咬药品。",
                "pinyin": "Línxíng qiánwǎng gāoyuán gāohán biānfáng shàosuǒ wèiwèn qián, hòuqín yīliáo zǒngjiān tèyì fǎnfù dīngzhǔ duìyuán men wùbì suíshēn xiàidài kàng gāoyuán fǎnyìng yǔ fáng dīngyǎo yàopǐn.",
                "en": "Prior to departing for plateau border sentries, the chief medical officer repeatedly exhorted team members to carry altitude sickness and insect bite remedies.",
                "es": "Antes de viajar a los puestos fronterizos de la meseta, el jefe médico encargó a los brigadistas llevar consigo medicamentos contra el mal de altura y picaduras."
            }
        ],
        "collocations": [
            {"hanzi": "被蚊子叮", "en": "bitten by a mosquito"},
            {"hanzi": "叮了一口", "en": "stung once / bitten once"},
            {"hanzi": "叮嘱", "en": "exhort / urge with care"},
            {"hanzi": "千叮万嘱", "en": "exhort and admonish countless times"},
            {"hanzi": "防蚊虫叮咬", "en": "prevent mosquito and insect bites"},
            {"hanzi": "叮咚作响", "en": "tinkle and clink melodiously"}
        ],
        "idioms": [
            {"hanzi": "千叮万嘱", "pinyin": "qiān dīng wàn zhǔ", "meaning_en": "give repeated earnest instructions and exhortations"},
            {"hanzi": "再三叮咛", "pinyin": "zài sān dīng níng", "meaning_en": "exhort over and over again with tender solicitude"},
            {"hanzi": "言犹在耳", "pinyin": "yán yóu zài ěr", "meaning_en": "words still ringing in one's ears; advice remembered freshly"},
            {"hanzi": "耳提面命", "pinyin": "ěr tí miàn mìng", "meaning_en": "instruct face to face and pull by the ear; give earnest guidance"}
        ],
        "character_decomposition": [
            {
                "character": "叮",
                "pinyin": "dīng",
                "meaning_en": "bite/sting; exhort; clear tinkle",
                "meaning_es": "picar; encargar; tintinear",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth/stinger piercing or words prompting)",
                "sound_component": "丁 (dīng, nail/pointed tool)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing mouth (口) with pointed nail (丁), describing a sharp sting like a nail, or sharp verbal reminders.",
                "visual_mnemonic_story_en": "An insect uses its mouthpart like a sharp nail (丁) to sting through skin with a needle-like prick.",
                "visual_mnemonic_story_es": "Un insecto usa su boca como un clavo diminuto y punzante (丁) para picar la piel.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RMN",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A mouth (口) driving in like a sharp nail (丁) stings into your skin or drives home a repeated warning (叮).",
            "composite_memory_hook_es": "Una boca (口) punzante como un clavo (丁) pica la piel o clava una advertencia insistente (叮).",
            "cultural_and_cognitive_roots": "Polysemous in Chinese culture: physically it mimics the sharp piercing of a nail (丁); rhetorically it duplicates in '叮咛' / '叮嘱', metaphorically nailing wise parental advice firmly into the listener's memory.",
            "tone_sandhi_and_pitch_modulation": "55 pitch contour. A high, clear, ringing 1st tone (55); sounds brisk and crisp like a metallic chime."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "订", "pinyin": "dìng", "meaning_en": "book; order", "distinction_note": "Features speech radical 讠 on the left instead of mouth 口"},
                {"character": "钉", "pinyin": "dīng / dìng", "meaning_en": "nail; tack", "distinction_note": "Features metal radical 钅 on the left instead of mouth 口"},
                {"character": "盯", "pinyin": "dīng", "meaning_en": "stare; gaze fixedly", "distinction_note": "Features eye radical 目 on the left instead of mouth 口"},
                {"character": "叮", "pinyin": "dīng", "meaning_en": "sting; exhort", "distinction_note": "Headword character itself"}
            ],
            "etymological_cognates": [
                {"character": "咬", "pinyin": "yǎo", "gloss_en": "bite; snap at in the mouth radical family"},
                {"character": "啄", "pinyin": "zhuó", "gloss_en": "peck; pick with beak"},
                {"character": "嚼", "pinyin": "jiáo", "gloss_en": "chew; masticate"},
                {"character": "嘱", "pinyin": "zhǔ", "gloss_en": "enjoin; bid words"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "叮 specifically denotes insect stinging/biting with mouthparts, or verbal earnest exhortation (叮嘱).",
            "contrasts": [
                {"id": "1", "compared_word": "叮 vs. 咬", "pinyin": "yǎo", "analysis": "咬 implies using upper and lower teeth to clamp down and chew, whereas 叮 specifically applies to insect mouthparts or stingers piercing the skin."},
                {"id": "2", "compared_word": "叮 vs. 蛰", "pinyin": "zhē", "analysis": "蛰 refers to venomous stinging by bees, wasps, or scorpions causing burning pain, whereas 叮 applies to mosquito and gnat blood-sucking bites."},
                {"id": "3", "compared_word": "叮 vs. 嘱咐", "pinyin": "zhǔfù", "analysis": "嘱咐 is a general verb for bidding or instructing, whereas 叮 specifically emphasizes repeated, earnest verbal urging (as in 叮嘱)."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "每次远行离家，母亲总会拉着我的手，千叮万嘱要按时吃饭、注意保暖。那些朴实无华的言语，宛如冬日里的一缕暖阳，穿透遥远的距离，在岁月的长河中化作心头最深沉的牵挂与前行的力量。",
                "pinyin": "Měi cì yuǎnxíng líjiā, mǔqīn zǒng huì lā zhe wǒ de shǒu, qiān dīng wàn zhǔ yào ànshí chīfàn, zhùyì bǎonuǎn. Nàxiē pǔshíwúhuá de yányǔ, wǎnrú dōngrì lǐ de yì lǚ nuǎnyáng, chuāntòu yuǎnyuán de jùlí, zài suìyuè de chánghé zhōng huàzuò xīntóu zuì shēnchén de qiānguà yǔ qiánxíng de lìliàng.",
                "en": "Whenever I left home for long journeys, mother held my hand, repeatedly exhorting me to eat on time and stay warm. Those unadorned words were like winter sunlight, spanning distance to become enduring solace and strength.",
                "es": "Cada vez que partía de viaje, mi madre me tomaba de las manos encargándome una y otra vez que comiera a tiempo y me abrigara. Esas sencillas palabras fueron como un sol invernal que acortó distancias, dándome fuerzas para el camino."
            },
            {
                "id": "#2",
                "hanzi": "在现代野外边境科考与丛林探险安全规范中，防范毒虫叮咬是保障队员生存能力的关键科目。通过配发高长效驱避防护服与抗组胺外用药膏，能够有效遏制野外有害蚊蠓叮咬引发的过敏性皮炎及虫媒疾病感染。",
                "pinyin": "Zài xiàndài yěwài biānjìng kěkǎo yǔ cónglín tànxiǎn ānquán guīfàn zhōng, fángfàn dúchóng dīngyǎo shì bǎozhàng duìyuán shēngcún nénglì de guānjiàn kēmù. Tōngguò pèifā gāo chángxiào qūbì fánghùfú yǔ kàngzǔ'àn wàiyòng yàogāo, nénggòu yǒuxiào èzhì yěwài yǒuhài wénměng dīngyǎo yǐnfā de guòmǐnxìng píyán jí chóngméi jíbìng gǎnrǎn.",
                "en": "In field expeditions and jungle safety protocols, preventing toxic insect bites is critical for team survival. Equipping long-lasting repellent gear and antihistamines curbs allergic dermatitis and vector-borne infections caused by insect bites.",
                "es": "En las expediciones por la selva, prevenir las picaduras de insectos venenosos es vital para la supervivencia. Dotar al equipo de ropa repelente y pomadas antihistamínicas frena la dermatitis alérgica y los contagios parasitarios."
            }
        ]
    },

    # 35 老婆
    {
        "id": "35",
        "hanzi": "老婆",
        "pinyin": "lǎo po",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "wife (colloquial; affectionate)",
            "es": "esposa; mujer (coloquial y cariñoso)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Colloquial",
                "definition_en": "informal, affectionate spoken term for one's wife or someone's spouse",
                "definition_es": "término coloquial y afectuoso para referirse a la propia esposa o cónyuge",
                "example_phrase": "疼老婆 (cherish one's wife)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "下班回家的路上，王强特意去花店买了一束新鲜的红玫瑰，打算给正在厨房忙着做晚餐的老婆一个惊喜。",
                "pinyin": "Xiàbān huíjiā de lùshang, Wáng Qiáng tèyì qù huādiàn mǎi le yí shù xīnxiān de hóng méiguī, dǎsuàn gěi zhèngzài chúfáng máng zhe zuò wǎncān de lǎopo yí gè jīngxǐ.",
                "en": "On his way home from work, Wang Qiang stopped by the florist to buy fresh red roses, intending to give his wife cooking dinner in the kitchen a surprise.",
                "es": "Al volver del trabajo, Wang Qiang pasó por la floristería a comprar rosas rojas para sorprender a su esposa, que preparaba la cena en la cocina."
            },
            {
                "id": "#2",
                "hanzi": "社会学学者在关于当代城市家庭劳务分工的调研中指出，“怕老婆”等民间幽默俗语的演变，从侧面折射出女性家庭话语权与家庭平等地位的实质性提升。",
                "pinyin": "Shèhuìxué xuézhě zài guānyú dāngdài chéngshì jiātíng láowù fēngōng de diàoyán zhōng zhǐchū, “pà lǎopo” děng mínjiān yōumò súyǔ de yǎnbiàn, cóng cèmiàn zhéshè chū nǚxìng jiātíng huàyǔquán yǔ jiātíng píngděng dìwèi de shízhìxìng tíshēng.",
                "en": "Sociologists researching urban household labor division note that humorous folk sayings like 'henpecked / fearing one's wife' mirror the substantive rise of women's domestic status and equality.",
                "es": "Los sociólogos señalan que dichos humorísticos populares como 'temer a la esposa' reflejan el aumento real de la equidad y del poder de decisión de las mujeres en el hogar moderno."
            }
        ],
        "collocations": [
            {"hanzi": "疼老婆", "en": "cherish and dote on one's wife"},
            {"hanzi": "怕老婆", "en": "henpecked / respect one's wife immensely"},
            {"hanzi": "娶老婆", "en": "take a wife / marry"},
            {"hanzi": "老婆孩子", "en": "wife and kids; family"},
            {"hanzi": "讨老婆", "en": "seek a wife to marry"},
            {"hanzi": "爱老婆", "en": "love one's wife"}
        ],
        "idioms": [
            {"hanzi": "白头偕老", "pinyin": "bái tóu xié lǎo", "meaning_en": "live together until white hair; grow old together in marital devotion"},
            {"hanzi": "相濡以沫", "pinyin": "xiāng rú yǐ mò", "meaning_en": "share meager resources in adversity; mutual support in marital hardship"},
            {"hanzi": "老骥伏枥", "pinyin": "lǎo jì fú lì", "meaning_en": "an old steed in the stable still aspires to gallop a thousand miles"},
            {"hanzi": "返老还童", "pinyin": "fǎn lǎo huán tóng", "meaning_en": "rejuvenate; recover youthful vigor in old age"}
        ],
        "character_decomposition": [
            {
                "character": "老",
                "pinyin": "lǎo",
                "meaning_en": "old; experienced; affectionate prefix",
                "meaning_es": "viejo; anciano; experimentado; prefijo afectivo",
                "radical": "老",
                "radical_meaning_en": "old",
                "meaning_component": "老 (elderly man with long hair leaning on cane)",
                "sound_component": "老 (inherent root)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Pictogram of an elderly revered person with long hair leaning upon a walking staff (匕/𠤎).",
                "visual_mnemonic_story_en": "An elderly person with silver hair leans on a walking cane (老), embodying lifelong companionship.",
                "visual_mnemonic_story_es": "Un anciano con cabellos canos se apoya en un bastón (老), simbolizando la compañía de toda la vida.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "JKP",
                "traditional": '""'
            },
            {
                "character": "婆",
                "pinyin": "po",
                "meaning_en": "elderly woman; grandmother; matron; wife",
                "meaning_es": "anciana; abuela; matrona; esposa",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman)",
                "sound_component": "波 (bō, rippling waves)",
                "stroke_count": 11,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Phono-semantic character pairing woman (女) with rippling waves (波), historically denoting a venerable matron with silver hair.",
                "visual_mnemonic_story_en": "A respected woman (女) whose hair has rippled like soft waves (波) through years of devotion.",
                "visual_mnemonic_story_es": "Una mujer respetable (女) cuyos cabellos ondean como suaves olas (波) tras años de vida compartida.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "EDV",
                "traditional": '""'
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The lifelong companion (老) with whom you vow to grow into venerable old age (婆) is your cherished wife (老婆).",
            "composite_memory_hook_es": "La compañera de por vida (老) con quien envejecerás hasta peinar canas (婆) es tu querida esposa (老婆).",
            "cultural_and_cognitive_roots": "Song Dynasty folklore records poet Mai Aixin desiring a concubine; his wife composed a rhyming couplet: '老公十分公道，老婆一片婆心'. Moved by her devotion, he abandoned the thought. Ever since, 'lǎogōng' and 'lǎopo' became China's most affectionate spousal terms.",
            "tone_sandhi_and_pitch_modulation": "214-35 contour. In everyday spoken Chinese, 婆 is universally reduced to a light neutral tone: lǎopo (21-neutral)."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "考", "pinyin": "kǎo", "meaning_en": "test; examine", "distinction_note": "Features 丂 at the bottom instead of 匕"},
                {"character": "孝", "pinyin": "xiào", "meaning_en": "filial piety", "distinction_note": "Features 子 (child) at the bottom beneath 土"},
                {"character": "波", "pinyin": "bō", "meaning_en": "wave; ripple", "distinction_note": "Features water radical 氵 on the left without 女"},
                {"character": "婆", "pinyin": "pó", "meaning_en": "matron; wife", "distinction_note": "Headword character itself"}
            ],
            "etymological_cognates": [
                {"character": "妻", "pinyin": "qī", "gloss_en": "formal wife"},
                {"character": "妇", "pinyin": "fù", "gloss_en": "married woman; matron"},
                {"character": "媳", "pinyin": "xí", "gloss_en": "daughter-in-law; wife in 媳妇"},
                {"character": "娘", "pinyin": "niáng", "gloss_en": "mother; young woman"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "老婆 is an affectionate, colloquial, and warm spoken term used to refer to one's own wife.",
            "contrasts": [
                {"id": "1", "compared_word": "老婆 vs. 妻子", "pinyin": "qīzi", "analysis": "妻子 is the formal, standard, written, and legal term for wife, whereas 老婆 is predominantly colloquial and intimate."},
                {"id": "2", "compared_word": "老婆 vs. 太太", "pinyin": "tàitai", "analysis": "太太 is a polite, respectful, and slightly formal term for someone else's wife or socially elevated spouse, whereas 老婆 is everyday casual."},
                {"id": "3", "compared_word": "老婆 vs. 爱人", "pinyin": "àirén", "analysis": "爱人 is gender-neutral meaning 'spouse' in mainland administrative/social contexts, whereas 老婆 specifically designates a female spouse."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "清晨厨房里冒着热气的清粥小菜，深夜归家时门厅留着的一盏暖灯，都是老婆给予这个家最温柔的守候。岁月悄然带走了青春的容颜，但彼此相视一笑的默契，却在柴米油盐的琐碎烟火中化作了不可磨灭的依恋。",
                "pinyin": "Qīngchén chúfáng lǐ màozhe rèqì de qīngzhōu xiǎocài, shēnyè guījiā shí méntīng liúzhe de yì zhǎn nuǎndēng, dōu shì lǎopo jǐyǔ zhè gè jiā zuì wēnróu de shǒuhòu. Suìyuè qiǎorán dàizǒu le qīngchūn de róngyán, dàn bǐcǐ xiāngshìyíxiào de mòqì, què zài cháimǐyóuyán de suǒsuì yānhuǒ zhōng huàzuò le bùkěmómiè de yīliàn.",
                "en": "Steaming porridge in the morning kitchen and a warm light in the foyer late at night are the gentlest guardianship a wife gives a home. Time takes youthful looks, but a knowing smile across daily meals becomes an indelible bond.",
                "es": "El tazón humeante en la cocina matinal y la luz tibia en el zaguán de noche son la devoción más dulce de una esposa. El tiempo atenúa la juventud, pero la sonrisa cómplice entre los quehaceres cotidianos forja un apego imborrable."
            },
            {
                "id": "#2",
                "hanzi": "在当代家庭社会学研究中，核心家庭内部的情感表达方式展现出深刻的平等化特征。男性在日常社交中大方表达对老婆的关爱与敬重，不仅体现了家庭决策权向平等协商的转变，更重塑了现代文明家庭伦理的包容范式。",
                "pinyin": "Zài dāngdài jiātíng shèhuìxué yánjiū zhōng, héxīn jiātíng nèibù de qínggǎn biǎodá fāngshì zhǎnxiàn chū shēnkè de píngděnghuà tèzhēng. Nánxìng zài rìcháng shèjiāo zhōng dàfāng biǎodá duì lǎopo de guān'ài yǔ jìngzhòng, bùjǐn tǐxiàn le jiātíng juécèquán xiàng píngděng xiéshāng de zhuǎnbìan, gèng zhòngshù le xiàndài wénmíng jiātíng lúnlǐ de bāoróng fànshì.",
                "en": "In contemporary family sociology, emotional expression within nuclear families shows profound egalitarian characteristics. Husbands openly expressing care and respect for their wives mirrors democratic household decisions, reshaping civilized ethics.",
                "es": "En la sociología familiar contemporánea, la expresión de afecto en el hogar evidencia una profunda igualdad. Que los hombres manifiesten cariño y respeto hacia sus esposas refleja decisiones domésticas democráticas, renovando la ética familiar."
            }
        ]
    }
]

if __name__ == '__main__':
    for w in words_batch7:
        save_word(w)

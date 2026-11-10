# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 争论
    {
        "id": "1",
        "hanzi": "争论",
        "pinyin": "zhēng lùn",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to argue; to dispute; to debate contentiously; controversy; debate",
            "es": "disputar; polemizar; discutir acaloradamente; controversia; debate"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to dispute, argue, or contest opposing views vigorously when opinions clash",
                "definition_es": "disputar o sostener puntos de vista opuestos con vehemencia cuando chocan las opiniones",
                "example_phrase": "引起激烈争论 (spark heated dispute)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an argument, dispute, controversy, or debate",
                "definition_es": "discusión acalorada, controversia, disputa o querella de ideas",
                "example_phrase": "停止无谓的争论 (stop pointless arguing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "学术沙龙上，两位教授围绕人工智能的道德边界展开了热烈争论，谁也无法轻易说服对方。",
                "pinyin": "Xuéshù shālóng shàng, liǎng wèi jiàoshòu wéirào réngōng zhìnéng de dàodé biānjiè zhǎnkāi le rèliè zhēnglùn, shéi yě wúfǎ qīngyì shuōfú duìfāng.",
                "en": "At the academic salon, two professors entered a heated dispute over the ethical boundaries of AI, neither easily convincing the other.",
                "es": "En el coloquio académico, dos catedráticos se enzarzaron en una viva disputa sobre los límites éticos de la IA, sin convencerse mutuamente."
            },
            {
                "id": "#2",
                "hanzi": "十九世纪七十年代，斯坦福与科恩围绕奔跑中的马蹄是否同时离地进行了著名争论，最终促成了电影技术的诞生。",
                "pinyin": "Shíjiǔ shìjì qīshí niándài, Sītǎnfú yǔ Kē'ēn wéirào bēnpǎo zhōng de mǎtí shìfǒu tóngshí lídì jìnxíng le zhùmíng zhēnglùn, zuìzhōng cùchéng le diànyǐng jìshù de dànshēng.",
                "en": "In the 1870s, Stanford and Cohen engaged in a famous debate over whether galloping horse hooves leave the ground simultaneously, triggering the birth of cinema.",
                "es": "En la década de 1870, Stanford y Cohen mantuvieron una célebre controversia sobre si los cascos del caballo dejaban el suelo al galopar, alumbrando el cine."
            }
        ],
        "collocations": [
            {"hanzi": "激烈争论", "en": "heated dispute/argument"},
            {"hanzi": "引发争论", "en": "trigger controversy/debate"},
            {"hanzi": "无休止的争论", "en": "endless dispute"},
            {"hanzi": "展开争论", "en": "launch into an argument"},
            {"hanzi": "争论不休", "en": "argue incessantly without pause"},
            {"hanzi": "学术争论", "en": "academic debate"}
        ],
        "idioms": [
            {"hanzi": "争论不休", "pinyin": "zhēng lùn bù xiū", "meaning_en": "argue incessantly without reaching an agreement"},
            {"hanzi": "各执一词", "pinyin": "gè zhí yì cí", "meaning_en": "each clings stubbornly to their own version of the story"},
            {"hanzi": "面红耳赤", "pinyin": "miàn hóng ěr chì", "meaning_en": "red in the face and ears with agitation"},
            {"hanzi": "平息纷争", "pinyin": "píng xī fēn zhēng", "meaning_en": "calm down and quell contentious disputes"}
        ],
        "character_decomposition": [
            {
                "character": "争",
                "pinyin": "zhēng",
                "meaning_en": "struggle; strive; contend; dispute",
                "meaning_es": "luchar; disputar; competir; contender",
                "radical": "刀",
                "radical_meaning_en": "knife",
                "meaning_component": "爫 (hand from above) + 彐 (hand from below grasping a stick)",
                "sound_component": "争 (zhēng)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of two human hands pulling and wrestling over a single object, symbolizing contention and struggle.",
                "visual_mnemonic_story_en": "Two hands reach out from above and below, wrestling fiercely over a single prize (争).",
                "visual_mnemonic_story_es": "Dos manos tiran a la vez desde arriba y abajo, forcejeando con brío por un mismo trofeo (争).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "NSD",
                "traditional": "爭"
            },
            {
                "character": "论",
                "pinyin": "lùn",
                "meaning_en": "discuss; debate; discourse; theory",
                "meaning_es": "discutir; debatir; teoría; tratado",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (speech/words)",
                "sound_component": "仑 (lún, bamboo slips in order / phonetic)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining spoken words 讠 with ordered bamboo slips 仑, meaning systematic theoretical discourse.",
                "visual_mnemonic_story_en": "Spoken words (讠) are systematically arranged like ordered bamboo slips (仑) in reasoned debate (论).",
                "visual_mnemonic_story_es": "Palabras meditadas (讠) se ordenan como tablillas de bambú (仑) para sostener un debate lógico (论).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVOP",
                "traditional": "論"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Two hands struggle to pull (争) while words fly in theoretical discourse (论), sparking an intense dispute (争论).",
            "composite_memory_hook_es": "Dos manos forcejean por la razón (争) mientras cruzan palabras teóricas (论), desatando la disputa (争论).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese dialectics (百家争鸣); while Confucianism emphasized harmony, ancient schools of thought (Mohists and Logicians) developed debate into formal epistemology.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'zhēng lùn' (55-51). Articulate 'zhēng' on level pitch 55, then descend decisively into 4th tone 'lùn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "净", "pinyin": "jìng", "meaning_en": "clean; pure", "distinction_note": "Has ice radical 冫 on left of 争"},
                {"character": "静", "pinyin": "jìng", "meaning_en": "quiet; still", "distinction_note": "Has 青 on left of 争"},
                {"character": "轮", "pinyin": "lún", "meaning_en": "wheel", "distinction_note": "Has vehicle radical 车 on left instead of speech 讠 in 论"},
                {"character": "伦", "pinyin": "lún", "meaning_en": "ethics; peer", "distinction_note": "Has person radical 亻 on left instead of 讠"}
            ],
            "etymological_cognates": [
                {"character": "辩", "pinyin": "biàn", "gloss_en": "debate; argue with fine distinctions"},
                {"character": "驳", "pinyin": "bó", "gloss_en": "refute; contradict opponent"},
                {"character": "竞", "pinyin": "jìng", "gloss_en": "compete; race toward goal"},
                {"character": "议", "pinyin": "yì", "gloss_en": "deliberate; discuss righteous policy"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "争论 emphasizes emotional or ideological friction where two parties argue vigorously over conflicting views.",
            "contrasts": [
                {"id": "1", "compared_word": "争论 vs. 辩论", "pinyin": "biànlùn", "analysis": "辩论 emphasizes formal, structured academic or competitive debates with rules, while 争论 implies emotional contention, clash, and dispute."},
                {"id": "2", "compared_word": "争论 vs. 讨论", "pinyin": "tǎolùn", "analysis": "讨论 is a cooperative, friendly discussion aimed at finding mutual solutions, whereas 争论 highlights opposing friction."},
                {"id": "3", "compared_word": "争论 vs. 争吵", "pinyin": "zhēngchǎo", "analysis": "争吵 is a vulgar, noisy quarrel or domestic spat, whereas 争论 involves ideas, theories, or principles."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "学术的繁荣离不开自由真诚的争论。当学者们各抒己见据理力争，真理的微光便在观点的剧烈交锋中悄然点亮。不因权威而盲从，不因分歧而交恶，在思想的争论与洗礼中，人类理性的大厦才能历经风雨而愈发坚固。",
                "pinyin": "Xuéshù de fánróng líbùkāi zìyóu zhēnchéng de zhēnglùn. Dāng xuézhěmen gèshū-jǐjiàn jùlǐ-lìzhēng, zhēnlǐ de wēiguāng biàn zài guāndiǎn de jùliè jiāofēng zhōng qiǎorán diǎnliàng. Bù yīn quánwēi ér mángcóng, bù yīn fēnqí ér jiāo'è, zài sīxiǎng de zhēnglùn yǔ xǐlǐ zhōng, rénlèi lǐxìng de dàshà cáinéng lìjīng fēngyǔ ér yùfā jiāngù.",
                "en": "Scholarly flourishing thrives on free and sincere debate. When scholars contest ideas with reason, truth's spark lights up amid intellectual clashes. Questioning authority without enmity, rationality's edifice grows stronger through debate.",
                "es": "La ciencia florece gracias a la controversia sincera. Cuando los sabios defienden sus tesis con rigor, la verdad destella en el choque de ideas. Sin rendirse ante dogmas ni enemistarse por disensos, el templo de la razón se afianza en el debate."
            },
            {
                "id": "#2",
                "hanzi": "回溯科技发展史，重大的发明往往脱胎于看似不起眼的激烈争论。十九世纪美国关于马奔跑时蹄子是否同时腾空的学术争论，促使摄影师发明了连续高速曝光拍摄装置。正是这场著名的科学争论，奇迹般地催生了现代活动电影技术。",
                "pinyin": "Huísù kējì fāzhǎnshǐ, zhòngdà de fāmíng wǎngwǎng tuōtāi yú kànsì bùqǐyǎn de jīliè zhēnglùn. Shíjiǔ shìjì Měiguó guānyú mǎ bēnpǎo shí tízi shìfǒu tóngshí téngkōng de xuéshù zhēnglùn, cùshǐ shèyǐngshī fāmíng le liánxù gāosù bàoguāng pāishè zhuāngzhì. Zhèng shì zhè chǎng zhùmíng de kēxué zhēnglùn, qíjì-bān de cuīshēng le xiàndài huódòng diànyǐng jìshù.",
                "en": "Tracing technological history, major inventions often stem from sharp debates. A 19th-century American dispute on whether horse hooves leave the ground spurred the invention of high-speed photography, miraculously giving birth to cinema.",
                "es": "En la historia de la técnica, grandes inventos nacieron de vivas polémicas. La disputa sobre si los caballos suspendían sus cuatro cascos al correr motivó la fotografía de alta velocidad. Esa controversia alumbró milagrosamente la cinematografía."
            }
        ]
    },

    # 02 奇迹
    {
        "id": "2",
        "hanzi": "奇迹",
        "pinyin": "qí jì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "miracle; wonder; marvel; phenomenal achievement",
            "es": "milagro; maravilla; prodigio; portento; hecho asombroso"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an extraordinary, marvelous event or astounding achievement that seems almost impossible by ordinary standards",
                "definition_es": "hecho extraordinario, prodigioso o hazaña asombrosa que parece imposible según los estándares ordinarios",
                "example_phrase": "创造奇迹 (create a miracle)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在医疗团队连续十几个小时的极限抢救下，重伤患者终于脱离了生命危险，创造了医学奇迹。",
                "pinyin": "Zài yīliáo tuánduì liánxù shí jǐ ge xiǎoshí de jíxiàn qiǎngjiù xià, zhòngshāng huànzhě zhōngyú tuōlí le shēngmìng wēixiǎn, chuàngzào le yīxué qíjì.",
                "en": "Under intense emergency rescue for over a dozen hours by the medical team, the critically injured patient pulled through, creating a medical miracle.",
                "es": "Tras más de diez horas de intensos cuidados por el equipo médico, el paciente grave quedó fuera de peligro, obrando un milagro médico."
            },
            {
                "id": "#2",
                "hanzi": "摄影师将连续拍摄的二十四张马蹄腾空照片放入放映机中快速播放，静止的画面奇迹般地化作了奔腾的活马。",
                "pinyin": "Shèyǐngshī jiāng liánxù pāishè de èrshísì zhāng mǎtí téngkōng zhàopiàn fàngrù fàngyìngjī zhōng kuàisù bōfàng, jìngzhǐ de huàmiàn qíjì-bān de huàzuò le bēnténg de huómǎ.",
                "en": "When the photographer projected twenty-four sequential snapshots into a projector, static frames miraculously transformed into a galloping horse.",
                "es": "Al proyectar las veinticuatro instantáneas tomadas en serie, las imágenes estáticas se transformaron milagrosamente en un caballo al galope."
            }
        ],
        "collocations": [
            {"hanzi": "创造奇迹", "en": "create a miracle"},
            {"hanzi": "医学奇迹", "en": "medical miracle"},
            {"hanzi": "奇迹般地", "en": "miraculously"},
            {"hanzi": "人间奇迹", "en": "earthly wonder / man-made miracle"},
            {"hanzi": "见证奇迹", "en": "witness a miracle"},
            {"hanzi": "发生奇迹", "en": "a miracle occurs"}
        ],
        "idioms": [
            {"hanzi": "起死回生", "pinyin": "qǐ sǐ huí shēng", "meaning_en": "raise from the dead; bring back to life miraculously"},
            {"hanzi": "回天乏术", "pinyin": "huí tiān fá shù", "meaning_en": "unable to turn the tide of fate; beyond miracle"},
            {"hanzi": "不可思议", "pinyin": "bù kě sī yì", "meaning_en": "inconceivable; beyond imagination and wonder"},
            {"hanzi": "神来之笔", "pinyin": "shén lái zhī bǐ", "meaning_en": "a stroke of divine brushwork; miraculous artistry"}
        ],
        "character_decomposition": [
            {
                "character": "奇",
                "pinyin": "qí",
                "meaning_en": "strange; rare; wonderful; odd; surprise",
                "meaning_es": "extraño; raro; maravilloso; impar; asombro",
                "radical": "大",
                "radical_meaning_en": "big",
                "meaning_component": "大 (great human stature)",
                "sound_component": "可 (kě, approval / exclaiming in awe)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ideogram showing an extraordinary human figure 大 inspiring gasps of vocal wonder 可.",
                "visual_mnemonic_story_en": "A great human figure (大) achieves something so extraordinary that observers shout in wonder (可): 'What a marvel!' (奇).",
                "visual_mnemonic_story_es": "Una figura admirable (大) realiza una hazaña tan insólita que la multitud exclama (可): '¡Qué portento!' (奇).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "KMNR",
                "traditional": ""
            },
            {
                "character": "迹",
                "pinyin": "jì",
                "meaning_en": "trace; footprint; mark; track; remains",
                "meaning_es": "huella; rastro; vestigio; indicio; marca",
                "radical": "辶",
                "radical_meaning_en": "walk",
                "meaning_component": "辶 (movement on a path)",
                "sound_component": "亦 (yì, armpits / human figure / phonetic)",
                "stroke_count": 9,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Phono-semantic character where feet walking along a path 辶 leave visible footprints and traces 迹.",
                "visual_mnemonic_story_en": "Footsteps walking along the snowy path (辶) leave indelible tracks and footprints (迹).",
                "visual_mnemonic_story_es": "Los pasos al avanzar por la senda nevada (辶) dejan rastros y huellas imborrables (迹).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YYC",
                "traditional": "跡"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An extraordinary marvel (奇) that leaves an indelible trace on history (迹) is a true miracle (奇迹).",
            "composite_memory_hook_es": "Un hecho maravilloso (奇) que deja una huella imborrable (迹) constituye un auténtico milagro (奇迹).",
            "cultural_and_cognitive_roots": "Literally 'marvelous footprints'; in ancient Chinese cosmology, divine interventions were verified by unusual physical imprints left upon the earthly terrain.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone: 'qí jì' (35-51). Syllable 'qí' glides upward smoothly, followed by a crisp descending strike on 'jì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "夺", "pinyin": "duó", "meaning_en": "seize; snatch", "distinction_note": "Has 寸 below 大 instead of 可 in 奇"},
                {"character": "奈", "pinyin": "nài", "meaning_en": "how; what", "distinction_note": "Has 示 below 大 instead of 可"},
                {"character": "变", "pinyin": "biàn", "meaning_en": "change", "distinction_note": "Has 又 at bottom, distinct from 迹"},
                {"character": "迈", "pinyin": "mài", "meaning_en": "stride", "distinction_note": "Has 万 inside 辶 instead of 亦"}
            ],
            "etymological_cognates": [
                {"character": "异", "pinyin": "yì", "gloss_en": "different; extraordinary anomaly"},
                {"character": "痕", "pinyin": "hén", "gloss_en": "scar; trace mark on skin"},
                {"character": "踪", "pinyin": "zōng", "gloss_en": "tracks; footprints in dust"},
                {"character": "妙", "pinyin": "miào", "gloss_en": "subtle; ingenious wonder"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "奇迹 denotes an astonishing, seemingly impossible phenomenon or momentous historic breakthrough.",
            "contrasts": [
                {"id": "1", "compared_word": "奇迹 vs. 神话", "pinyin": "shénhuà", "analysis": "神话 refers to ancient folklore mythologies, or metaphorical impossibilities, while 奇迹 denotes verifiable, real-world feats achieved against all odds."},
                {"id": "2", "compared_word": "奇迹 vs. 壮举", "pinyin": "zhuàngjǔ", "analysis": "壮举 emphasizes heroic, courageous human effort on a massive scale, while 奇迹 emphasizes the astonishing, almost magical outcome."},
                {"id": "3", "compared_word": "奇迹 vs. 偶然", "pinyin": "ǒurán", "analysis": "偶然 denotes a random coincidence, whereas 奇迹 represents an extraordinary milestone born of persistence."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生命本身就是大自然最壮丽的奇迹。一粒微小的草籽能够在坚硬的岩石缝隙中破土而出，历经暴风骤雨依然迎风绽放。生活从不缺少奇迹，只要心怀希望永不言弃，黑暗尽头终将迎来破晓的曙光。坚持，是奇迹的唯一起点。",
                "pinyin": "Shēngmìng běnshēn jiùshì dàzìrán zuì zhuànglì de qíjì. Yí lì wēixiǎo de cǎozǐ nénggòu zài jiānyìng de yánshí fèngxì zhōng pòtǔ-érchū, lìjīng bàofēng-zhòuyǔ yīrán yíngfēng zhànfàng. Shēnghuó cóng bù quēshǎo qíjì, zhǐyào xīnhuái xīwàng yǒng bù yánqì, hēi'àn jìntóu zhōng jiāng yínglái pòxiǎo de shǔguāng. Jiānchí, shì qíjì de wéiyī qǐdiǎn.",
                "en": "Life is nature's most magnificent miracle. A tiny seed bursts through rock fissures, blooming through storms. Life never lacks miracles; keeping hope and never surrendering brings dawn at dark's end. Persistence is the sole origin of miracles.",
                "es": "La vida es el mayor prodigio de la naturaleza. Una semilla menuda brota en la hendidura de la peña y florece desafiando tempestades. Jamás faltan milagros si se abriga la esperanza: la perseverancia es la cuna de lo asombroso."
            },
            {
                "id": "#2",
                "hanzi": "改革开放四十余年间，中国经济社会的飞速跃升被国际社会公认为当代人类发展史上的伟大奇迹。从落后的农业国迈入世界制造业第一大国，数亿人口摆脱绝对贫困，这一系列举世瞩目的非凡奇迹，离不开全体人民脚踏实地的艰苦奋斗。",
                "pinyin": "Gǎigé kāifàng sìshí yú nián jiān, Zhōngguó jīngjì shèhuì de fēisù yuèshēng bèi guójì shèhuì gōngrèn wéi dāngdài rénlèi fāzhǎnshǐ shàng de wěidà qíjì. Cóng luòhòu de nóngyèguó màirù shìjiè zhìzàoyè dì-yī dàguó, shùyì rénkǒu bǎituō juéduì píngkùn, zhè yíxìliè jǔshì-zhǔmù de fēifán qíjì, líbùkāi quántǐ rénmín jiǎotà-shídì de jiānkǔ fèndòu.",
                "en": "Over forty years of reform, China's economic ascent has been recognized as a great miracle of human history. Transitioning to a manufacturing giant and lifting hundreds of millions from poverty, this miracle stems from down-to-earth struggle.",
                "es": "En cuatro décadas de reforma, el auge de China ha sido reconocido como un portento histórico. Erigirse en potencia industrial y sacar a millones de la pobreza absoluta compone un milagro forjado con tenaz esfuerzo colectivo."
            }
        ]
    },

    # 03 围绕
    {
        "id": "3",
        "hanzi": "围绕",
        "pinyin": "wéi rào",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to revolve around; to center around; to encircle; to focus on a theme",
            "es": "girar en torno a; centrarse en; rodear; girar alrededor de"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to physically move around a center in a circular or elliptical path, or encircle an object",
                "definition_es": "desplazarse en círculo o elipse alrededor de un centro, o cercar físicamente algo",
                "example_phrase": "地球围绕太阳旋转 (the Earth revolves around the Sun)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to center discussion, policy, or research upon a core topic, problem, or theme",
                "definition_es": "centrar debates, políticas o investigaciones en torno a un tema o problema nuclear",
                "example_phrase": "围绕核心议题展开 (center around the core topic)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "孩子们欢声笑语地围绕在篝火四周载歌载舞，跳动的火光映红了每一张灿烂的笑脸。",
                "pinyin": "Háizimen huānshēng-xiàoyǔ de wéirào zài gōuhuǒ sìzhōu zàigē-zàiwǔ, tiàodòng de huǒguāng yìnghóng le měi yì zhāng cànlàn de xiàoliǎn.",
                "en": "Laughing and cheering, children encircled the bonfire dancing and singing, the dancing flames illuminating their smiling faces.",
                "es": "Entre risas y cantos, los niños bailaban alrededor de la fogata, mientras las llamas alumbraban sus alegres rostros."
            },
            {
                "id": "#2",
                "hanzi": "当年斯坦福与科恩正是围绕“马奔跑时马蹄是否全部腾空”这一分歧展开论战，推动了照相技术的重大革新。",
                "pinyin": "Dāngnián Sītǎnfú yǔ Kē'ēn zhèng shì wéirào 'mǎ bēnpǎo shí mǎtí shìfǒu quánbù téngkōng' zhè yì fēnqí zhǎnkāi lùnzhàn, tuīdòng le zhàoxiàng jìshù de zhòngdà géxīn.",
                "en": "Back then, Stanford and Cohen centered their debate around whether all hooves leave the ground, propelling a major photographic breakthrough.",
                "es": "Stanford y Cohen centraron su célebre controversia en si el caballo suspendía sus cuatro cascos, impulsando la técnica fotográfica."
            }
        ],
        "collocations": [
            {"hanzi": "围绕主题", "en": "center around the theme"},
            {"hanzi": "围绕中心", "en": "revolve around the center"},
            {"hanzi": "紧紧围绕", "en": "closely focus on / center tightly around"},
            {"hanzi": "围绕核心", "en": "center around the core"},
            {"hanzi": "围绕问题", "en": "focus on the issue"},
            {"hanzi": "围绕太阳公转", "en": "revolve around the Sun"}
        ],
        "idioms": [
            {"hanzi": "众星拱月", "pinyin": "zhòng xīng gǒng yuè", "meaning_en": "multitude of stars revolve around the bright moon; cluster around a center"},
            {"hanzi": "环顾四周", "pinyin": "huán gù sì zhōu", "meaning_en": "look around in all directions"},
            {"hanzi": "群策群力", "pinyin": "qún cè qún lì", "meaning_en": "pool collective wisdom and efforts"},
            {"hanzi": "万变不离其宗", "pinyin": "wàn biàn bù lí qí zōng", "meaning_en": "innumerable changes never depart from the central principle"}
        ],
        "character_decomposition": [
            {
                "character": "围",
                "pinyin": "wéi",
                "meaning_en": "surround; encircle; enclosure; corral",
                "meaning_es": "rodear; cercar; recinto; corral",
                "radical": "囗",
                "radical_meaning_en": "enclosure",
                "meaning_component": "囗 (surrounding wall boundary)",
                "sound_component": "韦 (wéi, leather / patrol / phonetic)",
                "stroke_count": 7,
                "composition_type": "全包围结构",
                "etymology_and_mnemonic": "Ideogram showing guards patrolling 韦 around the outer perimeter wall 囗 of a fortified city.",
                "visual_mnemonic_story_en": "A perimeter wall (囗) completely encircles the citadel to guard (韦) against intrusion (围).",
                "visual_mnemonic_story_es": "Un muro perimetral (囗) rodea la fortaleza para protegerla (韦) por los cuatro costados (围).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "WDS",
                "traditional": "圍"
            },
            {
                "character": "绕",
                "pinyin": "rào",
                "meaning_en": "wind around; coil; bypass; detour",
                "meaning_es": "enrollar; serpentear; dar rodeo; girar",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (silk cord/thread)",
                "sound_component": "尧 (yáo, lofty / winding / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where silken threads 纟 wind in circular loops around a spindle.",
                "visual_mnemonic_story_en": "Long silk cords (纟) wind in circular coils around a tall spool (尧), bypassing obstacles (绕).",
                "visual_mnemonic_story_es": "Finos hilos de seda (纟) se enrollan en espiral alrededor del carrete (尧), dando vueltas (绕).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VMJPU",
                "traditional": "繞"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Encircle with boundary walls (围) and wind silk cords in orbit (绕) to revolve around a center (围绕).",
            "composite_memory_hook_es": "Cerca con muros (围) y enrolla el hilo en torno al centro (绕) para girar alrededor de él (围绕).",
            "cultural_and_cognitive_roots": "Derived from celestial orbits (astronomy) and circular defensive architecture; in discourse analysis, it serves as the primary metaphor for thematic focus ('theme as solar center').",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by falling tone: 'wéi rào' (35-51). Syllable 'wéi' glides upward, followed by a crisp descending strike on 'rào'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "图", "pinyin": "tú", "meaning_en": "picture; map", "distinction_note": "Has 冬 inside 囗 instead of 韦"},
                {"character": "国", "pinyin": "guó", "meaning_en": "country", "distinction_note": "Has jade 玉 inside 囗 instead of 韦"},
                {"character": "烧", "pinyin": "shāo", "meaning_en": "burn", "distinction_note": "Has fire radical 火 on left of 尧 instead of 纟"},
                {"character": "晓", "pinyin": "xiǎo", "meaning_en": "dawn; know", "distinction_note": "Has sun radical 日 on left of 尧"}
            ],
            "etymological_cognates": [
                {"character": "环", "pinyin": "huán", "gloss_en": "ring; encircle like jade ring"},
                {"character": "转", "pinyin": "zhuǎn", "gloss_en": "turn; rotate like wheels"},
                {"character": "旋", "pinyin": "xuán", "gloss_en": "whirl; revolve under banners"},
                {"character": "周", "pinyin": "zhōu", "gloss_en": "perimeter; circumference"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "围绕 emphasizes physical orbiting/encirclement, or focusing intellectual analysis closely around a central core.",
            "contrasts": [
                {"id": "1", "compared_word": "围绕 vs. 环绕", "pinyin": "huánrào", "analysis": "环绕 emphasizes static physical surrounding on all sides ('青山环绕'), while 围绕 emphasizes active dynamic revolution or thematic focus ('围绕问题')."},
                {"id": "2", "compared_word": "围绕 vs. 针对", "pinyin": "zhēnduì", "analysis": "针对 means aiming directly at a specific target, person, or symptom ('针对性措施'), while 围绕 implies exploring various dimensions around a central theme."},
                {"id": "3", "compared_word": "围绕 vs. 旁敲侧击", "pinyin": "pángqiāo-cèjī", "analysis": "旁敲侧击 means beating around the bush evasively, whereas 围绕 focuses constructively on the main hub."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "仰望浩瀚夜空，无数星辰围绕着银河的漩涡静静旋转，展示着宇宙庄严的秩序。人类探索星空的脚步从未停歇，科学家们围绕着黑洞与暗物质的奥秘展开持续攻关，正是这种执着的叩问，不断拓展着人类认知的宏伟边界。",
                "pinyin": "Yǎngwàng hàohàn yèkōng, wúshù xīngchén wéirào zhe Yínhé de xuánwō jìngjìng xuánzhuǎn, zhǎnshì zhe yǔzhòu zhuāngyán de zhìxù. Rénlèi tànsuǒ xīngkōng de jiǎobù cóng wèi tíngxiē, kēxuéjiāmen wéirào zhe hēidòng yǔ ànwùzhì de àomì zhǎnkāi chíxù gōngguān, zhèng shì zhè zhǒng zhízhuó de kòuwèn, bùduàn tuòzhǎn zhe rénlèi rènzhī de hóngwěi biānjiè.",
                "en": "Gazing into the night, countless stars revolve quietly around the galactic spiral, showing cosmic order. Never halting starward exploration, scientists center investigations on black holes, expanding the boundaries of knowledge.",
                "es": "Al mirar el firmamento, miríadas de estrellas giran en torno a la espiral galáctica, mostrando el orden cósmico. La ciencia centra sus pesquisas en los agujeros negros, ampliando los horizontes del saber humano."
            },
            {
                "id": "#2",
                "hanzi": "高质量发展必须紧紧围绕供给侧结构性改革这条主线。各级产业部门围绕传统产业数字化转型与绿色低碳循环发展，出台了一系列精准的财政与金融扶持政策，有力推动了产业链核心关键技术的自主可控与协同升级。",
                "pinyin": "Gāo zhìliàng fāzhǎn bìxū jǐnjǐn wéirào gōngjǐcè jiégòuxìng gǎigé zhè tiáo zhǔxiàn. Gèjí chǎnyè bùmén wéirào chuántǒng chǎnyè shùzìhuà zhuǎnxíng yǔ lǜsè dītàn xúnhuán fāzhǎn, chūtái le yíxìliè jīngzhǔn de cáizhèng yǔ jīnróng fúchí zhèngcè, yǒulì tuīdòng le chǎnyèliàn héxīn guānjiàn jìshù de zìzhǔ kěkòng yǔ xiétóng shēngjí.",
                "en": "High-quality development must tightly center around supply-side structural reform. Industrial bodies focus on digital transformation and green development, issuing targeted policies to boost supply-chain autonomy and coordinated upgrades.",
                "es": "El crecimiento de calidad debe girar en torno a la reforma estructural de la oferta. Los ministerios industriales centran sus planes en la digitalización y la transición verde, dictando incentivos para afianzar la soberanía técnica fabril."
            }
        ]
    },

    # 04 奔跑
    {
        "id": "4",
        "hanzi": "奔跑",
        "pinyin": "bēn pǎo",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to run; to gallop; to sprint; to dash rapidly",
            "es": "correr; galopar; corretear; correr velozmente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to run swiftly with quick strides on foot, or gallop forward rapidly",
                "definition_es": "correr a gran velocidad a zancadas o galopar con ímpetu",
                "example_phrase": "在操场上奔跑 (run on the sports ground)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "清晨的阳光洒在绿茵场上，少年们迎着晨风尽情奔跑，挥洒着青春特有的蓬勃朝气。",
                "pinyin": "Qīngchén de yángguāng sǎ zài lǜyīnchǎng shàng, shàoniánmen yíng zhe chénfēng jìnqíng bēnpǎo, huīsǎ zhe qīngchūn tèyǒu de péngbó zhāoqì.",
                "en": "Morning sunlight spilled over the grassy field; youths ran freely against the dawn breeze, radiating youthful vitality.",
                "es": "La luz matinal bañaba el césped; los jóvenes corrían a placer contra la brisa, derrochando el vigor propio de la lozanía."
            },
            {
                "id": "#2",
                "hanzi": "当赛马在跑道上全力奔跑时，高速相机记录下了马蹄腾空的瞬间，彻底解开了多年的谜团。",
                "pinyin": "Dāng sàimǎ zài pǎodào shàng quánlì bēnpǎo shí, gāosù xiàngjī jìlù xià le mǎtí téngkōng de shùnjiān, chèdǐ jiěkāi le duōnián de mǐtuán.",
                "en": "As the racehorse galloped along the track with all its might, high-speed cameras captured the instant its hooves left the ground, resolving the mystery.",
                "es": "Cuando el corcel galopaba con furia por la pista, las cámaras rápidas atraparon el instante de los cascos en el aire, zanjando el enigma."
            }
        ],
        "collocations": [
            {"hanzi": "飞速奔跑", "en": "run at breakneck speed"},
            {"hanzi": "尽情奔跑", "en": "run to one's heart's content"},
            {"hanzi": "向前奔跑", "en": "dash forward"},
            {"hanzi": "狂热奔跑", "en": "run wild with fervor"},
            {"hanzi": "自由奔跑", "en": "run freely"},
            {"hanzi": "骏马奔跑", "en": "steeds galloping"}
        ],
        "idioms": [
            {"hanzi": "万马奔腾", "pinyin": "wàn mǎ bēn téng", "meaning_en": "ten thousand horses gallop forward; magnificent momentum"},
            {"hanzi": "东奔西跑", "pinyin": "dōng bēn xī pǎo", "meaning_en": "run around here and there; rush about busy"},
            {"hanzi": "奋勇争先", "pinyin": "fèn yǒng zhēng xiān", "meaning_en": "dash ahead courageously to take the lead"},
            {"hanzi": "策马疾驰", "pinyin": "cè mǎ jí chí", "meaning_en": "spur horse into rapid gallop"}
        ],
        "character_decomposition": [
            {
                "character": "奔",
                "pinyin": "bēn",
                "meaning_en": "run fast; rush; dash; flee",
                "meaning_es": "correr rápido; apresurarse; lanzarse",
                "radical": "大",
                "radical_meaning_en": "big",
                "meaning_component": "大 (human running with arms out) + 卉/三止 (three running feet)",
                "sound_component": "奔 (bēn)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient ideogram showing a person 大 running forward propelled by three running feet 止, meaning sprinting at top speed.",
                "visual_mnemonic_story_en": "A runner (大) sprints forward with three flying feet (卉), dashing fast like the wind (奔).",
                "visual_mnemonic_story_es": "Un atleta (大) se lanza hacia adelante impulsado por tres pies veloces (卉), corriendo como el rayo (奔).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "KJT",
                "traditional": ""
            },
            {
                "character": "跑",
                "pinyin": "pǎo",
                "meaning_en": "run; jog; race; flee; escape",
                "meaning_es": "correr; trotar; escapar; huir",
                "radical": "足",
                "radical_meaning_en": "foot",
                "meaning_component": "𧾷 (foot in motion)",
                "sound_component": "包 (bāo, bundle / phonetic)",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining foot radical 𧾷 with 包 (curved momentum), denoting rapid running on foot.",
                "visual_mnemonic_story_en": "Legs and feet (𧾷) push off the earth with bundled kinetic momentum (包) to run swiftly (跑).",
                "visual_mnemonic_story_es": "Las piernas y pies (𧾷) cobran impulso concentrado (包) para correr a zancadas (跑).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "RMPRU",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Propel yourself forward with three feet (奔) using foot strength (跑) to run and gallop fast (奔跑).",
            "composite_memory_hook_es": "Lánzate hacia adelante con zancadas (奔) impulsando tus pies (跑) para correr a galope tendido (奔跑).",
            "cultural_and_cognitive_roots": "Cognate with nomadic horse culture; galloping horses (奔腾) were synonymous with unstoppable historical progress, dynamic youth, and military momentum.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by dipping tone: 'bēn pǎo' (55-214). Level high plateau on 'bēn', dipping and rising fully on 3rd tone 'pǎo'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "夯", "pinyin": "hāng", "meaning_en": "rammer; tamp", "distinction_note": "Has 力 below 大 instead of 卉/十"},
                {"character": "奋", "pinyin": "fèn", "meaning_en": "exert; strive", "distinction_note": "Has 田 below 大 instead of 卉/十"},
                {"character": "抱", "pinyin": "bào", "meaning_en": "hug", "distinction_note": "Has hand radical 扌 on left instead of foot 𧾷 in 跑"},
                {"character": "饱", "pinyin": "bǎo", "meaning_en": "full/sated", "distinction_note": "Has food radical 饣 on left instead of 𧾷"}
            ],
            "etymological_cognates": [
                {"character": "驰", "pinyin": "chí", "gloss_en": "gallop swiftly on horseback"},
                {"character": "骋", "pinyin": "chěng", "gloss_en": "gallop freely; give free rein"},
                {"character": "窜", "pinyin": "cuàn", "gloss_en": "scurry; flee in panic"},
                {"character": "跨", "pinyin": "kuà", "gloss_en": "stride over; leap with legs"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "奔跑 emphasizes vigorous, energetic running across open spaces or dynamic sprinting of animals/humans.",
            "contrasts": [
                {"id": "1", "compared_word": "奔跑 vs. 跑步", "pinyin": "pǎobù", "analysis": "跑步 is an everyday exercise/sport activity ('每天跑步锻炼'), while 奔跑 conveys dramatic cinematic motion, wild freedom, or passionate pursuit ('在原野上奔跑')."},
                {"id": "2", "compared_word": "奔跑 vs. 疾驰", "pinyin": "jíchí", "analysis": "疾驰 is typically used for vehicles or steeds speeding on highways, while 奔跑 applies to living legs sprinting."},
                {"id": "3", "compared_word": "奔跑 vs. 散步", "pinyin": "sànbù", "analysis": "散步 (stroll leisurely) is the complete tempo antonym of 奔跑."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活就像一场没有终点的马拉松，我们都在各自的赛道上迎风奔跑。或许会遭遇泥泞与暴雨，或许会感到疲惫与孤单，但只要脚步不停歇，奔跑本身就是对生命最大的赞美。不向命运低头的人，终会跑出属于自己的精彩。",
                "pinyin": "Shēnghuó jiù xiàng yì chǎng méiyǒu zhōngdiǎn de mǎlāsōng, wǒmen dōu zài gèzì de sàidào shàng yíngfēng bēnpǎo. Huòxǔ huì zāoyù nǐnìng yǔ bàoyǔ, huòxǔ huì gǎndào píbèi yǔ gūdān, dàn zhǐyào jiǎobù bù tíngxiē, bēnpǎo běnshēn jiùshì duì shēngmìng zuì dà de zànměi. Bù xiàng mìngyùn dītóu de rén, zhōng huì pǎochū shǔyú zìjǐ de jīngcǎi.",
                "en": "Life is like an endless marathon where we run against the wind on our own tracks. We may face mud and storms, fatigue and loneliness, but keeping our steps moving is itself the grandest praise of life. Those who do not yield will triumph.",
                "es": "La vida es como un maratón sin meta en el que corremos contra el viento. Habrá lodo y tormentas, fatiga y soledad, pero no frenar el paso es el mayor homenaje al existir. Quien no se rinde ante el hado alcanza su propia plenitud."
            },
            {
                "id": "#2",
                "hanzi": "在现代野生动物保护区内，红外感应相机记录下了藏羚羊在广袤草原上自由奔跑的珍贵画面。数以万计的生灵迎着朝阳向迁徙地奔跑进发，蹄声如雷气势磅礴，彰显出大自然生生不息的野性力量与高原生态系统修复的显著成效。",
                "pinyin": "Zài xiàndài yěshēng dòngwù bǎohùqū nèi, hóngwài gǎnyìng xiàngjī jìlù xià le zànglíngyáng zài guǎngmào cǎoyuán shàng zìyóu bēnpǎo de zhēnguì huàmiàn. Shùyǐwànjì de shēnglíng yíng zhe zhāoyáng xiàng qiānxǐdì bēnpǎo jìnfā, tíshēng-rúlèi qìshì-pángbó, zhāngxiǎn chū dàzìrán shēngshēng-bùxī de yěxìng lìliàng yǔ gāoyuán shēngtài xìtǒng xiūfù de xiǎnzhù chéngxiào.",
                "en": "In modern wildlife reserves, infrared cameras captured precious footage of Tibetan antelopes galloping across open grasslands. Tens of thousands migration herds dash toward pastures with thunderous hooves, demonstrating ecological restoration.",
                "es": "En las reservas naturales, cámaras infrarrojas captaron el galope libre de antílopes tibetanos en la estepa. Miles de animales corren hacia sus pastos con cascos tronantes, mostrando la indómita fuerza natural y el éxito de la conservación."
            }
        ]
    },

    # 05 蹄子
    {
        "id": "5",
        "hanzi": "蹄子",
        "pinyin": "tí zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "hoof (of horse, ox, sheep, pig, etc.); trotter",
            "es": "pezuña; casco (de caballo, buey, oveja o cerdo); pata de animal"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the hard, horny covering protecting the feet of ungulate mammals like horses, cattle, and sheep",
                "definition_es": "envoltura córnea y dura que protege el extremo de las extremidades de mamíferos ungulados",
                "example_phrase": "马的蹄子 (horse's hooves)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "铁匠熟练地为骏马修剪变长的角质，随后牢牢钉上特制的铁马掌，以保护马匹的蹄子不被碎石磨损。",
                "pinyin": "Tiějiang shúliàn de wèi jùnmǎ xiūjiǎn biàn cháng de jiǎozhì, suìhòu láoláo dīng shàng tèzhì de tiě mǎzhǎng, yǐ bǎohù mǎpǐ de tízi bú bèi suìshí mósǔn.",
                "en": "The blacksmith skillfully trimmed the overgrown horn of the steed, then nailed on custom iron horseshoes to protect its hooves from gravel wear.",
                "es": "El herrero recortó con pericia el casco del corcel y clavó la herradura para proteger sus pezuñas del desgaste de las piedras."
            },
            {
                "id": "#2",
                "hanzi": "当年那场关于马奔跑时四个蹄子是否同时离地的著名争论，激发了连续动态摄影技术的划时代实验。",
                "pinyin": "Dāngnián nà chǎng guānyú mǎ bēnpǎo shí sì ge tízi shìfǒu tóngshí lídì de zhùmíng zhēnglùn, jīfā le liánxù dòngtài shèyǐng jìshù de huàshídài shíyàn.",
                "en": "The historic debate over whether a galloping horse's four hooves leave the ground simultaneously stimulated epoch-making motion photography.",
                "es": "Aquel célebre debate sobre si los cuatro cascos del caballo dejaban el suelo al galopar inspiró el histórico ensayo de fotografía secuencial."
            }
        ],
        "collocations": [
            {"hanzi": "马蹄子", "en": "horse's hoof"},
            {"hanzi": "猪蹄子", "en": "pig's trotter"},
            {"hanzi": "蹄子着地", "en": "hooves touch the ground"},
            {"hanzi": "蹄子腾空", "en": "hooves airborne in the air"},
            {"hanzi": "修剪蹄子", "en": "trim hooves"},
            {"hanzi": "蹄声清脆", "en": "crisp clip-clop sound of hooves"}
        ],
        "idioms": [
            {"hanzi": "马不停蹄", "pinyin": "mǎ bù tíng tí", "meaning_en": "the horse does not stop its hooves; advance without pause"},
            {"hanzi": "得胜回朝", "pinyin": "dé shèng huí cháo", "meaning_en": "return victorious to the imperial court"},
            {"hanzi": "金戈铁马", "pinyin": "jīn gē tiě mǎ", "meaning_en": "golden spears and armored horses; battlefield glory"},
            {"hanzi": "风驰电掣", "pinyin": "fēng chí diàn chè", "meaning_en": "swift as wind and lightning"}
        ],
        "character_decomposition": [
            {
                "character": "蹄",
                "pinyin": "tí",
                "meaning_en": "hoof; leg of pork",
                "meaning_es": "pezuña; casco; pata",
                "radical": "足",
                "radical_meaning_en": "foot",
                "meaning_component": "𧾷 (foot)",
                "sound_component": "帝 (dì, sovereign / phonetic harmony)",
                "stroke_count": 16,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where foot radical 𧾷 indicates an animal foot and 帝 provides phonetic harmony.",
                "visual_mnemonic_story_en": "An animal foot (𧾷) crowned with a majestic hard horny shield (帝) forms a galloping hoof (蹄).",
                "visual_mnemonic_story_es": "La extremidad del animal (𧾷) protegida por un escudo córneo soberbio (帝) forma el casco o pezuña (蹄).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "RMYJB",
                "traditional": ""
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; child; son",
                "meaning_es": "sufijo nominal; niño; hijo",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (pictogram of swaddled child)",
                "sound_component": "子 (zǐ)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictogram of an infant child; used productively as an unstressed colloquial noun suffix.",
                "visual_mnemonic_story_en": "A child (子) stands with open arms; appended to nouns to turn roots into familiar spoken words.",
                "visual_mnemonic_story_es": "Un niño pequeño (子) abre los brazos; sirve de sufijo para formar nombres cotidianos.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ND",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The hard horny foot (蹄) of an animal takes the common noun suffix (子) to name a hoof (蹄子).",
            "composite_memory_hook_es": "La pata córnea del animal (蹄) con el sufijo nominal (子) designa la pezuña o casco (蹄子).",
            "cultural_and_cognitive_roots": "Crucial in equine husbandry and cavalry logistics; in Chinese idiom, 'mǎbùtíngtí' (马不停蹄) symbolizes tireless work ethic and unending motion.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by neutral tone: 'tí zi' (35-2). Syllable 'tí' glides upward, followed by a soft, light neutral tone on 'zi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "啼", "pinyin": "tí", "meaning_en": "cry; weep; crow", "distinction_note": "Has mouth radical 口 on left instead of foot 𧾷 in 蹄"},
                {"character": "帝", "pinyin": "dì", "meaning_en": "emperor; sovereign", "distinction_note": "Lacks the left foot radical 𧾷 of 蹄"},
                {"character": "跑", "pinyin": "pǎo", "meaning_en": "run", "distinction_note": "Has 包 on right of 𧾷 instead of 帝"},
                {"character": "跳", "pinyin": "tiào", "meaning_en": "jump", "distinction_note": "Has 兆 on right of 𧾷 instead of 帝"}
            ],
            "etymological_cognates": [
                {"character": "爪", "pinyin": "zhuǎ", "gloss_en": "claw; bird/animal talons"},
                {"character": "掌", "pinyin": "zhǎng", "gloss_en": "palm; bear paw; horseshoe pad"},
                {"character": "趾", "pinyin": "zhǐ", "gloss_en": "toe; foot phalange"},
                {"character": "踝", "pinyin": "huái", "gloss_en": "ankle joint"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "蹄子 refers to the hard horny foot of ungulate animals (horses, cows, pigs, goats).",
            "contrasts": [
                {"id": "1", "compared_word": "蹄子 vs. 爪子", "pinyin": "zhuǎzi", "analysis": "爪子 refers to sharp claws of carnivores, birds, or rodents (cats, dogs, eagles), while 蹄子 is strictly for hooved animals."},
                {"id": "2", "compared_word": "蹄子 vs. 脚", "pinyin": "jiǎo", "analysis": "脚 is the universal biological term for human feet or furniture legs, while 蹄子 designates hooves."},
                {"id": "3", "compared_word": "蹄子 vs. 马蹄", "pinyin": "mǎtí", "analysis": "马蹄 specifically means a horse's hoof (or water chestnut), while 蹄子 covers cattle, pigs, and sheep as well."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "走在茶马古道的青石板路上，凹凸不平的石面上依然清晰可见当年马帮踩踏出的深深蹄印。数百年间，成群结队的骡马驮着茶叶与盐巴翻山越岭，坚硬的蹄子在坚石上叩击出清脆回响，谱写了西南边疆一段沧桑古朴的商贸传奇。",
                "pinyin": "Zǒu zài Chá-Mǎ Gǔdào de qīngshíbǎn lù shàng, āotū-bùpíng de shímiàn shàng yīrán qīngxī kějiàn dāngnián mǎbāng cǎità chū de shēnshēn tíyìn. Shùbǎi nián jiān, chéngqún-jiéduì de luómǎ tuó zhe cháyè yǔ yánbā fānshān-yuèlǐng, jiānyìng de tízi zài jiānshí shàng kòujī chū qīngcuì huíxiǎng, pǔxiě le xīnán biānjiāng yí duàn cāngsāng gǔpǔ de shāngmào chuánqí.",
                "en": "Walking the Tea Horse Road, deep hoofprints trodden by caravans remain etched in stones. For centuries, pack mules carrying tea and salt scaled ridges, hard hooves ringing against stone, writing a frontier trade legend.",
                "es": "En la Ruta del Té y los Caballos, hondas huellas de pezuñas siguen grabadas en el empedrado. Durante siglos, recuas de mulas cargadas de té cruzaron cordilleras, cuyos cascos repicaban en la roca tejiendo la leyenda del comercio."
            },
            {
                "id": "#2",
                "hanzi": "视觉残留原理与连续动态摄影的结合，彻底颠覆了人类对运动瞬间的传统认知。在早期油画中，画家们习惯将疾驰中的奔马画成前后蹄子同时向外伸展的平展姿态；直到实拍照片面世，人们才惊讶地发现，马匹腾空时四只蹄子其实是收拢在腹下的。",
                "pinyin": "Shìjué cánliú yuánlǐ yǔ liánxù dòngtài shèyǐng de jiéhé, chèdǐ diānfù le rénlèi duì yùndòng shùnjiān de chuántǒng rènzhī. Zài zǎoqī yóuhuà zhōng, huàjiāmen xíguàn jiāng jíchí zhōng de bēnmǎ huàchéng qiánhòu tízi tóngshí xiàng wài shēnzhǎn de píngzhǎn zītài; zhídào shípāi zhàopiàn miànshì, rénmen cái jīngyà de fāxiàn, mǎpǐ téngkōng shí sì zhī tízi qíshí shì shōulǒng zài fù xià de.",
                "en": "Motion photography overturned perceptions of movement. Early painters depicted galloping horses with hooves stretched front and back; real photos revealed that when airborne, all four hooves are actually tucked beneath the belly.",
                "es": "La fotografía secuencial revolucionó la percepción del movimiento. Los viejos pintores dibujaban caballos al galope con los cascos estirados; las fotos demostraron que, en el aire, el animal pliega en verdad las pezuñas bajo el vientre."
            }
        ]
    },

    # 06 辩论
    {
        "id": "6",
        "hanzi": "辩论",
        "pinyin": "biàn lùn",
        "part_of_speech": "Verb / Noun",
        "meanings_summary": {
            "en": "to debate; to argue logically; debate; formal argumentation",
            "es": "debatir; polemizar; debate; argumentación reglada"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to present logical arguments, refute opponent propositions, and debate formally on a specific topic",
                "definition_es": "exponer argumentos lógicos, rebatir tesis contrarias y debatir formalmente sobre un tema",
                "example_phrase": "就此问题展开激烈辩论 (debate fiercely on this question)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a formal structured competition, parliamentary contest, or academic debate",
                "definition_es": "competición formal de oratoria, certamen parlamentario o debate académico reglado",
                "example_phrase": "国际大专辩论赛 (international collegiate debate competition)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "两支代表队在全国大学生辩论赛决赛中妙语连珠，就科技发展与环境保护的关系展开了精彩辩论。",
                "pinyin": "Liǎng zhī dàibiǎotuán zài quánguó dàxuéshēng biànlùnsài juésài zhōng miàoyǔ-liánzhū, jiù kējì fāzhǎn yǔ huánjìng bǎohù de guānxi zhǎnkāi le jīngcǎi biànlùn.",
                "en": "In the national collegiate debate finals, both teams exchanged witty arguments, holding a splendid debate on technology and ecology.",
                "es": "En la final del torneo nacional de debate, ambos equipos cruzaron brillantes argumentos sobre tecnología y medio ambiente."
            },
            {
                "id": "#2",
                "hanzi": "为了验证辩论中的学术假说，斯坦福重金聘请专业摄影师在操场跑道旁架设相机，开创了实验科学的新范式。",
                "pinyin": "Wèile yànzhèng biànlùn zhōng de xuéshù jiǎshuō, Sītǎnfú zhòngjīn pìnqǐng zhuānyè shèyǐngshī zài cāochǎng pǎodào páng jiàshè xiàngjī, kāichuàng le shíyàn kēxué de xīn fànshì.",
                "en": "To verify the hypothesis raised in debate, Stanford hired a photographer to set up cameras beside the track, pioneering experimental science.",
                "es": "Para verificar la hipótesis de su debate, Stanford contrató a un fotógrafo que montó cámaras junto a la pista, inaugurando un hito científico."
            }
        ],
        "collocations": [
            {"hanzi": "辩论赛", "en": "debate competition"},
            {"hanzi": "激烈辩论", "en": "heated debate"},
            {"hanzi": "辩论技巧", "en": "debating skills"},
            {"hanzi": "辩论对手", "en": "debate opponent"},
            {"hanzi": "展开辩论", "en": "launch a debate"},
            {"hanzi": "公开辩论", "en": "public debate"}
        ],
        "idioms": [
            {"hanzi": "唇枪舌剑", "pinyin": "chún qiāng shé jiàn", "meaning_en": "cross verbal swords; fierce verbal battle"},
            {"hanzi": "据理力争", "pinyin": "jù lǐ lì zhēng", "meaning_en": "argue strongly on the basis of reason and justice"},
            {"hanzi": "无可辩驳", "pinyin": "wú kě biànbó", "meaning_en": "indisputable; irrefragable; irrefutable"},
            {"hanzi": "巧舌如簧", "pinyin": "qiǎo shé rú huáng", "meaning_en": "smooth-tongued like a reed instrument; glib-tongued"}
        ],
        "character_decomposition": [
            {
                "character": "辩",
                "pinyin": "biàn",
                "meaning_en": "dispute; debate; argue; distinguish",
                "meaning_es": "debatir; discutir; distinguir; defender",
                "radical": "辛",
                "radical_meaning_en": "bitter / acrid",
                "meaning_component": "辛 (punishment/dispute between two parties) + 讠 (speech)",
                "sound_component": "辡 (biàn, two accusers confronting each other)",
                "stroke_count": 16,
                "composition_type": "左中右结构",
                "etymology_and_mnemonic": "Ideogram showing spoken words 讠 delivered between two opposing litigants 辛 confronting each other in court.",
                "visual_mnemonic_story_en": "Clear words of truth (讠) stand between two contentious litigants (辛 辛) to debate and settle justice (辩).",
                "visual_mnemonic_story_es": "La palabra elocuente (讠) media entre dos litigantes acusadores (辛 辛) para debatir con justicia (辩).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YJYRJ",
                "traditional": "辯"
            },
            {
                "character": "论",
                "pinyin": "lùn",
                "meaning_en": "discuss; discourse; debate; theory",
                "meaning_es": "discutir; tratar; teoría; debatir",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (speech/words)",
                "sound_component": "仑 (lún, orderly bamboo slips)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken argument 讠 structured systematically like ordered bamboo records 仑.",
                "visual_mnemonic_story_en": "Spoken words (讠) are laid out with systematic logical order like bamboo slips (仑) in reasoned debate (论).",
                "visual_mnemonic_story_es": "Palabras reflexivas (讠) se ordenan como legajos (仑) para sostener una argumentación sólida (论).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVOP",
                "traditional": "論"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Deliver articulate speech between litigants (辩) with systematic logical discourse (论) to win the formal debate (辩论).",
            "composite_memory_hook_es": "Defiende tu postura entre partes (辩) ordenando tus palabras con lógica (论) para vencer en el debate (辩论).",
            "cultural_and_cognitive_roots": "Central to the ancient School of Names (名家, e.g., Hui Shi and Gongsun Long); 'biàn' was the art of distinguishing truth from falsehood via systematic logical propositions.",
            "tone_sandhi_and_pitch_modulation": "Two falling tones: 'biàn lùn' (51-51). Articulate both syllables with decisive, authoritative descending contours."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "辨", "pinyin": "biàn", "meaning_en": "distinguish; discern", "distinction_note": "Has knife radical 刂 in center between two 辛 instead of 讠"},
                {"character": "瓣", "pinyin": "bàn", "meaning_en": "petal; slice", "distinction_note": "Has melon radical 瓜 in center between two 辛"},
                {"character": "辫", "pinyin": "biàn", "meaning_en": "braid; pigtail", "distinction_note": "Has silk radical 纟 in center between two 辛"},
                {"character": "轮", "pinyin": "lún", "meaning_en": "wheel", "distinction_note": "Has vehicle radical 车 on left of 仑"}
            ],
            "etymological_cognates": [
                {"character": "诉", "pinyin": "sù", "gloss_en": "plead; tell court; accuse"},
                {"character": "析", "pinyin": "xī", "gloss_en": "dissect; analyze logic"},
                {"character": "述", "pinyin": "shù", "gloss_en": "state; narrate reasons"},
                {"character": "驳", "pinyin": "bó", "gloss_en": "rebut; dispute opposing side"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "辩论 refers to formal, rule-bound intellectual debate emphasizing logic, rhetoric, and systematic rebuttal.",
            "contrasts": [
                {"id": "1", "compared_word": "辩论 vs. 争论", "pinyin": "zhēnglùn", "analysis": "争论 refers to contentious ideological friction or emotional disputes in daily life, while 辩论 refers to structured formal debates with rules and evidence."},
                {"id": "2", "compared_word": "辩论 vs. 讨论", "pinyin": "tǎolùn", "analysis": "讨论 aims at consensus-building, while 辩论 pits two opposing affirmative and negative camps against each other."},
                {"id": "3", "compared_word": "辩论 vs. 争吵", "pinyin": "zhēngchǎo", "analysis": "争吵 is irrational, noisy bickering, while 辩论 demands disciplined rational argumentation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "辩论的魅力绝不在于用言辞压制对手，而在于通过逻辑的交锋照亮真理的轮廓。站在辩论台前，思维在电光石火间高速运转，每一个论点的立与破，都要求极高的敏锐度。优秀的辩手懂得倾听，在交锋中展现出包容的智慧。",
                "pinyin": "Biànlùn de mèilì jué bú zàiyú yòng yáncí yāzhì duìshǒu, ér zàiyú tōngguò luóji de jiāofēng zhàoliàng zhēnlǐ de lúnkuò. Zhàn zài biànlùntái qián, sīwéi zài diànguāng-shíhuǒ jiān gāosù yùnzhuǎn, měi yí ge lùndiǎn de lì yǔ pò, dōu yāoqiú jí gāo de mǐnruìdù. Yōuxiù de biànshǒu dǒngdé qīngtīng, zài jiāofēng zhōng zhǎnxiàn chū bāoróng de zhìhuì.",
                "en": "The charm of debate lies not in crushing opponents, but illuminating truth through logic. At the podium, thought runs like lightning; establishing or refuting arguments demands acuity. Great debaters listen well, showing inclusive wisdom.",
                "es": "La gracia del debate no estriba en avasallar al rival, sino en alumbrar la verdad con la lógica. Ante el atril, el ingenio vuela como el rayo; sostener o rebatir premisas exige lucidez. El buen orador sabe escuchar e integrar razones."
            },
            {
                "id": "#2",
                "hanzi": "在现代法治社会中，法庭辩论是查明案件事实与维护司法公正的关键程序。控辩双方围绕涉案证据的真实性、合法性与关联性展开法理辩论，法官依据严谨的庭审调查作出公正判决。规范透明的辩论机制，切实捍卫了法律的权威与尊严。",
                "pinyin": "Zài xiàndài fǎzhì shèhuì zhōng, fǎtíng biànlùn shì chámíng ànjiàn shíshí yǔ wéihù sīfǎ gōngzhèng de guānjiàn chéngxù. Kòng-biàn shuāngfāng wéirào shè'àn zhèngjù de zhēnshíxìng, héfǎxìng yǔ guāanliánxìng zhǎnkāi fǎlǐ biànlùn, fǎguān yījù yánjǐn de tíngshěn diàochá zuòchū gōngzhèng pànjué. Guīfàn tòumíng de biànlùn jīzhì, qièshí hànwèi le fǎlǜ de quánwēi yǔ zūnyán.",
                "en": "In modern rule of law, courtroom debate is pivotal for determining facts and justice. Prosecution and defense debate evidence veracity and legality, allowing judges to rule fairly. Transparent debate procedures uphold the law's dignity.",
                "es": "En el Estado de derecho, el careo procesal es crucial para esclarecer los hechos. Fiscales y letrados debaten la validez de las pruebas para que el tribunal dicte sentencia justa. La transparencia del debate afianza el imperio de la ley."
            }
        ]
    },

    # 07 青蛙
    {
        "id": "7",
        "hanzi": "青蛙",
        "pinyin": "qīng wā",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "frog; amphibian (known as beneficial insect-eater)",
            "es": "rana; anfibio anuro comedor de plagas"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "tailless amphibious animal known for jumping, croaking, and eating agricultural pests",
                "definition_es": "anfibio anuro de piel verdosa, patas traseras largas para saltar y voz característica que devora plagas agrícolas",
                "example_phrase": "池塘里的青蛙 (frogs in the pond)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "夏夜的稻田里蛙声一片，绿油油的青蛙蹲在荷叶上捕捉害虫，是农家最好的天然卫士。",
                "pinyin": "Xiàyè de dàotián lǐ wāshēng yípiàn, lǜyóuyóu de qīngwā dūn zài héyè shàng bǔzhuō hàichóng, shì nóngjiā zuì hǎo de tiānrán wèishì.",
                "en": "On summer nights, the paddy fields resound with croaking; bright green frogs squat on lotus leaves catching pests, the farmers' finest natural guardians.",
                "es": "En las noches estivales, los arrozales vibran con el croar; ranas verdosas apostadas en las hojas de loto cazan insectos, fieles guardianas del campo."
            },
            {
                "id": "#2",
                "hanzi": "在现代生物生理学课堂上，老师常以青蛙神经反射实验为例，生动讲解动物神经传导的基本机理。",
                "pinyin": "Zài xiàndài shēngwù shēnglǐxué kètáng shàng, lǎoshī cháng yǐ qīngwā shénjīng fǎnshè shíyàn wéi lì, shēngdòng jiǎngjiě dòngwù shénjīng chuándǎo de jīběn jīlǐ.",
                "en": "In modern physiology classes, teachers frequently use frog nerve reflex experiments to explain basic mechanisms of animal neural transmission.",
                "es": "En las clases de fisiología, los profesores emplean reflejos nerviosos de rana para ilustrar la transmisión de impulsos en los animales."
            }
        ],
        "collocations": [
            {"hanzi": "小青蛙", "en": "little frog"},
            {"hanzi": "青蛙叫", "en": "croaking of frogs"},
            {"hanzi": "井底之蛙", "en": "frog in the bottom of a well (narrow worldview)"},
            {"hanzi": "青蛙跳", "en": "frog jump/leap"},
            {"hanzi": "青蛙产卵", "en": "frogs laying eggs"},
            {"hanzi": "保护青蛙", "en": "protect frogs"}
        ],
        "idioms": [
            {"hanzi": "井底之蛙", "pinyin": "jǐng dǐ zhī wā", "meaning_en": "a frog at the bottom of a well; person of narrow outlook and shallow experience"},
            {"hanzi": "沉鱼落雁", "pinyin": "chén yú luò yàn", "meaning_en": "sinking fish and falling geese; enchanting female beauty"},
            {"hanzi": "蛙鸣蝉噪", "pinyin": "wā míng chán zào", "meaning_en": "croaking frogs and buzzing cicadas; clamorous annoying din"},
            {"hanzi": "井蛙之见", "pinyin": "jǐng wā zhī jiàn", "meaning_en": "shallow, narrow view of a frog in a well"}
        ],
        "character_decomposition": [
            {
                "character": "青",
                "pinyin": "qīng",
                "meaning_en": "green; blue; verdant; young; youth",
                "meaning_es": "verde; azul; lozano; joven; juventud",
                "radical": "青",
                "radical_meaning_en": "green/blue",
                "meaning_component": "生 (plant sprout budding)",
                "sound_component": "丹 (red cinnabar mine / contrasting color)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of green plant shoots 生 sprouting from the earth, representing verdant green color and spring youth.",
                "visual_mnemonic_story_en": "Fresh plant sprouts (生) burst from the dark soil, clothing the world in verdant green (青).",
                "visual_mnemonic_story_es": "Brotes tiernos (生) germinan de la tierra fértil, tiñendo el paisaje de verde lozano (青).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QMB",
                "traditional": ""
            },
            {
                "character": "蛙",
                "pinyin": "wā",
                "meaning_en": "frog; toad; amphibian",
                "meaning_es": "rana; sapo; batracio",
                "radical": "虫",
                "radical_meaning_en": "insect / creature",
                "meaning_component": "虫 (creature/crawler/amphibian)",
                "sound_component": "圭 (guī, jade tablet / onomatopoeia for croaking 'wa')",
                "stroke_count": 12,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining creature radical 虫 with 圭 simulating the rhythmic croak 'wa' of frogs.",
                "visual_mnemonic_story_en": "A green marsh creature (虫) croaks rhythmically by the royal jade boundary (圭), leaping as a frog (蛙).",
                "visual_mnemonic_story_es": "Un anfibio de laguna (虫) croa con compás junto a las lindes (圭), saltando como una rana (蛙).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "LIGG",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The verdant green (青) amphibian creature (蛙) leaps through the paddies catching pests as a beneficial frog (青蛙).",
            "composite_memory_hook_es": "El batracio de piel verde lozana (青) que croa en las charcas (蛙) es la beneficiosa rana (青蛙).",
            "cultural_and_cognitive_roots": "A cherished seasonal motif in traditional Chinese literature (辛弃疾: '听取蛙声一片'); celebrated in agriculture as an ally of farmers and indicator of clean freshwater ecosystems.",
            "tone_sandhi_and_pitch_modulation": "Two level high tones: 'qīng wā' (55-55). Hold both syllables on a steady, high melodic plateau."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "晴", "pinyin": "qíng", "meaning_en": "clear sunny weather", "distinction_note": "Has sun radical 日 on left instead of standalone 青"},
                {"character": "清", "pinyin": "qīng", "meaning_en": "clear; clean", "distinction_note": "Has water radical 氵 on left of 青"},
                {"character": "娃", "pinyin": "wá", "meaning_en": "baby; child", "distinction_note": "Has woman radical 女 on left instead of 虫 in 蛙"},
                {"character": "洼", "pinyin": "wā", "meaning_en": "low-lying hollow", "distinction_note": "Has water radical 氵 on left instead of 虫"}
            ],
            "etymological_cognates": [
                {"character": "蟾", "pinyin": "chán", "gloss_en": "toad; moon toad in folklore"},
                {"character": "蜍", "pinyin": "chú", "gloss_en": "toad species"},
                {"character": "蝌", "pinyin": "kē", "gloss_en": "tadpole; frog larvae"},
                {"character": "蚪", "pinyin": "dǒu", "gloss_en": "tadpole tail"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "青蛙 denotes the green, jumping, insectivorous anuran amphibian living near ponds and paddies.",
            "contrasts": [
                {"id": "1", "compared_word": "青蛙 vs. 蟾蜍", "pinyin": "chánchú", "analysis": "蟾蜍 (toad / 癞蛤蟆) has warty skin, shorter legs for crawling, and lives on dry land, while 青蛙 has smooth green skin and webbed jumping feet."},
                {"id": "2", "compared_word": "青蛙 vs. 蝌蚪", "pinyin": "kēdǒu", "analysis": "蝌蚪 is the aquatic tadpole larval stage of the frog with a tail and gills, prior to metamorphosis into a 青蛙."},
                {"id": "3", "compared_word": "青蛙 vs. 牛蛙", "pinyin": "niúwā", "analysis": "牛蛙 is the massive American bullfrog species farmed commercially for meat, distinct from the common native farm frog 青蛙."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "“稻花香里说丰年，听取蛙声一片。”宋代词人笔下的田园夏夜，总少不了青蛙那生机勃勃的合唱。在清风微拂的荷塘边，几只碧绿的青蛙伏在荷叶上静静守候，偶有飞虫掠过便迅捷一跃，勾勒出人与自然和谐共生的宁静诗画。",
                "pinyin": "'Dàohuā xiāng lǐ shuō fēngnián, tīngqǔ wāshēng yípiàn.' Sòngdài círén bǐxià de tiányuán xiàyè, zǒng shǎobùliǎo qīngwā nà shēngjī-bóbó de héchàng. Zài qīngfēng wēifú de hétáng biān, jǐ zhī bìlǜ de qīngwā fú zài héyè shàng jìngjìng shǒuhòu, ǒu yǒu fēichóng lüèguò biàn xùnjié yí yuè, gōulè chū rén yǔ zìrán héxié-gòngshēng de níngjìng shīhuà.",
                "en": "'Fragrance of rice flowers speaks of harvest, listening to croaking frogs.' Song dynasty verses capture summer nights. Green frogs wait on lotus pads, leaping at insects, painting a peaceful portrait of humans in harmony with nature.",
                "es": "'El aroma del arroz presagia cosecha entre el concierto de las ranas'. En los versos Song resuena la noche estival. Las ranas descansan sobre hojas de loto y cazan al vuelo, pintando la armonía entre el hombre y el campo."
            },
            {
                "id": "#2",
                "hanzi": "青蛙作为农田湿地生态系统的重要指示物种，对农药残留与水体污染极为敏感。近年来，农业部门大力推广生态绿色种植，大幅减少化学杀虫剂用量，为青蛙等有益两栖动物创造了健康的生存繁衍空间，有效恢复了农田生物多样性。",
                "pinyin": "Qīngwā zuòwéi nóngtián shīdì shēngtài xìtǒng de zhòngyào zhǐshì wùzhǒng, duì nóngyào cánliú yǔ shuǐtǐ wūrǎn jíwéi mǐngǎn. Jìnniánlái, nóngyè bùmén dàlì tuīguǎng shēngtài lǜsè zhòngzhí, dàfú jiǎnshǎo huàxué shāchóngjì yòngliàng, wèi qīngwā děng yǒuyì liǎngqī dòngwù chuàngzào le jiànkāng de shēngcún fányǎn kōngjiān, yǒuxiào huīfù le nóngtián shēngwù duōyàngxìng.",
                "en": "As a bio-indicator of wetland health, frogs are sensitive to pesticides and pollution. Promoting organic farming and curbing chemicals creates safe breeding habitats for amphibians, restoring agricultural biodiversity.",
                "es": "Como bioindicador de los humedales, la rana es muy sensible a pesticidas y aguas turbias. Fomentar la agricultura ecológica y reducir tóxicos recupera su hábitat reproductor, restableciendo la biodiversidad en los cultivos."
            }
        ]
    },

    # 08 啦
    {
        "id": "8",
        "hanzi": "啦",
        "pinyin": "la",
        "part_of_speech": "Particle",
        "meanings_summary": {
            "en": "modal particle fusion of 了 (le) and 啊 (a) marking exclamation, finality, or excitement",
            "es": "partícula modal fusión de 了 y 啊 que denota júbilo, cambio de estado o aviso"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Particle",
                "register": "Colloquial / Standard",
                "definition_en": "sentence-final modal particle expressing completed change of state merged with lively exclamatory emotion",
                "definition_es": "partícula modal al final de frase que denota la consumación de un cambio unida a exclamación viva o júbilo",
                "example_phrase": "下雪啦 (it is snowing!)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "下课铃声一响，操场上顿时热闹起来，孩子们欢呼雀跃地喊道：“放假啦！放假啦！”",
                "pinyin": "Xiàkè língshēng yì xiǎng, cāochǎng shàng dùnshí rènào qǐlái, háizimen huānhū-quèyuè de hǎndào: 'Fàngjià la! Fàngjià la!'",
                "en": "As soon as the bell rang, the playground bustled as children cheered joyfully: 'Vacation has started! Vacation is here!'",
                "es": "Al sonar el timbre, el patio se llenó de algarabía mientras los niños gritaban con júbilo: '¡Llegaron las vacaciones! ¡Vacaciones!'."
            },
            {
                "id": "#2",
                "hanzi": "经过反复调试实验装置，摄影师兴奋地大喊：“奇迹出现啦！静止的马片连成会跑的活马啦！”",
                "pinyin": "Jīngguò fǎnfù tiáoshì shíyàn zhuāngzhì, shèyǐngshī xīngfèn de dàhǎn: 'Qíjì chūxiàn la! Jìngzhǐ de mǎpiàn liánchéng huì pǎo de huómǎ la!'",
                "en": "After repeatedly calibrating the apparatus, the photographer shouted in excitement: 'The miracle has happened! The pictures have turned into a running horse!'",
                "es": "Tras ajustar el aparato, el fotógrafo gritó entusiasmado: '¡Ocurrió el milagro! ¡Las fotos fijas se han convertido en un caballo al galope!'."
            }
        ],
        "collocations": [
            {"hanzi": "快来啦", "en": "come quickly!"},
            {"hanzi": "知道啦", "en": "I know now!"},
            {"hanzi": "好啦", "en": "all right; that's enough"},
            {"hanzi": "算啦", "en": "forget it; let it drop"},
            {"hanzi": "成功啦", "en": "we succeeded!"},
            {"hanzi": "回家啦", "en": "going home now!"}
        ],
        "idioms": [
            {"hanzi": "大快人心", "pinyin": "dà kuài rén xīn", "meaning_en": "afford universal satisfaction; delight everyone"},
            {"hanzi": "皆大欢喜", "pinyin": "jiē dà huān xǐ", "meaning_en": "to the delight of all involved; universal joy"},
            {"hanzi": "欢天喜地", "pinyin": "huān tiān xǐ dì", "meaning_en": "overjoyed with heavenly rejoicing"},
            {"hanzi": "喜上眉梢", "pinyin": "xǐ shàng méi shāo", "meaning_en": "joy beaming on one's eyebrows"}
        ],
        "character_decomposition": [
            {
                "character": "啦",
                "pinyin": "la",
                "meaning_en": "modal particle le + a; exclamation",
                "meaning_es": "partícula modal le + a; exclamación",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth expressing sound)",
                "sound_component": "拉 (lā, pull / phonetic harmony)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic fusion particle where mouth radical 口 utters the merged phonetic contraction of 了 (le) and 啊 (a).",
                "visual_mnemonic_story_en": "An open mouth (口) pulls (拉) out a cheerful exclamation, shouting 'hurrah!' (啦).",
                "visual_mnemonic_story_es": "Una boca abierta (口) suelta una alegre exclamación (拉) festejando un desenlace (啦).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RYT",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Open your mouth (口) and pull out (拉) a joyful shout merging change of state and delight into a vibrant particle (啦).",
            "composite_memory_hook_es": "Abre la boca (口) y entona (拉) un grito de júbilo que une el cambio de estado y el asombro (啦).",
            "cultural_and_cognitive_roots": "A phonological fusion morpheme (合音字) originating in Song and Yuan vernacular drama; contracts 'le' (completed aspect) with 'a' (affective particle) into a single lively syllable.",
            "tone_sandhi_and_pitch_modulation": "Neutral tone: 'la' (pitch 2 or 5 depending on preceding tone). Short, light, unstressed musical cadence at the tail of sentences."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "拉", "pinyin": "lā", "meaning_en": "pull; drag", "distinction_note": "Has hand radical 扌 on left instead of mouth 口 in 啦"},
                {"character": "垃", "pinyin": "lā", "meaning_en": "garbage", "distinction_note": "Has earth radical 土 on left of 立 and 十"},
                {"character": "粒", "pinyin": "lì", "meaning_en": "grain", "distinction_note": "Has rice radical 米 on left of 立"},
                {"character": "哈", "pinyin": "hā", "meaning_en": "laughter", "distinction_note": "Has 合 on right instead of 拉"}
            ],
            "etymological_cognates": [
                {"character": "了", "pinyin": "le", "gloss_en": "aspect particle; completed change"},
                {"character": "啊", "pinyin": "a", "gloss_en": "exclamatory modal particle"},
                {"character": "呢", "pinyin": "ne", "gloss_en": "continuative question particle"},
                {"character": "嘛", "pinyin": "ma", "gloss_en": "obvious emphatic particle"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "啦 is a colloquial sentence-final modal particle expressing lively completion, sudden joy, relief, or an alert.",
            "contrasts": [
                {"id": "1", "compared_word": "啦 vs. 了", "pinyin": "le", "analysis": "了 is a neutral grammatical aspect/modal particle without emotional coloring, whereas 啦 adds lively exclamatory warmth ('下雨了' vs. '下雨啦!')."},
                {"id": "2", "compared_word": "啦 vs. 吧", "pinyin": "ba", "analysis": "吧 expresses suggestion, hesitation, or gentle conjecture ('走吧'), while 啦 announces a realized fact with gusto ('来啦')."},
                {"id": "3", "compared_word": "啦 vs. 吗", "pinyin": "ma", "analysis": "吗 strictly forms yes-no interrogative questions, while 啦 is affirmative or exclamatory."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "冬去春来，当第一抹嫩绿悄悄爬上枝头，枝头上的燕子开始筑巢，田埂上的孩子们脱下厚重的棉袄欢呼：“春天来啦！春天来啦！”那稚嫩清脆的欢呼声在春风里回荡，唤醒了沉睡的大地，吹散了漫长冬日的所有严寒。",
                "pinyin": "Dōngqù-chūnlái, dāng dì-yī mǒ nènlǜ qiāoqiāo pá shàng zhītóu, zhītóu shàng de yànzi kāishǐ zhùcháo, tiángěng shàng de háizimen tuōxià hòuzhòng de mián'ǎo huānhū: 'Chūntiān lái la! Chūntiān lái la!' Nà zhìnèn qīngcuì de huānhūshēng zài chūnfēng lǐ huídàng, huànxǐng le chénsùi de dàdì, chuīsàn le màncháng dōngrì de suǒyǒu yánhán.",
                "en": "Winter fades into spring; as the first green climbs twigs and swallows nest, kids strip off coats cheering: 'Spring is here! Spring is here!' That youthful cheer echoes in the breeze, awakening the earth and scattering winter chills.",
                "es": "Se va el invierno y brotan las yemas; al anidar las golondrinas, los niños se quitan los abrigos gritando: '¡Llegó la primavera! ¡Ya está aquí!'. Sus risas limpias despiertan los campos, disipando la frialdad invernal."
            },
            {
                "id": "#2",
                "hanzi": "科研攻关是一段漫长而艰辛的跋涉。经过成百上千次的失败与摸索，当计算机屏幕上最终跳出完美吻合的测试曲线时，整个实验室里顿时爆发出一片沸腾的欢呼声：“我们成功啦！这项技术终于突破啦！”所有的心血在此刻化作了自豪的泪水。",
                "pinyin": "Kēyán gōngguān shì yí duàn màncháng ér jiānxīn de báshè. Jīngguò chéngbǎi-shàngqiān cì de shībài yǔ mōsuǒ, dāng jìsuànjī píngmù shàng zuìzhōng tiàochū wánměi wènhé de cèshì qūxiàn shí, zhěng gè shíyànshì lǐ dùnshí bàofā chū yí piàn fèiténg de huānhūshēng: 'Wǒmen chénggōng la! Zhè xiàng jìshù zhōngyú tūpò la!' Suǒyǒu de xīnxuè zài cǐkè huàzuò le zìháo de lèishuǐ.",
                "en": "Scientific research is an arduous journey. After hundreds of failures, when computer screens display matching test curves, the lab erupts into cheers: 'We succeeded! The breakthrough is here!' Years of toil turn into tears of pride.",
                "es": "La investigación científica es una ardua senda. Tras incontables ensayos, cuando la pantalla muestra la curva perfecta de datos, el laboratorio prorrumpe en vítores: '¡Lo logramos! ¡Se hizo el hallazgo!'. El desvelo deviene júbilo."
            }
        ]
    },

    # 09 始终
    {
        "id": "9",
        "hanzi": "始终",
        "pinyin": "shǐ zhōng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "from beginning to end; all along; throughout; invariably",
            "es": "de principio a fin; en todo momento; invariablemente; desde el comienzo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "continuously and consistently throughout the entire process from start to finish",
                "definition_es": "de manera continua y constante a lo largo de todo el proceso de principio a fin",
                "example_phrase": "始终保持冷静 (remain calm throughout)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "面对突如其来的危机与复杂的舆论风波，团队负责人始终保持沉着冷静，有条不紊地组织应对。",
                "pinyin": "Miànduì tūrúqílái de wēijī yǔ fùzá de yúlùn fēngbō, tuánduì fùzérén shǐzhōng bǎochí chénzhuó lěngjìng, yǒutiáo-bùwěn de zǔzhī yìngduì.",
                "en": "Facing unexpected crises and complex media storms, the team leader remained calm and composed throughout, organizing responses in an orderly manner.",
                "es": "Ante la repentina crisis y las habladurías, el líder del equipo mantuvo la serenidad en todo momento, organizando la respuesta con temple."
            },
            {
                "id": "#2",
                "hanzi": "在长达数年的学术论战中，斯坦福始终坚信马奔跑时四个蹄子会同时腾空，并最终用实验相片证实了自己的判断。",
                "pinyin": "Zài chángdá shù nián de xuéshù lùnzhàn zhōng, Sītǎnfú shǐzhōng jiānxìn mǎ bēnpǎo shí sì ge tízi huì tóngshí téngkōng, bìng zuìzhōng yòng shíyàn xiàngpiàn zhèngshí le zìjǐ de pànduàn.",
                "en": "In years of debate, Stanford firmly believed all along that a galloping horse's four hooves leave the ground, ultimately proving his judgment with photos.",
                "es": "Durante años de controversia, Stanford sostuvo de principio a fin que el caballo suspendía sus cuatro cascos, probando su tesis con fotos."
            }
        ],
        "collocations": [
            {"hanzi": "始终坚持", "en": "persist from start to finish"},
            {"hanzi": "始终保持", "en": "maintain throughout"},
            {"hanzi": "始终如一", "en": "consistent from beginning to end"},
            {"hanzi": "始终不渝", "en": "unswerving all along"},
            {"hanzi": "始终未能", "en": "failed all along to"},
            {"hanzi": "贯穿始终", "en": "run through from start to finish"}
        ],
        "idioms": [
            {"hanzi": "始终如一", "pinyin": "shǐ zhōng rú yī", "meaning_en": "consistent and steadfast from beginning to end"},
            {"hanzi": "始终不渝", "pinyin": "shǐ zhōng bù yú", "meaning_en": "unswerving, unflagging, and steadfast throughout"},
            {"hanzi": "善始善终", "pinyin": "shàn shǐ shàn zhōng", "meaning_en": "start well and end well; carry through conscientiously to the end"},
            {"hanzi": "贯彻始终", "pinyin": "guàn chè shǐ zhōng", "meaning_en": "run continuously through from inception to finish"}
        ],
        "character_decomposition": [
            {
                "character": "始",
                "pinyin": "shǐ",
                "meaning_en": "begin; start; initial; first",
                "meaning_es": "comenzar; iniciar; principio; origen",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman giving birth to life)",
                "sound_component": "台 (tái, foundation / platform)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient ideogram showing a mother 女 giving birth to offspring, marking the initial beginning 始 of a new human life.",
                "visual_mnemonic_story_en": "A mother (女) on a platform (台) gives birth to a newborn, marking the very beginning (始) of life.",
                "visual_mnemonic_story_es": "Una madre (女) en el tálamo (台) alumbra a su criatura, señalando el principio y origen (始) de la vida.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "VIR",
                "traditional": ""
            },
            {
                "character": "终",
                "pinyin": "zhōng",
                "meaning_en": "end; finish; death; final",
                "meaning_es": "fin; concluir; muerte; final",
                "radical": "纟",
                "radical_meaning_en": "silk",
                "meaning_component": "纟 (silk thread reaching end)",
                "sound_component": "夂 (zhǐ, following foot / conclusion)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where a silk thread 纟 reaches its terminal knot 夂, meaning conclusion and finish.",
                "visual_mnemonic_story_en": "A spun silk thread (纟) is tied off with a firm final knot (夂) at its finish (终).",
                "visual_mnemonic_story_es": "El hilo de seda (纟) se remata con un nudo firme (夂) alcanzando su final (终).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "VMHEY",
                "traditional": "終"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "From the very beginning of life (始) to the final tying of the knot (终), persist all along (始终).",
            "composite_memory_hook_es": "Desde el primer inicio (始) hasta el nudo final (终), manténte firme en todo momento (始终).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese polar compounds (antonym pairing: 始 start + 终 end); encapsulates the Confucian moral virtue of steadfast perseverance without wavering.",
            "tone_sandhi_and_pitch_modulation": "Dipping tone followed by level high tone: 'shǐ zhōng' (214-55). Dip fully on 'shǐ', then leap to an elevated level high tone on 'zhōng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "胎", "pinyin": "tāi", "meaning_en": "fetus; tire", "distinction_note": "Has flesh radical 月 on left instead of woman 女 in 始"},
                {"character": "治", "pinyin": "zhì", "meaning_en": "govern; cure", "distinction_note": "Has water radical 氵 on left instead of 女"},
                {"character": "钟", "pinyin": "zhōng", "meaning_en": "clock; bell", "distinction_note": "Has metal radical 钅 on left instead of 纟 in 终"},
                {"character": "冬", "pinyin": "dōng", "meaning_en": "winter", "distinction_note": "Has two dots at bottom instead of 纟"}
            ],
            "etymological_cognates": [
                {"character": "初", "pinyin": "chū", "gloss_en": "initial; cut cloth at beginning"},
                {"character": "末", "pinyin": "mò", "gloss_en": "tip; end; ultimate branch"},
                {"character": "恒", "pinyin": "héng", "gloss_en": "constant; unchanging moon"},
                {"character": "总", "pinyin": "zǒng", "gloss_en": "always; gather all strands"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "始终 emphasizes unwavering continuity throughout an entire chronological timeline from start to finish.",
            "contrasts": [
                {"id": "1", "compared_word": "始终 vs. 一直", "pinyin": "yìzhí", "analysis": "一直 is a common colloquial adverb for continuous action or direction ('一直往前走'), while 始终 is formal and emphasizes steadfast consistency across a completed duration."},
                {"id": "2", "compared_word": "始终 vs. 从来", "pinyin": "cónglái", "analysis": "从来 emphasizes habitual custom or negative absolutes ('从来不吃肉'), while 始终 emphasizes maintaining a constant state throughout an ordeal."},
                {"id": "3", "compared_word": "始终 vs. 最终", "pinyin": "zuìzhōng", "analysis": "最终 solely marks the final terminal result ('最终获胜'), while 始终 covers the entire span from beginning to end."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "人这一辈子，最难能可贵的品格就是始终如一。当身处顺境繁花似锦时，不骄不躁保持谦逊；当身处逆境风雨交加时，不气不馁坚守初心。无论外界环境如何变幻，内心始终保有一方净土，这才是最强大的人生定力。",
                "pinyin": "Rén zhè yíbèizi, zuì nánnéng-kěguì de pǐngé jiùshì shǐzhōng-rúyī. Dāng shēnchǔ shùnjìng fánhuā-sìjǐn shí, bùjiāo-bùzào bǎochí qiānxùn; dāng shēnchǔ nìjìng fēngyǔ-jiāojiā shí, bùqì-bùněi jiānshǒu chūxīn. Wúlùn wàijiè huánjìng rúhé biànhuàn, nèixīn shǐzhōng bǎoyǒu yì fāng jìngtǔ, zhè cáishì zuì qiángdà de rénshēng dìnglì.",
                "en": "In life, the rarest virtue is consistency from beginning to end. Staying humble in prosperity and steadfast in adversity. Whatever changes outside, keeping a pure sanctuary within all along is life's greatest composure.",
                "es": "La mayor virtud en la vida es la constancia de principio a fin. Guardar la humildad en el triunfo y la entereza en la adversidad. Mudarán los tiempos, pero conservar limpia la propia conciencia en todo momento otorga serenidad invencible."
            },
            {
                "id": "#2",
                "hanzi": "中国在国际事务中始终奉行独立自主的和平外交政策。坚定维护以联合国宪章宗旨为核心的国际秩序，始终坚持通过平等对话协商化解地缘政治分歧。中国致力于推动构建人类命运共同体，始终做世界和平的建设者与全球发展的贡献者。",
                "pinyin": "Zhōngguó zài guójì shìwù zhōng shǐzhōng fèngxíng dúlì-zìzhǔ de hépíng wàijiāo zhèngcè. Jiāndìng wéihù yǐ Liánhéguó xiànzhāng zōngzhǐ wéi héxīn de guójì zhìxù, shǐzhōng jiānchí tōngguò píngděng duìhuà xiéshāng huàjiě dìyuán zhèngzhì fēnqí. Zhōngguó zhìlì yú tuīdòng gòujiàn rénlèi mìngyùn gòngtóngtǐ, shǐzhōng zuò shìjiè hépíng de jiànshèzhě yǔ quánqiú fāzhǎn de gòngxiànzhě.",
                "en": "China has invariably pursued an independent foreign policy of peace in international affairs. Defending the UN Charter and resolving disputes through dialogue, it remains a builder of peace and contributor to global development all along.",
                "es": "China sostiene en todo momento una diplomacia pacífica e independiente. Defiende la Carta de la ONU y aboga por el diálogo sin fisuras para resolver tensiones, consolidándose invariablemente como constructora de concordia mundial."
            }
        ]
    },

    # 10 脖子
    {
        "id": "10",
        "hanzi": "脖子",
        "pinyin": "bó zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "neck; cervix (of human or animal body)",
            "es": "cuello; cerviz; pescuezo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the part of the body connecting the head to the shoulders and torso in humans and animals",
                "definition_es": "parte del cuerpo que une la cabeza con el tronco en personas y animales",
                "example_phrase": "伸长脖子 (crane one's neck)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "长时间低头看手机或伏案工作，极易导致颈椎酸痛，建议大家工作一小时后适度活动活动脖子。",
                "pinyin": "Cháng shíjiān dītóu kàn shǒujī huò fú'àn gōngzuò, jí yì dǎozhì jǐngzhuī suāntòng, jiànyì dàjiā gōngzuò yì xiǎoshí hòu shìdù huódòng huodong bózi.",
                "en": "Bending down to look at screens or desks for hours causes neck aches; taking breaks every hour to stretch your neck is recommended.",
                "es": "Mirar el móvil agachado o pasar horas ante la pantalla sobrecarga las cervicales; conviene estirar el cuello tras una hora de labor."
            },
            {
                "id": "#2",
                "hanzi": "辩论场上双方各执己见互不相让，争论得面红脖子粗，谁也不肯轻易放弃自己的学术立场。",
                "pinyin": "Biànlùnchǎng shàng shuāngfāng gèzhí-jǐjiàn hùbù-xiāngràng, zhēnglùn de miànhóng-bózicū, shéi yě bù kěn qīngyì fàngqì zìjǐ de xuéshù lìchǎng.",
                "en": "On the debate floor, both sides held their ground stubbornly, arguing until red in the face with veins bulging on necks, yielding to none.",
                "es": "En el debate, ambas partes se enrocaron en sus posturas, disputando hasta ponerse rojos y con las venas del cuello hinchadas sin ceder un ápice."
            }
        ],
        "collocations": [
            {"hanzi": "伸长脖子", "en": "crane one's neck"},
            {"hanzi": "缩着脖子", "en": "huddle one's neck in the cold"},
            {"hanzi": "卡脖子", "en": "stranglehold; choke point (technological bottleneck)"},
            {"hanzi": "脖子酸痛", "en": "sore neck / stiff neck"},
            {"hanzi": "摸摸脖子", "en": "touch one's neck"},
            {"hanzi": "脸红脖子粗", "en": "red in the face with neck veins bulging in anger/argument"}
        ],
        "idioms": [
            {"hanzi": "延颈企踵", "pinyin": "yán jǐng qǐ zhǒng", "meaning_en": "crane neck and stand on tiptoe; eagerly anticipate"},
            {"hanzi": "脸红脖子粗", "pinyin": "liǎn hóng bó zi cū", "meaning_en": "flushed red face and swollen neck in furious dispute"},
            {"hanzi": "昂首挺胸", "pinyin": "áng shǒu tǐng xiōng", "meaning_en": "head held high and chest puffed out"},
            {"hanzi": "交头接耳", "pinyin": "jiāo tóu jiē ěr", "meaning_en": "whisper ear to ear secretly"}
        ],
        "character_decomposition": [
            {
                "character": "脖",
                "pinyin": "bó",
                "meaning_en": "neck; scruff",
                "meaning_es": "cuello; pescuezo; cerviz",
                "radical": "月",
                "radical_meaning_en": "moon / flesh",
                "meaning_component": "月 (flesh/body organ)",
                "sound_component": "勃 (bó, vigorous sudden growth / phonetic)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where flesh radical 月 combines with 勃 (vigorous swelling) denoting the muscular neck supporting the head.",
                "visual_mnemonic_story_en": "Fleshy sinews of the body (月) swell vigorously (勃) to form the muscular column of the neck (脖).",
                "visual_mnemonic_story_es": "La carne y los tendones (月) se yerguen con vigor (勃) conformando la firme columna del cuello (脖).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BJBD",
                "traditional": ""
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; child",
                "meaning_es": "sufijo nominal; niño",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "子 (infant child)",
                "sound_component": "子 (zǐ)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Pictogram of an infant; productive unstressed noun suffix in modern Chinese vocabulary.",
                "visual_mnemonic_story_en": "A child (子) stands gracefully; used as a noun suffix to name anatomical parts.",
                "visual_mnemonic_story_es": "Un niño menudo (子); sirve de sufijo para formar nombres de partes del cuerpo.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "ND",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The muscular flesh (脖) supporting the head takes the common noun suffix (子) to form the neck (脖子).",
            "composite_memory_hook_es": "La musculatura carnosa (脖) que sostiene la cabeza lleva el sufijo (子) para designar el cuello (脖子).",
            "cultural_and_cognitive_roots": "Anatomical term; modern political economy adapted 'qiǎ bózǐ' (卡脖子, chokehold on the neck) to describe strategic tech choke points or embargo bottlenecks.",
            "tone_sandhi_and_pitch_modulation": "Rising tone followed by neutral tone: 'bó zi' (35-2). Syllable 'bó' glides upward, followed by a light, unstressed neutral syllable 'zi'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "勃", "pinyin": "bó", "meaning_en": "thriving; vigorous", "distinction_note": "Has 力 on right instead of flesh 月 on left"},
                {"character": "脖", "pinyin": "bó", "meaning_en": "neck", "distinction_note": "Has 月 on left; do not confuse with 脯 (flesh 月 + 甫)"},
                {"character": "肢", "pinyin": "zhī", "meaning_en": "limb", "distinction_note": "Has 支 on right of 月"},
                {"character": "胳", "pinyin": "gē", "meaning_en": "armpit/arm", "distinction_note": "Has 各 on right of 月"}
            ],
            "etymological_cognates": [
                {"character": "颈", "pinyin": "jǐng", "gloss_en": "cervical neck; formal anatomical term"},
                {"character": "项", "pinyin": "xiàng", "gloss_en": "nape of neck; item; heading"},
                {"character": "咽", "pinyin": "yān", "gloss_en": "pharynx; throat passage"},
                {"character": "喉", "pinyin": "hóu", "gloss_en": "larynx; Adam's apple"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "脖子 is the universal everyday colloquial word for the anatomical neck in both humans and animals.",
            "contrasts": [
                {"id": "1", "compared_word": "脖子 vs. 颈部", "pinyin": "jǐngbù", "analysis": "颈部 is a formal, medical, and scientific term ('颈部淋巴结', '颈椎'), while 脖子 is everyday conversational."},
                {"id": "2", "compared_word": "脖子 vs. 咽喉", "pinyin": "yānhóu", "analysis": "咽喉 specifically denotes the internal throat and airway passage, while 脖子 refers to the external visible neck."},
                {"id": "3", "compared_word": "脖子 vs. 项", "pinyin": "xiàng", "analysis": "项 is a classical literary word for the back of the neck/nape ('望其项背'), rarely used alone in spoken Mandarin today."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "寒冬腊月北风呼啸，清晨出门的人们纷纷拉高衣领、紧紧缩起脖子。一条母亲亲手编织的红色羊毛围巾，厚实温暖地缠绕在脖子上，不仅挡住了刺骨的凛冽寒风，更把远方游子与家人的牵挂紧紧相连。那是冬日里最贴心的暖意。",
                "pinyin": "Hándōng-làyuè běifēng hūxiào, qīngchén chūmén de rénmen fēnfēn lāgāo yīlǐng, jǐnjǐn suōqǐ bózi. Yì tiáo mǔqīn qīnshǒu biānzhī de hóngsè yángmáo wéijīn, hòushi wēnduǎn de chánrào zài bózi shàng, bùjǐn dǎngzhù le cìgǔ de lǐnliè hánfēng, gèng bǎ yuǎnfāng yóuzǐ yǔ jiārén de qiānguà jǐnjǐn xiānglián. Nà shì dōngrì lǐ zuì tiēxīn de nuǎnyì.",
                "en": "In deep winter howling winds, people departing in the morning pull up collars and huddle necks. A warm red woolen scarf knit by mother wrapped around the neck blocks biting winds, tying traveler and home together with cozy warmth.",
                "es": "Con el viento helado del invierno, los transeúntes alzan solapas y encogen el cuello. Una bufanda de lana roja tejida por madre rodea el pescuezo, deteniendo la cellisca y uniendo al caminante con el calor familiar."
            },
            {
                "id": "#2",
                "hanzi": "突破关键核心技术“卡脖子”瓶颈，是实现高水平科技自立自强的重中之重。科研院所与领军企业紧密协同，瞄准工业软件、先进光刻机与高端航空轴承等短板领域持续攻关，彻底摆脱核心元器件受制于人的被动局面，筑牢科技安全基石。",
                "pinyin": "Tūpò guānjiàn héxīn jìshù 'qiǎ bózǐ' píngjǐng, shì shíxiàn gāoshuǐpíng kējì zìlì-zìqiáng de zhòngzhōngzhīzhòng. Kēyán yuànsuǒ yǔ lǐngjūn qǐyè jǐnmì xiétóng, miáozhǔn gōngyè ruǎnjiàn, xiānjìn guāngkèjī yǔ gāoduān hángkōng zhóuchéng děng duǎnbǎn lǐngyù chíxù gōngguān, chèdǐ bǎituō héxīn yuánqìjiàn shòuzhìyúrén de bèidòng júmiàn, zhùláo kējì ānquán jīshí.",
                "en": "Breaking through tech bottleneck chokeholds is paramount for self-reliance. Research institutes and leading firms collaborate on industrial software, lithography, and aviation bearings, shaking off dependencies to fortify technological security.",
                "es": "Romper los cuellos de botella en tecnologías críticas es clave para la soberanía técnica. Laboratorios y empresas colaboran en software y litografía avanzada, superando dependencias externas y blindando la seguridad tecnológica."
            }
        ]
    }
]

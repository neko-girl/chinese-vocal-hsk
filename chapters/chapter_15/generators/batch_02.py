# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch2 = [
    # 11 弱
    {
        "id": "11",
        "hanzi": "弱",
        "pinyin": "ruò",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "weak; feeble; inferior; vulnerable; young",
            "es": "débil; vulnerable; frágil; inferior"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "lacking physical strength, military power, firmness, or capability; inferior in strength",
                "definition_es": "que carece de fuerza física, poderío militar o solidez; vulnerable; inferior",
                "example_phrase": "力量薄弱 (power is weak and frail)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在群雄逐鹿的战国时期，诸侯各国弱肉强食，弱小的邦国随时面临被强邻吞并的危险。",
                "pinyin": "Zài qúnxióng-zhúlù de Zhànguó shíqī, zhūhóu gèguó ruòròu-qiángshí, ruòxiǎo de bāngguó suíshí miànlín bèi qiánglín tūnbìng de wēixiǎn.",
                "en": "During the Warring States period, states lived by the law of the jungle; small, weak principalities faced peril of annexation by strong neighbors.",
                "es": "En los Reinos Combatientes imperaba la ley de la selva; los principados débiles afrontaban en todo momento la amenaza de ser anexionados."
            },
            {
                "id": "#2",
                "hanzi": "虽然他在长跑耐力方面相对较弱，但凭借极佳的爆发力在短跑项目中斩获了冠军。",
                "pinyin": "Suīrán tā zài chángpǎo nàilì fāngmiàn xiāngduì jiào ruò, dàn píngjiè jí jiā de bàofālì zài duǎnpǎo xiàngmù zhōng zhǎnhuò le guànjūn.",
                "en": "Although he was relatively weak in long-distance endurance, his explosive sprinting speed secured him the championship.",
                "es": "Aunque su resistencia en fondo era algo débil, su gran potencia de arrancada le permitió coronarse campeón en velocidad."
            }
        ],
        "collocations": [
            {"hanzi": "软弱无力", "en": "weak and powerless"},
            {"hanzi": "弱点缺陷", "en": "weak points and shortcomings"},
            {"hanzi": "以弱胜强", "en": "defeat the strong with the weak"},
            {"hanzi": "敌强我弱", "en": "the enemy is strong while we are weak"},
            {"hanzi": "身体虚弱", "en": "physically frail and weak"},
            {"hanzi": "弱小群体", "en": "vulnerable / weak groups"}
        ],
        "idioms": [
            {"hanzi": "弱肉强食", "pinyin": "ruò ròu qiáng shí", "meaning_en": "the weak are meat for the strong; law of the jungle"},
            {"hanzi": "以弱胜强", "pinyin": "yǐ ruò shèng qiáng", "meaning_en": "defeat a stronger opponent through superior strategy"},
            {"hanzi": "扶弱济困", "pinyin": "fú ruò jì kùn", "meaning_en": "support the weak and relieve the distressed"},
            {"hanzi": "微不足道", "pinyin": "wēi bù zú dào", "meaning_en": "insignificant and negligible; too frail to mention"}
        ],
        "character_decomposition": [
            {
                "character": "弱",
                "pinyin": "ruò",
                "meaning_en": "weak; frail; young; inferior",
                "meaning_es": "débil; frágil; joven; inferior",
                "radical": "弓",
                "radical_meaning_en": "bow",
                "meaning_component": "two limp wooden bows wound with feathers / sinews",
                "sound_component": "弱 (ruò)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Two small, pliable bows decorated with soft feathers; represents pliable frailty and weakness.",
                "visual_mnemonic_story_en": "Two small, flexible archery bows (弓) lacking sufficient tension to launch heavy arrows (弱).",
                "visual_mnemonic_story_es": "Dos arcos ligeros (弓) con escasa tensión en la cuerda para disparar dardos pesados (弱).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NINIM",
                "traditional": "弱"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Two pliable bows wound together (弱) lack the taut power of battle bows, embodying weakness (弱).",
            "composite_memory_hook_es": "Dos arquillos flexibles gemelos (弱) carecen de la tensión férrea de combate, encarnando la debilidad (弱).",
            "cultural_and_cognitive_roots": "Derived from classical archery where youth practiced with light pliant bows before mastering rigid military warbows.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'ruò' (51). Crisp and sharp downward inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "弓", "pinyin": "gōng", "meaning_en": "archery bow", "distinction_note": "Single bow frame without feathers or duplicate"},
                {"character": "引", "pinyin": "yǐn", "meaning_en": "draw; lead", "distinction_note": "Single vertical stroke on right of 弓"},
                {"character": "张", "pinyin": "zhāng", "meaning_en": "stretch; open", "distinction_note": "Long 长 on right of 弓"},
                {"character": "强", "pinyin": "qiáng", "meaning_en": "strong", "distinction_note": "Insect 虫 inside right component"}
            ],
            "etymological_cognates": [
                {"character": "弱点", "pinyin": "ruòdiǎn", "gloss_en": "weakness; vulnerable spot"},
                {"character": "微弱", "pinyin": "wēiruò", "gloss_en": "faint; feeble (signal/light)"},
                {"character": "减弱", "pinyin": "jiǎnruò", "gloss_en": "weaken; abate"},
                {"character": "脆弱", "pinyin": "cuìruò", "gloss_en": "fragile; brittle"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "弱 signifies deficient strength, low resistance, or military disadvantage.",
            "contrasts": [
                {"id": 1, "compared_word": "弱 vs. 强", "pinyin": "qiáng", "analysis": "强 is the direct antonym meaning strong, powerful, and robust."},
                {"id": 2, "compared_word": "弱 vs. 软", "pinyin": "ruǎn", "analysis": "软 refers to physical softness in texture (cushion/cotton), while 弱 emphasizes lack of strength or capability."},
                {"id": 3, "compared_word": "弱 vs. 小", "pinyin": "xiǎo", "analysis": "小 denotes compact spatial size, while 弱 indicates deficient power or stamina."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在战国军事角逐中，“示敌以弱”是克敌制胜的重要谋略。长平前线秦军主帅白起故意命令前锋部队假装兵力薄弱、败下阵去，让赵括误以为秦军不堪一击，从而轻率放弃坚固防线出击，落入了秦军的致命圈套。",
                "pinyin": "Zài Zhànguó jūnshì juézhú zhōng, 'shì dí yǐ ruò' shì kèdí-zhìshèng de zhòngyào móulüè. Chángpíng qiánxiàn Qínjūn zhǔshuài Bái Qǐ gùyì mìnglìng qiánfēng bùduì jiǎzhuāng bīnglì bóruò, bài xià zhèn qù, ràng Zhào Kuò wùyǐwéi Qínjūn bùkān-yījī, cóng'ér qīngshuài fàngqì jiāngù fángxiàn chūjī, luòrù le Qínjūn de zhìmìng quāntào.",
                "en": "In Warring States warfare, 'feigning weakness' was a crucial stratagem. At Changping, Qin General Bai Qi ordered vanguards to fake defeat and weakness, deceiving Zhao Kuo into abandoning fortified positions to fall into an ambush.",
                "es": "En la guerra de los Reinos Combatientes, aparentar flaqueza era una astuta estratagema. En Changping, Bai Qi ordenó a la vanguardia fingir debilidad; Zhao Kuo creyó desmoronado al enemigo y abandonó sus baluartes cayendo en la trampa."
            },
            {
                "id": "#2",
                "hanzi": "唯物辩证法告诉我们，强与弱并不是绝对固定不变的，在一定条件下双方可以相互转化。处于弱势的一方只要善于扬长避短，集中优势力量攻其不备，同样能够打破平衡、以弱胜强，在逆境中开辟出崭新的胜利天地。",
                "pinyin": "Wéiwù-biànzhèngfǎ gàosu wǒmen, qiáng yǔ ruò bìng bùshì juéduì gùdìng-bùbiàn de, zài yīdìng tiáojiàn xià shuāngfāng kěyǐ xiānghù zhuǎnhuà. Chǔyú ruòshì de yīfāng zhǐyào shànyú yángcháng-bìduǎn, jízhōng yōushì lìliang gōng qí bù bèi, tóngyàng nénggòu dǎpò pínghéng, yǐ ruò shèng qiáng, zài nìjìng zhōng kāipì chū zhǎnxīn de shènglì tiāndì.",
                "en": "Dialectics teaches that strength and weakness are not immutable; under given conditions, they transform into each other. Disadvantaged forces concentrating strength on vulnerabilities can overturn balances and conquer stronger rivals.",
                "es": "La dialéctica enseña que la fuerza y la debilidad no son estáticas; bajo ciertas condiciones mutan recíprocamente. Quien parte de desventaja pero concentra fuerzas en las fallas ajenas puede vencer al fuerte y triunfar."
            }
        ]
    },

    # 12 形势
    {
        "id": "12",
        "hanzi": "形势",
        "pinyin": "xíng shì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "situation; circumstance; terrain; state of affairs",
            "es": "situación; coyuntura; panorama; relieve orográfico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the evolving state of affairs, overall situation, strategic landscape, or military terrain",
                "definition_es": "estado o panorama general de los acontecimientos, coyuntura estratégica o relieve geográfico",
                "example_phrase": "看清当前形势 (discern the current situation clearly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老将廉颇根据长平前线秦强赵弱的严峻形势，果断采取坚壁清野、坚守营垒的稳健策略。",
                "pinyin": "Lǎojiàng Lián Pō gēnjù Chángpíng qiánxiàn Qín qiáng Zhào ruò de yánjùn xíngshì, guǒduàn cǎiqǔ jiānbì-qīngyě, jiānshǒu yínglěi de wěnjiàn cèlüè.",
                "en": "General Lian Po, assessing the grim situation where Qin was strong and Zhao weak at Changping, decisively adopted a strategy of fortification and defense.",
                "es": "El curtido Lian Po, calibrando la delicada situación en Changping donde Qin aventajaba a Zhao, optó con prudencia por fortificar sus líneas."
            },
            {
                "id": "#2",
                "hanzi": "面对瞬息万变的全球经济形势，企业必须具备高度敏锐的战略洞察力，及时调整业务布局。",
                "pinyin": "Miànduì shùnxī-wànbiàn de quánqiú jīngjì xíngshì, qǐyè bìxū jùbèi gāodù mǐnruì de zhànlüè dòngchálì, jíshí tiáozhěng yèwù bùjú.",
                "en": "Confronting the fast-changing global economic situation, enterprises must possess keen strategic foresight to adapt operations promptly.",
                "es": "Ante la volátil coyuntura económica mundial, las corporaciones requieren perspicacia estratégica para reajustar a tiempo sus operaciones."
            }
        ],
        "collocations": [
            {"hanzi": "当前形势", "en": "current situation / present state of affairs"},
            {"hanzi": "形势严峻", "en": "the situation is grave / grim"},
            {"hanzi": "形势大好", "en": "the situation is splendid / favorable"},
            {"hanzi": "分析形势", "en": "analyze the situation / landscape"},
            {"hanzi": "客观形势", "en": "objective situation"},
            {"hanzi": "军事形势", "en": "military situation / tactical landscape"}
        ],
        "idioms": [
            {"hanzi": "审时度势", "pinyin": "shěn shí duó shì", "meaning_en": "judge the hour and size up the situation"},
            {"hanzi": "势如破竹", "pinyin": "shì rú pò zhú", "meaning_en": "sweeping forward with irresistible momentum"},
            {"hanzi": "顺势而为", "pinyin": "shùn shì ér wéi", "meaning_en": "act in accordance with the prevailing trend"},
            {"hanzi": "形势逼人", "pinyin": "xíng shì bī rén", "meaning_en": "the situation is pressing and brook no delay"}
        ],
        "character_decomposition": [
            {
                "character": "形",
                "pinyin": "xíng",
                "meaning_en": "shape; form; appearance; body",
                "meaning_es": "forma; contorno; aspecto; figura",
                "radical": "彡",
                "radical_meaning_en": "hair / ornament",
                "meaning_component": "开/井 (framework / balance) + 彡 (delicate brushwork/ornament)",
                "sound_component": "开 (kāi / xíng)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Outer physical contours carved or drawn with brush strokes 彡; denotes physical form.",
                "visual_mnemonic_story_en": "Traced lines (彡) defining the clean external silhouette and form of an object (形).",
                "visual_mnemonic_story_es": "Pinceladas estilizadas (彡) que delinean el contorno y la forma exterior de una figura (形).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MTTH",
                "traditional": "形"
            },
            {
                "character": "势",
                "pinyin": "shì",
                "meaning_en": "power; momentum; tendency; posture",
                "meaning_es": "fuerza; impulso; tendencia; postura",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "执 (holding authority / grasping seeds) + 力 (physical strength)",
                "sound_component": "埶 (shì)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Exerting dynamic strength 力 from an elevated authoritative position 执; signifies momentum and power.",
                "visual_mnemonic_story_en": "Channeling strength (力) from high ground to unleash irresistible momentum (势).",
                "visual_mnemonic_story_es": "Canalizar la fuerza muscular (力) desde un promontorio para desatar un empuje imparable (势).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GIS",
                "traditional": "勢"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The concrete visible form of reality (形) combined with its dynamic momentum (势) creates the strategic situation (形势).",
            "composite_memory_hook_es": "El contorno visible de las cosas (形) sumado a su impulso dinámico (势) define la situación estratégica (形势).",
            "cultural_and_cognitive_roots": "Sunzi's 'Art of War' dedicated chapters to 'Form' (形, static defense) and 'Momentum' (势, dynamic attack), synthesizing into macro situation.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'xíng shì' (35-51). Lift cleanly on 'xíng', descending firmly on 'shì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "行", "pinyin": "xíng", "meaning_en": "walk; line", "distinction_note": "Step 彳 on left instead of 幵 and 彡"},
                {"character": "刑", "pinyin": "xíng", "meaning_en": "punishment", "distinction_note": "Knife radical 刂 on right instead of 彡"},
                {"character": "热", "pinyin": "rè", "meaning_en": "hot; heat", "distinction_note": "Fire dots 灬 under 执 instead of 力"},
                {"character": "挚", "pinyin": "zhì", "meaning_en": "sincere", "distinction_note": "Hand 手 under 执 instead of 力"}
            ],
            "etymological_cognates": [
                {"character": "态势", "pinyin": "tàishì", "gloss_en": "posture; situational trend"},
                {"character": "局势", "pinyin": "júshì", "gloss_en": "situation; political landscape"},
                {"character": "形象", "pinyin": "xíngxiàng", "gloss_en": "image; figure"},
                {"character": "形成", "pinyin": "xíngchéng", "gloss_en": "form; take shape"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "形势 points to macro-level developments, strategic military layouts, or collective political landscapes.",
            "contrasts": [
                {"id": 1, "compared_word": "形势 vs. 情况", "pinyin": "qíngkuàng", "analysis": "情况 is concrete and covers specific details/status of an individual or incident, while 形势 denotes broader strategic tides."},
                {"id": 2, "compared_word": "形势 vs. 局势", "pinyin": "júshì", "analysis": "局势 highlights critical, volatile political or military chess games, whereas 形势 includes economic, social, or geographic trends."},
                {"id": 3, "compared_word": "形势 vs. 环境", "pinyin": "huánjìng", "analysis": "环境 emphasizes surrounding physical or cultural conditions, while 形势 describes dynamic trends over time."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平对峙初期，老将廉颇准确研判了战场形势。秦军远道而来利在速战，而赵军粮道畅通利在持久防守。廉颇依据形势修筑坚固壁垒坚守不战，秦军久攻不下疲惫不堪，双方形势本已朝着有利于赵国的方向发展。",
                "pinyin": "Chángpíng duìzhì chūqī, lǎojiàng Lián Pō zhǔnquè yánpàn le zhànchǎng xíngshì. Qínjūn yuǎndào-érlái lì zài sùzhàn, ér Zhàojūn liángdào chàngtōng lì zài chíjiǔ fángshǒu. Lián Pō yījù xíngshì xiūzhù jiāngù bìlěi jiānshǒu-bùzhàn, Qínjūn jiǔgōng-bùxià píbèi-bùkān, shuāngfāng xíngshì běn yǐ cháozhe yǒulìyú Zhàoguó de fāngxiàng fāzhǎn.",
                "en": "Early at Changping, General Lian Po accurately sized up the situation. Qin needed a swift fight, while Zhao benefited from protracted defense. Lian Po built sturdy bastions; Qin grew weary, and the strategic landscape swung in Zhao's favor.",
                "es": "Al inicio de Changping, el general Lian Po calibró con lucidez el panorama bélico. A Qin le convenía una victoria relámpago, mientras que a Zhao le favorecía la guerra de desgaste. Los baluartes de Lian Po inclinaban la coyuntura a favor de Zhao."
            },
            {
                "id": "#2",
                "hanzi": "在复杂多变的市场竞争中，卓越的领导者必须善于审时度势。不仅要深入分析行业当下的客观形势，更要前瞻性预判未来的科技与消费趋势。根据形势变化及时优化战略布局，企业方能在激流险滩中稳操胜券。",
                "pinyin": "Zài fùzá-duōbiàn de shìchǎng jìngzhēng zhōng, zhuóyuè de lǐngdǎozhě bìxū shànyú shěnshí-duóshì. Bùjǐn yào shēnrù fēnxī hángyè dāngxià de kèguān xíngshì, gèng yào qiánzhānxìng yùpàn wèilái de kējì yǔ xiāofèi qūshì. Gēnjù xíngshì biànhuà jíshí yōuhuà zhànlüè bùjú, qǐyè fāng néng zài jīliú-xiǎntān zhōng wěncāo-shèngquàn.",
                "en": "Amid complex market competition, outstanding leaders must size up situations astutely. Beyond analyzing current sector dynamics, they anticipate tech and consumer trends, optimizing strategies to steer firms safely to victory.",
                "es": "En la competencia mercantil, los líderes preclaros deben juzgar la coyuntura con agudeza. No basta examinar el panorama presente; es preciso prever tendencias y adaptar la estrategia para navegar con éxito en aguas turbulentas."
            }
        ]
    },

    # 13 命令
    {
        "id": "13",
        "hanzi": "命令",
        "pinyin": "mìng lìng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "command; order; decree; to command; to order",
            "es": "orden; mandato; comando; ordenar; decretar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "an authoritative directive, instruction, or decree issued by a superior that must be executed",
                "definition_es": "directriz, disposición imperativa o mandato expedido por una autoridad para su obligado cumplimiento",
                "example_phrase": "服从命令 (obey commands)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括一到长平前线接替廉颇，就立即鲁莽地下达了全军出击、主动进攻秦军的作战命令。",
                "pinyin": "Zhào Kuò yī dào Chángpíng qiánxiàn jiētì Lián Pō, jiù lìjí lǔmǎng de xiàdá le quán jūn chūjī, zhǔdòng jìngōng Qínjūn de zuòzhàn mìnglìng.",
                "en": "As soon as Zhao Kuo reached the Changping front replacing Lian Po, he rashly issued a combat order commanding the entire army to attack Qin.",
                "es": "Nada más llegar a Changping para relevar a Lian Po, Zhao Kuo impartió la temeraria orden de lanzar a todo el ejército al ataque contra Qin."
            },
            {
                "id": "#2",
                "hanzi": "消防救援指挥中心接到火警报警后，迅速下达出警命令，三辆消防车在五分钟内火速赶赴现场。",
                "pinyin": "Xiāofáng jiùyuán zhǐhuī zhōngxīn jiē dào huǒjǐng bàojǐng hòu, xùnsù xiàdá chūjǐng mìnglìng, sān liàng xiāofángchē zài wǔ fēnzhōng nèi huǒsù gǎnfù xiànchǎng.",
                "en": "Upon receiving the fire alarm, the rescue command center rapidly issued dispatch orders, and three fire engines dashed to the scene within five minutes.",
                "es": "Al recibir la alarma de incendio, el centro de coordinación emitió la orden de salida y tres camiones de bomberos acudieron al lugar en cinco minutos."
            }
        ],
        "collocations": [
            {"hanzi": "下达命令", "en": "issue an order / command"},
            {"hanzi": "服从命令", "en": "obey orders"},
            {"hanzi": "执行命令", "en": "execute orders"},
            {"hanzi": "紧急命令", "en": "urgent order"},
            {"hanzi": "军人以服从命令为天职", "en": "soldiers regard obedience to orders as sacred duty"},
            {"hanzi": "撤销命令", "en": "revoke an order"}
        ],
        "idioms": [
            {"hanzi": "令行禁止", "pinyin": "lìng xíng jìn zhǐ", "meaning_en": "orders executed promptly and prohibitions strictly observed"},
            {"hanzi": "军令如山", "pinyin": "jūn lìng rú shān", "meaning_en": "military orders are firm as mountains; non-negotiable"},
            {"hanzi": "唯命是从", "pinyin": "wéi mìng shì cóng", "meaning_en": "obey every command submissively"},
            {"hanzi": "发号施令", "pinyin": "fā hào shī lìng", "meaning_en": "bark out orders and order people around"}
        ],
        "character_decomposition": [
            {
                "character": "命",
                "pinyin": "mìng",
                "meaning_en": "life; fate; command; decree",
                "meaning_es": "vida; destino; mandato; ordenar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (authoritative spoken decree) + 令 (command proclamation)",
                "sound_component": "令 (lìng)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A mouth 口 delivering an imperative decree 令; signifies an order or destined mandate.",
                "visual_mnemonic_story_en": "A sovereign's mouth (口) pronouncing a binding decree that defines people's mission (命).",
                "visual_mnemonic_story_es": "La boca (口) de un soberano proclamando un decreto sagrado que sella un destino (命).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "ROMB",
                "traditional": "命"
            },
            {
                "character": "令",
                "pinyin": "lìng",
                "meaning_en": "order; command; season; cause",
                "meaning_es": "orden; mandato; estación; mandar",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "亼 (leader gathering people) + 卩 (kneeling figure obeying)",
                "sound_component": "令 (lìng)",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Gathered subjects 亼 kneeling 卩 to receive a formal mandate.",
                "visual_mnemonic_story_en": "Gathering people under a roof shelter (人) to deliver an official decree (令).",
                "visual_mnemonic_story_es": "Congregar vasallos bajo el alero real (人) para proclamar una ordenanza (令).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OII",
                "traditional": "令"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An imperative spoken mandate (命) delivered as a formal decree (令) constitutes an authoritative order (命令).",
            "composite_memory_hook_es": "El mandato soberano (命) promulgado como ordenanza regia (令) conforma una orden de obligado acatamiento (命令).",
            "cultural_and_cognitive_roots": "Military discipline principle ('军令如山') where failure to execute a superior's lawful command carried summary court-martial.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'mìng lìng' (51-51). Articulate both syllables with firm, authoritative downward snap."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "伞", "pinyin": "sǎn", "meaning_en": "umbrella", "distinction_note": "Contains multiple crossbars under 人"},
                {"character": "今", "pinyin": "jīn", "meaning_en": "now; present", "distinction_note": "Lacks the bottom dot/hook of 令"},
                {"character": "冷", "pinyin": "lěng", "meaning_en": "cold", "distinction_note": "Ice radical 冫 on left of 令"},
                {"character": "伶", "pinyin": "líng", "meaning_en": "clever; actor", "distinction_note": "Person radical 亻 on left of 令"}
            ],
            "etymological_cognates": [
                {"character": "命运", "pinyin": "mìngyùn", "gloss_en": "destiny; fate"},
                {"character": "指令", "pinyin": "zhǐlìng", "gloss_en": "instruction; computer command"},
                {"character": "寿命", "pinyin": "shòumìng", "gloss_en": "lifespan; longevity"},
                {"character": "司令", "pinyin": "sīlìng", "gloss_en": "commander; commanding officer"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "命令 indicates an authoritative, non-negotiable instruction that subordinates must execute without question.",
            "contrasts": [
                {"id": 1, "compared_word": "命令 vs. 请求", "pinyin": "qǐngqiú", "analysis": "请求 is a polite request asking for assistance, while 命令 is an unbendable directive from above."},
                {"id": 2, "compared_word": "命令 vs. 建议", "pinyin": "jiànyì", "analysis": "建议 offers advice for voluntary consideration, whereas 命令 carries binding administrative compulsion."},
                {"id": 3, "compared_word": "命令 vs. 指示", "pinyin": "zhǐshì", "analysis": "指示 gives guiding parameters or policy orientation, while 命令 demands exact tactical execution."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "赵括接掌赵军兵权后，第一道命令便是废除老将廉颇原先制定的坚守防御策略。他不顾副将们的苦苦劝谏，强行下达全线反攻的严厉命令。正是这一道脱离战场实际的昏庸命令，将数十万赵国将士推向了万劫不复的深渊。",
                "pinyin": "Zhào Kuò jiēzhǎng Zhàojūn bīngquán hòu, dì-yī dào mìnglìng biàn shì fèichú lǎojiàng Lián Pō yuánxiān zhìdìng de jiānshǒu fángyù cèlüè. Tā bùgù fùjiàng men de kǔkǔ quànjiàn, qiángxíng xiàdá quánxiàn fǎngōng de yánlì mìnglìng. Zhèngshì zhè yī dào tuōlí zhànchǎng shíjì de hūnyōng mìnglìng, jiāng shùshí wàn Zhàoguó jiàngshì tuī xiàng le wànjié-bùfù de shēnyuān.",
                "en": "Taking military command, Zhao Kuo's very first order repealed Lian Po's defensive policy. Disregarding deputies' entreaties, he forced an order for full-scale offensive. This reckless command pushed hundreds of thousands of troops into the abyss.",
                "es": "Al asumir el mando, la primera orden de Zhao Kuo fue abolir la prudente defensa de Lian Po. Desoyendo los ruegos de sus lugartenientes, impartió una estricta orden de contraataque general, precipitando al abismo a sus soldados."
            },
            {
                "id": "#2",
                "hanzi": "在现代突发公共安全事件的应急救援处置中，科学高效的统一命令体系是争分夺秒挽救生命的制度保障。指挥部下达的每一道疏散转移命令，都必须依托精确的实时数据与现场研判，做到指令清晰、雷厉风行，确保救援有序推进。",
                "pinyin": "Zài xiàndài tūfā gōnggòng ānquán shìjiàn de yìngjí jiùyuán chǔzhì zhōng, kēxué gāoxiào de tǒngyī mìnglìng tǐxì shì zhēngfēn-duómiǎo wǎnjiù shēngmìng de zhìdù bǎozhàng. Zhǐhuībù xiàdá de měi yī dào shūsàn zhuǎnyí mìnglìng, dōu bìxū yītuō jīngquè de shíshí shùjù yǔ xiànchǎng yánpàn, zuòdào zhǐlìng qīngxī, léilì-fēngxíng, quèbǎo jiùyuán yǒuxù tuījìn.",
                "en": "In modern public emergency responses, a unified command system safeguards swift lifesaving operations. Every evacuation order issued by headquarters relies on real-time data, ensuring clear instructions executed with decisive speed.",
                "es": "En la gestión de emergencias civiles, una cadena unificada de mando resulta vital para salvar vidas a contrarreloj. Cada orden de evacuación debe fundamentarse en datos en tiempo real, garantizando directrices claras y un auxilio coordinado."
            }
        ]
    },

    # 14 守
    {
        "id": "14",
        "hanzi": "守",
        "pinyin": "shǒu",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to guard; defend; keep watch; observe; abide by",
            "es": "defender; vigilar; guardar; custodiar; acatar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to defend against attack; guard a position; keep watch; abide by rules or promises",
                "definition_es": "defender una posición del asalto enemigo; vigilar; custodiar; acatar normas o promesas",
                "example_phrase": "坚守阵地 (firmly hold and defend a position)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老将廉颇深谙秦军远来求战的心态，严令赵国将士坚守堡垒阵地，绝不轻易出击。",
                "pinyin": "Lǎojiàng Lián Pō shēn'ān Qínjūn yuǎn lái qiú zhàn de xīntài, yánlìng Zhàoguó jiàngshì jiānshǒu bǎolěi zhèndì, juébù qīngyì chūjī.",
                "en": "General Lian Po understood Qin's urgency to force a quick decision, strictly ordering Zhao soldiers to defend bastions and refrain from sorties.",
                "es": "El general Lian Po conocía la prisa de Qin por librar combate y ordenó a sus tropas defender los bastiones sin salir a campo abierto."
            },
            {
                "id": "#2",
                "hanzi": "在现代社会契约精神中，恪守信誉、严守规则是每一个公民和企业应当践行的基本准则。",
                "pinyin": "Zài xiàndài shèhuì qìyuē jīngshén zhōng, kèshǒu xìnyù, yánshǒu guīzé shì měi yī gè gōngmín hé qǐyè yīngdāng jiànxíng de jīběn zhǔnzé.",
                "en": "In modern civic contract culture, abiding by credit and observing rules are fundamental principles that every citizen and enterprise must practice.",
                "es": "En el espíritu cívico contemporáneo, custodiar la palabra empeñada y acatar las normas son deberes inexcusables de ciudadanos y empresas."
            }
        ],
        "collocations": [
            {"hanzi": "坚守岗位", "en": "stick firmly to one's post"},
            {"hanzi": "守信用", "en": "keep one's word / promise"},
            {"hanzi": "守候在旁", "en": "stand watch / wait attentively beside"},
            {"hanzi": "防守坚固", "en": "stoutly defended"},
            {"hanzi": "守规矩", "en": "abide by rules and etiquette"},
            {"hanzi": "看守大门", "en": "guard the main entrance"}
        ],
        "idioms": [
            {"hanzi": "坚守不移", "pinyin": "jiān shǒu bù yí", "meaning_en": "adhere unswervingly and hold fast"},
            {"hanzi": "墨守成规", "pinyin": "mò shǒu chéng guī", "meaning_en": "stick to conventions dogmatically; hidebound"},
            {"hanzi": "守株待兔", "pinyin": "shǒu zhū dài tù", "meaning_en": "stand by a tree waiting for a hare; wait passively for windfalls"},
            {"hanzi": "守望相助", "pinyin": "shǒu wàng xiāng zhù", "meaning_en": "keep watch and help each other in neighborhood solidarity"}
        ],
        "character_decomposition": [
            {
                "character": "守",
                "pinyin": "shǒu",
                "meaning_en": "guard; defend; keep; watch over",
                "meaning_es": "defender; vigilar; guardar; custodiar",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (household roof) + 寸 (ruling hand / law measurement)",
                "sound_component": "守 (shǒu)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A hand 寸 holding protective authority inside a house 宀; signifies guarding one's home and borders.",
                "visual_mnemonic_story_en": "Guarding a domestic homestead (宀) with a vigilant, dutiful hand (寸) against intruders (守).",
                "visual_mnemonic_story_es": "Custodiar el hogar techado (宀) con mano atenta y vigilante (寸) para defenderlo (守).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "JDI",
                "traditional": "守"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Stationing a firm hand (寸) under the home roof (宀) means to guard and defend (守).",
            "composite_memory_hook_es": "Apostar una mano firme (寸) bajo el tejado del hogar (宀) define la acción de custodiar (守).",
            "cultural_and_cognitive_roots": "Derived from classical territorial defence where magistrates were appointed to guard cities ('太守') and abide by rites.",
            "tone_sandhi_and_pitch_modulation": "Third tone: 'shǒu' (214). Dip deeply into the lower register and rebound with clarity."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "寸", "pinyin": "cùn", "meaning_en": "inch; measurement", "distinction_note": "Lacks the roof radical 宀"},
                {"character": "安", "pinyin": "ān", "meaning_en": "safe; peaceful", "distinction_note": "Woman radical 女 under 宀 instead of 寸"},
                {"character": "定", "pinyin": "dìng", "meaning_en": "fix; settle", "distinction_note": "Foot 正 under 宀 instead of 寸"},
                {"character": "宇", "pinyin": "yǔ", "meaning_en": "space; universe", "distinction_note": "Yu 于 under 宀 instead of 寸"}
            ],
            "etymological_cognates": [
                {"character": "防守", "pinyin": "fángshǒu", "gloss_en": "defend; guard"},
                {"character": "遵守", "pinyin": "zūnshǒu", "gloss_en": "comply with; observe"},
                {"character": "保守", "pinyin": "bǎoshǒu", "gloss_en": "conservative; keep secret"},
                {"character": "守护", "pinyin": "shǒuhù", "gloss_en": "guard and protect"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "守 emphasizes holding ground defensively, guarding securely, or adhering to rules and vows.",
            "contrasts": [
                {"id": 1, "compared_word": "守 vs. 攻", "pinyin": "gōng", "analysis": "攻 is the direct antonym meaning to attack or launch an offensive."},
                {"id": 2, "compared_word": "守 vs. 逃", "pinyin": "táo", "analysis": "逃 means fleeing or abandoning ground, opposite to firmly holding 守."},
                {"id": 3, "compared_word": "守 vs. 护", "pinyin": "hù", "analysis": "护 stresses providing protective shielding to weaker parties, while 守 focuses on vigilantly defending borders or positions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在冷兵器战争中，“攻”与“守”是两种截然相反的战略形态。廉颇在长平前线依托地形筑垒坚守，令秦军数十万精锐进退两难。若赵王能坚持“以守待变”的策略，待秦军粮尽自退，战国历史的格局或许将被彻底改写。",
                "pinyin": "Zài lěngbīngqì zhànzhēng zhōng, 'gōng' yǔ 'shǒu' shì liǎng zhǒng jiérán-xiāngfǎn de zhànlüè xíngtài. Lián Pō zài Chángpíng qiánxiàn yītuō dìxíng zhùlěi jiānshǒu, lìng Qínjūn shùshí wàn jīngruì jìntuì-liǎngnán. Ruò Zhàowáng néng jiānchí 'yǐ shǒu dài biàn' de cèlüè, dài Qínjūn liáng jìn zì tuì, Zhànguó lìshǐ de géjú huòxǔ jiāng bèi chèdǐ gǎixiě.",
                "en": "In ancient warfare, attack and defense represented polar strategies. Lian Po's defense behind fortifications put Qin troops in a dilemma. Had King Zhao maintained this strategy until Qin's food ran out, history might have changed completely.",
                "es": "En la guerra clásica, ataque y defensa eran polos opuestos. La defensa numantina de Lian Po desconcertó a las tropas de Qin. Si el rey de Zhao hubiera mantenido la defensa hasta agotar el grano enemigo, la historia habría cambiado."
            },
            {
                "id": "#2",
                "hanzi": "“守”不仅是一种军事防御战术，更是一种坚守初心的道德操守。无论是在学术研究中耐得住冷板凳、严守学术底线，还是在日常生活中恪守契约与诚信，“守得云开见月明”的定力与坚韧，是成就卓越人生的基石。",
                "pinyin": "'Shǒu' bùjǐn shì yī zhǒng jūnshì fángyù zhànshù, gèng shì yī zhǒng jiānshǒu chūxīn de dàodé cāoshǒu. Wúlùn shì zài xuéshù yánjiū zhōng nàidézhù lěngbǎndèng, yánshǒu xuéshù dǐxiàn, háishì zài rìcháng shēnghuó zhōng kèshǒu qìyuē yǔ chéngxìn, 'shǒu dé yún kāi jiàn yuè míng' de dìnglì yǔ jiānrèn, shì chéngjiù zhuóyuè rénshēng de jīshí.",
                "en": "'Guarding' is not merely tactical defense, but moral integrity. Whether enduring quiet toil to uphold academic ethics or keeping agreements in life, steadfast tenacity until clouds clear paves the path to an accomplished life.",
                "es": "Defender una posición no es solo maniobra bélica, sino firmeza moral. Ya sea guardando el rigor ético en la ciencia o acatando acuerdos en la vida diaria, perseverar hasta que aclare el cielo es la base de una vida noble."
            }
        ]
    },

    # 15 阵地
    {
        "id": "15",
        "hanzi": "阵地",
        "pinyin": "zhèn dì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "battlefield position; front; stronghold; territory",
            "es": "posición en el frente; trinchera; baluarte; posición de combate"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a designated terrain or fortified area occupied by military troops for defense or attack; figurative sphere of activity",
                "definition_es": "terreno fortificado o sector ocupado por tropas militares para el combate; reducto o baluarte figurado",
                "example_phrase": "坚守阵地 (firmly hold one's battlefield position)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括接替廉颇后轻率放弃了坚固险要的防御阵地，冒然出击，结果使数十万大军落入秦军包围圈。",
                "pinyin": "Zhào Kuò jiētì Lián Pō hòu qīngshuài fàngqì le jiāngù xiǎnyào de fángyù zhèndì, màorán chūjī, jiéguǒ shǐ shùshí wàn dàjūn luòrù Qínjūn bāowéiquān.",
                "en": "Replacing Lian Po, Zhao Kuo rashly abandoned fortified strategic positions to attack recklessly, causing his army to fall into Qin's encirclement.",
                "es": "Al relevar a Lian Po, Zhao Kuo abandonó con temeridad las sólidas posiciones defensivas, haciendo que su ejército cayera en la trampa enemiga."
            },
            {
                "id": "#2",
                "hanzi": "互联网新媒体已经成为当代思想文化传播与公众舆论引导的重要阵地。",
                "pinyin": "Hùliánwǎng xīn méitǐ yǐjīng chéngwéi dāngdài sīxiǎng wénhuà chuánbō yǔ gōngzhòng yúlùn yǐndǎo de zhòngyào zhèndì.",
                "en": "New digital internet media have become vital battlegrounds for modern cultural communication and public opinion guidance.",
                "es": "Los nuevos medios digitales se han convertido en un baluarte crucial para la difusión cultural y la orientación de la opinión pública."
            }
        ],
        "collocations": [
            {"hanzi": "坚守阵地", "en": "firmly hold the position"},
            {"hanzi": "占领阵地", "en": "occupy / seize the position"},
            {"hanzi": "防御阵地", "en": "defensive position"},
            {"hanzi": "前沿阵地", "en": "frontline position / forward post"},
            {"hanzi": "阵地战", "en": "position warfare / trench combat"},
            {"hanzi": "思想阵地", "en": "ideological frontline / cultural sphere"}
        ],
        "idioms": [
            {"hanzi": "严阵以待", "pinyin": "yán zhèn yǐ dài", "meaning_en": "stand in battle array waiting for the enemy in combat readiness"},
            {"hanzi": "固若金汤", "pinyin": "gù ruò jīn tāng", "meaning_en": "strongly fortified like metal ramparts and boiling moats"},
            {"hanzi": "步步为营", "pinyin": "bù bù wéi yíng", "meaning_en": "make a stand at every step; advance cautiously"},
            {"hanzi": "临阵脱逃", "pinyin": "lín zhèn tuō táo", "meaning_en": "flee from the battlefield on the eve of battle"}
        ],
        "character_decomposition": [
            {
                "character": "阵",
                "pinyin": "zhèn",
                "meaning_en": "battle array; battle formation; position; gust",
                "meaning_es": "formación de batalla; posición; racha; despliegue",
                "radical": "阝",
                "radical_meaning_en": "mound / hill",
                "meaning_component": "阝 (earthen embankment) + 车 (war chariots deployed along it)",
                "sound_component": "阵 (zhèn)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "War chariots 车 deployed along an earthen defensive mound 阝 in tactical battle formation.",
                "visual_mnemonic_story_en": "Armored chariots (车) positioned in ranks along a defensive earthen ridge (阝) for battle (阵).",
                "visual_mnemonic_story_es": "Carros de combate (车) apostados a lo largo del terraplén (阝) en rigurosa formación defensiva (阵).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NLKQ",
                "traditional": "陣"
            },
            {
                "character": "地",
                "pinyin": "dì",
                "meaning_en": "earth; ground; land; soil; place",
                "meaning_es": "tierra; suelo; terreno; lugar",
                "radical": "土",
                "radical_meaning_en": "earth / soil",
                "meaning_component": "土 (soil / earth mound) + 也 (alluvial basin / serpent)",
                "sound_component": "也 (yě / dì)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Fertile soil 土 stretching across the terrestrial basin 也; represents land or territory.",
                "visual_mnemonic_story_en": "Mounds of fertile soil (土) forming vast terrestrial terrain (地).",
                "visual_mnemonic_story_es": "Montículos de tierra fértil (土) que conforman el suelo y el territorio (地).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "GPD",
                "traditional": "地"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Chariots drawn up in battle ranks (阵) anchored to fortified terrain (地) establish a military position (阵地).",
            "composite_memory_hook_es": "Carros desplegados en formación táctica (阵) anclados sobre el terreno defensivo (地) forjan la posición de combate (阵地).",
            "cultural_and_cognitive_roots": "Originates in classical chariot warfare where holding the prepared tactical position (阵) determined survival against cavalry charges.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'zhèn dì' (51-51). Articulate both syllables with martial, decisive force."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "陈", "pinyin": "chén", "meaning_en": "old; display", "distinction_note": "East 东 on right of 阝 instead of 车"},
                {"character": "连", "pinyin": "lián", "meaning_en": "connect", "distinction_note": "Movement 辶 on left of 车 instead of 阝"},
                {"character": "池", "pinyin": "chí", "meaning_en": "pool; pond", "distinction_note": "Water 氵 on left of 也 instead of 土"},
                {"character": "他", "pinyin": "tā", "meaning_en": "he; him", "distinction_note": "Person 亻 on left of 也 instead of 土"}
            ],
            "etymological_cognates": [
                {"character": "阵线", "pinyin": "zhènxiàn", "gloss_en": "battlefront; battle line"},
                {"character": "阵容", "pinyin": "zhènróng", "gloss_en": "lineup; battle array"},
                {"character": "阵雨", "pinyin": "zhènyǔ", "gloss_en": "shower; squall"},
                {"character": "地点", "pinyin": "dìdiǎn", "gloss_en": "location; place"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "阵地 strictly refers to a fortified battlefield stronghold or tactical line held by an army, or metaphorical sphere.",
            "contrasts": [
                {"id": 1, "compared_word": "阵地 vs. 战场", "pinyin": "zhànchǎng", "analysis": "战场 is the broad operational war theater, while 阵地 is a specific fortified tactical hill or line."},
                {"id": 2, "compared_word": "阵地 vs. 营地", "pinyin": "yíngdì", "analysis": "营地 refers to an encampment for soldiers' bivouac/sleep, whereas 阵地 is deployed for combat."},
                {"id": 3, "compared_word": "阵地 vs. 领土", "pinyin": "lǐngtǔ", "analysis": "领土 is sovereign legal national territory, unlike a localized military 阵地."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平之战中，廉颇苦心经营了三年之久的丹河防御阵地，是阻挡秦国大军东进的坚固铁壁。阵地依托险峻关隘修筑堡垒，储粮充足。赵括上任后自作主张全线弃守阵地，最终导致数十万主力在野战中被秦军围歼。",
                "pinyin": "Chángpíng zhī zhàn zhōng, Lián Pō kǔxīn jīngyíng le sān nián zhī jiǔ de Dānhé fángyù zhèndì, shì zǔdǎng Qínguó dàjūn dōng jìn de jiāngù tiěbì. Zhèndì yītuō xiǎnjùn guān'ài xiūzhù bǎolěi, chǔliáng chōngzú. Zhào Kuò shàngrèn hòu zìzuò-zhǔzhāng quánxiàn qìshǒu zhèndì, zuìzhōng dǎozhì shùshí wàn zhǔlì zài yězhàn zhōng bèi Qínjūn wéijiān.",
                "en": "At Changping, Lian Po's Danhe fortified position held for three years as an iron wall blocking Qin. The position anchored on mountain passes with abundant food. Zhao Kuo rashly abandoned it, leading his troops to slaughter in open combat.",
                "es": "En Changping, la posición fortificada del río Dan sostenida por Lian Po durante tres años frenó el avance de Qin. Bien abastecida en los pasos de montaña, Zhao Kuo la abandonó con temeridad, llevando a sus tropas al cerco en campo abierto."
            },
            {
                "id": "#2",
                "hanzi": "在当今全球文化多元激荡的时代，优秀传统文化是守护民族精神根基的重要阵地。面对纷繁复杂的外部思潮，我们必须守好自己的思想文化阵地，传承中华优秀传统美德，坚定文化自信，为民族复兴提供深厚滋养。",
                "pinyin": "Zài dāngjīn quánqiú wénhuà duōyuán jīdàng de shídài, yōuxiù chuántǒng wénhuà shì shǒuhù mínzú jīngshén gēnjī de zhòngyào zhèndì. Miànduì fēnfán-fùzá de wàibù sīcháo, wǒmen bìxū shǒu hǎo zìjǐ de sīxiǎng wénhuà zhèndì, chuánchéng Zhōnghuá yōuxiù chuántǒng měidé, jiāndìng wénhuà zìxìn, wèi mínzú fùxīng tígōng shēnhòu zīyǎng.",
                "en": "Amid global cultural exchanges, traditional heritage serves as a vital stronghold safeguarding national spirit. Confronting diverse currents, we must defend our cultural ground, passing down classic virtues with steadfast confidence.",
                "es": "En la era de la globalización cultural, la tradición clásica es un baluarte que resguarda el alma patria. Ante influencias foráneas, debemos custodiar nuestras posiciones culturales, preservando virtudes ancestrales con orgullo."
            }
        ]
    },

    # 16 绝对
    {
        "id": "16",
        "hanzi": "绝对",
        "pinyin": "jué duì",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "absolute; definitely; unconditionally; completely",
            "es": "absoluto; categórico; definitivamente; incondicional"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "unconditional, unrestricted, and without exception; completely and definitely",
                "definition_es": "incondicional, sin excepción ni limitación; de modo categórico y definitivo",
                "example_phrase": "绝对服从 (obey absolutely and unconditionally)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在纪律森严的军队中，部下必须绝对服从上级指挥官下达的作战命令，不得擅自违抗。",
                "pinyin": "Zài jìlǜ sēnyán de jūnduì zhōng, bùxià bìxū juéduì fúcóng shàngjí zhǐhuīguān xiàdá de zuòzhàn mìnglìng, bùdé shànzì wéikàng.",
                "en": "In a strictly disciplined army, subordinates must absolutely obey combat orders issued by commanding officers without defiance.",
                "es": "En un ejército de férrea disciplina, los subordinados deben acatar de forma absoluta las órdenes tácticas impartidas sin vacilar."
            },
            {
                "id": "#2",
                "hanzi": "这套精密航空发动机控制系统的安全性能经过了反复检验，具备极高的绝对可靠性。",
                "pinyin": "Zhè tào jīngmì hángkōng fādòngjī kòngzhì xìtǒng de ānquán xìngnéng jīngguò le fǎnfù jiǎnyàn, jùbèi jí gāo de juéduì kěkàoxìng.",
                "en": "The safety performance of this precision aero-engine control system was verified repeatedly, possessing exceptionally high absolute reliability.",
                "es": "El rendimiento de este sistema de control para turbinas aeronáuticas ha sido probado reiteradamente, gozando de una fiabilidad absoluta."
            }
        ],
        "collocations": [
            {"hanzi": "绝对保证", "en": "absolute guarantee"},
            {"hanzi": "绝对安全", "en": "absolutely safe / secure"},
            {"hanzi": "绝对服从", "en": "absolute obedience"},
            {"hanzi": "绝对优势", "en": "absolute advantage"},
            {"hanzi": "绝对真理", "en": "absolute truth"},
            {"hanzi": "绝不可能", "en": "absolutely impossible"}
        ],
        "idioms": [
            {"hanzi": "斩钉截铁", "pinyin": "zhǎn dīng jié tiě", "meaning_en": "resolute and decisive; cutting nails and severing iron"},
            {"hanzi": "万无一失", "pinyin": "wàn wú yī shī", "meaning_en": "absolutely sure without a single mistake"},
            {"hanzi": "毋庸置疑", "pinyin": "wú yōng zhì yí", "meaning_en": "beyond doubt; unquestionable"},
            {"hanzi": "一诺千金", "pinyin": "yī nuò qiān jīn", "meaning_en": "a promise worth a thousand pieces of gold; solemn vow"}
        ],
        "character_decomposition": [
            {
                "character": "绝",
                "pinyin": "jué",
                "meaning_en": "cut off; sever; absolute; unique; supreme",
                "meaning_es": "cortar; romper; absoluto; único; extremo",
                "radical": "纟",
                "radical_meaning_en": "silk / thread",
                "meaning_component": "纟 (silken thread) + 色/刀 (cutting blade severing threads completely)",
                "sound_component": "绝 (jué)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A sharp knife cleanly severing silk threads 纟 without remaining connection; denotes absolute finality.",
                "visual_mnemonic_story_en": "Severing silk cords (纟) completely in one decisive cut so nothing remains connected (绝).",
                "visual_mnemonic_story_es": "Cortar cordones de seda (纟) de un tajo limpio de modo tajante y definitivo (绝).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "VMNAU",
                "traditional": "絕"
            },
            {
                "character": "对",
                "pinyin": "duì",
                "meaning_en": "correct; opposite; pair; towards",
                "meaning_es": "correcto; par; frente a; hacia",
                "radical": "寸",
                "radical_meaning_en": "inch / hand",
                "meaning_component": "又 (hand) + 寸 (ruling hand / matching pair)",
                "sound_component": "对 (duì)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Two hands holding ceremonial paired vessels facing each other; marks comparison or counterpart.",
                "visual_mnemonic_story_en": "Hands presenting matching paired ceremonial objects face to face (对).",
                "visual_mnemonic_story_es": "Manos que ofrecen dos vasijas emparejadas cara a cara (对).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EII",
                "traditional": "對"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Severed from all comparisons (绝) and having no parallel counterpart (对) defines the absolute (绝对).",
            "composite_memory_hook_es": "Sin término de comparación (绝) ni pariente que lo iguale (对) se erige lo absoluto (绝对).",
            "cultural_and_cognitive_roots": "Philosophical concept originating in Buddhist and Daoist epistemology denoting unconditioned ultimate reality transcending dualities.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'jué duì' (35-51). Lift cleanly on 'jué', then drop decisively on 'duì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "断", "pinyin": "duàn", "meaning_en": "break; sever", "distinction_note": "Axe 斤 on right instead of 色"},
                {"character": "纪", "pinyin": "jì", "meaning_en": "discipline; age", "distinction_note": "Ji 己 on right of 纟 instead of 色"},
                {"character": "时", "pinyin": "shí", "meaning_en": "time", "distinction_note": "Sun 日 on left of 寸 instead of 又"},
                {"character": "封", "pinyin": "fēng", "meaning_en": "seal", "distinction_note": "Gui 圭 on left of 寸 instead of 又"}
            ],
            "etymological_cognates": [
                {"character": "决绝", "pinyin": "juéjué", "gloss_en": "resolute; breaking ties cleanly"},
                {"character": "绝望", "pinyin": "juéwàng", "gloss_en": "despair; hopeless"},
                {"character": "对比", "pinyin": "duìbǐ", "gloss_en": "compare; contrast"},
                {"character": "对方", "pinyin": "duìfāng", "gloss_en": "the other party; counterpart"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "绝对 marks unconditional certainty without caveats or comparative relativity.",
            "contrasts": [
                {"id": 1, "compared_word": "绝对 vs. 相对", "pinyin": "xiāngduì", "analysis": "相对 is the direct antonym meaning relative, conditional, or comparative."},
                {"id": 2, "compared_word": "绝对 vs. 肯定", "pinyin": "kěndìng", "analysis": "肯定 expresses personal psychological certainty, while 绝对 emphasizes categorical unconditionality."},
                {"id": 3, "compared_word": "绝对 vs. 大概", "pinyin": "dàgài", "analysis": "大概 denotes approximate probability, completely opposite to non-negotiable 绝对."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "兵法强调“兵无常势，水无常形”。战场上从来没有绝对万全的必胜公式，任何战术都必须根据敌情动态灵活变通。赵括却把书本兵法奉为不可更改的绝对真理，僵化教条，最终在变幻莫测的决战中自取灭亡。",
                "pinyin": "Bīngfǎ qiángdiào 'bīng wú chángshì, shuǐ wú chángxíng'. Zhànchǎng shang cónglái méiyǒu juéduì wànquán de bìshèng gōngshì, rènhé zhànshù dōu bìxū gēnjù díqíng dòngtài línghuó biàntōng. Zhào Kuò què bǎ shūběn bīngfǎ fèng wéi bùkě gēnggǎi de juéduì zhēnlǐ, jiānghuà jiàotiáo, zuìzhōng zài biànhuàn-mòcè de juézhàn zhōng zìqǔ-mièwáng.",
                "en": "Strategy stresses that 'military posture has no constant form, like water.' Battlefields harbor no absolute victory formulas. Zhao Kuo treated written texts as immutable absolute truth, destroying himself through dogmatism.",
                "es": "El arte militar afirma que la guerra no tiene pautas fijas, como el fluir del agua. No existen fórmulas absolutas de victoria. Zhao Kuo tomó los libros como dogmas inmutables y halló su propia perdición."
            },
            {
                "id": "#2",
                "hanzi": "在现代科学哲学体系中，人类对客观世界的认知是一个不断深化的过程，并没有绝对静止的终极真理。任何伟大的科学定律都是在一定边界条件下的相对真理，勇于质疑既有理论，正是推动科学不断迈向新高度的核心动力。",
                "pinyin": "Zài xiàndài kēxué zhéxué tǐxì zhōng, rénlèi duì kèguān shìjiè de rènzhī shì yī gè bùduàn shēnhuà de guòchéng, bìng méiyǒu juéduì jìngzhǐ de zhōngjí zhēnlǐ. Rènhé wěidà de kēxué dìnglǜ dōu shì zài yīdìng biānjiè tiáojiàn xià de xiāngduì zhēnlǐ, yǒngyú zhìyí jìyǒu lǐlùn, zhèngshì tuīdòng kēxué bùduàn mài xiàng xīn gāodù de héxīn dònglì.",
                "en": "In modern scientific philosophy, human knowledge deepens continually without absolute terminal truths. Great laws are relative truths under boundary conditions; daring to challenge prevailing frameworks propels science forward.",
                "es": "En la filosofía científica contemporánea, el conocimiento es un proceso en constante profundización sin dogmas absolutos. Las leyes físicas rigen bajo condiciones acotadas; cuestionarlas es el motor del avance científico."
            }
        ]
    },

    # 17 主动
    {
        "id": "17",
        "hanzi": "主动",
        "pinyin": "zhǔ dòng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "proactive; taking the initiative; active; of one's own accord",
            "es": "activo; proactivo; tomar la iniciativa; por propia voluntad"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "acting of one's own volition and taking the initiative rather than being driven by external force",
                "definition_es": "que actúa por propia iniciativa e impulso sin aguardar órdenes o presiones externas",
                "example_phrase": "掌握主动权 (seize the initiative)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "善于指挥的军事统帅总能通过巧妙布阵调动敌人，牢牢掌握战场作战的主动权。",
                "pinyin": "Shànyú zhǐhuī de jūnshì tǒngshuài zǒng néng tōngguò qiǎomiào bùzhèn diàodòng dírén, láoláo zhǎngwò zhànchǎng zuòzhàn de zhǔdòngquán.",
                "en": "Skillful military commanders always manipulate enemy forces through clever arrays, firmly seizing the combat initiative on the battlefield.",
                "es": "Los comandantes diestros logran mover al enemigo mediante hábiles maniobras, reteniendo con firmeza la iniciativa del combate."
            },
            {
                "id": "#2",
                "hanzi": "在大学自主学习过程中，学生应当主动查阅文献并积极向导师请教学术疑惑。",
                "pinyin": "Zài dàxué zìzhǔ xuéxí guòchéng zhōng, xuéshēng yīngdāng zhǔdòng cháyuè wénxiàn bìng jījí xiàng dǎoshī qǐngjiào xuéshù yíhuò.",
                "en": "During independent university study, students should proactively consult literature and actively seek counsel from advisors on academic puzzles.",
                "es": "En el estudio universitario autónomo, los alumnos deben consultar bibliografía por iniciativa propia y plantear dudas a sus tutores."
            }
        ],
        "collocations": [
            {"hanzi": "掌握主动权", "en": "seize / hold the initiative"},
            {"hanzi": "主动配合", "en": "proactively cooperate"},
            {"hanzi": "争取主动", "en": "strive for the initiative"},
            {"hanzi": "主动沟通", "en": "proactively communicate"},
            {"hanzi": "主动出击", "en": "take the initiative to attack"},
            {"hanzi": "变被动为主动", "en": "turn passive into proactive"}
        ],
        "idioms": [
            {"hanzi": "先发制人", "pinyin": "xiān fā zhì rén", "meaning_en": "take the initiative and strike first to gain the upper hand"},
            {"hanzi": "反客为主", "pinyin": "fǎn kè wéi zhǔ", "meaning_en": "turn from guest into host; seize leadership and initiative"},
            {"hanzi": "积极主动", "pinyin": "jī jí zhǔ dòng", "meaning_en": "enthusiastic and proactive"},
            {"hanzi": "抢占先机", "pinyin": "qiǎng zhàn xiān jī", "meaning_en": "seize the preemptive opportunity"}
        ],
        "character_decomposition": [
            {
                "character": "主",
                "pinyin": "zhǔ",
                "meaning_en": "master; host; owner; primary; main",
                "meaning_es": "dueño; amo; anfitrión; principal",
                "radical": "丶",
                "radical_meaning_en": "dot",
                "meaning_component": "flame burning at the top of an oil lamp stand 王",
                "sound_component": "主 (zhǔ)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A flame dot 丶 glowing atop an ancestral lamp stand 王; signifies the central master of the household.",
                "visual_mnemonic_story_en": "A radiant flame (丶) shining atop an oil lamp stand presiding as the master of the hall (主).",
                "visual_mnemonic_story_es": "La llama radiante (丶) que arde sobre la lámpara ceremonial presidiendo como dueña de casa (主).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "YG",
                "traditional": "主"
            },
            {
                "character": "动",
                "pinyin": "dòng",
                "meaning_en": "move; act; motion; stir",
                "meaning_es": "mover; actuar; movimiento; impulso",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "云 (clouds rolling across sky) + 力 (physical strength)",
                "sound_component": "云 (yún)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Using muscular strength 力 to drive physical movement like surging clouds 云; signifies action.",
                "visual_mnemonic_story_en": "Applying strength (力) to initiate dynamic action like billowing clouds (动).",
                "visual_mnemonic_story_es": "Aplicar la fuerza (力) para mover las cosas con la soltura de las nubes (动).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MIS",
                "traditional": "動"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Acting as one's own master (主) to initiate purposeful motion (动) means being proactive (主动).",
            "composite_memory_hook_es": "Obrar como dueño de los propios actos (主) para emprender el movimiento (动) define la proactividad (主动).",
            "cultural_and_cognitive_roots": "A core strategic concept in Sunzi's Art of War: 'He who arrives first at the battlefield and awaits the enemy is at ease' (致人而不致于人).",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'zhǔ dòng' (214-51). Dip low on 'zhǔ', then drop decisively on 'dòng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "玉", "pinyin": "yù", "meaning_en": "jade", "distinction_note": "Dot inside lower right instead of top flame dot"},
                {"character": "王", "pinyin": "wáng", "meaning_en": "king", "distinction_note": "Lacks the upper flame dot 丶 of 主"},
                {"character": "功", "pinyin": "gōng", "meaning_en": "merit", "distinction_note": "Work 工 on left instead of 云"},
                {"character": "幼", "pinyin": "yòu", "meaning_en": "young", "distinction_note": "Yao 幺 on left instead of 云"}
            ],
            "etymological_cognates": [
                {"character": "主人", "pinyin": "zhǔrén", "gloss_en": "master; host"},
                {"character": "主张", "pinyin": "zhǔzhāng", "gloss_en": "advocate; proposition"},
                {"character": "动作", "pinyin": "dòngzuò", "gloss_en": "movement; action"},
                {"character": "自动", "pinyin": "zìdòng", "gloss_en": "automatic; voluntary"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "主动 emphasizes seizing the initiative, acting by internal drive, and controlling circumstances.",
            "contrasts": [
                {"id": 1, "compared_word": "主动 vs. 被动", "pinyin": "bèidòng", "analysis": "被动 is the direct antonym meaning passive, reactive, or driven against one's will."},
                {"id": 2, "compared_word": "主动 vs. 积极", "pinyin": "jījí", "analysis": "积极 stresses enthusiastic and optimistic attitude, while 主动 emphasizes taking self-directed initiative."},
                {"id": 3, "compared_word": "主动 vs. 盲动", "pinyin": "mángdòng", "analysis": "盲动 means rash, blind action without planning, contrasting with calculated 主动."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "《孙子兵法》有云：“善战者，致人而不致于人。”高明的将领善于调动敌人，而不是被敌人牵着鼻子走。长平之战中，赵括自恃勇武盲目主动出击，反而丧失了战局的主动权，被狡猾的秦军分割包围在狭长山谷之中。",
                "pinyin": "Sūnzǐ Bīngfǎ yǒu yún: 'Shàn zhàn zhě, zhì rén ér bù zhì yú rén.' Gāomíng de jiànglǐng shànyú diàodòng dírén, ér bùshì bèi dírén qiānzhe bízi zǒu. Chángpíng zhī zhàn zhōng, Zhào Kuò zìshì yǒngwǔ mángmù zhǔdòng chūjī, fǎn'ér sàngshī le zhànjú de zhǔdòngquán, bèi jiǎohuá de Qínjūn fēngē-bāowéi zài xiácháng shāngǔ zhīzhōng.",
                "en": "The Art of War states: 'The skilled warrior moves the enemy rather than being moved.' In Changping, Zhao Kuo's rash initiative surrendered genuine initiative, allowing the Qin army to lure and encircle him in a narrow gorge.",
                "es": "Sun Tzu afirmó: 'El diestro en la guerra hace que el enemigo acuda a él, no va donde el enemigo quiere.' En Changping, la imprudente iniciativa de Zhao Kuo le hizo perder el control, siendo cercado en una angosta garganta."
            },
            {
                "id": "#2",
                "hanzi": "在当今充满机遇与挑战的职场竞争中，具备主动作为的意识往往是脱颖而出的关键。与其坐等任务下达，不如主动思考问题、主动寻找解决突破口。积极主动的人总能在平凡的岗位上创造出非凡的业绩。",
                "pinyin": "Zài dāngjīn chōngmǎn jīyù yǔ tiǎozhàn de zhíchǎng jìngzhēng zhōng, jùbèi zhǔdòng zuòwéi de yìshí wǎngwǎng shì tuōyǐng-érchū de guānjiàn. Yǔqí zuò děng rènwu xiàdá, bùrú zhǔdòng sīkǎo wèntí, zhǔdòng xúnzhǎo jiějué tūpòkǒu. Jījí-zhǔdòng de rén zǒng néng zài píngfán de gǎngwèi shang chuàngzào chū fēifán de yèjì.",
                "en": "In today's career competition, a proactive mindset is the key to standing out. Rather than sitting waiting for orders, proactively seeking solutions empowers individuals to achieve extraordinary feats in any role.",
                "es": "En la carrera profesional, la proactividad distingue a los sobresalientes. En vez de aguardar órdenes pasivamente, buscar soluciones por iniciativa propia permite forjar logros extraordinarios en cualquier puesto."
            }
        ]
    },

    # 18 挑战
    {
        "id": "18",
        "hanzi": "挑战",
        "pinyin": "tiǎo zhàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to challenge; defy; challenge (noun)",
            "es": "desafiar; retar; reto; desafío"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to invite an opponent to a contest, fight, or duel; to confront difficult trials or obstacles",
                "definition_es": "desafiar o retar a un oponente al combate o competición; afrontar dificultades exigentes",
                "example_phrase": "迎接严峻挑战 (face grim challenges)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军为了诱使赵括脱离坚固阵地，多次派出小股先锋部队到赵军营垒前叫阵挑战、大声辱骂。",
                "pinyin": "Qínjūn wèile yòushǐ Zhào Kuò tuōlí jiāngù zhèndì, duō cì pài chū xiǎo gǔ xiānfēng bùduì dào Zhàojūn yínglěi qián jiàozhèn tiǎozhàn, dàshēng rǔmà.",
                "en": "To lure Zhao Kuo away from fortified positions, Qin repeatedly sent vanguard units to challenge and taunt before Zhao camps.",
                "es": "Para tentar a Zhao Kuo a abandonar sus baluartes, Qin envió destacamentos a proferir retos e insultos ante el campamento enemigo."
            },
            {
                "id": "#2",
                "hanzi": "青年科研工作者应当敢于挑战学术权威，勇于在未知的科技无人区探索创新路径。",
                "pinyin": "Qīngnián kēyán gōngzuòzhě yīngdāng gǎnyú tiǎozhàn xuéshù quánwēi, yǒngyú zài wèizhī de kējì wúrénqū tànsuǒ chuàngxīn lùjìng.",
                "en": "Young researchers should dare to challenge academic dogmas and boldly explore innovative paths in uncharted scientific frontiers.",
                "es": "Los jóvenes científicos deben atreverse a desafiar dogmas consagrados y explorar sendas inéditas en la vanguardia del saber."
            }
        ],
        "collocations": [
            {"hanzi": "迎接挑战", "en": "meet / embrace challenges"},
            {"hanzi": "面临挑战", "en": "face / confront challenges"},
            {"hanzi": "发起挑战", "en": "launch a challenge"},
            {"hanzi": "巨大的挑战", "en": "formidable / massive challenge"},
            {"hanzi": "挑战极限", "en": "challenge the limits"},
            {"hanzi": "挑战权威", "en": "challenge authority"}
        ],
        "idioms": [
            {"hanzi": "明知山有虎，偏向虎山行", "pinyin": "míng zhī shān yǒu hǔ, piān xiàng hǔ shān xíng", "meaning_en": "go forward deliberately into danger despite knowing hazards"},
            {"hanzi": "乘风破浪", "pinyin": "chéng fēng pò làng", "meaning_en": "brave the wind and waves; forge ahead through adversity"},
            {"hanzi": "挺身而出", "pinyin": "tǐng shēn ér chū", "meaning_en": "step forward bravely to meet the challenge"},
            {"hanzi": "越战越勇", "pinyin": "yuè zhàn yuè yǒng", "meaning_en": "grow braver and more resolute with each battle"}
        ],
        "character_decomposition": [
            {
                "character": "挑",
                "pinyin": "tiǎo",
                "meaning_en": "provoke; incite; prick; lift up",
                "meaning_es": "provocar; incitar; alzar con la punta; azuzar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand action) + 兆 (signs / portents / crackles)",
                "sound_component": "兆 (zhào / tiāo)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Using a hand 扌 or spear tip to prick and stir up 兆 reactions; signifies inciting combat.",
                "visual_mnemonic_story_en": "Using a weapon tip with hands (扌) to prod and provoke an opponent into a duel (挑).",
                "visual_mnemonic_story_es": "Usar la punta de la lanza con las manos (扌) para azuzar al contrincante al duelo (挑).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "QLMO",
                "traditional": "挑"
            },
            {
                "character": "战",
                "pinyin": "zhàn",
                "meaning_en": "war; battle; combat; fight",
                "meaning_es": "guerra; batalla; combate; luchar",
                "radical": "戈",
                "radical_meaning_en": "dagger-axe / halberd",
                "meaning_component": "占 (territory claimed by divination) + 戈 (striking halberd)",
                "sound_component": "占 (zhàn)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Wielding bronze halberds 戈 in battle to contest territory 占; signifies combat.",
                "visual_mnemonic_story_en": "Wielding battle weapons (戈) to contest war prizes in combat (战).",
                "visual_mnemonic_story_es": "Empuñar las armas de bronce (戈) en el fragor de la contienda armada (战).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YRI",
                "traditional": "戰"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Prodding an adversary with hands (挑) to enter armed combat (战) constitutes a challenge (挑战).",
            "composite_memory_hook_es": "Provocar al contrincante (挑) para batirse en combate armado (战) conforma un desafío (挑战).",
            "cultural_and_cognitive_roots": "Originates from ancient chivalric dueling where heralds cast down gauntlets before battle lines ('叫战').",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'tiǎo zhàn' (214-51). Dip low on 'tiǎo', dropping sharply on 'zhàn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "桃", "pinyin": "táo", "meaning_en": "peach", "distinction_note": "Wood radical 木 on left instead of 扌"},
                {"character": "跳", "pinyin": "tiào", "meaning_en": "jump", "distinction_note": "Foot radical 足 on left instead of 扌"},
                {"character": "站", "pinyin": "zhàn", "meaning_en": "stand; station", "distinction_note": "Stand 立 on left instead of 戈 on right"},
                {"character": "贴", "pinyin": "tiē", "meaning_en": "stick; paste", "distinction_note": "Shell 贝 on left of 占"}
            ],
            "etymological_cognates": [
                {"character": "挑衅", "pinyin": "tiǎoxìn", "gloss_en": "provoke; incite defiance"},
                {"character": "挑选", "pinyin": "tiāoxuǎn", "gloss_en": "choose; pick (first tone tiāo)"},
                {"character": "战胜", "pinyin": "zhànshèng", "gloss_en": "vanquish; overcome"},
                {"character": "应战", "pinyin": "yìngzhàn", "gloss_en": "accept a battle challenge"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "挑战 involves initiating combat or confronting daunting obstacles requiring grit and skill.",
            "contrasts": [
                {"id": 1, "compared_word": "挑战 vs. 迎战", "pinyin": "yíngzhàn", "analysis": "挑战 is issuing the challenge, while 迎战 is accepting and facing the challenge incoming."},
                {"id": 2, "compared_word": "挑战 vs. 挑衅", "pinyin": "tiǎoxìn", "analysis": "挑衅 carries malicious, bullying provocation, whereas 挑战 is often noble, athletic, or ambitious."},
                {"id": 3, "compared_word": "挑战 vs. 退缩", "pinyin": "tuìsuō", "analysis": "退缩 is the direct antonym meaning to cower back from difficulties."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平前线，秦军将领深知赵括年少气盛、急于求成的性格弱点，每日派出小队骑兵到赵军壁垒前叫骂挑战。廉颇在位时对挑衅置之不理，而赵括一上任便按捺不住怒火，不顾地形险峻仓促应战，正中秦军诡计。",
                "pinyin": "Chángpíng qiánxiàn, Qínjūn jiànglǐng shēnzhī Zhào Kuò niánshào-qìshèng, jíyú-qiúchéng de xìnggé ruòdiǎn, měirì pài chū xiǎoduì qíbīng dào Zhàojūn bìlěi qián jiàomà tiǎozhàn. Lián Pō zàiwèi shí duì tiǎoxìn zhìzhī-bùlǐ, ér Zhào Kuò yī shàngrèn biàn ànnà-bùzhù nùhuǒ, bùgù dìxíng xiǎnjùn cāngcù yìngzhàn, zhèngzhòng Qínjūn guǐjì.",
                "en": "At Changping, Qin commanders knew Zhao Kuo's youthful impatience and sent daily riders to taunt and challenge him. Lian Po ignored them, but Zhao Kuo could not contain his fury, rushing into battle and falling into the ambush.",
                "es": "En Changping, los mandos de Qin sabían de la impetuosa soberbia de Zhao Kuo y enviaron jinetes a insultarlo a las puertas. Lian Po los ignoraba; Zhao Kuo, enfurecido, salió a combatir cayendo en la celada."
            },
            {
                "id": "#2",
                "hanzi": "人生就是一场不断战胜未知与迎接挑战的壮丽旅程。无论前方的道路多么坎坷漫长，敢于直面挑战、把艰难险阻视作磨砺意志的宝贵财富，我们才能在一次次风浪考验中强健筋骨，最终实现人生的崇高飞跃。",
                "pinyin": "Rénshēng jiùshì yī chǎng bùduàn zhànshèng wèizhī yǔ yíngjiē tiǎozhàn de zhuànglì lǚchéng. Wúlùn qiánfāng de dàolù duōme kǎnkě màncháng, gǎnyú zhímiàn tiǎozhàn, bǎ jiānnán-xiǎnzǔ shìzuò mólì yìzhì de bǎoguì cáifù, wǒmen cái néng zài yī cì cì fēnglàng kǎoyàn zhōng qiángjiàn jīngǔ, zuìzhōng shíxiàn rénshēng de chónggāo fēiyuè.",
                "en": "Life is a journey of overcoming the unknown and embracing challenges. No matter how rugged the road ahead, facing trials bravely and treating adversity as a forge of will fortifies us to achieve sublime leaps of character.",
                "es": "La vida es una travesía de retos y descubrimientos. Por áspero que sea el camino, encarar los desafíos y asumir los obstáculos como templanza del alma nos fortalece para consumar grandes hazañas personales."
            }
        ]
    },

    # 19 骂
    {
        "id": "19",
        "hanzi": "骂",
        "pinyin": "mà",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to curse; scold; abuse verbally; call names",
            "es": "maldecir; insultar; reñir; increpar; reprender"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to utter abusive words, scold angrily, curse, or reprimand someone harshly",
                "definition_es": "proferir insultos, improperios o reprender ásperamente a alguien con enfado",
                "example_phrase": "大声斥骂 (scold and reprimand loudly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军将士遵照白起的密令，在赵军营垒前日夜大声叫骂，讽刺赵括不过是个不敢出战的胆小鬼。",
                "pinyin": "Qínjūn jiàngshì zūnjào Bái Qǐ de mìlìng, zài Zhàojūn yínglěi qián rìyè dàshēng jiàomà, fěngcì Zhào Kuò bùguò shì gè bù gǎn chūzhàn de dǎnxiǎoguǐ.",
                "en": "Following Bai Qi's secret order, Qin soldiers shouted curses day and night outside Zhao's camp, taunting Zhao Kuo as a coward who feared battle.",
                "es": "Cumpliendo órdenes de Bai Qi, los soldados de Qin insultaban noche y día ante el campamento, tildando a Zhao Kuo de cobarde asustadizo."
            },
            {
                "id": "#2",
                "hanzi": "母亲并没有厉声责骂犯错的孩子，而是温和地拉着他的手，耐心地讲明做人应当诚实的道理。",
                "pinyin": "Mǔqīn bìng méiyǒu lìshēng zémà fàncuò de háizi, ér shì wēnhé de lā zhe tā de shǒu, nàixīn de jiǎngmíng zuòrén yīngdāng chéngshí de dàolǐ.",
                "en": "The mother did not harshly scold her errant child; instead, taking his hand gently, she patiently explained the principle of honesty.",
                "es": "La madre no reprendió con aspereza al hijo que erró; tomándole la mano con ternura, le explicó con paciencia el deber de la honradez."
            }
        ],
        "collocations": [
            {"hanzi": "责骂批评", "en": "scold and criticize"},
            {"hanzi": "大声叫骂", "en": "shout curses loudly"},
            {"hanzi": "挨骂受气", "en": "get scolded and suffer abuse"},
            {"hanzi": "骂人粗话", "en": "curse at people / profanities"},
            {"hanzi": "破口大骂", "en": "burst into abusive curses"},
            {"hanzi": "痛骂一顿", "en": "give someone a fierce dressing-down"}
        ],
        "idioms": [
            {"hanzi": "破口大骂", "pinyin": "pò kǒu dà mà", "meaning_en": "burst out into violent verbal abuse and cursing"},
            {"hanzi": "嬉笑怒骂", "pinyin": "xī xiào nù mà", "meaning_en": "ridiculing, joking, and scolding freely in literary prose"},
            {"hanzi": "恶语伤人", "pinyin": "è yǔ shāng rén", "meaning_en": "hurting people with cruel and venomous words"},
            {"hanzi": "忍气吞声", "pinyin": "rěn qì tūn shēng", "meaning_en": "swallow one's anger and endure insult without reply"}
        ],
        "character_decomposition": [
            {
                "character": "骂",
                "pinyin": "mà",
                "meaning_en": "scold; curse; abuse verbally",
                "meaning_es": "reñir; maldecir; insultar; increpar",
                "radical": "马",
                "radical_meaning_en": "horse",
                "meaning_component": "吅 (two mouths shouting loudly) + 马 (horse galloping / phonetic)",
                "sound_component": "马 (mǎ)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two open mouths 吅 clamoring noisily over a horse 马; signifies shouting verbal abuse and scolding.",
                "visual_mnemonic_story_en": "Two mouths (吅) shouting noisy angry words over a rearing horse (马) in abusive fury (骂).",
                "visual_mnemonic_story_es": "Dos bocas que vociferan (吅) improperios sobre un corcel enfurecido (马) al increpar (骂).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "RRNS",
                "traditional": "罵"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Two shouting mouths (吅) roaring like an agitated stallion (马) signifies abusive scolding (骂).",
            "composite_memory_hook_es": "Dos bocas vociferantes (吅) rugiendo con la furia de un potro (马) encarnan la acción de insultar o reñir (骂).",
            "cultural_and_cognitive_roots": "Common psychological warfare tactic in ancient Chinese battles ('骂阵') used to irritate hotheaded commanders into blunders.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'mà' (51). Sharp, short, and emphatic downward inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "马", "pinyin": "mǎ", "meaning_en": "horse", "distinction_note": "Lacks the two mouth radical 吅 on top"},
                {"character": "驾", "pinyin": "jià", "meaning_en": "drive; harness", "distinction_note": "Add 加 on top of 马 instead of 吅"},
                {"character": "骂 (traditional 罵)", "pinyin": "mà", "meaning_en": "curse", "distinction_note": "Simplified has 吅 over 马 instead of 网/罒"},
                {"character": "哭", "pinyin": "kū", "meaning_en": "cry; weep", "distinction_note": "Dog 犬 under 吅 instead of 马"}
            ],
            "etymological_cognates": [
                {"character": "斥责", "pinyin": "chìzé", "gloss_en": "reprimand; denounce"},
                {"character": "谩骂", "pinyin": "mànmà", "gloss_en": "hurl abuses; vilify"},
                {"character": "辱骂", "pinyin": "rǔmà", "gloss_en": "insult and curse"},
                {"character": "责备", "pinyin": "zébèi", "gloss_en": "blame; reprove"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "骂 focuses on angry, abusive, or disciplinary vocal chastisement.",
            "contrasts": [
                {"id": 1, "compared_word": "骂 vs. 批评", "pinyin": "pīpíng", "analysis": "批评 is rational objective critique of errors, while 骂 carries angry verbal scolding or profanity."},
                {"id": 2, "compared_word": "骂 vs. 夸", "pinyin": "kuā", "analysis": "夸 is the direct antonym meaning to praise, flatter, or compliment."},
                {"id": 3, "compared_word": "骂 vs. 劝", "pinyin": "quàn", "analysis": "劝 means gentle, patient persuasion, whereas 骂 is harsh and aggressive reprimand."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在长平之战的营垒前，秦军深谙攻心之道。他们派出精悍骑兵在阵前大声叫骂，讽刺赵军将领怯懦无能。老将廉颇心如磐石、置若罔闻，而年轻自负的赵括却经受不住敌军的嘲弄与辱骂，怒火攻心，终于铸成大错。",
                "pinyin": "Zài Chángpíng zhī zhàn de yínglěi qián, Qínjūn shēn'ān gōngxīn zhī dào. Tāmen pài chū jīnghàn qíbīng zài zhènqián dàshēng jiàomà, fěngcì Zhàojūn jiànglǐng qiènuò-wúnéng. Lián Pō xīnrúpánshí, zhìruòwǎngwén, ér niánqīng zìfù de Zhào Kuò què jīngshòu bù zhù díjūn de cháonòng yǔ rǔmà, nùhuǒ-gōngxīn, zhōngyú zhùchéng dàcuò.",
                "en": "Outside Changping camps, Qin practiced psychological warfare. Horsemen shouted abuses at the gates taunting Zhao generals. Lian Po remained deaf like rock, but vain Zhao Kuo could not endure curses, rushing out in blinding fury.",
                "es": "Ante las trincheras de Changping, Qin libró guerra psicológica. Jinetes vociferaban insultos denigrando al mando enemigo. Lian Po se mantuvo impávido como una roca, mas el vanidoso Zhao Kuo no toleró la mofa y cayó en la trampa."
            },
            {
                "id": "#2",
                "hanzi": "“良言一句三冬暖，恶语伤人六月寒。”在日常人际交往与家庭教育中，粗暴的责骂往往只会激化矛盾、刺伤自尊，而无法真正解决问题。学会克制怒气、心平气和地沟通，是衡量一个人修养与情商的重要标尺。",
                "pinyin": "'Liángyán yījù sāndōng nuǎn, èyǔ shāngrén liùyuè hán.' Zài rìcháng rénjì jiāowǎng yǔ jiātíng jiàoyù zhōng, cūbào de zémà wǎngwǎng zhǐ huì jīhuà máodùn, cìshāng zìzūn, ér wúfǎ zhēnzhèng jiějué wèntí. Xuéhuì kèzhì nùqì, xīnpíng-qìhé de gōutōng, shì héngliáng yī gè rén xiūyǎng yǔ qíngshāng de zhòngyào biāochǐ.",
                "en": "'A kind word warms three winter months; cruel words chill in June.' In daily relationships and education, harsh curses only aggravate friction and hurt dignity. Controlling anger and speaking calmly reflects high character and empathy.",
                "es": "'Una palabra afable calienta tres inviernos; la ofensa hiela en pleno estío.' En el hogar y la vida social, los improperios solo agravan heridas; refrenar la ira y dialogar con mesura es la prueba del temple humano."
            }
        ]
    },

    # 20 胆小鬼
    {
        "id": "20",
        "hanzi": "胆小鬼",
        "pinyin": "dǎn xiǎo guǐ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "coward; craven person; chicken",
            "es": "cobarde; gallina; pusilánime; miedica"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person who utterly lacks courage, is easily frightened, or shrinks from difficulty or danger",
                "definition_es": "persona timorata que carece de valor, se asusta fácilmente o huye ante el peligro",
                "example_phrase": "骂他是胆小鬼 (call him a coward)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军为了激怒赵括出战，故意派人在营垒前大声嘲笑他是只敢缩在堡垒里的胆小鬼。",
                "pinyin": "Qínjūn wèile jìnù Zhào Kuò chūzhàn, gùyì pài rén zài yínglěi qián dàshēng cháoxiào tā shì zhǐ gǎn suō zài bǎolěi lǐ de dǎnxiǎoguǐ.",
                "en": "To provoke Zhao Kuo into combat, Qin deliberately sent men to laugh outside his camp, taunting him as a coward hiding in bastions.",
                "es": "Para provocar la furia de Zhao Kuo, Qin envió emisarios a mofarse de él llamándole cobarde refugiado tras las murallas."
            },
            {
                "id": "#2",
                "hanzi": "面对突如其来的危急关头，真正的勇士绝不做临阵脱逃的胆小鬼，而是挺身而出勇挑重担。",
                "pinyin": "Miànduì tūrúqílái de wēijí guāntóu, zhēnzhèng de yǒngshì jué bù zuò línzhèn-tuōtáo de dǎnxiǎoguǐ, ér shì tǐngshēn'érchū yǒng tiāo zhòngdàn.",
                "en": "Facing sudden peril, true warriors never act as cowards fleeing from battle; instead, they step forward bravely to shoulder burdens.",
                "es": "Ante la adversidad repentina, el verdadero valiente rehúsa ser un cobarde que deserte; da un paso al frente asumiendo el deber."
            }
        ],
        "collocations": [
            {"hanzi": "做胆小鬼", "en": "be / act like a coward"},
            {"hanzi": "不是胆小鬼", "en": "not a coward"},
            {"hanzi": "嘲笑胆小鬼", "en": "mock someone as a coward"},
            {"hanzi": "胆小鬼行为", "en": "cowardly behavior"},
            {"hanzi": "被称为胆小鬼", "en": "be called a coward"},
            {"hanzi": "胆小怕事", "en": "timid and cowardly afraid of trouble"}
        ],
        "idioms": [
            {"hanzi": "胆小如鼠", "pinyin": "dǎn xiǎo rú shǔ", "meaning_en": "as timid as a mouse; gutless"},
            {"hanzi": "贪生怕死", "pinyin": "tān shēng pà sǐ", "meaning_en": "craving life and fearing death; cowardly"},
            {"hanzi": "胆大包天", "pinyin": "dǎn dà bāo tiān", "meaning_en": "audacious enough to cover the sky; bold and daring (antonym)"},
            {"hanzi": "视死如归", "pinyin": "shì sǐ rú guī", "meaning_en": "look upon death as going home; fearless hero"}
        ],
        "character_decomposition": [
            {
                "character": "胆",
                "pinyin": "dǎn",
                "meaning_en": "gallbladder; courage; guts; bravery",
                "meaning_es": "vesícula biliar; valor; agallas; coraje",
                "radical": "月",
                "radical_meaning_en": "flesh / organ",
                "meaning_component": "月/肉 (flesh / internal organ) + 旦 (dawn rising sun)",
                "sound_component": "旦 (dàn)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "The bodily internal organ 月 that generates resolute courage like the rising morning sun 旦.",
                "visual_mnemonic_story_en": "An internal organ (月) radiating courage and boldness like the dawn sun (旦) to form guts (胆).",
                "visual_mnemonic_story_es": "Una entraña vital (月) que irradia valentía al nacer el sol (旦), sede del coraje (胆).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "BAM",
                "traditional": "膽"
            },
            {
                "character": "小",
                "pinyin": "xiǎo",
                "meaning_en": "small; tiny; little; young",
                "meaning_es": "pequeño; diminuto; menor",
                "radical": "小",
                "radical_meaning_en": "small",
                "meaning_component": "a vertical object split in half into tiny flecks",
                "sound_component": "小 (xiǎo)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A vertical mark divided into two tiny side specks; indicates smallness.",
                "visual_mnemonic_story_en": "Dividing a small stone into tiny flecks (小).",
                "visual_mnemonic_story_es": "Partir una pequeña piedra en diminutas esquirlas (小).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "NC",
                "traditional": "小"
            },
            {
                "character": "鬼",
                "pinyin": "guǐ",
                "meaning_en": "ghost; spirit; crafty person; fellow",
                "meaning_es": "fantasma; espectro; pillo; tipo",
                "radical": "鬼",
                "radical_meaning_en": "ghost",
                "meaning_component": "kneeling human figure with an oversized eerie mask/skull",
                "sound_component": "鬼 (guǐ)",
                "stroke_count": 9,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A spirit or human wearing an uncanny skull-like head mask; used colloquially for a specific type of person.",
                "visual_mnemonic_story_en": "A figure with a mask scurrying in the shadows like an eerie apparition (鬼).",
                "visual_mnemonic_story_es": "Una silueta enmascarada que se escurre en la penumbra espectral (鬼).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "HUI",
                "traditional": "鬼"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A person whose courage (胆) is minutely tiny (小) and acts like a skittish phantom (鬼) is a coward (胆小鬼).",
            "composite_memory_hook_es": "Aquel cuyo coraje (胆) es diminuto (小) y huye como una sombra asustadiza (鬼) es un cobarde (胆小鬼).",
            "cultural_and_cognitive_roots": "Traditional Chinese medicine associates the gallbladder (胆) with decisiveness and bravery; '胆小' indicates faint-heartedness.",
            "tone_sandhi_and_pitch_modulation": "Third tone sandhi chain: 'dǎn xiǎo guǐ' -> pronounced 'dán xiáo guǐ' (35-35-214). The first two syllables shift to second tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "但", "pinyin": "dàn", "meaning_en": "but; however", "distinction_note": "Person radical 亻 on left instead of 月"},
                {"character": "少", "pinyin": "shǎo", "meaning_en": "few; little", "distinction_note": "Has downward right-slanting stroke across bottom"},
                {"character": "魁", "pinyin": "kuí", "meaning_en": "chief; head", "distinction_note": "Dipper 斗 on right of 鬼"},
                {"character": "魂", "pinyin": "hún", "meaning_en": "soul; spirit", "distinction_note": "Cloud 云 on left of 鬼"}
            ],
            "etymological_cognates": [
                {"character": "大胆", "pinyin": "dàdǎn", "gloss_en": "bold; audacious"},
                {"character": "胆量", "pinyin": "dǎnliàng", "gloss_en": "courage; guts"},
                {"character": "醉鬼", "pinyin": "zuìguǐ", "gloss_en": "drunkard"},
                {"character": "机灵鬼", "pinyin": "jīlingguǐ", "gloss_en": "clever little rascal"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "胆小鬼 is an informal colloquial noun mocking someone who shrinks from fright or lacks fortitude.",
            "contrasts": [
                {"id": 1, "compared_word": "胆小鬼 vs. 勇士", "pinyin": "yǒngshì", "analysis": "勇士 is the direct antonym meaning a brave, fearless warrior."},
                {"id": 2, "compared_word": "胆小鬼 vs. 英雄", "pinyin": "yīngxióng", "analysis": "英雄 is an admired heroic champion, opposite to craven 胆小鬼."},
                {"id": 3, "compared_word": "胆小鬼 vs. 懦夫", "pinyin": "nuòfū", "analysis": "懦夫 is formal literary for coward, whereas 胆小鬼 is the common spoken idiom."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在古代两军对垒中，如何激怒敌将是一门攻心战术。秦军在阵前高声讽刺赵括是“只配躲在营垒里喝稀饭的胆小鬼”。自幼心高气傲的赵括哪堪忍受这般当众羞辱，为了证明自己不是胆小鬼，他不顾一切地下令全军出击，最终惨败。",
                "pinyin": "Zài gǔdài liǎng jūn duìlěi zhōng, rúhé jìnù díjiàng shì yī mén gōngxīn zhànshù. Qínjūn zài zhènqián gāoshēng fěngcì Zhào Kuò shì 'zhǐ pèi duǒ zài yínglěi lǐ hē xīfàn de dǎnxiǎoguǐ'. Zìyòu xīngāo-qì'ào de Zhào Kuò nǎ kān rěnshòu zhè bān dāngzhòng xiūrǔ, wèile zhèngmíng zìjǐ bùshì dǎnxiǎoguǐ, tā bùgù-yīqiè de xiàlìng quán jūn chūjī, zuìzhōng cǎibài.",
                "en": "Provoking opposing generals was psychological warfare. Qin soldiers shouted that Zhao Kuo was a coward fit only to sip porridge in camp. Vain Zhao Kuo could not endure the humiliation; to prove he was no coward, he attacked and lost all.",
                "es": "En la guerra antigua, exasperar al general rival era un arte sutil. Qin gritaba que Zhao Kuo era un cobarde apto solo para tomar gachas en su tienda. El soberbio Zhao Kuo no soportó la afrenta; para demostrar su valor atacó y pereció."
            },
            {
                "id": "#2",
                "hanzi": "面对生活中的挫折与困难，承认害怕并不等于就是懦弱的胆小鬼。真正的勇敢不是毫无畏惧，而是在内心感到恐惧时，依然选择直面风浪、坚定地迈开脚步向前探索。克服恐惧的过程，正是心灵由弱小走向强大的必经之路。",
                "pinyin": "Miànduì shēnghuó zhōng de cuòzhé yǔ kùnnan, chéngrèn hàipà bìng bù děngyú jiùshì nuòruò de dǎnxiǎoguǐ. Zhēnzhèng de yǒnggǎn bùshì háowú wèijù, ér shì zài nèixīn gǎndào kǒngjù shí, yīrán xuǎnzé zhímiàn fēnglàng, jiāndìng de màikāi jiǎobù xiàngqián tànsuǒ. Kèfú kǒngjù de guòchéng, zhèngshì xīnlíng yóu ruòxiǎo zǒuxiàng qiángdà de bìjīng zhī lù.",
                "en": "Admitting fear before life's setbacks does not make one a coward. True bravery is not the absence of fear, but pressing forward into the storm despite fear. Conquering terror is how the soul matures from frailty into strength.",
                "es": "Reconocer el temor ante la adversidad no nos convierte en cobardes. El auténtico coraje no estriba en no sentir miedo, sino en marchar hacia la tempestad a pesar del pánico; vencer el recelo transforma la flaqueza en entereza."
            }
        ]
    }
]

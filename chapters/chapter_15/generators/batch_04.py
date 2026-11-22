# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 糊涂
    {
        "id": "31",
        "hanzi": "糊涂",
        "pinyin": "hú tu",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "confused; muddle-headed; foolish; blurred",
            "es": "confundido; confuso; despistado; aturdido"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "muddle-headed; lacking clear thinking or judgment; confused",
                "definition_es": "confundido; falto de juicio lúcido; con la mente embotada",
                "example_phrase": "头脑糊涂 (muddle-headed mind)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "长平阵前战局万分危急，主帅如果头脑糊涂、盲目听信虚假情报，势必会导致全军覆没的惨剧。",
                "pinyin": "Chángpíng zhènqián zhànjú wànfēn wēijí, zhǔshuài rúguǒ tóunǎo hútu, mángmù tīngxìn xūjiǎ qíngbào, shìbì huì dǎozhì quánjūn fùmò de cǎnjù.",
                "en": "At the frontlines of Changping the situation was critical; if the commander was muddle-headed and blindly trusted false intelligence, total army disaster was inevitable.",
                "es": "En el frente de Changping la situación era crítica; si el general estaba confundido y creía ciegamente informes falsos, la destrucción del ejército era ineludible."
            },
            {
                "id": "#2",
                "hanzi": "在这个关乎企业未来生死的重大投资决策上，董事会绝对不能犯糊涂，必须进行周密调研。",
                "pinyin": "Zài zhè ge guānhū qǐyè wèilái shēngsǐ de zhòngdà tóuzī juécè shang, dǒngshìhuì juéduì bù néng fàn hútu, bìxū jìnxíng zhōumì diàoyán.",
                "en": "On this major investment decision concerning the company's survival, the board must never be foolishly muddled; rigorous research is imperative.",
                "es": "En esta crucial decisión de inversión para el porvenir corporativo, la junta directiva no debe cometer torpezas; es indispensable investigar a fondo."
            }
        ],
        "collocations": [
            {"hanzi": "犯糊涂", "en": "make a foolish blunder / act muddle-headed"},
            {"hanzi": "脑子糊涂", "en": "confused in thought / muddled mind"},
            {"hanzi": "一时糊涂", "en": "momentary lapse of reason"},
            {"hanzi": "装糊涂", "en": "feign ignorance / play dumb"},
            {"hanzi": "稀里糊涂", "en": "careless and confused / in a muddle"},
            {"hanzi": "糊涂账", "en": "chaotic accounts / messy situation"}
        ],
        "idioms": [
            {"hanzi": "难得糊涂", "pinyin": "nán dé hú tu", "meaning_en": "where ignorance is bliss; blessed carelessness in small matters"},
            {"hanzi": "一塌糊涂", "pinyin": "yī tà hú tu", "meaning_en": "in an awful mess; in complete shambles"},
            {"hanzi": "糊里糊涂", "pinyin": "hú li hú tu", "meaning_en": "dazed and muddled; completely confused"},
            {"hanzi": "不省人事", "pinyin": "bù xǐng rén shì", "meaning_en": "fall unconscious; insensible to surroundings"}
        ],
        "character_decomposition": [
            {
                "character": "糊",
                "pinyin": "hú",
                "meaning_en": "paste; porridge; stick together; blur",
                "meaning_es": "pasta; engrudo; pegar; nublar",
                "radical": "米",
                "radical_meaning_en": "rice",
                "meaning_component": "米 (rice porridge / sticky cereal paste)",
                "sound_component": "胡 (hú)",
                "stroke_count": 15,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Boiling down rice 米 into sticky opaque porridge 胡 that clouds transparency; signifies blurred opacity.",
                "visual_mnemonic_story_en": "Sticky rice paste (米) spread thick (胡), blurring all clarity (糊).",
                "visual_mnemonic_story_es": "Una pasta espesa de arroz (米) que al untarse (胡) nubla la visión de todo (糊).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "FDJRB",
                "traditional": "糊"
            },
            {
                "character": "涂",
                "pinyin": "tu",
                "meaning_en": "smear; daub; mud; erase; route",
                "meaning_es": "untar; embadurnar; lodo; borrar",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water / muddy sludge) + 余 (surplus)",
                "sound_component": "余 (yú)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water 氵 mixed with wet muddy silt smeared across writing to blot it out; signifies coating or confusion.",
                "visual_mnemonic_story_en": "Wet sludge (氵) smeared over clean characters (余) until they become indistinguishable (涂).",
                "visual_mnemonic_story_es": "Lodo acuoso (氵) embadurnado sobre letras limpias (余) hasta borrarlas por completo (涂).",
                "tone_mnemonic_anchor": "neutral",
                "cangjie": "EOMD",
                "traditional": "塗"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Sticky rice paste (糊) smeared around (涂) blinds one's sight, leaving thoughts muddled (糊涂).",
            "composite_memory_hook_es": "Engrudo de arroz (糊) embadurnado (涂) que nubla la vista y confunde el juicio (糊涂).",
            "cultural_and_cognitive_roots": "Derived from culinary pasting and smearing mud, metaphorically applied to mental opacity and indistinct thought.",
            "tone_sandhi_and_pitch_modulation": "Second tone to neutral tone: 'hú tu' (35-neutral). Gentle drop into a short unstressed syllable."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "湖", "pinyin": "hú", "meaning_en": "lake", "distinction_note": "Water 氵 on left instead of rice 米"},
                {"character": "胡", "pinyin": "hú", "meaning_en": "reckless; beard", "distinction_note": "No rice 米 component"},
                {"character": "徐", "pinyin": "xú", "meaning_en": "slow; gentle", "distinction_note": "Step 彳 on left instead of water 氵"},
                {"character": "途", "pinyin": "tú", "meaning_en": "road; journey", "distinction_note": "Walk 辶 radical instead of water 氵"}
            ],
            "etymological_cognates": [
                {"character": "糊口", "pinyin": "húkǒu", "gloss_en": "scrape together a meager livelihood"},
                {"character": "含糊", "pinyin": "hánhu", "gloss_en": "vague; ambiguous"},
                {"character": "涂鸦", "pinyin": "túyā", "gloss_en": "scrawl; graffiti"},
                {"character": "抹涂", "pinyin": "mǎtú", "gloss_en": "daub; smear over"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "糊涂 emphasizes subjective mental haze, poor comprehension, or temporary loss of rational judgment.",
            "contrasts": [
                {"id": 1, "compared_word": "糊涂 vs. 愚蠢", "pinyin": "yúchǔn", "analysis": "愚蠢 denotes inherent intellectual deficit or folly, whereas 糊涂 describes temporary mental confusion or muddled reasoning."},
                {"id": 2, "compared_word": "糊涂 vs. 迷茫", "pinyin": "mímáng", "analysis": "迷茫 refers to feeling lost regarding future orientation, while 糊涂 denotes clouded logical thinking."},
                {"id": 3, "compared_word": "糊涂 vs. 混乱", "pinyin": "hùnluàn", "analysis": "混乱 describes external structural disorder or chaos, while 糊涂 characterizes an internal psychological state."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古来用兵最忌主帅头脑糊涂。赵括自幼熟读兵法，却缺乏实战临机应变的智慧。在长平阵前，面对白起佯装退却的诱敌战术，他头脑糊涂、轻率追击，将四十万精锐送入重围，千古遗恨。",
                "pinyin": "Gǔlái yòngbīng zuì jì zhǔshuài tóunǎo hútu. Zhào Kuò zìyòu shúdú bīngfǎ, què quēfá shízhàn línjī-yìngbiàn de zhìhuì. Zài Chángpíng zhènqián, miànduì Bái Qǐ yángzhuāng tuìquè de yòudí zhànshù, tā tóunǎo hútu, qīngshuài zhuījī, jiāng sìshí wàn jīngruì sòngrù zhòngwéi, qiāngǔ yíhèn.",
                "en": "In military history, nothing was more fatal than a commander being muddle-headed. Zhao Kuo had memorized tactics from childhood but lacked adaptive wisdom. Lured by Bai Qi's feigned retreat, his muddled thinking led 400,000 elite troops into total encirclement.",
                "es": "En la historia bélica nada fue más nefasto que un general confuso. Zhao Kuo dominaba la teoría pero carecía de agilidad práctica. Ante la falsa retirada de Bai Qi, su juicio nublado lanzó a 400.000 soldados a un cerco mortal."
            },
            {
                "id": "#2",
                "hanzi": "清代书画家郑板桥题写的“难得糊涂”，向来被奉为人际交往的达观境界。然而为人处世的“糊涂”，是指在非关根本原则的微小私利上不予锱铢必较，在面临国家大义与是非抉择时，心智则须如明镜般洞察秋毫。",
                "pinyin": "Qīngdài shūhuàjiā Zhèng Bǎnqiáo tíxiě de 'nándé hútu', xiànglái bèi fèng wéi rénjì jiāowǎng de dáguān jìngjiè. Rán'ér wéirén chǔshì de 'hútu', shì zhǐ zài fēiguān gēnběn yuánzé de wēixiǎo sīlì shang bù yǔ zīzhū-bìjiào, zài miànlín guójiā dàyì yǔ shìfēi juézé shí, xīnjì zé xū rú míngjìng bān dòngchá-qiūháo.",
                "en": "The famous motto 'where ignorance is bliss' by Zheng Banqiao has long been praised as philosophical detachment. Yet this conscious tolerance applies only to petty personal gains; in confronting major principles and virtue, one's mind must remain crystal clear.",
                "es": "El lema 'dichosa confusión' de Zheng Banqiao siempre ha sido admirado como sabiduría vital. Sin embargo, esa benevolencia solo atañe a pequeñas minucias personales; ante los principios éticos y el bien común, la mente debe conservar una lucidez impecable."
            }
        ]
    },

    # 32 公元
    {
        "id": "32",
        "hanzi": "公元",
        "pinyin": "gōng yuán",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "the Christian Era; Common Era; A.D.",
            "es": "era cristiana; era común; d.C."
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the international calendar system counting years from the traditionally estimated birth of Jesus Christ (CE / AD)",
                "definition_es": "cómputo cronológico internacional que cuenta los años a partir del nacimiento estimado de Jesucristo",
                "example_phrase": "公元前260年 (in 260 BC)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "著名的长平之战发生于公元前260年，它是中国战国时期规模最为庞大的决定性战役。",
                "pinyin": "Zhùmíng de Chángpíng zhī zhàn fāshēng yú gōngyuánqián 260 nián, tā shì Zhōngguó Zhànguó shíqī guīmó zuìwéi pángdà de juédìngxìng zhànyì.",
                "en": "The renowned Battle of Changping took place in 260 BC; it was the largest and most decisive campaign of China's Warring States era.",
                "es": "La célebre batalla de Changping ocurrió en el año 260 a.C.; fue la contienda decisiva de mayor envergadura del período de los Reinos Combatientes."
            },
            {
                "id": "#2",
                "hanzi": "出土的青铜铭文经碳十四测定，证实该古城遗址始建于公元前十一世纪的西周初期。",
                "pinyin": "Chūtǔ de qīngtóng míngwén jīng tàn-shísì cèdìng, zhèngshí gāi gǔchéng yízhǐ shǐjiàn yú gōngyuánqián shíyī shìjì de Xī Zhōu chūqī.",
                "en": "Carbon-14 testing of the excavated bronze inscriptions confirmed the ancient city ruins date back to the early Western Zhou in the 11th century BC.",
                "es": "La datación por carbono 14 de las inscripciones de bronce desenterradas confirmó que la antigua ciudad data de principios de la dinastía Zhou Occidental en el siglo XI a.C."
            }
        ],
        "collocations": [
            {"hanzi": "公元前", "en": "Before Christ (BC / BCE)"},
            {"hanzi": "公元纪年", "en": "Christian Era dating system"},
            {"hanzi": "进入公元", "en": "enter the Common Era"},
            {"hanzi": "公元元年", "en": "the year 1 AD"},
            {"hanzi": "公元初期", "en": "early Common Era"},
            {"hanzi": "公元纪元", "en": "Common Era calendar"}
        ],
        "idioms": [
            {"hanzi": "千秋万代", "pinyin": "qiān qiū wàn dài", "meaning_en": "throughout thousands of autumns and myriad generations; for endless generations"},
            {"hanzi": "历久弥新", "pinyin": "lì jiǔ mí xīn", "meaning_en": "remain fresh and vibrant with the passage of time"},
            {"hanzi": "年深日久", "pinyin": "nián shēn rì jiǔ", "meaning_en": "over prolonged years and days; over a very long span of time"},
            {"hanzi": "旷古绝伦", "pinyin": "kuàng gǔ jué lún", "meaning_en": "unmatched through all antiquity; unsurpassed in history"}
        ],
        "character_decomposition": [
            {
                "character": "公",
                "pinyin": "gōng",
                "meaning_en": "public; universal; fair; male",
                "meaning_es": "público; universal; imparcial; masculino",
                "radical": "八",
                "radical_meaning_en": "eight / divide",
                "meaning_component": "八 (divide outward / open share) + 厶 (private)",
                "sound_component": "公 (gōng)",
                "stroke_count": 4,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Distributing private 厶 resources openly 八 among all people; signifies public, common, and universal.",
                "visual_mnemonic_story_en": "Dividing (八) private goods (厶) to share publicly with everyone (公).",
                "visual_mnemonic_story_es": "Repartir abiertamente (八) lo privado (厶) para beneficio público de todos (公).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "CI",
                "traditional": "公"
            },
            {
                "character": "元",
                "pinyin": "yuán",
                "meaning_en": "first; primary; origin; unit",
                "meaning_es": "primero; primario; origen; unidad",
                "radical": "儿",
                "radical_meaning_en": "human legs",
                "meaning_component": "一 (supreme origin) + 兀/儿 (human head standing upright)",
                "sound_component": "元 (yuán)",
                "stroke_count": 4,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "The head 兀 crowned above the human body; denotes primary beginning, the source, and epoch.",
                "visual_mnemonic_story_en": "The head crowned atop the human figure (儿), representing the original beginning of time (元).",
                "visual_mnemonic_story_es": "La cabeza sobre la figura humana (儿), símbolo del origen primero y fuente primordial (元).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "MMU",
                "traditional": "元"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The public (公) universally agreed upon a common starting epoch (元) for international calendar counting (公元).",
            "composite_memory_hook_es": "La comunidad pública mundial (公) fijó un origen común de partida (元) para fechar los siglos (公元).",
            "cultural_and_cognitive_roots": "Adopted universally to align international chronological frameworks from the birth of Christ across scientific records.",
            "tone_sandhi_and_pitch_modulation": "First tone to second tone: 'gōng yuán' (55-35). High level start rising smoothly in pitch."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "无", "pinyin": "wú", "meaning_en": "none; without", "distinction_note": "Extra stroke and bottom curvature"},
                {"character": "天", "pinyin": "tiān", "meaning_en": "sky; day", "distinction_note": "Central line pierces through differently"},
                {"character": "公", "pinyin": "gōng", "meaning_en": "public; fair", "distinction_note": "Radical 八 on top with 厶 below"},
                {"character": "分", "pinyin": "fēn", "meaning_en": "divide; minute", "distinction_note": "Radical 八 on top with knife 刀 below"}
            ],
            "etymological_cognates": [
                {"character": "纪元", "pinyin": "jìyuán", "gloss_en": "epoch; era"},
                {"character": "元年", "pinyin": "yuánnián", "gloss_en": "first year of a reign or era"},
                {"character": "元首", "pinyin": "yuánshǒu", "gloss_en": "head of state; sovereign"},
                {"character": "公历", "pinyin": "gōnglì", "gloss_en": "solar / Gregorian calendar"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "公元 strictly refers to the international Common Era calendar standard used for numbering historical years.",
            "contrasts": [
                {"id": 1, "compared_word": "公元 vs. 纪元", "pinyin": "jìyuán", "analysis": "纪元 refers broadly to an epoch or transformative historical period, whereas 公元 specifically denotes the Common Era calendar."},
                {"id": 2, "compared_word": "公元 vs. 公历", "pinyin": "gōnglì", "analysis": "公历 refers to the solar Gregorian calendar mechanism itself, while 公元 specifies year counting along that timeline."},
                {"id": 3, "compared_word": "公元 vs. 年代", "pinyin": "niándài", "analysis": "年代 refers to decades or historic epochs (e.g., the 80s), whereas 公元 is the base coordinate benchmark."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "公元前260年，秦赵两国在长平爆发了震动天下的战略决战。这场战役彻底摧毁了赵国的军事主力，为秦国最终实现天下一统奠定了决定性基础，成为公元前中国古代史上的重要分水岭。",
                "pinyin": "Gōngyuánqián 260 nián, Qín Zhào liǎng guó zài Chángpíng bàofā le zhèndòng tiānxià de zhànlüè juézhàn. Zhè chǎng zhànyì chèdǐ cuīhuǐ le Zhàoguó de jūnshì zhǔlì, wèi Qínguó zuìzhōng shíxiàn tiānxià yītǒng diàndìng le juédìngxìng jīchǔ, chéngwéi gōngyuánqián Zhōngguó gǔdài shǐ shang de zhòngyào fēnshuǐlǐng.",
                "en": "In 260 BC, Qin and Zhao waged an earth-shattering strategic showdown at Changping. This battle destroyed Zhao's main military forces, laying the foundation for Qin's eventual unification of China as a watershed in ancient history.",
                "es": "En el 260 a.C., los reinos de Qin y Zhao libraron un duelo decisivo en Changping. La batalla quebrantó el ejército de Zhao y cimentó la unificación imperial de Qin, marcando un hito en la historia china antes de nuestra era."
            },
            {
                "id": "#2",
                "hanzi": "在古代漫长的历史长河中，世界各文明均沿用各自独立的朝代纪年法则。进入近现代后，以公元为基准的通用纪年体系逐渐普及全球，极大便利了不同国家开展跨国商贸、学术交流与历史文献对照。",
                "pinyin": "Zài gǔdài màncháng de lìshǐ chánghé zhōng, shìjiè gè wénmíng jūn yányòng gèzì dúlì de cháodài jìnián fǎzé. Jìnrù jìnxiàndài hòu, yǐ gōngyuán wéi jīzhǔn de tōngyòng jìnián tǐxì zhújiàn pǔjí quánqiú, jídà biànlì le bùtóng guójiā kāizhǎn kuàguó shāngmào, xuéshù jiāoliú yǔ lìshǐ wénxiàn duìzhào.",
                "en": "Throughout ancient times, world civilizations kept independent dynastic calendars. In modern times, the Common Era chronological framework spread globally, facilitating cross-border trade, scholarship, and historical comparison.",
                "es": "Durante siglos las distintas civilizaciones emplearon cómputos dinásticos independientes. En la era moderna, el cómputo de la era común se consolidó universalmente, favoreciendo el comercio exterior, la ciencia y el cotejo histórico."
            }
        ]
    },

    # 33 盲目
    {
        "id": "33",
        "hanzi": "盲目",
        "pinyin": "máng mù",
        "part_of_speech": "Adjective/Adverb",
        "meanings_summary": {
            "en": "blind; blindly; lacking foresight or objective analysis",
            "es": "ciego; ciegamente; sin criterio objetivo; precipitado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "acting without clear perception, proper understanding, or rational planning",
                "definition_es": "que carece de discernimiento claro, base racional o criterio objetivo",
                "example_phrase": "盲目出击 (launch a blind assault)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括接任主帅后盲目自信，既不侦察敌情也不熟悉战地形势，便仓促下令全线出击。",
                "pinyin": "Zhào Kuò jiērèn zhǔshuài hòu mángmù zìxìn, jì bù zhēnchá díqíng yě bù shúxī zhàndì xíngshì, biàn cāngcù xiàlìng quánxiàn chūjī.",
                "en": "After taking command, Zhao Kuo was blindly confident; without scouting enemy dispositions or understanding terrain, he rashly launched an all-out attack.",
                "es": "Al asumir el mando, Zhao Kuo confió ciegamente; sin explorar las líneas enemigas ni el terreno, ordenó un asalto frontal a la carrera."
            },
            {
                "id": "#2",
                "hanzi": "投资理财应当立足于严密的数据分析与风险评估，盲目跟风炒作往往会带来惨痛亏损。",
                "pinyin": "Tóuzī lǐcái yīngdāng lìzú yú yánmì de shùjù fēnxī yǔ fēngxiǎn pínggū, mángmù gēnfēng chǎozuò wǎngwǎng huì dàilái cǎntòng kuīsǔn.",
                "en": "Investing must be grounded in rigorous data analysis and risk appraisal; blindly jumping on speculative bandwagons often brings grievous losses.",
                "es": "Las inversiones deben fundamentarse en análisis de datos y cálculo de riesgos; seguir las modas a ciegas suele acarrear pérdidas devastadoras."
            }
        ],
        "collocations": [
            {"hanzi": "盲目跟风", "en": "blindly follow the crowd / bandwagon"},
            {"hanzi": "盲目自信", "en": "blind overconfidence"},
            {"hanzi": "盲目乐观", "en": "blindly optimistic"},
            {"hanzi": "盲目冲动", "en": "blind impulse"},
            {"hanzi": "盲目行动", "en": "act blindly"},
            {"hanzi": "盲目崇拜", "en": "blind worship / idolatry"}
        ],
        "idioms": [
            {"hanzi": "盲人摸象", "pinyin": "máng rén mō xiàng", "meaning_en": "blind people feeling an elephant; mistake the part for the whole"},
            {"hanzi": "盲人瞎马", "pinyin": "máng rén xiā mǎ", "meaning_en": "a blind person on a blind horse; rushing blindly into imminent catastrophe"},
            {"hanzi": "有目共睹", "pinyin": "yǒu mù gòng dǔ", "meaning_en": "obvious to all with eyes; undeniable fact witnessed by everyone"},
            {"hanzi": "掩耳盗铃", "pinyin": "yǎn ěr dào líng", "meaning_en": "cover one's ears while stealing a bell; self-deceit"}
        ],
        "character_decomposition": [
            {
                "character": "盲",
                "pinyin": "máng",
                "meaning_en": "blind; visually impaired; unseeing",
                "meaning_es": "ciego; invidente; sin visión",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "目 (eye / vision) + 亡 (perish / lose)",
                "sound_component": "亡 (wáng)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Eyes 目 destroyed or extinguished 亡; signifies loss of sight or blindness.",
                "visual_mnemonic_story_en": "Loss (亡) of sight in the eye (目) renders one blind (盲).",
                "visual_mnemonic_story_es": "La pérdida (亡) de visión en el ojo (目) deja a la persona ciega (盲).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YVBU",
                "traditional": "盲"
            },
            {
                "character": "目",
                "pinyin": "mù",
                "meaning_en": "eye; gaze; look; item; category",
                "meaning_es": "ojo; mirada; ver; renglón; partida",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "Pictograph of an eye with iris and pupils",
                "sound_component": "目 (mù)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A realistic pictograph of an open human eye showing the eyeball and pupil.",
                "visual_mnemonic_story_en": "An open eye (目) looking attentively at everything.",
                "visual_mnemonic_story_es": "Un ojo abierto (目) observando con fijeza el entorno.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "BU",
                "traditional": "目"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When the eyes (目) lose sight (盲), one acts blindly (盲目) without seeing reality.",
            "composite_memory_hook_es": "Cuando los ojos (目) pierden la visión (盲), se actúa a ciegas (盲目) sin comprender la realidad.",
            "cultural_and_cognitive_roots": "Extends the physical inability to see to figurative intellectual and strategic blindness.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'máng mù' (35-51). Rising tone followed by decisive falling tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "育", "pinyin": "yù", "meaning_en": "educate; nurture", "distinction_note": "Radical 月 at bottom instead of 目"},
                {"character": "忘", "pinyin": "wàng", "meaning_en": "forget", "distinction_note": "Heart 心 at bottom instead of 目"},
                {"character": "日", "pinyin": "rì", "meaning_en": "sun; day", "distinction_note": "One horizontal bar inside instead of two"},
                {"character": "自", "pinyin": "zì", "meaning_en": "self", "distinction_note": "Extra tick stroke on top"}
            ],
            "etymological_cognates": [
                {"character": "盲区", "pinyin": "mángqū", "gloss_en": "blind spot"},
                {"character": "色盲", "pinyin": "sèmáng", "gloss_en": "color blindness"},
                {"character": "文盲", "pinyin": "wénmáng", "gloss_en": "illiterate"},
                {"character": "注目", "pinyin": "zhùmù", "gloss_en": "gaze upon; fix attention"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "盲目 highlights acting without rational foresight, factual evidence, or objective analysis.",
            "contrasts": [
                {"id": 1, "compared_word": "盲目 vs. 冲动", "pinyin": "chōngdòng", "analysis": "冲动 indicates emotional turbulence causing impulsive actions, while 盲目 denotes lack of cognitive basis or clear direction."},
                {"id": 2, "compared_word": "盲目 vs. 草率", "pinyin": "cǎoshuài", "analysis": "草率 stresses careless and rushed execution, whereas 盲目 stresses fundamental ignorance of circumstances."},
                {"id": 3, "compared_word": "盲目 vs. 随便", "pinyin": "suíbiàn", "analysis": "随便 conveys informality or casual unconcern, while 盲目 carries severe consequences."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "孙子兵法云：“不知彼而知己，一胜一负；不知彼不知己，每战必殆。”赵括轻视对手、盲目出兵，既未探清秦军主力虚实，也未明察山川险隘，结果正中白起埋伏，使赵国陷入万劫不复的深渊。",
                "pinyin": "Sūnzǐ bīngfǎ yún: 'Bù zhī bǐ ér zhī jǐ, yí shèng yí fù; bù zhī bǐ bù zhī jǐ, měi zhàn bì dài.' Zhào Kuò qīngshì duìshǒu, mángmù chūbīng, jì wèi tànqīng Qín jūn zhǔlì xūshí, yě wèi míngchá shānchuān xiǎn'ài, jiéguǒ zhèngzhòng Bái Qǐ máifu, shǐ Zhàoguó xiànrù wànjiébùfù de shēnyuān.",
                "en": "The Art of War states: 'Ignorant of the enemy but knowing yourself, victory is equal to defeat; ignorant of both, peril follows every clash.' Zhao Kuo marched out blindly, falling right into Bai Qi's ambush and ruining the state of Zhao.",
                "es": "El Arte de la Guerra dicta: 'Quien ignora al enemigo y a sí mismo sucumbe en cada lance.' Zhao Kuo avanzó a ciegas, cayendo en la celada de Bai Qi y arrojando a su reino al abismo de la aniquilación."
            },
            {
                "id": "#2",
                "hanzi": "在当今海量信息交织的数字化时代，盲目跟风已成为大众心理的普遍隐患。无论是舆论场上的断章取义，还是资本市场的狂热泡沫，唯有保持独立严谨的批判精神，方能在喧嚣迷雾中守住理性底线。",
                "pinyin": "Zài dāngjīn hǎiliàng xìnxī jiāozhī de shùzìhuà shídài, mángmù gēnfēng yǐ chéngwéi dàzhòng xīnlǐ de pǔbiàn yǐnhuàn. Wúlùn shì yúlùnchǎng shang de duànzhāng-qǔyì, háishì zībǐn shìchǎng de kuángrè pàomò, wéiyǒu bǎochí dúlì yánjǐn de pīpàn jīngshén, fāng néng zài xuānxiāo míwù zhōng shǒuzhù lǐxìng dǐxiàn.",
                "en": "In today's digital era flooded with information, blind conformism is a widespread psychological trap. Whether in polarizing public discourse or asset bubbles, maintaining independent critical thinking is vital to preserving rationality.",
                "es": "En la era digital saturada de información, seguir la corriente a ciegas es un riesgo frecuente. Ya sea ante bulos o burbujas financieras, preservar el pensamiento crítico permite mantener la sensatez en medio del ruido."
            }
        ]
    },

    # 34 轻视
    {
        "id": "34",
        "hanzi": "轻视",
        "pinyin": "qīng shì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to look down upon; underestimate; belittle; slight",
            "es": "menospreciar; subestimar; desestimar; desdeñar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to treat someone or something with condescension, insufficient seriousness, or disdain",
                "definition_es": "tratar a alguien o algo con desdén, falta de seriedad o subestimación",
                "example_phrase": "轻视对手 (underestimate the opponent)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括自夸天下用兵莫能当，公然轻视身经百战的廉颇老将，结果在长平决战中酿成滔天大祸。",
                "pinyin": "Zhào Kuò zìkuā tiānxià yòngbīng mò néng dāng, gōngrán qīngshì shēnjīng-bǎizhàn de Lián Pō lǎojiàng, jiéguǒ zài Chángpíng juézhàn zhōng niàngchéng tāotiān dàhuò.",
                "en": "Zhao Kuo boasted none could match his military skills and openly belittled the veteran general Lian Po, causing a monumental catastrophe at Changping.",
                "es": "Zhao Kuo presumía de ser inigualable en la guerra y menospreció al veterano Lian Po, desatando una catástrofe sin igual en Changping."
            },
            {
                "id": "#2",
                "hanzi": "在激烈的市场竞争中，任何成熟企业都绝不能轻视初创小微企业的创新活力与颠覆潜力。",
                "pinyin": "Zài jīliè de shìchǎng jìngzhēng zhōng, rènhé chéngshú qǐyè dōu jué bù néng qīngshì chūchuàng xiǎowēi qǐyè de chuàngxīn huólì yǔ diānfù qiánlì.",
                "en": "In fierce market rivalry, no established firm must ever underestimate the innovative vigor and disruptive potential of emerging startups.",
                "es": "En la encarnizada competencia mercantil, ninguna gran empresa debe desestimar el dinamismo innovador de las empresas emergentes."
            }
        ],
        "collocations": [
            {"hanzi": "轻视对手", "en": "underestimate an opponent"},
            {"hanzi": "轻视困难", "en": "make light of difficulties"},
            {"hanzi": "受到轻视", "en": "be slighted / looked down upon"},
            {"hanzi": "不容轻视", "en": "cannot be taken lightly"},
            {"hanzi": "轻视经验", "en": "belittle practical experience"},
            {"hanzi": "轻视细节", "en": "overlook minor details"}
        ],
        "idioms": [
            {"hanzi": "骄兵必败", "pinyin": "jiāo bīng bì bài", "meaning_en": "an arrogant army is bound to suffer defeat"},
            {"hanzi": "不可小觑", "pinyin": "bù kě xiǎo qù", "meaning_en": "not to be underestimated or taken lightly"},
            {"hanzi": "等闲视之", "pinyin": "děng xián shì zhī", "meaning_en": "treat as ordinary and of no significance; dismiss lightly"},
            {"hanzi": "自视甚高", "pinyin": "zì shì shèn gāo", "meaning_en": "think very highly of oneself; pretentious"}
        ],
        "character_decomposition": [
            {
                "character": "轻",
                "pinyin": "qīng",
                "meaning_en": "light; slight; gentle; frivolous",
                "meaning_es": "ligero; leve; suave; frívolo",
                "radical": "车",
                "radical_meaning_en": "cart / chariot",
                "meaning_component": "车 (war chariot / weight) + 𢀖 (weaving shuttle flying swiftly)",
                "sound_component": "𢀖 (qīng)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A light vehicle 车 darting effortlessly like a weaver's shuttle 𢀖; signifies light weight and lack of seriousness.",
                "visual_mnemonic_story_en": "A light wagon (车) gliding along swiftly without heavy burden (轻).",
                "visual_mnemonic_story_es": "Un carromato ligero (车) que avanza con soltura sin peso excesivo (轻).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "KQNOM",
                "traditional": "輕"
            },
            {
                "character": "视",
                "pinyin": "shì",
                "meaning_en": "look; gaze; inspect; regard",
                "meaning_es": "mirar; observar; inspeccionar; considerar",
                "radical": "礻",
                "radical_meaning_en": "spirit / display",
                "meaning_component": "礻/示 (reveal / examine) + 见 (see / behold)",
                "sound_component": "示 (shì)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "To fix one's eyes 见 upon an altar 礻 to observe closely; denotes inspecting, seeing, and regarding.",
                "visual_mnemonic_story_en": "Observing (见) signs shown before the altar (礻) to judge their importance (视).",
                "visual_mnemonic_story_es": "Mirar con atención (见) las señales sagradas (礻) para valorar su alcance (视).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IFHU",
                "traditional": "視"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Viewing (视) someone as weighing nothing (轻) means underestimating or belittling them (轻视).",
            "composite_memory_hook_es": "Mirar (视) a alguien como si no tuviera peso alguno (轻) equivale a menospreciarlo (轻视).",
            "cultural_and_cognitive_roots": "Derives from contrasting weight (heavy vs. light), where 'heavy' equals respect and 'light' equals contempt.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'qīng shì' (55-51). High level pitch dropping sharply on 'shì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "经", "pinyin": "jīng", "meaning_en": "pass through; scripture", "distinction_note": "Radical 纟 on left instead of cart 车"},
                {"character": "轮", "pinyin": "lún", "meaning_en": "wheel", "distinction_note": "Right side 仑 instead of 𢀖"},
                {"character": "规", "pinyin": "guī", "meaning_en": "rule; regulate", "distinction_note": "Left side 夫 instead of 礻"},
                {"character": "现", "pinyin": "xiàn", "meaning_en": "appear; present", "distinction_note": "Jade 王 on left instead of 礻"}
            ],
            "etymological_cognates": [
                {"character": "轻蔑", "pinyin": "qīngmiè", "gloss_en": "scornful; contemptuous"},
                {"character": "轻浮", "pinyin": "qīngfú", "gloss_en": "frivolous; flippant"},
                {"character": "藐视", "pinyin": "miǎoshì", "gloss_en": "disdain; look down upon"},
                {"character": "重视", "pinyin": "zhòngshì", "gloss_en": "attach importance to; value"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "轻视 refers to undervaluing, taking lightly, or condescending toward an opponent, duty, or risk.",
            "contrasts": [
                {"id": 1, "compared_word": "轻视 vs. 蔑视", "pinyin": "mièshì", "analysis": "蔑视 carries visceral moral disdain or scorn, whereas 轻视 primarily means underestimating strength or importance."},
                {"id": 2, "compared_word": "轻视 vs. 忽视", "pinyin": "hūshì", "analysis": "忽视 means overlooking unintentionally due to negligence, while 轻视 involves conscious underestimation."},
                {"id": 3, "compared_word": "轻视 vs. 歧视", "pinyin": "qíshì", "analysis": "歧视 denotes unfair prejudice against a demographic group, whereas 轻视 applies to specific opponents or tasks."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古兵法有言：“轻敌者必受制于人。”赵括熟读兵法典籍，自以为通晓天下战阵，因而极度轻视廉颇的固守策略与秦军将领的智谋。正是这种对强敌的轻视与狂傲，最终让他付出了全军覆没的惨烈代价。",
                "pinyin": "Gǔ bīngfǎ yǒu yán: 'Qīngdí zhě bì shòuzhì yú rén.' Zhào Kuò shúdú bīngfǎ diǎnjí, zìyǐwéi tōngxiǎo tiānxià zhànzhèn, yīn'ér jídù qīngshì Lián Pō de gùshǒu cèlüè yǔ Qín jūn jiànglǐng de zhìmóu. Zhèng shì zhè zhǒng duì qiángdí de qīngshì yǔ kuáng'ào, zuìzhōng ràng tā fùchū le quánjūn fùmò de cǎnliè dàijià.",
                "en": "Ancient military wisdom says: 'He who slights the enemy will be subdued by him.' Zhao Kuo believed he knew all warfare, belittling Lian Po's defense and Qin's cunning. This arrogance and underestimation of his foe cost him the annihilation of his army.",
                "es": "La doctrina militar antigua dictaba: 'Quien subestima al rival termina sometido.' Zhao Kuo creía saberlo todo y desdeñó la prudente defensa de Lian Po y el ingenio de Qin. Esa arrogancia le costó la total destrucción de sus tropas."
            },
            {
                "id": "#2",
                "hanzi": "无论个人修养还是事业发展，都切忌轻视微小的积累与潜在的危险。千里之堤溃于蚁穴，很多看似无足轻重的隐患，往往因为受到人们的长期轻视而演变为难以挽回的灾难。保持谦逊谨慎，方为成事之道。",
                "pinyin": "Wúlùn gèrén xiūyǎng háishì shìyè fāzhǎn, dōu qièjì qīngshì wēixiǎo de jīlěi yǔ qiánzài de wēixiǎn. Qiānlǐ zhī dī kuì yú yǐxué, hěnduō kànsì wúzúqīngzhòng de yǐnhuàn, wǎngwǎng yīnwèi shòudào rénmen de chángqī qīngshì ér yǎnbiàn wéi nányǐ wǎnhuí de zāinàn. Bǎochí qiānxùn jǐnshèn, fāng wéi chéngshì zhī dào.",
                "en": "Whether in self-cultivation or career, never underestimate tiny habits or hidden hazards. A dike collapses from an ant hole; small risks become irreversible disasters when slighted. Humility and vigilance remain the keys to success.",
                "es": "En la superación personal y los negocios, jamás se deben menospreciar los pequeños detalles ni los peligros latentes. Grietas ignoradas destruyen diques; la humildad constante es el verdadero camino hacia el logro."
            }
        ]
    },

    # 35 方案
    {
        "id": "35",
        "hanzi": "方案",
        "pinyin": "fāng àn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "scheme; plan; program; proposal",
            "es": "plan; proyecto; esquema; propuesta de solución"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a systematically formulated program, method, or proposal designed to accomplish a specific objective",
                "definition_es": "programa, método o propuesta sistemática diseñada para resolver un problema o alcanzar un objetivo",
                "example_phrase": "制定作战方案 (formulate an operational battle plan)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "秦军将领白起在战前周密勘察长平地形，精心制定了诱敌深入与分割包围的作战方案。",
                "pinyin": "Qín jūn jiànglǐng Bái Qǐ zài zhànqián zhōumì kānchá Chángpíng dìxíng, jīngxīn zhìdìng le yòudí shēnrù yǔ fēn’gē bāowéi de zuòzhàn fāng'àn.",
                "en": "Before the clash, Qin general Bai Qi meticulously scouted the terrain of Changping and formulated an operational plan to lure the enemy deep and encircle them.",
                "es": "Antes de la batalla, el general Bai Qi de Qin reconoció minuciosamente el terreno y diseñó un plan de operaciones para atraer al enemigo y cercarlo."
            },
            {
                "id": "#2",
                "hanzi": "工程师团队夜以继日地攻克技术难关，最终拿出了一套兼顾施工安全与成本控制的改造方案。",
                "pinyin": "Gōngchéngshī tuánduì yèyǐjìrì de gōngkè jìshù nánguān, zuìzhōng náchū le yí tào jiāngù shīgōng ānquán yǔ chéngběn kòngzhì de gǎizào fāng'àn.",
                "en": "The engineering team worked around the clock on technical hurdles and delivered a renovation proposal balancing safety and budget.",
                "es": "El equipo de ingenieros resolvió día y noche las dificultades técnicas y presentó una propuesta de remodelación que equilibra seguridad y costes."
            }
        ],
        "collocations": [
            {"hanzi": "制定方案", "en": "formulate a plan / proposal"},
            {"hanzi": "实施方案", "en": "implement a plan"},
            {"hanzi": "替代方案", "en": "alternative proposal / plan B"},
            {"hanzi": "优化方案", "en": "optimize a proposal"},
            {"hanzi": "解决方案", "en": "solution scheme"},
            {"hanzi": "设计方案", "en": "design proposal"}
        ],
        "idioms": [
            {"hanzi": "谋定后动", "pinyin": "móu dìng hòu dòng", "meaning_en": "plan thoroughly before taking action"},
            {"hanzi": "运筹帷幄", "pinyin": "yùn chóu wéi wò", "meaning_en": "devise strategies in the command tent; masterminding operations"},
            {"hanzi": "足智多谋", "pinyin": "zú zhì duō móu", "meaning_en": "wise and full of stratagems; resourceful"},
            {"hanzi": "深思熟虑", "pinyin": "shēn sī shú lǜ", "meaning_en": "mature and deep consideration; carefully weighed"}
        ],
        "character_decomposition": [
            {
                "character": "方",
                "pinyin": "fāng",
                "meaning_en": "square; direction; side; method; prescription",
                "meaning_es": "cuadrado; dirección; lado; método; fórmula",
                "radical": "方",
                "radical_meaning_en": "square / direction",
                "meaning_component": "Pictograph of two boats lashed together moving forward or a carpenter's square",
                "sound_component": "方 (fāng)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Denotes standard rectangular orientation, orderly directions, and systematic formulas or recipes.",
                "visual_mnemonic_story_en": "A carpenter's square measuring directions and prescribing orderly formulas (方).",
                "visual_mnemonic_story_es": "Una escuadra de carpintero que mide rumbos y pauta fórmulas exactas (方).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YHS",
                "traditional": "方"
            },
            {
                "character": "案",
                "pinyin": "àn",
                "meaning_en": "desk; table; record; legal case; proposal",
                "meaning_es": "mesa; pupitre; expediente; caso; propuesta",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden desk / table) + 安 (peaceful / rest)",
                "sound_component": "安 (ān)",
                "stroke_count": 10,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A wooden table 木 upon which documents rest peacefully 安 for judicial review or formal planning.",
                "visual_mnemonic_story_en": "Official documents laid securely (安) on the magistrate's wooden desk (木) for scrutiny (案).",
                "visual_mnemonic_story_es": "Documentos oficiales descansando en calma (安) sobre el escritorio de madera (木) para su estudio (案).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "JVD",
                "traditional": "案"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A structured method (方) drafted on the wooden desk (案) forms an operational proposal (方案).",
            "composite_memory_hook_es": "El método riguroso (方) redactado sobre el pupitre (案) da origen al plan de acción (方案).",
            "cultural_and_cognitive_roots": "Originates from ancient statecraft dockets and strategies drafted on ministerial desks.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'fāng àn' (55-51). High level pitch followed by falling pitch with clear apostrophe syllable break."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "按", "pinyin": "àn", "meaning_en": "press; according to", "distinction_note": "Hand 扌 on left of 安 instead of 木 below"},
                {"character": "安", "pinyin": "ān", "meaning_en": "peaceful; safe", "distinction_note": "No wood 木 radical below"},
                {"character": "芳", "pinyin": "fāng", "meaning_en": "fragrant", "distinction_note": "Grass 艹 radical on top of 方"},
                {"character": "仿", "pinyin": "fǎng", "meaning_en": "imitate", "distinction_note": "Person 亻 on left of 方"}
            ],
            "etymological_cognates": [
                {"character": "档案", "pinyin": "dàng'àn", "gloss_en": "archives; official files"},
                {"character": "草案", "pinyin": "cǎo'àn", "gloss_en": "draft proposal"},
                {"character": "破案", "pinyin": "pò'àn", "gloss_en": "solve or crack a criminal case"},
                {"character": "方法", "pinyin": "fāngfǎ", "gloss_en": "method; manner"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "方案 denotes a comprehensive, systematic, and concrete blueprint tailored to solve an explicit problem.",
            "contrasts": [
                {"id": 1, "compared_word": "方案 vs. 计划", "pinyin": "jìhuà", "analysis": "计划 is broader, emphasizing timeline and agenda, whereas 方案 emphasizes actionable methodology and concrete design."},
                {"id": 2, "compared_word": "方案 vs. 策略", "pinyin": "cèlüè", "analysis": "策略 emphasizes high-level tactical maneuvers, whereas 方案 is the complete operational document."},
                {"id": 3, "compared_word": "方案 vs. 政策", "pinyin": "zhèngcè", "analysis": "政策 indicates overarching government or corporate guidelines, while 方案 is execution-level design."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在古代重大战事中，作战方案的优劣直接决定三军将士的生死存亡。秦国名将白起针对赵括急躁冒进的性格弱点，精心设计了诱敌入伏的作战方案，最终成功斩断赵军后路，一举取得了长平之战的彻底胜利。",
                "pinyin": "Zài gǔdài zhòngdà zhànshì zhōng, zuòzhàn fāng'àn de yōuliè zhíjiē juédìng sānjūn jiàngshì de shēngsǐ-cúnwáng. Qínguó míngjiàng Bái Qǐ zhēnduì Zhào Kuò jízào-màojìn de xìnggé ruòdiǎn, jīngxīn shèjì le yòudí-rùfú de zuòzhàn fāng'àn, zuìzhōng chénggōng zhǎnduàn Zhào jūn hòulù, yìjǔ qǔdé le Chángpíng zhī zhàn de chèdǐ shènglì.",
                "en": "In ancient warfare, the quality of operational plans determined survival. Qin general Bai Qi exploited Zhao Kuo's rashness, formulating a trap plan that cut Zhao's retreat and delivered total victory at Changping.",
                "es": "En la guerra antigua, la calidad de los planes decidía la vida o la muerte. Bai Qi se aprovechó de la temeridad de Zhao Kuo y diseñó un plan de emboscada que cortó la retirada enemiga, alcanzando la victoria total en Changping."
            },
            {
                "id": "#2",
                "hanzi": "现代企业在启动任何重大项目之前，都必须经历多轮严密的可行性方案论证。一套优秀的方案不仅要有开阔前瞻的战略构想，更要具备严谨细致的操作步骤和风险应急预案，从而确保各项业务平稳有序落地。",
                "pinyin": "Xiàndài qǐyè zài qǐdòng rènhé zhòngdà xiàngmù zhīqián, dōu bìxū jīnglì duō lún yánmì de kěxíngxìng fāng'àn lùnzhèng. Yí tào yōuxiù de fāng'àn bùjǐn yào yǒu kāikuò qiánzhān de zhànlüè gòuxiǎng, gèng yào jùbèi yánjǐn xìzhì de cāozuò bùzhòu yǔ fēngxiǎn yīngjí yù'àn, cóng'ér quèbǎo gè xiàng yèwù píngwěn yǒuxù luòdì.",
                "en": "Before launching projects, modern enterprises must vet feasibility schemes through rigorous evaluations. An outstanding proposal combines strategic foresight with concrete operational steps and risk contingencies.",
                "es": "Antes de iniciar proyectos, las empresas modernas someten sus propuestas a rigurosos estudios de viabilidad. Un buen plan aúna visión estratégica con pasos minuciosos y contingencias de riesgo para garantizar su éxito."
            }
        ]
    },

    # 36 进攻
    {
        "id": "36",
        "hanzi": "进攻",
        "pinyin": "jìn gōng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to attack; assault; go on the offensive",
            "es": "atacar; asaltar; pasar a la ofensiva; embestir"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to take offensive armed action or tactical advance against an enemy, opposing line, or objective",
                "definition_es": "iniciar acciones de ataque o avance ofensivo contra el enemigo, su frente o una posición",
                "example_phrase": "发起猛烈进攻 (launch a ferocious offensive)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括轻率改变廉颇坚守阵地的既定战略，贸然下令数十万赵军向秦军阵地发动全面进攻。",
                "pinyin": "Zhào Kuò qīngshuài gǎibiàn Lián Pō jiānshǒu zhèndì de jìdìng zhànlüè, màorán xiàlìng shùshí wàn Zhào jūn xiàng Qín jūn zhèndì fādòng quánmiàn jìngōng.",
                "en": "Zhao Kuo rashly altered Lian Po's established defensive strategy and commanded hundreds of thousands of Zhao troops to launch a total offensive against Qin positions.",
                "es": "Zhao Kuo alteró temerariamente la estrategia defensiva de Lian Po y ordenó a miles de soldados de Zhao lanzar una ofensiva frontal contra Qin."
            },
            {
                "id": "#2",
                "hanzi": "在决赛最后阶段，处于劣势的球队全力组织进攻，终于在伤停补时阶段打进了扳平比分的关键一球。",
                "pinyin": "Zài juésài zuìhòu jiēduàn, chǔyú lièshì de qiúduì quánlì zǔzhī jìngōng, zhōngyú zài shāngtíng-bǔshí jiēduàn dǎjìn le bānpíng bǐfēn de guānjiàn yì qiú.",
                "en": "In the final stage of the match, the trailing squad mobilized all-out attacks and scored a crucial equalizer during stoppage time.",
                "es": "En el tramo final del partido, el equipo en desventaja organizó un ataque total y marcó el gol del empate en el tiempo añadido."
            }
        ],
        "collocations": [
            {"hanzi": "发起进攻", "en": "launch an attack / offensive"},
            {"hanzi": "全面进攻", "en": "general / all-out offensive"},
            {"hanzi": "猛烈进攻", "en": "fierce assault"},
            {"hanzi": "组织进攻", "en": "organize an offensive"},
            {"hanzi": "抵御进攻", "en": "repel an offensive"},
            {"hanzi": "转入进攻", "en": "shift into offensive"}
        ],
        "idioms": [
            {"hanzi": "攻守兼备", "pinyin": "gōng shǒu jiān bèi", "meaning_en": "equally adept at both offense and defense"},
            {"hanzi": "攻其不备", "pinyin": "gōng qí bù bèi", "meaning_en": "attack where the enemy is least prepared; take by surprise"},
            {"hanzi": "反戈一击", "pinyin": "fǎn gē yī jī", "meaning_en": "turn one's weapon around to strike back; counterattack"},
            {"hanzi": "无懈可击", "pinyin": "wú xiè kě jī", "meaning_en": "leaving no flaw or loophole for attack; invulnerable"}
        ],
        "character_decomposition": [
            {
                "character": "进",
                "pinyin": "jìn",
                "meaning_en": "advance; enter; move forward; progress",
                "meaning_es": "avanzar; entrar; progresar; marchar hacia adelante",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (walk / movement forward) + 井 (neat well boundary)",
                "sound_component": "井 (jǐng)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Moving forward 辶 with steady marching pace; signifies advancing into position.",
                "visual_mnemonic_story_en": "Marching forward steadily along the pathway (辶) to make progress (进).",
                "visual_mnemonic_story_es": "Marchar con firmeza a lo largo del camino (辶) para abrir paso hacia adelante (进).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YTT",
                "traditional": "進"
            },
            {
                "character": "攻",
                "pinyin": "gōng",
                "meaning_en": "attack; assault; strike; study diligently",
                "meaning_es": "atacar; asaltar; golpear; dedicarse a fondo",
                "radical": "攵",
                "radical_meaning_en": "strike / tap",
                "meaning_component": "工 (carpenter's tool / labor) + 攵/攴 (hand holding a striking weapon)",
                "sound_component": "工 (gōng)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Holding a tool or weapon 攵 to pound and break enemy barriers 工; signifies attack and assault.",
                "visual_mnemonic_story_en": "Wielding a striking weapon (攵) with focused force (工) to breach enemy walls (攻).",
                "visual_mnemonic_story_es": "Empuñar un arma (攵) con ímpetu laborioso (工) para derribar las murallas rivales (攻).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "MOK",
                "traditional": "攻"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Advancing forward (进) and striking with weapons (攻) forms a decisive offensive assault (进攻).",
            "composite_memory_hook_es": "Avanzar con presteza (进) y asestar golpes (攻) conforma una ofensiva decidida (进攻).",
            "cultural_and_cognitive_roots": "Represents the dynamic movement and assault maneuvers in classical Chinese military treatises.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone to first tone: 'jìn gōng' (51-55). Sharp falling drop into sustained high tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "功", "pinyin": "gōng", "meaning_en": "merit; achievement", "distinction_note": "Radical 力 on right instead of strike 攵"},
                {"character": "巧", "pinyin": "qiǎo", "meaning_en": "skillful; clever", "distinction_note": "Radical 工 on left with 丂 on right"},
                {"character": "近", "pinyin": "jìn", "meaning_en": "near; close", "distinction_note": "Inside component is axe 斤 instead of 井"},
                {"character": "退", "pinyin": "tuì", "meaning_en": "retreat; withdraw", "distinction_note": "Antonym; 艮 inside radical 辶"}
            ],
            "etymological_cognates": [
                {"character": "攻击", "pinyin": "gōngjī", "gloss_en": "assault; attack verbally"},
                {"character": "攻克", "pinyin": "gōngkè", "gloss_en": "capture; overcome"},
                {"character": "主攻", "pinyin": "zhǔgōng", "gloss_en": "main offensive direction"},
                {"character": "进攻方", "pinyin": "jìngōngfāng", "gloss_en": "offensive side"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "进攻 specifically denotes dynamic tactical advancement and armed push toward an opponent or fortress.",
            "contrasts": [
                {"id": 1, "compared_word": "进攻 vs. 攻击", "pinyin": "gōngjī", "analysis": "攻击 can refer to physical attacks as well as verbal or cyber attacks, while 进攻 focuses on strategic military offensive pushes."},
                {"id": 2, "compared_word": "进攻 vs. 侵略", "pinyin": "qīnlüè", "analysis": "侵略 carries the explicit illicit sense of violating sovereign borders, unlike general military 进攻."},
                {"id": 3, "compared_word": "进攻 vs. 突击", "pinyin": "tūjī", "analysis": "突击 denotes a sudden, concentrated short-range raid, whereas 进攻 encompasses wide sustained campaigns."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平之战中，赵括自恃勇力，不听老将劝阻，盲目率军向秦军发动全线进攻。秦将白起故意伪装战败退却，引诱赵军长驱直入，随后派遣奇兵包抄后方，将进攻的赵军牢牢围困在崇山峻岭之间。",
                "pinyin": "Chángpíng zhī zhàn zhōng, Zhào Kuò zìshì-yǒnglì, bù tīng lǎojiàng quànzǔ, mángmù shuài jūn xiàng Qín jūn fādòng quánxiàn jìngōng. Qín jiàng Bái Qǐ gùyì wěizhuāng zhànbài tuìquè, yǐnyòu Zhào jūn chángqū-zhírù, suíhòu pàiqiǎn qíbīng bāochāo hòufāng, jiāng jìngōng de Zhào jūn láoláo wéikùn zài chóngshān-jùnlǐng zhījiān.",
                "en": "At Changping, relying on rash bravado, Zhao Kuo launched an all-out offensive against Qin. Bai Qi feigned retreat to lure Zhao deep, then dispatched cavalry to circle behind, encircling the attacking Zhao army in rugged mountains.",
                "es": "En Changping, cegado por la temeridad, Zhao Kuo atacó frontalmente a Qin. Bai Qi fingió retirarse para atraer al rival; luego envió tropas que envolvieron la retaguardia, cercando al ejército atacante en las montañas."
            },
            {
                "id": "#2",
                "hanzi": "体育竞技与军事战略有着异曲同工之妙。高水平的球队从不盲目发动无序进攻，而是通过严密的防守稳住阵脚，在耐心传导中寻觅对手防线的破绽，在关键时刻发起致命进攻，从而一举锁定胜局。",
                "pinyin": "Tǐyù jìngjì yǔ jūnshì zhànlüè yǒu zhe yìqǔ-tónggōng zhī miào. Gāo shuǐpíng de qiúduì cóng bù mángmù fādòng wúxù jìngōng, ér shì tōngguò yánmì de fángshǒu wěnzhù zhènjiǎo, zài nàixīn chuándǎo zhōng xúnmì duìshǒu fángxiàn de pòzhàn, zài guānjiàn shíkè fāqǐ zhìmìng jìngōng, cóng'ér yìjǔ suǒdìng shèngjú.",
                "en": "Sports competition shares deep parallels with military strategy. Elite teams never launch chaotic attacks; they stabilize defense, patiently seek openings in the opponent's lines, and strike decisively to seal victory.",
                "es": "El deporte y la táctica militar comparten principios comunes. Los equipos de élite nunca atacan sin orden; consolidan su defensa, esperan fisuras en el rival y asestan ataques letales que aseguran la victoria final."
            }
        ]
    },

    # 37 宝贵
    {
        "id": "37",
        "hanzi": "宝贵",
        "pinyin": "bǎo guì",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "precious; valuable; treasured",
            "es": "precioso; valioso; de gran valor; estimable"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "having great value, worth, or significance; extremely precious",
                "definition_es": "que tiene un gran valor, estima o utilidad trascendente; sumamente preciado",
                "example_phrase": "宝贵的经验 (precious experience)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老将廉颇在数十载沙场征战中积累了极其宝贵的实战经验，这些远非书本空谈所能比拟。",
                "pinyin": "Lǎojiàng Lián Pō zài shùshí zǎi shāchǎng zhēngzhàn zhōng jīlěi le jíqí bǎoguì de shízhàn jīngyàn, zhèxiē yuǎnfēi shūběn kōngtán suǒ néng bǐnǐ.",
                "en": "Veteran general Lian Po accumulated exceedingly precious combat experience over decades of campaigns, which empty book theories could never rival.",
                "es": "El veterano general Lian Po atesoró una valiosísima experiencia en décadas de combate, inalcanzable para la vana teoría de los libros."
            },
            {
                "id": "#2",
                "hanzi": "在快节奏的现代生活中，能够专心陪伴家人共享天伦之乐，是人生中最宝贵的幸福时刻。",
                "pinyin": "Zài kuài jiézòu de xiàndài shēnghuó zhōng, nénggòu zhuānxīn péibàn jiārén gòngxiǎng tiānlún zhī lè, shì rénshēng zhōng zuì bǎoguì de xìngfú shíkè.",
                "en": "In the fast pace of modern life, being able to focus on accompanying family and enjoying harmony is life's most precious happiness.",
                "es": "En la ajetreada vida moderna, poder dedicar tiempo a la familia y gozar de su afecto constituye el momento más valioso de la existencia."
            }
        ],
        "collocations": [
            {"hanzi": "宝贵经验", "en": "valuable / precious experience"},
            {"hanzi": "宝贵财富", "en": "precious wealth / asset"},
            {"hanzi": "宝贵时间", "en": "valuable time"},
            {"hanzi": "宝贵生命", "en": "precious life"},
            {"hanzi": "宝贵意见", "en": "valuable feedback / advice"},
            {"hanzi": "极为宝贵", "en": "extremely precious"}
        ],
        "idioms": [
            {"hanzi": "分秒必争", "pinyin": "fēn miǎo bì zhēng", "meaning_en": "seize every minute and second; race against time"},
            {"hanzi": "千金难买", "pinyin": "qiān jīn nán mǎi", "meaning_en": "priceless; cannot be bought even with a thousand gold coins"},
            {"hanzi": "寸阴可惜", "pinyin": "cùn yīn kě xī", "meaning_en": "every inch of time is precious and should not be squandered"},
            {"hanzi": "价值连城", "pinyin": "jià zhí lián chéng", "meaning_en": "worth several cities; invaluable treasure"}
        ],
        "character_decomposition": [
            {
                "character": "宝",
                "pinyin": "bǎo",
                "meaning_en": "treasure; precious; jewel; precious object",
                "meaning_es": "tesoro; precioso; joya; objeto valioso",
                "radical": "宀",
                "radical_meaning_en": "roof / house",
                "meaning_component": "宀 (house / treasury) + 玉 (radiant jade gem)",
                "sound_component": "缶 (archaic sound in traditional 寶)",
                "stroke_count": 8,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Precious jade stones 玉 treasured and safeguarded under the roof 宀 of the treasury; signifies jewel and treasure.",
                "visual_mnemonic_story_en": "Precious polished jade (玉) safeguarded safely under the roof (宀) as a treasure (宝).",
                "visual_mnemonic_story_es": "Una gema de jade (玉) custodiada bajo el tejado (宀) como un tesoro sagrado (宝).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "JMI",
                "traditional": "寶"
            },
            {
                "character": "贵",
                "pinyin": "guì",
                "meaning_en": "expensive; precious; noble; honor",
                "meaning_es": "caro; precioso; noble; honorable",
                "radical": "贝",
                "radical_meaning_en": "cowrie shell / currency",
                "meaning_component": "贝 (ancient shell currency) + 中/𠀎 (costly merchandise)",
                "sound_component": "臾/𠀎 (guì)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Goods backed by precious cowrie shell money 贝; denotes high value, nobility, and precious worth.",
                "visual_mnemonic_story_en": "Piles of rare shell money (贝) marking goods of highest noble value (贵).",
                "visual_mnemonic_story_es": "Montones de valiosas caracolas moneda (贝) que acreditan un alto valor y nobleza (贵).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LMBO",
                "traditional": "貴"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Treasures housed under the roof (宝) backed by costly wealth (贵) are exceedingly precious (宝贵).",
            "composite_memory_hook_es": "Las gemas del tesoro (宝) respaldadas por caudales valiosos (贵) son sumamente preciadas (宝贵).",
            "cultural_and_cognitive_roots": "Combines domestic treasury jade with cowrie money, expanding to spiritual, intellectual, and temporal value.",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'bǎo guì' (214-51). Half-third dip rising before sharp drop on 'guì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "实", "pinyin": "shí", "meaning_en": "solid; real; fruit", "distinction_note": "Head has 头 instead of jade 玉"},
                {"character": "定", "pinyin": "dìng", "meaning_en": "settle; fix", "distinction_note": "Radical 宀 with 正/疋 below"},
                {"character": "遗", "pinyin": "yí", "meaning_en": "lose; bequeath", "distinction_note": "Surrounded by walk radical 辶"},
                {"character": "资", "pinyin": "zī", "meaning_en": "resources; capital", "distinction_note": "Top component is 次 instead of 𠀎"}
            ],
            "etymological_cognates": [
                {"character": "珍贵", "pinyin": "zhēnguì", "gloss_en": "precious; invaluable"},
                {"character": "宝贝", "pinyin": "bǎobèi", "gloss_en": "cherished treasure; baby"},
                {"character": "宝藏", "pinyin": "bǎozàng", "gloss_en": "treasure trove"},
                {"character": "贵重", "pinyin": "guìzhòng", "gloss_en": "valuable; costly"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "宝贵 highlights immense intrinsic or non-material utility, wisdom, lessons, or time.",
            "contrasts": [
                {"id": 1, "compared_word": "宝贵 vs. 珍贵", "pinyin": "zhēnguì", "analysis": "珍贵 leans toward emotional affection and rare physical articles, while 宝贵 emphasizes intrinsic functional and intellectual value."},
                {"id": 2, "compared_word": "宝贵 vs. 昂贵", "pinyin": "ángguì", "analysis": "昂贵 refers strictly to high monetary price, whereas 宝贵 usually describes cherished non-material values."},
                {"id": 3, "compared_word": "宝贵 vs. 名贵", "pinyin": "míngguì", "analysis": "名贵 describes famous luxury specimens (e.g. rare herbs or stones), whereas 宝贵 has broad spiritual application."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在瞬息万变的生死战局中，老将廉颇凭借几十年浴血奋战摸索出的防御经验，是赵国赖以抵御强秦最宝贵的军事财富。赵王因谣言将其撤换，白白葬送了扭转乾坤的宝贵时机，铸成历史悲剧。",
                "pinyin": "Zài shùnxī-wànbiàn de shēngsǐ zhànjú zhōng, lǎojiàng Lián Pō píngjiè jǐshí nián yùxuè-fènzhàn mōsuǒ chū de fángyù jīngyàn, shì Zhàoguó làiyǐ dǐyù qiáng Qín zuì bǎoguì de jūnshì cáifù. Zhào wáng yīn yáoyán jiāng qí chèhuàn, báibái zàngsòng le niǔzhuǎn qiánkūn de bǎoguì shíjī, zhùchéng lìshǐ bēijù.",
                "en": "In life-and-death warfare, Lian Po's defensive experience forged over decades was Zhao's most precious asset against Qin. Swayed by rumors, King of Zhao replaced him, squandering a precious opportunity and causing historic tragedy.",
                "es": "En la guerra despiadada, la experiencia defensiva de Lian Po era el tesoro militar más preciado de Zhao frente al invasor. El rey de Zhao creyó los rumores y lo relevó, desperdiciando una valiosa ocasión y sellando la tragedia."
            },
            {
                "id": "#2",
                "hanzi": "光阴荏苒，日月如梭，时间是世间唯一无法逆转的宝贵资产。金钱耗尽尚有再度创造之机，青春年华一旦虚掷便永不复返。唯有懂得珍惜每一分宝贵光阴，脚踏实地钻研进取，方能铸就无悔的精彩人生。",
                "pinyin": "Guāngyīn-rěnrǎn, rìyuè-rúsuō, shíjiān shì shìjiān wéiyī wúfǎ nìzhuǎn de bǎoguì zīchǎn. Jīnqián hàojìn shàng yǒu zàidù chuàngzào zhī jī, qīngchūn niánhuá yídàn xūzhì biàn yǒng bù fùfǎn. Wéiyǒu dǒngdé zhēnxī měi yì fēn bǎoguì guāngyīn, jiǎotàshídì zuānyán jìnqǔ, fāng néng zhùjiù wúhuǐ de jīngcǎi rénshēng.",
                "en": "Time passes like a shuttle; it is the only non-renewable precious asset on earth. Lost money can be regained, but squandered youth never returns. Cherishing precious moments and striving forward creates a life without regrets.",
                "es": "El tiempo vuela sin freno y es el activo más valioso e irrecuperable de este mundo. El dinero gastado se puede volver a ganar, pero la juventud perdida no regresa jamás. Atesorar cada instante permite forjar una vida plena."
            }
        ]
    },

    # 38 讽刺
    {
        "id": "38",
        "hanzi": "讽刺",
        "pinyin": "fěng cì",
        "part_of_speech": "Verb/Noun",
        "meanings_summary": {
            "en": "to satirize; mock; sarcasm; irony",
            "es": "satirizar; burlarse de; ironía; sarcasmo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to criticize, ridicule, or mock through witty irony or caustic metaphor",
                "definition_es": "criticar, ridiculizar o censurar mediante ironía ingeniosa o metáfora mordaz",
                "example_phrase": "辛辣讽刺 (pungent satire)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "后世史学家常以“纸上谈兵”这一典故，深刻讽刺那些空谈高深理论而缺乏实践检验的夸夸其谈之辈。",
                "pinyin": "Hòushì shǐxuéjiā cháng yǐ 'zhǐshàng-tánbīng' zhè yí diǎngù, shēnkè fěngcì nàxiē kōngtán gāoshēn lǐlùn ér quēfá shíjiàn jiǎnyàn de kuākuā-qítán zhī bèi.",
                "en": "Later historians frequently cited the idiom 'armchair strategy' to sharply satirize those braggarts who preach lofty theories without practical testing.",
                "es": "Los historiadores posteriores utilizaron el modismo 'estrategia en el papel' para satirizar a quienes predican elevadas teorías sin haberlas puesto a prueba en la realidad."
            },
            {
                "id": "#2",
                "hanzi": "这部文学杰作运用了极其辛辣的幽默讽刺手法，无情揭示了当年封建官僚体制的虚伪与腐朽。",
                "pinyin": "Zhè bù wénxué jiézuò yùnyòng le jíqí xīnlà de yōumò fěngcì shǒufǎ, wúqíng jiēshì le dāngnián fēngjiàn guānliáo tǐzhì de xūwěi yǔ fǔxiǔ.",
                "en": "This literary masterpiece employed pungent humorous satire, ruthlessly exposing the hypocrisy and decay of the feudal bureaucratic system.",
                "es": "Esta obra maestra literaria empleó una sátira sumamente mordaz, desnudando sin piedad la hipocresía y corrupción de la burocracia feudal."
            }
        ],
        "collocations": [
            {"hanzi": "辛辣讽刺", "en": "pungent / biting satire"},
            {"hanzi": "充满讽刺", "en": "full of irony / satire"},
            {"hanzi": "讽刺小说", "en": "satirical novel"},
            {"hanzi": "讽刺意味", "en": "satirical undertone"},
            {"hanzi": "加以讽刺", "en": "subject to ridicule / satirize"},
            {"hanzi": "幽默讽刺", "en": "humorous irony"}
        ],
        "idioms": [
            {"hanzi": "冷嘲热讽", "pinyin": "lěng cháo rè fěng", "meaning_en": "scoffing and jeering; cynical mockery and burning satire"},
            {"hanzi": "指桑骂槐", "pinyin": "zhǐ sāng mà huái", "meaning_en": "point at the mulberry and scold the locust tree; criticize indirectly"},
            {"hanzi": "拐弯抹角", "pinyin": "guǎi wān mò jiǎo", "meaning_en": "speak in circumlocutions; beat around the bush"},
            {"hanzi": "尖酸刻薄", "pinyin": "jiān suān kè bó", "meaning_en": "sharp and biting; caustic and acerbic"}
        ],
        "character_decomposition": [
            {
                "character": "讽",
                "pinyin": "fěng",
                "meaning_en": "satirize; mock; chant; recite",
                "meaning_es": "satirizar; burlarse de; recitar; censurar",
                "radical": "讠",
                "radical_meaning_en": "speech / words",
                "meaning_component": "讠 (speech / words) + 风 (wind / indirect influence)",
                "sound_component": "风 (fēng)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 delivered indirectly like gentle wind 风 to critique flaws; denotes indirect satire.",
                "visual_mnemonic_story_en": "Delivering spoken words (讠) like a sharp gust of wind (风) to criticize obliquely (讽).",
                "visual_mnemonic_story_es": "Pronunciar palabras (讠) como una ráfaga de viento (风) que censura indirectamente (讽).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "IVHN",
                "traditional": "諷"
            },
            {
                "character": "刺",
                "pinyin": "cì",
                "meaning_en": "thorn; prick; pierce; sting; assassinate",
                "meaning_es": "espina; pinchar; punzar; picar; asesinar",
                "radical": "刂",
                "radical_meaning_en": "knife / blade",
                "meaning_component": "朿 (brambles / thorns) + 刂 (sharp knife blade)",
                "sound_component": "朿 (cì)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A thorny bramble 朿 combined with a sharp knife 刂; signifies pricking, stabbing, and stinging critique.",
                "visual_mnemonic_story_en": "A thorny plant (朿) with the sharpness of a knife (刂) that pricks and stings (刺).",
                "visual_mnemonic_story_es": "Una zarza espinosa (朿) tan punzante como una cuchilla (刂) que pincha y escuece (刺).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "DBLN",
                "traditional": "刺"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Words delivered obliquely like wind (讽) designed to prick like sharp thorns (刺) deliver biting satire (讽刺).",
            "composite_memory_hook_es": "Palabras que soplan como viento (讽) y pinchan como afiladas espinas (刺) crean la sátira (讽刺).",
            "cultural_and_cognitive_roots": "Rooted in classical poetic traditions (Feng) of remonstrating with emperors through subtle allegories.",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'fěng cì' (214-51). Half-third dip rising before falling sharply on 'cì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "风", "pinyin": "fēng", "meaning_en": "wind; custom", "distinction_note": "No speech 讠 radical on left"},
                {"character": "订", "pinyin": "dìng", "meaning_en": "book; subscribe", "distinction_note": "Right side is 丁 instead of 风"},
                {"character": "枣", "pinyin": "zǎo", "meaning_en": "jujube; date", "distinction_note": "Double 朿 without knife radical 刂"},
                {"character": "策", "pinyin": "cè", "meaning_en": "policy; strategy", "distinction_note": "Bamboo ⺮ radical on top"}
            ],
            "etymological_cognates": [
                {"character": "讥讽", "pinyin": "jīfěng", "gloss_en": "taunt; deride; mock"},
                {"character": "讽喻", "pinyin": "fěngyù", "gloss_en": "parable; moral allegory"},
                {"character": "刺耳", "pinyin": "cì'ěr", "gloss_en": "grating; harsh on the ears"},
                {"character": "刺激", "pinyin": "cìjī", "gloss_en": "stimulate; excite; provoke"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "讽刺 uses witty, ironic, or metaphoric critique to pierce and expose hypocrisy, vice, or incompetence.",
            "contrasts": [
                {"id": 1, "compared_word": "讽刺 vs. 嘲笑", "pinyin": "cháoxiào", "analysis": "嘲笑 denotes direct teasing or derisive laughter, whereas 讽刺 relies on artistic or literary irony with moral critique."},
                {"id": 2, "compared_word": "讽刺 vs. 批评", "pinyin": "pīpíng", "analysis": "批评 is straightforward evaluation pointing out shortcomings, whereas 讽刺 conveys disapproval through irony and sting."},
                {"id": 3, "compared_word": "讽刺 vs. 挖苦", "pinyin": "wāku", "analysis": "挖苦 refers to colloquial, petty barbs aimed at hurting someone's feelings, whereas 讽刺 often carries broader social critique."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "“纸上谈兵”作为流传两千余年的著名成语，不仅记录了长平之战的悲惨结局，更成为汉语中讽刺脱离实际、夸夸其谈的经典隐喻。这种鞭辟入里的历史讽刺，始终警醒着后人必须尊崇实践，切勿自欺欺人。",
                "pinyin": "'Zhǐshàng-tánbīng' zuòwéi liúchuán liǎng qiān yú nián de zhùmíng chéngyǔ, bùjǐn jìlù le Chángpíng zhī zhàn de bēicǎn jiéjú, gèng chéngwéi Hànyǔ zhōng fěngcì tuōlí shíjì, kuākuā-qítán de jīngdiǎn yǐnyù. Zhè zhǒng biānpì-rùlǐ de lìshǐ fěngcì, shǐzhōng jǐngxǐng zhe hòurén bìxū zūnchóng shíjiàn, qièwù zìqī-qīrén.",
                "en": "Passing down for two millennia, 'armchair strategy' not only chronicles Changping's tragedy but serves as Chinese's classic satire against impractical talkers. This piercing historical irony cautions us to honor practice and never deceive ourselves.",
                "es": "Con más de dos milenios de historia, 'estrategia en el papel' no solo narra la tragedia de Changping, sino que es la gran sátira china contra quienes teorizan sin base. Esta aguda ironía nos recuerda priorizar la práctica y evitar el autoengaño."
            },
            {
                "id": "#2",
                "hanzi": "讽刺艺术向来被誉为社会改良的有力思想武器。无论古代寓言还是现代先锋戏剧，创作者借助精妙的隐喻与讽刺笔触，能够以幽默的形式直击时代弊病，唤醒沉睡的大众心灵，促使全社会反思并不断革故鼎新。",
                "pinyin": "Fěngcì yìshù xiànglái bèi yù wéi shèhuì gǎiliáng de yǒulì sīxiǎng wǔqì. Wúlùn gǔdài yùyán háishì xiàndài xiānfēng xìjù, chuàngzuòzhě jièzhù jīngmiào de yǐnyù yǔ fěngcì bǐchù, nénggòu yǐ yōumò de xíngshì zhíjī shídài bìbìng, huànxǐng chénshuì de dàzhòng xīnlíng, cùshǐ quán shèhuì fǎnsī bìng bùduàn gégù-dǐngxīn.",
                "en": "The art of satire has long been hailed as an intellectual weapon for social reform. In fables or avant-garde drama, through witty metaphor and satire, artists critique social ills and awaken public conscience to inspire reform.",
                "es": "El arte satírico ha sido considerado un instrumento de mejora social. Tanto en fábulas como en el teatro contemporáneo, mediante metáforas ingeniosas los autores exponen las dolencias de su época para impulsar una constante renovación cívica."
            }
        ]
    },

    # 39 灵活
    {
        "id": "39",
        "hanzi": "灵活",
        "pinyin": "líng huó",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "flexible; agile; nimble; adaptable",
            "es": "flexible; ágil; adaptable; diestro; maniobrable"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "agile and adaptable; not rigid or bound by dogma; adjusting readily to changing situations",
                "definition_es": "ágil y adaptable; no rígido ni atado al dogma; capaz de adecuarse con rapidez a situaciones cambiantes",
                "example_phrase": "灵活机动 (agile and flexible maneuver)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "真正善于带兵的将领深谙兵无常势之理，绝不死搬兵书阵法，而是根据敌地形势灵活机动地调整部署。",
                "pinyin": "Zhēnzhèng shànyú dài bīng de jiànglǐng shēn'ān bīng wú cháng shì zhī lǐ, jué bù sǐ bān bīngshū zhènfǎ, ér shì gēnjù dídì xíngshì línghuó jīdòng de tiáozhěng bùshǔ.",
                "en": "Generals skilled in command understand warfare has no constant posture; never rigidly copying diagrams, they flexibly adjust troop deployments according to conditions.",
                "es": "Los generales hábiles saben que la guerra no tiene esquemas fijos; lejos de copiar manuales, adecuan sus posiciones con suma agilidad según el enemigo."
            },
            {
                "id": "#2",
                "hanzi": "在复杂的商务谈判中，既要坚定守护核心底线，也要根据对话氛围灵活变通具体的合作条款。",
                "pinyin": "Zài fùzá de shāngwù tánpàn zhōng, jì yào jiāndìng shǒuhù héxīn dǐxiàn, yě yào gēnjù duìhuà fēnwéi línghuó biàntōng jùtǐ de hézuò tiáokuǎn.",
                "en": "In complex commercial negotiations, one must firmly safeguard bottom lines while flexibly adapting specific collaboration clauses to the atmosphere.",
                "es": "En negociaciones comerciales complejas se debe defender la línea roja y, al mismo tiempo, adaptar las cláusulas contractuales con flexibilidad según el diálogo."
            }
        ],
        "collocations": [
            {"hanzi": "灵活变通", "en": "adapt flexibly / accommodate changes"},
            {"hanzi": "灵活运用", "en": "apply flexibly"},
            {"hanzi": "头脑灵活", "en": "quick-witted / nimble mind"},
            {"hanzi": "手脚灵活", "en": "nimble hands and feet / physically agile"},
            {"hanzi": "机制灵活", "en": "flexible mechanism"},
            {"hanzi": "灵活机动", "en": "agile and mobile"}
        ],
        "idioms": [
            {"hanzi": "随机应变", "pinyin": "suí jī yìng biàn", "meaning_en": "adapt oneself to changing conditions; act according to circumstances"},
            {"hanzi": "见机行事", "pinyin": "jiàn jī xíng shì", "meaning_en": "act as the occasion demands; act opportunely"},
            {"hanzi": "通权达变", "pinyin": "tōng quán dá biàn", "meaning_en": "adapt to circumstances; be pragmatic and flexible"},
            {"hanzi": "墨守成规", "pinyin": "mò shǒu chéng guī", "meaning_en": "stick stubbornly to outdated conventions; hidebound"}
        ],
        "character_decomposition": [
            {
                "character": "灵",
                "pinyin": "líng",
                "meaning_en": "agile; clever; spirit; soul; effective",
                "meaning_es": "ágil; despierto; espíritu; alma; eficaz",
                "radical": "火",
                "radical_meaning_en": "fire",
                "meaning_component": "彐/雨 (celestial rain prayers) + 火 (sparkling fiery spirit)",
                "sound_component": "霝 (archaic phonetic in traditional 靈)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Spiritual quickness and briskness bursting forth like leaping flames 火; denotes agile wit and vitality.",
                "visual_mnemonic_story_en": "A quick spirit leaping agilely like sparkling flames (火) full of nimble wit (灵).",
                "visual_mnemonic_story_es": "Un espíritu despierto que salta como llamaradas ágiles (火) desbordando ingenio (灵).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "SMF",
                "traditional": "靈"
            },
            {
                "character": "活",
                "pinyin": "huó",
                "meaning_en": "live; alive; living; dynamic; lively",
                "meaning_es": "vivir; vivo; viviente; dinámico; suelto",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (flowing water stream) + 舌 (active tongue)",
                "sound_component": "舌 (shé)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water 氵 flowing with vital living momentum like an agile moving tongue 舌; signifies life and mobility.",
                "visual_mnemonic_story_en": "Fresh clear water (氵) babbling dynamically like a moving tongue (舌), full of vital life (活).",
                "visual_mnemonic_story_es": "Agua fresca (氵) que fluye sin cesar como una lengua ágil (舌), rebosante de vida dinámica (活).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "EHR",
                "traditional": "活"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A sharp spirit (灵) flowing dynamically like living water (活) gives supreme flexibility (灵活).",
            "composite_memory_hook_es": "Un ingenio despierto (灵) que fluye con dinamismo como agua viva (活) concede total flexibilidad (灵活).",
            "cultural_and_cognitive_roots": "Derives from Daoist and military metaphors likening adaptive wisdom to the ever-shifting flow of water.",
            "tone_sandhi_and_pitch_modulation": "Second tone to second tone: 'líng huó' (35-35). Two consecutive rising pitches smoothly chained."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "寻", "pinyin": "xún", "meaning_en": "search; seek", "distinction_note": "Radical 寸 at bottom instead of 火"},
                {"character": "录", "pinyin": "lù", "meaning_en": "record", "distinction_note": "Radical 氺 at bottom"},
                {"character": "话", "pinyin": "huà", "meaning_en": "speech; language", "distinction_note": "Speech 讠 radical on left instead of water 氵"},
                {"character": "适", "pinyin": "shì", "meaning_en": "suitable; fit", "distinction_note": "Walk 辶 radical enclosing 舌"}
            ],
            "etymological_cognates": [
                {"character": "灵敏", "pinyin": "língmǐn", "gloss_en": "sensitive; keen; responsive"},
                {"character": "活跃", "pinyin": "huóyuè", "gloss_en": "active; dynamic; brisk"},
                {"character": "灵巧", "pinyin": "língqiǎo", "gloss_en": "dexterous; nimble; ingenious"},
                {"character": "死板", "pinyin": "sǐbǎn", "gloss_en": "rigid; inflexible (antonym)"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "灵活 emphasizes quick, responsive adaptation to changes in situations or physical agility.",
            "contrasts": [
                {"id": 1, "compared_word": "灵活 vs. 机智", "pinyin": "jīzhì", "analysis": "机智 emphasizes sharp wit and quick problem-solving during crises, while 灵活 denotes broader situational adaptability or physical agility."},
                {"id": 2, "compared_word": "灵活 vs. 敏捷", "pinyin": "mǐnjié", "analysis": "敏捷 emphasizes high physical speed or rapid reflexes, while 灵活 emphasizes non-dogmatic adaptability."},
                {"id": 3, "compared_word": "灵活 vs. 圆滑", "pinyin": "yuánhuá", "analysis": "圆滑 carries a distinctly negative connotation of being slick, unprincipled, and evasive in social dealings."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "孙子兵法精髓有云：“水因地而制流，兵因敌而制胜。”用兵的核心精义在于随机应变、灵活机动。秦将白起善于根据地形与敌情灵活调动兵力，而赵括死搬兵书阵法，最终导致赵军主力被全歼于崇山峻岭之中。",
                "pinyin": "Sūnzǐ bīngfǎ jīngsuǐ yǒu yún: 'Shuǐ yīn dì ér zhì liú, bīng yīn dí ér zhì shèng.' Yòngbīng de héxīn jīngyì zàiyú suíjī-yìngbiàn, línghuó jīdòng. Qín jiàng Bái Qǐ shànyú gēnjù dìxíng yǔ díqíng línghuó diàodòng bīnglì, ér Zhào Kuò sǐ bān bīngshū zhènfǎ, zuìzhōng dǎozhì Zhào jūn zhǔlì bèi quánjiān yú chóngshān-jùnlǐng zhīzhōng.",
                "en": "The Art of War states: 'Water shapes its course according to terrain; an army achieves victory by adapting to the enemy.' The soul of warfare lies in flexible mobility. Bai Qi adjusted deftly, while Zhao Kuo copied dogmatic plans, leading his army to total slaughter.",
                "es": "El Arte de la Guerra enseña: 'El agua amolda su cauce al terreno; el ejército forja la victoria adaptándose al adversario.' La clave radica en la agilidad táctica. Bai Qi adaptó sus tropas con maestría, mientras Zhao Kuo copió esquemas rígidos, condenando a su ejército."
            },
            {
                "id": "#2",
                "hanzi": "当今时代科技日新月异，社会分工与竞争形态变幻莫测。无论是科技企业的商业模式创新，还是职场人士的技能迭代，墨守成规都难逃淘汰命运。唯有保持敏锐的洞察力与灵活变通的智慧，方能在滔滔浪潮中立于不败之地。",
                "pinyin": "Dāngjīn shídài kējì rìxīn-yuèyì, shèhuì fēngōng yǔ jìngzhēng xíngtài biànhuàn-mòcè. Wúlùn shì kējì qǐyè de shāngyè móshì chuàngxīn, háishì zhíchǎng rénshì de jìnéng diédài, mòshǒu-chéngguī dōu nántáo táotài mìngyùn. Wéiyǒu bǎochí mǐnruì de dòngchálì yǔ línghuó biàntōng de zhìhuì, fāng néng zài tāotāo làngcháo zhōng lìyú búbài zhī dì.",
                "en": "In today's era of rapid tech advancement, competition shifts unpredictably. Whether in corporate model innovations or personal skill building, clinging to obsolete formulas leads to obsolescence. Sharp insight and flexible adaptability ensure standing invincible amid the waves.",
                "es": "En un mundo de avances tecnológicos vertiginosos, la competencia evoluciona sin cesar. Tanto en modelos de negocio como en la superación laboral, aferrarse a lo viejo conduce al olvido. La agudeza y la flexibilidad constante son la clave para mantenerse invictos."
            }
        ]
    }
]

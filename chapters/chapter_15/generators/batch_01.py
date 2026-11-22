# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch1 = [
    # 01 纸上谈兵
    {
        "id": "1",
        "hanzi": "纸上谈兵",
        "pinyin": "zhǐ shàng tán bīng",
        "part_of_speech": "Idiom",
        "meanings_summary": {
            "en": "to fight on paper; armchair strategy; empty theorizing divorced from reality",
            "es": "hacer la guerra sobre el papel; teorizar en el vacío; estrategia de sillón"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Idiom",
                "register": "Standard",
                "definition_en": "to discuss military affairs on paper without practical combat experience; refers to engaging in unrealistic idle theorizing",
                "definition_es": "discutir tácticas militares sobre el papel sin experiencia real; teorizar al margen de la práctica",
                "example_phrase": "纯属纸上谈兵 (purely armchair theorizing on paper)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "战国时期的赵括只会死记兵书却不懂灵活应变，在长平之战中纸上谈兵，最终导致赵军惨败。",
                "pinyin": "Zhànguó shíqī de Zhào Kuò zhǐ huì sǐjì bīngshū què bù dǒng línghuó yìngbiàn, zài Chángpíng zhī zhàn zhōng zhǐshàng-tánbīng, zuìzhōng dǎozhì Zhàojūn cǎibài.",
                "en": "During the Warring States period, Zhao Kuo memorized military texts by rote without flexible adaptation; fighting on paper at Changping, he caused his army's total defeat.",
                "es": "En los Reinos Combatientes, Zhao Kuo memorizó tratados bélicos sin saber adaptarse; su estrategia sobre el papel en Changping causó una hecatombe."
            },
            {
                "id": "#2",
                "hanzi": "搞科学研究决不能停留在纸上谈兵，必须深入实验室和一线现场开展扎扎实实的实践验证。",
                "pinyin": "Gǎo kēxué yánjiū juébùnéng tíngliú zài zhǐshàng-tánbīng, bìxū shēnrù shíyànshì hé yīxiàn xiànchǎng kāizhǎn zhāzhā-shíshí de shíjiàn yànzhèng.",
                "en": "Scientific research must never linger on paper theories; researchers must go deep into labs and field sites for rigorous empirical testing.",
                "es": "La labor científica no puede estancarse en elucubraciones teóricas; exige verificar las hipótesis sobre el terreno y en el laboratorio."
            }
        ],
        "collocations": [
            {"hanzi": "纯属纸上谈兵", "en": "purely armchair theorizing"},
            {"hanzi": "切忌纸上谈兵", "en": "strictly avoid fighting on paper"},
            {"hanzi": "不是纸上谈兵", "en": "not mere idle paper talk"},
            {"hanzi": "纸上谈兵的空论", "en": "empty armchair theorizing"},
            {"hanzi": "克服纸上谈兵", "en": "overcome empty armchair talk"},
            {"hanzi": "沦为纸上谈兵", "en": "degenerate into paper theorizing"}
        ],
        "idioms": [
            {"hanzi": "纸上谈兵", "pinyin": "zhǐ shàng tán bīng", "meaning_en": "armchair strategy; empty theorizing"},
            {"hanzi": "按图索骥", "pinyin": "àn tú suǒ jì", "meaning_en": "look for a steed according to a sketch; dogmatic approach"},
            {"hanzi": "实事求是", "pinyin": "shí shì qiú shì", "meaning_en": "seek truth from facts; pragmatic and realistic"},
            {"hanzi": "坐而论道", "pinyin": "zuò ér lùn dào", "meaning_en": "sit and talk philosophy without taking action"}
        ],
        "character_decomposition": [
            {
                "character": "纸",
                "pinyin": "zhǐ",
                "meaning_en": "paper",
                "meaning_es": "papel",
                "radical": "纟",
                "radical_meaning_en": "silk / fiber",
                "meaning_component": "纟 (plant silk fibers) + 氏 (pressing mallet / clan surface)",
                "sound_component": "氏 (shì / zhǐ)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Plant and silk fibers 纟 beaten flat into thin writing sheets 氏; represents paper.",
                "visual_mnemonic_story_en": "Beating fine silk and plant fibers (纟) into smooth flat sheets of writing paper (纸).",
                "visual_mnemonic_story_es": "Prensando fibras de seda vegetal (纟) hasta obtener hojas lisas de papel para escribir (纸).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "VMHVP",
                "traditional": "紙"
            },
            {
                "character": "上",
                "pinyin": "shàng",
                "meaning_en": "on; upon; above; upper",
                "meaning_es": "sobre; encima; arriba; superior",
                "radical": "一",
                "radical_meaning_en": "one / baseline",
                "meaning_component": "horizontal baseline 一 with an indicator stroke pointing above",
                "sound_component": "上 (shàng)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideograph with a horizontal baseline 一 and a vertical mark standing above it.",
                "visual_mnemonic_story_en": "A pointer stroke rising upright above the horizontal horizon line (上).",
                "visual_mnemonic_story_es": "Un trazo vertical que se yergue por encima de la línea base del horizonte (上).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YMY",
                "traditional": "上"
            },
            {
                "character": "谈",
                "pinyin": "tán",
                "meaning_en": "talk; converse; discuss; speak",
                "meaning_es": "hablar; conversar; platicar; discutir",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken words) + 炎 (blazing flame / glowing warmth)",
                "sound_component": "炎 (yán)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Words 讠 exchanged with glowing, lively enthusiasm like warm burning fires 炎; to discuss.",
                "visual_mnemonic_story_en": "Words of speech (讠) sparking animated warmth like burning campfire flames (谈).",
                "visual_mnemonic_story_es": "Palabras orales (讠) que desprenden el entusiasmo cálido del fuego que arde al conversar (谈).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "IVFF",
                "traditional": "談"
            },
            {
                "character": "兵",
                "pinyin": "bīng",
                "meaning_en": "soldier; weapons; military; troops",
                "meaning_es": "soldado; armas; militar; tropas",
                "radical": "八",
                "radical_meaning_en": "eight",
                "meaning_component": "斤 (sharp bronze axe) + 廾/八 (two hands gripping it)",
                "sound_component": "兵 (bīng)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Two hands 廾 firmly gripping a battleaxe 斤; represents a soldier or weapon of war.",
                "visual_mnemonic_story_en": "Two warrior hands raising a sharp battleaxe (斤) ready to defend the realm (兵).",
                "visual_mnemonic_story_es": "Dos manos firmes que alzan un hacha de combate (斤) dispuestas a defender las armas (兵).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "OMC",
                "traditional": "兵"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Discussing troops and war (谈兵) purely upon written paper (纸上) without battle experience is armchair strategy (纸上谈兵).",
            "composite_memory_hook_es": "Debatir sobre tropas y tácticas (谈兵) únicamente sobre el papel (纸上) sin experiencia real es teorizar en el vacío (纸上谈兵).",
            "cultural_and_cognitive_roots": "Originates from Sima Qian's 'Records of the Grand Historian' describing Zhao Kuo's disastrous generalship at the Battle of Changping (260 BC).",
            "tone_sandhi_and_pitch_modulation": "Four tones: 'zhǐ shàng tán bīng' (214-51-35-55). Dip on 'zhǐ', drop sharply on 'shàng', rise on 'tán', and conclude high on 'bīng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "低", "pinyin": "dī", "meaning_en": "low; beneath", "distinction_note": "Person radical 亻 on left instead of 纟"},
                {"character": "卡", "pinyin": "kǎ", "meaning_en": "card; block", "distinction_note": "Upper stroke pointing down combined with 上"},
                {"character": "淡", "pinyin": "dàn", "meaning_en": "bland; pale", "distinction_note": "Water radical 氵 on left instead of 讠"},
                {"character": "乒", "pinyin": "pīng", "meaning_en": "ping (table tennis)", "distinction_note": "Has only left leg stroke, missing right leg"}
            ],
            "etymological_cognates": [
                {"character": "报纸", "pinyin": "bàozhǐ", "gloss_en": "newspaper"},
                {"character": "谈话", "pinyin": "tánhuà", "gloss_en": "conversation; talk"},
                {"character": "士兵", "pinyin": "shìbīng", "gloss_en": "soldier; rank-and-file"},
                {"character": "兵法", "pinyin": "bīngfǎ", "gloss_en": "art of war; military strategy"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "纸上谈兵 mocks bookish theorists who recite dogma fluently but disastrously botch real-world application.",
            "contrasts": [
                {"id": 1, "compared_word": "纸上谈兵 vs. 实战经验", "pinyin": "shízhàn jīngyàn", "analysis": "实战经验 denotes battle-tested pragmatic capability, the exact remedy for 纸上谈兵."},
                {"id": 2, "compared_word": "纸上谈兵 vs. 按图索骥", "pinyin": "àn tú suǒ jì", "analysis": "按图索骥 criticizes inflexible rule-following, while 纸上谈兵 highlights empty talk lacking battlefield competence."},
                {"id": 3, "compared_word": "纸上谈兵 vs. 身体力行", "pinyin": "shēntǐ-lìxíng", "analysis": "身体力行 is the direct antonym meaning to personally practice and implement ideas in deed."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "战国名将赵奢深谙兵法，其子赵括自幼熟读兵书，谈起用兵之道口若悬河。然而赵奢却预言赵括必败，因为他把战场厮杀视同儿戏。长平之战中赵括盲目出击，惨遭秦军合围，成为后世讽刺“纸上谈兵”的惨痛教训。",
                "pinyin": "Zhànguó míngjiàng Zhào Shē shēn'ān bīngfǎ, qí zǐ Zhào Kuò zìyòu shúdú bīngshū, tán qǐ yòngbīng zhī dào kǒuruò-xuánhé. Rán'ér Zhào Shē què yùyán Zhào Kuò bì bài, yīnwèi tā bǎ zhànchǎng sīshā shìtóng érxì. Chángpíng zhī zhàn zhōng Zhào Kuò mángmù chūjī, cǎnzāo Qínjūn héwéi, chéngwéi hòushì fěngcì 'zhǐshàng-tánbīng' de cǎntòng jiàoxun.",
                "en": "General Zhao She was versed in strategy; his son Zhao Kuo recited military tactics effortlessly. Yet Zhao She foretold his son's doom for treating war lightly. Zhao Kuo's blunder at Changping became the tragic symbol of 'fighting on paper.'",
                "es": "El general Zhao She dominaba la táctica; su hijo Zhao Kuo recitaba tratados con soltura. Pero Zhao She predijo su fracaso por tomar la guerra como un juego. El desastre de Zhao Kuo en Changping se convirtió en trágico escarmiento."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业管理与经济决策中，“纸上谈兵”同样是一大忌讳。再完美的商业策划方案，如果脱离了真实的市场需求与一线调研，最终都只能沦为空洞的设想。唯有深入基层倾听用户心声，在实践中检验真理，方能行稳致远。",
                "pinyin": "Zài xiàndài qǐyè guǎnlǐ yǔ jīngjì juécè zhōng, 'zhǐshàng-tánbīng' tóngyàng shì yī dà jìhuì. Zài wánměi de shāngyè cèhuà fāng'àn, rúguǒ tuōlí le zhēnshí de shìchǎng xūqiú yǔ yīxiàn diàoyán, zuìzhōng dōu zhǐnéng lúnwéi kōngdòng de shèxiǎng. Wéiyǒu shēnrù jīcéng qīngtīng yònghù xīnshēng, zài shíjiàn zhōng jiǎnyàn zhēnlǐ, fāng néng xíngwěn-zhìyuǎn.",
                "en": "In corporate management, 'fighting on paper' remains a perilous pitfall. No matter how flawless a business proposal appears, divorcing it from market research renders it an empty fantasy. Only testing ideas on the ground yields success.",
                "es": "En la gestión corporativa, teorizar sobre el papel acarrea graves tropiezos. Por impecable que luzca un plan de negocio, si desoye el mercado real queda en vana quimera; solo el examen directo con los usuarios garantiza el éxito."
            }
        ]
    },

    # 02 军事
    {
        "id": "2",
        "hanzi": "军事",
        "pinyin": "jūn shì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "military affairs; military matters; army defense",
            "es": "asuntos militares; milicia; arte de la guerra"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "affairs, activities, equipment, and operations relating to armed forces, warfare, and national defense",
                "definition_es": "actividades, pertrechos y operaciones relativas a las fuerzas armadas, la guerra y la defensa nacional",
                "example_phrase": "军事演习 (military exercise)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "战国时期的著名军事家孙武所著的《孙子兵法》，被誉为世界上最古老而深刻的军事理论经典。",
                "pinyin": "Zhànguó shíqī de zhùmíng jūnshìjiā Sūn Wǔ suǒ zhù de Sūnzǐ Bīngfǎ, bèi yù wéi shìjiè shang zuì gǔlǎo ér shēnkè de jūnshì lǐlùn jīngdiǎn.",
                "en": "The Art of War, authored by renowned military strategist Sun Wu, is hailed as the world's oldest and most profound military theory classic.",
                "es": "El arte de la guerra, escrito por el insigne militar Sun Wu, es ensalzado como el tratado de estrategia bélica más antiguo y profundo del orbe."
            },
            {
                "id": "#2",
                "hanzi": "两国边境防务代表团就共同关心的军事安全问题举行了坦诚而深入的会谈。",
                "pinyin": "Liǎng guó biānjìng fángwù dàibiǎotuán jiù gòngtóng guānxīn de jūnshì ānquán wèntí jǔxíng le tǎncéng ér shēnrù de huìtán.",
                "en": "Border defense delegations from both countries held candid, in-depth talks on shared military and security concerns.",
                "es": "Delegaciones fronterizas de ambos países mantuvieron un diálogo franco y pormenorizado sobre asuntos de seguridad y defensa militar."
            }
        ],
        "collocations": [
            {"hanzi": "军事行动", "en": "military operation"},
            {"hanzi": "军事基地", "en": "military base"},
            {"hanzi": "军事演习", "en": "military drill / exercise"},
            {"hanzi": "军事力量", "en": "military power / capability"},
            {"hanzi": "军事技术", "en": "military technology"},
            {"hanzi": "军事专家", "en": "military expert"}
        ],
        "idioms": [
            {"hanzi": "兵戎相见", "pinyin": "bīng róng xiāng jiàn", "meaning_en": "meet each other with weapons; go to war"},
            {"hanzi": "投笔从戎", "pinyin": "tóu bǐ cóng róng", "meaning_en": "throw aside the pen and join the army"},
            {"hanzi": "运筹帷幄", "pinyin": "yùn chóu wéi wò", "meaning_en": "devise strategies within a military tent; masterminding victory"},
            {"hanzi": "厉兵秣马", "pinyin": "lì bīng mò mǎ", "meaning_en": "sharpen weapons and feed horses; prepare for combat"}
        ],
        "character_decomposition": [
            {
                "character": "军",
                "pinyin": "jūn",
                "meaning_en": "army; military; armed forces",
                "meaning_es": "ejército; militar; fuerzas armadas",
                "radical": "冖",
                "radical_meaning_en": "cover",
                "meaning_component": "冖 (military tent/encampment cover) + 车 (war chariots)",
                "sound_component": "军 (jūn)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "War chariots 车 marshaled beneath protective encampment pavilions 冖; signifies an army.",
                "visual_mnemonic_story_en": "War chariots (车) gathered securely under an army pavilion shelter (冖) ready for battle (军).",
                "visual_mnemonic_story_es": "Carros de combate (车) guarnecidos bajo el pabellón de campaña (冖) listos para la marcha (军).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "BKJ",
                "traditional": "軍"
            },
            {
                "character": "事",
                "pinyin": "shì",
                "meaning_en": "matter; thing; business; affair",
                "meaning_es": "asunto; materia; quehacer; labor",
                "radical": "亅",
                "radical_meaning_en": "hook",
                "meaning_component": "hand holding an official tally stylus or scribe's recording tablet",
                "sound_component": "事 (shì)",
                "stroke_count": 8,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "An official scribe holding up a record brush or tally board to record court state affairs.",
                "visual_mnemonic_story_en": "An officer holding up an administrative record stylus (事) to oversee affairs.",
                "visual_mnemonic_story_es": "Un escriba alzando una tablilla oficial para registrar los asuntos de gobierno (事).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "JXLN",
                "traditional": "事"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Chariots encamped for war (军) combined with administrative governance affairs (事) form military matters (军事).",
            "composite_memory_hook_es": "Los carros acampados para la batalla (军) unidos a la gestión oficial (事) definen la ciencia militar (军事).",
            "cultural_and_cognitive_roots": "A cornerstone domain of ancient governance: 'The major affairs of state are ritual sacrifice and military defense' (国之大事，在祀与戎).",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'jūn shì' (55-51). Hold 'jūn' high and firm, then drop decisively on 'shì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "车", "pinyin": "chē", "meaning_en": "vehicle; car", "distinction_note": "Lacks the top canopy cover 冖"},
                {"character": "挥", "pinyin": "huī", "meaning_en": "wave; wield", "distinction_note": "Hand radical 扌 on left of 军"},
                {"character": "吏", "pinyin": "lì", "meaning_en": "petty official", "distinction_note": "Lacks the central horizontal bars of 事"},
                {"character": "中", "pinyin": "zhōng", "meaning_en": "middle", "distinction_note": "Single vertical stroke through 口 box"}
            ],
            "etymological_cognates": [
                {"character": "军队", "pinyin": "jūnduì", "gloss_en": "armed forces; army"},
                {"character": "军官", "pinyin": "jūnguān", "gloss_en": "military officer"},
                {"character": "事务", "pinyin": "shìwù", "gloss_en": "general affairs; matters"},
                {"character": "事情", "pinyin": "shìqing", "gloss_en": "affair; matter; thing"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "军事 specifically encompasses strategic, tactical, and organizational affairs of national defense and armed forces.",
            "contrasts": [
                {"id": 1, "compared_word": "军事 vs. 政治", "pinyin": "zhèngzhì", "analysis": "政治 governs statecraft, law, and ideology, while 军事 represents armed defense instrumentalities."},
                {"id": 2, "compared_word": "军事 vs. 民事", "pinyin": "mínshì", "analysis": "民事 deals with civil laws, domestic contracts, and citizens' rights, contrasted with armed 军事."},
                {"id": 3, "compared_word": "军事 vs. 战争", "pinyin": "zhànzhēng", "analysis": "战争 refers to the armed conflict state itself, while 军事 covers the broader scientific institution, logistics, and doctrines."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代军事理论历史悠久、博大精深。《孙子兵法》强调“兵者，国之大事，死生之地，存亡之道，不可不察也”。它主张以谋略胜敌，强调“不战而屈人之兵”的高超境界，成为历代军事家推崇的至高典范。",
                "pinyin": "Zhōngguó gǔdài jūnshì lǐlùn lìshǐ yōujiǔ, bódà-jīngshēn. Sūnzǐ Bīngfǎ qiángdiào 'Bīng zhě, guó zhī dàshì, sǐshēng zhī dì, cúnwáng zhī dào, bùkě bù chá yě'. Tā zhǔzhāng yǐ móulüè shèng dí, qiángdiào 'bù zhàn ér qū rén zhī bīng' de gāochāo jìngjiè, chéngwéi lìdài jūnshìjiā tuīchóng de zhìgāo diǎnfàn.",
                "en": "Ancient Chinese military theory has a long and profound history. Sunzi stressed: 'Military affairs are vital to the state—the realm of life and death, the road to survival.' It championed outwitting enemies and subduing them without fighting.",
                "es": "La doctrina militar clásica china goza de una hondura milenaria. Sun Tzu subrayó: 'La guerra es el asunto primordial del Estado, el terreno de la vida y la muerte.' Abogó por vencer al enemigo mediante estratagemas sin librar combate."
            },
            {
                "id": "#2",
                "hanzi": "进入现代信息技术时代，军事科技的迅猛发展正在深刻重塑现代战争形态。无人作战平台、人工智能指挥网络以及太空防御系统，成为各大国军事现代化建设的前沿焦点。强大的综合军事实力，是捍卫国家和平安宁的坚强盾牌。",
                "pinyin": "Jìnrù xiàndài xìnxī jìshù shídài, jūnshì kējì de xùnměng fāzhǎn zhèngzài shēnkè zhòngsù xiàndài zhànzhēng xíngtài. Wúrén zuòzhàn píngtái, réngōng zhìnéng zhǐhuī wǎngluò yǐjí tàikōng fángyù xìtǒng, chéngwéi gè dàguó jūnshì xiàndàihuà jiànshè de qiányán jiāodiǎn. Qiángdà de zōnghé jūnshì shílì, shì hànwèi guójiā hépíng ānníng de jiānqiáng dùnpái.",
                "en": "In the information age, rapid advances in military technology reshape modern warfare. Unmanned combat units, AI command networks, and space defense stand at the forefront of military modernization, shielding national sovereignty and peace.",
                "es": "En la era de la información, el salto tecnológico transforma el arte bélico. Plataformas no tripuladas, redes de mando con IA y defensa aeroespacial lideran la vanguardia militar, protegiendo la paz y la soberanía patria."
            }
        ]
    },

    # 03 敌人
    {
        "id": "3",
        "hanzi": "敌人",
        "pinyin": "dí rén",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "enemy; foe; opponent; adversary",
            "es": "enemigo; adversario; rival hostil"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a person, hostile group, or opposing army that seeks to harm, defeat, or conquer another",
                "definition_es": "persona, facción armada o fuerza hostil que busca dañar, vencer o destruir a otra",
                "example_phrase": "消灭敌人 (wipe out the enemy)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在古代战争中，优秀的将领必须知己知彼，准确洞察敌人的战略意图与防守弱点。",
                "pinyin": "Zài gǔdài zhànzhēng zhōng, yōuxiù de jiànglǐng bìxū zhījǐ-zhībǐ, zhǔnquè dòngchá dírén de zhànlüè yìtú yǔ fángshǒu ruòdiǎn.",
                "en": "In ancient warfare, competent commanders had to know themselves and the enemy, accurately discerning foes' strategic intents and defenses.",
                "es": "En la guerra clásica, los buenos generales debían conocerse a sí mismos y al adversario, detectando las intenciones y flaquezas del enemigo."
            },
            {
                "id": "#2",
                "hanzi": "拖延和懒惰是我们在求学与自我成长道路上必须时刻警惕并战胜的无形敌人。",
                "pinyin": "Tuōyán hé lǎnduò shì wǒmen zài qiúxué yǔ zìwǒ chéngzhǎng dàolù shang bìxū shíkè jǐngtì bìng zhànshèng de wúxíng dírén.",
                "en": "Procrastination and indolence are invisible enemies that we must constantly guard against and overcome on our road to self-growth.",
                "es": "La desidia y la procrastinación constituyen enemigos invisibles a los que debemos combatir con tesón en nuestro desarrollo personal."
            }
        ],
        "collocations": [
            {"hanzi": "消灭敌人", "en": "eliminate / defeat the enemy"},
            {"hanzi": "顽强的敌人", "en": "tenacious / stubborn enemy"},
            {"hanzi": "共同的敌人", "en": "common enemy"},
            {"hanzi": "化敌为友", "en": "turn foes into friends"},
            {"hanzi": "敌人的阴谋", "en": "enemy's conspiracy / plot"},
            {"hanzi": "面对敌人", "en": "confront the enemy"}
        ],
        "idioms": [
            {"hanzi": "知己知彼，百战不殆", "pinyin": "zhī jǐ zhī bǐ, bǎi zhàn bù dài", "meaning_en": "know yourself and know your enemy, and you will never be defeated"},
            {"hanzi": "克敌制胜", "pinyin": "kè dí zhì shèng", "meaning_en": "overcome the enemy and secure victory"},
            {"hanzi": "同仇敌忾", "pinyin": "tóng chóu dí kài", "meaning_en": "share common hatred against a mortal foe"},
            {"hanzi": "化敌为友", "pinyin": "huà dí wéi yǒu", "meaning_en": "turn an enemy into a loyal friend"}
        ],
        "character_decomposition": [
            {
                "character": "敌",
                "pinyin": "dí",
                "meaning_en": "enemy; resist; match; equal",
                "meaning_es": "enemigo; resistir; rivalizar; igualar",
                "radical": "攵",
                "radical_meaning_en": "tap / strike",
                "meaning_component": "啇 (stalk of wheat / opponent across river) + 攵 (striking weapon)",
                "sound_component": "啇 (dī)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Striking with weapons 攵 against an opposing rival 啇 across the front line; marks an adversary.",
                "visual_mnemonic_story_en": "Striking with an iron weapon (攵) to repel a hostile opponent attacking the stronghold (敌).",
                "visual_mnemonic_story_es": "Blandir un arma (攵) para repeler al contendiente hostil que ataca la muralla (敌).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YBOK",
                "traditional": "敵"
            },
            {
                "character": "人",
                "pinyin": "rén",
                "meaning_en": "person; human",
                "meaning_es": "persona; humano",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "profile pictograph of a human walking",
                "sound_component": "人 (rén)",
                "stroke_count": 2,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Profile of a walking person with arms and legs.",
                "visual_mnemonic_story_en": "An upright walking human being (人).",
                "visual_mnemonic_story_es": "Un ser humano que marcha erguido (人).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "O",
                "traditional": "人"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A hostile adversary facing you in combat (敌) who is a human person (人) is an enemy (敌人).",
            "composite_memory_hook_es": "Un contrincante hostil que empuña las armas (敌) encarnado en persona (人) define al enemigo (敌人).",
            "cultural_and_cognitive_roots": "Derived from classical interstate wars where adversaries met in battle, extended figuratively to obstacles and vices.",
            "tone_sandhi_and_pitch_modulation": "Double second tone: 'dí rén' (35-35). Rise cleanly on both syllables with steady cadence."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "故", "pinyin": "gù", "meaning_en": "old; cause", "distinction_note": "Old 古 on left instead of 啇"},
                {"character": "政", "pinyin": "zhèng", "meaning_en": "politics", "distinction_note": "Correct 正 on left instead of 啇"},
                {"character": "入", "pinyin": "rù", "meaning_en": "enter", "distinction_note": "Right stroke overlaps left stroke"},
                {"character": "大", "pinyin": "dà", "meaning_en": "big", "distinction_note": "Horizontal bar across 人"}
            ],
            "etymological_cognates": [
                {"character": "敌手", "pinyin": "díshǒu", "gloss_en": "match; opponent; rival"},
                {"character": "敌对", "pinyin": "díduì", "gloss_en": "hostile; antagonistic"},
                {"character": "情敌", "pinyin": "qíngdí", "gloss_en": "romantic rival"},
                {"character": "强敌", "pinyin": "qiángdí", "gloss_en": "formidable foe"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "敌人 carries acute hostility, animosity, or lethal confrontation.",
            "contrasts": [
                {"id": 1, "compared_word": "敌人 vs. 朋友", "pinyin": "péngyou", "analysis": "朋友 is the direct antonym meaning a friendly companion or trusted ally."},
                {"id": 2, "compared_word": "敌人 vs. 对手", "pinyin": "duìshǒu", "analysis": "对手 refers to sporting or business rivals who compete without wishing each other's physical destruction, unlike 敌人."},
                {"id": 3, "compared_word": "敌人 vs. 仇人", "pinyin": "chóurén", "analysis": "仇人 stresses intense personal hatred/vendetta, whereas 敌人 can be a broad military or political adversary."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "战国末期秦赵长平之战，秦军主帅白起针对赵括缺乏实战经验的弱点，假装败退诱敌深入。骄傲轻敌的赵括误以为敌人溃退，盲目率大军追击，结果主力被秦军切断后路，四十万赵军最终陷入绝境而全军覆没。",
                "pinyin": "Zhànguó mòqī Qín-Zhào Chángpíng zhī zhàn, Qínjūn zhǔshuài Bái Qǐ zhēnduì Zhào Kuò quēfá shízhàn jīngyàn de ruòdiǎn, jiǎzhuāng bàituì yòudí shēnrù. Jiāo'ào qīngdí de Zhào Kuò wùyǐwéi dírén kuìtuì, mángmù shuài dàjūn zhuījī, jiéguǒ zhǔlì bèi Qínjūn qiēduàn hòulù, sìshí wàn Zhàojūn zuìzhōng xiànrù juéjìng ér quánjūn-fùmò.",
                "en": "At the Battle of Changping, Qin General Bai Qi feigned retreat to lure the enemy, knowing Zhao Kuo's inexperience. Arrogant Zhao Kuo pursued rashly, believing the enemy routed, only for his 400,000 troops to be encircled and annihilated.",
                "es": "En la batalla de Changping, el general Bai Qi fingió huir para atraer al inexperto Zhao Kuo. Confiado, Zhao Kuo persiguió al supuesto enemigo en desbandada, viendo a sus 400.000 soldados rodeados y aniquilados sin remedio."
            },
            {
                "id": "#2",
                "hanzi": "在人生的漫长征程中，最可怕的敌人往往不是外界的强劲竞争对手，而是潜藏于内心的傲慢、恐惧与懈怠。学会战胜自满、勇于克服懒惰，将内心的软弱转化为前进的动力，我们才能成为自己命运真正的主宰者。",
                "pinyin": "Zài rénshēng de màncháng zhēngchéng zhōng, zuì kěpà de dírén wǎngwǎng bùshì wàijiè de qiángjìn jìngzhēng duìshǒu, ér shì qiáncáng yú nèixīn de àomàn, kǒngjù yǔ xièdài. Xuéhuì zhànshèng zìmǎn, yǒngyú kèfú lǎnduò, jiāng nèixīn de ruǎnruò huàwéi qiánjìn de dònglì, wǒmen cái néng chéngwéi zìjǐ mìngyùn zhēnzhèng de zhǔzǎizhě.",
                "en": "On the long journey of life, the most fearsome enemy is often not an external adversary, but the arrogance, fear, and indolence lurking within. Conquering self-satisfaction and converting weakness into momentum makes us true masters of destiny.",
                "es": "En el camino de la vida, el enemigo más temible no suele ser el adversario externo, sino la soberbia, el temor y la holgazanería interior. Vencer la autocomplacencia y mudar la flaqueza en empuje nos convierte en dueños de nuestro destino."
            }
        ]
    },

    # 04 理论
    {
        "id": "4",
        "hanzi": "理论",
        "pinyin": "lǐ lùn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "theory; theoretical system; to argue/debate",
            "es": "teoría; cuerpo teórico; teorizar; discutir razones"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a systematic framework of concepts, principles, and laws derived from practice and used to explain phenomena",
                "definition_es": "conjunto sistemático de leyes, principios y conceptos formulados para explicar fenómenos y guiar la práctica",
                "example_phrase": "理论与实践相结合 (combine theory with practice)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "科学的理论只有与生产实践紧密结合，才能转化为推动社会生产力发展的强大现实动力。",
                "pinyin": "Kēxué de lǐlùn zhǐyǒu yǔ shēngchǎn shíjiàn jǐnmì jiéhé, cái néng zhuǎnhuà wéi tuīdòng shèhuì shēngchǎnlì fāzhǎn de qiángdà xiànshí dònglì.",
                "en": "Scientific theory can only be transformed into a mighty driving force for productive forces when closely integrated with practical production.",
                "es": "Las teorías científicas solo se convierten en motor del desarrollo cuando se articulan con la práctica transformadora de la producción."
            },
            {
                "id": "#2",
                "hanzi": "著名物理学家爱因斯坦提出的相对论理论，深刻彻底地革新了人类关于时间与空间的认知。",
                "pinyin": "Zhùmíng wùlǐxuéjiā Àiyīnsītǎn tíchū de xiāngduìlùn lǐlùn, shēnkè chèdǐ de géxīn le rénlèi guānyú shíjiān yǔ kōngjiān de rènzhī.",
                "en": "The theory of relativity formulated by Albert Einstein profoundly and thoroughly revolutionized human understanding of time and space.",
                "es": "La teoría de la relatividad formulada por Albert Einstein revolucionó de raíz la comprensión humana del tiempo y el espacio."
            }
        ],
        "collocations": [
            {"hanzi": "理论体系", "en": "theoretical framework / system"},
            {"hanzi": "理论研究", "en": "theoretical research"},
            {"hanzi": "理论与实践", "en": "theory and practice"},
            {"hanzi": "基本理论", "en": "fundamental theory"},
            {"hanzi": "深化理论", "en": "deepen theory"},
            {"hanzi": "理论创新", "en": "theoretical innovation"}
        ],
        "idioms": [
            {"hanzi": "言之成理", "pinyin": "yán zhī chéng lǐ", "meaning_en": "spoken with cogent reason and sound logic"},
            {"hanzi": "实事求是", "pinyin": "shí shì qiú shì", "meaning_en": "seek truth from practical facts"},
            {"hanzi": "据理力争", "pinyin": "jù lǐ lì zhēng", "meaning_en": "argue vigorously on the basis of reason"},
            {"hanzi": "通情达理", "pinyin": "tōng qíng dá lǐ", "meaning_en": "fair-minded, reasonable, and sensible"}
        ],
        "character_decomposition": [
            {
                "character": "理",
                "pinyin": "lǐ",
                "meaning_en": "reason; logic; order; manage; polish jade",
                "meaning_es": "razón; lógica; orden; gobernar; pulir jade",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王/玉 (raw jade stone) + 里 (settlement fields with orderly paths)",
                "sound_component": "里 (lǐ)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Carving natural veined patterns in raw jade 玉 following structural lines 里; implies intrinsic logic.",
                "visual_mnemonic_story_en": "Following the natural grain to carve raw jade (玉) into orderly patterns (理).",
                "visual_mnemonic_story_es": "Seguir las vetas naturales del jade (玉) para pulirlo conforme a una pauta armónica (理).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "MGWG",
                "traditional": "理"
            },
            {
                "character": "论",
                "pinyin": "lùn",
                "meaning_en": "discuss; discourse; debate; theory",
                "meaning_es": "discutir; disertar; debatir; teoría",
                "radical": "讠",
                "radical_meaning_en": "speech",
                "meaning_component": "讠 (spoken discourse) + 仑 (bamboo slips bound in logical sequence)",
                "sound_component": "仑 (lún)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Spoken words 讠 arranged into logical arguments like sequential bound bamboo slips 仑; to theorize.",
                "visual_mnemonic_story_en": "Words of speech (讠) arranged methodically like bound slips (仑) into an articulate thesis (论).",
                "visual_mnemonic_story_es": "Palabras (讠) ensambladas metódicamente como tablillas de bambú encuadernadas (仑) para formular una tesis (论).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "IVOP",
                "traditional": "論"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The intrinsic logic of things (理) expounded in systematic discourse (论) forms a theory (理论).",
            "composite_memory_hook_es": "La lógica interna de las cosas (理) expuesta en discurso ordenado (论) constituye una teoría (理论).",
            "cultural_and_cognitive_roots": "Blends Neo-Confucian 'Principle' (天理) with classical rhetoric and modern scientific epistemologies.",
            "tone_sandhi_and_pitch_modulation": "Third tone to fourth tone: 'lǐ lùn' (214-51). Dip deeply on 'lǐ', then drop with academic firmness on 'lùn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "埋", "pinyin": "mái", "meaning_en": "bury; inter", "distinction_note": "Soil radical 土 on left of 里 instead of 王"},
                {"character": "轮", "pinyin": "lún", "meaning_en": "wheel; rotate", "distinction_note": "Vehicle radical 车 on left instead of 讠"},
                {"character": "伦", "pinyin": "lún", "meaning_en": "ethics; relation", "distinction_note": "Person radical 亻 on left instead of 讠"},
                {"character": "沦", "pinyin": "lún", "meaning_en": "sink; degenerate", "distinction_note": "Water radical 氵 on left instead of 讠"}
            ],
            "etymological_cognates": [
                {"character": "理解", "pinyin": "lǐjiě", "gloss_en": "understand; comprehend"},
                {"character": "道理", "pinyin": "dàolǐ", "gloss_en": "principle; reason"},
                {"character": "讨论", "pinyin": "tǎolùn", "gloss_en": "discuss; talk over"},
                {"character": "论文", "pinyin": "lùnwén", "gloss_en": "thesis; academic paper"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "理论 emphasizes systematic abstract knowledge and conceptual principles explaining reality.",
            "contrasts": [
                {"id": 1, "compared_word": "理论 vs. 实践", "pinyin": "shíjiàn", "analysis": "实践 is the direct antonym meaning hands-on practical action and empirical testing."},
                {"id": 2, "compared_word": "理论 vs. 经验", "pinyin": "jīngyàn", "analysis": "经验 refers to accumulated perceptual know-how, while 理论 represents systematized conceptual laws."},
                {"id": 3, "compared_word": "理论 vs. 空想", "pinyin": "kōngxiǎng", "analysis": "空想 is baseless day-dreaming, whereas genuine 理论 is rooted in empirical validation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国古代兵书不仅记载了行军布阵的具体战术，更构建了博大精深的军事理论体系。然而先贤再三告诫，高深的军事理论唯有结合瞬息万变的战场实际灵活运用，才能化为克敌制胜的法宝，切不可拘泥于书本死板教条。",
                "pinyin": "Zhōngguó gǔdài bīngshū bùjǐn jìzǎi le xíngjūn bùzhèn de jùtǐ zhànshù, gèng gòujiàn le bódà-jīngshēn de jūnshì lǐlùn tǐxì. Rán'ér xiānxián zàisān gàojiè, gāoshēn de jūnshì lǐlùn wéiyǒu jiéhé shùnxī-wànbiàn de zhànchǎng shíjì línghuó yùnyòng, cái néng huà wéi kèdí-zhìshèng de fǎbǎo, qiè bùkě jūní yú shūběn sǐbǎn jiàotiáo.",
                "en": "Ancient military treatises built rich theoretical systems beyond tactical formations. Yet sages cautioned that military theory guarantees victory only when flexibly adapted to fast-changing battlefield conditions, rather than dogmatically followed.",
                "es": "Los tratados castrenses antiguos forjaron un hondo cuerpo teórico más allá de las formaciones tácticas. No obstante, los maestros advirtieron que la teoría bélica solo triunfa adaptándose a la realidad cambiante del campo de batalla."
            },
            {
                "id": "#2",
                "hanzi": "任何重大的科学发现都离不开基础理论的开创性突破。现代量子力学与人工智能算法的飞速发展，无一不是建立在深厚数学物理理论基石之上的。强化基础理论研究，是我们在全球科技竞争中实现原始创新的根本所在。",
                "pinyin": "Rènhé zhòngdà de kēxué fāxiàn dōu lìbùkāi jīchǔ lǐlùn de kāichuàngxìng tūpò. Xiàndài liàngzǐ lìxué yǔ réngōng zhìnéng suànfǎ de fēisù fāzhǎn, wúyībùshì jiànlì zài shēnhòu shùxué wùlǐ lǐlùn jīshí zhīshàng de. Qiánghuà jīchǔ lǐlùn yánjiū, shì wǒmen zài quánqiú kējì jìngzhēng zhōng shíxiàn yuánshǐ chuàngxīn de gēnběn suǒzài.",
                "en": "Every breakthrough in science rests upon foundational theoretical advances. Quantum physics and artificial intelligence rely squarely on deep mathematical theories. Strengthening basic theoretical research fuels authentic original innovation.",
                "es": "Los grandes descubrimientos de la ciencia nacen de avances teóricos de raíz. La física cuántica y la inteligencia artificial se erigen sobre sólidas bases matemáticas; potenciar la investigación teórica es la clave de la innovación."
            }
        ]
    },

    # 05 作战
    {
        "id": "5",
        "hanzi": "作战",
        "pinyin": "zuò zhàn",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to fight; engage in combat; conduct military operations",
            "es": "combatir; entrar en combate; librar una batalla; operar militarmente"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to conduct military fighting, campaigns, or strategic operations against opposing forces",
                "definition_es": "entrar en combate armado o desplegar maniobras bélicas y estratégicas contra el enemigo",
                "example_phrase": "协同作战 (coordinate joint combat operations)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "在复杂多变的高原山地环境中，陆空两军紧密配合，成功完成了联合模拟作战演练。",
                "pinyin": "Zài fùzá duōbiàn de gāoyuán shāndì huánjìng zhōng, lù-kōng liǎng jūn jǐnmì pèihé, chénggōng wánchéng le liánhé mónǐ zuòzhàn yǎnliàn.",
                "en": "In complex and variable plateau mountain terrain, army and air forces coordinated closely to successfully execute a joint combat simulation.",
                "es": "En la quebrada orografía de la meseta, el ejército de tierra y la aviación coordinaron con éxito un ejercicio de combate simulado conjunto."
            },
            {
                "id": "#2",
                "hanzi": "经验丰富的特战分队擅长在恶劣天气与黑夜掩护下神速出击，隐蔽开展敌后作战任务。",
                "pinyin": "Jīngyàn fēngfù de tèzhàn fēnduì shàncháng zài èliè tiānqì yǔ hēiyè yǎnhù xià shénsù chūjī, yǐnbì kāizhǎn díhòu zuòzhàn rènwu.",
                "en": "Experienced special forces units excel at striking swiftly under foul weather and night cover to conduct covert operations behind enemy lines.",
                "es": "Las tropas de operaciones especiales dominan el ataque relámpago al amparo de la niebla y la noche para combatir tras las líneas enemigas."
            }
        ],
        "collocations": [
            {"hanzi": "作战方案", "en": "operational plan / battle scheme"},
            {"hanzi": "协同作战", "en": "joint / coordinated combat operations"},
            {"hanzi": "作战指挥", "en": "combat command and control"},
            {"hanzi": "独立作战", "en": "fight independently"},
            {"hanzi": "并肩作战", "en": "fight shoulder to shoulder"},
            {"hanzi": "作战能力", "en": "combat readiness / fighting capability"}
        ],
        "idioms": [
            {"hanzi": "并肩作战", "pinyin": "bìng jiān zuò zhàn", "meaning_en": "fight shoulder to shoulder in solidarity"},
            {"hanzi": "各自为战", "pinyin": "gè zì wéi zhàn", "meaning_en": "each fighting on one's own without coordination"},
            {"hanzi": "背水一战", "pinyin": "bèi shuǐ yī zhàn", "meaning_en": "fight with one's back to the river; do or die battle"},
            {"hanzi": "孤军作战", "pinyin": "gū jūn zuò zhàn", "meaning_en": "fight as an isolated force without reinforcements"}
        ],
        "character_decomposition": [
            {
                "character": "作",
                "pinyin": "zuò",
                "meaning_en": "do; make; act; write; work",
                "meaning_es": "hacer; actuar; elaborar; escribir",
                "radical": "亻",
                "radical_meaning_en": "person",
                "meaning_component": "亻 (person standing) + 乍 (burst into active motion / collar incision)",
                "sound_component": "乍 (zhà)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A person 亻 springing into energetic action 乍 to create or do something; signifies purposeful action.",
                "visual_mnemonic_story_en": "A person (亻) springing into proactive action to undertake an assignment (作).",
                "visual_mnemonic_story_es": "Una persona (亻) que se pone en acción decidida para acometer una faena (作).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OHS",
                "traditional": "作"
            },
            {
                "character": "战",
                "pinyin": "zhàn",
                "meaning_en": "war; battle; fight; combat",
                "meaning_es": "guerra; batalla; luchar; combatir",
                "radical": "戈",
                "radical_meaning_en": "dagger-axe / halberd",
                "meaning_component": "占 (oracle divination / seizing territory) + 戈 (striking halberd)",
                "sound_component": "占 (zhàn)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Wielding bronze halberds 戈 in battle to conquer territory designated by divination 占; signifies armed war.",
                "visual_mnemonic_story_en": "Warriors brandishing sharp halberds (戈) to contest territorial flags in combat (战).",
                "visual_mnemonic_story_es": "Guerreros empuñando alabardas de bronce (戈) para disputar el estandarte bélico (战).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YRI",
                "traditional": "戰"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Actively engaging in deliberate physical action (作) with lethal halberds in war (战) means to conduct combat operations (作战).",
            "composite_memory_hook_es": "Emprender la acción decidida (作) blandiendo las armas de guerra (战) constituye la acción de combatir (作战).",
            "cultural_and_cognitive_roots": "Military term emphasizing professional tactical deployment and organized campaign execution, extended metaphorically to crises.",
            "tone_sandhi_and_pitch_modulation": "Double fourth tone: 'zuò zhàn' (51-51). Articulate both syllables with martial, punchy firmness."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "昨", "pinyin": "zuó", "meaning_en": "yesterday", "distinction_note": "Sun radical 日 on left instead of 亻"},
                {"character": "炸", "pinyin": "zhà", "meaning_en": "explode; deep-fry", "distinction_note": "Fire radical 火 on left instead of 亻"},
                {"character": "站", "pinyin": "zhàn", "meaning_en": "stand; station", "distinction_note": "Stand 立 on left instead of 戈 on right"},
                {"character": "点", "pinyin": "diǎn", "meaning_en": "dot; point", "distinction_note": "Fire dots 灬 under 占 instead of 戈"}
            ],
            "etymological_cognates": [
                {"character": "战斗", "pinyin": "zhàndòu", "gloss_en": "fight; battle; combat"},
                {"character": "战场", "pinyin": "zhànchǎng", "gloss_en": "battlefield; war front"},
                {"character": "工作", "pinyin": "gōngzuò", "gloss_en": "work; job"},
                {"character": "作为", "pinyin": "zuòwéi", "gloss_en": "accomplishment; conduct"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "作战 designates formal, strategic, and organized military operations by armies or organized units.",
            "contrasts": [
                {"id": 1, "compared_word": "作战 vs. 打架", "pinyin": "dǎjià", "analysis": "打架 denotes colloquial physical brawling between individuals, whereas 作战 is organized military warfare."},
                {"id": 2, "compared_word": "作战 vs. 停火", "pinyin": "tínghuǒ", "analysis": "停火 is the direct antonym meaning ceasefire or suspension of hostilities."},
                {"id": 3, "compared_word": "作战 vs. 演习", "pinyin": "yǎnxí", "analysis": "演习 refers to peacetime practice drills, while 作战 entails authentic enemy combat operations."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在古代冷兵器战争中，主将的临场作战指挥往往直接决定着数万将士的生死存亡。善于作战的名将，绝不墨守陈规，而是能够根据风向、地势与敌军动向灵活调整阵型，因敌制胜，化被动为主动。",
                "pinyin": "Zài gǔdài lěngbīngqì zhànzhēng zhōng, zhǔjiàng de línchǎng zuòzhàn zhǐhuī wǎngwǎng zhíjiē juédìng zhe shù wàn jiàngshì de shēngsǐ-cúnwáng. Shànyú zuòzhàn de míngjiàng, juébù mòshǒu-chéngguī, ér shì nénggòu gēnjù fēngxiàng, dìshì yǔ díjūn dòngxiàng línghuó tiáozhěng zhènxíng, yīndí-zhìshèng, huà bèidòng wéi zhǔdòng.",
                "en": "In ancient hand-to-hand warfare, a general's battlefield combat command directly decided the survival of thousands. Skilled commanders rejected dogmatism, adjusting formations by winds, terrain, and enemy moves to turn disadvantage into victory.",
                "es": "En la guerra clásica de armas blancas, el mando táctico del general decidía la vida de miles de combatientes. Los grandes estrategas jamás se ataban a fórmulas, amoldando su táctica al terreno y al viento para forjar el triunfo."
            },
            {
                "id": "#2",
                "hanzi": "现代信息化战争不仅是前线官兵的英勇作战，更是后方科研、后勤物资保障与电子网络对抗的立体综合较量。只有陆海空天多维兵种实现高度无缝的联合作战，才能在瞬息万变的现代战场上掌握主动权。",
                "pinyin": "Xiàndài xìnxīhuà zhànzhēng bùjǐn shì qiánxiàn guānbīng de yīngyǒng zuòzhàn, gèng shì hòufāng kēyán, hòuqín wùzī bǎozhàng yǔ diànzǐ wǎngluò duìkàng de lìtǐ zōnghé jiàoliàng. Zhǐyǒu lù-hǎi-kōng-tiān duōwéi bīngzhǒng shíxiàn gāodù wúfèng de liánhé zuòzhàn, cái néng zài shùnxī-wànbiàn de xiàndài zhànchǎng shang zhǎngwò zhǔdòngquán.",
                "en": "Modern digitalized warfare relies not just on bravery at the frontline, but on multi-domain logistics, cyber defense, and aerospace coordination. Only seamless joint operations across land, sea, air, and space secure battlefield dominance.",
                "es": "La contienda moderna supera el combate frontal para implicar logística avanzada, ciberdefensa y pugna electrónica. Solo una integración tridimensional entre tierra, mar y aire permite dominar la iniciativa en el combate contemporáneo."
            }
        ]
    },

    # 06 毛病
    {
        "id": "6",
        "hanzi": "毛病",
        "pinyin": "máo bìng",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "defect; shortcoming; fault; flaw; illness; habit",
            "es": "defecto; fallo; avería; imperfección; mala costumbre; indisposición"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a flaw, defect, mechanical malfunction, personal shortcoming, bad habit, or minor illness",
                "definition_es": "defecto, fallo mecánico, imperfección de carácter, mala costumbre o afección de salud",
                "example_phrase": "克服自身的毛病 (overcome one's own shortcomings)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "战国名将赵奢深知儿子赵括有着轻敌自负、眼高手低的致命毛病，因而再三告诫他不可轻易领兵。",
                "pinyin": "Zhànguó míngjiàng Zhào Shē shēnzhī érzi Zhào Kuò yǒu zhe qīngdí zìfù, yǎngāo-shǒudī de zhìmìng máobìng, yīn'ér zàisān gàojiè tā bùkě qīngyì lǐngbīng.",
                "en": "General Zhao She knew his son Zhao Kuo suffered from the fatal flaw of arrogance and underestimating foes, repeatedly warning him against command.",
                "es": "El general Zhao She conocía el defecto mortal de su hijo Zhao Kuo de subestimar al adversario, aconsejándole no tomar jamás el mando militar."
            },
            {
                "id": "#2",
                "hanzi": "这台二手复印机由于使用年限较长，最近几天频繁出现卡纸的小毛病，需要彻底检修。",
                "pinyin": "Zhè tái èrshǒu fùyìnjī yóuyú shǐyòng niánxiàn jiàocháng, zuìjìn jǐ tiān pínfán chūxiàn kǎzhǐ de xiǎo máobìng, xūyào chèdǐ jiǎnxiū.",
                "en": "Due to its long service life, this secondhand photocopier has frequently developed paper jam glitches recently and needs an overhaul.",
                "es": "Debido a los años de servicio, la fotocopiadora sufre frecuentes averías de atasco de papel, requiriendo una revisión exhaustiva."
            }
        ],
        "collocations": [
            {"hanzi": "出毛病", "en": "break down / go wrong"},
            {"hanzi": "改掉毛病", "en": "correct a bad habit / defect"},
            {"hanzi": "挑毛病", "en": "find fault / nitpick"},
            {"hanzi": "致命毛病", "en": "fatal flaw / critical defect"},
            {"hanzi": "老毛病", "en": "old habit / recurring ailment"},
            {"hanzi": "机器毛病", "en": "mechanical trouble / glitch"}
        ],
        "idioms": [
            {"hanzi": "吹毛求疵", "pinyin": "chuī máo qiú cī", "meaning_en": "blow away hair to find scars; nitpick petty flaws"},
            {"hanzi": "自相矛盾", "pinyin": "zì xiāng máo dùn", "meaning_en": "self-contradictory in thought or speech"},
            {"hanzi": "防微杜渐", "pinyin": "fáng wēi dù jiàn", "meaning_en": "nip evil in the bud before small flaws grow big"},
            {"hanzi": "改过自新", "pinyin": "gǎi guò zì xīn", "meaning_en": "turn over a new leaf by correcting past errors"}
        ],
        "character_decomposition": [
            {
                "character": "毛",
                "pinyin": "máo",
                "meaning_en": "hair; fur; feather; flaw; down",
                "meaning_es": "pelo; vello; pluma; pelusa; mínimo",
                "radical": "毛",
                "radical_meaning_en": "fur / hair",
                "meaning_component": "pictograph of fine curved strands of animal fur or hair",
                "sound_component": "毛 (máo)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient pictograph depicting thin strands of animal hair blowing in the wind.",
                "visual_mnemonic_story_en": "Fine strands of animal fur and hair (毛) blowing lightly in the breeze.",
                "visual_mnemonic_story_es": "Mechones de pelo fino de animal (毛) que ondean suavemente con el viento.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "HQU",
                "traditional": "毛"
            },
            {
                "character": "病",
                "pinyin": "bìng",
                "meaning_en": "illness; disease; fault; defect",
                "meaning_es": "enfermedad; padecimiento; defecto; tara",
                "radical": "疒",
                "radical_meaning_en": "sickness",
                "meaning_component": "疒 (sickbed / unwell frame) + 丙 (third Heavenly Stem / feverish tail)",
                "sound_component": "丙 (bǐng)",
                "stroke_count": 10,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A person lying unwell on a sickbed 疒 with body heat and ailment 丙; denotes illness or defect.",
                "visual_mnemonic_story_en": "Lying restfully on a patient's sickbed (疒) recovering from an ailment (病).",
                "visual_mnemonic_story_es": "Guardar reposo en el lecho del enfermo (疒) para sanar de una dolencia (病).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "KMBW",
                "traditional": "病"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A tiny flaw as minute as hair (毛) that causes systematic disorder (病) is a defect or glitch (毛病).",
            "composite_memory_hook_es": "Una imperfección diminuta como un pelo (毛) que engendra malestar o avería (病) conforma un defecto (毛病).",
            "cultural_and_cognitive_roots": "Derived from ancient horse breeding where veterinarians blew animal fur aside to check for hidden sores or skin defects.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'máo bìng' (35-51). Lift cleanly on 'máo', followed by a decisive drop on 'bìng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "手", "pinyin": "shǒu", "meaning_en": "hand", "distinction_note": "Central vertical stroke curves inward, not rightward hook"},
                {"character": "痛", "pinyin": "tòng", "meaning_en": "pain", "distinction_note": "Yong 甬 inside 疒 instead of 丙"},
                {"character": "痴", "pinyin": "chī", "meaning_en": "foolish", "distinction_note": "Zhi 知 inside 疒 instead of 丙"},
                {"character": "疗", "pinyin": "liáo", "meaning_en": "heal; treat", "distinction_note": "Liao 了 inside 疒 instead of 丙"}
            ],
            "etymological_cognates": [
                {"character": "缺点", "pinyin": "quēdiǎn", "gloss_en": "shortcoming; defect"},
                {"character": "疾病", "pinyin": "jíbìng", "gloss_en": "disease; illness"},
                {"character": "皮毛", "pinyin": "pímáo", "gloss_en": "fur and skin; superficial know-how"},
                {"character": "毛料", "pinyin": "máoliào", "gloss_en": "woolen material"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "毛病 is an everyday colloquial term covering mechanical glitches, bad personal habits, and character flaws.",
            "contrasts": [
                {"id": 1, "compared_word": "毛病 vs. 缺点", "pinyin": "quēdiǎn", "analysis": "缺点 is formal and refers to general shortcomings in work/character, while 毛病 spans machine glitches and bad quirks."},
                {"id": 2, "compared_word": "毛病 vs. 错误", "pinyin": "cuòwù", "analysis": "错误 refers to an incorrect action or mistaken calculation, whereas 毛病 refers to a habitual flaw or defect."},
                {"id": 3, "compared_word": "毛病 vs. 优点", "pinyin": "yōudiǎn", "analysis": "优点 is the direct antonym meaning merit, virtue, or strong point."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "赵括自幼聪颖好学，谈论兵法时连他的父亲赵奢也难不倒他。但他最大的毛病在于缺乏谦逊之心，自以为天下兵法已尽在胸中。这种目空一切、脱离实际的毛病，最终让他在残酷的长平之战中付出了生命的惨痛代价。",
                "pinyin": "Zhào Kuò zìyòu cōngyǐng hàoxué, tánlùn bīngfǎ shí lián tā de fùqīn Zhào Shē yě nánbùdǎo tā. Dàn tā zuì dà de máobìng zàiyú quēfá qiānxùn zhī xīn, zì yǐwéi tiānxià bīngfǎ yǐ jìn zài xiōngzhōng. Zhè zhǒng mùkōng-yīqiè, tuōlí shíjì de máobìng, zuìzhōng ràng tā zài cánkù de Chángpíng zhī zhàn zhōng fùchū le shēngmìng de cǎntòng dàijià.",
                "en": "Zhao Kuo was brilliant from youth, stumping even his father on tactics. Yet his greatest defect was lack of humility, assuming he mastered warfare completely. This arrogant flaw cost him his life and an army at Changping.",
                "es": "Zhao Kuo fue aventajado desde niño, deslumbrando a su padre al hablar de táctica. Pero su peor defecto fue la arrogancia; su vanidad alejada de la realidad le costó la vida y la derrota de su tropa en Changping."
            },
            {
                "id": "#2",
                "hanzi": "在现代精密机械与航空工业中，任何微小的设计毛病都可能演变成灾难性的重大事故。工程技术人员必须具备高度的责任感，耐心地通过反复模拟排查系统中的每一个潜在毛病，精益求精，确保装备万无一失。",
                "pinyin": "Zài xiàndài jīngmì jīxiè yǔ hángkōng gōngyè zhōng, rènhé wēixiǎo de shèjì máobìng dōu kěnéng yǎnbiàn chéng zāinànxìng de zhòngdà shìgù. Gōngchéng jìshù rényuán bìxū jùbèi gāodù de zérèngǎn, nàixīn de tōngguò fǎnfù mónǐ páichá xìtǒng zhōng de měi yī gè qiánzài máobìng, jīngyìqiújīng, quèbǎo zhuāngbèi wànwúyīshī.",
                "en": "In precision engineering and aerospace, any tiny design flaw can trigger catastrophic accidents. Technicians must maintain immense accountability, repeatedly simulating stress to eliminate latent glitches and ensure flawless reliability.",
                "es": "En la ingeniería aeronáutica de precisión, cualquier imperfección de diseño acarrea catástrofes. Los ingenieros deben actuar con rigor exhaustivo, subsanando fallos potenciales para garantizar una fiabilidad intachable."
            }
        ]
    },

    # 07 道理
    {
        "id": "7",
        "hanzi": "道理",
        "pinyin": "dào lǐ",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "principle; reason; truth; logic; argument",
            "es": "razón; principio; verdad; lógica; fundamento"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "underlying principles, rationale, or fundamental laws governing nature, morality, or reasoning",
                "definition_es": "principio rector, fundamento lógico o razón moral que rige las cosas y la conducta",
                "example_phrase": "讲清道理 (explain the rationale clearly)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老将军语重心长地向年轻军官解释兵法中“虚实相生、刚柔相济”的深刻道理。",
                "pinyin": "Lǎo jiāngjūn yǔzhòng-xīncháng de xiàng niánqīng jūnguān jiěshì bīngfǎ zhōng 'xū-shí xiāng shēng, gāng-róu xiāng jì' de shēnkè dàolǐ.",
                "en": "The veteran general earnestly explained the profound principle of 'interplay between void and substance, strength and yielding' in warfare to young officers.",
                "es": "El curtido general explicó a los jóvenes oficiales el hondo fundamento de combinar la firmeza y la flexibilidad en el arte bélico."
            },
            {
                "id": "#2",
                "hanzi": "这篇通俗易懂的寓言故事，向孩子们生动揭示了“骄兵必败”的朴素处世道理。",
                "pinyin": "Zhè piān tōngsú-yìdǒng de yùyán gùshì, xiàng háizi men shēngdòng jiēshì le 'jiāobīng-bìbài' de pǔsù chǔshì dàolǐ.",
                "en": "This easily understood fable vividly revealed the simple life truth to children that 'an arrogant army faces inevitable defeat.'",
                "es": "Esta fábula amena ilustró a los niños el principio elemental de que la soberbia conduce inevitablemente a la derrota."
            }
        ],
        "collocations": [
            {"hanzi": "讲道理", "en": "reason with someone; be reasonable"},
            {"hanzi": "有道理", "en": "makes sense / reasonable"},
            {"hanzi": "深刻的道理", "en": "profound principle / deep truth"},
            {"hanzi": "明白道理", "en": "understand the reason / principle"},
            {"hanzi": "蛮不讲理", "en": "utterly unreasonable"},
            {"hanzi": "符合道理", "en": "accord with reason and logic"}
        ],
        "idioms": [
            {"hanzi": "通情达理", "pinyin": "tōng qíng dá lǐ", "meaning_en": "fair-minded, reasonable, and sensible"},
            {"hanzi": "至理名言", "pinyin": "zhì lǐ míng yán", "meaning_en": "golden maxim; words of profound wisdom"},
            {"hanzi": "合情合理", "pinyin": "hé qíng hé lǐ", "meaning_en": "fair, sensible, and completely justified"},
            {"hanzi": "理所当然", "pinyin": "lǐ suǒ dāng rán", "meaning_en": "natural and right; taken for granted as logical"}
        ],
        "character_decomposition": [
            {
                "character": "道",
                "pinyin": "dào",
                "meaning_en": "way; path; road; principle; Dao",
                "meaning_es": "camino; sendero; principio; el Tao",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (movement on path) + 首 (head of wisdom guiding feet)",
                "sound_component": "首 (shǒu)",
                "stroke_count": 12,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A person walking on a path 辶 with an enlightened head 首; signifies the moral and cosmic Way.",
                "visual_mnemonic_story_en": "Walking thoughtfully with an enlightened head (首) along the path of moral truth (道).",
                "visual_mnemonic_story_es": "Avanzar con la cabeza despejada (首) por el camino de la rectitud y la sabiduría (道).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "YHUT",
                "traditional": "道"
            },
            {
                "character": "理",
                "pinyin": "lǐ",
                "meaning_en": "reason; logic; order; manage",
                "meaning_es": "razón; lógica; orden; principio",
                "radical": "王",
                "radical_meaning_en": "jade",
                "meaning_component": "王/玉 (raw jade stone) + 里 (settlement paths)",
                "sound_component": "里 (lǐ)",
                "stroke_count": 11,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Carving jade 玉 along its natural veined grain lines 里; signifies intrinsic logic.",
                "visual_mnemonic_story_en": "Polishing jade (玉) along its natural veins to discover its inner pattern (理).",
                "visual_mnemonic_story_es": "Tallar el jade (玉) respetando sus vetas para revelar su estructura armónica (理).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "MGWG",
                "traditional": "理"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The righteous path of wisdom (道) combined with the natural logic of things (理) forms sound principle (道理).",
            "composite_memory_hook_es": "El sendero de la rectitud (道) unido al principio lógico intrínseco (理) engendra la razón o fundamento (道理).",
            "cultural_and_cognitive_roots": "Deeply rooted in classical Chinese philosophy unifying the Cosmic Dao with Neo-Confucian Li (inherent structural principle).",
            "tone_sandhi_and_pitch_modulation": "Fourth tone to third tone: 'dào lǐ' (51-214). Drop firmly on 'dào', then dip and rebound smoothly on 'lǐ'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "导", "pinyin": "dǎo", "meaning_en": "lead; guide", "distinction_note": "Inch 寸 at bottom instead of 首 and 辶"},
                {"character": "首", "pinyin": "shǒu", "meaning_en": "head; first", "distinction_note": "Lacks the movement radical 辶"},
                {"character": "埋", "pinyin": "mái", "meaning_en": "bury", "distinction_note": "Soil radical 土 on left of 里 instead of 王"},
                {"character": "野", "pinyin": "yě", "meaning_en": "wild; field", "distinction_note": "Village 里 on left and予 on right"}
            ],
            "etymological_cognates": [
                {"character": "道德", "pinyin": "dàodé", "gloss_en": "morals; ethics"},
                {"character": "理想", "pinyin": "lǐxiǎng", "gloss_en": "ideal; dream"},
                {"character": "理解", "pinyin": "lǐjiě", "gloss_en": "understand; comprehend"},
                {"character": "道义", "pinyin": "dàoyì", "gloss_en": "morality and justice"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "道理 encompasses moral truths, logical justifications, and natural principles underlying phenomena.",
            "contrasts": [
                {"id": 1, "compared_word": "道理 vs. 理由", "pinyin": "lǐyóu", "analysis": "理由 refers to a specific pretext, excuse, or justification for an action, whereas 道理 refers to universal principles or sound sense."},
                {"id": 2, "compared_word": "道理 vs. 理论", "pinyin": "lǐlùn", "analysis": "理论 designates a formal academic system, while 道理 can be everyday common sense and moral wisdom."},
                {"id": 3, "compared_word": "道理 vs. 歪理", "pinyin": "wāilǐ", "analysis": "歪理 is the direct antonym meaning fallacious, twisted, or specious arguments."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "赵国名将赵奢告诫赵括：“兵，死地也，而括易言之。”这句话蕴含着极深的人生道理。战争关乎千家万户生死存亡，若只懂在纸面上空谈道理，却不知在实践中体察险恶，到头来不仅害了自己，更会误国殃民。",
                "pinyin": "Zhàoguó míngjiàng Zhào Shē gàojiè Zhào Kuò: 'Bīng, sǐdì yě, ér Kuò yì yán zhī.' Zhè jù huà yùnhán zhe jí shēn de rénshēng dàolǐ. Zhànzhēng guānhū qiānjiā-wànhù shēngsǐ-cúnwáng, ruò zhǐ dǒng zài zhǐmiàn shang kōngtán dàolǐ, què bùzhī zài shíjiàn zhōng tǐchá xiǎn'è, dàotóulái bùjǐn hài le zìjǐ, gèng huì wùguó-yāngmín.",
                "en": "General Zhao She cautioned Zhao Kuo: 'War is mortal ground, yet you speak of it lightly.' War touches millions of lives; empty talk on paper without understanding real perils harms oneself and devastates the nation.",
                "es": "Zhao She advirtió a su hijo: 'La guerra es terreno de muerte y hablas de ella con ligereza.' Debatir razones en abstracto sin calibrar la crudeza práctica no solo destruye al individuo, sino que arruina a la patria."
            },
            {
                "id": "#2",
                "hanzi": "人与人交往最重要的准则是讲道理与讲信义。遇到矛盾分歧时，彼此心平气和地摆事实、讲道理，尊重对方的合理诉求，往往能化干戈为玉帛。通情达理的沟通方式，是维系社会和谐人际关系的润滑剂。",
                "pinyin": "Rén yǔ rén jiāowǎng zuì zhòngyào de zhǔnzé shì jiǎng dàolǐ yǔ jiǎng xìnyì. Yùdào máodùn fēnqí shí, bǐcǐ xīnpíng-qìhé de bǎi shìshí, jiǎng dàolǐ, zūnzhòng duìfāng de hélǐ sùqiú, wǎngwǎng néng huà gāngē wéi yùbó. Tōngqíng-dálǐ de gōutōng fāngshì, shì wéixì shèhuì héxié rénjì guānxi de rùnhuájì.",
                "en": "The most vital principle in social dealings is reasoning with good faith. When disputes arise, presenting facts calmly and reasoning with mutual respect turns hostility into harmony, serving as the lubricant of relationships.",
                "es": "En el trato humano, la regla de oro consiste en actuar con razón y probidad. Exponer los hechos con serenidad y atender razones legítimas desarma discordias, actuando como el mejor bálsamo de convivencia."
            }
        ]
    },

    # 08 迟早
    {
        "id": "8",
        "hanzi": "迟早",
        "pinyin": "chí zǎo",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "sooner or later; eventually; in time",
            "es": "tarde o temprano; a la larga; con el tiempo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "inevitably occurring at some future moment, regardless of whether it happens sooner or later",
                "definition_es": "que ocurrirá de modo inexorable en algún instante venidero, antes o después",
                "example_phrase": "迟早要发生 (sooner or later bound to happen)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵括如果不改掉狂妄自大、纸上谈兵的毛病，带兵打仗迟早要给赵国招致惨重的灾难。",
                "pinyin": "Zhào Kuò rúguǒ bù gǎidiào kuángwàng-zìdà, zhǐshàng-tánbīng de máobìng, dài bīng dǎzhàng chízǎo yào gěi Zhàoguó zhāozhì cǎnzhòng de zāinàn.",
                "en": "If Zhao Kuo failed to correct his arrogance and armchair habit, leading troops into combat would sooner or later bring disaster upon the State of Zhao.",
                "es": "Si Zhao Kuo no corregía su fatuidad y diletantismo teórico, mandar tropas al combate traería tarde o temprano una hecatombe al reino de Zhao."
            },
            {
                "id": "#2",
                "hanzi": "只要坚持不懈地朝着既定目标努力拼搏，汗水与付出迟早会换来丰硕的收获。",
                "pinyin": "Zhǐyào jiānchí-bùxiè de cháozhe jìdìng mùbiāo nǔlì pīnbó, hànshuǐ yǔ fùchū chízǎo huì huàn lái fēngshuò de shōuhuò.",
                "en": "As long as one perseveres tirelessly toward the set goal, sweat and dedication will sooner or later yield fruitful rewards.",
                "es": "Con tal de perseverar infatigablemente hacia la meta fijada, el sudor y el tesón cosecharán tarde o temprano frutos ubérrimos."
            }
        ],
        "collocations": [
            {"hanzi": "迟早会", "en": "sooner or later will ..."},
            {"hanzi": "迟早要来", "en": "inevitably bound to arrive"},
            {"hanzi": "迟早明白", "en": "understand eventually"},
            {"hanzi": "迟早成功", "en": "succeed sooner or later"},
            {"hanzi": "迟早水落石出", "en": "truth will out sooner or later"},
            {"hanzi": "迟早露出马脚", "en": "eventually betray oneself"}
        ],
        "idioms": [
            {"hanzi": "水落石出", "pinyin": "shuǐ luò shí chū", "meaning_en": "as water recedes stones appear; truth comes to light eventually"},
            {"hanzi": "天网恢恢", "pinyin": "tiān wǎng huī huī", "meaning_en": "the net of heaven is vast; evil will inevitably be punished"},
            {"hanzi": "苦尽甘来", "pinyin": "kǔ jìn gān lái", "meaning_en": "bitterness ends and sweetness begins; joy comes after sorrow"},
            {"hanzi": "功到自然成", "pinyin": "gōng dào zì rán chéng", "meaning_en": "when effort is ripe, success comes naturally"}
        ],
        "character_decomposition": [
            {
                "character": "迟",
                "pinyin": "chí",
                "meaning_en": "late; delayed; slow; tardy",
                "meaning_es": "tarde; lento; demorado; retrasado",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (motion along road) + 尺 (foot rule / short step)",
                "sound_component": "尺 (chǐ)",
                "stroke_count": 7,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Walking 辶 taking only small measured foot-lengths 尺 along the way; to advance slowly and arrive late.",
                "visual_mnemonic_story_en": "Advancing along a road (辶) inch by inch (尺), arriving slow and late (迟).",
                "visual_mnemonic_story_es": "Caminar por el sendero (辶) paso a paso medido a palmos (尺), demorando la marcha (迟).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "YSO",
                "traditional": "遲"
            },
            {
                "character": "早",
                "pinyin": "zǎo",
                "meaning_en": "early; morning; beforehand",
                "meaning_es": "temprano; mañana; con antelación",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun) + 十 (first morning light / armor horizon)",
                "sound_component": "早 (zǎo)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "The sun 日 peeking just above the horizon 十 at early dawn; marks early time.",
                "visual_mnemonic_story_en": "The shining morning sun (日) rising above the crossline horizon at dawn (早).",
                "visual_mnemonic_story_es": "El disco solar (日) despuntando sobre el horizonte en el alba temprana (早).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "AJ",
                "traditional": "早"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Whether late (迟) or early (早), the outcome will inevitably occur sooner or later (迟早).",
            "composite_memory_hook_es": "Sea tarde (迟) o sea temprano (早), el desenlace ocurrirá inexorablemente (迟早).",
            "cultural_and_cognitive_roots": "Expresses traditional conviction in karmic inevitability and the natural maturation of time.",
            "tone_sandhi_and_pitch_modulation": "Second tone to third tone: 'chí zǎo' (35-214). Lift smoothly on 'chí', then dip deeply and rise on 'zǎo'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "尺", "pinyin": "chǐ", "meaning_en": "ruler; foot", "distinction_note": "Lacks the movement radical 辶"},
                {"character": "送", "pinyin": "sòng", "meaning_en": "send; deliver", "distinction_note": "Pass 关 variant under 辶 instead of 尺"},
                {"character": "草", "pinyin": "cǎo", "meaning_en": "grass", "distinction_note": "Grass radical 艹 on top of 早"},
                {"character": "旱", "pinyin": "hàn", "meaning_en": "drought", "distinction_note": "Shield 干 under 日 instead of 十"}
            ],
            "etymological_cognates": [
                {"character": "迟到", "pinyin": "chídào", "gloss_en": "arrive late; be tardy"},
                {"character": "推迟", "pinyin": "tuīchí", "gloss_en": "postpone; delay"},
                {"character": "早晨", "pinyin": "zǎochén", "gloss_en": "early morning"},
                {"character": "及早", "pinyin": "jízǎo", "gloss_en": "as early as possible"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "迟早 conveys certainty that a future event is inevitable, with timing as the only variable.",
            "contrasts": [
                {"id": 1, "compared_word": "迟早 vs. 早晚", "pinyin": "zǎowǎn", "analysis": "早晚 is a colloquial synonym for sooner or later, while 迟早 is common across both written prose and spoken registers."},
                {"id": 2, "compared_word": "迟早 vs. 最终", "pinyin": "zuìzhōng", "analysis": "最终 denotes the final concluding stage in a process, whereas 迟早 affirms the inexorability of an occurrence."},
                {"id": 3, "compared_word": "迟早 vs. 决不", "pinyin": "juébù", "analysis": "决不 is the direct antonym asserting that an event will never take place under any circumstance."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "当年赵奢听闻赵括谈论军事时，不仅未露喜色，反而忧心忡忡。他对妻子说：“兵是生死之地，赵括却视若易事。赵国若不用他还罢了，若真让他做大将，破赵军者迟早必是赵括！”历史的演进不幸言中了他的预言。",
                "pinyin": "Dāngnián Zhào Shē tīngwén Zhào Kuò tánlùn jūnshì shí, bùjǐn wèi lù xǐsè, fǎn'ér yōuxīn-chōngchōng. Tā duì qīzǐ shuō: 'Bīng shì sǐdì yě, ér Kuò shì ruò yì shì. Zhàoguó ruò bù yòng tā hái bà le, ruò zhēn ràng tā zuò dàjiàng, pò Zhàojūn zhě chízǎo bì shì Zhào Kuò!' Lìshǐ de yǎnjìn bùxìng yánzhòng le tā de yùyán.",
                "en": "When Zhao She heard his son talk of war, he frowned: 'War is mortal ground, yet Kuo treats it lightly. If Zhao appoints him general, the one who destroys our army will sooner or later be Kuo!' History tragically fulfilled his prophecy.",
                "es": "Al oír a su hijo hablar de táctica, Zhao She sentenció apesadumbrado: 'La guerra es mortífera y él la toma a la ligera. Si el rey lo nombra general, ¡tarde o temprano será quien hunda a Zhao!' La historia confirmó el presagio."
            },
            {
                "id": "#2",
                "hanzi": "自然界的万物生长皆有其内在的节律。春天埋入泥土的种子，只要经历风雨的洗礼与阳光的哺育，迟早会破土成苗、开花结果。在人生的求索道路上，耐得住寂寞与沉淀的人，迟早会迎来属于自己的高光时刻。",
                "pinyin": "Zìránjiè de wànwù shēngzhǎng jiē yǒu qí nèizài de jiélǜ. Chūntiān máirù nítǔ de zhǒngzi, zhǐyào jīnglì fēngyǔ de xǐlǐ yǔ yángguāng de bǔyù, chízǎo huì pòtǔ chéng miáo, kāihuā-jiéguǒ. Zài rénshēng de qiúsuǒ dàolù shang, nàidézhù jìmò yǔ chéndiàn de rén, chízǎo huì yínglái shǔyú zìjǐ de gāoguāng shíkè.",
                "en": "All living things grow according to nature's rhythms. Seeds buried in spring, nurtured by rain and sun, will sooner or later sprout and bear fruit. Those who endure quiet dedication will eventually embrace their finest hours.",
                "es": "Todo en la naturaleza responde a ritmos armónicos. La semilla que resiste la intemperie primaveral tarde o temprano florece y da fruto; quien persevera en el callado afán alcanza tarde o temprano la plenitud soñada."
            }
        ]
    },

    # 09 军队
    {
        "id": "9",
        "hanzi": "军队",
        "pinyin": "jūn duì",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "army; armed forces; troops",
            "es": "ejército; fuerzas armadas; tropas"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the organized armed forces of a nation trained and equipped for warfare and national defense",
                "definition_es": "cuerpo militar organizado y equipado de un Estado para la defensa y operaciones bélicas",
                "example_phrase": "强大的军队 (a powerful army)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "一支纪律严明、作风优良的军队，是捍卫国家领土主权与维护人民和平生活的坚固长城。",
                "pinyin": "Yī zhī jìlǜ-yánmíng, zuòfēng-yōuliáng de jūnduì, shì hànwèi guójiā lǐngtǔ zhǔquán yǔ wéihù rénmín hépíng shēnghuó de jiāngù chángchéng.",
                "en": "A strictly disciplined and well-trained army serves as an impregnable Great Wall defending national sovereignty and peaceful life.",
                "es": "Un ejército de rigurosa disciplina constituye la muralla inexpugnable que salvaguarda la soberanía nacional y la paz del pueblo."
            },
            {
                "id": "#2",
                "hanzi": "长平之战中，秦国军队在名将白起的统一指挥下，巧妙分割包围了赵国主力部队。",
                "pinyin": "Chángpíng zhī zhàn zhōng, Qínguó jūnduì zài míngjiàng Bái Qǐ de tǒngyī zhǐhuī xià, qiǎomiào fēngē-bāowéi le Zhàoguó zhǔlì bùduì.",
                "en": "At the Battle of Changping, the Qin army under General Bai Qi's unified command cleverly partitioned and encircled Zhao's main forces.",
                "es": "En la batalla de Changping, el ejército de Qin bajo el mando de Bai Qi dividió y rodeó con destreza el grueso de las tropas de Zhao."
            }
        ],
        "collocations": [
            {"hanzi": "国家军队", "en": "national army / armed forces"},
            {"hanzi": "军队建设", "en": "army building / military buildup"},
            {"hanzi": "正规军队", "en": "regular army"},
            {"hanzi": "指挥军队", "en": "command the army"},
            {"hanzi": "军队现代化", "en": "military modernization"},
            {"hanzi": "庞大的军队", "en": "vast / formidable army"}
        ],
        "idioms": [
            {"hanzi": "千军万马", "pinyin": "qiān jūn wàn mǎ", "meaning_en": "thousands of troops and tens of thousands of horses; mighty army"},
            {"hanzi": "纪律严明", "pinyin": "jì lǜ yán míng", "meaning_en": "strictly disciplined and orderly"},
            {"hanzi": "兵贵神速", "pinyin": "bīng guì shén sù", "meaning_en": "speed is precious in warfare; lightning strike"},
            {"hanzi": "养兵千日，用兵一时", "pinyin": "yǎng bīng qiān rì, yòng bīng yī shí", "meaning_en": "train troops for a thousand days to use them for an hour"}
        ],
        "character_decomposition": [
            {
                "character": "军",
                "pinyin": "jūn",
                "meaning_en": "military; army; armed forces",
                "meaning_es": "ejército; militar; fuerzas armadas",
                "radical": "冖",
                "radical_meaning_en": "cover",
                "meaning_component": "冖 (military tent cover) + 车 (war chariots)",
                "sound_component": "军 (jūn)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "War chariots 车 assembled beneath encampment canopies 冖; signifies organized troops.",
                "visual_mnemonic_story_en": "War chariots (车) gathered under camp covers (冖) ready for combat (军).",
                "visual_mnemonic_story_es": "Carros de guerra (车) agrupados bajo el toldo militar (冖) listos para la marcha (军).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "BKJ",
                "traditional": "軍"
            },
            {
                "character": "队",
                "pinyin": "duì",
                "meaning_en": "team; squad; queue; unit",
                "meaning_es": "equipo; fila; brigada; escuadrón",
                "radical": "阝",
                "radical_meaning_en": "mound / hill",
                "meaning_component": "阝 (earthen ridge/embankment) + 人 (soldiers falling in line)",
                "sound_component": "队 (duì)",
                "stroke_count": 4,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Soldiers lining up along an earthen defensive embankment 阝 into an orderly squad; to form a queue.",
                "visual_mnemonic_story_en": "Soldiers falling into an orderly defensive line along an earthen ridge (阝) to form a squad (队).",
                "visual_mnemonic_story_es": "Soldados alineados en rigurosa hilera junto al terraplén (阝) formando una unidad (队).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NLO",
                "traditional": "隊"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Chariot encampments (军) assembled into disciplined tactical ranks (队) form an army (军队).",
            "composite_memory_hook_es": "El cuerpo expedicionario (军) alineado en unidades operativas (队) conforma el ejército (军队).",
            "cultural_and_cognitive_roots": "Captures the transition from ancient noble chariot formations to mass infantry corps organized in strict echelons.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'jūn duì' (55-51). High steady pitch on 'jūn', descending decisively on 'duì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "车", "pinyin": "chē", "meaning_en": "vehicle", "distinction_note": "Lacks the upper cover radical 冖"},
                {"character": "晕", "pinyin": "yūn", "meaning_en": "dizzy; faint", "distinction_note": "Sun 日 on top of 车 instead of 冖"},
                {"character": "防", "pinyin": "fáng", "meaning_en": "defend", "distinction_note": "Square 方 on right of 阝 instead of 人"},
                {"character": "阳", "pinyin": "yáng", "meaning_en": "sun; positive", "distinction_note": "Sun 日 on right of 阝 instead of 人"}
            ],
            "etymological_cognates": [
                {"character": "队员", "pinyin": "duìyuán", "gloss_en": "team member"},
                {"character": "排队", "pinyin": "páiduì", "gloss_en": "line up; queue"},
                {"character": "军费", "pinyin": "jūnfèi", "gloss_en": "military expenditure"},
                {"character": "军纪", "pinyin": "jūnjì", "gloss_en": "military discipline"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "军队 specifically denotes the formal, institutionalized military forces of a sovereign nation.",
            "contrasts": [
                {"id": 1, "compared_word": "军队 vs. 部队", "pinyin": "bùduì", "analysis": "部队 refers to specific operational divisions or field units, while 军队 encompasses the whole military establishment."},
                {"id": 2, "compared_word": "军队 vs. 士兵", "pinyin": "shìbīng", "analysis": "士兵 refers to individual enlisted fighters, whereas 军队 is the institutional collective armed body."},
                {"id": 3, "compared_word": "军队 vs. 警察", "pinyin": "jǐngchá", "analysis": "警察 handles domestic civic policing and public order, while 军队 defends against foreign external threats."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "战国末期，赵国军队向以骁勇善战著称，胡服骑射更使赵军骑兵名震诸侯。然而长平之战中，赵王临阵撤换沉着稳健的老将廉颇，改派赵括统领全军，最终致使数十万精锐军队被秦军围困全歼，赵国国力从此一蹶不振。",
                "pinyin": "Zhànguó mòqī, Zhàoguó jūnduì xiàng yǐ xiāoyǒng-shànzhàn zhùchēng, húfú-qíshè gèng shǐ Zhàojūn qíbīng míng zhèn zhūhóu. Rán'ér Chángpíng zhī zhàn zhōng, Zhàowáng línzhèn chèhuàn chénzhuó-wěnjiàn de lǎojiàng Lián Pō, gǎi pài Zhào Kuò tǒnglǐng quán jūn, zuìzhōng zhìshǐ shùshí wàn jīngruì jūnduì bèi Qínjūn wéikùn quánjiān, Zhàoguó guólì cóngcǐ yījué-bùzhèn.",
                "en": "In the late Warring States, the Zhao army was celebrated for fierce cavalry tactics. Yet at Changping, King Zhao replaced cautious General Lian Po with Zhao Kuo; hundreds of thousands of elite troops were encircled, crippling the state forever.",
                "es": "En los Reinos Combatientes, el ejército de Zhao gozaba de fama por su formidable caballería. Mas en Changping, el rey relevó al cauto Lian Po por Zhao Kuo, lo que llevó al aniquilamiento de su tropa de élite y al declive del reino."
            },
            {
                "id": "#2",
                "hanzi": "一支现代化的强大军队，不仅必须装备最尖端的科学武器装备，更需要具备高度严明的军纪与无私奉献的战斗精神。在抗击自然灾害与保卫人民生命财产的急难险重关头，军队始终是人民最可信赖的中流砥柱。",
                "pinyin": "Yī zhī xiàndàihuà de qiángdà jūnduì, bùjǐn bìxū zhuāngbèi zuì jiānduān de kēxué wǔqì zhuāngbèi, gèng xūyào jùbèi gāodù yánmíng de jūnjì yǔ wúsī-fèngxiàn de zhàndòu jīngshén. Zài kàngjī zìrán zāihài yǔ bǎowèi rénmín shēngmìng cáichǎn de jínàn-xiǎnzhòng guāntóu, jūnduì shǐzhōng shì rénmín zuì kě xìnlài de zhōngliú-dǐzhù.",
                "en": "A powerful modern army requires cutting-edge armaments alongside strict discipline and self-sacrificing spirit. During natural disasters and national perils, the armed forces remain the most trustworthy pillar protecting the people.",
                "es": "Un ejército moderno no solo exige armamento de punta, sino férrea disciplina y abnegación. Ante catástrofes naturales y graves crisis nacionales, las fuerzas armadas constituyen el baluarte más leal y firme de la ciudadanía."
            }
        ]
    },

    # 10 派
    {
        "id": "10",
        "hanzi": "派",
        "pinyin": "pài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to send; dispatch; assign; faction; school of thought",
            "es": "enviar; mandar; destinar; asignar; facción; escuela"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to dispatch, assign, or depute persons to perform a task, mission, or military duty",
                "definition_es": "enviar, comisionar o despachar a alguien para cumplir un cometido, misión o faena",
                "example_phrase": "派代表出席 (dispatch representatives to attend)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "赵王轻信了秦国散布的离间谣言，执意罢免廉颇，改派毫无实战经验的赵括统领大军前线作战。",
                "pinyin": "Zhàowáng qīngxìn le Qínguó sànbù de líjiàn yáoyán, zhíyì bàmǐan Lián Pō, gǎi pài háowú shízhàn jīngyàn de Zhào Kuò tǒnglǐng dàjūn qiánxiàn zuòzhàn.",
                "en": "Gullible to rumors spread by Qin, King Zhao insisted on dismissing Lian Po and sent inexperienced Zhao Kuo to command the front lines.",
                "es": "Creyendo los falsos rumores de Qin, el rey de Zhao cesó a Lian Po y mandó al frente al inexperto Zhao Kuo al mando de las tropas."
            },
            {
                "id": "#2",
                "hanzi": "得知地震灾区急需医疗救援后，省人民医院立即派出了第一批资深外科专家医疗队连夜奔赴前线。",
                "pinyin": "Dézhī dìzhèn zāiqū jíxū yīliáo jiùyuán hòu, shěng rénmín yīyuàn lìjí pài chū le dì-yī pī zīshēn wàikē zhuānjiā yīliáoduì liányè bēnfù qiánxiàn.",
                "en": "Learning that the earthquake disaster area urgently needed medical aid, the hospital immediately dispatched its first team of surgeons overnight.",
                "es": "Al conocerse la emergencia en la zona sísmica, el hospital provincial envió de inmediato un primer equipo de cirujanos esa misma noche."
            }
        ],
        "collocations": [
            {"hanzi": "派出代表", "en": "dispatch representatives"},
            {"hanzi": "派人前往", "en": "send someone over"},
            {"hanzi": "派遣专家", "en": "depute / dispatch experts"},
            {"hanzi": "分配任务", "en": "assign tasks / duties"},
            {"hanzi": "一派胡言", "en": "complete nonsense / pack of lies (classifier)"},
            {"hanzi": "各流各派", "en": "various factions and schools"}
        ],
        "idioms": [
            {"hanzi": "名门正派", "pinyin": "míng mén zhèng pài", "meaning_en": "reputable and orthodox school or lineage"},
            {"hanzi": "一派胡言", "pinyin": "yī pài hú yán", "meaning_en": "sheer nonsense; absurd drivel"},
            {"hanzi": "自成一派", "pinyin": "zì chéng yī pài", "meaning_en": "form a unique school of one's own"},
            {"hanzi": "差强人意", "pinyin": "chā qiáng rén yì", "meaning_en": "barely satisfactory; passable"}
        ],
        "character_decomposition": [
            {
                "character": "派",
                "pinyin": "pài",
                "meaning_en": "send; dispatch; branch of water; faction",
                "meaning_es": "enviar; mandar; ramal fluvial; facción",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water flow) + 𠂢 (river branching into tributary streams)",
                "sound_component": "𠂢 (pài)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Water 氵 branching off into several diverging river tributaries 𠂢; signifies sending out streams or people.",
                "visual_mnemonic_story_en": "A river stream (氵) branching out in diverging channels to carry boats to distant ports (派).",
                "visual_mnemonic_story_es": "El curso del río (氵) ramificándose en brazos de agua para enviar barcas a diversos rumbos (派).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "EHHV",
                "traditional": "派"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Water branching outward into separate channels (氵+𠂢) represents dispatching people outward on missions (派).",
            "composite_memory_hook_es": "El río que bifurca sus ramales hacia rumbos diversos (氵+𠂢) encarna la acción de enviar o comisionar (派).",
            "cultural_and_cognitive_roots": "Originates from hydrology meaning tributary branches of a main river, extended to philosophical schools (流派) and executive deputation.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'pài' (51). Crisp, decisive downward inflection."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "旅", "pinyin": "lǚ", "meaning_en": "travel; brigade", "distinction_note": "Square 方 on left instead of 氵"},
                {"character": "波", "pinyin": "bō", "meaning_en": "wave; ripple", "distinction_note": "Skin 皮 on right instead of 𠂢"},
                {"character": "泳", "pinyin": "yǒng", "meaning_en": "swim", "distinction_note": "Eternal 永 on right instead of 𠂢"},
                {"character": "河", "pinyin": "hé", "meaning_en": "river", "distinction_note": "Can 可 on right instead of 𠂢"}
            ],
            "etymological_cognates": [
                {"character": "派遣", "pinyin": "pàiqiǎn", "gloss_en": "dispatch; depute"},
                {"character": "流派", "pinyin": "liúpài", "gloss_en": "school of thought; sect"},
                {"character": "学派", "pinyin": "xuépài", "gloss_en": "academic school"},
                {"character": "委派", "pinyin": "wěipài", "gloss_en": "appoint; assign"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "派 as a verb highlights authoritative or organizational dispatch of personnel on designated tasks.",
            "contrasts": [
                {"id": 1, "compared_word": "派 vs. 送", "pinyin": "sòng", "analysis": "送 implies delivering an object or escorting someone off, while 派 means assigning someone on an official mission."},
                {"id": 2, "compared_word": "派 vs. 遣", "pinyin": "qiǎn", "analysis": "遣 is formal literary (often paired as 派遣), while 派 is ubiquitous in both spoken and written Chinese."},
                {"id": 3, "compared_word": "派 vs. 留", "pinyin": "liú", "analysis": "留 is the direct antonym meaning to detain, keep in place, or retain."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "长平之战前夕，秦相范雎用重金派间谍潜入赵国，四处散布“秦军最惧怕赵括”的谣言。缺乏政治远见的赵王果然中计，不顾群臣强烈反对，执意派赵括代替廉颇出征，这一昏庸决策最终铸成了无法挽回的亡国悲剧。",
                "pinyin": "Chángpíng zhī zhàn qiánxī, Qínxiàng Fàn Jū yòng zhòngjīn pài jiàndié qiánrù Zhàoguó, sìchù sànbù 'Qínjūn zuì jùpà Zhào Kuò' de yáoyán. Quēfá zhèngzhì yuǎnjiàn de Zhàowáng guǒrán zhòngjì, bùgù qúnchén qiángliè fǎnduì, zhíyì pài Zhào Kuò dàitì Lián Pō chūzhēng, zhè yī hūnyōng juécè zuìzhōng zhùchéng le wúfǎ-wǎnhuí de wángguó bēijù.",
                "en": "On the eve of Changping, Qin's minister bribed spies to enter Zhao and spread rumors that 'Qin feared only Zhao Kuo.' Blindly duped, King Zhao insisted on dispatching Zhao Kuo to replace Lian Po, sealing a tragic catastrophe.",
                "es": "Antes de Changping, el primer ministro de Qin sobornó espías para difundir que Qin solo temía a Zhao Kuo. El crédulo monarca de Zhao cayó en la trampa y envió a Zhao Kuo al relevo, consumando una tragedia irreparable."
            },
            {
                "id": "#2",
                "hanzi": "在现代企业战略管理中，合理选拔与准确派任核心业务骨干，是项目克难制胜的首要关键。管理者必须知人善任，绝不能任人唯亲或盲目指派，唯有派最合适、最有实战能力的人奔赴攻坚战场，才能确保团队战无不胜。",
                "pinyin": "Zài xiàndài qǐyè zhànlüè guǎnlǐ zhōng, hélǐ xuǎnbá yǔ zhǔnquè pàirèn héxīn yèwù gǔgàn, shì xiàngmù kènán-zhìshèng de shǒuyào guānjiàn. Guǎnlǐzhě bìxū zhīrén-shànrèn, juébùnéng rènrén-wéiqīn huò mángmù zhǐpài, wéiyǒu pài zuì héshì, zuì yǒu shízhàn nénglì de rén bēnfù gōngjiān zhànchǎng, cái néng quèbǎo tuánduì zhànwúbùshèng.",
                "en": "In modern corporate strategy, selecting and dispatching key professionals is essential for project triumph. Managers must appoint candidates based on tested ability rather than favoritism, sending capable people to lead tasks to victory.",
                "es": "En la gestión empresarial moderna, comisionar con acierto a los perfiles idóneos resulta determinante. Los directivos deben asignar cometidos por mérito y solvencia probada; enviar a los más aptos garantiza el éxito de los proyectos."
            }
        ]
    }
]

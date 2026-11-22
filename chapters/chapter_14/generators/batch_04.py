# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch4 = [
    # 31 关闭
    {
        "id": "31",
        "hanzi": "关闭",
        "pinyin": "guān bì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to close; shut; shut down; turn off",
            "es": "cerrar; clausurar; apagar; desconectar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to close doors, windows, valves, or operations of a facility or business",
                "definition_es": "cerrar puertas, ventanas, válvulas o clausurar la actividad de un local o negocio",
                "example_phrase": "关闭大门 (close the main gate)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "夜幕降临之后，四合院厚重的朱红大门缓缓关闭，院内立刻变成了一个安静的世界。",
                "pinyin": "Yèmù jiànglín zhīhòu, sìhéyuàn hòuzhòng de zhūhóng dàmén huǎnhuǎn guānbì, yuànnèi lìkè biànchéng le yī gè ānjìng de shìjiè.",
                "en": "After nightfall, the thick vermilion gate of the courtyard slowly closed, immediately turning the compound into a tranquil world.",
                "es": "Al caer la noche, el pesado portón bermellón del siheyuan se cerró con lentitud, convirtiendo el patio en un remanso de quietud."
            },
            {
                "id": "#2",
                "hanzi": "由于需要进行全面的设备检修与系统升级，该图书馆将临时关闭三天。",
                "pinyin": "Yóuyú xūyào jìnxíng quánmiàn de shèbèi jiǎnxiū yǔ xìtǒng shēngjí, gāi túshūguǎn jiāng línshí guānbì sān tiān.",
                "en": "Owing to necessary comprehensive equipment overhaul and system upgrades, the library will temporarily close for three days.",
                "es": "Debido a labores integrales de mantenimiento y actualización de sistemas, la biblioteca cerrará temporalmente durante tres días."
            }
        ],
        "collocations": [
            {"hanzi": "关闭门窗", "en": "close doors and windows"},
            {"hanzi": "关闭电源", "en": "turn off power supply"},
            {"hanzi": "临时关闭", "en": "temporarily close / shut"},
            {"hanzi": "永久关闭", "en": "permanently shut down"},
            {"hanzi": "自动关闭", "en": "shut off automatically"},
            {"hanzi": "关闭通道", "en": "close the corridor / channel"}
        ],
        "idioms": [
            {"hanzi": "闭门造车", "pinyin": "bì mén zào chē", "meaning_en": "build a cart behind closed doors; divorce oneself from reality"},
            {"hanzi": "夜不闭户", "pinyin": "yè bù bì hù", "meaning_en": "doors unbolted at night; state of great peace and honesty"},
            {"hanzi": "闭门思过", "pinyin": "bì mén sī guò", "meaning_en": "shut doors to reflect on one's past errors"},
            {"hanzi": "紧闭双眼", "pinyin": "jǐn bì shuāng yǎn", "meaning_en": "close both eyes tightly"}
        ],
        "character_decomposition": [
            {
                "character": "关",
                "pinyin": "guān",
                "meaning_en": "close; shut; pass; barrier; concern",
                "meaning_es": "cerrar; paso; frontera; concernir",
                "radical": "丷",
                "radical_meaning_en": "horns / split",
                "meaning_component": "horizontal wooden crossbar locking two gate leaves",
                "sound_component": "关 (guān)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "A heavy wooden beam bolted across gateway doors to close and seal off entry.",
                "visual_mnemonic_story_en": "Bolting a thick wooden crossbar across the gateway to close the entrance (关).",
                "visual_mnemonic_story_es": "Cruzar un pesado trinquete de madera sobre el portón para cerrar el paso (关).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "TUK",
                "traditional": "關"
            },
            {
                "character": "闭",
                "pinyin": "bì",
                "meaning_en": "shut; close; block; conclude",
                "meaning_es": "cerrar; clausurar; obstruir; concluir",
                "radical": "门",
                "radical_meaning_en": "door / gate",
                "meaning_component": "门 (double-leaf gateway) + 才 (wooden bar/stake locking it)",
                "sound_component": "闭 (bì)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Placing a locking bar inside the frame of double doors 门; to shut tightly.",
                "visual_mnemonic_story_en": "Swinging the heavy wooden doors (门) shut and fastening the lock (闭).",
                "visual_mnemonic_story_es": "Ajustar las dos hojas del portón (门) asegurando el cerrojo (闭).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LND",
                "traditional": "閉"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Bolting the gateway bar (关) and shutting the double doorleaves (闭) means to close (关闭).",
            "composite_memory_hook_es": "Echar el cerrojo del zaguán (关) y ajustar ambas hojas (闭) define la acción de cerrar (关闭).",
            "cultural_and_cognitive_roots": "Originates from ancient city fortification and compound gate locking rites to protect domestic privacy and defense.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'guān bì' (55-51). High steady pitch on 'guān', followed by a decisive drop on 'bì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "开", "pinyin": "kāi", "meaning_en": "open; begin", "distinction_note": "Lacks the upper diagonal tick marks of 关"},
                {"character": "天", "pinyin": "tiān", "meaning_en": "sky; day", "distinction_note": "Horizontal line across 大 instead of upper dots"},
                {"character": "闪", "pinyin": "shǎn", "meaning_en": "flash; dodge", "distinction_note": "Person radical 人 inside 门 instead of 才"},
                {"character": "问", "pinyin": "wèn", "meaning_en": "ask; question", "distinction_note": "Mouth radical 口 inside 门 instead of 才"}
            ],
            "etymological_cognates": [
                {"character": "关门", "pinyin": "guānmén", "gloss_en": "close the door; go out of business"},
                {"character": "闭幕", "pinyin": "bìmù", "gloss_en": "conclude; curtain falls"},
                {"character": "关注", "pinyin": "guānzhù", "gloss_en": "pay close attention to"},
                {"character": "封闭", "pinyin": "fēngbì", "gloss_en": "seal off; secluded"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "关闭 is the universal term for physical closing (doors, valves, screens) or administrative shutdowns.",
            "contrasts": [
                {"id": 1, "compared_word": "关闭 vs. 开启", "pinyin": "kāiqǐ", "analysis": "开启 is the direct antonym meaning to open, unlock, or power on."},
                {"id": 2, "compared_word": "关闭 vs. 封闭", "pinyin": "fēngbì", "analysis": "关闭 simply shuts access, whereas 封闭 seals off an area completely into seclusion or isolation."},
                {"id": 3, "compared_word": "关闭 vs. 停业", "pinyin": "tíngyè", "analysis": "停业 specifically means suspending business trade, while 关闭 has broader physical and mechanical applications."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的广亮大门非常讲究。每当夜幕降临，院里的大门便准时关闭并插上坚固的门栓。大门一经关闭，就把外界长巷的纷繁喧嚣完全阻隔在外，为院内聚居的大家族守护着一份恬静私密的天地。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de guǎngliàng dàmén fēicháng jiǎngjiu. Měi dāng yèmù jiànglín, yuàn lǐ de dàmén biàn zhǔnshí guānbì bìng chā shang jiāngù de ménshuān. Dàmén yījīng guānbì, jiù bǎ wàijiè chángxiàng de fēnfán xuānxīao wánquán zǔgé zài wài, wèi yuànnèi jùjū de dàjiātíng shǒuhù zhe yī fèn tiánjìng sìmì de tiāndì.",
                "en": "The grand gate of old Beijing courtyards followed strict customs. At nightfall, the entrance was punctually closed and barred. Once closed, outside alley clamor was sealed out, protecting a serene and private domestic world for the family.",
                "es": "El portalón señorial del siheyuan pekinés seguía venerables normas. Al caer el crepúsculo, se cerraba con puntualidad pasando la tranca. Una vez cerrado, el bullicio quedaba fuera, salvaguardando un remanso íntimo para el hogar."
            },
            {
                "id": "#2",
                "hanzi": "在工业生产与实验操作中，严格遵守关闭程序是保障安全的关键。无论是化工厂切断高压气阀，还是实验室关闭精密设备电源，每一个关闭步骤都必须按照操作手册逐一核对，确保人员和财产万无一失。",
                "pinyin": "Zài gōngyè shēngchǎn yǔ shíyàn cāozuò zhōng, yángé zūnshǒu guānbì chéngxù shì bǎozhàng ānquán de guānjiàn. Wúlùn shì huàgōngchǎng qiēduàn gāoyā qìfá, háishì shíyànshì guānbì jīngmì shèbèi diànyuán, měi yī gè guānbì bùzhòu dōu bìxū ànzhào cāozuò shǒucè zhúyī héduì, quèbǎo rényuán hé cáichǎn wànwúyīshī.",
                "en": "In industrial production and laboratory work, strictly observing shut-down protocols is vital for safety. Whether isolating high-pressure valves or powering down precision units, every step must be verified to prevent accidents.",
                "es": "En faenas fabriles y de laboratorio, observar los protocolos de cierre resulta indispensable para la seguridad. Ya sea aislar válvulas de gas o apagar equipos sensibles, cada paso debe cotejarse para garantizar la protección común."
            }
        ]
    },

    # 32 封闭
    {
        "id": "32",
        "hanzi": "封闭",
        "pinyin": "fēng bì",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to seal; close off; secluded; isolated; insular",
            "es": "sellar; aislar; clausurar; cerrado al exterior; incomunicado"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to seal completely so as to prevent entry, exit, or air leakage; to close off from outside contact",
                "definition_es": "sellar herméticamente impidiendo el paso o la comunicación; aislar del exterior",
                "example_phrase": "封闭式管理 (closed / sequestered management)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院这种封闭式的建筑格局，既保证了内部生活的私密安全，又营造出独立的院落世界。",
                "pinyin": "Sìhéyuàn zhè zhǒng fēngbìshì de jiànzhù géjú, jì bǎozhèng le nèibù shēnghuó de sìmì ānquán, yòu yíngzào chū dúlì de yuànluò shìjiè.",
                "en": "The enclosed architectural layout of courtyards guaranteed interior privacy and safety while forging an independent courtyard universe.",
                "es": "La traza cerrada y hermética del siheyuan aseguraba la privacidad de la vida familiar a la par que forjaba un micromundo independiente."
            },
            {
                "id": "#2",
                "hanzi": "受强暴风雪恶劣天气影响，通往山区景区的多条高速公路已被交警部门临时封闭。",
                "pinyin": "Shòu qiáng bàofēngxuě èliè tiānqì yǐngxiǎng, tōngwǎng shānqū jǐngqū de duō tiáo gāosù gōnglù yǐ bèi jiāojǐng bùmén línshí fēngbì.",
                "en": "Affected by severe blizzards, several highways leading to the mountain scenic area have been temporarily closed by traffic police.",
                "es": "Debido a las intensas ventiscas, la policía de tráfico clausuró temporalmente varias autovías que conducen a la zona montañosa."
            }
        ],
        "collocations": [
            {"hanzi": "封闭式管理", "en": "closed-loop management"},
            {"hanzi": "封闭道路", "en": "close off roads"},
            {"hanzi": "自我封闭", "en": "self-enclosure / introverted isolation"},
            {"hanzi": "严密封闭", "en": "tightly sealed off"},
            {"hanzi": "封闭环境", "en": "closed / isolated environment"},
            {"hanzi": "封闭空间", "en": "enclosed space"}
        ],
        "idioms": [
            {"hanzi": "固步自封", "pinyin": "gù bù zì fēng", "meaning_en": "stand still and cease progress; rest on laurels"},
            {"hanzi": "闭关锁国", "pinyin": "bì guān suǒ guó", "meaning_en": "close passes and lock ports; self-imposed national isolation"},
            {"hanzi": "风雨不透", "pinyin": "fēng yǔ bù tòu", "meaning_en": "sealed so tightly that neither wind nor rain penetrates"},
            {"hanzi": "深居简出", "pinyin": "shēn jū jiǎn chū", "meaning_en": "live in secluded retirement, rarely venturing out"}
        ],
        "character_decomposition": [
            {
                "character": "封",
                "pinyin": "fēng",
                "meaning_en": "seal; confer; envelope; boundary",
                "meaning_es": "sellar; conferir; sobre; frontera",
                "radical": "寸",
                "radical_meaning_en": "inch / measurement",
                "meaning_component": "圭 (earth mounds marking boundaries) + 寸 (ruling hand)",
                "sound_component": "封 (fēng)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Planting trees or heaping mounds of earth 圭 with one's hand 寸 to mark a sealed territorial boundary.",
                "visual_mnemonic_story_en": "Using official authority (寸) to raise border boundary mounds (圭) sealing an estate (封).",
                "visual_mnemonic_story_es": "Erguir mojones de tierra (圭) con mano soberana (寸) para delimitar y sellar un territorio (封).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "GDI",
                "traditional": "封"
            },
            {
                "character": "闭",
                "pinyin": "bì",
                "meaning_en": "close; shut; conclude; obstruct",
                "meaning_es": "cerrar; clausurar; concluir; obstruir",
                "radical": "门",
                "radical_meaning_en": "gate / door",
                "meaning_component": "门 (double-leaf gateway) + 才 (locking bolt)",
                "sound_component": "闭 (bì)",
                "stroke_count": 6,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Double doorleaves 门 barred shut with a wooden lock 才; to close tightly.",
                "visual_mnemonic_story_en": "Fastening a solid bolt across gate leaves (门) to close them shut (闭).",
                "visual_mnemonic_story_es": "Correr el pasador sobre ambas hojas (门) para dejarlas bien cerradas (闭).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "LND",
                "traditional": "閉"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Raising a perimeter boundary seal (封) and barring the gates (闭) creates an isolated enclosure (封闭).",
            "composite_memory_hook_es": "Levantar un cerco perimetral (封) y echar el cerrojo (闭) aísla el recinto del exterior (封闭).",
            "cultural_and_cognitive_roots": "Captures the architectural ethos of northern Chinese homesteads prioritizing domestic enclosure against steppes winds and banditry.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'fēng bì' (55-51). High sustained pitch on 'fēng', followed by a sharp drop on 'bì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "射", "pinyin": "shè", "meaning_en": "shoot; emit", "distinction_note": "Body radical 身 on left instead of 圭"},
                {"character": "对", "pinyin": "duì", "meaning_en": "correct; towards", "distinction_note": "Hand/again radical 又 on left instead of 圭"},
                {"character": "闲", "pinyin": "xián", "meaning_en": "leisure; idle", "distinction_note": "Wood radical 木 inside 门 instead of 才"},
                {"character": "闹", "pinyin": "nào", "meaning_en": "noisy; hustle", "distinction_note": "Market radical 市 inside 门 instead of 才"}
            ],
            "etymological_cognates": [
                {"character": "封锁", "pinyin": "fēngsuǒ", "gloss_en": "blockade; seal off"},
                {"character": "封存", "pinyin": "fēngcún", "gloss_en": "seal up for safekeeping"},
                {"character": "闭合", "pinyin": "bìhé", "gloss_en": "close up; seal tightly"},
                {"character": "禁闭", "pinyin": "jìnbì", "gloss_en": "confinement; solitary"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "封闭 describes complete seclusion, impenetrable sealing, or psychological insularity cutoff from external access.",
            "contrasts": [
                {"id": 1, "compared_word": "封闭 vs. 开放", "pinyin": "kāifàng", "analysis": "开放 is the direct antonym meaning open, transparent, and welcoming of external exchange."},
                {"id": 2, "compared_word": "封闭 vs. 关闭", "pinyin": "guānbì", "analysis": "关闭 merely refers to swinging a door shut, while 封闭 implies complete systemic isolation or sealing."},
                {"id": 3, "compared_word": "封闭 vs. 保守", "pinyin": "bǎoshǒu", "analysis": "保守 refers to ideological reluctance to change, whereas 封闭 stresses lack of communication or external connection."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "四合院的封闭特征源于古代中国人对家庭安全与安宁的追求。朝向胡同的外墙厚重坚实、极少开窗，整座院落形成了一个对外封闭、对内开放的私密空间。这种内敛的建筑品格，深刻折射出传统文化的含蓄内敛。",
                "pinyin": "Sìhéyuàn de fēngbì tèzhēng yuányú gǔdài Zhōngguó rén duì jiātíng ānquán yǔ ānníng de zhuīqiú. Cháoxiàng hútòng de wàiqiáng hòuzhòng jiānshí, jí shǎo kāichuāng, zhěng zuò yuànluò xíngchéng le yī gè duìwài fēngbì, duì nèi kāifàng de sìmì kōngjiān. Zhè zhǒng nèiliǎn de jiànzhù pǐngé, shēnkè zhéshè chū chuántǒng wénhuà de hánxù-nèiliǎn.",
                "en": "The enclosed trait of courtyards stemmed from ancient pursuit of family safety and serenity. Exterior walls facing alleys were thick without windows, forging an introverted space sealed outwardly but open inwardly to clan members.",
                "es": "El carácter hermético del siheyuan nació del anhelo de paz y resguardo familiar. Sus gruesos muros exteriores apenas tenían vanos, forjando un espacio cerrado al exterior pero volcado hacia el patio interior con discreta sobriedad."
            },
            {
                "id": "#2",
                "hanzi": "在快速发展的现代社会中，任何一个组织或个人如果长期处于自我封闭的状态，就必然会错失时代发展的机遇。只有主动打破封闭的思想藩篱，广泛与外界交流合作，吸纳先进的思想理念，才能在时代浪潮中保持蓬勃活力。",
                "pinyin": "Zài kuàisù fāzhǎn de xiàndài shèhuì zhōng, rènhé yī gè zǔzhī huò gèrén rúguǒ chángqī chǔyú zìwǒ fēngbì de zhuàngtài, jiù bìrán huì cuòshī shídài fāzhǎn de jīyù. Zhǐyǒu zhǔdòng dǎpò fēngbì de sīxiǎng fānlí, guǎngfàn yǔ wàijiè jiāoliú hézuò, xīnà xiānjìn de sīxiǎng lǐniàn, cái néng zài shídài làngcháo zhōng bǎochí péngbó huólì.",
                "en": "In fast-paced modern society, organizations or individuals lingering in self-enclosure inevitably miss historical opportunities. Only by dismantling closed dogmas and welcoming open collaboration can one sustain vibrant vitality in times of change.",
                "es": "En la sociedad actual, quien se recluye en el aislamiento pierde el compás del progreso. Solo derribando barreras mentales y abriéndose a la cooperación y al intercambio de saberes es posible preservar la lozanía ante los retos del porvenir."
            }
        ]
    },

    # 33 打交道
    {
        "id": "33",
        "hanzi": "打交道",
        "pinyin": "dǎ jiāo dao",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to deal with; come into contact with; interact with",
            "es": "tratar con; relacionarse con; tener trato con"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to have social contact, business relations, or interpersonal dealings with someone",
                "definition_es": "mantener trato frecuente, relación social o comercial con personas o instituciones",
                "example_phrase": "跟邻居打交道 (interact with neighbors)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "住在北京老胡同四合院里的人们，每天抬头不见低头见，常常与街坊邻里热情地打交道。",
                "pinyin": "Zhù zài Běijīng lǎo hútòng sìhéyuàn lǐ de rénmen, měitiān táitóu bù jiàn dītóu jiàn, chángcháng yǔ jiēfang línlǐ rèqíng de dǎ jiāodao.",
                "en": "Living in old Beijing alley courtyards, people crossed paths daily and interacted warmly with neighborhood peers.",
                "es": "Los vecinos de los viejos callejones de Pekín, encontrándose a cada paso, mantenían un trato cordial y diario con la vecindad."
            },
            {
                "id": "#2",
                "hanzi": "作为一名涉外商务谈判代表，他经常需要与来自不同文化背景的国际客户打交道。",
                "pinyin": "Zuòwéi yī míng shèwài shāngwù tánpàn dàibiǎo, tā jīngcháng xūyào yǔ láizì bùtóng wénhuà bèijǐng de guójì kèhù dǎ jiāodao.",
                "en": "As an international business negotiator, he frequently needs to deal with global clients from diverse cultural backgrounds.",
                "es": "Como negociador comercial internacional, a menudo debe tratar con clientes de diversos trasfondos culturales."
            }
        ],
        "collocations": [
            {"hanzi": "跟……打交道", "en": "deal with / interact with ..."},
            {"hanzi": "不愿打交道", "en": "unwilling to deal with"},
            {"hanzi": "长期打交道", "en": "deal with over the long term"},
            {"hanzi": "打交道的方式", "en": "manner of dealing with people"},
            {"hanzi": "经常打交道", "en": "frequently interact with"},
            {"hanzi": "打交道的经验", "en": "experience in dealing with others"}
        ],
        "idioms": [
            {"hanzi": "礼尚往来", "pinyin": "lǐ shàng wǎng lái", "meaning_en": "courtesy demands reciprocity; return of goodwill"},
            {"hanzi": "和睦相处", "pinyin": "hé mù xiāng chǔ", "meaning_en": "live together in peace and harmony"},
            {"hanzi": "八面玲珑", "pinyin": "bā miàn líng lóng", "meaning_en": "smooth and tactful in dealing with everyone"},
            {"hanzi": "打成一片", "pinyin": "dǎ chéng yī piàn", "meaning_en": "merge completely with the masses; become one with"}
        ],
        "character_decomposition": [
            {
                "character": "打",
                "pinyin": "dǎ",
                "meaning_en": "hit; engage in; do; play; beat",
                "meaning_es": "golpear; hacer; practicar; entablar",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (active hand action) + 丁 (striking nail / peg)",
                "sound_component": "丁 (dīng)",
                "stroke_count": 5,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A hand 扌 driving a nail 丁; evolved into a versatile verbal prefix for initiating activities.",
                "visual_mnemonic_story_en": "Using hands (扌) to initiate and forge dynamic social activities (打).",
                "visual_mnemonic_story_es": "Mover las manos (扌) para emprender con soltura cualquier actividad social (打).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "QM",
                "traditional": "打"
            },
            {
                "character": "交",
                "pinyin": "jiāo",
                "meaning_en": "cross; intersect; associate; exchange",
                "meaning_es": "cruzar; intercambiar; asociarse; trato",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "pictograph of a person crossing their legs in dance or barter",
                "sound_component": "交 (jiāo)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A person standing with crossed legs; signifies mutual intersecting exchange and social relations.",
                "visual_mnemonic_story_en": "Paths crossing and intersecting gracefully to form warm friendships (交).",
                "visual_mnemonic_story_es": "Caminos que se cruzan armónicamente para forjar relaciones y amistades (交).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YCK",
                "traditional": "交"
            },
            {
                "character": "道",
                "pinyin": "dao",
                "meaning_en": "way; path; principle; channel",
                "meaning_es": "camino; vía; doctrina; sendero",
                "radical": "辶",
                "radical_meaning_en": "walk / movement",
                "meaning_component": "辶 (movement on path) + 首 (head directing vision)",
                "sound_component": "首 (shǒu)",
                "stroke_count": 12,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Walking 辶 with a clear head 首 guiding one along the proper path; here part of colloquial compound.",
                "visual_mnemonic_story_en": "Walking thoughtfully with an enlightened head (首) along life's shared path (道).",
                "visual_mnemonic_story_es": "Caminar con la cabeza despejada (首) siguiendo el sendero del entendimiento mutuo (道).",
                "tone_mnemonic_anchor": "neutral",
                "cangjie": "YHUT",
                "traditional": "道"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Engaging in hands-on action (打) to build mutual paths of connection (交道) means to deal with people (打交道).",
            "composite_memory_hook_es": "Poner manos a la obra (打) para tender senderos de intercambio (交道) significa tener trato con alguien (打交道).",
            "cultural_and_cognitive_roots": "Essential colloquial idiom reflecting the bustling warmth and tact of urban Beijing neighborhood and bazaar culture.",
            "tone_sandhi_and_pitch_modulation": "Third tone to first tone to neutral: 'dǎ jiāo dao' (214-55-neutral). Dip on 'dǎ', stay level on 'jiāo', and conclude lightly on 'dao'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "订", "pinyin": "dìng", "meaning_en": "order; book", "distinction_note": "Speech radical 讠 beside 丁 instead of 扌"},
                {"character": "父", "pinyin": "fù", "meaning_en": "father", "distinction_note": "Crossed strokes without lid 亠 on top"},
                {"character": "选", "pinyin": "xuǎn", "meaning_en": "choose", "distinction_note": "First radical 先 under 辶 instead of 首"},
                {"character": "通", "pinyin": "tōng", "meaning_en": "through; pass", "distinction_note": "Yong radical 甬 under 辶 instead of 首"}
            ],
            "etymological_cognates": [
                {"character": "交往", "pinyin": "jiāowǎng", "gloss_en": "associate with; interact"},
                {"character": "交流", "pinyin": "jiāoliú", "gloss_en": "exchange; communicate"},
                {"character": "打了招呼", "pinyin": "dǎ le zhāohu", "gloss_en": "greeted; said hello"},
                {"character": "道路", "pinyin": "dàolù", "gloss_en": "road; path; route"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "打交道 is an idiomatic verb phrase describing ongoing interpersonal contact, working relations, or everyday transactions.",
            "contrasts": [
                {"id": 1, "compared_word": "打交道 vs. 交流", "pinyin": "jiāoliú", "analysis": "交流 focuses on exchanging information or feelings, whereas 打交道 covers pragmatic daily interaction and business dealings."},
                {"id": 2, "compared_word": "打交道 vs. 往来", "pinyin": "wǎnglái", "analysis": "往来 can refer to physical traffic or written letters, while 打交道 is personal face-to-face or working contact."},
                {"id": 3, "compared_word": "打交道 vs. 隔绝", "pinyin": "géjué", "analysis": "隔绝 is the direct antonym meaning completely severed from contact or dealings."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的生活充满了浓浓的人情味。院里的邻居们不仅同在一个水龙头下洗菜洗衣服，更常常在庭院中热情打交道。谁家做了解暑绿豆汤，总会盛上一碗端给街坊；这种淳朴真诚的打交道方式，温暖了几代人。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de shēnghuó chōngmǎn le nóngnóng de rénqíngwèi. Yuàn lǐ de línjū men bùjǐn tóng zài yī gè shuǐlóngtóu xià xǐ cài xǐ yīfu, gèng chángcháng zài tíngyuàn zhōng rèqíng dǎ jiāodao. Shuí jiā zuò le jiěshǔ lǜdòutāng, zǒng huì chéng shang yī wǎn duān gěi jiēfang; zhè zhǒng chúnpǔ zhēnchéng de dǎ jiāodao fāngshì, wēnnuǎn le jǐ dài rén.",
                "en": "Courtyard life in old Beijing overflowed with human warmth. Neighbors sharing a water tap interacted with sincere cordiality. Whoever cooked mung bean soup shared a bowl across the yard; this heartfelt interaction warmed generations.",
                "es": "La vida en el siheyuan pekinés rebosaba de calor humano. Los vecinos, compartiendo la fuente común, mantenían un trato solícito; si alguien cocinaba sopa fresca, ofrecía un tazón a la vecindad, uniendo a generaciones con afecto sincero."
            },
            {
                "id": "#2",
                "hanzi": "在现代社会中，如何与形形色色的人友好打交道，是一门极其重要的处世智慧。无论是与职场同事协作推进项目，还是在跨文化舞台上与海外商业伙伴商务谈判，学会换位思考、真诚待人，才能在打交道中赢得长久的尊重与深厚的互信。",
                "pinyin": "Zài xiàndài shèhuì zhōng, rúhé yǔ xíngxíng-sèsè de rén yǒuhǎo dǎ jiāodao, shì yī mén jíqí zhòngyào de chǔshì zhìhuì. Wúlùn shì yǔ zhíchǎng tóngshì xiézuò tuījìn xiàngmù, háishì zài kuà wénhuà wǔtái shang yǔ hǎiwài shāngyè huǒbàn shāngwù tánpàn, xuéhuì huànwèi sīkǎo, zhēnchéng dàirén, cái néng zài dǎ jiāodao zhōng yíngdé chángjiǔ de zūnzhòng yǔ shēnhòu de hùxìn.",
                "en": "In modern society, dealing amiably with diverse people is vital social wisdom. Whether coordinating team projects or negotiating with foreign business partners, empathy and sincerity are prerequisites for earning enduring respect and trust.",
                "es": "En el mundo contemporáneo, saber relacionarse con toda clase de personas es un arte primordial. Ya sea colaborando con colegas o negociando con socios internacionales, la empatía y la franqueza ganan respeto y confianza duraderos."
            }
        ]
    },

    # 34 日子
    {
        "id": "34",
        "hanzi": "日子",
        "pinyin": "rì zi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "days; date; livelihood; daily life",
            "es": "días; fecha; vida cotidiana; subsistencia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the passage of days; a particular date; one's livelihood and domestic quality of life",
                "definition_es": "el transcurso de las jornadas; fecha señalada; condición de subsistencia y vida diaria",
                "example_phrase": "日子过得红火 (living a prosperous and thriving life)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "老北京四合院里的居民们互相照应、和睦相处，把平平淡淡的寻常日子过得有滋有味。",
                "pinyin": "Lǎo Běijīng sìhéyuàn lǐ de jūmín men hùxiāng zhàoying, hémù xiāngchǔ, bǎ píngpíng-dàndàn de xúncháng rìzi guò de yǒuzī-yǒuwèi.",
                "en": "Residents in Beijing courtyards cared for each other in harmony, filling ordinary routine days with flavor and zest.",
                "es": "Los vecinos del siheyuan pekinés se ayudaban en armonía, llenando de sazón y alegría el transcurso de los días sencillos."
            },
            {
                "id": "#2",
                "hanzi": "转眼之间，大学毕业离校的日子即将来临，同学们依依不舍地合影留念。",
                "pinyin": "Zhuǎnyǎn zhījiān, dàxué bìyè líxiào de rìzi jíjiāng láilín, tóngxué men yīyī-bùshě de héyǐng liúniàn.",
                "en": "In the blink of an eye, the date for college graduation was drawing near, and classmates reluctantly posed for farewell photos.",
                "es": "En un abrir y cerrar de ojos, la fecha de graduación universitaria se aproximaba y los compañeros se fotografiaban con nostalgia."
            }
        ],
        "collocations": [
            {"hanzi": "过日子", "en": "live one's life / manage domestic life"},
            {"hanzi": "好日子", "en": "good life / happy days"},
            {"hanzi": "日子过得充实", "en": "living fulfilling days"},
            {"hanzi": "苦日子", "en": "hard times / days of hardship"},
            {"hanzi": "特别的日子", "en": "special date / memorable day"},
            {"hanzi": "日子一天天过去", "en": "days slipping by one by one"}
        ],
        "idioms": [
            {"hanzi": "度日如年", "pinyin": "dù rì rú nián", "meaning_en": "a day dragged out like a year; enduring agony"},
            {"hanzi": "良辰吉日", "pinyin": "liáng chén jí rì", "meaning_en": "propitious moment and auspicious date"},
            {"hanzi": "旷日持久", "pinyin": "kuàng rì chí jiǔ", "meaning_en": "protracted and drawn out over many days"},
            {"hanzi": "指日可待", "pinyin": "zhǐ rì kě dài", "meaning_en": "can be anticipated in the near future; just around the corner"}
        ],
        "character_decomposition": [
            {
                "character": "日",
                "pinyin": "rì",
                "meaning_en": "sun; day; daily",
                "meaning_es": "sol; día; diario",
                "radical": "日",
                "radical_meaning_en": "sun / day",
                "meaning_component": "pictograph of sun with a dark central core",
                "sound_component": "日 (rì)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictograph of the round radiant sun marking diurnal cycles.",
                "visual_mnemonic_story_en": "The shining sun (日) rising day after day to illuminate life.",
                "visual_mnemonic_story_es": "El sol refulgente (日) que asciende cada mañana pautando el fluir vital.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "A",
                "traditional": "日"
            },
            {
                "character": "子",
                "pinyin": "zi",
                "meaning_en": "noun suffix; child; son",
                "meaning_es": "sufijo nominal; hijo; infante",
                "radical": "子",
                "radical_meaning_en": "child",
                "meaning_component": "pictograph of an infant swaddled with outstretched arms",
                "sound_component": "子 (zǐ)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "An infant baby waving arms; serves as a universal nominalizing suffix in everyday vernacular.",
                "visual_mnemonic_story_en": "A cheerful baby extending welcoming hands (子).",
                "visual_mnemonic_story_es": "Una criatura sonriente con los brazos en alto (子).",
                "tone_mnemonic_anchor": "neutral",
                "cangjie": "ND",
                "traditional": "子"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Sun-marked days (日) combined with the nominal suffix (子) gives the common word for everyday life and dates (日子).",
            "composite_memory_hook_es": "La cuenta de los soles (日) unida al sufijo coloquial (子) conforma el transcurso de la vida y los días (日子).",
            "cultural_and_cognitive_roots": "Deeply emotional colloquial word encapsulating domestic struggle, frugal management ('过日子'), and festive celebrations.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone to neutral tone: 'rì zi' (51-neutral). Articulate 'rì' with downward emphasis, letting 'zi' fall lightly."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "目", "pinyin": "mù", "meaning_en": "eye; item", "distinction_note": "Two inner horizontal bars instead of one"},
                {"character": "白", "pinyin": "bái", "meaning_en": "white; clear", "distinction_note": "Has an upper diagonal tick mark on top"},
                {"character": "月", "pinyin": "yuè", "meaning_en": "moon; month", "distinction_note": "Curved crescent strokes instead of square box"},
                {"character": "田", "pinyin": "tián", "meaning_en": "field", "distinction_note": "Crossed grid strokes inside 囗 frame"}
            ],
            "etymological_cognates": [
                {"character": "时光", "pinyin": "shíguāng", "gloss_en": "time; years; days"},
                {"character": "日月", "pinyin": "rìyuè", "gloss_en": "sun and moon; passage of time"},
                {"character": "生计", "pinyin": "shēngjì", "gloss_en": "livelihood; living"},
                {"character": "光阴", "pinyin": "guāngyīn", "gloss_en": "fleeting time; days"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "日子 functions colloquially for both a calendar date and one's qualitative domestic livelihood/lifestyle.",
            "contrasts": [
                {"id": 1, "compared_word": "日子 vs. 日期", "pinyin": "rìqī", "analysis": "日期 is formal and strictly refers to a calendar date (year/month/day), while 日子 covers life and livelihood."},
                {"id": 2, "compared_word": "日子 vs. 生活", "pinyin": "shēnghuó", "analysis": "生活 is formal and broad (career, culture, biology), while 过日子 specifically means managing domestic chores and household expenses."},
                {"id": 3, "compared_word": "日子 vs. 时间", "pinyin": "shíjiān", "analysis": "时间 measures hours and chronological duration, whereas 日子 evokes lived domestic experience."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "在老北京的四合院里，“过日子”是一门充满温情的艺术。春日扫落花，夏夜纳凉风，秋日摘红枣，冬日煨暖炉。邻里之间借一把葱、添一勺油，朴素的柴米油盐在互助相守中化作了红火踏实的好日子。",
                "pinyin": "Zài lǎo Běijīng de sìhéyuàn lǐ, 'guò rìzi' shì yī mén chōngmǎn wēnqíng de yìshù. Chūnrì sǎo luòhuā, xiàyè nà liángfēng, qiūrì zhāi hóngzǎo, dōngrì wēi nuǎnlú. Línlǐ zhījiān jiè yī bǎ cōng, tiān yī sháo yóu, pǔsù de chái-mǐ-yóu-yán zài hùzhù xiāngshǒu zhōng huà zuò le hónghuo tàshi de hǎo rìzi.",
                "en": "In old Beijing courtyards, 'living everyday life' was an art of human warmth. Sweeping spring petals, catching summer breezes, and sharing salt and oil between neighbors transformed simple domestic chores into thriving, tranquil happiness.",
                "es": "En el siheyuan pekinés, 'gobernar el hogar' era un arte entrañable. Barrer pétalos primaverales o compartir condimentos entre vecinos convertía las tareas domésticas en un discurrir apacible y dichoso."
            },
            {
                "id": "#2",
                "hanzi": "幸福的生活往往并不依赖奢华的物质享受，而在于我们以怎样的心态面对平凡的日子。在日复一日的简单作息中发现惊喜，懂得珍惜身边的家人与挚友，脚踏实地耕耘每一天，就能把看似平淡的日子过得丰盈而充实。",
                "pinyin": "Xìngfú de shēnghuó wǎngwǎng bù yīlài shēhuá de wùzhì xiǎngshòu, ér zàiyú wǒmen yǐ zěnyàng de xīntài miànduì píngfán de rìzi. Zài rì-fù-yī-rì de jiǎndān zuòxī zhōng fāxiàn jīngxǐ, dǒngdé zhēnxī shēnbiān de jiārén yǔ zhìyǒu, jiǎotà-shídì gēngyún měitiān, jiù néng bǎ kànsì píngdàn de rìzi guò de fēngyíng ér chōngshí.",
                "en": "Happiness rarely depends on lavish luxury, but on our attitude toward ordinary days. Finding surprises in simple routines, cherishing family, and cultivating each moment faithfully transforms plain days into fulfilling abundance.",
                "es": "La felicidad no estriba en el lujo suntuario, sino en encarar las jornadas sencillas con gratitud. Hallar asombro en lo cotidiano y atesorar a los seres queridos colma el transcurso de los días de plenitud y sentido."
            }
        ]
    },

    # 35 充分
    {
        "id": "35",
        "hanzi": "充分",
        "pinyin": "chōng fèn",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "full; ample; abundant; fully; to the full",
            "es": "pleno; suficiente; abundante; plenamente; al máximo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "fully sufficient in quantity, degree, or condition; thoroughly developed or exercised",
                "definition_es": "enteramente suficiente en cantidad, grado o alcance; cabal; desarrollado al máximo",
                "example_phrase": "充分发挥优势 (give full play to advantages)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院坐北朝南的建筑朝向，使正房在一整年里都能享受到充分的阳光照射与良好的采光。",
                "pinyin": "Sìhéyuàn zuòběi-cháonán de jiànzhù cháoxiàng, shǐ zhèngfáng zài yī zhěng nián lǐ dōu néng xiǎngshòu dào chōngfèn de yángguāng zhàoshè yǔ liánghǎo de cǎiguāng.",
                "en": "The courtyard's south-facing orientation allowed the main room to enjoy ample sunshine and excellent natural lighting throughout the year.",
                "es": "La orientación al sur del siheyuan permitía que la sala principal disfrutara de plena insolación y excelente iluminación natural todo el año."
            },
            {
                "id": "#2",
                "hanzi": "在正式递交科研项目立项申请前，课题组成员进行了长达半年的充分文献调研与论证。",
                "pinyin": "Zài zhèngshì dìjiāo kēyán xiàngmù lìxiàng shēnqǐng qián, kètízǔ chéngyuán jìnxíng le cháng dá bàn nián de chōngfèn wénxiàn diàoyán yǔ lùnzhèng.",
                "en": "Before formally submitting the research grant proposal, the project members carried out half a year of thorough and ample literature review.",
                "es": "Antes de tramitar formalmente la propuesta científica, los investigadores realizaron durante medio año un examen bibliográfico exhaustivo."
            }
        ],
        "collocations": [
            {"hanzi": "充分理由", "en": "ample reason / sufficient justification"},
            {"hanzi": "充分准备", "en": "full / thorough preparation"},
            {"hanzi": "充分发挥", "en": "bring into full play"},
            {"hanzi": "充分利用", "en": "make full use of"},
            {"hanzi": "充分肯定", "en": "fully acknowledge / endorse"},
            {"hanzi": "条件充分", "en": "conditions are ample and satisfied"}
        ],
        "idioms": [
            {"hanzi": "充耳不闻", "pinyin": "chōng ěr bù wén", "meaning_en": "stuff one's ears and refuse to listen; turn a deaf ear"},
            {"hanzi": "充类至尽", "pinyin": "chōng lèi zhì jìn", "meaning_en": "push reasoning to the fullest logical extension"},
            {"hanzi": "气壮山河", "pinyin": "qì zhuàng shān hé", "meaning_en": "spirit full and majestic enough to move mountains and rivers"},
            {"hanzi": "面面俱到", "pinyin": "miàn miàn jù dào", "meaning_en": "attentive to every aspect meticulously"}
        ],
        "character_decomposition": [
            {
                "character": "充",
                "pinyin": "chōng",
                "meaning_en": "fill; satisfy; charge; full",
                "meaning_es": "llenar; colmar; cargar; pleno",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "亠 (head) + 育 (nurture / grow to full newborn size)",
                "sound_component": "充 (chōng)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A newborn child nurtured and growing robust until plump and fully developed; to fill to brim.",
                "visual_mnemonic_story_en": "Nurturing an infant until flourishing and bursting with full vigor (充).",
                "visual_mnemonic_story_es": "Nutrir a un infante hasta que florece con robusta plenitud física (充).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YHU",
                "traditional": "充"
            },
            {
                "character": "分",
                "pinyin": "fèn",
                "meaning_en": "part; portion; share; degree; lot",
                "meaning_es": "parte; porción; medida; cuota",
                "radical": "刀",
                "radical_meaning_en": "knife",
                "meaning_component": "八 (divide / separate) + 刀 (cutting blade)",
                "sound_component": "分 (fēn / fèn)",
                "stroke_count": 4,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Using a knife 刀 to divide 八 an object into fair portions and full measured shares fèn.",
                "visual_mnemonic_story_en": "A knife (刀) cleanly apportioning resources into complete, measured shares (分).",
                "visual_mnemonic_story_es": "Una hoja (刀) que reparte los recursos en raciones justas y medidas (分).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "CSH",
                "traditional": "分"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Filled to the brim (充) to meet one's full measured quota (分) is ample and sufficient (充分).",
            "composite_memory_hook_es": "Colmado hasta el borde (充) en la medida justa y cabal (分) conforma lo pleno y suficiente (充分).",
            "cultural_and_cognitive_roots": "Blends agricultural fulfillment (grain vessels filled to brim) with philosophical moderation and sufficiency.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'chōng fèn' (55-51). High steady pitch on 'chōng', descending with decisive strength on 'fèn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "允", "pinyin": "yǔn", "meaning_en": "permit; allow", "distinction_note": "Lacks the upper dot/horizontal strokes of 亠"},
                {"character": "弃", "pinyin": "qì", "meaning_en": "abandon; discard", "distinction_note": "Fork 廾 radical at bottom instead of 儿"},
                {"character": "刃", "pinyin": "rèn", "meaning_en": "blade edge", "distinction_note": "Dot inside knife 刀 instead of 八 on top"},
                {"character": "公", "pinyin": "gōng", "meaning_en": "public; fair", "distinction_note": "Private radical 厶 under 八 instead of 刀"}
            ],
            "etymological_cognates": [
                {"character": "充满", "pinyin": "chōngmǎn", "gloss_en": "brimming with; filled"},
                {"character": "充足", "pinyin": "chōngzú", "gloss_en": "adequate; plentiful"},
                {"character": "分寸", "pinyin": "fēncun", "gloss_en": "sense of propriety / measure"},
                {"character": "本分", "pinyin": "běnfèn", "gloss_en": "one's duty; honest lot"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "充分 stresses completeness in degree, depth of argumentation, or maximizing capacity.",
            "contrasts": [
                {"id": 1, "compared_word": "充分 vs. 充足", "pinyin": "chōngzú", "analysis": "充足 emphasizes quantitative sufficiency of tangible supplies (water, funds), while 充分 highlights qualitative thoroughness (reasons, preparations)."},
                {"id": 2, "compared_word": "充分 vs. 充实", "pinyin": "chōngshí", "analysis": "充实 describes substantial inner content (fulfilling life/mind), while 充分 denotes meeting all requirements."},
                {"id": 3, "compared_word": "充分 vs. 欠缺", "pinyin": "qiànquē", "analysis": "欠缺 is the direct antonym denoting inadequate preparation or deficient conditions."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统建筑大师在规划四合院时，充分利用了自然地理优势。坐北朝南的布局充分迎纳冬日低斜的暖阳，又通过庭院树冠阻挡酷暑的直射，将自然采光与防风遮阳的功效发挥到了极致，展现出高超的设计智慧。",
                "pinyin": "Zhōngguó chuántǒng jiànzhù dàshī zài guīhuà sìhéyuàn shí, chōngfèn lìyòng le zìrán dìlǐ yōushì. Zuòběi-cháonán de bùjú chōngfèn yíngnà dōngrì dīxié de nuǎnyáng, yòu tōngguò tíngyuàn shùguān zǔdǎng kùshǔ de zhíshè, jiāng zìrán cǎiguāng yǔ fángfēng-zhēyáng de gōngxiào fāhuī dào le jízhì, zhǎnxiàn chū gāochāo de shèjì zhìhuì.",
                "en": "Master architects fully utilized geographical advantages when planning courtyards. Facing south welcomed low winter sun, while tree canopies shaded summer glare, making full use of natural light and ventilation with supreme wisdom.",
                "es": "Los maestros constructores aprovecharon plenamente la geografía al trazar el siheyuan. Mirar al sur captaba el sol invernal, mientras las copas de los árboles tamizaban el estío, maximizando la luz y brisas con admirable talento."
            },
            {
                "id": "#2",
                "hanzi": "在任何重大决策出台之前，必须进行充分的调查研究与风险评估。广泛听取社会各界的意见建议，充分论证各项实施方案的科学性与可行性，才能避免盲目推进带来的决策失误，确保公共政策行稳致远。",
                "pinyin": "Zài rènhé zhòngdà juécè chūtái zhīqián, bìxū jìnxíng chōngfèn de diàochá yánjiū yǔ fēngxiǎn pínggū. Guǎngfàn tīngqǔ shèhuì gèjiè de yìjiàn jiànyì, chōngfèn lùnzhèng gè xiàng shíshī fāng'àn de kēxuéxìng yǔ kěxíngxìng, cái néng bìmiǎn mángmù tuījìn dàilái de juécè shīwù, quèbǎo gōnggòng zhèngcè xíngwěn-zhìyuǎn.",
                "en": "Before issuing major policies, thorough research and risk assessment are imperative. Gathering wide counsel and fully substantiating feasibility prevents blind missteps, ensuring public decisions remain prudent and sound.",
                "es": "Antes de promulgar resoluciones de calado, es preceptivo un estudio riguroso de riesgos. Recabar pareceres y fundamentar plenamente la viabilidad técnica evita desatinos, garantizando políticas públicas solventes."
            }
        ]
    },

    # 36 令
    {
        "id": "36",
        "hanzi": "令",
        "pinyin": "lìng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to make; cause (someone to feel); order; command; season",
            "es": "hacer; causar; infundir; ordenar; mandato; estación"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "pivotal verb meaning to cause or make someone feel a particular emotion; also to command or order",
                "definition_es": "verbo causativo que significa hacer que alguien experimente un sentimiento; ordenar",
                "example_phrase": "令人难忘 (make people remember unforgettable feelings)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "漫步在青砖灰瓦、花木扶疏的四合院中，那种安宁祥和的东方意境令人心旷神怡、流连忘返。",
                "pinyin": "Mànbù zài qīngzhuān-huīwǎ, huāmù-fúshū de sìhéyuàn zhōng, nà zhǒng ānníng xiánghé de dōngfāng yìjìng lìng rén xīnkuàng-shényí, liúlián-wàngfǎn.",
                "en": "Strolling through gray-brick and leafy courtyards, that tranquil Eastern atmosphere makes one feel relaxed, captivated, and reluctant to leave.",
                "es": "Pasear por el siheyuan de ladrillos grises y vegetación frondosa infunde un sosiego que despeja el ánimo y cautiva los sentidos."
            },
            {
                "id": "#2",
                "hanzi": "科研团队在极度艰苦的试验环境下取得的这一突破性成果，令同行专家们由衷赞叹。",
                "pinyin": "Kēyán tuánduì zài jídù jiānkǔ de shìyàn huánjìng xià qǔdé de zhè yī tūpòxìng chéngguǒ, lìng tóngháng zhuānjiā men yóuzhōng zàntàn.",
                "en": "This breakthrough achieved by the research team under arduous conditions caused peers to admire them from the bottom of their hearts.",
                "es": "El hallazgo alcanzado por el equipo científico bajo duras condiciones de laboratorio hizo que sus colegas lo elogiaran con admiración sincera."
            }
        ],
        "collocations": [
            {"hanzi": "令人满意", "en": "make people satisfied / gratifying"},
            {"hanzi": "令人难忘", "en": "make it unforgettable"},
            {"hanzi": "令人震惊", "en": "make people astonished / shocking"},
            {"hanzi": "令人欣慰", "en": "make people gratified / comforting"},
            {"hanzi": "下达命令", "en": "issue an order / command"},
            {"hanzi": "军令如山", "en": "military orders are firm as mountains"}
        ],
        "idioms": [
            {"hanzi": "令人发指", "pinyin": "lìng rén fà zhǐ", "meaning_en": "make one's hair stand on end with outrage"},
            {"hanzi": "巧言令色", "pinyin": "qiǎo yán lìng sè", "meaning_en": "fine words and ingratiating manners; deceitful flattery"},
            {"hanzi": "令行禁止", "pinyin": "lìng xíng jìn zhǐ", "meaning_en": "orders executed promptly and prohibitions strictly obeyed"},
            {"hanzi": "自愧不如", "pinyin": "zì kuì bù rú", "meaning_en": "feel inferior and ashamed of one's shortcomings"}
        ],
        "character_decomposition": [
            {
                "character": "令",
                "pinyin": "lìng",
                "meaning_en": "order; command; cause; make",
                "meaning_es": "ordenar; mandato; hacer; causar",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "亼 (leader's mouth issuing decrees) + 卩 (kneeling person obeying)",
                "sound_component": "令 (lìng)",
                "stroke_count": 5,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "A ruler gathered atop a hall issuing a decree 亼 to a kneeling subject 卩; evolved into causing an effect.",
                "visual_mnemonic_story_en": "A leader gathering people under a roof (人) to deliver an inspiring proclamation that moves everyone (令).",
                "visual_mnemonic_story_es": "Un dignatario congregando vasallos bajo el alero (人) para proclamar una orden que conmueve a todos (令).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "OII",
                "traditional": "令"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "An authoritative decree issued from above (令) moves or causes (令) people to feel deep reactions.",
            "composite_memory_hook_es": "Una orden emitida con autoridad (令) provoca o causa (令) una reacción afectiva en quien la recibe.",
            "cultural_and_cognitive_roots": "Originates as an imperial command in oracle script, widening into a causative literary marker (使/让/令) invoking emotions.",
            "tone_sandhi_and_pitch_modulation": "Fourth tone: 'lìng' (51). Deliver with crisp, authoritative downward momentum."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "今", "pinyin": "jīn", "meaning_en": "now; present", "distinction_note": "Lacks the bottom dot/hook mark of 令"},
                {"character": "冷", "pinyin": "lěng", "meaning_en": "cold; chill", "distinction_note": "Ice radical 冫 to the left of 令"},
                {"character": "怜", "pinyin": "lián", "meaning_en": "pity; sympathize", "distinction_note": "Heart radical 忄 to the left of 令"},
                {"character": "铃", "pinyin": "líng", "meaning_en": "bell; chime", "distinction_note": "Metal radical 钅 to the left of 令"}
            ],
            "etymological_cognates": [
                {"character": "命令", "pinyin": "mìnglìng", "gloss_en": "order; command"},
                {"character": "法令", "pinyin": "fǎlìng", "gloss_en": "decree; statute laws"},
                {"character": "时令", "pinyin": "shílìng", "gloss_en": "season; seasonal time"},
                {"character": "指令", "pinyin": "zhǐlìng", "gloss_en": "instruction; directive"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "令 functions primarily as a causative pivotal verb inducing psychological feelings (令+人+adjective/verb).",
            "contrasts": [
                {"id": 1, "compared_word": "令 vs. 让", "pinyin": "ràng", "analysis": "让 is colloquial and can denote giving permission or yielding, while 令 is written and introduces emotional reactions."},
                {"id": 2, "compared_word": "令 vs. 使", "pinyin": "shǐ", "analysis": "使 can link concrete factual transformations, while 令 is heavily favored for emotional sensations (令人感动)."},
                {"id": 3, "compared_word": "令 vs. 劝", "pinyin": "quàn", "analysis": "劝 means persuading or advising someone, whereas 令 as causative directly produces the psychological effect."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "走进北京保存完好的古老四合院，高高悬挂的红灯笼与雕刻精美的垂花门令人目不暇接。院落里弥漫着淡淡的茉莉花茶清香，那份穿越历史风尘而来的安详从容，令人瞬间忘却了都市生活的喧嚣与浮躁。",
                "pinyin": "Zǒu jìn Běijīng bǎocún wánhǎo de gǔlǎo sìhéyuàn, gāogāo xuánguà de hóng dēnglong yǔ diāokè jīngměi de chuíhuāmén lìng rén mùbùxiájiē. Yuànluò lǐ mímàn zhe dàndàn de mòlihuā chá qīngxiāng, nà fèn chuānyuè lìshǐ fēngchén ér lái de ānxiáng cóngróng, lìng rén shùnjiān wàngquè le dūshì shēnghuó de xuānxīao yǔ fúzào.",
                "en": "Entering a preserved Beijing courtyard, high-hanging red lanterns and carved gates leave visitors feast their eyes. Fragrant jasmine tea drifts through the yard, and its historical serenity makes one instantly forget urban bustle.",
                "es": "Al franquear un siheyuan pekinés, los farolillos rojos y cancelas caladas dejan atónita la mirada. El aroma a té de jazmín y la quietud histórica hacen olvidar de golpe las prisas y el tráfago de la gran ciudad."
            },
            {
                "id": "#2",
                "hanzi": "中国古代先贤关于自律自省的至理名言，至今读来依然令人振聋发聩。“见贤思齐焉，见不贤而内自省也”，这种虚怀若谷的治学修身精神，令一代代后人深受启迪，成为指引人们不断完善人格的精神明灯。",
                "pinyin": "Zhōngguó gǔdài xiānxián guānyú zìlǜ-zìxǐng de zhìlǐ míngyán, zhìjīn dú lái yīrán lìng rén zhènlóng-fākuì. 'Jiàn xián sī qí yān, jiàn bù xián ér nèi zìxǐng yě', zhè zhǒng xūhuái-ruògǔ de zhìxué xiūshēn jīngshén, lìng yīdàidài hòurén shēn shòu qǐdí, chéngwéi zhǐyǐn rénmen bùduàn wánshàn réngé de jīngshén míngdēng.",
                "en": "Ancient sages' aphorisms on self-discipline remain thought-provoking today: 'When seeing worthy individuals, strive to emulate them.' This introspective scholarly humility inspires successive generations to cultivate their character.",
                "es": "Las sentencias de los sabios antiguos sobre la templanza siguen conmoviendo: 'Al ver al sabio, procura igualarlo; al ver al necio, examínate a ti mismo.' Esta humildad letrada ha inspirado a generaciones a perfeccionar su alma."
            }
        ]
    },

    # 37 亲切
    {
        "id": "37",
        "hanzi": "亲切",
        "pinyin": "qīn qiè",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "cordial; genial; warm; amiable; intimate",
            "es": "cordial; afectuoso; cercano; cálido; entrañable"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "warm, cordial, and approachable in manner or words; evoking familiar domestic warmth",
                "definition_es": "cálido, cariñoso y accesible en el trato o lenguaje; que infunde cercanía y confianza",
                "example_phrase": "亲切的笑容 (a warm and genial smile)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院里老街坊们见面时那一声声亲切的问候，让远离故土的游子感受到了久违的家的温暖。",
                "pinyin": "Sìhéyuàn lǐ lǎo jiēfang men jiànmiàn shí nà yī shēng shēng qīnqiè de wènhòu, ràng yuǎnlí gùtǔ de yóuzǐ gǎnshòudào le jiǔwéi de jiā de wēnnuǎn.",
                "en": "The warm greetings exchanged when neighbors met in courtyards made returning travelers feel long-lost home comfort.",
                "es": "Los saludos entrañables que se cruzaban los viejos vecinos del siheyuan hacían sentir al viajero el calor añorado del hogar."
            },
            {
                "id": "#2",
                "hanzi": "那位资深老教授对待青年学生态度极其亲切，总是耐心地解答大家在求学中的每一个疑惑。",
                "pinyin": "Nà wèi zīshēn lǎo jiàoshòu duìdài qīngnián xuéshēng tàidù jíqí qīnqiè, zǒngshì nàixīn de jiědá dàjiā zài qiúxué zhōng de měi yī gè yíhuò.",
                "en": "That veteran professor was exceptionally warm toward young students, patiently resolving every academic question.",
                "es": "Aquel veterano catedrático dispensaba un trato sumamente afable a los jóvenes, resolviendo con paciencia sus inquietudes."
            }
        ],
        "collocations": [
            {"hanzi": "亲切问候", "en": "cordial greetings"},
            {"hanzi": "亲切关怀", "en": "warm and loving concern"},
            {"hanzi": "感到亲切", "en": "feel warm and familiar"},
            {"hanzi": "态度亲切", "en": "warm and genial attitude"},
            {"hanzi": "亲切交谈", "en": "cordial conversation"},
            {"hanzi": "和蔼亲切", "en": "amiable and approachable"}
        ],
        "idioms": [
            {"hanzi": "和蔼可亲", "pinyin": "hé ǎi kě qīn", "meaning_en": "affable, genial, and readily approachable"},
            {"hanzi": "平易近人", "pinyin": "píng yì jìn rén", "meaning_en": "unassuming, approachable, and easy to associate with"},
            {"hanzi": "关怀备至", "pinyin": "guān huái bèi zhì", "meaning_en": "caring with every possible consideration"},
            {"hanzi": "情同手足", "pinyin": "qíng tóng shǒu zú", "meaning_en": "affection as close as brothers; tight-knit bond"}
        ],
        "character_decomposition": [
            {
                "character": "亲",
                "pinyin": "qīn",
                "meaning_en": "parent; relative; close; intimate; kiss",
                "meaning_es": "pariente; allegado; íntimo; besar;親",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "辛 (hazel tree / upright staff) + 见 (see with eyes)",
                "sound_component": "亲 (qīn)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Standing on tiptoe to gaze out 见 and welcome approaching blood relatives 亲 back home.",
                "visual_mnemonic_story_en": "Eagerly gazing into the distance (见) to welcome returning family relatives (亲).",
                "visual_mnemonic_story_es": "Otear el camino (见) con anhelo para abrazar a los familiares que regresan al hogar (亲).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YFD",
                "traditional": "親"
            },
            {
                "character": "切",
                "pinyin": "qiè",
                "meaning_en": "close; eager; cut; correspond to",
                "meaning_es": "cercano; ferviente; cortar; corresponder",
                "radical": "刀",
                "radical_meaning_en": "knife",
                "meaning_component": "七 (severing line) + 刀 (cutting blade penetrating deep)",
                "sound_component": "七 (qī)",
                "stroke_count": 4,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "A blade 刀 pressing right up close against material to make a clean cut; denotes utmost intimacy.",
                "visual_mnemonic_story_en": "A knife (刀) pressing closely and tightly against an object without gap (切).",
                "visual_mnemonic_story_es": "Una hoja (刀) que se ciñe con estrecha proximidad sin dejar resquicio (切).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "PSH",
                "traditional": "切"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Familial kinship (亲) pressing closely and intimately (切) feels thoroughly warm and cordial (亲切).",
            "composite_memory_hook_es": "El afecto del parentesco (亲) estrechado en íntima cercanía (切) infunde calidez entrañable (亲切).",
            "cultural_and_cognitive_roots": "Blends Confucian kinship warmth with empathetic proximity, defining the ideal tone for mentors and neighbors.",
            "tone_sandhi_and_pitch_modulation": "First tone to fourth tone: 'qīn qiè' (55-51). High level pitch on 'qīn', dropping with warm emphasis on 'qiè'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "辛", "pinyin": "xīn", "meaning_en": "toilsome; bitter", "distinction_note": "Lacks the bottom small/wood strokes of 亲"},
                {"character": "幸", "pinyin": "xìng", "meaning_en": "fortunate; lucky", "distinction_note": "Soil radical 土 at top instead of 立/亠"},
                {"character": "切 (qiē)", "pinyin": "qiē", "meaning_en": "cut; slice", "distinction_note": "First tone when verbal (to slice veggies)"},
                {"character": "功", "pinyin": "gōng", "meaning_en": "merit; achievement", "distinction_note": "Work 工 on left instead of 七"}
            ],
            "etymological_cognates": [
                {"character": "亲密", "pinyin": "qīnmì", "gloss_en": "close; intimate"},
                {"character": "亲人", "pinyin": "qīnrén", "gloss_en": "family members; loved ones"},
                {"character": "急切", "pinyin": "jíqiè", "gloss_en": "eager; impatient"},
                {"character": "关切", "pinyin": "guānqiè", "gloss_en": "deeply concerned"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "亲切 conveys approachable warmth, genial kindness, and familiar affection.",
            "contrasts": [
                {"id": 1, "compared_word": "亲切 vs. 热情", "pinyin": "rèqíng", "analysis": "热情 highlights lively exuberance and high-energy excitement, while 亲切 emphasizes gentle warmth and intimacy."},
                {"id": 2, "compared_word": "亲切 vs. 严肃", "pinyin": "yánsù", "analysis": "严肃 is the direct antonym denoting stern solemnity, contrasting with approachable 亲切 manner."},
                {"id": 3, "compared_word": "亲切 vs. 冷淡", "pinyin": "lěngdàn", "analysis": "冷淡 means aloof or indifferent, opposite to kind and accessible 亲切."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "漫步在老北京幽深的胡同里，最动人的莫过于四合院门口那几声亲切的乡音问候。“吃了吗您呐？”这句看似普通的招呼，透着邻里之间不分彼此的熟稔与关爱，让冰冷的城市砖石也变得充满人情味。",
                "pinyin": "Mànbù zài lǎo Běijīng yōushēn de hútòng lǐ, zuì dòngrén de mòguòyú sìhéyuàn ménkǒu nà jǐ shēng qīnqiè de xiāngyīn wènhòu. 'Chī le ma nín na?' Zhè jù kànsì pǔtōng de zhāohu, tòu zhe línlǐ zhījiān bù fēn bǐcǐ de shúrěn yǔ guān'ài, ràng bīnglěng de chéngshì zhuānshí yě biàn de chōngmǎn rénqíngwèi.",
                "en": "Strolling through deep Beijing alleys, nothing touches hearts like cordial local greetings at courtyard gates: 'Have you eaten yet?' This ordinary pleasantry brims with mutual familiarity, infusing stone alleys with human warmth.",
                "es": "Paseando por los callejones de Pekín, lo más conmovedor son los saludos afables ante los portales: '¿Ha comido ya?' Esta pregunta sencilla rebosa de confianza vecinal, templando la frialdad del asfalto con calor humano."
            },
            {
                "id": "#2",
                "hanzi": "在医疗护理实践中，医护人员亲切温和的言语往往具备抚慰人心的神奇疗效。面对焦虑不安的病患，一句亲切的鼓励、一个温暖的眼神，不仅能有效缓解患者内心的恐惧，更能建立起深厚互信的医患关系。",
                "pinyin": "Zài yīliáo hùlǐ shíjiàn zhōng, yīhù rényuán qīnqiè wēnhé de yányǔ wǎngwǎng jùbèi fǔwèi rénxīn de shénqí liáoxiào. Miànduì jiāolǜ-bù'ān de bìnghuàn, yī jù qīnqiè de gǔlì, yī gè wēnnuǎn de yǎnshén, bùjǐn néng yǒuxiào huǎnjiě huànzhě nèixīn de kǒngjù, gèng néng jiànlì qǐ shēnhòu hùxìn de yī-huàn guānxi.",
                "en": "In healthcare, cordial and gentle words from nurses possess wondrous healing power. A kind encouragement or warm glance alleviates anxiety, building trusting relationships between patients and caregivers.",
                "es": "En la labor sanitaria, las palabras afectuosas del personal médico poseen virtudes curativas para el alma. Un estímulo cercano y una mirada compasiva disipan temores y cimentan la mutua confianza clínica."
            }
        ]
    },

    # 38 劳动
    {
        "id": "38",
        "hanzi": "劳动",
        "pinyin": "láo dòng",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "labor; work; physical work; toil",
            "es": "trabajar; laborar; trabajo manual; faena"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to engage in physical or mental work to produce goods, build shelters, or create social wealth",
                "definition_es": "ejercer trabajo físico o intelectual para elaborar bienes, edificar o transformar el entorno",
                "example_phrase": "辛勤劳动 (work diligently / honest toil)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "中国古代四合院建筑的每一块砖瓦和雕梁，都凝聚着广大建筑工匠辛勤劳动的汗水与高超技艺。",
                "pinyin": "Zhōngguó gǔdài sìhéyuàn jiànzhù de měi yī kuài zhuānwǎ hé diāoliáng, dōu níngjù zhe guǎngdà jiànzhù gōngjiàng xīnqín láodòng de hànshuǐ yǔ gāochāo jìyì.",
                "en": "Every brick, tile, and carved beam in traditional courtyards embodies the sweat and mastery of building craftsmen's diligent labor.",
                "es": "Cada ladrillo, teja y viga tallada del siheyuan pekinés encarna el sudor y la primorosa destreza de las faenas de los albañiles clásicos."
            },
            {
                "id": "#2",
                "hanzi": "通过亲身参与农场劳动实践，中小学生们深刻体会到了“粒粒皆辛苦”的粮食来之不易。",
                "pinyin": "Tōngguò qīnshēn cānyù nóngchǎng láodòng shíjiàn, zhōng-xiǎoxuéshēng men shēnkè tǐhuì dào le 'lìlì jiē xīnkǔ' de liángshí láizhībùyì.",
                "en": "Through firsthand participation in farm labor, school students appreciated that every grain of food is hard-won through toil.",
                "es": "Participando en faenas agrícolas, los escolares comprendieron que cada grano en el plato es fruto de un esfuerzo laborioso."
            }
        ],
        "collocations": [
            {"hanzi": "辛勤劳动", "en": "hard and diligent labor"},
            {"hanzi": "劳动人民", "en": "working people / laborers"},
            {"hanzi": "体力劳动", "en": "manual / physical labor"},
            {"hanzi": "脑力劳动", "en": "mental / intellectual labor"},
            {"hanzi": "劳动模范", "en": "model worker"},
            {"hanzi": "热爱劳动", "en": "love labor / cherish hard work"}
        ],
        "idioms": [
            {"hanzi": "自食其力", "pinyin": "zì shí qí lì", "meaning_en": "earn one's own living through hard work; self-reliant"},
            {"hanzi": "辛勤耕耘", "pinyin": "xīn qín gēng yún", "meaning_en": "till and cultivate with assiduous diligence"},
            {"hanzi": "不劳而获", "pinyin": "bù láo ér huò", "meaning_en": "reap without sowing; gain without labor"},
            {"hanzi": "劳苦功高", "pinyin": "láo kǔ gōng gāo", "meaning_en": "having worked hard and achieved monumental merit"}
        ],
        "character_decomposition": [
            {
                "character": "劳",
                "pinyin": "láo",
                "meaning_en": "labor; toil; work; weary",
                "meaning_es": "trabajo; fatiga; labor; esfuerzo",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "𤇾 (torches burning late into night) + 力 (physical strength)",
                "sound_component": "劳 (láo)",
                "stroke_count": 7,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Exerting physical strength 力 under burning torches late into night; to toil relentlessly.",
                "visual_mnemonic_story_en": "Burning torches over head while exerting strength (力) to finish evening labor (劳).",
                "visual_mnemonic_story_es": "Antorchas encendidas sobre la cabeza mientras se aplica la fuerza muscular (力) en la faena (劳).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "TBS",
                "traditional": "勞"
            },
            {
                "character": "动",
                "pinyin": "dòng",
                "meaning_en": "move; act; change; motion",
                "meaning_es": "mover; actuar; cambiar; movimiento",
                "radical": "力",
                "radical_meaning_en": "strength / power",
                "meaning_component": "云 (clouds swirling across sky) + 力 (muscular force)",
                "sound_component": "云 (yún)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Applying physical force 力 like churning clouds 云 to shift things; marks physical motion.",
                "visual_mnemonic_story_en": "Applying strength (力) to set heavy objects into swift motion like rolling clouds (动).",
                "visual_mnemonic_story_es": "Aplicar la fuerza (力) para mover objetos pesados con el dinamismo de las nubes (动).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "MIS",
                "traditional": "動"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Exerting muscle power (劳) to initiate dynamic action (动) forms the definition of labor (劳动).",
            "composite_memory_hook_es": "Aplicar la fuerza muscular (劳) en continuo dinamismo físico (动) constituye la labor (劳动).",
            "cultural_and_cognitive_roots": "A cornerstone value of Chinese civilization asserting that honest labor creates all material civilization and moral character.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'láo dòng' (35-51). Rise smoothly on 'láo', then drop with resolute firmness on 'dòng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "芳", "pinyin": "fāng", "meaning_en": "fragrant", "distinction_note": "Square 方 under 艹 instead of 力"},
                {"character": "功", "pinyin": "gōng", "meaning_en": "merit; skill", "distinction_note": "Work 工 on left of 力 instead of 云"},
                {"character": "劝", "pinyin": "quàn", "meaning_en": "persuade", "distinction_note": "Again 又 on left of 力 instead of 云"},
                {"character": "劫", "pinyin": "jié", "meaning_en": "rob; plunder", "distinction_note": "Go 去 on left of 力 instead of 云"}
            ],
            "etymological_cognates": [
                {"character": "劳苦", "pinyin": "láokǔ", "gloss_en": "hard toil; hardship"},
                {"character": "劳碌", "pinyin": "láolù", "gloss_en": "bustling toil; drudgery"},
                {"character": "运动", "pinyin": "yùndòng", "gloss_en": "sports; movement"},
                {"character": "行动", "pinyin": "xíngdòng", "gloss_en": "take action; movement"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "劳动 signifies purposeful human exertion creating material or intellectual value, distinguished from leisure.",
            "contrasts": [
                {"id": 1, "compared_word": "劳动 vs. 工作", "pinyin": "gōngzuò", "analysis": "工作 refers to formal professional employment or career duties, while 劳动 stresses the physical/mental exertion itself."},
                {"id": 2, "compared_word": "劳动 vs. 休闲", "pinyin": "xiūxián", "analysis": "休闲 is the direct antonym meaning leisure, relaxation, and free time away from work."},
                {"id": 3, "compared_word": "劳动 vs. 游戏", "pinyin": "yóuxì", "analysis": "游戏 denotes playful recreational activity aimed at amusement, not productive creation."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "纵览中国建筑史，万里长城、紫禁城与老北京四合院，无一不是古代劳动人民心血智慧的结晶。工匠们用坚韧不拔的劳动开山取石、烧砖构木，在华夏大地上筑就了一座座令人惊叹的建筑奇迹。",
                "pinyin": "Zònglǎn Zhōngguó jiànzhùshǐ, Wànlǐ Chángchéng, Zǐjìnchéng yǔ lǎo Běijīng sìhéyuàn, wúyībùshì gǔdài láodòng rénmín xīnxuè zhìhuì de jiéjīng. Gōngjiàng men yòng jiānrèn-bùbá de láodòng kāishān qǔshí, shāozhuān gòumù, zài Huáxià dàdì shang zhùjiù le yī zuò zuò lìngrén jīngtàn de jiànzhù qíjì.",
                "en": "Looking across Chinese history, the Great Wall, Forbidden City, and courtyards all crystallize ancient working people's wisdom. With tenacious labor, artisans quarried stones and fired bricks, erecting astonishing architectural wonders.",
                "es": "A lo largo de la historia de China, la Gran Muralla, la Ciudad Prohibida y el siheyuan son fruto del ingenio del pueblo trabajador. Canteros y carpinteros forjaron con su labor maravillas que hoy asombran al mundo."
            },
            {
                "id": "#2",
                "hanzi": "劳动不仅创造了灿烂的物质财富，更在潜移默化中塑造着人类崇高坚韧的精神品质。只有脚踏实地尊重劳动、热爱劳动，依靠辛勤的双手去开拓进取，才能创造出真正属于自己的美好前程，赢得社会的普遍尊重。",
                "pinyin": "Láodòng bùjǐn chuàngzào le cànlàn de wùzhì cáifù, gèng zài qiányí-mòhuà zhōng sùzào zhe rénlèi chónggāo jiānrèn de jīngshén pǐnzhì. Zhǐyǒu jiǎotà-shídì zūnzhòng láodòng, rè'ài láodòng, yīkào xīnqín de shǒusuǒ qù kāituò jìnqǔ, cái néng chuàngzào chū zhēnzhèng shǔyú zìjǐ de měihǎo qiánchéng, yíngdé shèhuì de pǔbiàn zūnzhòng.",
                "en": "Labor creates material wealth while quietly molding noble human virtues. Only by respecting labor and relying on diligent hands can one pioneer a wonderful future and earn enduring social respect.",
                "es": "El trabajo no solo engendra bienes materiales, sino que cincela virtudes morales de entereza. Honrar el trabajo y bregar con honradez es el sendero para labrarse un porvenir próspero y el respeto comunitario."
            }
        ]
    },

    # 39 人民
    {
        "id": "39",
        "hanzi": "人民",
        "pinyin": "rén mín",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "the people; citizens; masses",
            "es": "el pueblo; los ciudadanos; las masas populares"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the body of citizens of a nation as a collective political and social whole",
                "definition_es": "conjunto de personas que componen una nación o comunidad política y social",
                "example_phrase": "为人民服务 (serve the people)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "北京四合院不仅是古代贵族与士绅的府邸，更是千千万万普通劳动人民安居乐业的温馨家园。",
                "pinyin": "Běijīng sìhéyuàn bùjǐn shì gǔdài guìzú yǔ shìshēn de fǔdǐ, gèng shì qiānqiān-wànwàn pǔtōng láodòng rénmín ānjū-lèyè de wēnxīn jiāyuán.",
                "en": "Beijing quadrangles were not only mansions of aristocrats, but also cozy homes where millions of ordinary working people lived in peace.",
                "es": "El siheyuan pekinés no fue solo residencia de dignatarios, sino el hogar acogedor donde millones de familias plebeyas vivían y trabajaban en paz."
            },
            {
                "id": "#2",
                "hanzi": "任何负责任的国家政府，都应当始终把人民的生命健康安全与切身福祉放在首要位置。",
                "pinyin": "Rènhé fùzérèn de guójiā zhèngfǔ, dōu yīngdāng shǐzhōng bǎ rénmín de shēngmìng jiànkāng ānquán yǔ qièshēn fúzhǐ fàng zài shǒuyào wèizhì.",
                "en": "Any responsible national government must always prioritize the lives, health, and welfare of the people above all else.",
                "es": "Todo gobierno responsable debe colocar en el centro de sus prioridades la vida, salud y bienestar del pueblo."
            }
        ],
        "collocations": [
            {"hanzi": "中国人民", "en": "the Chinese people"},
            {"hanzi": "全国人民", "en": "the people of the whole country"},
            {"hanzi": "人民群众", "en": "the broad masses of the people"},
            {"hanzi": "造福人民", "en": "bring benefit to the people"},
            {"hanzi": "人民大会堂", "en": "Great Hall of the People"},
            {"hanzi": "人民政府", "en": "People's Government"}
        ],
        "idioms": [
            {"hanzi": "国泰民安", "pinyin": "guó tài mín ān", "meaning_en": "the country is prosperous and the people enjoy peaceful security"},
            {"hanzi": "民胞物与", "pinyin": "mín bāo wù yǔ", "meaning_en": "fellow humans are brethren and all creatures are companions"},
            {"hanzi": "爱民如子", "pinyin": "ài mín rú zǐ", "meaning_en": "love the common people as one's own children"},
            {"hanzi": "水能载舟，亦能覆舟", "pinyin": "shuǐ néng zài zhōu, yì néng fù zhōu", "meaning_en": "water can float a boat, but can also capsize it (the people's will)"}
        ],
        "character_decomposition": [
            {
                "character": "人",
                "pinyin": "rén",
                "meaning_en": "person; human; mankind",
                "meaning_es": "persona; ser humano; individuo",
                "radical": "人",
                "radical_meaning_en": "person",
                "meaning_component": "pictograph of an erect human standing sideways with legs",
                "sound_component": "人 (rén)",
                "stroke_count": 2,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone glyph showing a standing human figure viewed from profile.",
                "visual_mnemonic_story_en": "Two supporting legs walking forward with dignity as an upright human (人).",
                "visual_mnemonic_story_es": "Dos piernas firmes que avanzan con dignidad erguida como ser humano (人).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "O",
                "traditional": "人"
            },
            {
                "character": "民",
                "pinyin": "mín",
                "meaning_en": "people; citizens; folk; public",
                "meaning_es": "pueblo; ciudadanía; plebe; popular",
                "radical": "氏",
                "radical_meaning_en": "clan",
                "meaning_component": "eye pierced by a needle (ancient captive/laborer marker)",
                "sound_component": "民 (mín)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient glyph showing an eye pierced by a needle; later evolved to designate common citizens and the people.",
                "visual_mnemonic_story_en": "The multitude of common people gathered together as one community (民).",
                "visual_mnemonic_story_es": "La multitud de ciudadanos congregados como comunidad civil (民).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "RVP",
                "traditional": "民"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Individual human beings (人) joined in common citizenship (民) constitute the people (人民).",
            "composite_memory_hook_es": "El individuo (人) unido al cuerpo social de ciudadanos (民) define al pueblo soberano (人民).",
            "cultural_and_cognitive_roots": "Foundational political concept in Chinese statecraft from Mencius's 'people are most precious' (民为贵) to modern governance.",
            "tone_sandhi_and_pitch_modulation": "Double second tone: 'rén mín' (35-35). Rise smoothly and harmoniously on both syllables."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "入", "pinyin": "rù", "meaning_en": "enter", "distinction_note": "Right stroke overlaps left stroke"},
                {"character": "八", "pinyin": "bā", "meaning_en": "eight", "distinction_note": "Two strokes do not touch"},
                {"character": "氏", "pinyin": "shì", "meaning_en": "clan; family", "distinction_note": "Has an extra hook on bottom right"},
                {"character": "良", "pinyin": "liáng", "meaning_en": "good; virtuous", "distinction_note": "Top dot over 目-like shape"}
            ],
            "etymological_cognates": [
                {"character": "民主", "pinyin": "mínzhǔ", "gloss_en": "democracy; democratic"},
                {"character": "民众", "pinyin": "mínzhòng", "gloss_en": "the masses; common folk"},
                {"character": "公民", "pinyin": "gōngmín", "gloss_en": "citizen"},
                {"character": "民俗", "pinyin": "mínsú", "gloss_en": "folk customs; folklore"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "人民 denotes the collective body of citizens and masses of a country with political and constitutional standing.",
            "contrasts": [
                {"id": 1, "compared_word": "人民 vs. 公民", "pinyin": "gōngmín", "analysis": "公民 is a strict legal term denoting individuals holding nationality and constitutional rights, whereas 人民 is a collective political concept."},
                {"id": 2, "compared_word": "人民 vs. 群众", "pinyin": "qúnzhòng", "analysis": "群众 refers to the broad non-party masses or spectators, while 人民 covers the entire sovereign national population."},
                {"id": 3, "compared_word": "人民 vs. 国民", "pinyin": "guómín", "analysis": "国民 emphasizes subjects or nationals in relation to the state apparatus, whereas 人民 highlights the democratic mass collective."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院的建筑风格生动反映了普通人民的生活追求。无论王府大宅还是平民院落，四面合围的格局都寄托着人民对家庭和睦、岁月静好的美好憧憬，凝聚着华夏人民千百年来守望相助的生存智慧。",
                "pinyin": "Lǎo Běijīng sìhéyuàn de jiànzhù fēnggé shēngdòng fǎnyìng le pǔtōng rénmín de shēnghuó zhuīqiú. Wúlùn wángfǔ dàzhái háishì píngmín yuànluò, sìmiàn héwéi de géjú dōu jìtuō zhe rénmín duì jiātíng hémù, suìyuè-jìnghǎo de měihǎo chōngjǐng, níngjù zhe Huáxià rénmín qiānbǎi nián lái shǒuwàng-xiāngzhù de shēngcún zhìhuì.",
                "en": "The architectural character of courtyards reflected the aspirations of common people. From princely mansions to humble dwellings, the enclosed layout embodied hopes for domestic harmony, crystallizing survival wisdom through mutual aid.",
                "es": "La arquitectura del siheyuan refleja los anhelos del pueblo sencillo. Mansiones o patios humildes compartían una traza que cobijaba la armonía familiar, condensando siglos de sabiduría y solidaridad comunitaria."
            },
            {
                "id": "#2",
                "hanzi": "人民是历史的创造者，是推动人类文明繁荣发展的根本力量。从古代水利灌溉工程的开凿，到现代高新科技产业的崛起，每一步辉煌跨越都离不开亿万人民的辛勤奋斗。尊重人民的历史主体地位，社会才能长治久安。",
                "pinyin": "Rénmín shì lìshǐ de chuàngzàozhě, shì tuīdòng rénlèi wénmíng fánróng fāzhǎn de gēnběn lìliàng. Cóng gǔdài shuǐlì guàngài gōngchéng de kāizáo, dào xiàndài gāoxīn kējì chǎnyè de juéqǐ, měi yī bù huīhuáng kuàyuè dōu lìbùkāi yìwàn rénmín de xīnqín fèndòu. Zūnzhòng rénmín de lìshǐ zhǔtǐ dìwèi, shèhuì cái néng chángzhì-jiǔ'ān.",
                "en": "The people are the creators of history and the fundamental force driving human progress. From ancient irrigation works to modern tech industries, every leap relies on the toil of millions. Respecting the people ensures enduring peace.",
                "es": "El pueblo es el artífice de la historia y el motor del avance de la civilización. Desde las acequias milenarias hasta la alta tecnología, cada hito se forja con la brega popular; honrar al pueblo garantiza la estabilidad común."
            }
        ]
    },

    # 40 矛盾
    {
        "id": "40",
        "hanzi": "矛盾",
        "pinyin": "máo dùn",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "contradiction; conflict; paradoxical; dispute",
            "es": "contradicción; conflicto; paradójico; discrepancia"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "a clash or conflict between opposing forces, ideas, or interests; self-contradictory proposition",
                "definition_es": "choque o pugna entre ideas, intereses o fuerzas opuestas; situación o enunciado paradójico",
                "example_phrase": "化解邻里矛盾 (resolve neighborhood conflicts)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "四合院中几代人同住一个屋檐下，难免会因为生活琐事产生摩擦，但大家总能通过耐心沟通化解矛盾。",
                "pinyin": "Sìhéyuàn zhōng jǐ dài rén tóng zhù yī gè wūyán xià, nánmiǎn huì yīnwèi shēnghuó suǒshì chǎnshēng mócā, dàn dàjiā zǒng néng tōngguò nàixīn gōutōng huàjiě máodùn.",
                "en": "With generations cohabiting under one courtyard roof, daily frictions were inevitable, yet family members resolved contradictions through patient talk.",
                "es": "Con varias generaciones bajo el mismo techo, surgían roces cotidianos, pero siempre disolvían las discrepancias mediante el diálogo paciente."
            },
            {
                "id": "#2",
                "hanzi": "他在求职过程中陷入了既想留在大城市发展又渴望陪伴年迈父母的内心深层矛盾之中。",
                "pinyin": "Tā zài qiúzhí guòchéng zhōng xiànrù le jì xiǎng liú zài dà chéngshì fāzhǎn yòu kěwàng péibàn niánmài fùmǔ de nèixīn shēncéng máodùn zhīzhōng.",
                "en": "In his job hunting, he was caught in an internal contradiction between pursuing career in the metropolis and caring for elderly parents.",
                "es": "En su búsqueda laboral, cayó en la honda contradicción interna entre triunfar en la gran ciudad y acompañar a sus ancianos padres."
            }
        ],
        "collocations": [
            {"hanzi": "化解矛盾", "en": "resolve / defuse contradictions"},
            {"hanzi": "激化矛盾", "en": "aggravate / intensify conflicts"},
            {"hanzi": "主要矛盾", "en": "principal contradiction"},
            {"hanzi": "内部矛盾", "en": "internal contradiction"},
            {"hanzi": "自相矛盾", "en": "self-contradictory"},
            {"hanzi": "矛盾重重", "en": "ridden with conflicts"}
        ],
        "idioms": [
            {"hanzi": "自相矛盾", "pinyin": "zì xiāng máo dùn", "meaning_en": "contradict oneself; self-contradictory"},
            {"hanzi": "针锋相对", "pinyin": "zhēn fēng xiāng duì", "meaning_en": "opposed like needle to awl; tit for tat in confrontation"},
            {"hanzi": "冰释前嫌", "pinyin": "bīng shì qián xián", "meaning_en": "past resentments melt away like thawing ice"},
            {"hanzi": "殊途同归", "pinyin": "shū tú tóng guī", "meaning_en": "reach the same destination by different routes"}
        ],
        "character_decomposition": [
            {
                "character": "矛",
                "pinyin": "máo",
                "meaning_en": "spear; lance; pike",
                "meaning_es": "lanza; pica; asta afilada",
                "radical": "矛",
                "radical_meaning_en": "spear",
                "meaning_component": "pictograph of a long thrusting spear with a pointed bronze head",
                "sound_component": "矛 (máo)",
                "stroke_count": 5,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictograph of an attacking spear with sharp blade and shaft.",
                "visual_mnemonic_story_en": "A sharp bronze warrior spear (矛) designed to pierce any defense.",
                "visual_mnemonic_story_es": "Una lanza de bronce punzante (矛) concebida para quebrar cualquier defensa.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "NINH",
                "traditional": "矛"
            },
            {
                "character": "盾",
                "pinyin": "dùn",
                "meaning_en": "shield; defense",
                "meaning_es": "escudo; defensa; resguardo",
                "radical": "目",
                "radical_meaning_en": "eye",
                "meaning_component": "厂 (protective canopy) + 目 (watchful eye behind visor)",
                "sound_component": "盾 (dùn)",
                "stroke_count": 9,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "A warrior's eye 目 peeking cautiously out from behind an armored defensive shield 厂.",
                "visual_mnemonic_story_en": "A watchful eye (目) peering safely from behind an impenetrable armor shield (盾).",
                "visual_mnemonic_story_es": "Un ojo avizor (目) que atisba tras la robusta lámina de un escudo defensivo (盾).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HJBU",
                "traditional": "盾"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The sharpest spear (矛) tested against the strongest shield (盾) creates an irresolvable contradiction (矛盾).",
            "composite_memory_hook_es": "La lanza más afilada (矛) enfrentada al escudo invulnerable (盾) forja la contradicción irresoluble (矛盾).",
            "cultural_and_cognitive_roots": "Derived from Han Feizi's famous parable of an armorer selling spears piercing anything and shields blocking everything simultaneously.",
            "tone_sandhi_and_pitch_modulation": "Second tone to fourth tone: 'máo dùn' (35-51). Lift cleanly on 'máo', followed by a sharp downward drop on 'dùn'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "予", "pinyin": "yǔ", "meaning_en": "give; bestow", "distinction_note": "Lacks the upper curved barbed hook of 矛"},
                {"character": "质", "pinyin": "zhì", "meaning_en": "quality; substance", "distinction_note": "Shell 贝 inside 厂 instead of 目 and 十"},
                {"character": "看", "pinyin": "kàn", "meaning_en": "look; watch", "distinction_note": "Hand 龵 over 目 instead of shield frame"},
                {"character": "省", "pinyin": "shěng", "meaning_en": "province; save", "distinction_note": "Little 少 over 目 instead of 盾"}
            ],
            "etymological_cognates": [
                {"character": "冲突", "pinyin": "chōngtū", "gloss_en": "conflict; clash"},
                {"character": "对立", "pinyin": "duìlì", "gloss_en": "oppose; stand in opposition"},
                {"character": "盾牌", "pinyin": "dùnpái", "gloss_en": "shield (weapon/metaphor)"},
                {"character": "分歧", "pinyin": "fēnqí", "gloss_en": "divergence; disagreement"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "矛盾 refers to logical incompatibilities, structural conflicts of interest, or psychological quandaries.",
            "contrasts": [
                {"id": 1, "compared_word": "矛盾 vs. 冲突", "pinyin": "chōngtū", "analysis": "冲突 involves active physical or verbal clashes, while 矛盾 can exist latently as an underlying structural clash."},
                {"id": 2, "compared_word": "矛盾 vs. 一致", "pinyin": "yīzhì", "analysis": "一致 is the direct antonym meaning harmonious alignment, consensus, or uniformity."},
                {"id": 3, "compared_word": "矛盾 vs. 摩擦", "pinyin": "mócā", "analysis": "摩擦 emphasizes surface friction in daily interactions, while 矛盾 points to deeper structural opposition."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统院落的大家族生活不仅有天伦之乐，也充斥着代际之间的观念矛盾。正房与厢房的分立布局，既保证了礼制尊卑，也给不同小家庭留下了缓冲空间，使潜在的家庭矛盾能够在屋檐下得到温和调解。",
                "pinyin": "Zhōngguó chuántǒng yuànluò de dàjiātíng shēnghuó bùjǐn yǒu tiānlún-zhīlè, yě chōngchì zhe dàijì zhījiān de guānniàn máodùn. Zhèngfáng yǔ xiāngfáng de fēnlì bùjú, jì bǎozhèng le lǐzhì zūnbēi, yě gěi bùtóng xiǎojiātíng liúxià le huǎnchōng kōngjiān, shǐ qiánzài de jiātíng máodùn nénggòu zài wūyán xià dédào wēnhé tiáojiě.",
                "en": "Big family life in courtyards enjoyed domestic joy but wrestled with intergenerational contradictions. The separated layout of main and wing rooms maintained hierarchy while providing buffer space to resolve family disputes gently.",
                "es": "La convivencia en el siheyuan aunaba dicha familiar y discrepancias generacionales. La separación entre la sala principal y las alas laterales daba un respiro prudencial para amortiguar y disolver roces familiares."
            },
            {
                "id": "#2",
                "hanzi": "事物发展的辩证法则表明，矛盾普遍存在于自然界与人类社会的各个领域。正是矛盾双方的既对立又统一，推动着事物不断打破平衡并迈向更高的发展阶段。勇于正视矛盾、妥善解决矛盾，是推动社会前行的内在动力。",
                "pinyin": "Shìwù fāzhǎn de biànzhèng fǎzé biǎomíng, máodùn pǔbiàn cúnzài yú zìránjiè yǔ rénlèi shèhuì de gègè lǐngyù. Zhèngshì máodùn shuāngfāng de jì duìlì yòu tǒngyī, tuīdòng zhe shìwù bùduàn dǎpò pínghéng bìng mài xiàng gèng gāo de fāzhǎn jiēduàn. Yǒngyú zhèngshì máodùn, tuǒshàn jiějué máodùn, shì tuīdòng shèhuì qiánxíng de nèizài dònglì.",
                "en": "Dialectical laws reveal that contradictions exist universally in nature and society. The unity and struggle of opposing forces drives progress toward higher stages. Confronting contradictions bravely serves as the engine of societal advance.",
                "es": "Las leyes dialécticas enseñan que la contradicción es consustancial a la naturaleza y a la sociedad. La pugna y unidad de contrarios rompe equilibrios para avanzar; encarar las contradicciones es el motor del progreso."
            }
        ]
    },

    # 41 浓
    {
        "id": "41",
        "hanzi": "浓",
        "pinyin": "nóng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "dense; thick; strong (atmosphere/feeling); intense; concentrated",
            "es": "denso; espeso; concentrado; intenso (sabor, atmósfera o afecto)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "having high density, strong consistency, deep color, or intense emotional atmosphere",
                "definition_es": "de gran densidad, consistencia espesa, color intenso o profunda carga emocional",
                "example_phrase": "浓郁的人情味 (strong human warmth)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "每逢除夕之夜，北京四合院家家户户挂红灯、贴春联，庭院里弥漫着浓郁而喜庆的节日气氛。",
                "pinyin": "Měi féng chúxī-zhīyè, Běijīng sìhéyuàn jiājiā-hùhù guà hóngdēng, tiē chūnlián, tíngyuàn lǐ mímàn zhe nóngyù ér xǐqìng de jiérì qìfēn.",
                "en": "Every New Year's Eve, courtyard homes hung red lanterns and pasted couplets, filling the yard with a dense, joyful festive atmosphere.",
                "es": "En Nochevieja, los hogares del siheyuan colgaban faroles rojos y coplas primaverales, llenando el patio de una densa y jubilosa atmósfera festiva."
            },
            {
                "id": "#2",
                "hanzi": "在老茶馆里泡上一碗浓郁醇厚的茉莉花茶，细细品味那份穿越岁月的芳香与苦涩。",
                "pinyin": "Zài lǎo cháguǎn lǐ pào shang yī wǎn nóngyù chúnhòu de mòlihuā chá, xìxì pǐnwèi nà fèn chuānyuè suìyuè de fāngxiāng yǔ kǔsè.",
                "en": "Brewing a bowl of dense, mellow jasmine tea in an old teahouse, one savors the aroma and bitterness across the years.",
                "es": "Preparar un cuenco de té de jazmín denso y maduro en una vieja tetería permite saborear la fragancia y el dulzor que atraviesan los años."
            }
        ],
        "collocations": [
            {"hanzi": "浓郁气氛", "en": "dense / strong atmosphere"},
            {"hanzi": "浓厚的兴趣", "en": "keen / strong interest"},
            {"hanzi": "浓茶", "en": "strong tea"},
            {"hanzi": "浓烟", "en": "dense smoke"},
            {"hanzi": "浓眉大眼", "en": "thick eyebrows and big eyes"},
            {"hanzi": "感情浓厚", "en": "deep and strong affection"}
        ],
        "idioms": [
            {"hanzi": "浓墨重彩", "pinyin": "nóng mò zhòng cǎi", "meaning_en": "thick ink and heavy colors; paint in glowing, vivid strokes"},
            {"hanzi": "情浓意切", "pinyin": "qíng nóng yì qiè", "meaning_en": "deep feelings and earnest sincerity"},
            {"hanzi": "春意阑珊", "pinyin": "chūn yì lán shān", "meaning_en": "spring mood waning (contrasted with 浓)"},
            {"hanzi": "血浓于水", "pinyin": "xiè nóng yú shuǐ", "meaning_en": "blood is thicker than water; family ties are unbreakable"}
        ],
        "character_decomposition": [
            {
                "character": "浓",
                "pinyin": "nóng",
                "meaning_en": "dense; thick; concentrated; strong",
                "meaning_es": "denso; espeso; concentrado; intenso",
                "radical": "氵",
                "radical_meaning_en": "water",
                "meaning_component": "氵 (water drops) + 农 (fertile agricultural land and dew)",
                "sound_component": "农 (nóng)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Heavy liquid moisture 氵 soaking rich agricultural soils 农; denotes dense dew, thick flavor, or intense saturation.",
                "visual_mnemonic_story_en": "Abundant water droplets (氵) saturating fertile farmland (农) until rich, dense dew forms (浓).",
                "visual_mnemonic_story_es": "Gotas abundantes de agua (氵) que impregnan el campo fértil (农) formando un rocío denso (浓).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "EBHV",
                "traditional": "濃"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Heavy water moisture (氵) enriching fertile fields (农) yields dense dew and concentrated flavor (浓).",
            "composite_memory_hook_es": "El rocío abundante (氵) que empapa la tierra de labranza (农) evoca lo denso, espeso e intenso (浓).",
            "cultural_and_cognitive_roots": "Deeply linked to agrarian imagery of morning mist and heavy dew, widening to rich tea, dark ink, and profound human affection.",
            "tone_sandhi_and_pitch_modulation": "Second tone: 'nóng' (35). Lift the pitch with smooth, resonant warmth."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "农", "pinyin": "nóng", "meaning_en": "agriculture; farmer", "distinction_note": "Lacks the water radical 氵 on the left"},
                {"character": "深", "pinyin": "shēn", "meaning_en": "deep; profound", "distinction_note": "Right side is 罙 instead of 农"},
                {"character": "淡", "pinyin": "dàn", "meaning_en": "bland; pale; weak", "distinction_note": "Right side is two fires 炎 instead of 农"},
                {"character": "清", "pinyin": "qīng", "meaning_en": "clear; clean", "distinction_note": "Right side is 青 instead of 农"}
            ],
            "etymological_cognates": [
                {"character": "浓厚", "pinyin": "nónghòu", "gloss_en": "dense; pronounced; deep"},
                {"character": "浓缩", "pinyin": "nóngsuō", "gloss_en": "concentrate; condense"},
                {"character": "浓密", "pinyin": "nóngmì", "gloss_en": "thick; dense (foliage/hair)"},
                {"character": "浓香", "pinyin": "nóngxiāng", "gloss_en": "heady fragrance"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "浓 signifies high saturation of liquid concentration, deep pigments, thick atmosphere, or profound emotion.",
            "contrasts": [
                {"id": 1, "compared_word": "浓 vs. 淡", "pinyin": "dàn", "analysis": "淡 is the direct antonym meaning bland, diluted, pale, or emotionally distant."},
                {"id": 2, "compared_word": "浓 vs. 深", "pinyin": "shēn", "analysis": "深 refers to spatial depth or chronological late hours, whereas 浓 emphasizes density and saturation."},
                {"id": 3, "compared_word": "浓 vs. 稀", "pinyin": "xī", "analysis": "稀 indicates sparse population or watery consistency (porridge), opposite to dense 浓."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "老北京四合院最具魅力之处，在于它所散发出的浓浓人情味。院落里邻里街坊相伴几十年，逢年过节互送热气腾腾的饺子，谁家遇难大家齐心相助。这种浓厚的邻里亲情，成了古都胡同最温暖的记忆。",
                "pinyin": "Lǎo Běijīng sìhéyuàn zuì jù mèilì zhīchù, zàiyú tā suǒ sànfā chū de nóngnóng rénqíngwèi. Yuànluò lǐ línlǐ jiēfang xiāngbàn jǐshí nián, féng nián guò jié hù sòng rèqì-téngténg de jiǎozi, shuí jiā yùnàn dàjiā qíxīn xiāngzhù. Zhè zhǒng nónghòu de línlǐ qīnqíng, chéng le gǔdū hútòng zuì wēnnuǎn de jìyì.",
                "en": "The greatest charm of old Beijing courtyards lies in their dense human warmth. Neighbors living together for decades exchanged steaming dumplings during holidays and aided each other, etching fond memories in historic alleys.",
                "es": "El encanto supremo del siheyuan pekinés radica en su denso calor humano. Familias vecinas convivieron decenios compartiendo empanadillas festivas y auxilio mutuo, grabando el recuerdo más cálido de los viejos hutongs."
            },
            {
                "id": "#2",
                "hanzi": "中国书法艺术讲究“浓淡相宜”。书法家蘸上饱满的浓墨，在宣纸上挥毫泼墨，浓墨沉着雄健如磐石，淡墨灵动飘逸如飞云。浓淡干湿的巧妙交融，使得黑白分明的汉字线条展现出无穷无尽的生命气象。",
                "pinyin": "Zhōngguó shūfǎ yìshù jiǎngjiu 'nóng-dàn xiāngyí'. Shūfǎjiā zhàn shang bǎomǎn de nóngmò, zài xuānzhǐ shang huīháo-pōmò, nóngmò chénzhuó xióngjiàn rú pánshí, dànmò língdòng piāoyì rú fēiyún. Nóng-dàn gān-shī de qiǎomiào jiāoróng, shǐdé hēibái-fēnmíng de Hànzì xiàntiáo zhǎnxiàn chū wúqióng-wújìn de shēngmìng qìxiàng.",
                "en": "Chinese calligraphy emphasizes harmony between thick and diluted ink. Calligraphers dip pens in concentrated ink; dense ink stands sturdy like rocks, while diluted ink floats like clouds, giving boundless vitality to Hanzi strokes.",
                "es": "La caligrafía china aprecia el equilibrio entre tinta espesa y aguada. El trazo de tinta densa muestra firmeza pétrea, mientras la aguada emula nubes al viento; su juego dota al ideograma de vitalidad infinita."
            }
        ]
    }
]

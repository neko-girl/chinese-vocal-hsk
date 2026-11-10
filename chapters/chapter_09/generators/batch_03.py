# -*- coding: utf-8 -*-
from core.toon_builder import save_word

words_batch3 = [
    # 21 光临
    {
        "id": "21",
        "hanzi": "光临",
        "pinyin": "guāng lín",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to honor with one's presence; to visit; to frequent (polite honorific)",
            "es": "honrar con su presencia; visitar; acudir (fórmula de cortesía)"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Formal / Honorific",
                "definition_en": "polite honorific expression used by hosts, shops, or institutions welcoming guests or patrons",
                "definition_es": "expresión cortés empleada por anfitriones o comercios para agradecer la presencia o llegada de clientes",
                "example_phrase": "欢迎光临 (welcome to our shop/establishment)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "画廊开幕典礼上，馆长站在大厅前热情迎接各位艺术界同仁与收藏家的光临指导。",
                "pinyin": "Huàláng kāimù diǎnlǐ shàng, guǎnzhǎng zhàn zài dàtīng qián rèqíng yíngjiē gèwèi yìshùjiè tóngrén yǔ shōucángjiā de guānglín zhǐdǎo.",
                "en": "At the gallery opening ceremony, the curator stood before the hall welcoming the presence and guidance of art peers and collectors.",
                "es": "En la inauguración de la galería, el director aguardaba en el vestíbulo agradeciendo la presencia y las luces de colegas y coleccionistas."
            },
            {
                "id": "#2",
                "hanzi": "北京宣武门外的那家绍兴餐馆，因鲁迅等知名文人墨客的频繁光临而声名远扬，门庭若市。",
                "pinyin": "Běijīng Xuānwǔmén wài de nà jiā Shàoxīng cānguǎn, yīn Lǔ Xùn děng zhīmíng wénrén-mòkè de pínfán guānglín ér shēngmíng yuǎnyáng, méntíng-ruòshì.",
                "en": "That Shaoxing diner outside Beijing's Xuanwumen gained renown and bustling patronage due to frequent visits by Lu Xun and prominent writers.",
                "es": "Aquel mesón de Shaoxing en Pekín cobró gran fama y bullicio gracias a las asiduas visitas de Lu Xun y célebres literatos."
            }
        ],
        "collocations": [
            {"hanzi": "欢迎光临", "en": "welcome; please come in"},
            {"hanzi": "光临指导", "en": "honor us with your presence and guidance"},
            {"hanzi": "敬请光临", "en": "cordially invite you to attend"},
            {"hanzi": "光临寒舍", "en": "grace my humble home with your visit"},
            {"hanzi": "频频光临", "en": "frequently visit / patronize"},
            {"hanzi": "感谢光临", "en": "thank you for your presence"}
        ],
        "idioms": [
            {"hanzi": "蓬荜生辉", "pinyin": "péng bì shēng huī", "meaning_en": "your presence adds luster to my humble abode"},
            {"hanzi": "扫径以待", "pinyin": "sǎo jìng yǐ dài", "meaning_en": "sweep path to await the arrival of an esteemed guest"},
            {"hanzi": "如雷贯耳", "pinyin": "rú léi guàn ěr", "meaning_en": "reverberate like thunder; renowned name"},
            {"hanzi": "宾至如归", "pinyin": "bīn zhì rú guī", "meaning_en": "guests feel at home; warm hospitality"}
        ],
        "character_decomposition": [
            {
                "character": "光",
                "pinyin": "guāng",
                "meaning_en": "light; ray; glory; honor; bare",
                "meaning_es": "luz; rayo; gloria; honor; desnudo",
                "radical": "儿",
                "radical_meaning_en": "legs",
                "meaning_component": "火 (fire/torch)",
                "sound_component": "儿 (legs of a kneeling torchbearer)",
                "stroke_count": 6,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Oracle bone pictogram showing a person kneeling with a bright burning torch 火 upon their head, emitting radiance and honor.",
                "visual_mnemonic_story_en": "A kneeling attendant raises a blazing torch (火) over their head to cast bright light and honor (光) upon visitors.",
                "visual_mnemonic_story_es": "Un criado de rodillas alza una antorcha encendida (火) sobre la cabeza para alumbrar y honrar (光) al forastero.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "FMU",
                "traditional": ""
            },
            {
                "character": "临",
                "pinyin": "lín",
                "meaning_en": "approach; overlook; arrive; descend",
                "meaning_es": "acercarse; asomarse; llegar; descender",
                "radical": "丨",
                "radical_meaning_en": "vertical line",
                "meaning_component": "臣 (eye looking down) + 𠂉 (human figure)",
                "sound_component": "品 (three items inspected below)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing an official's eye 臣 gazing downward from a height upon subjects below, meaning to arrive from above.",
                "visual_mnemonic_story_en": "An esteemed noble gaze (臣) turns downward as an honored dignitary arrives and descends (临) into the hall.",
                "visual_mnemonic_story_es": "La mirada atenta (臣) desciende desde lo alto mientras el ilustre personaje llega y se asoma (临) al salón.",
                "tone_mnemonic_anchor": "35",
                "cangjie": "LLNW",
                "traditional": "臨"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Your glorious radiance (光) arrives to illuminate (临) our humble hall, honoring us with your presence (光临).",
            "composite_memory_hook_es": "Tu benévola luz (光) desciende y llega (临) a colmar nuestra casa, honrándonos con tu visita (光临).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese epistolary and court etiquette; visitors were conceptualized as bringing solar luster ('guānghuī') into an otherwise dark, rustic abode.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by rising tone: 'guāng lín' (55-35). Hold 'guāng' steadily at high pitch 55, then glide smoothly upward into 2nd tone 'lín'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "先", "pinyin": "xiān", "meaning_en": "first; early", "distinction_note": "Has horizontal crossbar inside bottom legs instead of fire-like top"},
                {"character": "鉴", "pinyin": "jiàn", "meaning_en": "inspect; mirror", "distinction_note": "Has 金 at bottom of 监/临 structures"},
                {"character": "览", "pinyin": "lǎn", "meaning_en": "survey; view", "distinction_note": "Has 见 at bottom instead of the right strokes of 临"},
                {"character": "严", "pinyin": "yán", "meaning_en": "strict; severe", "distinction_note": "Has 一 at top instead of left-right division"}
            ],
            "etymological_cognates": [
                {"character": "到", "pinyin": "dào", "gloss_en": "arrive at destination"},
                {"character": "访", "pinyin": "fǎng", "gloss_en": "visit; inquire respectfully"},
                {"character": "顾", "pinyin": "gù", "gloss_en": "look back; patronize customer-wise"},
                {"character": "至", "pinyin": "zhì", "gloss_en": "reach; arrive like arrow hitting mark"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "光临 is an honorific verb used solely to praise or welcome the arrival of guests, clients, or superiors.",
            "contrasts": [
                {"id": "1", "compared_word": "光临 vs. 来到", "pinyin": "láidào", "analysis": "来到 is a neutral factual verb ('he arrived at the station'), while 光临 is strictly an honorific formula ('welcome your esteemed arrival')."},
                {"id": "2", "compared_word": "光临 vs. 拜访", "pinyin": "bàifǎng", "analysis": "拜访 is spoken by the visitor describing their own respectful visit to another ('我去拜访老师'), while 光临 is spoken by the host to the visitor."},
                {"id": "3", "compared_word": "光临 vs. 光顾", "pinyin": "guānggù", "analysis": "光顾 is used specifically in commercial transactions welcoming patrons to spend money, while 光临 applies broadly to ceremonies, banquets, and homes."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "古人扫径以待远客，一席粗茶便足慰平生。当挚友踏雪而来叩响柴扉，主家满心欢喜相迎，那句发自肺腑的欢迎光临，绝非市井虚辞，而是高山流水般的知音相惜。灯火可亲的庭院里，酒香胜过千言万语。",
                "pinyin": "Gǔrén sǎojìng-yǐdài yuǎnkè, yì xí chūchá biàn zú wèi píngshēng. Dāng zhìyǒu tàxuě-érlái kòuxiǎng cháifēi, zhǔjiā mǎnxīn huānxǐ xiāngyíng, nà jù fāzì-fèifǔ de huānyíng guānglín, juéfēi shìjǐng xūcí, ér shì gāoshān-liúshuǐ bān de zhīyīn xiāngxī. Dēnghuǒ-kěqīn de tíngyuàn lǐ, jiǔxiāng shèngguò qiānyán-wànyǔ.",
                "en": "Ancients swept paths awaiting guests; simple tea consoled life. When a dear friend knocks through the snow, welcoming them is no empty commercial greeting, but deep resonance. By warm lamplight, the wine aroma outshines all words.",
                "es": "Los antiguos barrían la senda aguardando amigos; un té bastaba para festejar la vida. Cuando el allegado llama a la puerta sobre la nieve, darle la bienvenida no es fórmula hueca, sino complicidad de almas afines al calor de la lumbre."
            },
            {
                "id": "#2",
                "hanzi": "在现代高端服务业竞争中，真诚周到的礼仪规范是树立品牌口碑的核心要素。星级酒店与国际航空通过持续优化客户体验，将温馨专业的光临问候融入每一个服务触点，让来自五湖四海的旅客在异乡也能深切感受到宾至如归的尊崇与关怀。",
                "pinyin": "Zài xiàndài gāoduān fúwùyè jìngzhēng zhōng, zhēnchéng zhōudào de lǐyí guīfàn shì shùlì pǐnpái kǒubēi de héxīn yàosù. Xīngjí jiǔdiàn yǔ guójì hángkōng tōngguò chíxù yōuhuà kèhù tǐyàn, jiāng wēnxīn zhuānyè de guānglín wènhòu róngrù měi yí ge fúwù chùdiǎn, ràng láizì wǔhú-sìhǎi de lǚkè zài yìxiāng yě néng shēnqiè gǎnshòudào bīnzhì-rúguī de zūnchóng yǔ guānhuái.",
                "en": "In high-end hospitality, sincere etiquette builds brand reputation. Luxury hotels integrate professional welcomes into every service touchpoint, allowing travelers from afar to feel the warmth, respect, and belonging of a home away from home.",
                "es": "En la hostelería de alto nivel, la cortesía sincera cimenta la reputación. Los hoteles y aerolíneas incorporan una acogida profesional en cada detalle, haciendo que el viajero foráneo experimente la consideración y el calor de sentirse como en casa."
            }
        ]
    },

    # 22 交际
    {
        "id": "22",
        "hanzi": "交际",
        "pinyin": "jiāo jì",
        "part_of_speech": "Noun / Verb",
        "meanings_summary": {
            "en": "social communication; social interaction; interpersonal contact; to socialize",
            "es": "comunicación social; relaciones interpersonales; trato social; alternar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "interpersonal communication, social activities, and public networking",
                "definition_es": "comunicación interpersonal, relaciones públicas y vida social",
                "example_phrase": "交际能力 (social / interpersonal skills)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Verb",
                "register": "Formal",
                "definition_en": "to socialize with others, network, and engage in mutual relations",
                "definition_es": "relacionarse con otros, alternar socialmente y cultivar contactos",
                "example_phrase": "善于交际 (good at socializing)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "他在职场中不仅业务精湛，而且极富交际能力，总能妥善处理各部门之间错综复杂的协作关系。",
                "pinyin": "Tā zài zhíchǎng zhōng bùjǐn yèwù jīngzhàn, érqiě jí fù jiāojì nénglì, zǒng néng tuǒshàn chǔlǐ gè bùmén zhījiān cuòzōng-fùzá de xiézuò guānxi.",
                "en": "In the workplace, he is not only technically skilled but gifted in interpersonal skills, handling complex cross-department collaboration smoothly.",
                "es": "En el trabajo sobresale por su competencia técnica y sus dotes sociales, resolviendo con soltura la colaboración interdepartamental."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅并非不食人间烟火的孤傲斗士，在民国文人圈子里，他宴请同行、以文会友的交际活动十分频繁。",
                "pinyin": "Lǔ Xùn bìngfēi bùshí-rénjiān-yānhuǒ de gū'ào dòushì, zài Mínguó wénrén quānzi lǐ, tā yànqǐng tóngháng, yǐwén-huìyǒu de jiāojì huódòng shífēn pínfán.",
                "en": "Lu Xun was by no means an aloof hermit; in Republican literary circles, his social gatherings hosting peers and making friends were frequent.",
                "es": "Lu Xun no fue un ermitaño inaccesible; en los círculos letrados de la República alternaba con frecuencia agasajando colegas y trabando amistad."
            }
        ],
        "collocations": [
            {"hanzi": "交际能力", "en": "interpersonal/social skills"},
            {"hanzi": "善于交际", "en": "good at socializing"},
            {"hanzi": "社交/交际圈", "en": "social circle"},
            {"hanzi": "交际广泛", "en": "broad social connections"},
            {"hanzi": "语言交际", "en": "linguistic communication"},
            {"hanzi": "日常交际", "en": "daily social interaction"}
        ],
        "idioms": [
            {"hanzi": "八面玲珑", "pinyin": "bā miàn líng lóng", "meaning_en": "smooth and tactful in all directions; socially adept"},
            {"hanzi": "左右逢源", "pinyin": "zuǒ yòu féng yuán", "meaning_en": "gain resources left and right; navigate smoothly"},
            {"hanzi": "莫逆之交", "pinyin": "mò nì zhī jiāo", "meaning_en": "intimate, sworn friendship of complete mutual trust"},
            {"hanzi": "情投意合", "pinyin": "qíng tóu yì hé", "meaning_en": "find each other congenial; shared affinity"}
        ],
        "character_decomposition": [
            {
                "character": "交",
                "pinyin": "jiāo",
                "meaning_en": "cross; intersect; deliver; associate; friend",
                "meaning_es": "cruzar; cruzarse; entregar; relacionarse; amigo",
                "radical": "亠",
                "radical_meaning_en": "lid",
                "meaning_component": "亠 (head/torso) + 父 (crossed legs)",
                "sound_component": "交 (jiāo)",
                "stroke_count": 6,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of a standing human figure with crossed legs, symbolizing mutual exchange, crossing, and friendship.",
                "visual_mnemonic_story_en": "A friendly figure extends open arms and crosses legs, ready to exchange ideas and make friends (交).",
                "visual_mnemonic_story_es": "Una persona con las piernas cruzadas extiende los brazos, dispuesta a entablar trato y amistad (交).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YCK",
                "traditional": ""
            },
            {
                "character": "际",
                "pinyin": "jì",
                "meaning_en": "border; boundary; between; juncture",
                "meaning_es": "borde; frontera; entre; coyuntura",
                "radical": "阝",
                "radical_meaning_en": "mound/hill",
                "meaning_component": "阝 (mound/earthen wall)",
                "sound_component": "示 (shì, altar / connection between heaven and earth)",
                "stroke_count": 7,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Traditional 際 shows an altar 示 at the boundary border 阝 where human earth and divine heaven meet.",
                "visual_mnemonic_story_en": "Standing at the boundary wall (阝) to present tokens (示) opens doors across border junctures (际).",
                "visual_mnemonic_story_es": "Junto al muro fronterizo (阝), presentar ofrendas (示) permite tender puentes en el límite (际).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "NLMF",
                "traditional": "際"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Cross paths (交) across social boundaries (际) to engage in vibrant social communication (交际).",
            "composite_memory_hook_es": "Cruza tus pasos (交) en el punto de encuentro fronterizo (际) para cultivar el trato social (交际).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese semantics where 'jiāo' represents interpersonal bridge-building and 'jì' represents the interstice or nexus between diverse social actors.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'jiāo jì' (55-51). Articulate 'jiāo' on steady pitch 55, then drop cleanly into 4th tone 'jì'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "父", "pinyin": "fù", "meaning_en": "father", "distinction_note": "Lacks the upper dot and crossbar 亠 of 交"},
                {"character": "校", "pinyin": "xiào", "meaning_en": "school", "distinction_note": "Has tree radical 木 on left of 交"},
                {"character": "郊", "pinyin": "jiāo", "meaning_en": "suburb", "distinction_note": "Has right city radical 阝 on the right of 交"},
                {"character": "防", "pinyin": "fáng", "meaning_en": "defend", "distinction_note": "Has 方 on right instead of 示 in 际"}
            ],
            "etymological_cognates": [
                {"character": "往", "pinyin": "wǎng", "gloss_en": "go to and fro; associate"},
                {"character": "通", "pinyin": "tōng", "gloss_en": "connect; communicate smoothly"},
                {"character": "往来", "pinyin": "wǎnglái", "gloss_en": "social dealings and visits"},
                {"character": "涉", "pinyin": "shè", "gloss_en": "wade through river; involve"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "交际 emphasizes interpersonal networking, social protocol, and communicative competence in public life.",
            "contrasts": [
                {"id": "1", "compared_word": "交际 vs. 交流", "pinyin": "jiāoliú", "analysis": "交流 emphasizes mutual two-way transmission of ideas, culture, or feelings, while 交际 emphasizes broad social networking and interpersonal diplomacy."},
                {"id": "2", "compared_word": "交际 vs. 社交", "pinyin": "shèjiāo", "analysis": "社交 is primarily a noun modifier describing social media or society events ('社交平台'), while 交际 focuses on conversational and diplomatic skill."},
                {"id": "3", "compared_word": "交际 vs. 勾结", "pinyin": "gōujié", "analysis": "勾结 has a strongly derogatory meaning of corrupt collusion, while 交际 is neutral and positive."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "健康的社交不在于微信列表里有成百上千个好友，而在于交际过程中彼此给予的真诚与温度。真正的交情不需要虚情假意的周旋应酬，而是三两知己围炉夜话时的推心置腹。懂得拒绝无效社交，心灵才能回归丰盈与清宁。",
                "pinyin": "Jiànkāng de shèjiāo bú zàiyú Wēixìn lièbiǎo lǐ yǒu chéngbǎi-shàngqiān ge hǎoyǒu, ér zàiyú jiāojì guòchéng zhōng bǐcǐ jǐyǔ de zhēnchéng yǔ wēndù. Zhēnzhèng de jiāoqíng bù xūyào xūqíng-jiǎyì de zhōuxuán yīngchou, ér shì sānliǎng zhījǐ wéilú-yèhuà shí de tuīxīn-zhìfù. Dǒngdé jùjué wúxiào shèjiāo, xīnlíng cáinéng huíguī fēngyíng yǔ qīngníng.",
                "en": "Healthy networking lies not in thousands of virtual contacts, but sincerity exchanged. True friendship requires no hypocritical pleasantries, but candid fireside chats with true confidants. Rejecting shallow social noise restores peace.",
                "es": "La sana sociabilidad no se mide en listas interminables de contactos, sino en la sinceridad mutua. La amistad verdadera prescinde de cumplidos vanos y prefiere la sobremesa franca al calor del hogar. Filtrar el ruido social devuelve la paz interior."
            },
            {
                "id": "#2",
                "hanzi": "跨文化交际能力已成为全球化时代国际复合型人才的必备素养。面对不同国家和民族在价值观与行为范式上的客观差异，青年一代必须学会以开放包容的胸怀倾听对话，在跨文化交际中化解误解偏见，增进不同文明间的互信互鉴。",
                "pinyin": "Kuà wénhuà jiāojì nénglì yǐ chéngwéi quánqiúhuà shídài guójì fùhéxíng réncái de bìbèi sùyǎng. Miànduì bùtóng guójiā yǔ mínzú zài jiàzhíguān yǔ xíngwéi fànshì shàng de kèguān chāyì, qīngnián yídài bìxū xuéhuì yǐ kāifàng bāoróng de xiōnghuái qīngtīng duìhuà, zài kuà wénhuà jiāojì zhōng huàjiě wùjiě piānjiàn, zēngjìn bùtóng wénmíng jiān de hùxìn hùjiàn.",
                "en": "Cross-cultural communication competence has become essential for global talent. Facing differences in values and norms, youth must listen with an inclusive mindset, dispelling misunderstandings through dialogue to foster mutual civilizational trust.",
                "es": "La competencia intercultural es indispensable para el talento globalizado. Ante las divergencias de valores y costumbres, las nuevas generaciones deben dialogar con mente abierta, desvaneciendo prejuicios y cimentando la confianza mutua entre pueblos."
            }
        ]
    },

    # 23 大方
    {
        "id": "23",
        "hanzi": "大方",
        "pinyin": "dà fang",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "generous; open-handed; natural and poised; tasteful; in good taste",
            "es": "generoso; desprendido; natural; suelto; elegante; de buen gusto"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "generous and open-handed with money or goods, not stingy or penny-pinching",
                "definition_es": "generoso, desprendido y liberal con el dinero o las pertenencias; nada tacaño",
                "example_phrase": "出手很大方 (very generous when spending)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "natural, poised, and unconstrained in manner and speech; free from awkward self-consciousness",
                "definition_es": "desenvuelto, natural y con aplomo en los modales; sin timidez ni afectación",
                "example_phrase": "举止大方 (poised and natural deportment)"
            },
            {
                "sense_number": "3",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "tasteful, elegant, simple, and not gaudy in visual design or dress",
                "definition_es": "elegante, sobrio, de buen tono y no recargado en el vestir o el diseño",
                "example_phrase": "衣着大方 (tastefully dressed)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "新来的主持人举止优雅落落大方，在聚光灯前毫不怯场，赢得了全场观众的喝彩。",
                "pinyin": "Xīnlái de zhǔchírén jǔzhǐ yōuyǎ luòluò-dàfang, zài jùguāngdēng qián háobù qièchǎng, yíngdé le quánchǎng guānzhòng de hècǎi.",
                "en": "The newly arrived presenter was elegant, poised, and perfectly natural, without stage fright under the spotlights, winning applause.",
                "es": "La nueva presentadora mostró soltura y porte distinguido, sin amilanarse ante los focos y arrancando los aplausos del público."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅先生为人极其豪爽大方，每逢青年作家囊中羞涩求助，他总是慷慨解囊资助出版与生活。",
                "pinyin": "Lǔ Xùn xiānsheng wéirén jíqí háoshuǎng dàfang, měiféng niánqīng zuòjiā nángzhōng-xiūsè qiúzhù, tā zǒng shì kāngkǎi-jiěnáng zīzhù chūbǎn yǔ shēnghuó.",
                "en": "Mr. Lu Xun was remarkably frank and generous; whenever young struggling writers sought help, he always opened his purse liberally for them.",
                "es": "Lu Xun era sumamente desprendido y generoso; cuando jóvenes escritores apurados pedían auxilio, él costeaba sus ediciones y manutención."
            }
        ],
        "collocations": [
            {"hanzi": "出手大方", "en": "spend generously"},
            {"hanzi": "举止大方", "en": "natural and poised deportment"},
            {"hanzi": "落落大方", "en": "graceful and unconstrained"},
            {"hanzi": "为人很大方", "en": "very generous in character"},
            {"hanzi": "款式大方", "en": "tasteful and clean design style"},
            {"hanzi": "穿着大方", "en": "tastefully and decently dressed"}
        ],
        "idioms": [
            {"hanzi": "落落大方", "pinyin": "luò luò dà fāng", "meaning_en": "natural, poised, and dignified in conduct"},
            {"hanzi": "慷慨解囊", "pinyin": "kāng kǎi jiě náng", "meaning_en": "generously untie one's purse to give financial help"},
            {"hanzi": "贻笑大方", "pinyin": "yí xiào dà fāng", "meaning_en": "become a laughingstock to true experts/masters"},
            {"hanzi": "雍容大雅", "pinyin": "yōng róng dà yǎ", "meaning_en": "poised, dignified, and exquisitely refined"}
        ],
        "character_decomposition": [
            {
                "character": "大",
                "pinyin": "dà",
                "meaning_en": "big; great; major; expansive",
                "meaning_es": "grande; mayor; amplio; noble",
                "radical": "大",
                "radical_meaning_en": "big",
                "meaning_component": "大 (person stretching limbs out)",
                "sound_component": "大 (dà)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of a fully grown human standing with arms and legs outstretched in majestic breadth.",
                "visual_mnemonic_story_en": "A person stretches arms wide in noble expansiveness, embracing all things in greatness (大).",
                "visual_mnemonic_story_es": "Un hombre abre los brazos de par en par con hidalguía, abarcando el espacio con grandeza (大).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "K",
                "traditional": ""
            },
            {
                "character": "方",
                "pinyin": "fang",
                "meaning_en": "square; direction; side; upright; rule",
                "meaning_es": "cuadrado; rumbo; lado; recto; norma",
                "radical": "方",
                "radical_meaning_en": "square / direction",
                "meaning_component": "方 (plows lashed together square)",
                "sound_component": "方 (fāng)",
                "stroke_count": 4,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Ancient ideogram showing two boats or plows lashed square across; represents proper measure and moral uprightness.",
                "visual_mnemonic_story_en": "A compass points steadily in all four square directions, guiding conduct along righteous paths (方).",
                "visual_mnemonic_story_es": "La brújula señala con rectitud los cuatro puntos cardinales, orientando el recto proceder (方).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YHS",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Possessing a broad, great heart (大) and upright moral poise (方) makes one truly generous and poised (大方).",
            "composite_memory_hook_es": "Tener un corazón magnánimo (大) y modales intachables (方) define a la persona desprendida y elegante (大方).",
            "cultural_and_cognitive_roots": "Originally rooted in the Daoist Zhuangzi phrase 'dàfāng zhī jiā' (大方之家, master of the great cosmic way); over centuries it evolved into a compliment for unselfish generosity and graceful poise.",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by neutral tone: 'dà fang' (51-2). Articulate 'dà' with a crisp falling 4th tone, letting 'fang' fall into an unstressed neutral tone."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "太", "pinyin": "tài", "meaning_en": "too; excessive", "distinction_note": "Has extra dot below between legs of 大"},
                {"character": "犬", "pinyin": "quǎn", "meaning_en": "dog", "distinction_note": "Has dot on upper right shoulder of 大"},
                {"character": "万", "pinyin": "wàn", "meaning_en": "ten thousand", "distinction_note": "Has no dot at top and right hook instead of vertical"},
                {"character": "斤", "pinyin": "jīn", "meaning_en": "catty; axe", "distinction_note": "Has slant stroke on top left instead of dot of 方"}
            ],
            "etymological_cognates": [
                {"character": "广", "pinyin": "guǎng", "gloss_en": "broad; vast shelter"},
                {"character": "博", "pinyin": "bó", "gloss_en": "extensive; rich; plentiful"},
                {"character": "慷", "pinyin": "kāng", "gloss_en": "fervent; generous in spirit"},
                {"character": "恺", "pinyin": "kǎi", "gloss_en": "joyous; benevolent and generous"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "大方 characterizes unselfish open-handedness with wealth, or natural, unconstrained elegance in posture and dress.",
            "contrasts": [
                {"id": "1", "compared_word": "大方 vs. 慷慨", "pinyin": "kāngkǎi", "analysis": "慷慨 is a literary, elevated adjective specifically emphasizing enthusiastic financial donation or self-sacrifice, while 大方 is broadly used for money, clothes, and natural manner."},
                {"id": "2", "compared_word": "大方 vs. 小气", "pinyin": "xiǎoqi", "analysis": "小气 (stingy / petty) is the direct antonym of 大方 in both financial generosity and personal magnanimity."},
                {"id": "3", "compared_word": "大方 vs. 潇洒", "pinyin": "xiāosǎ", "analysis": "潇洒 emphasizes suave, carefree, dashing charm, while 大方 stresses grounded poise, good taste, and decent generosity."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "做人的最高境界在于大方。对待钱财不斤斤计较，施惠于人而不图回报；与人相处从容坦率，不忸怩作态不卑躬屈膝。这种由内而外生发的大方与舒朗，胜过世间一切矫揉造作的伪装，让人如沐春风倍感踏实。",
                "pinyin": "Zuòrén de zuìgāo jìngjiè zàiyú dàfang. Duìdài qiáncái bù jīnjīn-jìjiào, shīhuì yú rén ér bù tú huíbào; yǔ rén xiāngchǔ cóngróng tǎnshuài, bù niǔnī-zuòtài bù bēigōng-qūxī. Zhè zhǒng yóu nèi ér wài shēngfā de dàfang yǔ shūlǎng, shèngguò shìjiān yíqiè jiǎoróu-zàozuò de wěizhuāng, ràng rén rúmù-chūnfēng bèi gǎn tàshí.",
                "en": "The highest realm of character is poise and generosity. Not squabbling over pennies, giving without demanding returns, and treating others frankly without servility. This inner magnanimity outshines false pretense like a soothing spring breeze.",
                "es": "La mayor nobleza reside en la generosidad y el aplomo. No regatear pequeñeces, brindar ayuda sin esperar paga y tratar al prójimo con soltura sin dobleces. Esa hidalguía que brota del fondo vale más que fingimientos, regalando sosiego."
            },
            {
                "id": "#2",
                "hanzi": "现代极简主义设计强调“简而不陋，素雅大方”。设计师摒弃繁复冗余的雕琢堆砌，通过洗练利落的几何线条与天然材质的质朴肌理，营造出经得起岁月淘洗的空间美感。这种大方得体的审美理念，正深刻引领着当代都市居住风尚。",
                "pinyin": "Xiàndài jíjiǎn zhǔyì shèjì qiángdiào 'jiǎn ér bú lòu, sùyǎ dàfang'. Shèjìshī bǐngqì fánfù rǒngyú de diāozhuó duīqì, tōngguò xǐliàn lìluò de jǐhé xiàntiáo yǔ tiānrán cáizhì de zhìpǔ jīlǐ, yíngzào chū jīngdeqǐ suìyuè táoxǐ de kōngjiān měigǎn. Zhè zhǒng dàfang-détǐ de shěnmǐ lǐniàn, zhèng shēnkè yǐnlǐng zhe dāngdài dūshì jūzhù fēngshàng.",
                "en": "Minimalist design stresses clean elegance: simple yet tasteful. Stripping superfluous ornamentation, designers use crisp lines and natural textures to build timeless spaces. This tasteful aesthetic profoundly guides contemporary urban living.",
                "es": "El minimalismo moderno apuesta por la sobriedad distinguida. Al prescindir de barroquismos y valerse de líneas depuradas y materiales puros, se conciben espacios de belleza imperecedera. Ese porte sobrio guía hoy las vanguardias del diseño."
            }
        ]
    },

    # 24 好客
    {
        "id": "24",
        "hanzi": "好客",
        "pinyin": "hào kè",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "hospitable; friendly to visitors; fond of entertaining guests",
            "es": "hospitalario; acogedor; generoso con las visitas; amante de agasajar"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "enthusiastic, warm, and generous in receiving, entertaining, and lodging guests",
                "definition_es": "cálido, entusiasta y desprendido al recibir, atender y alojar a los visitantes",
                "example_phrase": "热情好客的主人 (warm and hospitable host)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "草原上的牧民纯朴好客，每当有远方的客人骑马到来，总会端出喷香的奶茶和手把肉热情款待。",
                "pinyin": "Cǎoyuán shàng de mùmín chūnpǔ hàokè, měidāng yǒu yuǎnfāng de kèrén qǐmǎ dàolái, zǒng huì duānchū pēnxiāng de nǎichá hé shǒubàròu rèqíng kuǎndài.",
                "en": "Herdsmen on the grassland are simple and hospitable; whenever travelers arrive on horseback, they serve fragrant milk tea and mutton cordially.",
                "es": "Los pastores de la estepa son hospitalarios y llanos; al llegar viajeros a caballo, siempre sirven té con leche aromático y carnes asadas."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅在北京与上海居住期间极度好客，家中常常高朋满座，同乡挚友与求教青年络绎不绝。",
                "pinyin": "Lǔ Xùn zài Běijīng yǔ Shànghǎi jūzhù qījiān jídù hàokè, jiā zhōng chángcháng gāopéng-mǎnzuò, tóngxiāng zhìyǒu yǔ qiújiào qīngnián luòyì-bùjué.",
                "en": "Lu Xun was exceptionally hospitable in Beijing and Shanghai; his home was constantly filled with distinguished friends and visiting youths.",
                "es": "Lu Xun fue un anfitrión entrañable en Pekín y Shanghái; su morada paraba colmada de paisanos, amigos dilectos y jóvenes aprendices."
            }
        ],
        "collocations": [
            {"hanzi": "热情好客", "en": "warm and hospitable"},
            {"hanzi": "生性好客", "en": "naturally hospitable by disposition"},
            {"hanzi": "好客之邦", "en": "a nation known for hospitality"},
            {"hanzi": "好客的民风", "en": "hospitable folk customs"},
            {"hanzi": "淳朴好客", "en": "honest, simple, and hospitable"},
            {"hanzi": "好客的主人家", "en": "hospitable host family"}
        ],
        "idioms": [
            {"hanzi": "倾囊相助", "pinyin": "qīng náng xiāng zhù", "meaning_en": "empty one's purse to assist a friend in need"},
            {"hanzi": "高朋满座", "pinyin": "gāo péng mǎn zuò", "meaning_en": "a hall full of distinguished and noble guests"},
            {"hanzi": "投桃报李", "pinyin": "tóu táo bào lǐ", "meaning_en": "return a plum when given a peach; reciprocate mutual goodwill"},
            {"hanzi": "倒屣相迎", "pinyin": "dào xǐ xiāng yíng", "meaning_en": "rush out with shoes on backwards in eager welcome"}
        ],
        "character_decomposition": [
            {
                "character": "好",
                "pinyin": "hào",
                "meaning_en": "be fond of; love; like (4th tone)",
                "meaning_es": "amar; gustar; ser aficionado a (4to tono)",
                "radical": "女",
                "radical_meaning_en": "woman",
                "meaning_component": "女 (woman/mother)",
                "sound_component": "子 (child)",
                "stroke_count": 6,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram showing a loving mother 女 embracing her newborn child 子; pronounced hào when expressing fondness.",
                "visual_mnemonic_story_en": "A fond mother (女) lovingly cradles her sweet child (子), showing deep affection and love (好).",
                "visual_mnemonic_story_es": "Una madre abnegada (女) abraza a su pequeño (子), reflejando entrañable apego y gusto (好).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "VND",
                "traditional": ""
            },
            {
                "character": "客",
                "pinyin": "kè",
                "meaning_en": "guest; visitor; traveler; customer",
                "meaning_es": "huésped; invitado; forastero; cliente",
                "radical": "宀",
                "radical_meaning_en": "roof",
                "meaning_component": "宀 (sheltering roof)",
                "sound_component": "各 (gè, arrival of person from another place)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ideogram showing an individual 各 from another location arriving under the household roof 宀 as a respected guest.",
                "visual_mnemonic_story_en": "Under the warm roof (宀), travelers from various regions (各) are welcomed as honored guests (客).",
                "visual_mnemonic_story_es": "Bajo el alero hospitalario (宀), visitantes de diversos confines (各) son acogidos como huéspedes (客).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "JHER",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "A generous heart that loves (好, hào) to welcome travelers under the roof as guests (客) is truly hospitable (好客).",
            "composite_memory_hook_es": "Quien ama de corazón (好, hào) recibir a viajeros bajo su techo como huéspedes (客) es hospitalario (好客).",
            "cultural_and_cognitive_roots": "Derived from classical Chinese virtue ethics; in ancient China, hosting traveling scholars and wanderers (养客) was considered the supreme badge of chivalric honor and generosity.",
            "tone_sandhi_and_pitch_modulation": "Two falling tones: 'hào kè' (51-51). Note the crucial 4th tone on 'hào' (meaning 'to be fond of'); do not pronounce as 3rd tone hǎo."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "如", "pinyin": "rú", "meaning_en": "as if; like", "distinction_note": "Has 口 on right instead of 子"},
                {"character": "容", "pinyin": "róng", "meaning_en": "contain; tolerate", "distinction_note": "Has 谷 below 宀 instead of 各"},
                {"character": "家", "pinyin": "jiā", "meaning_en": "family", "distinction_note": "Has pig 豕 below 宀 instead of 各"},
                {"character": "安", "pinyin": "ān", "meaning_en": "peaceful", "distinction_note": "Has 女 below 宀 instead of 各"}
            ],
            "etymological_cognates": [
                {"character": "嗜", "pinyin": "shì", "gloss_en": "addicted to; fond of flavor"},
                {"character": "宾", "pinyin": "bīn", "gloss_en": "esteemed guest; visitor at court"},
                {"character": "朋", "pinyin": "péng", "gloss_en": "friend; companion; two strings of cowries"},
                {"character": "友", "pinyin": "yǒu", "gloss_en": "friend; two clasped hands"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "好客 specifically characterizes an enthusiastic, warm disposition toward entertaining visitors and treating guests well.",
            "contrasts": [
                {"id": "1", "compared_word": "好客 vs. 热情", "pinyin": "rèqíng", "analysis": "热情 is a broad personality trait describing general warmth, zeal, or energy in any situation, while 好客 is restricted to receiving guests and travelers."},
                {"id": "2", "compared_word": "好客 vs. 友善", "pinyin": "yǒushàn", "analysis": "友善 means amicable and kind to others, whereas 好客 specifically implies opening one's home and table to visitors."},
                {"id": "3", "compared_word": "好客 vs. 周到", "pinyin": "zhōudào", "analysis": "周到 emphasizes thorough, flawless attentiveness in service or protocol, while 好客 emphasizes genuine emotional enthusiasm for guests."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "山里人天性纯朴好客，哪怕家境并不宽裕，逢有陌生旅人借宿，也总会杀鸡宰鸭拿出最好的存粮款待。围坐在暖融融的柴火堆旁，听着老人讲述山间古老的传说，那种毫无防备的赤诚与善意，足以驱散长途跋涉的所有严寒。",
                "pinyin": "Shānlǐ rén tiānxìng chūnpǔ hàokè, nǎpà jiājìng bìng bù kuānyù, féng yǒu mòshēng lǚrén jièsù, yě zǒng huì shājī-zǎiyā ná chū zuì hǎo de cúnliáng kuǎndài. Wéizuò zài nuǎnróngróng de cháihuǒduī páng, tīng zhe lǎorén jiǎngshù shānjiān gǔlǎo de chuánshuō, nà zhǒng háowú-fángbèi de chìchéng yǔ shànyì, zúyǐ qūsàn chángtú bǎshè de suǒyǒu yánhán.",
                "en": "Mountain folk are naturally hospitable; even with modest means, when strangers seek shelter they prepare their best provisions. Sitting by the crackling woodfire listening to mountain legends, their warmth dispels all chills of the journey.",
                "es": "Los montañeses son hospitalarios por naturaleza; aun con pocos recursos, ante un viajero perdido preparan sus mejores viandas. Al calor del fuego de leña, escuchando viejas leyendas, su generosa calidez disipa el frío del camino."
            },
            {
                "id": "#2",
                "hanzi": "“好客中国”不仅是享誉世界的国家旅游名片，更是中华优秀传统文化中“有朋自远方来，不亦乐乎”的当代传承。在各大国际经贸展会与体育盛事中，志愿者们以真诚热忱的好客之礼迎接四海宾朋，向世界生动展现了礼仪之邦的大国风范。",
                "pinyin": "'Hàokè Zhōngguó' bùjǐn shì xiǎngyù shìjiè de guójiā lǚyóu míngpiàn, gèng shì Zhōnghuá yōuxiù chuántǒng wénhuà zhōng 'yǒu péng zì yuǎnfāng lái, bú yì lè hū' de dāngdài chuánchéng. Zài gèdà guójì jīngmào zhǎnhuì yǔ tǐyù shèngshì zhōng, zhìyuànzhěmen yǐ zhēnchéng rèchén de hàokè zhī lǐ yíngjiē sìhǎi bīnpéng, xiàng shìjiè shēngdòng zhǎnxiàn le lǐyí-zhī-bāng de dàguó fēngfàn.",
                "en": "'Hospitable China' reflects the ancient teaching: 'To have friends come from afar, is this not delightful?' In international expos and tournaments, volunteers greet global guests with sincere hospitality, displaying civilizational elegance.",
                "es": "'China hospitalaria' evoca el milenario lema de Confucio: '¿No es un gozo recibir amigos de tierras lejanas?'. En cumbres y torneos internacionales, los voluntarios acogen al forastero con afabilidad, mostrando la hidalguía de una nación de protocolo."
            }
        ]
    },

    # 25 呼朋唤友
    {
        "id": "25",
        "hanzi": "呼朋唤友",
        "pinyin": "hū péng huàn yǒu",
        "part_of_speech": "Idiom",
        "meanings_summary": {
            "en": "to invite friends; to gather companions together; to call on cronies",
            "es": "convocar a los amigos; reunir a la pandilla; llamar a los compadres"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Idiom",
                "register": "Standard",
                "definition_en": "calling out to summon friends, comrades, and companions to gather, celebrate, or act together",
                "definition_es": "llamar o convocar a amigos y compañeros para congregarse, salir de excursión o celebrar juntos",
                "example_phrase": "呼朋唤友去聚餐 (call friends together to have a meal)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "春暖花开的时节，大学生们常常呼朋唤友前往郊野公园踏青野餐，享受大自然的美丽风光。",
                "pinyin": "Chūnnuǎn-huākāi de shíjié, dàxuéshēngmen chángcháng hūpéng-huànyǒu qiánwǎng jiāoyě gōngyuán tàqīng yěcān, xiǎngshòu dàzìrán de měilì fēngguāng.",
                "en": "When spring blossoms bloom, university students often gather friends together to hike in suburban parks, enjoying nature's beauty.",
                "es": "Cuando la primavera florece, los universitarios suelen reunir a los amigos para salir de campo al parque campestre y disfrutar del sol."
            },
            {
                "id": "#2",
                "hanzi": "每逢发了稿费或有朋自远方来，鲁迅先生总爱呼朋唤友前往熟悉的绍兴酒馆，推杯换盏纵论古今。",
                "pinyin": "Měiféng fā le gǎofèi huò yǒu péng zì yuǎnfāng lái, Lǔ Xùn xiānsheng zǒng ài hūpéng-huànyǒu qiánwǎng shúxī de Shàoxīng jiǔguǎn, tuībēi-huànzhǎn zònglùn-gǔjīn.",
                "en": "Whenever royalties arrived or friends came from afar, Mr. Lu Xun loved gathering companions to local taverns, toasting and debating history.",
                "es": "Al cobrar honorarios o recibir visitas de fuera, Lu Xun convocaba a su círculo de amigos hacia las tabernas de Shaoxing para brindar y charlar."
            }
        ],
        "collocations": [
            {"hanzi": "呼朋唤友去聚会", "en": "gather friends to attend a party"},
            {"hanzi": "呼朋唤友出门", "en": "call friends together to go out"},
            {"hanzi": "呼朋唤友来做客", "en": "invite friends over as guests"},
            {"hanzi": "呼朋唤友踏青", "en": "gather companions for a spring outing"},
            {"hanzi": "呼朋唤友共饮", "en": "call friends together for drinks"},
            {"hanzi": "呼朋唤友游玩", "en": "gather friends for leisure and recreation"}
        ],
        "idioms": [
            {"hanzi": "招兵买马", "pinyin": "zhāo bīng mǎi mǎ", "meaning_en": "recruit troops and buy horses; assemble personnel"},
            {"hanzi": "走南闯北", "pinyin": "zǒu nán chuǎng běi", "meaning_en": "travel throughout south and north; journey far and wide"},
            {"hanzi": "引类呼朋", "pinyin": "yǐn lèi hū péng", "meaning_en": "gather one's ilk and summon cronies"},
            {"hanzi": "三五成群", "pinyin": "sān wǔ chéng qún", "meaning_en": "in small groups of threes and fives"}
        ],
        "character_decomposition": [
            {
                "character": "呼",
                "pinyin": "hū",
                "meaning_en": "call; shout; exhale; summon",
                "meaning_es": "llamar; clamar; exhalar; gritar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth shouting)",
                "sound_component": "乎 (hū, breath / exclamation)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where open mouth 口 exhales sound with vocal force 乎 to call out.",
                "visual_mnemonic_story_en": "Opening the mouth (口) wide to shout outward into the open air (乎) calls out to distant friends (呼).",
                "visual_mnemonic_story_es": "Abrir la boca (口) de par en par para soltar la voz al aire (乎) llama a los compadres (呼).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "RHFD",
                "traditional": ""
            },
            {
                "character": "朋",
                "pinyin": "péng",
                "meaning_en": "friend; companion; associate",
                "meaning_es": "amigo; camarada; compañero",
                "radical": "月",
                "radical_meaning_en": "moon / cowrie",
                "meaning_component": "月 (ancient cowrie shells strung together)",
                "sound_component": "朋 (péng)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Oracle bone pictogram showing two matched strings of precious cowrie currency, symbolizing equal, bonded friends.",
                "visual_mnemonic_story_en": "Two matching strands of lustrous cowrie shells hang side by side, symbolizing bonded peers and friends (朋).",
                "visual_mnemonic_story_es": "Dos hileras gemelas de conchas preciosas penden juntas, simbolizando amigos inseparables (朋).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "BB",
                "traditional": ""
            },
            {
                "character": "唤",
                "pinyin": "huàn",
                "meaning_en": "call; summon; awaken; shout",
                "meaning_es": "llamar; convocar; despertar; vocear",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (mouth)",
                "sound_component": "奂 (huàn, brilliant change / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character combining mouth 口 with 奂, signifying raising the voice to summon or awaken.",
                "visual_mnemonic_story_en": "Using the mouth (口) to utter a vibrant clear sound (奂) awakens and summons companions (唤).",
                "visual_mnemonic_story_es": "Con la boca (口) se emite una voz sonora (奂) para despertar y convocar a los cercanos (唤).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "RNBK",
                "traditional": ""
            },
            {
                "character": "友",
                "pinyin": "yǒu",
                "meaning_en": "friend; companion; friendly",
                "meaning_es": "amigo; compañero; fraterno",
                "radical": "又",
                "radical_meaning_en": "right hand",
                "meaning_component": "又 (hand) + 𠂇 (hand reaching together)",
                "sound_component": "友 (yǒu)",
                "stroke_count": 4,
                "composition_type": "半包围结构",
                "etymology_and_mnemonic": "Oracle bone pictogram of two right hands 又 reaching out to clasp each other in warm mutual assistance.",
                "visual_mnemonic_story_en": "Two hands reach out in the same direction, clasping together in lifelong loyal friendship (友).",
                "visual_mnemonic_story_es": "Dos manos amigas se extienden en el mismo sentido, estrechándose en fraternal lealtad (友).",
                "tone_mnemonic_anchor": "214",
                "cangjie": "KE",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Shout out (呼) to your peers (朋) and summon (唤) your dear friends (友) to gather merrily (呼朋唤友).",
            "composite_memory_hook_es": "Clama en voz alta (呼) a los compadres (朋) y convoca (唤) a los amigos (友) para festejar juntos (呼朋唤友).",
            "cultural_and_cognitive_roots": "A classic four-character idiom reflecting traditional Chinese communal sociability; conveys an upbeat, festive atmosphere of spontaneous companionship and merry gatherings.",
            "tone_sandhi_and_pitch_modulation": "Level, rising, falling, dipping: 'hū péng huàn yǒu' (55-35-51-214). A rich four-syllable pitch arc moving through all four classic tone contours."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "呼吸", "pinyin": "hūxī", "meaning_en": "breathe", "distinction_note": "吸 has 及 on right instead of 乎"},
                {"character": "服", "pinyin": "fú", "meaning_en": "clothes; obey", "distinction_note": "Has 月 on left, but 𠬝 on right instead of another 月 in 朋"},
                {"character": "换", "pinyin": "huàn", "meaning_en": "exchange; change", "distinction_note": "Has hand radical 扌 on left instead of mouth 口 in 唤"},
                {"character": "发", "pinyin": "fā", "meaning_en": "send out; hair", "distinction_note": "Has top stroke crossing with dot, distinct from 友"}
            ],
            "etymological_cognates": [
                {"character": "叫", "pinyin": "jiào", "gloss_en": "shout; call out aloud"},
                {"character": "招", "pinyin": "zhāo", "gloss_en": "beckon with hand; recruit"},
                {"character": "邀", "pinyin": "yāo", "gloss_en": "invite along the path"},
                {"character": "聚", "pinyin": "jù", "gloss_en": "gather together like flock"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "呼朋唤友 depicts a lively, festive scene of joyously gathering friends and companions for leisure, outings, or dining.",
            "contrasts": [
                {"id": "1", "compared_word": "呼朋唤友 vs. 结党营私", "pinyin": "jiédǎng-yíngsī", "analysis": "呼朋唤友 has a cheerful, wholesome, or neutral lifestyle tone, while 结党营私 is an idiom describing corrupt conspiratorial faction-building."},
                {"id": "2", "compared_word": "呼朋唤友 vs. 走亲访友", "pinyin": "zǒuqīn-fǎngyǒu", "analysis": "走亲访友 refers specifically to formal family holiday visits to relatives, while 呼朋唤友 conveys casual, high-spirited peer gatherings."},
                {"id": "3", "compared_word": "呼朋唤友 vs. 聚众闹事", "pinyin": "jùzhòng-nàoshì", "analysis": "聚众闹事 denotes illegal riotous mob behavior, completely antithetical to friendly 呼朋唤友."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "金秋十月的周末天高气爽，红叶染透了漫山遍野。平日里忙碌奔波的年轻人纷纷呼朋唤友，背起行囊去登高赏秋。大家坐在山顶的巨石上分享零食畅聊心事，爽朗的笑声穿透松林，在湛蓝的天空下激荡出青春最欢畅的乐章。",
                "pinyin": "Jīnqiū shíyuè de zhòumò tiāngāo-qìshuǎng, hóngyè rǎntòu le mànshān-biànyě. Píngrì lǐ mánglù bēnbō de niánqīngrén fēnfēn hūpéng-huànyǒu, bēiqǐ xíngnáng qù dēnggāo shǎngqiū. Dàjiā zuò zài shāndǐng de jùshí shàng fēnxiǎng língshí chàngliáo xīnshì, shuǎnglǎng de xiàoshēng chuāntòu sōnglín, zài zhànlán de tiānkōng xià jīdàng chū qīngchūn zuì huānchàng de yuèzhāng.",
                "en": "On an autumn weekend under crisp skies, red leaves blanketed hills. Busy youths gathered companions, packing bags to hike. Sharing snacks on summit boulders and chatting freely, clear laughter echoed through pines, celebrating youth.",
                "es": "En un límpido fin de semana de otoño, las hojas tiñen las laderas. Jóvenes atareados convocan a los amigos para coronar la cumbre. Compartiendo viandas sobre las peñas, sus risas francas cruzan los pinares celebrando la juventud."
            },
            {
                "id": "#2",
                "hanzi": "文人结社与雅集是近代中国知识界独特的生活方式。无论是在北京胡同里的小酌论道，还是在上海租界的咖啡厅畅谈新思潮，先辈们常常呼朋唤友共同商讨办刊启蒙救国之策。思想的火花在频繁的友人聚会中激烈迸发，推动了时代巨浪。",
                "pinyin": "Wénrén jiéshè yǔ yǎjí shì jìndài Zhōngguó zhīshijiè dútè de shēnghuó fāngshì. Wúlùn shì zài Běijīng hútòng lǐ de xiǎozhuó lùndào, háishì zài Shànghǎi zūjiè de kāfēitīng chàngtán xīn sīcháo, xiānbèimen chángcháng hūpéng-huànyǒu gòngtóng shāngtǎo bànkān qǐmēng jiùguó zhī cè. Sīxiǎng de huǒhuā zài pínfán de yǒurén jùhuì zhōng jīliè bèngfā, tuīdòng le shídài jùlàng.",
                "en": "Literati salons were a hallmark of modern Chinese intellectuals. Whether sipping wine in Beijing hutongs or discussing ideas in Shanghai cafes, predecessors gathered companions to deliberate publications. Sparks from these meetings drove historical tides.",
                "es": "Las tertulias letradas marcaron a la intelectualidad moderna. Ya fuera brindando en los callejones de Pekín o debatiendo en cafés de Shanghái, los próceres reunían amigos para fundar revistas y abrir mentes, desatando olas históricas."
            }
        ]
    },

    # 26 招待
    {
        "id": "26",
        "hanzi": "招待",
        "pinyin": "zhāo dài",
        "part_of_speech": "Verb",
        "meanings_summary": {
            "en": "to receive guests; to entertain; to treat; reception; hospitality",
            "es": "atender; recibir; agasajar; hospedar; convidar; recepción"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Verb",
                "register": "Standard",
                "definition_en": "to welcome, provide food and lodging for, and look after guests with courtesy",
                "definition_es": "recibir, dar de comer, alojar o agasajar a los invitados con atenciones y cortesía",
                "example_phrase": "热情招待来宾 (warmly entertain incoming guests)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "逢年过节，祖母总会提前准备好满满一桌丰盛的家乡菜肴，热情招待前来拜年的亲朋好友。",
                "pinyin": "Féngnián-guòjié, zǔmǔ zǒng huì tíqián zhǔnbèi hǎo mǎnmǎn yì zhuō fēngshèng de jiāxiāng càiyáo, rèqíng zhāodài qiánlái bàinián de qīnpéng-hǎoyǒu.",
                "en": "During holidays, grandmother prepares a full table of lavish hometown dishes to warmly entertain relatives and friends visiting for New Year.",
                "es": "En las festividades, la abuela prepara de antemano una opípara mesa de platos tradicionales para agasajar a los allegados que vienen a felicitar."
            },
            {
                "id": "#2",
                "hanzi": "在近代北京文人圈子中，鲁迅以生性好客著称，广和居的“碎金白菜”是他用来招待知心朋友的招牌菜。",
                "pinyin": "Zài jìndài Běijīng wénrén quānzi zhōng, Lǔ Xùn yǐ shēngxìng hàokè zhùchēng, Guǎnghéjū de 'suìjīn báicài' shì tā yòng lái zhāodài zhīxīn péngyou de zhāopái cài.",
                "en": "In modern Beijing literary circles, Lu Xun was famous for hospitality; Guangheju's signature shredded cabbage was his favorite treat for close friends.",
                "es": "En los cenáculos letrados de Pekín, Lu Xun descollaba por su hospitalidad; la col dorada del mesón Guangheju era su plato predilecto para convidar amigos."
            }
        ],
        "collocations": [
            {"hanzi": "热情招待", "en": "warmly entertain"},
            {"hanzi": "招待所", "en": "guesthouse; hostel"},
            {"hanzi": "招待会", "en": "reception conference (e.g. press conference)"},
            {"hanzi": "盛情招待", "en": "lavish and generous hospitality"},
            {"hanzi": "设宴招待", "en": "host a banquet to entertain"},
            {"hanzi": "招待不周", "en": "apologize for inadequate hospitality"}
        ],
        "idioms": [
            {"hanzi": "款待周到", "pinyin": "kuǎn dài zhōu dào", "meaning_en": "attentive and thoughtful entertainment of guests"},
            {"hanzi": "宾至如归", "pinyin": "bīn zhì rú guī", "meaning_en": "guests feel as comfortable as if at home"},
            {"hanzi": "设宴款待", "pinyin": "shè yàn kuǎn dài", "meaning_en": "arrange a banquet to entertain guests lavishly"},
            {"hanzi": "相敬如宾", "pinyin": "xiāng jìng rú bīn", "meaning_en": "treat each other with mutual respect like guests"}
        ],
        "character_decomposition": [
            {
                "character": "招",
                "pinyin": "zhāo",
                "meaning_en": "beckon; wave; summon; recruit; attract",
                "meaning_es": "hacer señas; convocar; reclutar; atraer",
                "radical": "扌",
                "radical_meaning_en": "hand",
                "meaning_component": "扌 (hand beckoning)",
                "sound_component": "召 (zhào, summon / phonetic)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where hand radical 扌 beckons with gestures to summon 召 someone forward.",
                "visual_mnemonic_story_en": "A welcoming hand (扌) gestures warmly, calling (召) guests forward to enter the feast (招).",
                "visual_mnemonic_story_es": "Una mano amable (扌) hace señas con presteza, llamando (召) al visitante hacia el banquete (招).",
                "tone_mnemonic_anchor": "55",
                "cangjie": "QSHR",
                "traditional": ""
            },
            {
                "character": "待",
                "pinyin": "dài",
                "meaning_en": "treat; wait; receive; entertain",
                "meaning_es": "atender; esperar; tratar; hospedar",
                "radical": "彳",
                "radical_meaning_en": "step",
                "meaning_component": "彳 (step / approach on road)",
                "sound_component": "寺 (sì, temple / law court / phonetic)",
                "stroke_count": 9,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ideogram showing standing on a path 彳 with courtly decorum 寺, waiting to receive arriving guests.",
                "visual_mnemonic_story_en": "Standing respectfully along the pathway (彳) near the temple hall (寺), a host waits to attend (待) to guests.",
                "visual_mnemonic_story_es": "Apostado en la senda (彳) junto al pabellón (寺), el anfitrión aguarda para atender con esmero (待) a los huéspedes.",
                "tone_mnemonic_anchor": "51",
                "cangjie": "HOGDI",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Beckon warmly with your hand (招) and wait attentively by the threshold (待) to entertain guests (招待).",
            "composite_memory_hook_es": "Haz señas acogedoras con la mano (招) y aguarda en el umbral (待) para agasajar a los invitados (招待).",
            "cultural_and_cognitive_roots": "Derived from classical host-guest ritual (宾主之礼); emphasizes respectful reception, providing seating, tea, and warm culinary comfort.",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'zhāo dài' (55-51). Articulate 'zhāo' with a steady high pitch 55, then descend firmly on 'dài'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "召", "pinyin": "zhào", "meaning_en": "summon; call", "distinction_note": "Lacks the hand radical 扌 of 招"},
                {"character": "绍", "pinyin": "shào", "meaning_en": "introduce; connect", "distinction_note": "Has silk radical 纟 on left instead of 扌"},
                {"character": "侍", "pinyin": "shì", "meaning_en": "attend upon; serve", "distinction_note": "Has person radical 亻 on left instead of double-step 彳"},
                {"character": "持", "pinyin": "chí", "meaning_en": "hold; grasp", "distinction_note": "Has hand radical 扌 on left instead of 彳"}
            ],
            "etymological_cognates": [
                {"character": "款", "pinyin": "kuǎn", "gloss_en": "entertain with sincere funds"},
                {"character": "接", "pinyin": "jiē", "gloss_en": "receive; touch hands with"},
                {"character": "延", "pinyin": "yán", "gloss_en": "extend invitation; prolong"},
                {"character": "遇", "pinyin": "yù", "gloss_en": "meet; encounter on path"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "招待 focuses on hosting, serving food, and providing lodging and hospitality for guests or attendees.",
            "contrasts": [
                {"id": "1", "compared_word": "招待 vs. 款待", "pinyin": "kuǎndài", "analysis": "款待 is more formal and emphasizes deeply generous, lavish, and heartfelt hospitality, while 招待 applies to both grand banquets and basic guesthouse services."},
                {"id": "2", "compared_word": "招待 vs. 接待", "pinyin": "jiēdài", "analysis": "接待 emphasizes the organizational, administrative protocol of receiving delegations at doors, while 招待 emphasizes dining, drinking, and hosting."},
                {"id": "3", "compared_word": "招待 vs. 招待所", "pinyin": "zhāodàisuǒ", "analysis": "招待所 is the physical noun for modest state/institutional guesthouses, while 招待 is the universal verb."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "中国传统的待客之道，最见人间温情。哪怕家中清贫，主人也会倾其所有端出最好的饭菜招待远客。饭桌上频频劝菜的热忱，临别前塞进行囊的土特产，无不浸润着古老农耕文明中最朴素、最真挚的善良与厚道。",
                "pinyin": "Zhōngguó chuántǒng de dàikè zhī dào, zuì jiàn rénjiān wēnqíng. Nǎpà jiāzhōng qīngpín, zhǔrén yě huì qīng qí suǒyǒu duānchū zuì hǎo de fàncài zhāodài yuǎnkè. Fànzhuō shàng pínpín quàncài de rèchén, línbié qián sāijìn xíngnáng de tǔtèchǎn, wúbù jìnrùn zhe gǔlǎo nónggēng wénmíng zhōng zuì pǔsù, zuì zhēnzhì de shànliáng yǔ hòudào.",
                "en": "Traditional Chinese hospitality best reveals human warmth. Even in poverty, hosts offer their finest food. Urging extra servings at table and tucking local snacks into departing travelers' bags radiates heartfelt agrarian kindness.",
                "es": "La hospitalidad tradicional china destila calidez humana. Aun en la escasez, el dueño de casa ofrece sus mejores manjares. Rogar que repitan plato y regalar viandas para el viaje refleja la entrañable bondad del mundo rural."
            },
            {
                "id": "#2",
                "hanzi": "在大型国际经贸论坛期间，新闻发布厅与招待会现场秩序井然。组委会不仅精心安排了同声传译与多语种咨询服务，更在晚宴上以融合中西特色的精美冷餐招待中外媒体记者，高效务实的组织工作赢得了与会代表的广泛赞誉。",
                "pinyin": "Zài dàxíng guójì jīngmào lùntán qījiān, xīnwén fābùtīng yǔ zhāodàihuì xiànchǎng zhìxù-jǐngrán. Zǔwěihuì bùjǐn jīngxīn ānpái le tóngshēng-chuányì yǔ duō yǔzhǒng zīxún fúwù, gèng zài wǎnyàn shàng yǐ rónghé zhōng-xī tèsè de jīngměi lěngcān zhāodài zhōng-wài méitǐ jìzhě, gāoxiào wùshí de zǔzhī gōngzuò yíngdé le yùhuì dàibiǎo de guǎngfàn zànyù.",
                "en": "During international economic forums, press halls and receptions run in perfect order. Providing simultaneous translation and hosting journalists with exquisite fusion dinners, the efficient organizing team won broad praise from delegates.",
                "es": "En los foros económicos mundiales, las recepciones de prensa discurren con pulcritud. La organización dispuso traducción simultánea y agasajó a los corresponsales con una cena fusión, ganándose el reconocimiento general por su eficacia."
            }
        ]
    },

    # 27 高档
    {
        "id": "27",
        "hanzi": "高档",
        "pinyin": "gāo dàng",
        "part_of_speech": "Adjective",
        "meanings_summary": {
            "en": "high-grade; top-quality; upscale; high-end; superior",
            "es": "de alta gama; de primera calidad; exclusivo; selecto; de lujo"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adjective",
                "register": "Standard",
                "definition_en": "of superior quality, high price, exquisite material, or upscale market grade",
                "definition_es": "de calidad superior, precio elevado, acabados esmerados o gama comercial exclusiva",
                "example_phrase": "高档消费品 (high-end consumer goods)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "商业步行街两侧林立着各类高档时装旗舰店与珠宝专柜，在璀璨的霓虹灯下显得格外繁华。",
                "pinyin": "Shāngyè bùxíngjiē liǎngcè línlì zhe gèlèi gāodàng shízhuāng qíjiàndiàn yǔ zhūbǎo zhuānguì, zài cuǐcàn de níhóngdēng xià xiǎnde géwài fánhuá.",
                "en": "Both sides of the pedestrian street are lined with high-end fashion flagships and jewelry counters, looking exceptionally bustling under neon lights.",
                "es": "A ambos lados del bulevar peatonal se alinean tiendas de alta costura y joyerías selectas, que lucen vibrantes bajo las luces de neón."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅宴请文友并不盲目迷信昂贵的高档酒楼，而是更看重菜品的独特风味与席间无拘无束的谈兴。",
                "pinyin": "Lǔ Xùn yànqǐng wényǒu bìng bù mángmù míxìn ángguì de gāodàng jiǔlóu, ér shì gèng kànzhòng càipǐn de dútè fēngwèi yǔ xíjiān wújū-wúshù de tánxìng.",
                "en": "When entertaining writer friends, Lu Xun never blindly worshipped costly high-end restaurants, valuing unique flavors and uninhibited conversation far more.",
                "es": "Al convidar amigos, Lu Xun no se desvivía por suntuosos mesones de postín, sino que apreciaba el sabor único y la tertulia desenfadada."
            }
        ],
        "collocations": [
            {"hanzi": "高档商品", "en": "high-end merchandise"},
            {"hanzi": "高档小区", "en": "upscale residential community"},
            {"hanzi": "高档餐厅", "en": "fine dining / upscale restaurant"},
            {"hanzi": "高档服装", "en": "high-grade apparel"},
            {"hanzi": "档次高", "en": "high caliber / high-grade"},
            {"hanzi": "高档耐用品", "en": "high-end durable goods"}
        ],
        "idioms": [
            {"hanzi": "美轮美奂", "pinyin": "měi lún měi huàn", "meaning_en": "magnificent and stately architectural beauty"},
            {"hanzi": "身价倍增", "pinyin": "shēn jià bèi zēng", "meaning_en": "value and social stature multiply dramatically"},
            {"hanzi": "物美价廉", "pinyin": "wù měi jià lián", "meaning_en": "excellent quality at low price (antonym nuance)"},
            {"hanzi": "琳琅满目", "pinyin": "lín láng mǎn mù", "meaning_en": "a feast for the eyes; dazzling array of precious goods"}
        ],
        "character_decomposition": [
            {
                "character": "高",
                "pinyin": "gāo",
                "meaning_en": "tall; high; lofty; superior",
                "meaning_es": "alto; elevado; superior; eminente",
                "radical": "高",
                "radical_meaning_en": "tall",
                "meaning_component": "高 (pictogram of a tall multistory tower)",
                "sound_component": "高 (gāo)",
                "stroke_count": 10,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram depicting a tall multistory watchtower with roof, terrace, and entrance archway.",
                "visual_mnemonic_story_en": "A towering watchtower (高) with lofty roofs and terraces rises above common city rooftops.",
                "visual_mnemonic_story_es": "Una atalaya señorial (高) con terrazas y tejados elevados descuella sobre las casas bajas.",
                "tone_mnemonic_anchor": "55",
                "cangjie": "YRBR",
                "traditional": ""
            },
            {
                "character": "档",
                "pinyin": "dàng",
                "meaning_en": "grade; file; shelf; pigeonhole; crosspiece",
                "meaning_es": "gama; categoría; estante; expediente",
                "radical": "木",
                "radical_meaning_en": "wood",
                "meaning_component": "木 (wooden shelves/dividers)",
                "sound_component": "当 (dāng, proper value / phonetic)",
                "stroke_count": 10,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Phono-semantic character where wooden shelving dividers 木 sort items into designated quality grades 当.",
                "visual_mnemonic_story_en": "Wooden shelves (木) divide merchandise into proper categories (当), sorting goods into distinct grades (档).",
                "visual_mnemonic_story_es": "Estantes de madera (木) clasifican los artículos según su valía (当) en distintas gamas (档).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "DFSM",
                "traditional": "檔"
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Goods placed on the highest (高) wooden shelf tier (档) represent top high-grade quality (高档).",
            "composite_memory_hook_es": "Las mercancías colocadas en el estante de madera (档) más alto (高) pertenecen a la gama superior (高档).",
            "cultural_and_cognitive_roots": "Derived from classical artisan categorization where goods were sorted on wooden racks (格档) into low, medium, and high tiers (低档, 中档, 高档).",
            "tone_sandhi_and_pitch_modulation": "Level high tone followed by falling tone: 'gāo dàng' (55-51). Articulate 'gāo' on level pitch 55, then drop crisply into 4th tone 'dàng'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "亮", "pinyin": "liàng", "meaning_en": "bright", "distinction_note": "Has 冖 and 儿 at bottom instead of 口 in 高"},
                {"character": "毫", "pinyin": "háo", "meaning_en": "hair", "distinction_note": "Has 毛 at bottom instead of 口 in 高"},
                {"character": "档", "pinyin": "dàng", "meaning_en": "file/grade", "distinction_note": "Has 木 on left; do not confuse with 挡 (hand radical 扌)"},
                {"character": "铛", "pinyin": "dāng", "meaning_en": "clang; pan", "distinction_note": "Has metal radical 钅 on left"}
            ],
            "etymological_cognates": [
                {"character": "级", "pinyin": "jí", "gloss_en": "tier; degree; silk steps"},
                {"character": "品", "pinyin": "pǐn", "gloss_en": "rank; quality; three mouths"},
                {"character": "优", "pinyin": "yōu", "gloss_en": "superior; abundant actor"},
                {"character": "贵", "pinyin": "guì", "gloss_en": "costly; noble; cowrie basket"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "高档 refers to upscale market classification, superior material quality, and high consumer pricing tier.",
            "contrasts": [
                {"id": "1", "compared_word": "高档 vs. 高级", "pinyin": "gāojí", "analysis": "高级 can describe abstract ranks, advanced engineering technology ('高级职称', '高级算法'), while 高档 strictly describes commercial goods, commodities, and venues."},
                {"id": "2", "compared_word": "高档 vs. 昂贵", "pinyin": "ángguì", "analysis": "昂贵 solely notes high monetary price, whereas 高档 implies refined materials, exquisite craftsmanship, and prestigious brand status."},
                {"id": "3", "compared_word": "高档 vs. 低档", "pinyin": "dīdàng", "analysis": "低档 (low-end / budget tier) is the direct commercial antonym of 高档."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "一个人的品位与格调，从不取决于消费了多少高档奢侈品，而在于对生活细节的专注与审美的纯粹。穿着质朴舒适的布衣，读着启迪智慧的经典，内心的安宁与自信便足以抵御世俗的浮华。真正的贵气，源于精神的丰盈。",
                "pinyin": "Yí ge rén de pǐnwèi yǔ gédiào, cóng bù qǔjué yú xiāofèi le duōshǎo gāodàng shēchǐpǐn, ér zàiyú duì shēnghuó xìjié de zhuānzhù yǔ shěnmǐ de chúncuì. Chuānzhe zhìpǔ shūshì de bùyī, dú zhe qǐdí zhìhuì de jīngdiǎn, nèixīn de ānníng yǔ zìxìn biàn zúyǐ dǐyù shìsú de fúhuá. Zhēnzhèng de guìqì, yuányú jīngshén de fēngyíng.",
                "en": "Taste and stature never depend on consuming high-end luxury, but on mindful attention to detail and pure aesthetics. Wearing simple cotton clothes and reading classics, inner peace and self-assurance easily withstand secular vanity.",
                "es": "La distinción no estriba en comprar lujos de alta gama, sino en cuidar los detalles con esmero. Vestir lino sobrio y leer a los clásicos brinda un sosiego y una seguridad que disipan la vanidad terrenal. La nobleza emana del espíritu."
            },
            {
                "id": "#2",
                "hanzi": "制造业向高端迈进是经济高质量发展的核心抓手。国内工业母机与高档数控机床研发团队通过突破多轴联动核心算法，全面打破了长期以来的外部技术垄断，不仅提升了高端装备制造国产化率，更为现代化工业体系构筑了坚固防线。",
                "pinyin": "Zhìzàoyè xiàng gāoduān màijìn shì jīngjì gāo zhìliàng fāzhǎn de héxīn zhuāshǒu. Guónèi gōngyè mǔjī yǔ gāodàng shùkòng jīchuáng yánfā tuánduì tōngguò tūpò duōzhóu liándòng héxīn suànfǎ, quánmiàn dǎpò le chángqī yǐlái de wàibù jìshù lǒngduàn, bùjǐn tíshēng le gāoduān zhuāngbèi zhìzào guóchǎnhuà lǜ, gèng wèi xiàndàihuà gōngyè tǐxì gòuzhù le jiāngù fángxiàn.",
                "en": "Stepping into high-end manufacturing drives economic quality. Breaching monopolies in high-grade CNC machine tools and core algorithms, domestic teams raised domestic equipment ratios, fortifying defenses for modern industry.",
                "es": "El avance hacia la alta gama fabril dinamiza la economía. Los equipos de mecanizado avanzado rompieron monopolios técnicos al desarrollar algoritmos propios, elevando la cuota de producción nacional y blindando la industria moderna."
            }
        ]
    },

    # 28 胃口
    {
        "id": "28",
        "hanzi": "胃口",
        "pinyin": "wèi kǒu",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "appetite; liking; taste; interest; ambition",
            "es": "apetito; ganas de comer; gusto; inclinación; ambición"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "physiological desire for food; physical appetite",
                "definition_es": "deseo fisiológico de ingerir alimentos; apetito corporal",
                "example_phrase": "胃口很好 (have a very good appetite)"
            },
            {
                "sense_number": "2",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "interest, taste, or appetite for specific arts, activities, or business ventures",
                "definition_es": "inclinación, afición, gusto o ambición por determinados temas o proyectos",
                "example_phrase": "不对胃口 (not to one's liking/taste)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "这道酸辣爽口的开胃小菜色泽诱人，让人一尝之下顿时胃口大开，连吃了两碗白米饭。",
                "pinyin": "Zhè dào suānlà shuǎngkǒu de kāiwèi xiǎocài sèzé yòurén, ràng rén yì cháng zhīxià dùnshí wèikǒu dà kāi, lián chī le liǎng wǎn bái mǐfàn.",
                "en": "This sour and spicy appetizer is enticing; tasting it immediately stimulated my appetite, so I ate two bowls of rice in a row.",
                "es": "Este aperitivo agridulce y crujiente abre el apetito con su color seductor; tras catarlo comí dos cuencos de arroz seguidos."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅晚年虽然胃病时常发作，但每逢故乡好友带来绍兴梅干菜与糟肉，他依然胃口极佳地品尝几筷。",
                "pinyin": "Lǔ Xùn wǎnnián suīrán wèibìng shícháng fāzuò, dàn měiféng gùxiāng hǎoyǒu dàilái Shàoxīng méigāncài yǔ zāoròu, tā yīrán wèikǒu jí jiā de pǐncháng jǐ kuài.",
                "en": "Although suffering frequent stomach trouble in later years, whenever hometown friends brought Shaoxing dried mustard greens and wine pork, he tasted them with great appetite.",
                "es": "Pese a padecer achaques de estómago en sus últimos años, cuando paisanos le traían carne curada de Shaoxing comía con gran apetito."
            }
        ],
        "collocations": [
            {"hanzi": "胃口大开", "en": "have one's appetite whetted"},
            {"hanzi": "没有胃口", "en": "have no appetite"},
            {"hanzi": "吊胃口", "en": "keep someone on tenterhooks; whet appetite"},
            {"hanzi": "合胃口", "en": "suit one's taste/liking"},
            {"hanzi": "坏了胃口", "en": "spoil one's appetite"},
            {"hanzi": "胃口不小", "en": "have big ambition/appetite"}
        ],
        "idioms": [
            {"hanzi": "津津有味", "pinyin": "jīn jīn yǒu wèi", "meaning_en": "with great relish; thoroughly enjoyable"},
            {"hanzi": "狼吞虎咽", "pinyin": "láng tūn hǔ yàn", "meaning_en": "wolf down food like wolves and tigers; ravenous"},
            {"hanzi": "食不甘味", "pinyin": "shí bù gān wèi", "meaning_en": "food lacks sweet flavor; too worried to eat with relish"},
            {"hanzi": "欲壑难填", "pinyin": "yù hè nán tián", "meaning_en": "abyss of desire is hard to fill; insatiable appetite"}
        ],
        "character_decomposition": [
            {
                "character": "胃",
                "pinyin": "wèi",
                "meaning_en": "stomach; digestive organ",
                "meaning_es": "estómago; órgano gástrico",
                "radical": "月",
                "radical_meaning_en": "moon / flesh",
                "meaning_component": "月 (flesh/organ)",
                "sound_component": "田 (tián, stomach grain granary pictogram)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram of the stomach sac storing grain 田 above the flesh radical 月/肉.",
                "visual_mnemonic_story_en": "A fleshy digestive sac (月) holding grains of food (田) represents the vital stomach organ (胃).",
                "visual_mnemonic_story_es": "Una bolsa carnosa (月) que almacena los granos ingeridos (田) representa el estómago (胃).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "WB",
                "traditional": ""
            },
            {
                "character": "口",
                "pinyin": "kǒu",
                "meaning_en": "mouth; opening; entrance; taste",
                "meaning_es": "boca; entrada; abertura; paladar",
                "radical": "口",
                "radical_meaning_en": "mouth",
                "meaning_component": "口 (pictogram of open human mouth)",
                "sound_component": "口 (kǒu)",
                "stroke_count": 3,
                "composition_type": "单一结构",
                "etymology_and_mnemonic": "Oracle bone pictogram depicting an open human mouth receiving sustenance.",
                "visual_mnemonic_story_en": "An open mouth (口) cheerfully receives delicious food to nourish the body.",
                "visual_mnemonic_story_es": "Una boca abierta (口) acoge gozosa los bocados para nutrir el organismo.",
                "tone_mnemonic_anchor": "214",
                "cangjie": "R",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "When the stomach (胃) desires food, the mouth (口) salivates with eager appetite (胃口).",
            "composite_memory_hook_es": "Cuando el estómago (胃) pide sustento, la boca (口) se abre con vivo apetito (胃口).",
            "cultural_and_cognitive_roots": "Metaphorical mapping between physical digestion and cognitive taste; Chinese treats intellectual interest ('duì wèikǒu', 对胃口) and ambitious desire ('wèikǒu dà', 胃口大) as bodily appetite.",
            "tone_sandhi_and_pitch_modulation": "Falling tone followed by dipping tone: 'wèi kǒu' (51-214). Pronounce 'wèi' firmly, followed by an undulating 3rd tone on 'kǒu'."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "骨", "pinyin": "gǔ", "meaning_en": "bone", "distinction_note": "Top structure has roof framing, unlike 田 in 胃"},
                {"character": "肖", "pinyin": "xiào", "meaning_en": "resemble", "distinction_note": "Has 小 at top instead of 田"},
                {"character": "日", "pinyin": "rì", "meaning_en": "sun", "distinction_note": "Has horizontal bar in center, unlike open square 口"},
                {"character": "中", "pinyin": "zhōng", "meaning_en": "middle", "distinction_note": "Has vertical stroke piercing through center of 口"}
            ],
            "etymological_cognates": [
                {"character": "食", "pinyin": "shí", "gloss_en": "eat; food; meal"},
                {"character": "脾", "pinyin": "pí", "gloss_en": "spleen; temperament in medicine"},
                {"character": "欲", "pinyin": "yù", "gloss_en": "desire; appetite; wish"},
                {"character": "嗜", "pinyin": "shì", "gloss_en": "addiction; taste for flavor"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "胃口 denotes physical hunger/desire to eat, or metaphorically represents taste, interest, or ambition.",
            "contrasts": [
                {"id": "1", "compared_word": "胃口 vs. 食欲", "pinyin": "shíyù", "analysis": "食欲 is a formal, medical/physiological term strictly referring to biological desire for food, while 胃口 is widely used idiomatically for taste ('吊胃口')."},
                {"id": "2", "compared_word": "胃口 vs. 兴趣", "pinyin": "xìngqù", "analysis": "兴趣 denotes general intellectual hobby or curious interest, while 胃口 when used metaphorically carries a zestful, hungry pursuit of a match."},
                {"id": "3", "compared_word": "胃口 vs. 胃病", "pinyin": "wèibìng", "analysis": "胃病 is clinical pathology (gastric disease), while 胃口 describes functional desire for food."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "心情舒畅的时候，粗茶淡饭也能吃得津津有味；心事重重之际，即便面对山珍海味也难有丝毫胃口。人生的胃口往往是内心境遇的晴雨表。学会卸下过重的精神包袱，放慢脚步体会当下的清欢，生活的滋味自然会甘之如饴。",
                "pinyin": "Xīnqíng shūchàng de shíhòu, chūchá-dànfàn yě néng chī de jīnjīn-yǒuwèi; xīnshì-chóngchóng zhī jì, jíbiàn miànduì shānzhēn-hǎiwèi yě nán yǒu sīháo wèikǒu. Rénshēng de wèikǒu wǎngwǎng shì nèixīn jìngyù de qíngyǔbiǎo. Xuéhuì xièxià guòzhòng de jīngshén bāofu, fàngmàn jiǎobù tǐhuì dāngxià de qīnghuān, shēnghuó de zīwèi zìrán huì gānzhī-rúyí.",
                "en": "When lighthearted, simple fare is savored; weighed down by worry, delicacies spark no appetite. Appetite mirrors the soul. Learning to unload burdens and slow down lets life's flavors become sweet again naturally.",
                "es": "Con el ánimo alegre, la comida humilde sabe a gloria; abrumado de pesares, los manjares no despiertan apetito. Las ganas de comer son barómetro del alma. Aliviar fardos y desacelerar permite saborear de nuevo la dulzura de vivir."
            },
            {
                "id": "#2",
                "hanzi": "在影视内容创作领域，盲目迎合市场的速食产品正在逐渐败坏受众的观影胃口。同质化严重的悬疑套路与低俗搞笑，引发了观众强烈的审美疲劳。唯有扎根现实生活、用心打磨剧本思想深度的原创精品，才能真正满足大众日益提升的文化胃口。",
                "pinyin": "Zài yǐngshì nèiróng chuàngzuò lǐngyù, mángmù yínghé shìchǎng de sùshí chǎnpǐn zhèngzài zhújiàn bàihuài shòuzhòng de guānyǐng wèikǒu. Tóngzhìhuà yánzhòng de xuányí tàolù yǔ dīsú gǎoxiào, yǐnfā le guānzhòng qiángliè de shěnmǐ pílào. Wéiyǒu zhāgēn xiànshí shēnghuó, yòngxīn dǎmó jùběn sīxiǎng shēndù de yuánchuàng jīngpǐn, cáinéng zhēnzhèng mǎnzú dàzhòng rìyì tíshēng de wénhuà wèikǒu.",
                "en": "In film and television, formulaic fast-food content spoils audience appetite. Clichéd plots cause aesthetic fatigue. Only genuine originals rooted in life with deep scripts can satisfy the public's rising cultural appetite.",
                "es": "En la creación audiovisual, los productos clónicos arruinan el paladar del espectador. El exceso de fórmulas manidas genera hastío. Solo guiones meditados con hondura humana satisfacen las exigencias de un público cada vez más formado."
            }
        ]
    },

    # 29 明明
    {
        "id": "29",
        "hanzi": "明明",
        "pinyin": "míng míng",
        "part_of_speech": "Adverb",
        "meanings_summary": {
            "en": "obviously; plainly; undoubtedly; clearly; manifestly (often introducing a contrast)",
            "es": "a todas luces; patentemente; a ojos vistas; evidentemente; cuando es bien sabido que"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Adverb",
                "register": "Standard",
                "definition_en": "plainly, visibly, or undeniably true; often used before a clause that highlights an unexpected contradiction or denial",
                "definition_es": "manifiestamente, a todas luces o a ojos vistas; suele contraponer una evidencia a una negación injustificada",
                "example_phrase": "明明知道却不说 (obviously know but refuse to say)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "天气预报明明说了今天全天有大暴雨，他出门时却偏偏不带伞，结果被淋成了落汤鸡。",
                "pinyin": "Tiānqì yùbào míngmíng shuō le jīntiān quántiān yǒu dà bàoyǔ, tā chūmén shí què piānpiān bú dài sǎn, jiéguǒ bèi línchéng le luòtāngjī.",
                "en": "The weather forecast plainly stated heavy rain all day, yet he stubbornly brought no umbrella and got soaked to the bone.",
                "es": "El parte meteorológico anunció claramente aguaceros para todo el día; él salió sin paraguas y acabó empapado como una sopa."
            },
            {
                "id": "#2",
                "hanzi": "鲁迅明明患有严重的胃病需要静养忌口，但面对好友热忱的邀约，他依然欣然前往，舍命陪君子。",
                "pinyin": "Lǔ Xùn míngmíng huànyǒu yánzhòng de wèibìng xūyào jìngyǎng jìkǒu, dàn miànduì hǎoyǒu rèchén de yāoyuē, tā yīrán xīnrán qiánwǎng, shěmìng péi jūnzǐ.",
                "en": "Lu Xun clearly suffered severe gastric troubles requiring diet restrictions, yet facing friends' warm invitations, he still joined happily.",
                "es": "Lu Xun padecía patentemente de males estomacales y debía guardar dieta; aun así, ante la invitación de amigos acudía solícito a departir."
            }
        ],
        "collocations": [
            {"hanzi": "明明知道", "en": "plainly know; know very well"},
            {"hanzi": "明明记得", "en": "distinctly remember"},
            {"hanzi": "明明看见", "en": "plainly saw with one's own eyes"},
            {"hanzi": "事实明明摆着", "en": "the facts are plainly evident"},
            {"hanzi": "明明在撒谎", "en": "obviously lying"},
            {"hanzi": "明明可以", "en": "clearly could have"}
        ],
        "idioms": [
            {"hanzi": "明察秋毫", "pinyin": "míng chá qiū háo", "meaning_en": "see down to the finest autumn down hair; clear discernment"},
            {"hanzi": "黑白分明", "pinyin": "hēi bái fēn míng", "meaning_en": "black and white are clearly demarcated; unmistakable"},
            {"hanzi": "洞若观火", "pinyin": "dòng ruò guān huǒ", "meaning_en": "as clear as looking at a bright blazing fire"},
            {"hanzi": "昭然若揭", "pinyin": "zhāo rán ruò jiē", "meaning_en": "abundantly manifest; exposed in broad daylight"}
        ],
        "character_decomposition": [
            {
                "character": "明",
                "pinyin": "míng",
                "meaning_en": "bright; clear; understand; obvious; dawn",
                "meaning_es": "claro; brillante; evidente; entender; alba",
                "radical": "日",
                "radical_meaning_en": "sun",
                "meaning_component": "日 (sun) / 囧 (window)",
                "sound_component": "月 (moon radiance)",
                "stroke_count": 8,
                "composition_type": "左右结构",
                "etymology_and_mnemonic": "Ancient ideogram pairing the solar disc 日 with the lunar crescent 月 (or window 囧), symbolizing radiant clarity.",
                "visual_mnemonic_story_en": "The brilliant sun (日) and glowing moon (月) shine together, illuminating all things with undeniable clarity (明).",
                "visual_mnemonic_story_es": "El sol radiante (日) y la luna llena (月) brillan juntos, alumbrando la verdad sin sombra de duda (明).",
                "tone_mnemonic_anchor": "35",
                "cangjie": "AB",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "Reduplicating bright light (明) upon bright clarity (明) makes an undeniable truth obvious and manifest (明明).",
            "composite_memory_hook_es": "Duplicar la luz clara (明) sobre la claridad evidente (明) hace que la verdad salte a la vista (明明).",
            "cultural_and_cognitive_roots": "Reduplication of 'míng' intensifies subjective certitude; used in rhetorical discourse when pointing out a glaring contrast between known reality and someone's evasive behavior.",
            "tone_sandhi_and_pitch_modulation": "Two rising tones: 'míng míng' (35-35). Two steady parallel upward sweeps from mid pitch to high."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "朋", "pinyin": "péng", "meaning_en": "friend", "distinction_note": "Has two moons 月 月 side-by-side instead of 日 and 月"},
                {"character": "昭", "pinyin": "zhāo", "meaning_en": "bright; manifest", "distinction_note": "Has 召 on right instead of 月"},
                {"character": "旺", "pinyin": "wàng", "meaning_en": "prosperous", "distinction_note": "Has 王 on right of 日 instead of 月"},
                {"character": "暗", "pinyin": "àn", "meaning_en": "dark; obscure", "distinction_note": "Has 音 on right; direct antonym of 明"}
            ],
            "etymological_cognates": [
                {"character": "显", "pinyin": "xiǎn", "gloss_en": "manifest; visible under sun"},
                {"character": "晰", "pinyin": "xī", "gloss_en": "clear; split wood under sun"},
                {"character": "彻", "pinyin": "chè", "gloss_en": "thorough; penetrating; lucid"},
                {"character": "白", "pinyin": "bái", "gloss_en": "white; clear; in vain"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "明明 is an adverb emphasizing an undeniable fact, almost always set against an unjustified denial or contradictory action.",
            "contrasts": [
                {"id": "1", "compared_word": "明明 vs. 明显", "pinyin": "míngxiǎn", "analysis": "明显 is an adjective meaning obvious or discernible ('明显的变化'), while 明明 is an adverb modifying verbs with contrastive emphasis ('他明明知道')."},
                {"id": "2", "compared_word": "明明 vs. 显然", "pinyin": "xiǎnrán", "analysis": "显然 means evidently or obviously deduced from clues ('显然他是对的'), while 明明 carries an emotional tone of indignation at contradiction."},
                {"id": "3", "compared_word": "明明 vs. 明确", "pinyin": "míngquè", "analysis": "明确 is an adjective/verb meaning explicit, unambiguous, or to clarify ('明确目标'), not an emphatic adverb."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "生活中最令人叹息的隔阂，莫过于彼此明明深爱着对方，却在赌气与沉默中渐行渐远。很多误会明明只需要一句坦诚的解释便能烟消云散，却偏偏被虚荣的面子硬生生演变成了经年遗憾。学会低头，才是成熟的开端。",
                "pinyin": "Shēnghuó zhōng zuì lìngrén tànxī de géhé, mòguòyú bǐcǐ míngmíng shēn'ài zhe duìfāng, què zài dǔqì yǔ chénmò zhōng jiànxíng-jiànyuǎn. Hěnduō wùhuì míngmíng zhǐ xūyào yí jù tǎnchéng de jiěshì biàn néng yānxiāo-yúnsàn, què piānpiān bèi xūróng de miànzi yìngshēngshēng yǎnbiàn chéng le jīngnián yíhàn. Xuéhuì dītóu, cáishì chéngshú de kāiduān.",
                "en": "Life's saddest distance is when two people clearly love each other yet drift apart in silence. Many misunderstandings plainly need only one sincere word to dissolve, yet pride turns them into regrets. Yielding is the start of maturity.",
                "es": "La mayor desazón surge cuando dos personas se quieren con evidencia, pero se distancian por orgullo. Muchos malentendidos se disiparían con una frase franca, mas la vanidad los torna pesares. Aprender a ceder es el principio de la madurez."
            },
            {
                "id": "#2",
                "hanzi": "科研求真最忌讳掩耳盗铃。实验数据明明已经出现了无法自圆其说的反常偏差，个别学者却为了迎合既定课题结论，试图对异常数值进行修饰遮掩。科学的大厦唯有建立在实事求是的铁证之上，任何侥幸弄虚作假终将被历史证伪。",
                "pinyin": "Kēyán qiúzhēn zuì jìhuì yǎn'ěr-dàolíng. Shíyàn shùjù míngmíng yǐjīng chūxiàn le wúfǎ zìyuán-qíshuō de fǎncháng piānchā, gèbié xuézhě què wèile yínghé jìdìng kètí jiélùn, shìtú duì yìcháng shùzhí jìnxíng xiūshì zhēyǎn. Kēxué de dàshà wéiyǒu jiànlì zài shíshì-qiúshì de tiězhèng zhīshàng, rènhé jiǎoxìng nòngxū-zuòjiǎ zhōng jiāng bèi lìshǐ zhèngwěi.",
                "en": "Scientific rigor abhors self-deception. Experimental data plainly shows anomalous discrepancies, yet some attempt to gloss over them to fit conclusions. Science must stand on ironclad evidence; falsification will inevitably be disproven by history.",
                "es": "En la ciencia está proscrito engañarse. Aunque los datos muestren a todas luces desvíos anómalos, maquillar cifras para encajar hipótesis falsea el rigor. El templo del saber se asienta sobre pruebas de hierro; la trampa sucumbe ante la verdad."
            }
        ]
    },

    # 30 胃
    {
        "id": "30",
        "hanzi": "胃",
        "pinyin": "wèi",
        "part_of_speech": "Noun",
        "meanings_summary": {
            "en": "stomach; gastric organ; belly",
            "es": "estómago; órgano digestivo gástrico"
        },
        "senses": [
            {
                "sense_number": "1",
                "part_of_speech": "Noun",
                "register": "Standard",
                "definition_en": "the muscular organ of the digestive tract in humans and animals where food is broken down",
                "definition_es": "órgano muscular del aparato digestivo de humanos y animales donde se descomponen los alimentos",
                "example_phrase": "保护胃部健康 (protect stomach health)"
            }
        ],
        "example_sentences": [
            {
                "id": "#1",
                "hanzi": "经常不规律进食和暴饮暴食极易损伤脆弱的胃黏膜，导致慢性胃炎等消化系统疾病发作。",
                "pinyin": "Jīngcháng bù guīlǜ jìnshí hé bàoyǐn-bàoshí jí yì sǔnshāng cuìruò de wèi niánmó, dǎozhì mànxìng wèiyán děng xiāohuà xìtǒng jíbìng fāzuò.",
                "en": "Irregular eating and bingeing easily damage the delicate stomach mucosa, triggering chronic gastritis and digestive ailments.",
                "es": "Comer a deshoras y darse atracones daña la mucosa gástrica, provocando gastritis crónica y desórdenes digestivos."
            },
            {
                "id": "#2",
                "hanzi": "根据鲁迅先生的日记与书信考证，他在北京和上海写作期间常年饱受胃病折磨，严重时夜不能寐。",
                "pinyin": "Gēnjù Lǔ Xùn xiānsheng de rìjì yǔ shūxìn kǎozhèng, tā zài Běijīng hé Shànghǎi xiězuò qījiān chángnián bǎoshòu wèibìng zhémó, yánzhòng shí yè bùnéng mèi.",
                "en": "Researching Lu Xun's diaries confirms he suffered year-round from stomach illness while writing, frequently kept awake at night.",
                "es": "Los diarios de Lu Xun atestiguan que padeció intensas dolencias de estómago mientras escribía, perdiendo el sueño en sus crisis."
            }
        ],
        "collocations": [
            {"hanzi": "胃病", "en": "stomach illness / gastric ailment"},
            {"hanzi": "胃痛", "en": "stomach ache / gastralgia"},
            {"hanzi": "暖胃", "en": "warm and comfort the stomach"},
            {"hanzi": "空腹伤胃", "en": "harm the empty stomach"},
            {"hanzi": "胃酸", "en": "gastric acid"},
            {"hanzi": "胃溃疡", "en": "gastric ulcer"}
        ],
        "idioms": [
            {"hanzi": "刮目相看", "pinyin": "guā mù xiāng kàn", "meaning_en": "rub one's eyes and look at someone with new respect"},
            {"hanzi": "痛定思痛", "pinyin": "tòng dìng sī tòng", "meaning_en": "reflect deeply on painful lessons after pain subsides"},
            {"hanzi": "养生之道", "pinyin": "yǎng shēng zhī dào", "meaning_en": "the way of preserving health and life"},
            {"hanzi": "饮鸩止渴", "pinyin": "yǐn zhèn zhǐ kě", "meaning_en": "drink poison to quench thirst; seek relief with disastrous means"}
        ],
        "character_decomposition": [
            {
                "character": "胃",
                "pinyin": "wèi",
                "meaning_en": "stomach; digestive sac",
                "meaning_es": "estómago; saco digestivo",
                "radical": "月",
                "radical_meaning_en": "moon / flesh",
                "meaning_component": "月 (flesh/body organ)",
                "sound_component": "田 (tián, granary storage chamber)",
                "stroke_count": 9,
                "composition_type": "上下结构",
                "etymology_and_mnemonic": "Ancient oracle bone pictogram of a fleshy muscular pouch 月 storing grain harvests 田 for digestion.",
                "visual_mnemonic_story_en": "A muscular organ pouch of flesh (月) receives grains from the rice fields (田) to digest in the stomach (胃).",
                "visual_mnemonic_story_es": "Una bolsa carnosa (月) asimila los granos del campo (田) para hacer la digestión gástrica (胃).",
                "tone_mnemonic_anchor": "51",
                "cangjie": "WB",
                "traditional": ""
            }
        ],
        "mnemonics_and_roots": {
            "composite_memory_hook_en": "The flesh pouch (月) that holds and digests field grains (田) is your vital stomach (胃).",
            "composite_memory_hook_es": "La bolsa carnosa (月) que digiere los granos del campo (田) es el estómago (胃).",
            "cultural_and_cognitive_roots": "Traditional Chinese Medicine (TCM) refers to the stomach as the 'Sea of Grain and Water' (水谷之海) and the minister of granaries (仓廪之官), vital for postnatal vitality.",
            "tone_sandhi_and_pitch_modulation": "Falling 4th tone: 'wèi' (51). Crisp, solid descending contour from pitch 5 to pitch 1."
        },
        "traps_and_cognates": {
            "look_alikes": [
                {"character": "骨", "pinyin": "gǔ", "meaning_en": "bone", "distinction_note": "Has 冎 at top instead of 田 in 胃"},
                {"character": "宵", "pinyin": "xiāo", "meaning_en": "night", "distinction_note": "Has roof 宀 at top instead of 田"},
                {"character": "渭", "pinyin": "wèi", "meaning_en": "Wei River", "distinction_note": "Has water radical 氵 on the left of 胃"},
                {"character": "谓", "pinyin": "wèi", "meaning_en": "say; tell", "distinction_note": "Has speech radical 讠 on the left of 胃"}
            ],
            "etymological_cognates": [
                {"character": "肚", "pinyin": "dù", "gloss_en": "belly; abdomen"},
                {"character": "肠", "pinyin": "cháng", "gloss_en": "intestines; bowels"},
                {"character": "腑", "pinyin": "fǔ", "gloss_en": "internal organs; entrails"},
                {"character": "脏", "pinyin": "zàng", "gloss_en": "viscera; internal anatomy"}
            ]
        },
        "semantic_boundary_contrasts": {
            "core_nuance": "胃 strictly denotes the anatomical stomach organ responsible for breaking down food.",
            "contrasts": [
                {"id": "1", "compared_word": "胃 vs. 肚子", "pinyin": "dùzi", "analysis": "肚子 is the broad colloquial word for the entire external belly or abdominal cavity, while 胃 is the specific internal organ."},
                {"id": "2", "compared_word": "胃 vs. 胃口", "pinyin": "wèikǒu", "analysis": "胃 is the physical organ, whereas 胃口 is appetite or psychological interest in something."},
                {"id": "3", "compared_word": "胃 vs. 肠胃", "pinyin": "chángwèi", "analysis": "肠胃 is a collective term for the entire gastrointestinal tract (stomach and intestines), while 胃 is solely the stomach."}
            ]
        },
        "extended_reading_passages": [
            {
                "id": "#1",
                "hanzi": "胃是人体中最敏感的情绪器官之一。长期的焦虑、紧张与熬夜，往往会通过神经系统迅速波及胃部，引起痉挛与隐痛。呵护好自己的胃，按时吃一顿温热的三餐，不仅是保持身体健康的底线，更是对疲惫心灵最温存的体恤。",
                "pinyin": "Wèi shì réntǐ zhōng zuì mǐngǎn de qíngxù qìguān zhīyī. Chángqī de jiāolǜ, jǐnzhāng yǔ áoyè, wǎngwǎng huì tōngguò shénjīng xìtǒng xùnsù bōjí wèibù, yǐnqǐ jìngluán yǔ yǐntòng. Hēhù hǎo zìjǐ de wèi, ànshí chī yí dùn wēnrè de sāncān, bùjǐn shì bǎochí shēntǐ jiànkāng de dǐxiàn, gèng shì duì píbèi xīnlíng zuì wēncún de tǐxù.",
                "en": "The stomach is one of the body's most sensitive emotional organs. Anxiety and sleep deprivation swiftly strike through the nervous system, causing cramps and aches. Caring for one's stomach with warm, regular meals is gentlest comfort.",
                "es": "El estómago es uno de los órganos más sensibles a las emociones. La ansiedad constante y el desvelo alteran los nervios, provocando cólicos. Cuidar la digestión y comer caliente a sus horas es el mayor mimo para un cuerpo fatigado."
            },
            {
                "id": "#2",
                "hanzi": "随着幽门螺旋杆菌筛查技术的广泛普及，我国早期胃癌的诊疗水平取得了长足进步。消化内科专家呼吁，四十岁以上高危人群应当定期接受无痛胃镜检查，做到早发现、早诊断、早干预，筑牢消化道肿瘤防控的坚固屏障。",
                "pinyin": "Suízhe yōumén luóxuángǎnjūn shāichá jìshù de guǎngfàn pǔjí, wǒguó zǎoqī wèiyán de zhěnliáo shuǐpǐng qǔdé le chángzú jìnbù. Xiāohuà nèikē zhuānjiā hūyù, sìshí suì yǐshàng gāowēi rénqún yīngdāng dìngqī jiēshòu wútòng wèijìng jiǎnchá, zuòdào zǎo fāxiàn, zǎo zhěnduàn, zǎo gānyù, zhùláo xiāohuàdào zhǒngliú fángkòng de jiāngù píngzhàng.",
                "en": "With widespread screening for H. pylori, early gastric cancer diagnosis has progressed significantly. Gastroenterologists urge those over 40 to undergo painless gastroscopy regularly for early detection and intervention.",
                "es": "Con el cribado de Helicobacter pylori, la detección precoz del cáncer gástrico ha avanzado a pasos agigantados. Los especialistas recomiendan gastroscopias preventivas a mayores de 40 años para atajar a tiempo cualquier anomalía."
            }
        ]
    }
]

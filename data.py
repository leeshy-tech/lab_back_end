database_user = "root"
database_password = "lisai430094"
database_table = "user"

# 中国图书馆分类法
category = {
    "马列毛邓":[
        ("A1","马克思恩格斯著作"),
        ("A2","列宁著作"),
        ("A3","斯大林著作"),
        ("A4","毛泽东著作"),
        ("A49","邓小平著作"),
        ("A5","马克思、恩格斯、列宁、斯大林、毛泽东、邓小平著作汇编"),
        ("A7","马克思、恩格斯、列宁、斯大林、毛泽东、邓小平生平和传记"),
        ("A8","马克思主义、列宁主义、毛泽东思想、邓小平理论的学习和研究")
    ],
    "哲学宗教":[
        ("B-4","哲学教育与普及"),
        ("B0","哲学理论"),
        ("B1","世界哲学"),
        ("B2","中国哲学"),
        ("B3","亚洲哲学"),
        ("B4","非洲哲学"),
        ("B5","欧洲哲学"),
        ("B6","大洋洲哲学"),
        ("B7","美洲哲学"),
        ("B80","思维科学"),
        ("B81","逻辑学（论理学）"),
        ("B82","伦理学（道德哲学）"),
        ("B83","美学"),
        ("B84","心理学"),
        ("B9","宗教")
    ],
    "社会科学总论":[
        ("C0","社会科学理论与方法论"),
        ("C1","社会科学现状及发展"),
        ("C2","社会科学机构、团体、会议"),
        ("C3","社会科学研究方法"),
        ("C4","社会科学教育与普及"),
        ("C5","社会科学丛书、文集、连续性出版物"),
        ("C6","社会科学参考工具书"),
        ("C7","社会科学文献检索工具书"),
        ("C8","统计学"),
        ("C91","社会学"),
        ("C92","人口学"),
        ("C93","管理学"),
        ("C94","系统科学"),
        ("C95","民族学"),
        ("C96","人才学"),
        ("C97","劳动科学")
    ],
    "政治法律":[
        ("D0","政治理论"),
        ("D1","国际共产主义运动"),
        ("D2","中国共产党"),
        ("D33/37","各国共产党"),
        ("D4","工人、农民、青年、妇女运动与组织"),
        ("D5","世界政治"),
        ("D6","中国政治"),
        ("D73/77","各国政治"),
        ("D8","外交、国际关系"),
        ("D9","法律"),
        ("DF","法律")
    ],
    "军事":[
        ("E0","军事理论"),
        ("E1","世界军事"),
        ("E2","中国军事"),
        ("E3/7","各国军事"),
        ("E8","战略学、战役学、战术学"),
        ("E9","军事技术"),
        ("E99","军事地形学、军事地理学")
    ],
    "经济":[
        ("F0","经济学"),
        ("F1","世界各国经济概况、经济史、经济地理"),
        ("F2","经济计划与管理"),
        ("F3","农业经济"),
        ("F4","工业经济"),
        ("F49","信息产业经济（总论）"),
        ("F5","交通运输经济"),
        ("F59","旅游经济"),
        ("F6","邮电经济"),
        ("F7","贸易经济"),
        ("F8","财政、金融")
    ],
    "文化科学教育体育":[
        ("G0","文化理论"),
        ("G1","世界各国文化与文化事业"),
        ("G2","信息与知识传播"),
        ("G3","科学、科学研究"),
        ("G4","教育"),
        ("G8","体育")
    ],
    "语言文字":[
        ("H0","语言学"),
        ("H1","汉语"),
        ("H2","中国少数民族语言"),
        ("H3","常用外国语"),
        ("H4","汉藏语系"),
        ("H5","阿尔泰语系（突厥-蒙古-通古斯语系）"),
        ("H61","南亚语系（澳斯特罗-亚细亚语系）"),
        ("H62","南印语系（达罗毗荼语系、德拉维达语系）"),
        ("H63","南岛语系（马来亚-玻里尼西亚语系）"),
        ("H64","东北亚诸语言"),
        ("H65","高加索语系（伊比利亚-高加索语系）"),
        ("H66","乌拉尔语系（芬兰-乌戈尔语系）"),
        ("H67","闪-含语系（阿非罗-亚细亚语系）"),
        ("H7","印欧语系"),
        ("H81","非洲诸语言"),
        ("H83","美洲诸语言"),
        ("H84","大洋洲诸语言"),
        ("H9","国际辅助语")
    ],
    "文学":[
        ("I0","文学理论"),
        ("I1","世界文学"),
        ("I2","中国文学"),
        ("I3/7","各国文学")
    ],
    "艺术":[
        ("J0","艺术理论"),
        ("J1","世界各国艺术概况"),
        ("J2","绘画"),
        ("J29","书法、篆刻"),
        ("J3","雕塑"),
        ("J4","摄影艺术"),
        ("J5","工艺美术"),
        ("J59","建筑艺术"),
        ("J6","音乐"),
        ("J7","舞蹈"),
        ("J8","戏剧艺术"),
        ("J9","电影、电视艺术")
    ],
    "历史地理":[
        ("K0","史学理论"),
        ("K1","世界史"),
        ("K2","中国史"),
        ("K3","亚洲史"),
        ("K4","非洲史"),
        ("K5","欧洲史"),
        ("K6","大洋洲史"),
        ("K7","美洲史"),
        ("K81","传记"),
        ("K85","文物考古"),
        ("K89","风俗习惯"),
        ("K9","地理")
    ],
    "自然科学总论":[
        ("N0","自然科学理论与方法论"),
        ("N1","自然科学现状及发展"),
        ("N2","自然科学机构、团体、会议"),
        ("N3","自然科学研究方法"),
        ("N4","自然科学教育与普及"),
        ("N5","自然科学丛书、文集、连续性出版物"),
        ("N6","自然科学参考工具书"),
        ("N7","自然科学文献检索工具"),
        ("N8","自然科学调查、考察"),
        ("N9","1自然研究、自然历史"),
        ("N93","非线性科学"),
        ("N94","系统科学"),
        ("N99","情报学、情报工作"),
    ],
    "数理科学和化学":[
        ("O1","数学"),
        ("O3","力学"),
        ("O4","物理学"),
        ("O6","化学"),
        ("O7","晶体学")
    ],
    "天文学地球科学":[
        ("P1","天文学"),
        ("P2","测绘学"),
        ("P3","地球物理学"),
        ("P4","大气科学（气象学）"),
        ("P5","地质学"),
        ("P7","海洋学"),
        ("P9","自然地理学")
    ],
    "生物科学":[
        ("Q-0","生物科学的理论与方法"),
        ("Q-1","生物科学现状与发展"),
        ("Q-3","生物科学的研究方法与技术"),
        ("Q-4","生物科学教育与普及"),
        ("Q-9","生物资源调查"),
        ("Q1","普通生物学"),
        ("Q2","细胞生物学"),
        ("Q3","遗传学"),
        ("Q4","生理学"),
        ("Q5","生物化学"),
        ("Q6","生物物理学"),
        ("Q7","分子生物学"),
        ("Q81","生物工程学（生物技术）"),
        ("Q89","环境生物学"),
        ("Q91","古生物学"),
        ("Q93","微生物学"),
        ("Q94","植物学"),
        ("Q95","动物学"),
        ("Q96","昆虫学"),
        ("Q98","人类学")
    ],
    "医药卫生":[
        ("R-0","一般理论"),
        ("R-1","现状与发展"),
        ("R-3","医学研究方法"),
        ("R1","预防医学、卫生学"),
        ("R2","中国医学"),
        ("R3","基础医学"),
        ("R4","临床医学"),
        ("R5","内科学"),
        ("R6","外科学"),
        ("R71","妇产科学"),
        ("R72","儿科学"),
        ("R73","肿瘤学"),
        ("R74","神经病学与精神病学"),
        ("R75","皮肤病学与性病学"),
        ("R76","耳鼻咽喉科学"),
        ("R77","眼科学"),
        ("R78","口腔科学"),
        ("R79","外国民族医学"),
        ("R8","特种医学"),
        ("R9","药学")
    ],
    "农业科学":[
        ("S-0","一般性理论"),
        ("S-1","农业科学技术现状与发展"),
        ("S-3","农业科学研究、试验"),
        ("S-9","农业经济"),
        ("S1","农业基础科学"),
        ("S2","农业工程"),
        ("S3","农学（农艺学）"),
        ("S4","植物保护"),
        ("S5","农作物"),
        ("S6","园艺"),
        ("S7","林业"),
        ("S8","畜牧、动物医学、狩猎、蚕、蜂"),
        ("S9","水产、渔业")
    ],
    "工业技术":[
        ("T-0","工业技术理论"),
        ("T-1","工业技术现状与发展"),
        ("T-2","机构、团体、会议"),
        ("T-6","参考工具书"),
        ("T-9","工业经济"),
        ("TB","一般工业技术"),
        ("TD","矿业工程"),
        ("TE","石油、天然气工业"),
        ("TF","冶金工业"),
        ("TG","金属学与金属工艺"),
        ("TH","机械、仪表工业"),
        ("TJ","武器工业"),
        ("TK","能源与动力工程"),
        ("TL","原子能技术"),
        ("TM","电工技术"),
        ("TN","无线电电子学、电信技术"),
        ("TP","自动化技术、计算机技术"),
        ("TQ","化学工业"),
        ("TS","轻工业、手工业"),
        ("TU","建筑科学"),
        ("TV","水利工程")
    ],
    "交通运输":[
        ("U-9","交通运输经济"),
        ("U1","综合运输"),
        ("U2","铁路运输"),
        ("U4","公路运输"),
        ("U6","水路运输"),
        ("U8","航空运输")
    ],
    "航空航天":[
        ("V1","航空、航天技术的研究与探索"),
        ("V2","航空"),
        ("V4","航天（宇宙航行）"),
        ("V7","航空、航天医学"),
    ],
    "环境科学安全科学":[
        ("X-0","环境科学理论"),
        ("X-1","环境科学技术现状与发展"),
        ("X-4","环境保护宣传教育及普及"),
        ("X-6","环境保护参考工具书"),
        ("X1","环境科学基础理论"),
        ("X2","社会与环境"),
        ("X3","环境保护管理"),
        ("X4","灾害及其防治"),
        ("X5","环境污染及其防治"),
        ("X7","废物处理与综合利用"),
        ("X8","环境质量评价与环境监测"),
        ("X9","安全科学")
    ],
    "综合性图书":[
        ("Z1","丛书"),
        ("Z2","百科全书、类书"),
        ("Z3","辞典"),
        ("Z4","论文集、全集、选集、杂著"),
        ("Z5","年鉴、年刊"),
        ("Z6","期刊、连续性出版物"),
        ("Z8","图书目录、文摘、索引")
    ]
}

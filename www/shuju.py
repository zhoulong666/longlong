import random
import time

a=0
while True:
    a += 1
    # 生成640221开头的12位随机数字
    random_number = ''.join(str(random.randint(0, 9)) for _ in range(12))
    number = "640221" + random_number

    # # 常见的英文名列表
    # first_names = ["James", "Mary", "John", "Picia", "Robert", "Jeifer", "Micel", "Linda", "Willi",
    #                "Elith", "David", "Barba","aaa","bbb","ccc","ddd","eee","fff","ggg","gfd","sssd","ggg","huj","jgtg","edrf","bhng","derf","hujh","ikuj","oplk","ju","hy","gbv","ed","cdxx"]
    # last_names = ["Smith", "Johns", "Willi", "Brown", "Jones", "Garca", "Miller", "Davis", "Rdrig",
    #               "Marti", "Hernan", "Lopez","qw","we","rt","yu","ui","op","as","df","fg","hj","jk","kl","zx","xc","cv","vb","bn","mj","nh","bgg","fvf","dcd","fyhdd"]
    # # 随机生成英文名字
    # def random_english_name():
    #     first_name = random.choice(first_names)  # 随机选择一个名字
    #     last_name = random.choice(last_names)  # 随机选择一个姓氏
    #     return first_name + " " + last_name
    # 打印随机生成的英文名字
    # ewe = random_english_name()


    # 随机生成“年-月-日”
    def random_date():
        year = random.randint(2010, 2024)  # 随机生成年份
        month = random.randint(1, 12)  # 随机生成月份
        day = random.randint(1, 28) if month == 2 else random.randint(1, 30) if month in [4, 6, 9,
                                                                                          11] else random.randint(1, 31)
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)


    numberp = random.randint(1, 9999999999)
    numbero = random.randint(1, 50000)
    numbert = random.randint(1, 9000)
    numbers = random.randint(11111111111,19988999999)
    sd=str(numbers)
    mvm=str(numbert)
    qpqp=str(numberp)
    klk=str(numbero)

    # 随机生成姓名
    import random

    # 姓氏列表
    surnames = ['张', '王', '李', '赵', '刘', '陈', '杨', '黄', '周', '吴', '严', '赵', '韩', '杰', '车', '浩', '吉','补','不','部','卜','别','簿','热','我','外','儿','诶','哦','饿','你','么','噢','怕','跑','批'
                '林', '龙', '东', '杭','房','模','零','其','欧','坡','全','的','迟','颇','卡','说','了','贴','肉','吃','这','在','像','琪','宝','那','球','千','午','曹','嫩','咩','妞','台']
    # 名字列表
    names = ['伟', '敏', '婷', '克', '宇', '静', '磊', '娜', '杰', '丽', '娟', '卷', '明', '格', '星', '鱼', '广', '肉', '浩', '吉','补','不','部','卜','别','簿','热','我','外','儿','诶','哦','饿','你',
             '动','都','电','如','并','哇','人','哦','撒','事','咯','体']
    namd=['丽', '娟', '卷', '明', '格', '星', '鱼', '广', '肉', '浩', '吉','补','不','部','卜','别','簿','热','我','外','儿','诶','哦','饿','你',
             '动','都','电','如','并','哇','人','哦','撒','事','咯','体','了','贴','肉','吃','这','在','像','琪','宝','那','球','千','午','曹','嫩','咩','妞']


    def generate_random_name():
        surname = random.choice(surnames)
        name = random.choice(names)
        wwx=random.choice(namd)
        return surname + name+wwx


    nnn = generate_random_name()


    # 随机生成“年-月-日”
    def random_date():
        year = random.randint(1900, 2100)  # 随机生成年份
        month = random.randint(1, 12)  # 随机生成月份
        day = random.randint(1, 28) if month == 2 else random.randint(1, 30) if month in [4, 6, 9,
                                                                                          11] else random.randint(1, 31)
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    # 随机生成“时:分:秒”
    def random_time():
        hour = random.randint(1, 23)  # 随机生成小时
        minute = random.randint(1, 59)  # 随机生成分钟
        second = random.randint(1, 59)  # 随机生成秒
        return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    # 生成完整的日期时间
    def random_datetime():
        date = random_date()
        time = random_time()
        return date + "?" + time


    # 打印随机生成的日期时间
    plp=random_datetime()

    import random

    # 定义一些常见的医院科室
    departments = [
        "内科", "外科", "儿科", "妇产科", "骨科",'五官科','麻痹科','麻醉科','风湿免疫科','急诊科','心脏大血管科','检验科','信息科','病理科','输血科','营养科','医学影像科','药学部','护理部','核医学部'
        "皮肤科", "眼科", "耳鼻喉科", "口腔科", "肿瘤科",
        "泌尿科", "神经科", "心血管科", "呼吸科", "消化科",
        "内分泌科", "血液科", "传染科", "精神科", "康复科"
    ]
    def generate_random_department():
        # 从科室列表中随机选择一个
        return random.choice(departments)


    import random

    # 定义一些常见的医院名称元素
    city_names = ["北京", "上海", "广州", "深圳", "西安", "南京", "武汉", "成都", "杭州", "重庆",'香港','台湾','海南','山东','庆阳','天水','陇南','福州','金昌','汕头','揭阳','惠州','珠海','鹤山','贵阳','六盘水','武当山','厦门','宣城','合肥','天津','吴川']
    hospital_types = ["人民医院", "中医院", "儿童医院", "妇幼保健院", "骨科医院", "肿瘤医院", "康复医院", "第三医院",'体检中心','牙科医院','第五人民医院','解放军医院','医养中心','老年人医院'
                      "第二医院", "大学附属医院"]
    prefixes = ["市", "省", "综合",'区','国际','县']


    def generate_random_hospital():
        # 随机组合城市名、医院类型、和前缀
        city = random.choice(city_names)
        prefix = random.choice(prefixes)
        hospital_type = random.choice(hospital_types)

        return f"{city}{prefix}{hospital_type}"


    # 测试生成随机医院名称
    for _ in range(1):  # 生成随机医院名称
        cxcx=generate_random_hospital()

    # 测试生成随机科室
    for _ in range(1):  # 生成随机科室
        aax=generate_random_department()


        # 随机生成“年-月-日”
        def random_date():
            year = random.randint(1900, 2015)
            month = random.randint(1, 12)  # 随机生成月份
            day = random.randint(1, 28) if month == 2 else random.randint(1, 30) if month in [4, 6, 9,
                                                                                              11] else random.randint(1,
                                                                                                                      31)
            return "{:04d}-{:02d}-{:02d}".format(year, month, day)


        # 打印随机生成的日期
        lll = random_date()


        def random_date():
            year =  random.randint(2080, 2100)
            month = random.randint(1, 12)  # 随机生成月份
            day = random.randint(1, 28) if month == 2 else random.randint(1, 30) if month in [4, 6, 9,
                                                                                              11] else random.randint(1,
                                                                                                                      31)
            return "{:04d}-{:02d}-{:02d}".format(year, month, day)


        # 打印随机生成的日期
        llm = random_date()

    # 打印随机生成的日期
    mmm = random_date()
    # print(number,plp,nnn,qpqp,klk,mvm,sd,aax,cxcx)
    # 某个条件满足时退出循环
    print(lll,llm)
    if a==10000:
        break
        print("循环结束")












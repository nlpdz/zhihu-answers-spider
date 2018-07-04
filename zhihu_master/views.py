# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

import requests
import json
import pymysql.cursors
from zhihu_master import models
from decimal import Decimal
from django.db.models import Q


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'cookies':'_zap=c7375486-4e80-4d04-ab23-a660131e26f0; q_c1=44470a028b2e42a7a7a5b0c95c7162d0|1505908172000|1502961616000; q_c1=44470a028b2e42a7a7a5b0c95c7162d0|1519874338000|1502961616000; aliyungf_tc=AQAAALQ+jSqytw4Ai1G3PTU8YYDVuSz3; _xsrf=79975523c9d0e71eabc822008e319fe7; l_n_c=1; l_cap_id="ZTMxODcxNDcwMmUzNDJhOTg4MjZkOTg3NWFlMTk1ZGE=|1519965266|87a6d04c92ccd8ef081bb6378b199c184c47d888"; r_cap_id="YjIxZmJkNTU2ODgxNDc1N2IxM2YyMDkwMDY1Y2ZkNmE=|1519965266|d05a248af174b2e683e8004f343f21063b3ab036"; cap_id="ZjA0MGQwOWFkNzhhNGUxN2I5MzY0NjhiM2YwMWY2YWM=|1519965266|a58c6aeac69689f1f7677a7e29c747c64572288a"; n_c=1; __utma=155987696.1220683017.1519965266.1519965266.1519965266.1; __utmc=155987696; __utmz=155987696.1519965266.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); capsion_ticket="2|1:0|10:1519965367|14:capsion_ticket|44:MWQyZjYzY2M1ZGYwNDhjZjllMDJiYTcxOGZhMjEzOGY=|ef641fd398c8517dc6c15da7cd91c7d52c5e86136e12e767f04a59711b450a9d"; z_c0="2|1:0|10:1519965376|4:z_c0|80:MS4xeWpPT0J3QUFBQUFtQUFBQVlBSlZUY0FpaGx2YnRNdUtUWjRHQm1PRHA0RUl3NWpIOHA3S3NRPT0=|d7c9c42a6ff17ad9ecde1086d30fecbbe1d264db6910cbc91082de8646bc58d4"; __utmv=155987696.|1=userId=952884057676181504=1; d_c0="AODsWitVOQ2PTqCYYL7_hSOM-kaQUAJh5PM=|1519965831"; infinity_uid="2|1:0|10:1519967198|12:infinity_uid|24:OTUyODg0MDU3Njc2MTgxNTA0|9962897b470ac1fe68597da5b7ca7188c6a20c6a8f61d070630a0e3fa50df4e2"; __utmt=1; __utmb=155987696.115.0.1519967549997',
}


# print('连接到mysql服务器...')
# db = pymysql.connect("localhost", "root", "123456", "zhihu_masters", charset="utf8")
# print('连接上了!')
# cursor = db.cursor()


# 连接mysql数据库
# def connect_to_mysql(table):
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS {}(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,bio VARCHAR(100) DEFAULT NULL,description VARCHAR(100) DEFAULT NULL,answer_count INT(11) DEFAULT NULL,zhihu_url VARCHAR(100) DEFAULT NULL,public_answer_count INT(8) DEFAULT NULL,user_id VARCHAR(100) DEFAULT NULL,user_name VARCHAR(100) DEFAULT NULL,gender INT(2) DEFAULT NULL,avatar_url VARCHAR(100) DEFAULT NULL,question_price INT(8) DEFAULT NULL,follower_count INT(8) DEFAULT NULL)".format(table))
#     print('创建{}表'.format(table))


def parse(url, table):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(type(response.text))
        data = json.loads(response.text)
        for item in data['data']:
            bio = item['bio']
            description = item['description']
            answer_count = item['answer_count']
            zhihu_url = str(item['zhihu_url'])
            public_answer_count = item['public_answer_count']
            user_id = str(item['id'])
            user_name = item['name']
            gender = item['gender']
            avatar_url = str(item['avatar_url'])
            question_price = item['question_price']
            follower_count = item['follower_count']

            if table.objects.filter(user_id=user_id):
                continue
            table.objects.create(bio=bio,description=description,answer_count=answer_count,zhihu_url=zhihu_url,
                                          public_answer_count=public_answer_count,user_id=user_id,user_name=user_name,
                                          gender=gender,avatar_url=avatar_url,question_price=question_price,follower_count=follower_count)
            print('数据入库...')

            # sql = "INSERT INTO {}".format(table)+"(bio, description, answer_count, zhihu_url, public_answer_count, user_id, user_name, gender, avatar_url, question_price, follower_count) VALUES('%s', '%s', '%d', '%s', '%d', '%s', '%s', '%d', '%s', '%d', '%d')" % (
            #     bio, description, answer_count, zhihu_url, public_answer_count, user_id, user_name, gender, avatar_url,
            #     question_price, follower_count)
            # try:
            #     cursor.execute(sql)
            #     db.commit()
            # except:
            #     pass


# 心理学
def xinlixue():
    print('正在爬取心理学类答主信息...')
    xinlixue_ = models.xinlixue
    # connect_to_mysql('xinlixue')
    for offset in range(61):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551432/answerers?limit=10&offset=%d' % (offset*10)
        # parse(url, 'xinlixue')
        parse(url,xinlixue_)
    print('完成')


# 医学
def yixue():
    print('正在爬取医学类答主信息...')
    yixue_ = models.yixue
    # connect_to_mysql('yixue')
    for offset in range(31):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19604128/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, yixue_)
    print('完成')


# 职业规划
def zhiyeguihua():
    print('正在爬取职业规划类答主信息...')
    zhiyeguihua_ = models.zhiyeguihua
    # connect_to_mysql('zhiyeguihua')
    for offset in range(10):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19560641/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, zhiyeguihua_)
    print('完成')


# 理财
def licai():
    print('正在爬取理财类答主信息...')
    licai_ = models.licai
    # connect_to_mysql('licai')
    for offset in range(3):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19555939/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, licai_)
    print('完成')


# 法律
def falv():
    print('正在爬取法律类答主信息...')
    falv_ = models.falv
    # connect_to_mysql('falv')
    for offset in range(26):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550874/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, falv_)
    print('完成')


# 创业
def chuangye():
    print('正在爬取创业类答主信息...')
    chuangye_ = models.chuangye
    # connect_to_mysql('chuangye')
    for offset in range(12):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550560/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, chuangye_)
    print('完成')


# 房地产
def fangdichan():
    print('正在爬取房地产类答主信息...')
    fangdichan_ = models.fangdichan
    # connect_to_mysql('fangdichan')
    for offset in range(4):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19555355/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, fangdichan_)
    print('完成')


# 保险
def baoxian():
    print('正在爬取保险类答主信息...')
    baoxian_ = models.baoxian
    # connect_to_mysql('baoxian')
    for offset in range(2):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19562045/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, baoxian_)
    print('完成')


# 旅游
def lvyou():
    print('正在爬取旅游类答主信息...')
    lvyou_ = models.lvyou
    # connect_to_mysql('lvyou')
    for offset in range(9):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551469/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, lvyou_)
    print('完成')


# 汽车
def qiche():
    print('正在爬取汽车类答主信息...')
    qiche_ = models.qiche
    # connect_to_mysql('qiche')
    for offset in range(15):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551915/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, qiche_)
    print('完成')


# 儿童教育
def ertongjiaoyu():
    print('正在爬取儿童教育类答主信息...')
    ertongjiaoyu_ = models.ertongjiaoyu
    # connect_to_mysql('ertongjiaoyu')
    for offset in range(9):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19556671/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, ertongjiaoyu_)
    print('完成')


# 时间管理
def shijianguanli():
    print('正在爬取时间管理类答主信息...')
    shijianguanli_ = models.shijianguanli
    # connect_to_mysql('shijianguanli')
    for offset in range(1):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550921/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, shijianguanli_)
    print('完成')


# 摄影
def sheying():
    print('正在爬取摄影类答主信息...')
    sheying_ = models.sheying
    # connect_to_mysql('sheying')
    for offset in range(12):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551388/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, sheying_)
    print('完成')


# 语言学习
def yuyanxuexi():
    print('正在爬取语言学习类答主信息...')
    yuyanxuejxi_ = models.yuyanxuexi
    # connect_to_mysql('yuyanxuexi')
    for offset in range(1):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19585374/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, yuyanxuejxi_)
    print('完成')


# 电影
def dianyan():
    print('正在爬取电影类答主信息...')
    dianyan_ = models.dianyan
    # connect_to_mysql('dianyan')
    for offset in range(64):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550429/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, dianyan_)
    print('完成')


# 游戏
def youxi():
    print('正在爬取游戏类答主信息...')
    youxi_ = models.youxi
    # connect_to_mysql('youxi')
    for offset in range(36):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550994/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, youxi_)
    print('完成')


# 音乐
def yinyue():
    print('正在爬取音乐类答主信息...')
    yinyue_ = models.yinyue
    # connect_to_mysql('yinyue')
    for offset in range(17):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19550453/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, yinyue_)
    print('完成')


# 时尚
def shishang():
    print('正在爬取时尚类答主信息...')
    shishang_ = models.shishang
    # connect_to_mysql('shishang')
    for offset in range(15):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551052/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, shishang_)
    print('完成')


# 健身
def jianshen():
    print('正在爬取健身类答主信息...')
    jianshen_ = models.jianshen
    # connect_to_mysql('jianshen')
    for offset in range(15):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19552192/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, jianshen_)
    print('完成')


# 美食
def meishi():
    print('正在爬取美食类答主信息...')
    meishi_ = models.meishi
    # connect_to_mysql('meishi')
    for offset in range(26):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19551137/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, meishi_)
    print('完成')


# 食品安全
def shipinanquan():
    print('正在爬取食品安全类答主信息...')
    shipinanquan_ = models.shipinanquan
    # connect_to_mysql('shipinanquan')
    for offset in range(2):
        url = 'https://www.zhihu.com/zhi/infinity/topics/19562435/answerers?limit=10&offset=%d' % (offset * 10)
        parse(url, shipinanquan_)
    print('完成')


# 爬取数据
def spider(request):
    xinlixue()
    yixue()
    zhiyeguihua()
    licai()
    falv()
    chuangye()
    fangdichan()
    baoxian()
    lvyou()
    qiche()
    ertongjiaoyu()
    shijianguanli()
    sheying()
    yuyanxuexi()
    dianyan()
    youxi()
    yinyue()
    shishang()
    jianshen()
    meishi()
    shipinanquan()
    return render(request, "spider.html")


# 答主回答问题所需金额分析
def pay_money_statistics(request):

    xinlixue_pay = models.xinlixue.objects.filter()
    yixue_pay = models.yixue.objects.filter()
    zhiyeguihua_pay = models.zhiyeguihua.objects.filter()
    licai_pay = models.licai.objects.filter()
    falv_pay = models.falv.objects.filter()
    chuangye_pay = models.chuangye.objects.filter()
    fangdichan_pay = models.fangdichan.objects.filter()
    baoxian_pay = models.baoxian.objects.filter()
    lvyou_pay = models.lvyou.objects.filter()
    qiche_pay = models.qiche.objects.filter()
    ertongjiaoyu_pay = models.ertongjiaoyu.objects.filter()
    shijianguanli_pay = models.shijianguanli.objects.filter()
    sheying_pay = models.sheying.objects.filter()
    yuyanxuexi_pay = models.yuyanxuexi.objects.filter()
    dianyan_pay = models.dianyan.objects.filter()
    youxi_pay = models.youxi.objects.filter()
    yinyue_pay = models.yinyue.objects.filter()
    shishang_pay = models.shishang.objects.filter()
    jianshen_pay = models.jianshen.objects.filter()
    meishi_pay = models.meishi.objects.filter()
    shipinanquan_pay = models.shipinanquan.objects.filter()
    number = []
    number.append(len(xinlixue_pay))
    number.append(len(yixue_pay))
    number.append(len(zhiyeguihua_pay))
    number.append(len(licai_pay))
    number.append(len(falv_pay))
    number.append(len(chuangye_pay))
    number.append(len(fangdichan_pay))
    number.append(len(baoxian_pay))
    number.append(len(lvyou_pay))
    number.append(len(qiche_pay))
    number.append(len(ertongjiaoyu_pay))
    number.append(len(shijianguanli_pay))
    number.append(len(sheying_pay))
    number.append(len(yuyanxuexi_pay))
    number.append(len(dianyan_pay))
    number.append(len(youxi_pay))
    number.append(len(yinyue_pay))
    number.append(len(shishang_pay))
    number.append(len(jianshen_pay))
    number.append(len(meishi_pay))
    number.append(len(shipinanquan_pay))


    # 各类别，金额总和
    count = []
    xinlixue_price_count = question_price_all(xinlixue_pay) / 100
    yixue_price_count = question_price_all(yixue_pay) / 100
    zhiyeguihua_price_count = question_price_all(zhiyeguihua_pay) / 100
    licai_price_count = question_price_all(licai_pay) / 100
    falv_price_count = question_price_all(falv_pay) / 100
    chuangye_price_count = question_price_all(chuangye_pay) / 100
    fangdichan_price_count = question_price_all(fangdichan_pay) / 100
    baoxian_price_count = question_price_all(baoxian_pay) / 100
    lvyou_price_count = question_price_all(lvyou_pay) / 100
    qiche_price_count = question_price_all(qiche_pay) / 100
    ertongjiaoyu_price_count = question_price_all(ertongjiaoyu_pay) / 100
    shijianguanli_price_count = question_price_all(shijianguanli_pay) / 100
    sheying_price_count = question_price_all(sheying_pay) / 100
    yuyanxuexi_price_count = question_price_all(yuyanxuexi_pay) / 100
    dianyan_price_count = question_price_all(dianyan_pay) / 100
    youxi_price_count = question_price_all(youxi_pay) / 100
    yinyue_price_count = question_price_all(yinyue_pay) / 100
    shishang_price_count = question_price_all(shishang_pay) / 100
    jianshen_price_count = question_price_all(jianshen_pay) / 100
    meishi_price_count = question_price_all(meishi_pay) / 100
    shipinanquan_price_count = question_price_all(shipinanquan_pay) / 100
    count.append(xinlixue_price_count)
    count.append(yixue_price_count)
    count.append(zhiyeguihua_price_count)
    count.append(licai_price_count)
    count.append(falv_price_count)
    count.append(chuangye_price_count)
    count.append(fangdichan_price_count)
    count.append(baoxian_price_count)
    count.append(lvyou_price_count)
    count.append(qiche_price_count)
    count.append(ertongjiaoyu_price_count)
    count.append(shijianguanli_price_count)
    count.append(sheying_price_count)
    count.append(yuyanxuexi_price_count)
    count.append(dianyan_price_count)
    count.append(youxi_price_count)
    count.append(yinyue_price_count)
    count.append(shishang_price_count)
    count.append(jianshen_price_count)
    count.append(meishi_price_count)
    count.append(shipinanquan_price_count)

    # 各类别人均问价：
    ave = []
    xinlixue_price_ave = float('%.2f' % (xinlixue_price_count /len(xinlixue_pay)))
    yixue_price_ave = float('%.2f' % (yixue_price_count / len(yixue_pay)))
    zhiyeguihua_price_ave = float('%.2f' % (zhiyeguihua_price_count / len(zhiyeguihua_pay)))
    licai_price_ave = float('%.2f' % (licai_price_count / len(licai_pay)))
    falv_price_ave = float('%.2f' % (falv_price_count / len(falv_pay)))
    chuangye_price_ave = float('%.2f' % (chuangye_price_count / len(chuangye_pay)))
    fangdichan_price_ave = float('%.2f' % (fangdichan_price_count / len(fangdichan_pay)))
    baoxian_price_ave = float('%.2f' % (baoxian_price_count / len(baoxian_pay)))
    lvyou_price_ave = float('%.2f' % (lvyou_price_count / len(lvyou_pay)))
    qiche_price_ave = float('%.2f' % (qiche_price_count / len(qiche_pay)))
    ertongjiaoyu_price_ave = float('%.2f' % (ertongjiaoyu_price_count / len(ertongjiaoyu_pay)))
    shijianguanli_price_ave = float('%.2f' % (shijianguanli_price_count / len(shijianguanli_pay)))
    sheying_price_ave = float('%.2f' % (sheying_price_count / len(sheying_pay)))
    yuyanxuexi_price_ave = float('%.2f' % (yuyanxuexi_price_count / len(yuyanxuexi_pay)))
    dianyan_price_ave = float('%.2f' % (dianyan_price_count / len(dianyan_pay)))
    youxi_price_ave = float('%.2f' % (youxi_price_count / len(youxi_pay)))
    yinyue_price_ave = float('%.2f' % (yinyue_price_count / len(yinyue_pay)))
    shishang_price_ave = float('%.2f' % (shishang_price_count / len(shishang_pay)))
    jianshen_price_ave = float('%.2f' % (jianshen_price_count / len(jianshen_pay)))
    meishi_price_ave = float('%.2f' % (meishi_price_count / len(meishi_pay)))
    shipinanquan_price_ave = float('%.2f' % (shipinanquan_price_count / len(shipinanquan_pay)))
    ave.append(xinlixue_price_ave)
    ave.append(yixue_price_ave)
    ave.append(zhiyeguihua_price_ave)
    ave.append(licai_price_ave)
    ave.append(falv_price_ave)
    ave.append(chuangye_price_ave)
    ave.append(fangdichan_price_ave)
    ave.append(baoxian_price_ave)
    ave.append(lvyou_price_ave)
    ave.append(qiche_price_ave)
    ave.append(ertongjiaoyu_price_ave)
    ave.append(shijianguanli_price_ave)
    ave.append(sheying_price_ave)
    ave.append(yuyanxuexi_price_ave)
    ave.append(dianyan_price_ave)
    ave.append(youxi_price_ave)
    ave.append(yinyue_price_ave)
    ave.append(shishang_price_ave)
    ave.append(jianshen_price_ave)
    ave.append(meishi_price_ave)
    ave.append(shipinanquan_price_ave)

    name = ['心理学', '医学', '职业规划', '理财', '法律', '创业', '房地产', '保险', '旅游', '汽车', '儿童教育', '时间管理', '摄影', '语言学习', '电影', '游戏',
            '音乐', '时尚', '健身', '美食', '食品安全']
    number2 = []
    for i in number:
        number2.append(i / 100)

    count2 = []
    for i in count:
        count2.append(i/1000)


    z = zip(name, number, count, ave)


    return render(request, 'pay_money_statistics.html', {"z": z, 'anwser_number':json.dumps(number2), 'price_count': json.dumps(count2),'ave':json.dumps(ave)})


# 各类别，问答金额总和
def question_price_all(cls):
    price = 0
    for i in cls:
        price += i.question_price
    return price


# 各类别性别分析
def sex(request):
    # 数据库中gender = 1 和 -1为男， gender = 0 为女
    men_count = []
    women_count = []
    men_rate = []
    women_rate = []
    xinlixue_men = models.xinlixue.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    xinlixue_women = models.xinlixue.objects.filter(gender__exact=0)
    M_rate = Decimal(len(xinlixue_men)/len(models.xinlixue.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(xinlixue_men))
    women_count.append(len(xinlixue_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)


    yixue_men = models.yixue.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    yixue_women = models.yixue.objects.filter(gender__exact=0)
    M_rate = Decimal(len(yixue_men)/len(models.yixue.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(yixue_men))
    women_count.append(len(yixue_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    zhiyeguihua_men = models.zhiyeguihua.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    zhiyeguihua_women = models.zhiyeguihua.objects.filter(gender__exact=0)
    M_rate = Decimal(len(zhiyeguihua_men)/len(models.zhiyeguihua.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(zhiyeguihua_men))
    women_count.append(len(zhiyeguihua_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    licai_men = models.licai.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    licai_women = models.licai.objects.filter(gender__exact=0)
    M_rate = Decimal(len(licai_men)/len(models.licai.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(licai_men))
    women_count.append(len(licai_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    falv_men = models.falv.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    falv_women = models.falv.objects.filter(gender__exact=0)
    M_rate = Decimal(len(falv_men)/len(models.falv.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(falv_men))
    women_count.append(len(falv_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    chuangye_men = models.chuangye.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    chuangye_women = models.chuangye.objects.filter(gender__exact=0)
    M_rate = Decimal(len(chuangye_men)/len(models.chuangye.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(chuangye_men))
    women_count.append(len(chuangye_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    fangdichan_men = models.fangdichan.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    fangdichan_women = models.fangdichan.objects.filter(gender__exact=0)
    M_rate = Decimal(len(fangdichan_men)/len(models.fangdichan.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(fangdichan_men))
    women_count.append(len(fangdichan_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    baoxian_men = models.baoxian.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    baoxian_women = models.baoxian.objects.filter(gender__exact=0)
    M_rate = Decimal(len(baoxian_men)/len(models.baoxian.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(baoxian_men))
    women_count.append(len(baoxian_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    lvyou_men = models.lvyou.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    lvyou_women = models.lvyou.objects.filter(gender__exact=0)
    M_rate = Decimal(len(lvyou_men)/len(models.lvyou.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(lvyou_men))
    women_count.append(len(lvyou_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    qiche_men = models.qiche.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    qiche_women = models.qiche.objects.filter(gender__exact=0)
    M_rate = Decimal(len(qiche_men)/len(models.qiche.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(qiche_men))
    women_count.append(len(qiche_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    ertongjiaoyu_men = models.ertongjiaoyu.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    ertongjiaoyu_women = models.ertongjiaoyu.objects.filter(gender__exact=0)
    M_rate = Decimal(len(ertongjiaoyu_men)/len(models.ertongjiaoyu.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(ertongjiaoyu_men))
    women_count.append(len(ertongjiaoyu_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    shijianguanli_men = models.shijianguanli.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    shijianguanli_women = models.shijianguanli.objects.filter(gender__exact=0)
    M_rate = Decimal(len(shijianguanli_men)/len(models.shijianguanli.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(shijianguanli_men))
    women_count.append(len(shijianguanli_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    sheying_men = models.sheying.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    sheying_women = models.sheying.objects.filter(gender__exact=0)
    M_rate = Decimal(len(sheying_men)/len(models.sheying.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(sheying_men))
    women_count.append(len(sheying_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    yuyanxuexi_men = models.yuyanxuexi.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    yuyanxuexi_women = models.yuyanxuexi.objects.filter(gender__exact=0)
    M_rate = Decimal(len(yuyanxuexi_men)/len(models.yuyanxuexi.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(yuyanxuexi_men))
    women_count.append(len(yuyanxuexi_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    dianyan_men = models.dianyan.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    dianyan_women = models.dianyan.objects.filter(gender__exact=0)
    M_rate = Decimal(len(dianyan_men)/len(models.dianyan.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(dianyan_men))
    women_count.append(len(dianyan_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    youxi_men = models.youxi.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    youxi_women = models.youxi.objects.filter(gender__exact=0)
    M_rate = Decimal(len(youxi_men)/len(models.youxi.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(youxi_men))
    women_count.append(len(youxi_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    yinyue_men = models.yinyue.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    yinyue_women = models.yinyue.objects.filter(gender__exact=0)
    M_rate = Decimal(len(yinyue_men)/len(models.yinyue.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(yinyue_men))
    women_count.append(len(yinyue_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    shishang_men = models.shishang.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    shishang_women = models.shishang.objects.filter(gender__exact=0)
    M_rate = Decimal(len(shishang_men)/len(models.shishang.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(shishang_men))
    women_count.append(len(shishang_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    jianshen_men = models.jianshen.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    jianshen_women = models.jianshen.objects.filter(gender__exact=0)
    M_rate = Decimal(len(jianshen_men)/len(models.jianshen.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(jianshen_men))
    women_count.append(len(jianshen_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    meishi_men = models.meishi.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    meishi_women = models.meishi.objects.filter(gender__exact=0)
    M_rate = Decimal(len(meishi_men)/len(models.meishi.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(meishi_men))
    women_count.append(len(meishi_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    shipinanquan_men = models.shipinanquan.objects.filter(Q(gender__exact=1) | Q(gender__exact=-1))
    shipinanquan_women = models.shipinanquan.objects.filter(gender__exact=0)
    M_rate = Decimal(len(shipinanquan_men)/len(models.shipinanquan.objects.filter())).quantize(Decimal('0.00'))
    w_rate = 1 - M_rate
    men_count.append(len(shipinanquan_men))
    women_count.append(len(shipinanquan_women))
    men_rate.append(M_rate)
    women_rate.append(w_rate)

    name = ['心理学', '医学', '职业规划', '理财', '法律', '创业', '房地产', '保险', '旅游', '汽车', '儿童教育', '时间管理', '摄影', '语言学习', '电影', '游戏',
            '音乐', '时尚', '健身', '美食', '食品安全']

    z = zip(name, men_count, men_rate, women_count, women_rate)


    return render(request, 'sex.html', {"z": z, "men_count": json.dumps(men_count), "women_count": json.dumps(women_count)})


# top3答主推荐
def top3(request):
    answer_count = []
    user_name = []
    zhihu_url = []
    question_price = []
    follower_count = []

    xinlixue_top3 = models.xinlixue.objects.filter().order_by('-answer_count')[0:3]
    for i in xinlixue_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    yixue_top3 = models.yixue.objects.filter().order_by('-answer_count')[0:3]
    for i in yixue_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    zhiyeguihua_top3 = models.zhiyeguihua.objects.filter().order_by('-answer_count')[0:3]
    for i in zhiyeguihua_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    licai_top3 = models.licai.objects.filter().order_by('-answer_count')[0:3]
    for i in licai_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    falv_top3 = models.falv.objects.filter().order_by('-answer_count')[0:3]
    for i in falv_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    chuangye_top3 = models.chuangye.objects.filter().order_by('-answer_count')[0:3]
    for i in chuangye_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    fangdichan_top3 = models.fangdichan.objects.filter().order_by('-answer_count')[0:3]
    for i in fangdichan_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    baoxian_top3 = models.baoxian.objects.filter().order_by('-answer_count')[0:3]
    for i in baoxian_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    lvyou_top3 = models.lvyou.objects.filter().order_by('-answer_count')[0:3]
    for i in lvyou_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    qiche_top3 = models.qiche.objects.filter().order_by('-answer_count')[0:3]
    for i in qiche_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    ertongjiaoyu_top3 = models.ertongjiaoyu.objects.filter().order_by('-answer_count')[0:3]
    for i in ertongjiaoyu_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    shijianguanli_top3 = models.shijianguanli.objects.filter().order_by('-answer_count')[0:3]
    for i in shijianguanli_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    sheying_top3 = models.sheying.objects.filter().order_by('-answer_count')[0:3]
    for i in sheying_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    yuyanxuexi_top3 = models.yuyanxuexi.objects.filter().order_by('-answer_count')[0:3]
    for i in yuyanxuexi_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    dianyan_top3 = models.dianyan.objects.filter().order_by('-answer_count')[0:3]
    for i in dianyan_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    youxi_top3 = models.youxi.objects.filter().order_by('-answer_count')[0:3]
    for i in youxi_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    yinyue_top3 = models.yinyue.objects.filter().order_by('-answer_count')[0:3]
    for i in yinyue_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    shishang_top3 = models.shishang.objects.filter().order_by('-answer_count')[0:3]
    for i in shishang_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    jianshen_top3 = models.jianshen.objects.filter().order_by('-answer_count')[0:3]
    for i in jianshen_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    meishi_top3 = models.meishi.objects.filter().order_by('-answer_count')[0:3]
    for i in meishi_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)
    shipinanquan_top3 = models.shipinanquan.objects.filter().order_by('-answer_count')[0:3]
    for i in shipinanquan_top3:
        user_name.append(i.user_name)
        answer_count.append(i.answer_count)
        zhihu_url.append(i.zhihu_url)
        question_price.append(i.question_price/100)
        follower_count.append(i.follower_count)

    name = ['心理学top1','心理学top2','心理学top3', '医学top1','医学top2','医学top3', '职业规划top1','职业规划top2', '职业规划top3','理财top1','理财top2','理财top3', '法律top1','法律top2', '法律top3','创业top1','创业top2','创业top3', '房地产top1','房地产top2','房地产top3', '保险top1','保险top2','保险top3', '旅游top1', '旅游top2', '旅游top3','汽车top1','汽车top2','汽车top3', '儿童教育top1','儿童教育top2','儿童教育top3', '时间管理top1','时间管理top2','时间管理top3', '摄影top1','摄影top2','摄影top3', '语言学习top1','语言学习top2','语言学习top3', '电影top1','电影top2','电影top3', '游戏top1','游戏top2','游戏top3',
            '音乐top1','音乐top2','音乐top3', '时尚top1','时尚top2','时尚top3', '健身top1','健身top2','健身top3', '美食top1','美食top2','美食top3', '食品安全top1','食品安全top2','食品安全top3',]

    z = zip(name, user_name, zhihu_url, answer_count, question_price, follower_count)

    return render(request, 'top3.html', {"z": z})

















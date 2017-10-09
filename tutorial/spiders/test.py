# coding=utf-8
import random
import scrapy
from tutorial.items import ESFItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class ESFListSpider(scrapy.Spider):
    name = "esflist"
    # allowed_domains = ["fang.com"]
    # base_url = "http://esf.wuhan.fang.com/map/?mapmode=y&orderby=30&ecshop=ecshophouse&PageNo=$&a=ajaxSearch&city=wuhan&searchtype=loupan"
    base_url = "http://esf.wuhan.fang.com/map/?mapmode=y&orderby=30&ecshop=ecshophouse&PageNo=$&a=ajaxSearch&city=wuhan&searchtype=loupan"
    start_urls = []
    for i in range(2, 4):
        start_urls.append(str(base_url).replace("$", str(i)))
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    def parse(self, response):
        infos = response.xpath("//a/@href").extract()
        for i in infos:
            i_str = str(i).encode("utf-8")
            if "esf" in i_str:
                url = i_str.replace('\\', '').strip()
                yield scrapy.Request(url=url.replace("\"", ""), callback=self.parse_details)
    def parse_details(self, response):
        print "+++++++++++++被执行了+++++++++++++++++++"
        # print response
        # path
        xpath = "//body/div[@class='wid1200 clearfix']/div[@class='main clearfix']/div[@class='mainBoxL']"
        div_title = "//body/div[@class='xfline']/div[@class='xfline-c']/div[@class='xfline-cont']/div[@class='left']/span[@class='esf_xqname']/text()"
        total_price = "//body/div[@class='xfline']/div[@class='xfline-c']/div[@class='xfline-cont']/div[@class='left']/span[@class='esf_xqname']/text()"
        p_gray9 = "/p[@class='gray9']"
        h1 = "/h1"
        span_mr10 = "/span[@class='mr10']"
        div_houseInfor_clearfix = "/div[@class='houseInfor clearfix']"
        div_inforTxt = "/div[@class='inforTxt']"
        dl = "/dl"
        dt_gray6_zongjia1 = "/dt[@class='gray6 zongjia1']"
        span_red20b = "/span[@class='red20b']"
        dd_gray6 = "/dd[@class='gray6']"
        dd = "/dd"
        dt = "/dt"
        item = ESFItem()
        item['title'] = response.xpath(div_title).extract() # 标题
        item['total_price'] = response.xpath(div_title).extract() # 总价
        item['house_build_area'] = response.xpath(div_title).extract() # 建筑面积
        item['house_build_area'] = response.xpath(div_title).extract() # 单价
        item['house_build_area'] = response.xpath(div_title).extract() # 户型
        item['house_build_area'] = response.xpath(div_title).extract() # 朝向
        item['house_build_area'] = response.xpath(div_title).extract() # 楼层
        item['house_build_area'] = response.xpath(div_title).extract() # 装修
        item['house_build_area'] = response.xpath(div_title).extract() # 小区
        item['house_build_area'] = response.xpath(div_title).extract() # 区域
        item['house_build_area'] = response.xpath(div_title).extract() # 区域
		
        item['title'] = response.xpath(div_title).extract()
        print item['title']       
        return item
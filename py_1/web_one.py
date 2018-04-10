from bs4 import BeautifulSoup
import requests

url = 'http://scnj.58.com/sale.shtml'
url_host = 'http://scnj.58.com'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
for i in soup.select('ul.ym-submnu > li > b > a'):
    print(url_host + i.get('href'))

channel_list = '''
http://scnj.58.com/danche/
http://scnj.58.com/fzixingche/
http://scnj.58.com/diandongche/
http://scnj.58.com/sanlunche/
http://scnj.58.com/bijiben/
http://scnj.58.com/pbdn/
http://scnj.58.com/diannaopeijian/
http://scnj.58.com/zhoubianshebei/
http://scnj.58.com/shuma/
http://scnj.58.com/shumaxiangji/
http://scnj.58.com/mpsanmpsi/
http://scnj.58.com/youxiji/
http://scnj.58.com/jiadian/
http://scnj.58.com/dianshiji/
http://scnj.58.com/ershoukongtiao/
http://scnj.58.com/xiyiji/
http://scnj.58.com/bingxiang/
http://scnj.58.com/binggui/
http://scnj.58.com/chuang/
http://scnj.58.com/ershoujiaju/
http://scnj.58.com/bangongshebei/
http://scnj.58.com/diannaohaocai/
http://scnj.58.com/bangongjiaju/
http://scnj.58.com/ershoushebei/
http://scnj.58.com/yingyou/
http://scnj.58.com/yingeryongpin/
http://scnj.58.com/muyingweiyang/
http://scnj.58.com/muyingtongchuang/
http://scnj.58.com/yunfuyongpin/
http://scnj.58.com/fushi/
http://scnj.58.com/nanzhuang/
http://scnj.58.com/fsxiemao/
http://scnj.58.com/xiangbao/
http://scnj.58.com/meirong/
http://scnj.58.com/yishu/
http://scnj.58.com/shufahuihua/
http://scnj.58.com/zhubaoshipin/
http://scnj.58.com/yuqi/
http://scnj.58.com/tushu/
http://scnj.58.com/tushubook/
http://scnj.58.com/wenti/
http://scnj.58.com/yundongfushi/
http://scnj.58.com/jianshenqixie/
http://scnj.58.com/huju/
http://scnj.58.com/qiulei/
http://scnj.58.com/yueqi/
http://scnj.58.com/chengren/
http://scnj.58.com/nvyongpin/
http://scnj.58.com/qinglvqingqu/
http://scnj.58.com/qingquneiyi/
http://scnj.58.com/chengren/
http://scnj.58.com/xiaoyuan/
http://scnj.58.com/ershouqiugou/
http://scnj.58.com/tiaozao/
'''
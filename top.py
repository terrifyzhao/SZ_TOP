import requests
import webbrowser
import time


def monitor(size, ID, keyword, brand, shop_id):
    url = f'http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx?ID=2&brandName={brand}'
    while True:
        content = requests.get(url)
        theme_id = 0
        if any([True for k in keyword if k in content.text]):
            themes_str = content.text.split('^')
            for theme in themes_str:
                if any([True for k in keyword if k in theme]):
                    theme_id = theme.split('‘')[1]
                    break
        if theme_id != 0:
            get_shop_id(theme_id)
            get_number(theme_id, size, ID, brand, shop_id)
            evaluate(theme_id, ID, size, keyword)
            break
        time.sleep(5)
        print('monitor...')


def get_number(theme, size, ID, brand, shop_id):
    url = f'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=8&zhuti={theme}&shop_id={shop_id}&man_id={ID}&size={size}&brandName={brand}'
    res = requests.get(url)
    print(res.text)


def evaluate(theme, ID, size, keyword):
    url = f'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=9&zhuti={theme}&man_id={ID}'
    res = requests.get(url)
    if size in res.text and any([True for k in keyword if k in res.text]):
        print('取号成功，3秒后自动打开取号页面，请再次人工确认')
    for i in range(2, -1, -1):
        print(f'{i + 1}...')
        time.sleep(1)
    webbrowser.open('http://hn.topsports.com.cn/phone/qh_select.html')


def get_shop_id(theme):
    url = f'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=5&zhuti_id={theme}'
    shops = requests.get(url).text.split('^')
    print()
    for shop in shops:
        key, value = shop.split('‘')
        print(key + ':' + value)


def test():
    url1 = 'http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx?ID=2&brandName=NK&addCode=HN'
    url2 = 'http://hn.topsports.com.cn/asdf123zxc/phone/DataSour.aspx?ID=2&brandName=Jordan&addCode=HN'
    while True:
        content = requests.get(url1)
        if '不好意思，出错啦！' in content.text:
            print('conten1:', '不好意思，出错啦！')
        else:
            print('conten1:', content.text)
        if any([True for k in keyword if k in content.text]):
            webbrowser.open('http://hn.topsports.com.cn/asdf123zxc/phone/qh_xin.html?area_code=HN')
            break

        time.sleep(5)
        content = requests.get(url2)
        if '不好意思，出错啦！' in content.text:
            print('conten2:', '不好意思，出错啦！')
        else:
            print('conten2:', content.text)
        if any([True for k in keyword if k in content.text]):
            webbrowser.open('http://hn.topsports.com.cn/asdf123zxc/phone/qh_xin.html?area_code=HN')
            break
        time.sleep(10)
        print('monitor...')


if __name__ == '__main__':
    # US尺码
    size = '8.5'
    # 身份证号
    ID = 'xxxxx'
    # 关键词，可以填写多个
    keyword = ['016', 'CD0461-016', 'WMS', 'Air', 'Black', 'Toe']
    # 品牌
    brand = 'Jordan'
    # shop id，默认是万象天地店，执行代码会打印所有的店的id
    shop_id = 'NKSZ94'
    # monitor(size, ID, keyword, brand, shop_id)
    test()

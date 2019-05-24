import requests
import webbrowser


def monitor(size, ID, keyword):
    url = 'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=2&brandName=Jordan'
    while True:
        content = requests.get(url)
        theme_id = 0
        if keyword in content.text:
            themes_str = content.text.split('^')
            for theme in themes_str:
                if keyword in theme:
                    theme_id = theme.split('‘')[1]
                    break
        if theme_id != 0:
            get_number(theme_id, size, ID)
            evaluate(theme_id, ID)
            return


def get_number(theme, size, ID):
    url = f'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=8&zhuti={theme}&shop_id=NKSZ94&man_id={ID}&size={size}&brandName=Jordan'
    res = requests.get(url)
    print(res.text)


def evaluate(theme, ID):
    url = f'http://hn.topsports.com.cn/phone/DataSour.aspx?ID=9&zhuti={theme}&man_id={ID}'
    webbrowser.open(url)


if __name__ == '__main__':
    # US尺码
    size = '8.5'
    # 身份证号
    ID = '530302199409126375'
    # 关键词
    keyword = '507'
    monitor(size, ID, keyword)

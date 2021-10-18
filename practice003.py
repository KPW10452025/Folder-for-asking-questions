from os import write
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 爬取巴哈姆特動畫新聞原始碼
# https://www.gamer.com.tw/anime/

# Request URL:
# https://api.gamer.com.tw/www/v1/platform_news.php?layout=3&type=4&machine=0%2C0&page=1
# https://api.gamer.com.tw/www/v1/platform_news.php?layout=3&type=4&machine=0%2C0&page=2
# https://api.gamer.com.tw/www/v1/platform_news.php?layout=3&type=4&machine=0%2C0&page=3
# base_url = https://api.gamer.com.tw/www/v1/platform_news.php?layout=3&type=4&machine=0%2C0&page=

# 因為不想浪費硬碟空間故只顯示在 terminal 不做下載動作。

def create_request(page):
    base_url = 'https://api.gamer.com.tw/www/v1/platform_news.php?layout=3&type=4&machine=0%2C0&page='
    url = base_url + str(page)

    headers = {
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }

    request = urllib.request.Request(url = url, headers = headers, )
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open("巴哈姆特動畫新聞第" + str(page) + "頁.json", mode = "w", encoding = "utf-8") as fp:
        fp.write(content)

if __name__ == "__main__":
    start_page = int(input("請輸入想獲取標題的起始頁碼："))
    end_page = int(input("請輸入想獲取標題的結束頁碼："))
    show_or_download = int(input("單純顯示網頁源碼請輸入1；下載網頁源碼請輸入2："))

    if show_or_download == 1:
        for page in range(start_page, end_page + 1):
            request = create_request(page)
            content = get_content(request)
            print(content)
    elif show_or_download == 2:
        for page in range(start_page, end_page + 1):
            request = create_request(page)
            content = get_content(request)
            down_load(page, content)
    else:
        print("請正確輸入指令！")

# 目前問題，無法將 content 轉換成中文

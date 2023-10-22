import requests

def main():
    url = "https://e.weather.com.cn/mweather/101230101.shtml"
    ans = requests.get(url=url)
    print(ans.text)
    
if __name__ == "__main__":
    main()
    
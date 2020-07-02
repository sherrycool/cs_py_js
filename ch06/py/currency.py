import requests
'''
请求URI: (GET)http: // api.tianapi.com/txapi/fxrate/index
执行时间: 0.10645198822021484
请求参数: ?key = 795abf092e9fde6d3da9bd649bcbadc9 & fromcoin = USD & tocoin = CNY
& money = 1
'''


def main():
    tocoin = input("First Currency: ")
    fromcoin = input("Second Currency: ")
    key = '795abf092e9fde6d3da9bd649bcbadc9'
    money = 1
    res = requests.get("http://api.tianapi.com/txapi/fxrate/index",
                       params={'key': key, 'tocoin': tocoin,
                               "fromcoin": fromcoin, 'money': money})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    data = res.json()
    print(data)
    try:
        rate = data['newslist'][0]['money']
        print(f"1 {fromcoin} is equal to {rate} {tocoin}")
    except:
        print("Error!")
    #if data['msg'] != '数据返回为空':
        
        
    


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*ß
import requests 
import json
def main(): #http://api.fixer.io/latest?base=USD&symbols=EUR
    res = requests.get("http://hq.sinajs.cn/list=sz002307,sh600928")
    print(res.status_code)
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful.")
    '''
    data = res.json() # 用不了作者给的api 我用的这个不是json格式
    print(data)
    '''
    print(res.text)


if __name__ == "__main__":
    main()
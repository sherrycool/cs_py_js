# -*- coding: utf-8 -*
import requests 
import json
def main(): 
    res = requests.get("http://comtrade.un.org/api/get?max=100&type=C&freq=A&px=HS&ps=2013&r=826&p=0&rg=all&cc=ALL&fmt=json")
    print(res.status_code)
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful.")
    
    data = res.json() # 用不了作者给的api 我用的这个不是json格式
    #print(data)
    print(data.keys())
    print(data['validation']['datasetTimer'])
    print(data['validation'])
    '''
    print(res.text)
    '''


if __name__ == "__main__":
    main()


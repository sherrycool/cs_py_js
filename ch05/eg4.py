import requests

def main():
	year = input("Year:") #2016 --> ps
	c_or_s  = input("commodity or service: ") # c or s --> type
	res = requests.get("http://comtrade.un.org/api/get?max=100&freq=A&px=HS &p=0&rg=all&cc=ALL&fmt=json",
						params={'ps':year, 'type':c_or_s})  
		# 会把参数加到api地址里面 "http://comtrade.un.org/api/get?max=100&type=C&freq=A&px=HS&ps=2013&r=826&p=0&rg=all&cc=ALL&fmt=json"
	if res.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")

	data = res.json()
	print(data)

if __name__ == "__main__":
	main()


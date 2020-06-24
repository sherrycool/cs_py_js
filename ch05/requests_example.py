#encoding=utf-8
from vsimport import *
import requests

def main():
	res = requests.get("https://blog.csdn.net/u011585024/article/details/88385332")
	print(res.text)


if __name__ == "__main__":
	main()
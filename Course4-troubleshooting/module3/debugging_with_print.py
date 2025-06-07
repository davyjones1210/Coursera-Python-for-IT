import urllib3

def get_web_page(url):
	http = urllib3.PoolManager()
	response = http.request("GET", url)
	print(response.data.decode("utf-8"))
	

import urllib3

def get_web_page(url):
	http = urllib3.PoolManager()


	print("Retrieving URL:", url)
	response = http.request("GET", url)


	print("HTTP response code:", response.status, response.reason)
	print(response.data.decode("utf-8"))
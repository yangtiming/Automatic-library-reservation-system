import requests
import execjs
import re



user = "201883016"
pw = "password"
url = 'https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php'
headers = {
	'origin': 'https://sso.dlut.edu.cn',
	'referer': 'https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php',
	'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"macOS"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}

session = requests.Session()
r = session.get(url= url,headers=headers)
lt = re.findall('id="lt" name="lt" value="(.*?)"',r.text)[0]
execution = re.findall('name="execution" value="(.*?)"',r.text)[0]

with open('des.js')as f:
	ctx = execjs.compile(f.read())
	s = user+pw+lt
	rsa = ctx.call('strEnc',user+pw+lt,'1','2','3')
####
	
data= {
	'rsa':rsa,
	'ul':len(user),
	'pl':len(pw),
	'lt':lt,
	'execution':execution,
	'_eventId':'submit'
}


result= session.post(url= url,data= data, headers= headers)



url = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=myOrderList&order=asc&offset=0&limit=5'

headers = {
	'Host': 'seat.lib.dlut.edu.cn',
	'Origin': 'http://seat.lib.dlut.edu.cn',
	'Referer': 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderInfo.php',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
	'X-Requested-With' : 'XMLHttpRequest',
	
}

order_list = session.get(url= url,headers=headers).text

order_id = re.findall(r'"order_id":"\d+"',order_list)

order_end_time = re.findall(r'"order_end_time":"\d+"',order_list)
print(order_id[0])
#print(order_list)
#for i in range(len(order_list[1]['rows'])):
#	list_order_id.append(order_list['rows'][i]["order_id"])
#	list_order_stat.append(order_list['rows'][i]["order_end_time"])
	
#print(list_order_id,list_order_stat)


######
url = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=myOrderOperation'

headers = {
	'Host': 'seat.lib.dlut.edu.cn',
	'Origin': 'http://seat.lib.dlut.edu.cn',
	'Referer': 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderInfo.php',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
	'X-Requested-With' : 'XMLHttpRequest',
	
}
#r = session.get(url= url,headers=headers)
#lt = re.findall('id="order_id" name="order_id" value="(.*?)"',r.text)
#print("lt",lt) Release Temp in Cancel In
data= {

	'order_id' : str(order_id[0][-8:-1]),
	'order_type' : '2',
	'method' : 'in', # Release Temp Cancel
}
results= session.post(url= url,data= data, headers= headers)
print(results.text)

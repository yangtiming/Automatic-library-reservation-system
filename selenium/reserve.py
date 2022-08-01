import time
from time import strftime, localtime
from reserve_seat_main import main

def reserves():
	start = time.time()
	while (1):
		t=time.sleep(10)
		end = time.time()
		if ( int(start-end)%60 )==0:
			print("正在等待06:30",strftime('%H:%M',localtime()))
		if strftime('%H:%M',localtime())=="06:29" :
			main()
			return

print("正在进入预约系统")
reserves()
print("结束")


		

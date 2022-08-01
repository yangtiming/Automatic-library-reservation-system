# encoding:utf-8
import time
from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options
import json 
def choose(webdriver,want_select,ret_dic,room_dir):
    end=0
    all_select= []
    all_select_dir = []
    for i in range(len(ret_dic)):
        for j in range(len(ret_dic[1])):
            if int(ret_dic[i][j]["seat_type"])==1 and int(ret_dic[i][j]["seat_order_status"])==1:
                all_select.append(ret_dic[i][j]["seat_label"])
                all_select_dir.append(str(i+1)+" "+str(j+1))
                
    print(ret_dic[1][1]["room_name"],all_select)
    if len(all_select) != 0:
        tmp = [val for val in want_select if val in all_select]
        if len(tmp)!=0:
            a=all_select_dir[all_select.index(tmp[0])].split(" ")[0]
            b=all_select_dir[all_select.index(tmp[0])].split(" ")[1]
            
            if int(room_dir)!=11:
                _room = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr['+str(room_dir)+']/td')
                _room.click()
                time.sleep(0.4)
                _shoudong = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
                _shoudong.click()
                time.sleep(0.4)
                select_seat= '/html/body/div[2]/section/div/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/'+'tr['+str(a)+']/'+'td['+str(b)+']'
                seat = webdriver.find_element_by_xpath(select_seat)
                seat.click()
                time.sleep(0.4)
                queren = webdriver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
                queren.click()
                time.sleep(10)
                webdriver.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php")
                time.sleep(2)
                webdriver.close()
                end=1
    return end


        
def main():
    user_id = '201883016'
    password = 'password'
    
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    webdriver = Chrome(chrome_options=chrome_options)

    webdriver.maximize_window()
    
    '''登录'''
    webdriver.get("https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php")
    input_userid = webdriver.find_element_by_id('un')
    input_userid.send_keys(user_id)
    input_password = webdriver.find_element_by_id('pd')
    input_password.send_keys(password)
    login_button = webdriver.find_element_by_class_name('login_box_landing_btn')
    login_button.click()
    time.sleep(1)
    xuan=webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/a[1]')
    xuan.click()
    time.sleep(2)
    bochuan = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td')
    bochuan.click()
    time.sleep(1)
    
    
    year  = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]
    list_change=[0,0,0,0,0,0,0,0,0,0,0,0]
    list_change_v1=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    want_select_dating=[]
    want_select_401=[]
    want_select_404=[]
    
    #want_select_301=[]

    want_select_301=[
        "145","146","147"
        "098","099","100","101","102","103","104","105",
        "001","010","019","029","038","047","056","065",
        "077","081","085","089","093","097",
        "107","116","117","126","127",
    #    "132","133","134","135","136",
        "009","018","027","037","046","055","064","073",
        "074","078","082","086","090","094"
    ]

    

    #want_select_312=[]

    want_select_312=["147","148","149",
        "135","136","137","138","139","140","141","142",
        "001","005","009","013","017","021",
        "033","042","051","060","069","078","087","102",
        "004","008","012","016","020","024",
        "025","034","044","052","061","070","079","094",
        "088","093","107","112","117","122",
        "092","106","111","116","121","126"
    ]


    
    want_select_409= [
        "096","097","098","099","100","101","101","102","103","116",
        "104","105","106","107","108","109","110","111","112","113",
        "093","094","095",
        "092","114","115",
        "016","017","018",
        "013","014","015",
    ]
    #want_select_501= []

    want_select_501= [
        "001","010","019","027","035","044","053","062",
        "076","082","088","094","100","106","112","118",
        "144","139","134","129","124","119",
        "148","143","138","133","128","123"
        "009","018","026","034","043","052","061","070"
        "071","077","083","089","095","101","107","113"
    ]

    
    
    want_select_504= [
        '157','158','159','160','161','162','163','164',
        "133","134","135","136","137","138","139","140",
        '281','282','283','284','285','286','287','288',
        '256','257','258','259','260','261','262','263',
        '248','249','250','251','252','253','254','255',
        
        "001","006","011","016","021","026","031","036","041","046","051","056","061","066","071","076","081","086","091","096","101","106",
        '005','010','015','020','025','030','035','040','045','050','055','060','065','070','075','080','085','090','095','100','105','110',
        
        
        
    ]
    #want_select_507= []

    want_select_507= [
        "001","007","013","019","025","031","037","043",
        "057","066","075","084","093","102","111","120",
        "125","130","135","140","145","150",
        "121","126","131","136","141","146"
        "006","012","018","024","030","036","042","048"
        "049","058","068","077","085","094","103","112"
    ]

    want_select_111=[]
    time_flag=1
    end=0

    while (1):
       # try:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        #print("0",list_change)
        #print("1",list_change_v1)
        
        
        today_button = webdriver.find_element_by_id('todayBtn')
        today_button.click()
        time.sleep(1)
        #tomorrow_button = browser.find_element_by_id('nextDayBtn')
        #tomorrow_button.click()
        time.sleep(0.1)
        
        room_300 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[2]').text
        print(room_300)
        list_change[2]=int(room_300[-1])
        room_301 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[3]').text
        print(room_301)
        list_change[3]=int(room_301[-1])
        room_312 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[4]').text
        list_change[4]=int(room_312[-1])
        print(room_312)
        
        room_401 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[5]').text
        list_change[5]=int(room_401[-1])
        print(room_401)
        room_404 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[6]').text
        list_change[6]=int(room_404[-1])
        print(room_404)
        room_409 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[7]').text
        list_change[7]=int(room_409[-1])
        print(room_409)
        
        room_501 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[8]').text
        list_change[8]=int(room_501[-1])
        print(room_501)
        room_504 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[9]').text
        list_change[9]=int(room_504[-1])
        print(room_504)
        room_507 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[10]').text
        list_change[10]=int(room_507[-1])
        print(room_507)
        room_111 = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[11]').text
        list_change[11]=int(room_111[-1])
        print(room_111)
        
        print("0",list_change)
        print("1",list_change_v1)
        v = list(map(lambda x: x[0]-x[1], zip(list_change, list_change_v1)))
        print(v)
        if v[2]>0 and len(want_select_dating)!=0:
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #三楼大厅
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=212'
            url = url_begin+data+room_id
        
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_dating = json.loads(text)
            end=choose(webdriver,want_select_dating,json_data_dating,"2")
        
        if v[3]>0 and len(want_select_301)!=0:
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #301
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=168'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_301 = json.loads(text)
            end=choose(webdriver,want_select_301,json_data_301,"3")
            
        if v[4]>0 and len(want_select_312)!=0: 
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)   
            #312
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=170'
            url = url_begin+data+room_id
        
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_312 = json.loads(text)
            end=choose(webdriver,want_select_312,json_data_312,"4")
        
        if v[5]>0 and len(want_select_401)!=0:   
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #401
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=195'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_401 = json.loads(text)
            end=choose(webdriver,want_select_401,json_data_401,"5")
            
        if v[6]>0 and len(want_select_404)!=0: 
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #404
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=197'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_404 = json.loads(text)
            end=choose(webdriver,want_select_404,json_data_404,"6")
        
        if v[7]>0 and len(want_select_409)!=0: 
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #409
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=196'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_409 = json.loads(text)
            end=choose(webdriver,want_select_409,json_data_409,"7")
        
        if v[8]>0 and len(want_select_501)!=0:  
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #501
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=198'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_501 = json.loads(text)
            end=choose(webdriver,want_select_501,json_data_501,"8")
        
        if v[9]>0 and len(want_select_504)!=0:  
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #504
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=199'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_504 =json.loads(text)
            end=choose(webdriver,want_select_504,json_data_504,"9")
            
        if v[10]>0 and len(want_select_507)!=0:  
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #507
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=200'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')   
            json_data_507 = json.loads(text)
            end=choose(webdriver,want_select_507,json_data_507,"10")
            
        if v[11]>0  and len(want_select_111)!=0:  
            if time_flag==1:
                time.sleep(1)
            time.sleep(0.1)
            #111
            url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
            data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
            room_id = '&room_id=241'
            url = url_begin+data+room_id
            
            response = webdriver.request("GET",url)
            text = response.text
            if text.startswith(u'\ufeff'):
                    text = text.encode('utf8')[3:].decode('utf8')
            json_data_111 = json.loads(text)
            end=choose(webdriver,want_select_111,json_data_111,"11")
            



        for i in range(len(list_change_v1)):
            list_change_v1[i]=	list_change[i]
        time_flag=0
        print("没有找到预定位置请等待")
        if end==1:
            return
        '''
        except:
            for i in range(len(list_change_v1)):
                list_change_v1[i]=	list_change[i]
            time_flag=0
            if end==1:
                return
            print("错误重新开始")
            time.sleep(3)
            continue
        '''



main()
print("end")

# encoding:utf-8
import time
from time import strftime, localtime
from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait    # WebDriverWait 库，负责循环等待
from selenium.webdriver.support import expected_conditions as EC    # expected_conditions 类，负责条件出发

import json 
import random


def choose(webdriver,want_select,ret_dic,room_dir):
    end=0
    all_select= []
    all_select_dir = []
    for i in range(len(ret_dic)):
        for j in range(len(ret_dic[1])):
            if int(ret_dic[i][j]["seat_type"])==1 and int(ret_dic[i][j]["seat_order_status"])==1:
                all_select.append(ret_dic[i][j]["seat_label"])
                all_select_dir.append(str(i+1)+" "+str(j+1))
            if int(ret_dic[i][j]["seat_type"])==3 and int(ret_dic[i][j]["seat_order_status"])==2:
                all_select.append(ret_dic[i][j]["seat_label"])
                all_select_dir.append(str(i+1)+" "+str(j+1))
            if int(ret_dic[i][j]["seat_type"])==3 and int(ret_dic[i][j]["seat_order_status"])==3:
                all_select.append(ret_dic[i][j]["seat_label"])
                all_select_dir.append(str(i+1)+" "+str(j+1))
                
    print(ret_dic[1][1]["room_name"],all_select)
    tmp = [val for val in want_select if val in all_select]
    print("您选的座位空闲:",tmp)
    while(1):
        if strftime('%H:%M',localtime())=="06:31":
            return
    #    time.sleep(1)
        time.sleep(0.6)
        today_button = webdriver.find_element_by_id('todayBtn')
        today_button.click()
        time.sleep(0.1)
        tomorrow_button =  webdriver.find_element_by_id('nextDayBtn')
        tomorrow_button.click()
        time.sleep(0.1)
        time_flagg=1
        if len(tmp)!=0:
            for ik in range(len(tmp)):
                if time_flagg==1:
                    time.sleep(0.05)
                time_flagg=0
                a=all_select_dir[all_select.index(tmp[ik])].split(" ")[0]
                b=all_select_dir[all_select.index(tmp[ik])].split(" ")[1]
                print("您选的座位坐标",a,b)
                try:
                    select_seat= '/html/body/div[2]/section/div/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/'+'tr['+str(a)+']/'+'td['+str(b)+']'
                    color = webdriver.find_element_by_xpath(select_seat+'/div').get_attribute("style")
                    print(color)    
                    if color == "background-color: rgb(185, 222, 160);": #绿色
                        print("绿色可选")
                        seat = webdriver.find_element_by_xpath(select_seat)
                        seat.click()
                        
                        queren = webdriver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
                        while(queren.is_displayed()!=True):
                            time.sleep(0.05)
                        queren.click()
                        
        
                        
                        try:
                            WebDriverWait(webdriver,2,0.2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[1]')))
                            print("text",webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/h5').text,webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div').text)
                        except Exception as e:
                            print("内内",e)
                            
                        if webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/h5').text == '信息提示':    
                            print("success")
                            time.sleep(10)
                            webdriver.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php")
                            time.sleep(2)
                            webdriver.close()
                            end=1
                            return end
                        else:
                            print("别人太快啦，继续继续")
                            queren = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button')
                            queren.click()
                            time.sleep(0.4)
                    else:
                        print("换一个位置") 
                except Exception as e:
                    time.sleep(0.1)
                    today_button = webdriver.find_element_by_id('todayBtn')
                    today_button.click()
                    time.sleep(0.5)
                    print("内",e)

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
    
    import datetime
    now_time=datetime.datetime.now()
    year  = int((now_time+datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M:%S")[0:4])
    month = int((now_time+datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M:%S")[5:7])
    day = int((now_time+datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M:%S")[8:10])
    list_change=[0,0,0,0,0,0,0,0,0,0,0,0]
    list_change_v1=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    want_select_dating=[]
    want_select_401=[]
    want_select_404=[]
    
    #want_select_301=[]
    
    want_select_301=[
    #    "115"
    #    "145","146","147"
    #    "098","099","100","101","102","103","104","105",
    #    "001","010","019","029","038","047","056","065",
    #    "077","081","085","089","093","097",
    #    "107","116","117","126","127",
    #    "132","133","134","135","136",
    #    "009","018","027","037","046","055","064","073",
    #   "074","078","082","086","090","094"
    ]

    

    #want_select_312=[]

    want_select_312=[
    #    "147","148","149",
    #    "135","136","137","138","139","140","141","142",
    #    "001","005","009","013","017","021",
    #    "033","042","051","060","069","078","087","102",
    #    "004","008","012","016","020","024",
    #    "025","034","044","052","061","070","079","094",
    #    "088","093","107","112","117","122",
    #    "092","106","111","116","121","126"
    ]


    
    want_select_409= [
       # "096",
        "097",
       # "098",
        "099","100","101","101",
        #"102",
        "103","116",
        "104","105","106","107","108","109",
        #"110",
        "111","112","113",
    #    "093","094","095",
    #    "092","114","115",
    #    "016","017","018",
    #    "013","014","015",
    ]
    random.shuffle(want_select_409)

    #want_select_501= []

    want_select_501= [
    #    "001","010","019","027","035","044","053","062",
    #    "076","082","088","094","100","106","112","118",
    #    "144","139","134","129","124","119",
    #    "148","143","138","133","128","123"
    #    "009","018","026","034","043","052","061","070"
    #    "071","077","083","089","095","101","107","113"
    ]

    
    
    want_select_504= [
    #    '157','158','159','160','161','162','163','164',
    #    "133","134","135","136","137","138","139","140",
    #    '281','282','283','284','285','286','287','288',
    #    '256','257','258','259','260','261','262','263',
    #    '248','249','250','251','252','253','254','255',
        
    #    "001","006","011","016","021","026","031","036","041","046","051","056","061","066","071","076","081","086","091","096","101","106",
    #    '005','010','015','020','025','030','035','040','045','050','055','060','065','070','075','080','085','090','095','100','105','110',
        
        
        
    ]
    #want_select_507= []
    
    want_select_507= [
    #    "001","007","013","019","025","031","037","043",
    #    "057","066","075","084","093","102","111","120",
    #    "125","130","135","140","145","150",
    #    "121","126","131","136","141","146"
    #    "006","012","018","024","030","036","042","048"
    #    "049","058","068","077","085","094","103","112"
    ]

    want_select_111=[]
    time_flag=1
    end=0

    room_id = '&room_id=196' 
    if len(want_select_dating)!=0:
        room_dir="2"
        room_id = '&room_id=212'
    if len(want_select_301)!=0:
        room_dir="3"
        room_id = '&room_id=168'
    if len(want_select_312)!=0: 
        room_dir="4"
        room_id = '&room_id=170'
    if len(want_select_401)!=0:
        room_dir="5"
        room_id = '&room_id=195' 
    if len(want_select_404)!=0:
        room_dir="6"
        room_id = '&room_id=197' 
    if len(want_select_409)!=0:
        room_dir="7"
        room_id = '&room_id=196' 
    if len(want_select_501)!=0: 
        room_dir="8"
        room_id = '&room_id=198'
    if len(want_select_504)!=0: 
        room_dir="9"
        room_id = '&room_id=199'
    if len(want_select_507)!=0: 
        room_dir="10"
        room_id = '&room_id=200'
    if len(want_select_111)!=0:
        room_dir="11"
        room_id = '&room_id=241' 

    url_begin='http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap'
    data= '&order_date='+str(year)+'%2F'+str(month)+'%2F'+str(day)
    url = url_begin+data+room_id
    response = webdriver.request("GET",url)
    text = response.text
    if text.startswith(u'\ufeff'):
            text = text.encode('utf8')[3:].decode('utf8')
    json_data_deal_with = json.loads(text)    
     

    _room = webdriver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr['+str(room_dir)+']/td')
    _room.click()
    time.sleep(0.4)
    _shoudong = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    _shoudong.click()
    time.sleep(0.4)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    
    if  len(want_select_dating)!=0:
        #if time_flag==1:
        #    time.sleep(1)
    
        end=choose(webdriver,want_select_dating,json_data_deal_with,"2")
    
    if len(want_select_301)!=0:
        #301
        end=choose(webdriver,want_select_301,json_data_deal_with,"3")
        
    if  len(want_select_312)!=0: 

        #312
        end=choose(webdriver,want_select_312,json_data_deal_with,"4")
    
    if  len(want_select_401)!=0:   

        #401
        end=choose(webdriver,want_select_401,json_data_deal_with,"5")
        
    if len(want_select_404)!=0: 

        #404
        end=choose(webdriver,want_select_404,json_data_deal_with,"6")
    
    if len(want_select_409)!=0: 

        #409
        end=choose(webdriver,want_select_409,json_data_deal_with,"7")
    
    if len(want_select_501)!=0:  

        #501
        end=choose(webdriver,want_select_501,json_data_deal_with,"8")
    
    if len(want_select_504)!=0:  
        #504
        end=choose(webdriver,want_select_504,json_data_deal_with,"9")
        
    if len(want_select_507)!=0:  

        #507
        end=choose(webdriver,want_select_507,json_data_deal_with,"10")
        
    if len(want_select_111)!=0:  

        #111
        end=choose(webdriver,want_select_111,json_data_deal_with,"11")
        

        
        


#main()
#print("end")

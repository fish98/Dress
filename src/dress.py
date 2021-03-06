#coding:utf-8

from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome.options import Options

# TODO3: refine print notes with ****

def main():
    
    url = input("Please Enter Product Url:\n") # "https://detail.tmall.hk/hk/item.htm?tbpm=1&spm=a230r.1.14.1.13274fd0N9LZEy&id=45361707245&ns=1&abbucket=7&skuId=3164503563109"
    buyDay = input("\nPlease Enter the DUE DATE:\n (For example `2019-12-12`)\n")
    buyTime = input("\nPlease Enter the DUE TIME:\n (For example `08:00:00`)\n")
    bt = buyDay + " " + buyTime
    
    bt_dt = datetime.datetime.strptime(bt, "%Y-%m-%d %H:%M:%S")
    now_dt = datetime.datetime.now()
    
    print("There are %.1f miniutes before CHONG CHONG CHONG"%((bt_dt-now_dt).seconds/60))
    input("Press any key to start...") 
    print("Starting ...")
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options) 
    driver.maximize_window()

    start(url, driver)
    buy(bt, url, driver)

def start(url, driver):

    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

# Check different platform

    if "taobao" in url:
        driver.find_element_by_link_text("亲，请登录").click()
    elif "tmall" in url:
        driver.find_element_by_link_text("请登录").click()
    else: 
        print("This poor software does not support the url been provided QAQ...\nPlease check whether url is set correctly or contact ttfish\n")
        return

    print("Please Login in 30 seconds\n Scan QR code to login ...")
    
    time.sleep(30)

    return 

    
def buy(buy_time, url, driver):

    if "taobao" in url:
        btn_buy="#J_juValid > div.tb-btn-buy > a"
        btn_order="#submitOrderPC_1 > div.wrapper > a"

    elif "tmall" in url:
        btn_buy="#J_LinkBuy"
        btn_order="#submitOrderPC_1 > div > a"
        btn_vertify="body > div.next-overlay-wrapper.opened > div.next-dialog.next-overlay-inner > div > div > div > div.auth-btm > span.auth-btn-sub"
    
    else: 
        return 

#   Click BUYYYYYYYY!!!

    while True:
        if datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")>buy_time:
            try:
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    print("Generate Purchase Order ...")
                    break
                time.sleep(0.01)
            except:
                time.sleep(0.01)    

#   F**king Vertify Dialog before purchase
#   If the product is sold in Tmall from a foriegn counrty :: Uncomment lines below

    # while True: 
    #     try:
    #         if driver.find_element_by_css_selector(btn_vertify):
    #             driver.find_element_by_css_selector(btn_vertify).click()
    #             print("Pass Vertify S**T ...")
    #             break
    #         time.sleep(0.01)
    #     except:
    #         time.sleep(0.01)    
    
#   Hand in purchase

    while True:
        try:
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                print("Order Succeed! Shut your mouth and Take your money ...")
                break
        except:
            time.sleep(0.01)   

if __name__ == '__main__':
    main()
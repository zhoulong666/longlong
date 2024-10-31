from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

ser=Service("./geckodriver.exe")
driver=webdriver.Firefox(service=ser)
driver.get("http://192.168.3.107:9000/login")

driver.find_element(by=By.XPATH,value="").click()    #点击（XPATH定位）

driver.find_element(by=By.XPATH,value="").send_keys("")   #输入（XPATH定位）


#随机生成姓名
import random
# 姓氏列表
surnames = ['张', '王', '李', '赵', '刘', '陈', '杨', '黄', '周', '吴','严','赵','韩','杰','车','浩','吉','林','龙','东','杭']
# 名字列表
names = ['伟', '敏', '婷', '克', '宇', '静', '磊', '娜', '杰', '丽','娟','卷','明','格','星','鱼','广','肉','动']
def generate_random_name():
    surname = random.choice(surnames)
    name = random.choice(names)
    return surname + name
nnn=generate_random_name()



#浏览器窗口最大化（防止元素被隐藏导致无法定位）注意屏幕分辨率
driver.maximize_window()


time.sleep(5)  #强制等待（不管元素出不出现）


#生成一个18位的随机数字
random_number = ''.join(str(random.randint(0, 9)) for _ in range(18))


import string
# 生成一个4位的随机字母组合
def generate_random_letters(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))
four_random_letters = generate_random_letters(4)



# 鼠标滚到指定位置（具体元素)
target = driver.find_element(by=By.XPATH,value="")
driver.execute_script("arguments[0].scrollIntoView();", target)


#清空输入框并重新填写
driver.find_element(by=By.XPATH,value="").clear()
driver.find_element(by=By.XPATH,value="").send_keys("周龙")


#设置一个等待时间，如果在这个等待时间内，网页加载完成，则执行下一步；否则一直等待时间截止
#   弊端：程序会一直等待整个页面加载完成直到超时，但我需要的那个元素早就加载完成了，只是页面上有个别其他元素加载特别慢，我仍要等待页面全部加载完成才能执行下一步
driver.implicitly_wait(10)  #隐式等待


# 超时时间为30秒，每0.5秒检查1次，直到ID=kw的元素出现
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH,"")))
element.click()  #显式等待

driver.quit()  #退出


# 创建一个参数对象，用来控制chrome以无界面模式打开
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
#驱动必须复制在此目录下
opt = Options()  # 新建参数对象
opt.add_argument("--headless")  # 无头
opt.add_argument("--disbale-gpu")  # 无图形化界面
web = Firefox(options=opt)  # 把参数配置设置到浏览器中
web.get("http://192.168.3.107:9000/login")

#  ctrl + R （Pycharm全局替换内容）   ctrl + F （全局查找）




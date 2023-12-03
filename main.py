# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author  : zlbd
# This is a sample Python script.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By     #导入By类
from selenium.webdriver.support.ui import WebDriverWait     #导入显示等待类
from selenium.webdriver.support import expected_conditions  #导入期望场景类

"""
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
（1）Tag
（2）NavigableString
（3）BeautifulSoup
（4）Comment
"""
from bs4 import BeautifulSoup


def comments():
    """
    元素查找方法汇总
    find_element_by_name
    find_element_by_id
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    以上是单元素查找，多元素把 element 变成 elements 即可。

    还有一种较通用的方法
    from selenium.webdriver.common.by import By    注意这里要导入
    input_first = browser.find_element(By.ID,"q")    ID可以换成其他
    """
    pass


def main():
    # 1. 获取浏览器对象
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  #可设定无界面模式，即操作浏览器时，隐层浏览器, 设置无界面  可选
    browser = webdriver.Chrome(options = options)
    print("hello world")
    browser.implicitly_wait(10)  # # 智能等待，在设置时间范围内，只要条件成立，马上结束等待, implicitly_wait

    # 2. 访问页面
    browser.get('https://cn.bing.com/')
    #browser.minimize_window()  # 窗口最小化，窗口最大化用 wd.maximize_window()，可有可无，看情况

    # 3. 查找某元素
    element = browser.find_element(By.ID, "est_cn")
    print(element)
    print(element.text)

    # 4. 拟按键输入，查找元素并交互模
    xpathContent = "/html/body/div[2]/div/div[3]/div[2]/form/div[1]/input"
    element = browser.find_element(By.XPATH, xpathContent)
    if element:
        element.send_keys("selenium")
        element.submit()

    try:
        # 最多等待10秒直到浏览器标题栏中出现我希望的字样（比如查询关键字出现在浏览器的title中）
        WebDriverWait(browser, 10).until(
            expected_conditions.title_contains('selenium'))
        print(browser.title)

        bsobj = BeautifulSoup(browser.page_source, "html.parser")
        print(type(bsobj.text))

        num_text_element = bsobj.find('span', {'class': 'nums_text'})
        print(num_text_element)

    finally:
        # 关闭浏览器
        browser.close()

    print('----------------done!!------------------')

tu = 9
zhuan = 3
shape = 4

def paste(hunningtu):
    return None


class tu:
    def paste(self, hunningtu):

        return None

class hunningtu(tu):
    pass

class ZhuanClass(tu):
    def paste(self, tt):
        super().paste(self. tt)
        self.t = tu()
        b = connect()
        a = 3
        b = 4
        try:
            t = a / b
        except ZeroDivisionError as xxx:
            print(xxx)
            print(str(xxx))
            print("xxxxxxxx-------------------------")
            print(type(xxx))
            print("--------")
            print(dir(xxx))
            t = 5
            while True:
                b = connect()
                # do connect
                if reconnect == True:
                    break
                else:
                    t = t -1
                    if (t < 1):
                        break
            pass
        except KeyboardInterrupt as e2:
            print("e2")
        except Exception as eBase:
            print(eBase)

        self.shape = 3

        return None

if __name__ == '__main__':
    try:
        main()
    except Exception as xxx:
        print(xxx)
        print(str(xxx))
    print('----------------done!------------------')

# EOF

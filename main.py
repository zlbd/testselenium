# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author  : zlbd

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://cn.bing.com/search?q=%e7%99%be%e5%ba%a6&qs=SC&pq=baidu&sc=10-5&cvid=55131F227A304C3CB96FFFC540CB1431&FORM=QBLH&sp=1&lq=0')
time.sleep(1)
# 点击打开新窗口的链接
link = wd.find_element(By.XPATH, '//*[@id="b_results"]/li[1]/h2/a')
link.click()
mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '百度一下' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)
wd.switch_to.window(mainWindow)
time.sleep(1)
print(wd.title)


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
wd = webdriver.Chrome()
wd.implicitly_wait(10)
def isAscending(xs):
    for n in range(len(xs) - 1):
        if xs[n] > xs[n+1]:
            return False
    return True
wd.get('https://www.uniqlo.cn/c/4221124018.html')
time.sleep(10)
# 点击打开新窗口的链接
element = wd.find_element(By.XPATH,"//*[@style='display: flex;']").click()
wd.find_element(By.XPATH, "//*[@class='sort-content']/*[3]").click()
time.sleep(5)
price = wd.find_elements(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[2]/div[1]/div/div/div/div/div[5]/div/div[2]/div/div[1]/div/a/div/span')
all=[]
for ele in price:
    all.append(ele.text)
print(all)
assert isAscending(all) is True



class DialogAddTagXXX(object):

    def __init__(self):
        pass

    def get_grid_bodies(self, locator):
            """
            :param locator: tuple. eg: ("By.XPATH", r"//ag-grid-angular[@id='myGrid']" layer)
            :return bodies: list.
            """
            # step1:
            # Get locator.
            body_locator = (locator[0], locator[1] + r"//div[contains(@class, 'ag-center-cols-container')]/div")
            # step2:
            # Get body elements.
            elements = self.common.find_elements(body_locator)
            # step3:
            # Get bodies text.
            if len(elements) == 0:
                return []
            else:
                bodies = []
                for _line in elements:
                    _div_index = int(elements.index(_line)) + 1
                    _line_locator = (locator[0], body_locator[1] + "/../div[%s]/div" % _div_index)
                    _line_subelements = self.common.find_elements(_line_locator)
                    _line_items = [_ele.text for _ele in _line_subelements]
                    bodies.append(_line_items)
                return bodies

        def get_grid_datalist(self, locator):
            """
            :param locator: tuple. eg: ("By.XPATH", r"//ag-grid-angular[@id='myGrid']" layer)
            :return _datalist: list.
            """
            # step1:
            # Get grid headers.
            headers = self.get_grid_headers(locator)
            # step2:
            # Get grid bodies.
            bodies = self.get_grid_bodies(locator)
            # step3:
            # Get grid datalist.
            datalist = []
            for body in bodies:
                _dict = {}
                for head in headers:
                    _index = headers.index(head)
                    _dict[head] = body[_index]
                datalist.append(_dict)
            return datalist

        def select_row_by_index(self, locator, index):
            """
            Select row checkbox by index.
            :param locator: tuple. eg: ("By.XPATH", r"<span[@class='ag-selection-checkbox']> layer")
            :param index: int. start from 1.
            :return:
            """
            # step1:
            # Get locator.
            with_index_locator = (locator[0], locator[1] % index)
            status_locator = (with_index_locator[0], with_index_locator[1] + r'//input')
            # step2:
            # Select row checkbox.
            status = self.common.find_element(status_locator).is_selected()
            if not status:
                self.common.click_element(locator)

        def get_visible_bodies_from_tagXXX_grid(self):
            """
            Get visible bodies from 'tagXXX' grid.
            """
            # step1:
            # Get locator.
            _grid_tagXXX_locator = self.Dialog_AT_Pane.grid_tagXXX()
            # step2:
            # Get tags browsed.
            grid_bodies = self.GridActor.get_grid_bodies(_grid_tagXXX_locator)
            return grid_bodies
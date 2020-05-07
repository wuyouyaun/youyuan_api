# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://menu.apec.develop:8099/?#/pubBasics/pub/marketManage")
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div/ul/li[1]/a/span").click()
driver.find_element_by_class_name("el-menu-item").click()
driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/button").click()
# 新增业务资格管理
time.sleep(2)
all_handles = driver.window_handles
print (all_handles)

# a = driver.switch_to_alert()
# driver.implicitly_wait(10)
driver.find_element_by_xpath("//span/i[@class='el-icon-arrow-up']").click()


# time.sleep(3)
# driver.find_element_by_xpath("html/body/div[5]/div[1]/div[1]/ul/li[3]").click()
# s.find_element_by_xpath("html/body/div[5]/div[1]/div[1]/ul/li[3]/span").click()



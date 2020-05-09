#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 点击页面元素
def my_click(browser, type, value):
    if type == "id":
        element = browser.find_element_by_id(value)
    elif type == "name":
        element = browser.find_element_by_name(value)
    elif type == "class":
        element = browser.find_element_by_css_selector(value)
    else:
        print("Can't find element")
        return
    element.click()
    time.sleep(3)

# 用户签到
def my_login(browser):
    browser.get("https://passport.jd.com/uc/login")
    time.sleep(3)
    my_click(browser, "class", "div.login-tab.login-tab-r")

    loginname = browser.find_element_by_id("loginname")
    nloginpwd = browser.find_element_by_id("nloginpwd")
    loginname.send_keys("fantasyxc")
    nloginpwd.send_keys("xiachang2007")

    my_click(browser, "id", "loginsubmit")
    print("login success")
    time.sleep(3)

    # 把页面保存为图片，验证是否登录成功
    browser.get_screenshot_as_file("login.png")

# 店内签到
def shop_sign_in(browser):
    print("店内签到")
    browser.get("https://bean.jd.com/myJingBean/list")
    time.sleep(3)
    shops = browser.find_elements_by_xpath("//ul[@class='bean-shop-list']/li/a[@class='s-btn']")
    urls = [s.get_attribute("href") for s in shops]
    for url in urls:
        try:
            browser.get(url)
            time.sleep(3)
            my_click(browser, "class", "a.d-header-icon.unsigned")
            print("%s 签到成功" % url)
        except:
            print("%s 签到失败" % url)

# 用户登录
def user_sign_in(driver):
    print("用户签到")
    url = "http://vip.jd.com/home.html"
    driver.get(url)
    time.sleep(3)
    my_click(driver, "class", "sign-in")
    print("%s 签到成功" % url)

def main():
    browser = webdriver.PhantomJS(executable_path=r"C:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs")
    # 最大化浏览器窗口
    browser.maximize_window()

    my_login(browser)
    user_sign_in(browser)
    shop_sign_in(browser)

    browser.quit()

if __name__ == "__main__":
    main()
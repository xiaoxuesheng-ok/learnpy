# 控制 css
from selenium import webdriver
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image",2)
driver = webdriver.Firefox(firefox_profile=fp)
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

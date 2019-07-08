from selenium  import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBianry


# caps = webdriver.DesiredCapabilities().FIREFOX

# caps["marionette"] = Flase

# binary = FirefoxBianry(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\firefox.exe")

## driver = webdriver.Firefox(firefox_binary=binary,capabilities = caps)

# 只有默认安装路径 才能这么写
driver = webdriver.Firefox()

driver.get("http://www.santostang,com/2017/03/02/helloworld")

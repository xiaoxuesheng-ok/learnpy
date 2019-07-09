from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://www.santostang.com/2018/07/04/hello-world/")

time.sleep(3)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)

driver.switch_to.default_content()

for i in range(1,10) :
    #往下滚动页面， 需要再主页面进行。
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    # 但是需要点击的buttion 再iframe里边。
    load_more = driver.find_element_by_css_selector('button.more-btn')

    load_more.click()

    time.sleep(2)

    comments = driver.find_elements_by_css_selector('div.reply-content')
    for eachcomment in comments:
        content = eachcomment.find_element_by_tag_name('p')
        print (content.text)
     # 把iframe又转回去， 向下滚动。
    driver.switch_to.default_content()


driver.close()

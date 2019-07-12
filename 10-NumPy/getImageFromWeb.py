import time
from urllib.request import urlretrieve
from PIL import Image
import tesseract
from selenium import webdriver


def getImageText(imageUrl):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())

# 创建新的Selenium driver
driver = webdriver.Firefox()

driver.get('https://www.amazon.com/Death-Ivan-Ilyich'\
    '-Nikolayevich-Tolstoy/dp/1427027277')
time.sleep(2)

# 点击图书预览按钮
driver.find_element_by_id('imgBlkFront').click()
imageList = []

# 等待页面加载
time.sleep(5)

while 'pointer' in driver.find_element_by_id(
    'sitbReaderRightPageTurner').get_attribute('style'):
    # 当右箭头可以点击时，点击翻页
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # 获取已加载的任何新页面（可以同时加载多个页面，
    # 但是由于使用的是集合，重复的页面不会被加进来)
    pages = driver.find_elements_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print("No pages found")
    for page in pages:
        image = page.get_attribute('src')
        print('Found image: {}'.format(image))
        if image not in imageList:
            imageList.append(image)
            getImageText(image)

driver.quit()

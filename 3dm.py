from selenium import webdriver

import time
w3dm=webdriver.Chrome()
w3dm.get('http://www.3dmgame.com')
print (w3dm.title)

content=w3dm.find_element_by_class_name('conCon')
lis=content.find_elements_by_tag_name('a')
for li in lis:
    print(li.text)


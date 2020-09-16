# -*- coding: utf-8 -*-

import time
import pandas as pd   
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://www.youtube.com/watch?v=1GPsepFmNes&ab_channel=BGMmaker"

data=[]
with Chrome(executable_path="chromedriver.exe") as driver:
    wait = WebDriverWait(driver,15)
    driver.get(link)
    for item in range(5): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
        time.sleep(45)
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
            data.append(comment.text)

df = pd.DataFrame(data, columns=['comment'])
df.head()
print(data)
print(len(data))
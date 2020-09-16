# -*- coding: utf-8 -*-

import time
import pandas as pd   
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.youtube.com/watch?v=rzWSEtahHus&ab_channel=EltonJohn"
def scraping(link):
    # Input : a link which is the link to a video
    # Output : a list of comments
    # Goal : scrap few comments for make a sentimental analysis of them
    data=[]
    with Chrome(executable_path="chromedriver.exe") as driver:
        wait = WebDriverWait(driver,15)
        driver.get(link)
        for item in range(3): 
            # range is for the number of commentary you wan't to have
            wait.until(EC.visibility_of_element_located((By.TAG_NAME,"body"))).send_keys(Keys.END)
            time.sleep(100) 
            # range is the time you nedd for scrap all the comments
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
                data.append(comment.text)
    
    df = pd.DataFrame(data, columns=['comment'])
    df.head()
    return data

test = scraping(link)
print(len(test))
print(test)
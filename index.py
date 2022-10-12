from pprint import pprint
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pprint import pprint
#import mysql.connector
#import time 
#import conexion
def waitUntilReady(driver, delay, by, value_by):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, value_by)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    #PATH = "C:\\Data\\Universidad\\twitterselenium\\chromedriver.exe"
    #driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome('./chromedriver')
def getTweets(user):
    driver.get("https://twitter.com/" + user)
    waitUntilReady(driver, 5, By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='tweet']")
    #elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
    for element in elements:
        print(element.text)
    #print(elements.text)
    #set(elements)

users = (["@ManuelTurizoMTZ","@andrescepeda","@Greeicy_rendon", "@TheRock" , "@J_Rodrigues99"])    
for user in users: 
    getTweets(user)  
#driver.close()


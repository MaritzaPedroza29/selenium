from contextlib import nullcontext
from pprint import pprint
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pprint import pprint
import mysql.connector

users = (["@ManuelTurizoMTZ"])    
conexion = nullcontext
driver = webdriver.Chrome('./chromedriver')

def openDB():
    conexion = mysql.connector.connect(
        user='root', password='', host='localhost', database='twitter'
    )

def insertarSQL(sql):
    openDB()
    cursor = conexion.cursor()
    try:
        cursor.execute(sql)
        conexion.commit()
    except:
        conexion.rollback()
    conexion.close()
    return 0

def guardarTweet(texto):
    sql= "insert into dato(twitter) values(`"+texto+"`)"
    print("sql " + sql)
    try:
        insertarSQL(sql)
        return True
    except:
        print("Error al insertar: ", sql)
        return False

def waitUntilReady(driver, delay, by, value_by):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, value_by)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

def getTweets(user):
    driver.get("https://twitter.com/" + user)
    waitUntilReady(driver, 5, By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='tweet']")
    for element in elements:
        txt = element.text
        txtLimpio = txt.replace('\n', ' ')
        #txtLimpio = txt.rstrip('\n')
        #guardarTweet(txt)
        print(txtLimpio)

for user in users: 
    print(user)
    getTweets(user)  
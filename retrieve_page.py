from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import winsound


newsletter = "https://forocoches.substack.com/"

def init():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    return driver

driver = init()

def reload():
    
    driver.get(newsletter)
    maybe_later = driver.find_element(By.CLASS_NAME, "maybe-later")
    if (maybe_later): 
        maybe_later.click()
    
    while True:
        driver.get(newsletter)
        title = driver.find_element(By.CLASS_NAME, "post-preview-title")
        link = title.get_attribute("href")
        if (link != "https://forocoches.substack.com/p/unos-guaguas-un-estadio-haciendo"):
            driver.get(link)
            párrafos = driver.find_elements(By.XPATH, "//h3[text()='Las invis']/following-sibling::p")
            instrucciones = párrafos[1].text
            códigos = [párrafos[2].text, párrafos[3].text, párrafos[4].text]
            print(instrucciones)
            print(códigos)
            notes = {'C': 1635, 'E': 2060, 'F': 2183, 'G': 2450, 'A': 2750, ' ': 37}
            melody = 'EAGC CGAE AFGC CGAF' 
            for note in melody:
                winsound.PlaySound(notes[note], 700)
            break
        time.sleep(15)


reload()

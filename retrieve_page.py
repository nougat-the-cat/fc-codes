from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import winsound


newsletter = "https://forocoches.substack.com/"

def unhyphen(string):
  return string.replace("-", "")

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
        if (link != "https://forocoches.substack.com/p/[1ST URL LATEST WEEK HERE]"):
            driver.get(link)
            párrafos = driver.find_elements(By.XPATH, "//h3[text()='Las invis']/following-sibling::p")
            instrucciones = párrafos[1].text
            códigos = [párrafos[2].text, párrafos[3].text, párrafos[4].text]
            print(instrucciones)
            for código in códigos:
                clean_string = unhyphen(código)
                print(clean_string)
            
            note_freqs = {
                "B3": 246.9, "C4": 261.63, "C#4": 277.2, "D4": 293.66, "Eb4": 311.1, "E4": 329.63, "F4": 349.23, 
                "F#4": 370, "G4": 392.00, "G#4": 415.3, "A4": 440.00, "Bb4": 466.2, "B4": 493.88, " ": 37
            }

            melody = [
                ("F4", 125), ("A4", 125), ("G4", 125), ("C4", 125), (" ", 125), 
                ("A4", 125), ("F4", 125), ("G4", 125), ("C4", 125), (" ", 125), 
                ("C4", 250), ("G4", 125), ("A4", 125), ("F4", 125), (" ", 125), 
                ("F4", 125), ("G4", 125), ("A4", 125), ("F4", 125), (" ", 125), 
            ]

            for note, duration in melody:
                freq = note_freqs[note]
                winsound.Beep(int(freq), duration*6)
            break
        time.sleep(15)


reload()

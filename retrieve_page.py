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


def unhyphen(string):
    clean = string.replace("-", "")
    return clean

def swapcase(codes):
    swapped = ""
    for i in range(len(codes)):
        swapped += codes[i].swapcase()
    return swapped

def swap(string, pos1, pos2):
    string = list(string)
    string[pos1], string[pos2] = string[pos2], string[pos1]
    string = ''.join(string)
    return string

def first_number(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return i

def last_number(string):
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            return i

def swap_numbers(string):
    pos1 = first_number(string)
    pos2 = last_number(string)
    string = swap(string, pos1, pos2)
    return string


def reload():
    driver.get(newsletter)
    maybe_later = driver.find_element(By.CLASS_NAME, "maybe-later")
    if (maybe_later): 
        maybe_later.click()
    
    while True:
        driver.get(newsletter)
        title = driver.find_element(By.CLASS_NAME, "post-preview-title")
        link = title.get_attribute("href")
        if (link != "https://forocoches.substack.com/p/[1st url latest week]"):
            driver.get(link)
            párrafos = driver.find_elements(By.XPATH, "//h3[text()='Las invis']/following-sibling::p")
            instrucciones = párrafos[1].text
            códigos = [párrafos[2].text, párrafos[3].text, párrafos[4].text]
            códigos = list(map(unhyphen, códigos))
            swapped = list(map(swapcase, códigos))
            first_last_num_swapped_swap = list(map(swap_numbers, swapped))
            first_last_num_swap = list(map(swap_numbers, códigos))
            print(instrucciones+"\n")
            print("Sin guiones: " + str(códigos))
            print("May. por minúsc.: " + str(swapped))
            print("May. por minúsc. y primer por últ. núm. : " + str (first_last_num_swapped_swap))
            print("Solo primer por últ. núm.: " + str(first_last_num_swap))

            note_freqs = {
                "B3": 246.9, "C4": 261.63, "C#4": 277.2, "D4": 293.66, "Eb4": 311.1, "E4": 329.63, "F4": 349.23, 
                "F#4": 370, "G4": 392.00, "G#4": 415.3, "A4": 440.00, "Bb4": 466.2, "B4": 493.88, " ": 37,
            }

            melody = [
                ("F4", 125), ("A4", 125), ("G4", 125), ("C4", 125), (" ", 125), 
                ("A4", 125), ("F4", 125), ("G4", 125), ("C4", 125), (" ", 125), 
                ("C4", 250), ("G4", 125), ("A4", 125), ("F4", 125), (" ", 125), 
                ("F4", 125), ("G4", 125), ("A4", 125), ("F4", 125), (" ", 125)
            ]

            for note, duration in melody:
                freq = note_freqs[note]
                winsound.Beep(int(freq), duration*7)
            break
        time.sleep(15)


reload()

import telegram 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.update import Update
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import winsound
from methods import *


TOKEN = "[YOUR TOKEN]"
CHAT_ID = "[YOUR CHAT ID]"
newsletter = "https://forocoches.substack.com/"
invitaciones = "https://forocoches.com/codigo/"

bot = telegram.Bot(token=TOKEN)


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
        if (link != "https://forocoches.substack.com/p/una-necroporra-un-jabali-de-200kg"):
            driver.get(link)
            párrafos = driver.find_elements(By.XPATH, "//h3[text()='Las invis']/following-sibling::p")
            instrucciones = párrafos[0].text
            códigos = [párrafos[1].text, párrafos[2].text, párrafos[3].text]
            
            códigos = list(map(unhyphen, códigos))
            swapped = list(map(swapcase, códigos))
            highest_del = list(map(del_highest, swapped))
            lowest_del = list(map(del_lowest, swapped))

            bot.send_message(chat_id=CHAT_ID, text=instrucciones)
            bot.send_message(chat_id=CHAT_ID, text=invitaciones)
            bot.send_message(chat_id=CHAT_ID, text="Sin guiones: \n\n" + str(códigos))
            bot.send_message(chat_id=CHAT_ID, text="Sin guiones, may. por minúsc. y viceversa: \n\n" + str(swapped))
            bot.send_message(chat_id=CHAT_ID, text="Sin guiones, may. por minúsc. y viceversa, núm. más alto eliminado: \n\n" + str(highest_del))
            bot.send_message(chat_id=CHAT_ID, text="Sin guiones, may. por minúsc. y viceversa, núm. más bajo eliminado: \n\n" + str(lowest_del))

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

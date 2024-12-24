from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from selenium import *
from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
from selenium.webdriver.support import expected_conditions as EC

BaseCase.main(__name__, __file__)  # Call pytest


class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://cnvmp3.com/")
        
        xpathFORMAT = "/html/body/main/section[2]/div[1]/div/div[2]/div[3]/div[2]"
        WebDriverWait(self, 20).until(EC.visibility_of_element_located((By.XPATH, xpathFORMAT))).click()
        
        elem_listFORMAT = self.find_elements(By.XPATH, "/html/body/main/section[2]/div[1]/div/div[2]/div[3]/div[3]")

        link = "https://www.youtube.com/watch?v=2DVJoyzzHrY"
        format = "MP4"
        VIDEOquality = "360"
        AUDIOquality = "96"
        qualityID = "quality-video-select-list-" + VIDEOquality
        audioID = "quality-audio-select-list-" + AUDIOquality

        if format == "MP4" :
            self.sleep(2)
            elem_listFORMAT[0].click()
            xpathQUALITY = "/html/body/main/section[2]/div[1]/div/div[2]/div[1]"
            WebDriverWait(self, 20).until(EC.visibility_of_element_located((By.XPATH, xpathQUALITY))).click()
            elemQUALITY = self.find_element(By.ID, qualityID)
            elemQUALITY.click()
            self.sleep(2)
        elif format == "MP3":
            xpathAUDIO = "/html/body/main/section[2]/div[1]/div/div[2]/div[2]/div[2]"
            WebDriverWait(self, 20).until(EC.visibility_of_element_located((By.XPATH, xpathAUDIO))).click()
            elemAUDIO = self.find_element(By.ID, audioID)
            elemAUDIO.click()
            self.sleep(2)
        
        link_enter = self.find_element(By.ID, "video-url")
        link_enter.send_keys(link)
        
        convertButton = self.find_element(By.ID, "convert-button")
        convertButton.click()

        wait = WebDriverWait(self, 10)
        wait.until(EC.title_is("SeleniumHQ Browser Automation"))
        keyboard.press_and_release('enter')
        self.sleep(4)

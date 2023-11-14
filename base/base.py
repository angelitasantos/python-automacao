#----------------------------------------------------------------------------------------------------------------
# DEFINIR AS BIBLIOTECAS QUE SERÃO UTILIZADAS E AS FUNÇÕES PADRÕES


# -*- coding: utf-8 -*-
import sys
import os
from datetime import date
import time
from time import sleep
import pyautogui
import pyperclip
from xml.etree import cElementTree as ETree
import xml.etree.ElementTree as ETree
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import openpyxl
import pynput
import locale


class Base:

    def __init__(self, base):
        self.base = base

    def __repr__(self):
        return self.base
    
    self = 'self'
    time_sleep_1 = 1
    time_sleep_3 = 3
 
    def abrir_powershell(self):
        pyautogui.hotkey('win', 'r')
        time.sleep(Base.time_sleep_1)
        pyautogui.write('powershell')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def fechar_powershell(self):
        pyautogui.write('exit')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def executar_hotkey_colar(self):
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(Base.time_sleep_1)
        pyautogui.press('enter')
        time.sleep(Base.time_sleep_1)

    def executar_hotkey_copiar(self, destino, origem):
        copiar_item = f'Copy-Item "{destino}" "{origem}"'
        pyperclip.copy(copiar_item)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)

    def executar_comando_cd(self, caminho_rede):
        time.sleep(Base.time_sleep_1)
        comando_cd = f'cd "{caminho_rede}"'
        pyperclip.copy(comando_cd)
        time.sleep(Base.time_sleep_1)
        Base.executar_hotkey_colar(self)
        time.sleep(Base.time_sleep_1)



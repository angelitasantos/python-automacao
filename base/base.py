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

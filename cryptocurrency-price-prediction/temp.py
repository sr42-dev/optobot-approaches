'''
import tensorflow
import json
import requests
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, LSTM
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error
import matplotlib
'''
import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import json
import random
import re
import time
from datetime import datetime
from threading import Timer
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
'''
endpoint = 'https://min-api.cryptocompare.com/data/histoday'
res = requests.get(endpoint + '?fsym=BTC&tsym=CAD&limit=500')
data = json.loads(res.content)['Data']

for element in data:

    element.pop('conversionType', None)
    element.pop('conversionSymbol', None)

hist = pd.DataFrame(data)
print('______________________________________________')
print(hist)
hist = hist.set_index('time')
hist.index = pd.to_datetime(hist.index, unit='s')

# 10 digit format to Y-M-D H:M:S

#from datetime import datetime
#ts = int("1284101485")
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


print('______________________________________________')
print(hist)
print('______________________________________________')
print(dict(hist))
print('______________________________________________')
print(hist.head(5))
print('______________________________________________')
print(dict(hist.head(5)))
print('______________________________________________')
print((dict(hist.head(5))['volumefrom'].to_dict()))
print('______________________________________________')
print(str(list((dict(hist.head(5))['volumefrom'].to_dict()).keys())[0]))
print('______________________________________________')

datatypes1 = ['high','low','open','volumefrom','volumeto','close']
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def init_browser():
    global browser


    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3') # open in profile 3 (person 1)
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--use-fake-ui-for-media-stream')
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.default_content_setting_values.media_stream_mic': 1,
        'profile.default_content_setting_values.media_stream_camera': 1,
        'profile.default_content_setting_values.geolocation': 1,
        'profile.default_content_setting_values.notifications': 1,
        'profile': {
            'password_manager_enabled': False
        }
    })
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # make the window a minimum width to show the meetings menu
    window_size = browser.get_window_size()
    if window_size['width'] < 1200:
        print("Resized window width")
        browser.set_window_size(1200, window_size['height'])

    if window_size['height'] < 850:
        print("Resized window height")
        browser.set_window_size(window_size['width'], 850)

init_browser()

browser.get("https://binomo.com/")

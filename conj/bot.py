import re
import pyautogui
from time import sleep
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import keyboard

# [x] Map english words to spanish words
# [x] Get relavent region of the screen
# [x] Recognize english word
# [x] Enter spanish word
# [] Put it all together!

vocab = {}

with open('vocab.txt', encoding='utf-8') as vocabFile:
    for line in vocabFile:
        words = re.split('\t|\n|/', line)
        vocab[words[0]] = words[1]
# x, y = 367 460
# x, y = 1449 552

X = 367
Y = 460
WIDTH = 1449 - X
HEIGHT = 552 - Y

keyboard.wait('esc')

while 1:
    img = pyautogui.screenshot(region=(X, Y, WIDTH, HEIGHT))
    english = pytesseract.image_to_string(img).lower().split('\n')[0]
    keyboard.write(vocab[english])
    keyboard.press_and_release('enter')
    sleep(0.1)
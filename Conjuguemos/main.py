import re
import pyautogui
from time import sleep
import keyboard
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

vocab = {}


with open('vocab.txt', encoding='utf-8') as vocabFile:
    for line in vocabFile:
        words = re.split('\t|\n|/', line)
        print(words)
        vocab[words[0]] = words[-2]

# print(vocab)
# while 1:
    # print(pyautogui.position())
    # sleep(1)
# pyautogui.displayMousePosition()

topLeftCorner = (363, 457)
bottomRightCorner = (1448, 616)

LEFT = topLeftCorner[0]
TOP = topLeftCorner[1]
WIDTH = bottomRightCorner[0] - topLeftCorner[0]
HEIGHT = bottomRightCorner[1] - topLeftCorner[1]

keyboard.wait('esc')
while not keyboard.is_pressed('q'):
    img = pyautogui.screenshot(region=(LEFT, TOP, WIDTH, HEIGHT))
    output = pytesseract.image_to_string(img).lower()
    output = re.split('\n|/', output)[0]
    keyboard.write(vocab[output])
    keyboard.press_and_release('enter')
    sleep(0.1)

# C:\Program Files\Tesseract-OCR

# x, y = 363 457
# x, y, 1448 616

import pyautogui as pg
import cv2
import pytesseract
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pg.click(636, 396)

timer = time.time()
while True:
    if time.time() - timer <= 60:
        file_name = 'screen.png'
        pg.screenshot(file_name, region=(420, 250, 1000, 125))
        img = cv2.imread(file_name)
        text_for_typing = pytesseract.image_to_string(img).split()
        for word in text_for_typing:
            pg.typewrite(word)
            pg.typewrite(['space'])
    else:
        print('Congratulations')
        break






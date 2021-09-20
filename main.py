import cv2
from handTrackingModule import HandDetector
from button import Button
from time import sleep
from pynput.keyboard import Controller, Key


DETECTION_LENGTH = 20
SLEEP_TIME = 0.35

cap = cv2.VideoCapture(0)

cap.set(3, 850) # width
cap.set(4, 720) # height

detector = HandDetector(detectionCon=0.8)

qwerty = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'back'],
          ['A', 'S', 'D', 'F', "G", 'H', 'J', 'K', 'L', ';', "'", 'enter'],
          ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']]

typedText = ''

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.position
        w, h = button.size
        drawButton(button, (255, 0, 255), x, y, w, h)
    return img


def drawButton(button, color, x, y, w, h):
    cv2.rectangle(img, button.position, (x + w, y + h), color, cv2.FILLED)
    cv2.putText(img, button.text, (x + 20, y + 45),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), thickness=3)


def typing(button):
    if button.text == 'enter':
        global typedText
        typedText = ''
        keyboard.press(Key.enter)

    elif button.text == 'back':
        typedText = typedText[:-1]
        keyboard.press(Key.backspace)

    else:
        typedText += button.text
        keyboard.press(button.text)
    sleep(SLEEP_TIME)

keyboard = Controller()

buttonList = []
for i in range(len(qwerty)):
    for j, key in enumerate(qwerty[i]):
        buttonList.append(Button([70 * j + 20, 70 * i + 20], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img) # detect hand
    lmList, bboxInfo = detector.findPosition(img) # make box and get list of points
    img = drawAll(img, buttonList)

    if lmList: # check if there is a hand in the mage
        for button in buttonList:
            x, y = button.position
            w, h = button.size

            # check if the tip of our index finger (8) is in the area
            if x <= lmList[8][0] <= x+w and y <= lmList[8][1] <= y+h:
                drawButton(button, (175, 0, 175), x, y, w, h)

                # mark as a click when the index finger and middle finger are close together
                length, _, _ = detector.findDistance(8, 12, img)

                if length < DETECTION_LENGTH:
                    drawButton(button, (0, 255, 0), x, y, w, h)
                    typing(button)




    # rectangle to know what we typed
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0,  175), cv2.FILLED)
    cv2.putText(img, typedText, (60, 425),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
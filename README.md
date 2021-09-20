# virtual_keyboard

The project creates a virtual keyboard using mainly mediapipe and opencv so that you can still have access to your keyboard when you are far away form the laptop. For instance, in my case, when I connect my laptop to the TV using HDMI cable, I don't want to have to stand up everytime I want to watch something else.


## How it works:
The project tracks your index finger. More specifically, it tracks the hand MediaPipe index 8 in order to know whether you are on a certain key.
When you want to hit on a key, move your index finger and your middle finger close to one another. More specifically, the distance between index 8 and index 12 will be tracked.

![alt text](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)

After running the program, click on anywhere you would want to use your keyboard, and start typing!

### Very Important!
Depending on how far away from the webcame you are, you will want to tune the treshold of the distance in detection (the further away from the webcam you will be, the lower the threshold should be in order to not accidently click into a button.
You might want to also change the confidence level of the detection. All of which you can find in the main.py

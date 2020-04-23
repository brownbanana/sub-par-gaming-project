
from pygame import mixer
import os,time

mixer.init()
mixer.music.load("C:\\Users\\iogby\\AppData\\Local\\qwe\\moist1moist.mp3")

time.sleep(120)
a = 1
while True:
    os.system("C:\\Users\\iogby\\AppData\\Local\\qwe\\moist1\\moist{}.png".format(a))
    time.sleep(1)
    mixer.music.play()
    time.sleep(30)
    a += 1
    if a == 6:
        a = 1

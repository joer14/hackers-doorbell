# Joe Rowley - 2017
# little web app you can run on your own machine
# when someone pings your ip address at port 5000
# the app will flash your screen and pause your music
# make sure you enable the keyboard shortcut:
# http://www.cultofmac.com/215227/make-the-invert-display-keyboard-shortcut-work-again-in-mountain-lion-os-x-tips/

import os
from time import sleep
from flask import Flask
app = Flask(__name__)

invertCmd = """
osascript -e 'tell application "System Events" to key code 28 using {control down, option down, command down}'
"""
muteCmd = """
osascript -e 'tell application "System Events" to set volume with output muted'
"""
unmuteCmd = """
osascript -e 'tell application "System Events" to set volume without output muted'
"""
# may want to switch Spotify to iTunes or music player of choice
pauseCmd = """
osascript -e 'tell application "Spotify" to pause'
"""

def invert():
    os.system(invertCmd)
    sleep(0.1)

def flash(iters):
    for _ in range(iters):
        invert()
        sleep(0.1)
        invert()
        sleep(0.1)

def activate():
    os.system(pauseCmd)
    os.system(muteCmd)
    flash(3)
    os.system(unmuteCmd)

@app.route('/')
def hello_world():
    activate()
    return 'Ding dong!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')

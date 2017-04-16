# Hackers Doorbell
A one button device that emulates a keyboard and mutes audio to alert a headphone wearing user of another person's physical presence. 
---
<p align="center">
<a href="url"><img alt="button in glass jar with usb cord" src="http://i.imgur.com/063OOYC.jpg" align="center" height="400"></a>
</p>

## What it does:

When someone pushes the button, the device simulates the pause button being pushed on the keyboard, then the mute button. After that it quickly inverts and uninverts the colors on the screen by using a built in Apple shortcut. Finally it unmutes the volume. This should alert the computer user to the presence of someone else. 

## Demo:

<p align="center">
<a href="url"><img alt="button in glass jar pauses music on computer." src="https://media.giphy.com/media/l0IxYNhAo3AKqwSIw/giphy.gif" align="center" height="400"></a>
</p>

In addition to muting audio, the screen flashes and the music app goes from playing to paused.


## Why:

I work in an open office, and have issues focusing when people are talking around me, so I often wear large overear headphones and listen to [music](https://www.last.fm/user/joer14). This is fine except that when people need to get my attention they often either tap me on the shoulder or have to stand and talk loudly into my (headphone covered) ears, or wave something awkwardly close to me (since I sit in a corner they can't just walk in front of my desk). I'm fine with the physical contact but it's still a little jarring when you're deep in flow and it can be awkward for other people. With this device, my coworkers can simply push a button that lays next to my desk and not startle me. 

## How:

I use a [Teensy 3.1 microprocessor ](https://www.pjrc.com/store/teensy31.html) connected to a push button to emulate a keyboard. When the button is pushed a series of keyboard shortcuts is executed.

## Cool Thing About this Approach:

You don't need any special software running on your mac, just the ability to [enable a default keyboard shortcut](http://www.cultofmac.com/215227/make-the-invert-display-keyboard-shortcut-work-again-in-mountain-lion-os-x-tips/) on your mac. 

## Materials:

- [Teensy 3.1 ($20)](https://www.pjrc.com/store/teensy31.html) - any microprocessor that supports HID Keyboard emulation should work. I just had one of these laying around. A TEENSY LC is $12 and should also work. [Sparkfun’s ProMicro ($20)](https://www.sparkfun.com/products/12640) should also work. 
- Push Button (~$2). I a few arcade style buttons around, but [this one](https://www.sparkfun.com/products/9336) should work (keep in mind your case space constraints). 
- 10k [pullup resistor](https://en.wikipedia.org/wiki/Pull-up_resistor)
- A case. I used a glass nug jug from [CBCB](http://cbcbberkeley.com) in Berkeley. Sometimes you need to buy their top shelf stuff to get glass jars, so YMMV. 
- Miscellaneous connectors (I recommend using headers so you can reuse your board for a later project potentially) 
    - [Break Away Headers - you need male and female (Spacing: 0.1"/ 2.54 mm)](https://www.sparkfun.com/products/116)
    - Wire and terminal connectors to connect to your button
- Solder
- USB Cable

## Tools:
- Soldering Iron
- Pen to trace your cuts
- Case cutting tool(s). I used my soldering iron to cut up the case, because I love the smell of chlorine / am lazy and a bad person. I recommend you use a vice + drill press + rotary tool + a little sandpaper. Way cleaner looking results and your eyes won't hurt from the smell of burning chlorine. 

## Software:
- [Arduino IDE](https://www.arduino.cc/en/main/software) (1.8.2 at time of writing)
- [Teensy Loader App](https://www.pjrc.com/teensy/loader.html) (1.33 at time of writing) 
- [Teensy Arduino Install Package](https://www.pjrc.com/teensy/teensyduino.html) (1.36 at time of writing)

## Other:
- [Image gallery including schematic and a few tips](http://imgur.com/a/Q9pLy)

## Buying a Doorbell:
Do you want one of these devices, for yourself or a coworker? Maybe a department pack? Please fill out [this survey](https://goo.gl/forms/Xr6fzHABMX8Xw1Yh2). If enough people express interest, I may look into reducing the cost, and either selling kits or preassembled units. I could also add a dip switch so that people could easily change shortcuts to fit specific operating system. 

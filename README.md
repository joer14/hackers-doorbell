# Hackers Doorbell
A 1 button device that emulates a keyboard and mutes audio to alert a headphone wearing user of another person's physical presence. 
---
<p align="center">
<a href="url"><img alt="button in glass jar with usb cord" src="http://i.imgur.com/063OOYC.jpg" align="center" height="400"></a>
</p>

## What it does:

When someone pushes the button, the device simulates the pause button being pushed on the keyboard, then the mute button. After that it quickly inverts and uninverts the colors on the screen by using a built in Apple shortcut. Finally it unmutes the volume. This should alert the computer user to the presence of someone else. 

## Why:

I work in an open office, and have issues focusing when people are talking around me, so I often wear large overear headphones and listen to [music](https://www.last.fm/user/joer14). This is fine except that when people need to get my attention they often either tap me on the shoulder or have to stand and talk loudly into my (headphone covered) ears, or wave something awkwardly close to me (since I sit in a corner they can't just walk in front of my desk). I'm fine with the physical contact but it's still a little jarring when you're deep in flow and it can be awkward for other people. With this device others can simply push a button that lays next to my desk and not startle me. 

## How:

I use a [Teensy 3.1 microprocessor ](https://www.pjrc.com/store/teensy31.html) connected to a button to emulate a keyboard. When the button is pushed a series of keyboard shortcuts is executed.

## Cool Things About this Approach:

You don't need any special software running on your mac, just the ability to [enable a default keyboard shortcut](http://www.cultofmac.com/215227/make-the-invert-display-keyboard-shortcut-work-again-in-mountain-lion-os-x-tips/) on your mac. 

## Materials:

- [Teensy 3.1 ($20)](https://www.pjrc.com/store/teensy31.html) - any microprocessor that supports HID Keyboard emulation should work. I just had one of these laying around. A TEENSY LC is $12 and should also work. [Sparkfun’s ProMicro ($20)](https://www.sparkfun.com/products/12640) should also work. 
- Push Button (~$2). I had one already around, but [this one](https://www.sparkfun.com/products/9336) should work (keep in mind your case space constraints). 
- 10k [pullup resistor](https://en.wikipedia.org/wiki/Pull-up_resistor)
- A case. I used a glass nug jug from [CBCB](http://cbcbberkeley.com) in Berkeley.
- Miscellaneous connectors (I recommend using headers so you can reuse your board for a later project potentially) 
    - [Break Away Headers - you need male and female (Spacing: 0.1"/ 2.54 mm)](https://www.sparkfun.com/products/116)
    - Wire and terminal connectors to connect to your button
- Solder
- USB Cable

## Tools:
- Soldering Iron
- Pen to trace your cuts
- Cutting tool for mounting stuff in your case (I used my soldering iron to cut up the case, because I love the smell of chlorine/am lazy/a bad person)

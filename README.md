DJ Spotify
==========

Hacked together at MIDEM Music Hack Day 2014. 

Here's the hack in action: [http://www.youtube.com/watch?v=uTgwAMZiwMw](http://www.youtube.com/watch?v=uTgwAMZiwMw)

## How it works
This system relies on a virtual machine (Parallels in my hack's case) to play a second Spotify stream. The two streams are then sent into individual tracks in Ableton Live, each with a Max For Live patch which reads the Spotify streams into internal buffers which can then be sped up or slowed down at will, effectively allowing you to beat-match and, theoretically, do a whole DJ with streamed content. 

## Components and required software
![DJ Spotify topology](http://reactifymusic.com/wp-content/uploads/2014/02/DJ-Spotify-diagram-1.jpg)
The above is a diagram of how the hack works. As you can see it's a complete spider's web of messy hacks involving most components of the OS.

In order to recreate this particular set-up on your machine you will need the following software installed:
- [Ableton Live](https://www.ableton.com/)
- [Max For Live](https://www.ableton.com/en/live/max-for-live/)
- [SoundFlower](http://cycling74.com/soundflower-landing-page/)
- [Pure data](http://puredata.info/)
- [Spotify](https://www.spotify.com/us/download/)
- [Parallels](http://www.parallels.com/)

There are alternatives for many of these programs e.g. Jack instead of Soundflower, Virtual Box instead of Parallels, and Pure data is simply used to reroute the output of Soundflower to another input of Soundflower, so really, any DAW application capable of passing audio from an input to an ouput will do...

For the automated retreival of EchoNest data for the currently playing Spotify track, you will also need:
- [Growl](http://growl.info/)
- [pyechonest](https://github.com/echonest/pyechonest)
- [appscript](https://pypi.python.org/pypi/appscript)
- [pyOSC](https://pypi.python.org/pypi/pyOSC)

If you choose to use Spotify and would like to display key and BPM information alongside your playlists, you can also install and use my Key and BPM Spotify app, the code for which can be found here:
- [Spotify Key BPM App](https://github.com/reactify/spotify-key-bpm)

Finally, if you would like to control Ableton Live with a custom DJing template on the iPad, install TouchOSC on your iPad:
- [TouchOSC](http://hexler.net/software/touchosc)

## Method
#### Two audio streams
1. On your main machine, install all of the above software and start Spotify
2. On your virtual machine, install Spotify and, if desired, Growl, pyechonest, appscript and pyOSC
3. On your main machine start SoundFlower and set the system audio output to be SoundFlower (64ch) in your System Preferences
4. Set the audio output of Parallels (note: *not* the system output of your virtual machine, but of the virtual machine hosting software itself) to be SoundFlower (2ch)
5. Open _main.pd and set it's input device to be SoundFlower (2ch) and it's output to be SoundFlower (64ch)
6. Start Live Template.als in Ableton Live and set the audio input of Live to by SoundFlower (64ch). Set the audio output to be whatever you want e.g. Built-in Output or an external soundcard
Start audio playing on your main and virtual machines, and, in Live, you should now see audio from your main machine coming in on Track 1, and audio from your virtual machine coming in on Track 2

#### Automated key and BPM retreival from Echonest
Unless otherwise stated, the following steps must be performed on both your main and virtual machines

1. Open Growl and place the Rules.scpt file in the following path: 
	"/Users/[username]/Library/Application Scripts/com.Growl.GrowlHelperApp/"
	Growl should run this AppleScript every time it receives a notification, so we use it to automatically launch the getTempoAndKey.py Python script which, in turn, queries Spotify for it's currently playing track, retreives the Key/BPM/Mode data for that track from EchoNest, and sends that information over OSC
2. Check that Growl is running the AppleScript by uncommenting the 'say "hello"' line in the Rules.scpt. Try skipping tracks in Spotify. If your machine says 'Hello', then you're good to go
3. In Rules.scpt change the path to the getTempoAndKey.py file to wherever you have it saved
4. In getTempoAndKey.py change the EchoNest API Key on line 7 to your own one. Go [here](http://developer.echonest.com/) if you need to get an EchoNest API Key.
5. On your main machine, change the port number on line 4 of getTempoAndKey.py to 8070, and to 8090 on the virtual machine
6. In Live on your main machine, check that the key and BPM data is coming through to the Stream-Pitch Max For Live devices on tracks 1 and 2

#### Extra brownie points - controlling Live
Now that you've got all the audio coming in to Live, you could make MIDI mappings to any hardware controller you happen to have lying around. If you would like to use the TouchOSC layout I made for iPad, follow these steps

1. Set-up TouchOSC to communicate with your main machine. [Instructions here](http://hexler.net/docs/touchosc-configuration)
2. Open TouchOSC Editor and sync the Max DJ.touchosc layout on to your iPad [Instructions here](http://hexler.net/docs/touchosc-editor-sync)
3. With any luck, all the MIDI mappings should still be present in Live, but if they're not, remake them

#### Even more extra brownie points - displaying arist, title and BPM information in TouchOSC
The Live template also has the capacity to talk back to the TouchOSC layout so that it can display the aritst, title and BPM information of the currently playing tracks. To get this working:

1. In the Master track in Live, open the Master-tempo-send Max For Live device and change the IP address and port number to those of your iPad. Again, see [here](http://hexler.net/docs/touchosc-configuration) for instructions on where to find those

#### Beer time!
Now, go and pour yourself a tasty beverage because you deserve it for getting this far. Tweet us at [@reactify](www.twitter.com/reactify) if you do because I would like to personally congratulate you (on getting this far, not pouring yourself a tasty beverage...)

#### Legal stuff
Copyright (c) [2014] [Yuli Levtov]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
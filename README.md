DJ Spotify
==========

Hacked together at MIDEM Music Hack Day 2014. The hack in action
[http://www.youtube.com/watch?v=uTgwAMZiwMw](http://www.youtube.com/watch?v=uTgwAMZiwMw)

# How it works
This system relies on a virtual machine (Parallels in my hack's case) to play a second Spotify stream. The two streams are then sent into individual tracks in Ableton Live, each with a Max For Live patch which reads the Spotify streams into internal buffers which can then be sped up or slowed down at will, effectively allowing you to beat-match and, theoretically, do a whole DJ with streamed content. 

# Components and required software
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

Optional, for the automated retreival of EchoNest data for the currently playing Spotify track:
- [Growl](http://growl.info/)
- [pyechonest](https://github.com/echonest/pyechonest)
- [appscript](https://pypi.python.org/pypi/appscript)
- [pyOSC](https://pypi.python.org/pypi/pyOSC)
from appscript import *
import OSC

port = 8070

from pyechonest import config
config.ECHO_NEST_API_KEY="XKAK8BHSXTQSZ1YQKXKLLAA"
        
title = app(u'Spotify').current_track.name.get()
artist = app(u'Spotify').current_track.artist.get()

print title
print artist

from pyechonest import song

rkp_results = song.search(artist=artist, title=title)

print 'tempo:',rkp_results[0].audio_summary['tempo']
print 'key:',rkp_results[0].audio_summary['key']
print 'mode:',rkp_results[0].audio_summary['mode']
print 'time_signature:',rkp_results[0].audio_summary['time_signature']

tempo = rkp_results[0].audio_summary['tempo']
key = rkp_results[0].audio_summary['key']
mode = rkp_results[0].audio_summary['mode']
timesig = rkp_results[0].audio_summary['time_signature']

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/key")
msg.append(key)
client.sendto(msg, ('localhost', port))

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/mode")
msg.append(mode)
client.sendto(msg, ('localhost', port)) 

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/tempo")
msg.append(tempo)
client.sendto(msg, ('localhost', port))

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/title")
msg.append(title)
client.sendto(msg, ('localhost', port)) 

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/artist")
msg.append(artist)
client.sendto(msg, ('localhost', port)) 
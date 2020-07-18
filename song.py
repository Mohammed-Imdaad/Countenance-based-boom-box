import os
import threading
import time
from mutagen.mp3 import MP3
from pygame import mixer
import random 
happy_playlist = ["happy\\1.mp3","happy\\2.mp3","happy\\3.mp3","happy\\4.mp3","happy\\5.mp3","happy\\6.mp3","happy\\7.mp3","happy\\8.mp3","happy\\9.mp3","happy\\10.mp3"]
sad_playlist=["sad\\1.mp3","sad\\2.mp3","sad\\3.mp3","sad\\4.mp3","sad\\5.mp3","sad\\6.mp3","sad\\7.mp3","sad\\8.mp3","sad\\9.mp3","sad\\10.mp3"]
angry_playlist=["angry\\1.mp3","angry\\2.mp3","angry\\3.mp3","angry\\4.mp3","angry\\5.mp3","angry\\6.mp3","angry\\7.mp3","angry\\8.mp3","angry\\9.mp3","angry\\10.mp3"]
surprised_playlist=["surprised\\1.mp3","surprised\\2.mp3","surprised\\3.mp3","surprised\\4.mp3","surprised\\5.mp3","surprised\\6.mp3","surprised\\7.mp3","surprised\\8.mp3","surprised\\9.mp3","surprised\\10.mp3"]
disgusted_playlist=["disgusted\\1.mp3","disgusted\\2.mp3","disgusted\\3.mp3","disgusted\\4.mp3","disgusted\\5.mp3","disgusted\\6.mp3","disgusted\\7.mp3","disgusted\\8.mp3","disgusted\\9.mp3","disgusted\\10.mp3"]
fear_playlist=["fear\\1.mp3","fear\\2.mp3","fear\\3.mp3","fear\\4.mp3","fear\\5.mp3","fear\\6.mp3","fear\\7.mp3","fear\\8.mp3","fear\\9.mp3","fear\\10.mp3"]
confused_playlist=["confused\\1.mp3","confused\\2.mp3","confused\\3.mp3","confused\\4.mp3","confused\\5.mp3","confused\\6.mp3","confused\\7.mp3","confused\\8.mp3","confused\\9.mp3","confused\\10.mp3"]
calm_playlist=["calm\\1.mp3","calm\\2.mp3","calm\\3.mp3","calm\\4.mp3","calm\\5.mp3","calm\\6.mp3","calm\\7.mp3","calm\\8.mp3","calm\\9.mp3","calm\\10.mp3"]

mixer.init()  # initializing the mixer
mixer.music.set_volume(0.7)

def stop_music():
    mixer.music.stop()

def show_details(play_song):
    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print ("Total Length" + ' - ' + timeformat)

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()

def start_count(t):
    # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
    # Continue - Ignores all of the statements below it. We check if music is paused or not.
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if 0:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print ("Current Time" + ' - ' + timeformat)
            time.sleep(1)
            current_time += 1

def play_music(play_it):
    if 0:
        mixer.music.unpause()
    else:
        stop_music()
        time.sleep(1)
        mixer.music.load(play_it)
        mixer.music.play()
        show_details(play_it)
    

def playHappy():
 print ('Playing Happy Songs Playlist')
 k=random.choice(happy_playlist)
 play_music(k)

def playSad():
 print ('Playing Sad Songs Playlist')
 k=random.choice(sad_playlist)
 play_music(k)

def playAngry():
 print ('Playing Angry Songs Playlist')
 k=random.choice(angry_playlist)
 play_music(k)

def playSurprised():
 print ('Playing Surprised Songs Playlist')
 k=random.choice(surprised_playlist)
 play_music(k)

def playDisgusted():
 print ('Playing Disgusted Songs Playlist')
 k=random.choice(disgusted_playlist)
 play_music(k)

def playFear():
 print ('Playing Fear Songs Playlist')
 k=random.choice(fear_playlist)
 play_music(k)

def playConfused():
 print ('Playing Confused Songs Playlist')
 k=random.choice(confused_playlist)
 play_music(k)

def playCalm():
 print ('Playing Calm Songs Playlist')
 k=random.choice(calm_playlist)
 play_music(k)

#playHappy()

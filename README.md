# Countenance-based-boom-box
  With the world moving towards fields like Artificial Intelligence(AI) and Machine Learning(ML), our aim is to provide the users a platform through which on their current expression, music is played using Facial Expression Recognition.   

            -------------------------------------------------------------------------------------------------------

PACKAGES TO BE INSTALLED :

1. Ananconda Prompt --> https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe
2. Opencv --> pip install opencv-python
3. Boto3 library ---> pip install boto3
4. mutagen --> pip install mutagen
5. Pygame --> pip install pygame

            -------------------------------------------------------------------------------------------------------
AMAZON REKOGNITION SERVICE :
            
1. Create AWS console account ---> Free trail 
2. Create user in IAM service ---> a. Users b.Add user c. Policies/Permissions -- i. AmazonRekognitionFullAccess ii. AmazonSNSFullAccess d. Security Credentials -- i. Access id ii.Secret Access Key (Save in a best place so that it is only one time generate key) save in excel sheet. 
3. Add Access id and Secret Access Key in emotiondetection.py program which is given in this repository.

            -------------------------------------------------------------------------------------------------------
        

  In today’s world, with ever increasing advancements in the field of multimedia and technology, various music players have been developed with features like fast forward, reverse, variable playback speed (seek and time compression), local playback, streaming playback with multicast streams. Although these features satisfy the  user’s basic requirements, yet the user has to face the task of manually browsing through the playlist of songs and select songs based on his current mood and behavior. Music plays a very important role in enhancing an individual’s life as it is an important medium of entertainment for music lovers and listeners and sometimes even imparts a therapeutic approach. 
 
  Music has been proven to be an integral part of everyone’s life. It acts as a source for entertainment and also used for various medical needs as it is proven to be a Stress Reliever. There are numerous high-end music players available with the latest features of handling the volume, modulation, pitch, sound, genre, etc. Though these features are very useful for the users but sometimes it becomes quite irritating and time-consuming to manually browse through the playlist for the intended song which user wants to play based on his/her mood and emotional state. For the purpose of providing the users with the best possible and effortless pleasure of music, Facial Expression Recognition (FER) based systems have been adopted as they provide more fast, accurate and efficient results with less effort. With the world moving towards fields like Artificial Intelligence(AI) and Machine Learning(ML), our aim is to provide the users a platform through which on their current mood, music is played using Facial Expression Recognition. 
 
  Facial expressions give important clues about emotions. Computer systems based on affective interaction could play an important role in the next generation of computer vision systems. Face emotion can be used in areas of security, entertainment. A human can express his/her emotion through lip and eye. The work describes the development of Countenance Based Boom Box, which is an application meant for users to minimize the efforts in managing large playlists. Generally people have a large number of songs in their database or playlists. Thus to avoid trouble of selecting a song, most people will just randomly select a song from their playlist and some of the songs may not be appropriate for the current mood of the user and it may disappoint the user. Countenance Based Boom Box is interactive, sophisticated and innovative web based application to be used as a music player in a different manner. 
 
  The application works in a different manner from the traditional software as it scans and classifies the audio files present on the device and according to the predefined parameters (Audio Features) present on the application in order to produce a set of mood based playlists. The real time graphical input provided to the application is classified (Facial expression recognition) to produce a mood which will then be used to select the required playlist from the earlier set. The main objective of the paper is to design and generate a playlist based on current emotional state and behavior of the user. Face detection and facial feature extraction from image is the first step in emotion based music player. For the face detection to work effectively, user needs to provide an input image which should not be blur and tilted. 
 
  The main objective of this work is to develop an intelligent system that can easily recognize the facial expression and accordingly play a music track based on that particular expression/emotion recognized. The seven universally classified emotions are Happy, Sad, Anger, Disgust, Fear, Surprise and Neutral. 
 
 

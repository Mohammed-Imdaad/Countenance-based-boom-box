import boto3
import json
from song import *
j=[]
k=[]
access_id="AKIARN6RJQ2T2T3TT2PQ"
access_key="gSXkqjSjXfwn9BO9jNFh4wbHAFl6LIQQeOeheV3T"
region="us-west-1"


def detect_faces(photo):
    client=boto3.client('rekognition',
                        region_name=region,
                        aws_access_key_id=access_id,
                        aws_secret_access_key=access_key)

    imagee=open(photo,'rb')
    response = client.detect_faces(Image={'Bytes':imagee.read()},Attributes=['ALL'])
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        for i in faceDetail['Emotions']:
            print(i["Type"],i["Confidence"])
            j.append(i["Confidence"])
            k.append(i["Type"])        
    n=j.index(max(j))
    print("Emotion Found with confidence",k[n],j[n])
    if(k[n]=="HAPPY"):
        print("Happy")
        playHappy()
    elif(k[n]=="SAD"):
        print("Sad")
        playSad()
    elif(k[n]=="ANGRY"):
        print("Angry")
        playAngry()
    elif(k[n]=="SURPRISED"):
        print("Surprised")
        playSurprised()
    elif(k[n]=="DISGUSTED"):
        print("Disgusted")
        playDisgusted()
    elif(k[n]=="FEAR"):
        print("Fear")
        playFear()
    elif(k[n]=="CONFUSED"):
        print("Confused")
        playConfused()
    elif(k[n]=="CALM"):
        print("Calm")
        playCalm()
   
    j.clear()
    k.clear()
    imagee.close()
    return len(response['FaceDetails'])

def main():
    photo='feed.jpg'
    detect_faces(photo)
    

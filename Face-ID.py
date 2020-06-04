from playsound import playsound
import sys
import os
import pickle #To save and retrieve weights
sys.path.insert(0, '/Users/xenox/Documents/Coaaadinggg/Gesture_Detector/')
from Face_Recogniser import Face_Detector
import cv2
import pyautogui

face = Face_Detector()
font = cv2.FONT_HERSHEY_PLAIN
rec = cv2.face.LBPHFaceRecognizer_create() #rec for trec or recognizer
rec.read('/Users/xenox/Documents/Coaaadinggg/Face-ID/trained.yml')


vid = cv2.VideoCapture(0)

while (vid.isOpened()):
    _,frame = vid.read()
    frame = cv2.flip(frame,1)
    img,roi,x,y = face.detect(frame)

    with open('/Users/xenox/Documents/Coaaadinggg/Face-ID/label.pickle','rb') as f:
        labels = {a:b for b,a in pickle.load(f).items()}
    if roi != "No Face Detected":
        idd,conf = rec.predict(roi)
        
        if conf >= 0.8: 
            if labels[idd] == "shubh":    
                pyautogui.click()             
                pyautogui.write('Microsoft_Sucks')   
                pyautogui.press('enter')
                os.system("test")
                os.system("say welcome shubh")  
                break
            else:
                os.system("test")
                os.system("say eat shit") 
        else:
            os.system("test")
            os.system("say eat shit")             
            #cv2.putText(img,labels[idd],(x,y + 20),font,1,(0,255,0),2)  

    #cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
playsound('/Users/xenox/Downloads/napalm_death.mp3') 
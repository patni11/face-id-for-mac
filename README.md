#Video
https://www.youtube.com/watch?v=zMbGYoQXbMU

# face-id-for-mac
To use it properly you will need:-
Python 3 successfully installed 
PIL
opencv
pickle
numpy
pyautogui
playsound #if you want to play music at the end
and Sleep watcher 

After installing all of these. Go to sleep watcher folder and follow their readme.md.
after doing that go to hello.sh file in the folder and put the path to Face-ID.py file

DO NOT RUN THE PROGRAM NOW!
In the main folder i.e folder of this project create another folder called 'Images' -> exactly as spelled without ''

Now go to terminal and run collecting_images.py file,
it will ask you to type your name,
then it will create a folder inside Images with your name and the program will take your images and store it there.

Now run creating_files.py file, this will create label.pickle and trained.yml file.

If all the steps are done successfully then, go to Face-ID.py file and paste the full path of yout trained.yml and lable.pickle file, where-ever required. now replace 'shubh' with your name as writen by you earlier. Change the password to your own password on MAC.

Now it should work fine. 
open terminal and run the following command :- 
/usr/local/sbin/sleepwatcher --verbose --wakeup /Users/xenox/Desktop/Shell/hello.sh  (put the full path of your hello.sh file)

Done!!!

if you are having any error or issues :- DM me on insta - shubh_p_11
NOTE:- This is not the most secure way to login, anyone with your image can open your mac, I created this because I could not find anything like it on net.


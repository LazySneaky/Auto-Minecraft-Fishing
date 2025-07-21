import sounddevice as sd, numpy as np , pyautogui, time

fishing = False



def cast_rod():
     global fishing
     pyautogui.click(button='right') #cast the rod
     time.sleep(0.2)
     fishing = True
     print("Casted rod")
     


def callback(indata, *_):
     global fishing 
     volume = np.linalg.norm(indata)
     
     if volume>0.7 and fishing: #only responds when rod is in water
          print("Reeling in the fish!")
          pyautogui.click(button='right')
          print("waiting for next fish")    
          fishing = False
          time.sleep(2)
          cast_rod()

cast_rod()


with sd.InputStream(callback=callback, channels=1, samplerate=44100) as stream:
     print("Listening to splash...")
     while True:
        time.sleep(0.1)
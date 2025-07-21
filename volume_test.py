import sounddevice as sd
import numpy as np
import time

duration = 0.3

print("gettin the audio vro")

def get_vol_lvl(indata):
    volume = np.linalg.norm(indata)
    return volume 

with sd.InputStream(channels=1, samplerate=44100) as stream:
    while True:
        audio_data,_ = stream.read(int(44100*duration))
        vol = get_vol_lvl(audio_data)
        print(f"Volume: {vol:.3f}")
        time.sleep(0.1)

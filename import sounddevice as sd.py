import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(duration, filename):
    print("Recording audio...")
    sample_rate = 44100
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()
    write(filename, sample_rate, recording)
    print(f"Audio recording saved as {filename}")
record_audio(5, "my_recording.wav")

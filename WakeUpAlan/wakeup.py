import datetime
import pyaudio
import wave
import time

chunk = 1024
f = wave.open(r"explosion.wav", "rb")
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)

data = f.readframes(chunk)

while True:
    if datetime.datetime.now().time() == '06:31:30:000000':
        stream.write(data)
        data = f.readframes(chunk)
        time.sleep(5)
        stream.stop_stream()
        stream.close()
        p.terminate()
    time.sleep(82800)
    continue

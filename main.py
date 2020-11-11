import pyaudio
import time
import wave

CHUNK=1024*2
RATE=44100
p=pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RECORD_SECONDS = 5       # 5秒録音

stream=p.open(	format = FORMAT,
		channels = CHANNELS,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)

frames = []
while True:
    print(len(frames))
    if frames == []:
        # 録音処理
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* Farst Recording Done.")
        print("* Audio Play Start...")
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        stream.write(frames.pop(0))
        data = stream.read(CHUNK)
        frames.append(data)
	
stream.stop_stream()
stream.close()
p.terminate()

print("Stop Streaming")
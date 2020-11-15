import pyaudio
import time
import wave

#Audio Setting
CHUNK=1024*2
RATE=44100
p=pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RECORD_SECONDS = None # 5秒録音

while RECORD_SECONDS == None:
    print("声を遅らせる秒数(遅延時間)を入力してください (半角数字) :")
    input_data = input()

    try:
        int(input_data)
        RECORD_SECONDS = float(input_data)
        print("遅延時間: ", RECORD_SECONDS, "秒に設定されました")
    except ValueError:
        print("遅延時間は、半角数字2桁で設定してください。")

stream=p.open(	format = FORMAT,
		channels = CHANNELS,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)

frames = []
while True:
    if frames == []:
        # 録音処理
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* Farst Recording Done.")
        print("* Streaming...")
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        stream.write(frames.pop(0))
        data = stream.read(CHUNK)
        frames.append(data)
	
stream.stop_stream()
stream.close()
p.terminate()

print("Streaming End.")
import time
import wave
from audiostream import get_input

frames = []

'''
def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)

# get the default audio input (mic on most cases)


mic = get_input(callback=mic_callback)
mic.start()

time.sleep(5)

mic.stop()

wf = wave.open("test.wav", 'wb')
wf.setnchannels(mic.channels)
wf.setsampwidth(2)
wf.setframerate(mic.rate)
wf.writeframes(b''.join(frames))
wf.close()

'''


def mic_callback(buf):
    print('got', len(buf))
    frames.append(buf)
    print('size of frames: ' + len(frames))

def bcallback(instance):
    mic = get_input(callback=mic_callback, source='mic')
    mic.start()
    #mic.poll()
    time.sleep(5)
    mic.stop()

class MyApp(App):
    def build(self):
        btn1 = Button(text='Audio Record')
        btn1.bind(on_press=bcallback)
        return btn1

#if name == 'main':
if __name__=='__main__':
    MyApp().run()

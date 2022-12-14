import pyttsx3
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Companion:

    def announce(self, stringvar):
        print(stringvar)
        self.voice_engine.say(stringvar)
        self.voice_engine.runAndWait()
        return
    def chat(self):

        print("Beginning chat protocol, enter text to chat with AI...")
        self.chat_flag = True
        while self.go_flag == True:

            self.sequence = input()
            if self.sequence == "":
                self.go_flag == False
            else:
                self.inputs = self.tokenizer.encode(self.sequence, return_tensors='pt')
                self.outputs = self.model.generate(self.inputs, max_length=200, do_sample=True)
                self.text = self.tokenizer.decode(self.outputs[0], skip_special_tokens=True)
                print(self.text)

    def voice_chat(self):
        print("Beginning chat protocol, enter text to chat with AI...")
        self.chat_flag = True
        while self.go_flag == True:

            self.sequence = input()
            if self.sequence == "":
                self.go_flag == False
            else:
                self.inputs = self.tokenizer.encode(self.sequence, return_tensors='pt')
                self.outputs = self.model.generate(self.inputs, max_length=200, do_sample=True)
                self.text = self.tokenizer.decode(self.outputs[0], skip_special_tokens=True)
                self.announce(self.text)

    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.go_flag = True
        self.sequence = ""
        self.chat_flag = False
        self.inputs = None
        self.outputs = None
        self.text = None

        # TTS Engine Initialization
        self.voice_engine = pyttsx3.init()
        self.voices = self.voice_engine.getProperty("voices")
        self.voice_engine.setProperty('rate', 175)
        self.voice_engine.setProperty('voice', self.voices[1].id)

        # Voice Recognition Initialization
        self.recog_model = vosk.Model("vosk-model-small-en-us-0.15")
        self.voice_recog = vosk.KaldiRecognizer(self.recog_model, 16000)
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=81)
        self.stream.start_stream()

        # Tests/ Strings
        self.voice_engine.runAndWait()


def main():
    artemis = Companion()
    artemis.chat()

if __name__ == "__main__":
    main()
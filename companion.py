import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Companion:
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

    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.go_flag = True
        self.sequence = ""
        self.chat_flag = False
        self.inputs = None
        self.outputs = None
        self.text = None


def main():
    artemis = Companion()
    artemis.chat()

if __name__ == "__main__":
    main()
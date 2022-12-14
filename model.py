# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import AdonisAI

def pprint(feature_command):
    return feature_command + 'Executed'

athena = AdonisEngine(bot_name = 'alexa',
input_mechanism = [InputOutput.text_output, InputOutput.text_to_speech],
backend_tts_api = 'pyttsx3',
wake_word_detection_status = True,
wake_word_detection_mechanism = InputOutput.speech_to_text_deepspeach_streaming,
shutdown_command = 'shutdown',
secret_key = 'your_secret_key')

print(athena.check_registered_command())

athena.engine_start()
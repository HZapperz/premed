import pyttsx4
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import os
import sys

engine = pyttsx4.init('coqui_ai_tts')
engine.setProperty('speaker_wav', './docs/i_have_a_dream_10s.wav')

engine.say('this is an english text to voice test, listen it carefully and tell who i am.')
engine.runAndWait()
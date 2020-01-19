from pydub import AudioSegment
from pydub.playback import play
from time import sleep
from glob import glob
import random

honks = [AudioSegment.from_mp3(name) for name in glob("honks/*.mp3")]
sound = AudioSegment.from_mp3('honks/Honk1.mp3')
while True:
    choice = random.choice(honks)
    play(choice)
    sleep(choice.duration_seconds + .5)

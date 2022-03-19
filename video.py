import cv2
import sys
from PIL import Image
import os
import moviepy.editor as mpe
import pyttsx3
import time

avg_w = 0
avg_h = 0

for i in range(int(sys.argv[1])):
    os.system("python3 main.py")
    im = Image.open("out.png")
    width, height = im.size
    avg_w += width
    avg_h += height

    im.save(f"memes/{i}.png")

avg_w = int(avg_w / int(sys.argv[1]))
avg_h = int(avg_h / int(sys.argv[1]))
count = 0

for file in os.listdir("memes"):
    im = Image.open(f"memes/{file}")
    width, height = im.size
    imr = im.resize((avg_w, avg_h), Image.ANTIALIAS)
    imr.save(f"video/{count}.png")
    count += 1

count = 0
engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.say('hello world')
# engine.runAndWait()
# engine.stop()

clips = list()
for i in range(len(os.listdir("video"))):
    out = cv2.VideoWriter(f"videos/{i}.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.2, (avg_w, avg_h))
    out.write(cv2.imread(f"video/{i}.png"))
    out.release()

    clip = mpe.VideoFileClip(f"videos/{i}.avi")
    # engine.save_to_file("hello world", "tts.mp3")
    # engine.runAndWait()
    # time.sleep(1)
    # audio = mpe.AudioFileClip("tts.mp3")

    # fclip = clip.set_audio(audio)
    clips.append(clip)

    print(f"Clip {i}")

    # out = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.2, (avg_w, avg_h))
    
    # for file in os.listdir("video"):
    #     out.write(cv2.imread(f"video/{file}"))

    # out.release()

final = mpe.concatenate_videoclips(clips, method="compose")
audio = mpe.AudioFileClip("music.mp3")
audio = audio.set_duration(final.duration)
final_audio = mpe.CompositeAudioClip([audio])
final = final.set_audio(final_audio)

final.write_videofile("out.mp4")

# clip = mpe.VideoFileClip("out.avi")
# audio = mpe.AudioFileClip("music.mp3")
# audio = audio.set_duration(clip.duration)
# final_audio = mpe.CompositeAudioClip([audio])
# final_clip = clip.set_audio(final_audio)
# final_clip.write_videofile("out.mp4")


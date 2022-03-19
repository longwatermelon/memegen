import cv2
import sys
from PIL import Image
import os
import moviepy.editor as mpe

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

for v in os.listdir("video"):
    out = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.2, (avg_w, avg_h))
    
    for file in os.listdir("video"):
        out.write(cv2.imread(f"video/{file}"))

    out.release()


clip = mpe.VideoFileClip("out.avi")
audio = mpe.AudioFileClip("music.mp3")
audio = audio.set_duration(clip.duration)
final_audio = mpe.CompositeAudioClip([audio])
final_clip = clip.set_audio(final_audio)
final_clip.write_videofile("out.mp4")

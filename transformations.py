import sys
import numpy as np
import tkinter as tk

from PIL import Image
from colorama import Cursor
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def resize(video):
    maxWidth = 450
    width, height = video.size
    width_offset = 3 
    newHight = height / width_offset * maxWidth / width
    if(width > maxWidth or height > newHight):
        video = video.resize((maxWidth, int(newHight)))
    return video

def ToGrayscale(image:Image):
    ASCIIstring = "  ,-':<>;+!*/?%&98#"
    lenA = len(ASCIIstring)
    width, height = image.size
    for y in range(height):
        string = ''
        for x in range(width):
           pixel_color = image.getpixel((x, y))
           avg = int((pixel_color[0] + pixel_color[1] + pixel_color[2]) / 3)
           string = string + ASCIIstring[int(avg / 255 * (lenA-1))]
        sys.stdout.write(string + '\n')
        sys.stdout.flush()
    
def ToClip(video:str):
    clip = VideoFileClip(video)
    clip = resize(clip)
    p = 0
    for frame in enumerate(clip.iter_frames(fps=clip.fps, dtype='uint8')):
        with Image.fromarray(np.array(frame[1])) as im:
            ToGrayscale(im)
            sys.stdout.write(Cursor.POS(0, 0))
             
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("video files", "*.mp4")])
    root.destroy()
    return file_path     
         
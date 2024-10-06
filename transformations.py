import sys
import numpy as np
import tkinter as tk

from colorama import Cursor
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def resize(video:VideoFileClip):
    maxWidth = 300
    width, height = video.size
    width_offset = 3 
    newHight = height / width_offset * maxWidth / width
    if(width > maxWidth or height > newHight):
        video = video.resize((maxWidth, int(newHight)))
    return video

def ToGrayscale(frame:np.array):
    ASCIIstring = "  ,-':<>;+!*/?%&98#"
    lenA = len(ASCIIstring)
    avgim = np.mean(frame, axis=2)
    width, height = avgim.shape

    for y in range(width):
        for x in range(height):
           sys.stdout.write(ASCIIstring[int(avgim[y][x] / 255 * (lenA-1))])
        sys.stdout.write('\n')
        sys.stdout.flush()
    
def ToClip(video:str):
    clip = VideoFileClip(video)
    clip = resize(clip)
    for frame in enumerate(clip.iter_frames(fps=clip.fps, dtype='uint8')):
        ToGrayscale(frame[1])
        sys.stdout.write(Cursor.POS(0, 0))
             
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("video files", "*.mp4")])
    root.destroy()
    return file_path     
         
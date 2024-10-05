import os
import sys

import tkinter as tk

from PIL import Image
from imageio import imwrite
from tkinter import filedialog
from moviepy.editor import VideoFileClip


def resize(image:Image):
    maxWidth = 300
    width, height = image.size
    width_offset = 3 
    newHight = height / width_offset * maxWidth / width
    if(width > maxWidth or height > newHight):
        image = image.resize((maxWidth, int(newHight)))
    return image

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
    output_folder = 'extracted_frames'
    os.makedirs(output_folder,  exist_ok=True)
    clip = VideoFileClip(video)

    for i, frame in enumerate(clip.iter_frames(fps=clip.fps, dtype='uint8')):
        frame_filename = os.path.join(output_folder, f'{i}.jpg')
        imwrite(frame_filename, frame)

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("video files", "*.mp4")])
    root.destroy()
    return file_path     
         
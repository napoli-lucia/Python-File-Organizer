#Organize files by extension

import os
import shutil

extensions = { 
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".doc": "documents",
        ".docx": "documents",
        ".pdf": "pdfs",
        ".txt": "notes",
        ".xls": "excel",
        ".xlsx": "excel",
        ".csv": "excel",
        ".ppsx": "ppts",
        ".pptx": "ppts",
        ".zip": "compressed",
        ".rar": "compressed",
        ".mp4": "video",
        ".mkv": "video",
        ".avi": "video",
        ".mov": "video",
        ".mp3": "audio",
        ".ogg": "audio",
        ".wav": "audio",
        ".exe": "installer"
}

os.chdir("/Users/lucia/Downloads")

for file in os.listdir():
    ext = os.path.splitext(file)[1]
    
    if ext in extensions:
        
        folder = str(extensions[ext])
        
        #new folder
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        
        #move file
        dst = "/Users/lucia/Downloads/{}".format(folder)        
        shutil.move(file, dst)
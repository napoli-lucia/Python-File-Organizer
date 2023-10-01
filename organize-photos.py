#Organize photos by date

import os
import datetime
import shutil
from PIL import Image

file_path = '/Users/lucia/Pictures'
os.chdir(file_path)


def move(file,date):
    #new folder
    if not os.path.exists(date):
        os.mkdir(date)

    #move file
    shutil.move(file, date)


#Modification date
def move_files_m_dt():
    for file in os.listdir(file_path):
        m_time = os.path.getmtime(file)
        m_dt = datetime.date.fromtimestamp(m_time)
        date = str(m_dt)

        move(file, date)


#Taken date
def move_files_t_dt():
    for file in os.listdir(file_path):
        ext = os.path.splitext(file)[1]
        extensions = (".jpg",".jpeg",".png")
        if ext not in extensions:
            continue

        exif = Image.open(file)._getexif()
        if not exif:
            raise Exception('Image {0} does not have EXIF data.'.format(file))
        creation_time = exif[36867]
        splitted = creation_time.split()
        date = splitted[0].replace(":","-")

        move(file, date)


move_files_m_dt()
move_files_t_dt()
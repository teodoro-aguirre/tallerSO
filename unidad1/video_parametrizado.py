import threading, time
from tkinter import *
from tkinter import filedialog

import cv2

def video(nombre, segundos):
    time.sleep(segundos)
    
    video = cv2.VideoCapture('video.mp4')
    while(video.isOpened()):
        res, frame = video.read()

        if(res == True):
            cv2.imshow(nombre, frame)

            if(cv2.waitKey(24) == ord('s')):
                break
        else:
            break

    video.release()
    cv2.destroyWindow(nombre)

root = tkinter.Tk()
root.withdraw()

ilename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona un archivo", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 


hiloVideo = threading.Thread(target=video, args=('Video', 0))

hiloVideo.start()

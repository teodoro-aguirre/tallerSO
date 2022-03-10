import threading, time
import cv2

VENTANA_VIDEO = 'Video'
VENTANA_CAMARA = 'WebCam'

def video_camara(nombre, segundos):
    global VENTANA_CAMARA
    time.sleep(segundos)
    capture = cv2.VideoCapture(0)
    while(capture.isOpened()):
        res, frame = capture.read()
        
        cv2.imshow(VENTANA_CAMARA, frame)

        if(cv2.waitKey(1) == ord('s')):
            break

    capture.release()
    cv2.destroyWindow(VENTANA_CAMARA)

def video(nombre, segundos):
    global VENTANA_VIDEO
    time.sleep(segundos)
    
    video = cv2.VideoCapture('video.mp4')
    while(video.isOpened()):
        res, frame = video.read()

        if res:
            cv2.imshow(VENTANA_VIDEO, frame)

            if(cv2.waitKey(24) == ord('s')):
                break
        else:
            break

    video.release()
    cv2.destroyWindow(VENTANA_VIDEO)


hiloVideoCamara = threading.Thread(target = video_camara, args = (' da ', 5))
hiloVideo = threading.Thread(target=video, args=('name', 20))


hiloVideoCamara.start()
hiloVideo.start()




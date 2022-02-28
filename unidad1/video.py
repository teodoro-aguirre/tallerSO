# -*- coding: cp1252 -*-
import cv2 # Importo la librería openCV

video = cv2.VideoCapture('video.mp4')	# El nombre del video o la ruta del video si es necesario

while (video.isOpened()):		# video.isOpened() devuelve True si se pudo acceder al video
	
	res, frame = video.read()	# leo el siguiente frame del video y lo deposito en frame
								# res, tendrá un True en caso de que la lectura haya sido exitosa
	
	if (res == True):
		cv2.imshow('Mi video', frame)	# cv2.imshow() despliega una imagen en una ventana
										# la ventana automáticamente se ajusta al tamaño de la imagen
										# El primer parámetro es un título para la ventana
										# El segundo es la imagen a ser desplegada
										# El método no devuelve valor alguno

		if (cv2.waitKey(24) == ord('s')):	# Se muestra la ventana hasta que la tecla presionada sea una 's'
			break
	else:
		break
 	
video.release() # libero recursos
cv2.destroyAllWindows() # Cierro cualquier ventana cv2
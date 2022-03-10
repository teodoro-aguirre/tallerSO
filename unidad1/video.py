# Importo la libreria openCV
import cv2

# El nombre del video o la ruta del video si es necesario
video = cv2.VideoCapture('video.mp4')

# video.isOpened() devuelve True si se pudo acceder al video
while video.isOpened():
	# leo el siguiente frame del video y lo deposito en frame
	res, frame = video.read()
	# res, tendr� un True en caso de que la lectura haya sido exitosa
	
	if res:
		# cv2.imshow() despliega una imagen en una ventana
		cv2.imshow('Mi video', frame)
		# la ventana automaticamente se ajusta al tama�o de la imagen
		# El primer par�metro es un t�tulo para la ventana
		# El segundo es la imagen a ser desplegada
		# El m�todo no devuelve valor alguno

		# Se muestra la ventana hasta que la tecla presionada sea una 's'
		if cv2.waitKey(24) == ord('s'):
			break
	else:
		break

# libero recursos
video.release()
# Cierro cualquier ventana cv2
cv2.destroyAllWindows()
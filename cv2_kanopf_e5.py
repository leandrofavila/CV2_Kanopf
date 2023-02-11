'''
5. Gere um código que abra a sua câmera do
computador( caso não tenha, instale o aplicativo
droidcam no celular e no computador, ele vai ser
reconhecido como uma câmera pelo windows), salve
uma imagem do seu rosto e depois coloque um
círculo com um raio que você pode definir qualquer
um e com o centro exatamente no seu nariz,(para
localizar as coordenadas do seu nariz na imagem,
você pode abrir a mesma imagem no paint e ir com o
mouse em cima do seu nariz, e você consegue
pegar as coordenadas desse ponto
'''
import cv2

image = cv2.imread('kbca_pic1.png')

radius = int(input('Insira o raio do circulo! '))

cv2.circle(image, (490, 190), radius, (255, 0, 0))

cv2.imshow('image', image)
cv2.waitKey(0)

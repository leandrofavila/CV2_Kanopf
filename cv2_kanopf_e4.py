'''
4. crie com código que tenha 2 input, o primeiro com as
coordenadas para fazer um recorte na imagem e o
segundo com uma nova largura menor do que a
imagem recortada para dar um resize, para fazer
resize apenas com a largura revise o código que tem
o fator de proporcionalidade.
'''
import cv2

image = cv2.imread('SerraAngel.png')

cv2.imshow('original_image', image)
dim = image.shape

a, b, c, d = [int(x) for x in input('4 valores de entre {}X{} '.format(dim[0], dim[1])).split()]
crop = image[a:b, c:d]
cv2.imshow("croped_image", crop)

n_width = int(input('Valor menor ou igual a {} '.format(b-a)))
width = image.shape[1]
height = image.shape[0]
prop = float(height/width)
n_height = int(n_width*prop)
n_dim = (n_width, n_height)
n_image = cv2.resize(crop, n_dim, interpolation=cv2.INTER_AREA)
cv2.imshow('croped_image_resized', n_image)

cv2.waitKey(0)

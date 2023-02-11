'''
2. Escreva um código que abra uma imagem e insira nela um
texto que o programa solicita como input, este texto deve
conter as informações de qual a dimensão da imagem,
depois disso insira um quadrado envolta do texto.
'''
import cv2

w, h = [int(x) for x in input('Insira largura e altura! ').split()]

image = cv2.imread('SerraAngel.png')

image = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)

text = 'size = {}X{}'.format(w, h)
pos_text = (w-(w-10), h-(h-40))
put_text = cv2.putText(image, text, pos_text, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

text_width = size[0][0]
text_height = size[0][1]
line_height = text_height + size[1] + 5

x = image.shape[1] - 5 - text_width
y = 5 + size[0][1] + 2 * line_height

cv2.rectangle(image, (w-(w-5), h-(h-5)), (text_width+15, (text_height*2)+5), (255, 0, 0), 2)

cv2.imshow('img', image)
cv2.waitKey(0)

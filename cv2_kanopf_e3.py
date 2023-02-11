'''
3. Crie um código que tenha uma lista contendo os
raios de um círculo, após isso faça com que o
opencv coloque círculos com esses raios definidos
na lista, a cada loop o programa deve avançar
apenas ao clicar alguma tecla, utilizando cv2 waitkey
dentro do loop, também, você deve criar um input
dentro do loop que solicite a cor que você deseja
inserir esse círculo, lembrando que o opencv recebe
a cor no seguinte formato (0,0,255) por exemplo.
'''
import cv2

image = cv2.imread('SerraAngel.png')

#radius = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
for r in range(10, 1000, 10):
    color = [int(x) for x in input('3 valores de 0 a 255 ').split()]
    print(color)
    cv2.circle(image, (image.shape[1] // 2, image.shape[0] // 2), r, color)
    cv2.imshow('img', image)
    cv2.waitKey(0)

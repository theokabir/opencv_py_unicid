import numpy as np
import cv2 as cv
from enum import Enum


class REFLECTION_AXIS(Enum):
    DOWN = [[-1, 0], [0, 1]]
    LEFT = [[1, 0], [0, -1]]
    RIGHT = [[-1, 0], [0, -1]]


def rect(start: (int, int), end: (int, int)):
    new_square = np.array([
        start,
        (start[0], end[1]),
        end,
        (end[0], start[1])
    ])
    return polygon(new_square)


class polygon:
    def __init__(self, points: np.array):
        self.points = points

    def show(self, image: np.ndarray, color=(0, 255, 0), thickness=-1):
        cv.drawContours(image, [self.points], -1, color, thickness)

    def rotate(self, angle_degrees):
        # Converte o ângulo de graus para radianos
        angle_radians = np.radians(angle_degrees)

        # Calcula o centro de massa dos pontos
        center = np.mean(self.points, axis=0)
        c_x, c_y = center

        # Cria a matriz de rotação
        cos_angle = np.cos(angle_radians)
        sin_angle = np.sin(angle_radians)

        # Calcula as novas coordenadas dos pontos após a rotação
        rotated_points = []
        for px, py in self.points:
            # Desloca o ponto para o sistema de coordenadas do centro de massa
            dx, dy = px - c_x, py - c_y

            # Aplica a rotação
            new_x = c_x + cos_angle * dx - sin_angle * dy
            new_y = c_y + sin_angle * dx + cos_angle * dy

            # Adiciona o ponto rotacionado à lista
            rotated_points.append([new_x, new_y])

        # Converte a lista de pontos rotacionados em um array NumPy e converte para inteiros
        self.points = np.array(rotated_points).astype(int)

    def translate(self, x, y):
        # soma todos
        self.points = np.array(self.points).astype(int) + np.array([x, y])

    def scale(self, scale_factor):
        # calcula centro de massa
        c_x, c_y = np.mean(self.points, axis=0)
        self.points = np.array([
            # faz a multiplixação entre os eixos para a escala
            [
                p_x * scale_factor,
                p_y * scale_factor
            ]
            for p_x, p_y in self.points
        ]).astype(int)
        # calcula novo centro de massa
        m_x, m_y = np.mean(self.points, axis=0)
        # move a forma multiplicada para o centro de massa antigo
        self.translate(int(c_x - m_x), int(c_y - m_y))

    def reflextion(self, axis: REFLECTION_AXIS):
        nArr = np.array([
            np.max(point, axis.value)
            for point in self.points
        ])

        print(nArr)

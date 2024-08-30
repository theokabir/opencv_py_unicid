import numpy as np
import cv2 as cv
from enum import Enum
from uuid import uuid4


class REFLECTION_AXIS(Enum):
    DOWN = [[-1, 0], [0, 1]]
    LEFT = [[1, 0], [0, -1]]
    RIGHT = [[-1, 0], [0, -1]]


def square(size: int):
    new_square = np.array([
        (0, 0),
        (0, size),
        (size, size),
        (size, 0)
    ])
    return Polygon(new_square)


def triangle(size: int):
    height = size * np.sqrt(3) / 2
    new_triangle = np.array([
        (size/2, 0),
        (size, height),
        (0, height)
    ]).astype(int)
    return Polygon(new_triangle)


def arrow(size: int):
    half_size = size*.5
    size_1_4 = size*.25
    size_3_4 = size*.75
    new_arrow = np.array([
        (size_1_4, 0),
        (size_3_4, 0),
        (size_3_4, half_size),
        (size, half_size),
        (half_size, size),
        (0, half_size),
        (size_1_4, half_size)
    ]).astype(int)
    return Polygon(new_arrow)


def star(size: int):
    cx, cy = int(size/2), int(size/2)  # Calcula o centro da estrela

    # Calculate the radius for the outer and inner points of the star
    outer_radius = size / 2
    inner_radius = outer_radius * 0.382  # Calcula o raio dos pontos internos da estrela

    # Define Ângulo dos pontos
    angles = np.deg2rad([90, 162, 234, 306, 18])

    # calcula os pontos externos
    outer_points = np.array([
        (cx + np.cos(angle) * outer_radius, cy - np.sin(angle) * outer_radius)
        for angle in angles
    ], dtype=np.int32)

    #  calcula os pontos internos girando em 36 graus referente aos pontos externos
    inner_angles = angles + np.deg2rad(36)
    inner_points = np.array([
        (cx + np.cos(angle) * inner_radius, cy - np.sin(angle) * inner_radius)
        for angle in inner_angles
    ], dtype=np.int32)

    # preenche o vetor com os pontos calculados a cima de forma intercalada
    star_points = np.empty((10, 2), dtype=np.int32)
    star_points[0::2] = outer_points
    star_points[1::2] = inner_points

    return Polygon(star_points)


class Polygon:
    def __init__(self, points: np.array, color=(255, 255, 255), thickness=-1):
        self.points = points
        self.color = color
        self.thickness = thickness

    def show(self, image: np.ndarray):
        cv.drawContours(image, [self.points], -1, self.color, self.thickness)

    def rotate(self, angle_degrees):
        # Converte o ângulo de graus para radianos
        angle_radians = np.radians(angle_degrees)

        # Calcula o centro de massa dos pontos
        center = np.mean(self.points, axis=0)
        c_x, c_y = center.astype(int)

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

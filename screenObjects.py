from polygon import Polygon


class ScreenObjects(object):
    def __init__(self):
        self.polygons: list[Polygon] = []
        self.closed: bool = False

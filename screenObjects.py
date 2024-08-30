from polygon import Polygon


class ScreenObjects(object):
    def __init__(self):
        self.polygons: list[Polygon] = []
        self.closed: bool = False

    def getFormIndex(self, identifier: str) -> int:
        for i, obj in enumerate(self.polygons):
            if obj.id is identifier:
                return i
        return -1

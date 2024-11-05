import sys


class Position:
    def __init__(self, data):
        self.x = int(data[0])
        self.y = int(data[1])

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_overlapped_area(self, position) -> int:
        if not self.is_overlapped(position):
            return 0

        return ((min(self.get_x(), position.get_x()) + 10) - max(self.get_x(), position.get_x())) * (
                (min(self.get_y(), position.get_y()) + 10) - max(self.get_y(), position.get_y()))

    def is_overlapped(self, position) -> bool:
        return abs(self.get_x() - position.get_x()) < 10 and abs(self.get_y() - position.get_y() < 10)


count = int(sys.stdin.readline().strip())
positions = [Position(sys.stdin.readline().split()) for _ in range(count)]

area = 100 * count

for i in range(len(positions) - 1):
    for j in range(i+1, len(positions)):
        print(i, ': ',positions[i].get_x(), positions[i].get_y(), ' | ', j, ': ',positions[j].get_x(), positions[j].get_y())
        print(positions[i].get_overlapped_area(positions[j]))
        area -= positions[i].get_overlapped_area(positions[j])

print(area)
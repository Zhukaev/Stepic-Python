class Points:
    def __init__(self, k):
        self.size = k;
        self.points =  []
    def add(self, *coords):
        # добавить точку
        self.points.append([])
        for coord in coords:
            self.points[len(self.points) - 1].append(coord)
        self.points[len(self.points) - 1] = tuple(self.points[len(self.points) - 1])
        #print(self.points)
    def remove(self, *coords):
        # удалить точку
        coord = []
        for c in coords:
            coord.append(c)
        i = self.filter(coord)
        if i != 0:
            self.points.remove(i)
        #print(self.points)
    def range_query(self, *coord_ranges):
        # запросить точки
        coord = []
        for c in coord_ranges:
            coord.append(c)
        for point in self.points:
            for i in range(len(self.points[0])):
                #print(point[i], coord[i], point[i] > coord[i][0], point[i] < coord[i][1])
                if not (point[i] >= coord[i][0] and point[i] <= coord[i][1]):
                    break
            else:
                yield point

    def filter(self, coord):
        for point in self.points:
            for i in range(len(self.points[0])):
                #print(point[i], coord[i], point[i] == coord[i])
                if point[i] != coord[i]:
                    break
            else:
                return point
        return 0
import math
class Shape:
    def __init__(self, shape_id):
        self.shape_id = shape_id

    def move(self, dx, dy):
        raise NotImplementedError("Метод move должен быть реализован в подклассе")

    def compare(self, other):
        if not isinstance(other, Shape):
            return "Сравнение возможно только с геометрическими фигурами"
        return self.area() - other.area()

    def area(self):
        raise NotImplementedError("Метод area должен быть реализован в подклассе")

    def __str__(self):
        return f"{self.__class__.__name__} '{self.shape_id}'"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def __str__(self):
        return f"({self.x}, {self.y})"


class Triangle(Shape):
    def __init__(self, shape_id, point1, point2, point3):
        super().__init__(shape_id)
        self.vertices = [point1, point2, point3]

    def move(self, dx, dy):
        for vertex in self.vertices:
            vertex.move(dx, dy)
        print(f"Треугольник '{self.shape_id}' перемещен на ({dx}, {dy})")

    def area(self):
        a = self.vertices[0].distance_to(self.vertices[1])
        b = self.vertices[1].distance_to(self.vertices[2])
        c = self.vertices[2].distance_to(self.vertices[0])

        # Формула Герона
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def perimeter(self):
        a = self.vertices[0].distance_to(self.vertices[1])
        b = self.vertices[1].distance_to(self.vertices[2])
        c = self.vertices[2].distance_to(self.vertices[0])
        return a + b + c

    def __str__(self):
        vertices_str = ", ".join(str(v) for v in self.vertices)
        return f"{super().__str__()} с вершинами [{vertices_str}], площадь: {self.area():.2f}"


class Tetragon(Shape):
    def __init__(self, shape_id, point1, point2, point3, point4):
        super().__init__(shape_id)
        self.vertices = [point1, point2, point3, point4]

    def move(self, dx, dy):
        for vertex in self.vertices:
            vertex.move(dx, dy)
        print(f"Четырехугольник '{self.shape_id}' перемещен на ({dx}, {dy})")

    def area(self):
        p1, p2, p3, p4 = self.vertices

        a1 = p1.distance_to(p2)
        b1 = p2.distance_to(p3)
        c1 = p3.distance_to(p1)
        s1 = (a1 + b1 + c1) / 2
        area1 = math.sqrt(s1 * (s1 - a1) * (s1 - b1) * (s1 - c1))

        a2 = p1.distance_to(p3)
        b2 = p3.distance_to(p4)
        c2 = p4.distance_to(p1)
        s2 = (a2 + b2 + c2) / 2
        area2 = math.sqrt(s2 * (s2 - a2) * (s2 - b2) * (s2 - c2))

        return area1 + area2

    def perimeter(self):
        perimeter = 0
        for i in range(4):
            perimeter += self.vertices[i].distance_to(self.vertices[(i + 1) % 4])
        return perimeter

    def __str__(self):
        vertices_str = ", ".join(str(v) for v in self.vertices)
        return f"{super().__str__()} с вершинами [{vertices_str}], площадь: {self.area():.2f}"


def main():
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)

    p4 = Point(1, 1)
    p5 = Point(5, 1)
    p6 = Point(3, 4)

    p7 = Point(0, 0)
    p8 = Point(4, 0)
    p9 = Point(4, 3)
    p10 = Point(0, 3)

    p11 = Point(1, 1)
    p12 = Point(5, 1)
    p13 = Point(4, 4)
    p14 = Point(0, 4)

    triangle1 = Triangle("Треугольник-1", p1, p2, p3)
    triangle2 = Triangle("Треугольник-2", p4, p5, p6)

    tetragon1 = Tetragon("Прямоугольник", p7, p8, p9, p10)
    tetragon2 = Tetragon("Четырехугольник-2", p11, p12, p13, p14)

    shapes = [triangle1, triangle2, tetragon1, tetragon2]

    for shape in shapes:
        print(f"  - {shape}")
    print()

    print("метод move:")
    triangle1.move(2, 1)
    tetragon1.move(-1, 2)
    print()

    print("фигуры после перемещения:")
    for shape in shapes:
        print(f"  - {shape}")
    print()

    print("сравнение фигур по площади:")
    comparisons = [
        (triangle1, triangle2, "Треугольник-1, Треугольник-2"),
        (tetragon1, tetragon2, "Прямоугольник, Четырехугольник-2"),
        (triangle1, tetragon1, "Треугольник-1, Прямоугольник"),
        (triangle2, tetragon2, "Треугольник-2, Четырехугольник-2")
    ]

    for shape1, shape2, description in comparisons:
        difference = shape1.compare(shape2)
        if difference > 0:
            result = f"площадь больше на {difference:.2f}"
        elif difference < 0:
            result = f"площадь меньше на {abs(difference):.2f}"
        else:
            result = "площади равны"
        print(f"  {description}: {result}")
    print()

    print(f"  Периметр {triangle1.shape_id}: {triangle1.perimeter():.2f}")
    print(f"  Периметр {tetragon1.shape_id}: {tetragon1.perimeter():.2f}")


if __name__ == "__main__":
    main()
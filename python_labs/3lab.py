import math
class ShapeError(Exception):
    pass
class InvalidPointError(ShapeError):
    pass
class InvalidShapeError(ShapeError):
    pass
class Shape:
    def __init__(self, shape_id):
        if not shape_id or not isinstance(shape_id, str):
            raise ValueError("Идентификатор должен быть непустой строкой")
        self.shape_id = shape_id

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Координаты перемещения должны быть числами")
        raise NotImplementedError("Метод move должен быть реализован в подклассе")

    def compare(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Сравнение возможно только с геометрическими фигурами")
        try:
            return self.area() - other.area()
        except Exception as e:
            raise ShapeError(f"Ошибка при сравнении фигур: {e}")

    def area(self):
        raise NotImplementedError("Метод area должен быть реализован в подклассе")

    def __str__(self):
        return f"{self.__class__.__name__} '{self.shape_id}'"

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Координаты точки должны быть числами")
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Координаты перемещения должны быть числами")
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Расстояние можно вычислить только до другой точки")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Triangle(Shape):
    def __init__(self, shape_id, point1, point2, point3):
        super().__init__(shape_id)

        if not all(isinstance(p, Point) for p in [point1, point2, point3]):
            raise TypeError("Все вершины должны быть объектами Point")

        if self._are_points_collinear(point1, point2, point3):
            raise InvalidShapeError("Точки треугольника не должны быть коллинеарными")

        self.vertices = [point1, point2, point3]

    def _are_points_collinear(self, p1, p2, p3):
        area = abs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2)
        return area < 1e-10

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Координаты перемещения должны быть числами")

        for vertex in self.vertices:
            vertex.move(dx, dy)
        print(f"Треугольник '{self.shape_id}' перемещен на ({dx}, {dy})")

    def area(self):
        try:
            a = self.vertices[0].distance_to(self.vertices[1])
            b = self.vertices[1].distance_to(self.vertices[2])
            c = self.vertices[2].distance_to(self.vertices[0])

            if a + b <= c or a + c <= b or b + c <= a:
                raise InvalidShapeError("Невозможно вычислить площадь: нарушено неравенство треугольника")

            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))

            if area <= 0:
                raise InvalidShapeError("Некорректная площадь треугольника")

            return area
        except Exception as e:
            raise ShapeError(f"Ошибка вычисления площади треугольника: {e}")

    def perimeter(self):
        try:
            a = self.vertices[0].distance_to(self.vertices[1])
            b = self.vertices[1].distance_to(self.vertices[2])
            c = self.vertices[2].distance_to(self.vertices[0])
            return a + b + c
        except Exception as e:
            raise ShapeError(f"Ошибка вычисления периметра треугольника: {e}")

    def __str__(self):
        vertices_str = ", ".join(str(v) for v in self.vertices)
        try:
            area = self.area()
            return f"{super().__str__()} с вершинами [{vertices_str}], площадь: {area:.2f}"
        except ShapeError:
            return f"{super().__str__()} с вершинами [{vertices_str}], площадь: не вычислена"


class Tetragon(Shape):
    def __init__(self, shape_id, point1, point2, point3, point4):
        super().__init__(shape_id)

        if not all(isinstance(p, Point) for p in [point1, point2, point3, point4]):
            raise TypeError("Все вершины должны быть объектами Point")

        if self._is_self_intersecting(point1, point2, point3, point4):
            raise InvalidShapeError("Четырехугольник не должен быть самопересекающимся")

        self.vertices = [point1, point2, point3, point4]

    def _is_self_intersecting(self, p1, p2, p3, p4):
        def cross_product(o, a, b):
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        def segments_intersect(a, b, c, d):
            o1 = cross_product(a, b, c)
            o2 = cross_product(a, b, d)
            o3 = cross_product(c, d, a)
            o4 = cross_product(c, d, b)

            if o1 * o2 < 0 and o3 * o4 < 0:
                return True
            return False

        return segments_intersect(p1, p2, p3, p4) or segments_intersect(p2, p3, p4, p1)

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("Координаты перемещения должны быть числами")

        for vertex in self.vertices:
            vertex.move(dx, dy)
        print(f"Четырехугольник '{self.shape_id}' перемещен на ({dx}, {dy})")

    def area(self):
        try:
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

            total_area = area1 + area2

            if total_area <= 0:
                raise InvalidShapeError("Некорректная площадь четырехугольника")

            return total_area
        except Exception as e:
            raise ShapeError(f"Ошибка вычисления площади четырехугольника: {e}")

    def perimeter(self):
        try:
            perimeter = 0
            for i in range(4):
                perimeter += self.vertices[i].distance_to(self.vertices[(i + 1) % 4])
            return perimeter
        except Exception as e:
            raise ShapeError(f"Ошибка вычисления периметра четырехугольника: {e}")

    def __str__(self):
        vertices_str = ", ".join(str(v) for v in self.vertices)
        try:
            area = self.area()
            return f"{super().__str__()} с вершинами [{vertices_str}], площадь: {area:.2f}"
        except ShapeError:
            return f"{super().__str__()} с вершинами [{vertices_str}], площадь: не вычислена"


def main():
    try:
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
            try:
                difference = shape1.compare(shape2)
                if difference > 0:
                    result = f"площадь больше на {difference:.2f}"
                elif difference < 0:
                    result = f"площадь меньше на {abs(difference):.2f}"
                else:
                    result = "площади равны"
                print(f"  {description}: {result}")
            except ShapeError as e:
                print(f"  {description}: ошибка сравнения - {e}")
        print()

        try:
            print(f"  Периметр {triangle1.shape_id}: {triangle1.perimeter():.2f}")
        except ShapeError as e:
            print(f"  Ошибка вычисления периметра треугольника: {e}")

        try:
            print(f"  Периметр {tetragon1.shape_id}: {tetragon1.perimeter():.2f}")
        except ShapeError as e:
            print(f"  Ошибка вычисления периметра четырехугольника: {e}")

    except Exception as e:
        print(f"Критическая ошибка: {e}")


def test_exceptions():
    print("\n=== ТЕСТИРОВАНИЕ ИСКЛЮЧЕНИЙ ===")

    try:
        Point("invalid", "coordinates")
    except TypeError as e:
        print(f"Ошибка создания точки: {e}")

    try:
        Triangle("", Point(0, 0), Point(1, 0), Point(0, 1))
    except ValueError as e:
        print(f"Ошибка создания треугольника: {e}")

    try:
        Triangle("collinear", Point(0, 0), Point(1, 1), Point(2, 2))
    except InvalidShapeError as e:
        print(f"Ошибка создания треугольника: {e}")

    try:
        p1, p2, p3, p4 = Point(0, 0), Point(2, 2), Point(0, 2), Point(2, 0)
        Tetragon("intersecting", p1, p2, p3, p4)
    except InvalidShapeError as e:
        print(f"Ошибка создания четырехугольника: {e}")


if __name__ == "__main__":
    main()
    test_exceptions()
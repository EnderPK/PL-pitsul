import math

def is_point_inside_circle(x, y, a, b, r):
    """Проверяет, лежит ли точка внутри окружности"""
    return math.sqrt((x - a)**2 + (y - b)**2) <= r

def count_points_inside_circle(a, b, r, points):
    """Считает количество точек внутри окружности"""
    count = 0
    for point in points:
        if is_point_inside_circle(point[0], point[1], a, b, r):
            count += 1
    return count

# Тестовые данные
a, b = 0, 0  # центр окружности
r = 5  # радиус окружности
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]  # точки

print(f"Количество точек внутри окружности: {count_points_inside_circle(a, b, r, points)}")
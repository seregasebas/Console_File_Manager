'''Тесты для встроенных функций:
filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot'''
# импортируем математику
import math

# Тест для filter
def test_filter():
    # выполнение условий с цифрами
    assert list(filter(lambda x: x>10, [3,5,6,11,2,34,56])) == [11, 34, 56]
    # выполнение фильтра со str
    assert list(filter(lambda x: x == 'hi', ['hello', 'hi', 'hi', 'what'])) == ['hi', 'hi']

# Тест для map
def test_map():
    assert list(map(int, ['23', '77'])) == [23, 77]
    assert isinstance(list(map(int, ['77']))[0], int)

# Тест для sorted
def test_sorted():
    assert sorted([1,8,3], reverse = False) == [1,3,8]
    assert sorted([1,8,3], reverse = True) == [8,3,1]
    assert sorted(['alpha', 'gamma', 'beta']) == ['alpha', 'beta', 'gamma']
    assert sorted(['hi','hello', 'fly'], key=len) == ['hi', 'fly', 'hello']

# Тест для math.pi
def test_math_pi():
    assert math.pi == 3.141592653589793

# Тест для math.sqrt
def test_math_sqrt():
    assert math.sqrt(9) == 3

# Тест для math.pow
def test_math_pow():
    assert math.pow(2,-1) == 0.5
    assert math.pow(2,3) == 8.0

# Тест для math.hypot
def test_math_hypot():
    assert math.hypot(4,5) == math.sqrt(4 * 4 + 5 * 5)
from functions.level_2.two_square_equation import solve_square_equation

import pytest

def test__solve_square_equation__two_roots_success():
    assert solve_square_equation(2, -4, -6) == (-1, 3)

def test__solve_square_equation__one_root_success():
    assert solve_square_equation(3, -6, 3) == (1.0, 1.0)

def test__solve_square_equation__zero_root_success():
    assert solve_square_equation(4.0, 8.0, 5.0) == (None, None)

def test__solve_square_equation__not_square_coefficient():
    assert solve_square_equation(0, 8, 5) == (-0.625, None)

def test__solve_square_equation__not_square_coefficient_and_linear_coefficient():
    assert solve_square_equation(0, 0, 5) == (None, None)

@pytest.mark.parametrize(('a', 'b', 'c', 'expected'), [
    (1, -5, 6, (2.0, 3.0)),
    (1, 6, 9, (-3.0, -3.0)),
    (2, 4, 5, (None, None))
])
def test__solve_square_equation__solves_quadratic_equations(a, b, c, expected):
    assert solve_square_equation(a, b, c) == expected
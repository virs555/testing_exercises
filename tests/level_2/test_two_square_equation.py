from functions.level_2.two_square_equation import solve_square_equation

import pytest

@pytest.mark.parametrize(('a', 'b', 'c', 'expected'), [
    (1, -5, 6, (2.0, 3.0)),
    (2, -7, 3, (0.5, 3.0)),
    (1, -3, 2, (1.0, 2.0))
])
def test__solve_square_equation__return_two_roots(a, b, c, expected):
    assert solve_square_equation(a, b, c) == expected

@pytest.mark.parametrize(('a', 'b', 'c', 'expected'), [
    (1, -2, 1, (1.0, 1.0)),
    (4, -4, 1, (0.5, 0.5)),
    (16, -8, 1, (0.25, 0.25))
])
def test__solve_square_equation__return_one_roots(a, b, c, expected):
    assert solve_square_equation(a, b, c) == expected

@pytest.mark.parametrize(('a', 'b', 'c', 'expected'), [
    (1, 2, 3, (None, None)),
    (2, 3, 5, (None, None)),
    (4, 4, 5, (None, None))
])
def test__solve_square_equation__return_none_when_without_roots(a, b, c, expected):
    assert solve_square_equation(4.0, 8.0, 5.0) == (None, None)

def test__solve_square_equation__return_one_root_when_no_square_coeff():
    assert solve_square_equation(0, 8, 5) == (-0.625, None)

def test__solve_square_equation__return_no_solution_for_zero_a_and_b_with_nonzero_c():
    assert solve_square_equation(0, 0, 5) == (None, None)
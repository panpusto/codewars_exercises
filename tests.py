import pytest

from exercises import calculating_with_functions as c
from exercises.increment_string import increment_string
from exercises.summation import summation
from exercises.intro_bites_08_by_PyBites import BeltStats, ninja_belts, get_total_points
from exercises.intro_bite_09_by_PyBites import get_workout_motd, INVALID_DAY, CHILL_OUT


def test_summation():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791


#   test for intro_bites_08_by_PyBites
def test_get_total_points_given_belts():
    assert get_total_points(ninja_belts) == 2675


def test_get_total_points_more_belts():
    more_belts = dict(brown=BeltStats(400, 2),
                      black=BeltStats(600, 5))

    # this way to dict merge is >= 3.5 (PEP 448)
    ninja_belts_updated = {**ninja_belts, **more_belts}

    assert get_total_points(ninja_belts_updated) == 6475


#   tests for intro_bite_09_by_PyBites
@pytest.mark.parametrize("day, expected", [
    ('Monday', 'Go train Chest+biceps'),
    ('monday', 'Go train Chest+biceps'),
    ('Tuesday', 'Go train Back+triceps'),
    ('TuEsdAy', 'Go train Back+triceps'),
    ('Wednesday', 'Go train Core'),
    ('wednesdaY', 'Go train Core'),
    ('Thursday', 'Go train Legs'),
    ('Friday', 'Go train Shoulders'),
    ('Saturday', CHILL_OUT),
    ('Sunday', CHILL_OUT),
    ('sundAy', CHILL_OUT),
    ('nonsense', INVALID_DAY),
    ('monday2', INVALID_DAY),
])
def test_get_workout_valid_case_insensitive_dict_lookups(day, expected):
    assert get_workout_motd(day) == expected


#   test for increment_string.py
def test_increment_string():
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    assert increment_string("foobar1") == "foobar2"
    assert increment_string("foobar00") == "foobar01"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar099") == "foobar100"
    assert increment_string("") == "1"


#   test for calculating_with functions
def test_calculating_with_functions():
    assert c.seven(c.times(c.five())) == 35
    assert c.four(c.plus(c.nine())) == 13
    assert c.eight(c.minus(c.three())) == 5
    assert c.six(c.divided_by(c.two())) == 3

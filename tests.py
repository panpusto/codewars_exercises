import pytest

from exercises.summation import summation
from intro_bites_08_by_PyBites import BeltStats, ninja_belts, get_total_points


def test_summation():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791


def test_get_total_points_given_belts():
    assert get_total_points(ninja_belts) == 2675


def test_get_total_points_more_belts():
    more_belts = dict(brown=BeltStats(400, 2),
                      black=BeltStats(600, 5))

    # this way to dict merge is >= 3.5 (PEP 448)
    ninja_belts_updated = {**ninja_belts, **more_belts}

    assert get_total_points(ninja_belts_updated) == 6475
"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

import pytest

from inflammation.models import daily_mean, daily_max, daily_min


@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0,0], [0,0], [0,0] ], [0,0]),
            ([ [1,2], [3,4], [5,6] ], [3,4])
        ])

def test_daily_mean(test, expected):
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

def test_daily_min_string():
    """Test for TypeError when passing strings."""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [1,3], [56,9], [0,2] ], [0,2])
        ])

def test_daily_min(test, expected):
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [1,2], [30, np.nan] ], [30, np.nan])
        ])

def test_daily_max(test, expected):
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

        




from mtf import line
import numpy as np
import pytest


def test_on_line():

    l = line.Line.from_points((0, 0), (1, 1))

    assert l.dist((0, 0)) == 0


def test_dist():
    l = line.Line.from_points((0, 0), (1, 1))

    assert l.dist((1, 0)) == pytest.approx(np.sqrt(2) / 2)


def test_signed_dist():
    l = line.Line.from_points((0, 0), (1, 1))

    d_up = l.signed_dist((0, 1))
    d_down = l.signed_dist((1, 0))

    assert np.sign(d_up) == -1 * np.sign(d_down)
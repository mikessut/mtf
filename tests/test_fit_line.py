import mtf
from mtf.line import Line
import tests
import pytest
import logging


log = logging.getLogger(__name__)
log.setLevel("DEBUG")

def test_fit_line_vert():

    l = mtf.fit_line(tests.vert_test_img())

    expected_line = Line.from_points(*tests.TEST_LINE_POINTS)

    log.info(f"line: {l} {expected_line}")

    assert expected_line.slope == pytest.approx(l.slope, 0.005)


def test_fit_line_horz():

    l = mtf.fit_line(tests.horz_test_img())

    expected_line = Line.from_points(*[(y, x) for x, y in tests.TEST_LINE_POINTS])

    log.info(f"line: {l} {expected_line}")

    assert expected_line.slope == pytest.approx(l.slope, 0.005)

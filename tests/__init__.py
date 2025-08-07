import numpy as np
from mtf.line import Line
from scipy.ndimage import gaussian_filter


TEST_IMG_SHAPE = (400, 400)

SLANT_ANGLE = np.radians(5)

TEST_LINE_POINTS = [
    (220, 0), 
    (100 + np.tan(SLANT_ANGLE) * TEST_IMG_SHAPE[0], TEST_IMG_SHAPE[1])
]

def vert_test_img(sigma=2):
    img = np.zeros(TEST_IMG_SHAPE)

    l = Line.from_points(*TEST_LINE_POINTS)

    ROWS, COLS = np.indices(img.shape)

    DIST = np.vectorize(lambda x, y: l.signed_dist((x, y)))(COLS.flatten(), ROWS.flatten()).reshape(TEST_IMG_SHAPE)

    img[DIST > 0] = 1
    img[DIST <= 0] = 0

    return gaussian_filter(img, sigma)


def horz_test_img(sigma=2):
    img = vert_test_img(sigma)
    return img.T
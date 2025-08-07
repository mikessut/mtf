import mtf
import matplotlib.pyplot as plt
import tests


def test_LSF():
    img = tests.vert_test_img(sigma=.2)

    line = mtf.fit_line(img)

    x, y, dy = mtf.img_to_LSF(img, line)

    plt.figure()
    plt.plot(x, y)

    plt.figure()
    plt.plot(x[1:], dy)

    f, MTF = mtf.LSF_to_MTF(y)

    plt.figure()
    plt.plot(f, MTF)

    plt.show()
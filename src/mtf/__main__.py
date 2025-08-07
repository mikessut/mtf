import argparse
import mtf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('input_image')
    args = parser.parse_args()

    img = np.array(Image.open(args.input_image))

    line = mtf.fit_line(img)
    x, y, dy = mtf.img_to_LSF(img, line)
    f, MTF = mtf.LSF_to_MTF(y)

    plt.figure()
    plt.imshow(img)

    _, ax = plt.subplots(2, 1)
    ax[0].plot(x, y)
    ax[1].plot(x[1:], dy)

    plt.figure()
    plt.plot(f, MTF)

    plt.show()
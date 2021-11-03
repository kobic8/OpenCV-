# This is a Python script based on:
# https://opencv24-python-tutorials.readthedocs.io/_/downloads/en/stable/pdf/
import cv2.cv2 as cv2


def read_write_image():
    # read image.
    flag = 0  # load a greyscale image
    flag = -1  # loads including alpha channel
    flag = 0  # loads a color image

    filename = 'DataBase/img_for_obj_detection.ppm'

    img = cv2.imread(filename, flag)
    # show image
    cv2.imshow('Image', img)
    print("Press s to save the image, or ESC to exit")
    key = cv2.waitKey(0)  # to allow us to see the image
    if key == ord('s'):
        # write image
        filename_gray = filename[:-4] + ".png"
        cv2.imwrite(filename_gray, img)
        cv2.destroyAllWindows()
    elif key == 27:  # ESC
        cv2.destroyAllWindows()


def read_with_matplotlib():
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    # read image.
    print(matplotlib.get_backend())
    filename = 'DataBase/img_for_obj_detection.png'
    img = cv2.imread(filename, 0)
    # show image
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # hide tick values for X Y
    plt.show()


def image_blending():
    img1 = cv2.imread("/home/yakovc/PycharmProjects/opencv_tut/DataBase/pic_1_openCV.png") # pic_1_openCV.png")
    img2 = cv2.imread("DataBase/pic_2_bot.png")

    dim1 = list(img1.shape)[:-1]
    dim2 = list(img2.shape)[:-1]
    if not dim1 == dim2:
        print("dimensions of image1 are: {}".format(dim1))
        print("dimensions of image2 are: {}".format(dim2))
        print("reverse way is: {}".format(dim1[::-1]))
        # img2 = cv2.resize(img2, [228, 286])
        img2 = cv2.resize(img2, dim1[::-1])
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(cv2.__version__)
    # read_with_matplotlib()
    image_blending()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

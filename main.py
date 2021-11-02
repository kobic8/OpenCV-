# This is a Python script based on:
# https://opencv24-python-tutorials.readthedocs.io/_/downloads/en/stable/pdf/
import cv2.cv2 as cv2


def read_write_image():
    # read image.
    flag = 0  # load a greyscale image
    flag = -1  # loads including alpha channel
    flag = 0  # loads a color image

    filename = 'img_for_obj_detection.ppm'

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

    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(cv2.__version__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_write_image()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



def create_mask(path, color_threshold):
    """
    create a binary mask of an image using a color threshold
    args:
    - path [str]: path to image file
    - color_threshold [array]: 1x3 array of RGB value
    returns:
    - img [array]: RGB image array
    - mask [array]: binary array
    """
    # IMPLEMENT THIS FUNCTION
    # img = mpimg.imread(path)
    img_pillow = np.array(Image.open(path))

    red = img_pillow[:, :, 0]
    blue = img_pillow[:, :, 1]
    green = img_pillow[:, :, 2]

    red_thres, blue_thres, green_thres = color_threshold
    mask = (red>red_thres) & (blue>blue_thres) & (green>green_thres)

    return img_pillow, mask


def mask_and_display(img, mask):
    """
    display 3 plots next to each other: image, mask and masked image
    args:
    - img [array]: HxWxC image array
    - mask [array]: HxW mask array
    """
    # IMPLEMENT THIS FUNCTION
    masked_image = img * np.stack([mask]*3, axis=2)
    fig, ax = plt.subplots(1,3)
    ax[0].imshow(img)
    ax[1].imshow(mask)
    ax[2].imshow(masked_image)
    plt.show()
    print('debug stop')


if __name__ == '__main__':
    path = 'data/images/segment-1231623110026745648_480_000_500_000_with_camera_labels_38.png'
    color_threshold = [128, 128, 128]
    img, mask = create_mask(path, color_threshold)
    mask_and_display(img, mask)
import glob
from PIL import Image, ImageStat
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_mean_std(image_list):
    """
    calculate mean and std of image list
    args:
    - image_list [list[str]]: list of image paths
    returns:
    - mean [array]: 1x3 array of float, channel wise mean
    - std [array]: 1x3 array of float, channel wise std
    """
    # IMPLEMENT THIS FUNCTION
    means = []
    stds = []


    for image in image_list:
        stat = ImageStat.Stat(Image.open(image))
        means.append(np.array(stat.mean))
        stds.append(np.array(stat.stddev))

    total_mean = np.mean(means, axis=0)
    total_std = np.mean(stds, axis=0)

    print('debug')

    return total_mean, total_std


def channel_histogram(image_list):
    """
    calculate channel wise pixel value
    args:
    - image_list [list[str]]: list of image paths
    """
    # IMPLEMENT THIS FUNCTION
    red_list = []
    green_list = []
    blue_list = []

    for image_path in image_list:
        print(f'Processing   {image_path}')
        image = np.array(Image.open(image_path))
        red = image[:, :, 0]
        green = image[:, :, 1]
        blue = image[:, :, 2]
        red_list.extend(red.flatten())
        blue_list.extend(blue.flatten())
        green_list.extend(green.flatten())

    plt.figure()
    sns.kdeplot(red_list, color='r')
    sns.kdeplot(green_list, color='g')
    sns.kdeplot(blue_list, color='b')
    plt.show()

    print('debug stop')


if __name__ == "__main__": 
    image_list = glob.glob('data/images/*')
    mean, std = calculate_mean_std(image_list)
    channel_histogram(image_list[:2])
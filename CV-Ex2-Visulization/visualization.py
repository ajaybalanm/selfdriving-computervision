from utils import get_data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def viz(ground_truth):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """
    # IMPLEMENT THIS FUNCTION
    images = []
    for g in ground_truth:
        print(g['filename'])
        images.append('./data/images/'+g['filename'])


    # fig, ax = plt.subplots(2,1)
    # plt.show()
    nrow = 4
    ncol = 5


    _, axs = plt.subplots(nrow, ncol, figsize=(100, 100))
    axs = axs.flatten()
    for img, ax in zip(images, axs):
        # img1 = mpimg(img)
        ax.imshow(mpimg.imread(img))
    plt.show()

    print('Debug Stop')

if __name__ == "__main__": 
    ground_truth, _ = get_data()
    viz(ground_truth)
from utils import get_data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle

def createRectangle(box,classes):

    x = box[0]
    y = box[1]
    # this is the top left. plt.show() has different coordinates (0,0) is bottom left
    # where as img show() has (0,0) as top left.
    # so we don't need to convert the coordinates

    width = box[2] - box[0]
    height = box[3] - box[1]
    if classes == 1:
        color = 'g'
    elif classes == 2:
        color = 'r'

    rect = Rectangle((y, x), height, height=width, fc='none', ec=color, lw=1)

    return rect





def viz(ground_truth):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """
    # IMPLEMENT THIS FUNCTION

    fig, axs = plt.subplots(4, 5)
    axs = axs.flatten()
    for g, ax in zip(ground_truth, axs):
        ax.imshow(mpimg.imread('./data/images/' + g['filename']))
        for box, classes in zip(g['boxes'], g['classes']):
            rect = createRectangle(box, classes)
            ax.add_patch(rect)
        ax.axis('off')

    plt.show()


if __name__ == "__main__": 
    ground_truth, _ = get_data()
    viz(ground_truth)
from utils import get_data
from matplotlib import pyplot as plt


def viz(ground_truth):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """
    # IMPLEMENT THIS FUNCTION

    fig, ax = plt.subplots(2,1)
    plt.show()
    print('Debug Stop')

if __name__ == "__main__": 
    ground_truth, _ = get_data()
    viz(ground_truth)
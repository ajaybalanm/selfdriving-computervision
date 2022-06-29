import copy
import json


import numpy as np 
from PIL import Image
from utils import display_results, check_results


def calculate_iou(gt_bbox, pred_bbox):
    """
    calculate iou 
    args:
    - gt_bbox [array]: 1x4 single gt bbox
    - pred_bbox [array]: 1x4 single pred bbox
    returns:
    - iou [float]: iou between 2 bboxes
    - [xmin, ymin, xmax, ymax]
    """
    xmin = np.max([gt_bbox[0], pred_bbox[0]])
    ymin = np.max([gt_bbox[1], pred_bbox[1]])
    xmax = np.min([gt_bbox[2], pred_bbox[2]])
    ymax = np.min([gt_bbox[3], pred_bbox[3]])
    
    intersection = max(0, xmax - xmin) * max(0, ymax - ymin)
    gt_area = (gt_bbox[2] - gt_bbox[0]) * (gt_bbox[3] - gt_bbox[1])
    pred_area = (pred_bbox[2] - pred_bbox[0]) * (pred_bbox[3] - pred_bbox[1])
    
    union = gt_area + pred_area - intersection
    return intersection / union, [xmin, ymin, xmax, ymax]


def hflip(img, bboxes):
    """
    horizontal flip of an image and annotations
    args:
    - img [PIL.Image]: original image
    - bboxes [list[list]]: list of bounding boxes
    return:
    - flipped_img [PIL.Image]: horizontally flipped image
    - flipped_bboxes [list[list]]: horizontally flipped bboxes
    """
    # IMPLEMENT THIS FUNCTION
    bboxes = np.array(bboxes)
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_bboxes = copy.copy(bboxes)

    print(id(bboxes))
    print(id(flipped_bboxes))

    for flip_box in flipped_bboxes:
        flip_box[1] = img.width - flip_box[1]
        flip_box[3] = img.width - flip_box[3]

    display_results(img, bboxes, flipped_img, flipped_bboxes)

    print('debug stop')
    return flipped_img, flipped_bboxes


def resize(img, boxes, size):
    """
    resized image and annotations
    args:
    - img [PIL.Image]: original image
    - boxes [list[list]]: list of bounding boxes
    - size [array]: 1x2 array [width, height]
    returns:
    - resized_img [PIL.Image]: resized image
    - resized_boxes [list[list]]: resized bboxes
    """
    # IMPLEMENT THIS FUNCTION

    resized_image = img.resize(size)
    bboxes = np.array(boxes)

    resized_boxes = copy.copy(bboxes)

    h, w = size

    height_ratio = h /img.height
    width_ratio = w / img.width



    resized_boxes[:, 0] = resized_boxes[:, 0] * height_ratio
    resized_boxes[:, 1] = resized_boxes[:, 1] * width_ratio
    resized_boxes[:, 2] = resized_boxes[:, 2] * height_ratio
    resized_boxes[:, 3] = resized_boxes[:, 3] * width_ratio

    display_results(img, boxes, resized_image, resized_boxes)

    print('debug stop')

    return resized_image, resized_boxes


def random_crop(img, boxes, crop_size, min_area=100):
    """
    random cropping of an image and annotations
    args:
    - img [PIL.Image]: original image
    - boxes [list[list]]: list of bounding boxes
    - crop_size [array]: 1x2 array [width, height]
    - min_area [int]: min area of a bbox to be kept in the crop
    returns:
    - cropped_img [PIL.Image]: resized image
    - cropped_boxes [list[list]]: resized bboxes
    """
    # IMPLEMENT THIS FUNCTION
    return cropped_image, cropped_boxes

if __name__ == "__main__":

    with open('data/ground_truth.json') as f:
        ground_truth = json.load(f)

    assignment_image = 'segment-12208410199966712301_4480_000_4500_000_with_camera_labels_79.png'
    img = Image.open(f'data/images/{assignment_image}')
    img_array = np.array(img)
    bboxes = [g['boxes'] for g in ground_truth if g['filename'] == assignment_image][0]

    flipped_img, flipped_bboxes = hflip(img, bboxes)
    resized_image, resized_boxes = resize(img, bboxes, size=[640, 640])

    check_results(resized_image, resized_boxes, 'resize')
    check_results(flipped_img, flipped_bboxes, 'hflip')


    print('debug stop')
    # fix seed to check results
    
    # open annotations
    
    # filter annotations and open image
    
    # check horizontal flip, resize and random crop
    # use check_results defined in utils.py for this

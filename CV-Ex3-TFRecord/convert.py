import io
import os
import argparse
import logging

import tensorflow.compat.v1 as tf
from PIL import Image
from waymo_open_dataset import dataset_pb2 as open_dataset

from utils import parse_frame, int64_feature, int64_list_feature, bytes_feature
from utils import bytes_list_feature, float_list_feature


def create_tf_example(filename, encoded_jpeg, annotations):
    """
    convert to tensorflow object detection API format
    args:
    - filename [str]: name of the image
    - encoded_jpeg [bytes-likes]: encoded image
    - annotations [list]: bboxes and classes
    returns:
    - tf_example [tf.Example]
    """
    # TO BE IMPLEMENTED  
    encoded_jpeg_io = io.BytesIO(encoded_jpeg)
    image = Image.open(encoded_jpeg_io)
    width, height = image.size

    classid_map = {1: 'vehicle', 2: 'pedestrian'}
    xmins = []
    ymins = []
    xmaxs = []
    ymaxs = []
    classes_text = []
    classid = []

    for item in annotations: 
        xmin= item.box.center_x - (item.box.length/2)
        ymin= item.box.center_y - (item.box.width/2)
        xmax= item.box.center_x + (item.box.length/2)
        ymax= item.box.center_y + (item.box.width/2)
        xmins.append(xmin / width)
        ymins.append(ymin / height)
        xmaxs.append(xmax / width)
        ymaxs.append(ymax / height)
        classes_text.append(classid_map[item.type].encode('utf8'))
        classid.append(item.type)

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': int64_feature(height),
        'image/width' : int64_feature(width),
        'image/filename' : bytes_feature(filename.encode('utf8')),
        'image/object/bbox/xmin' : float_list_feature(xmins),
        'image/object/bbox/ymin' : float_list_feature(ymins),
        'image/object/bbox/xmax' : float_list_feature(xmaxs),
        'image/object/bbox/ymax' : float_list_feature(ymaxs),
        'image/object/class/text': bytes_list_feature(classes_text),
        'image/object/class/id' : int64_list_feature(classid)
    }))

    print('debug stop')
    return tf_example


def process_tfr(path):
    """
    process a waymo tf record into a tf api tf record
    """
    # create processed data dir
    file_name = os.path.basename(path)

    logging.info(f'Processing {path}')
    writer = tf.python_io.TFRecordWriter(f'output/{file_name}')
    dataset = tf.data.TFRecordDataset(path, compression_type='')
    for idx, data in enumerate(dataset):
        frame = open_dataset.Frame()
        frame.ParseFromString(bytearray(data.numpy()))
        encoded_jpeg, annotations = parse_frame(frame)
        filename = file_name.replace('.tfrecord', f'_{idx}.tfrecord')
        tf_example = create_tf_example(filename, encoded_jpeg, annotations)
        writer.write(tf_example.SerializeToString())
    writer.close()


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', required=True, type=str,
                        help='Waymo Open dataset tf record')
    args = parser.parse_args()  
    process_tfr(args.path)
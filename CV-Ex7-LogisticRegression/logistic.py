import tensorflow as tf
from solution.utils import check_softmax, check_acc, check_model, check_ce

import numpy as np



def softmax(logits):
    """
    softmax implementation
    args:
    - logits [tensor]: 1xN logits tensor
    returns:
    - soft_logits [tensor]: softmax of logits
    """
    # IMPLEMENT THIS FUNCTION
    num = tf.exp(logits)
    den = tf.math.reduce_sum(num, keepdims=False)

    soft_logits = num/den
    print('debug stop')


    return soft_logits


def cross_entropy(scaled_logits, one_hot):
    """
    Cross entropy loss implementation
    args:
    - scaled_logits [tensor]: NxC tensor where N batch size / C number of classes
    - one_hot [tensor]: one hot tensor
    returns:
    - loss [tensor]: cross entropy 
    """
    # IMPLEMENT THIS FUNCTION
    loss = -tf.reduce_sum(one_hot * np.log(scaled_logits)) / float(scaled_logits.shape[0])
    return loss


def model(X, W, b):
    """
    logistic regression model
    args:
    - X [tensor]: input HxWx3
    - W [tensor]: weights
    - b [tensor]: bias
    returns:
    - output [tensor]
    """
    # IMPLEMENT THIS FUNCTION

    x = tf.reshape(X, (-1, W.shape[0]))
    y_hat = tf.matmul(x, W) + b

    output = softmax(y_hat)

    print('debug stop')
    return output


def accuracy(y_hat, Y):
    """
    calculate accuracy
    args:
    - y_hat [tensor]: NxC tensor of models predictions
    - y [tensor]: N tensor of ground truth classes
    returns:
    - acc [tensor]: accuracy
    """
    # IMPLEMENT THIS FUNCTION

    argmax = tf.cast(tf.argmax(y_hat, axis=1), Y.dtype)
    true_positives = tf.math.reduce_sum(tf.cast(argmax == Y, Y.dtype))
    print('debug stop')
    return true_positives/Y.shape[0]

def main():
    check_softmax(softmax)
    check_ce(cross_entropy)
    check_model(model)
    check_acc(accuracy)


if __name__ == "__main__":
    main()

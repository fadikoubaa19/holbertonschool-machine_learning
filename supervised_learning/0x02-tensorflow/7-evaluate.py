#!/usr/bin/env python3
"""
7-evaluate
"""

import tensorflow as tf


def evaluate(X, Y, save_path):
    """evaluation of neural network"""
    with tf.Session() as sess:
        salide = tf.train.import_meta_graph("{}.meta".format(save_path))
        salide.restore(sess, save_path)

        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        y_pred = tf.get_collection("y_pred")[0]
        accuracy = tf.get_collection("accuracy")[0]
        loss = tf.get_collection("loss")[0]

        eval_y_pred = sess.run(y_pred, feed_dict={x: X, y: Y})
        eval_accuracy = sess.run(accuracy, feed_dict={x: X, y: Y})
        eval_loss = sess.run(loss, feed_dict={x: X, y: Y})
        return eval_y_pred, eval_accuracy, eval_l

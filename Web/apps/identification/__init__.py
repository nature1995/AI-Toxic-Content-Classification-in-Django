import os
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF

# 指定第一块GPU可用 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

config = tf.ConfigProto()
config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
sess = tf.Session(config=config)

KTF.set_session(sess)

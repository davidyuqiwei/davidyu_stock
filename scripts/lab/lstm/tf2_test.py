import numpy as np
import tensorflow as tf

# 建立模型
inputs = tf.keras.layers.Input(shape=(3, 1))
lstm = tf.keras.layers.LSTM(1)(inputs)
model = tf.keras.models.Model(inputs=inputs, outputs=lstm)
# t1, t2, t3 序列
data = np.atleast_3d([0.1, 0.2, 0.3])
model.predict(data)

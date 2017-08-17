from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D
import tensorflow as tf

model = Sequential()
model.add(GlobalAveragePooling2D(input_shape=(7, 7, 512)))
model.add(Dense(133, activation='softmax'))
model.load_weights('./backend/resources/models/weights.hdf5')

graph = tf.get_default_graph()

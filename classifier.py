import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
train_datagen= ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(
	'Data/Train',
	target_size=(150,150),
	batch_size=20,
	class_mode='binary')
test_datagen=ImageDataGenerator(rescale=1./255)
test_generator=test_datagen.flow_from_directory(
	'Data/Test',
	target_size=(150,150),
	batch_size=20,
	class_mode='binary')
model=tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(16,(3,3),activation='relu',input_shape=(150,150,3)),
	tf.keras.layers.MaxPooling2D(2,2),
 	tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
 	tf.keras.layers.MaxPooling2D(2,2),
 	tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
 	tf.keras.layers.Flatten(),
 	tf.keras.layers.Dense(512,activation='relu'),
 	tf.keras.layers.Dense(1,activation='sigmoid')])
model.compile(loss='binary_crossentropy',optimizer=RMSprop(lr=0.001),metrics=['accuracy'])
model.summary()
history=model.fit_generator(train_generator,steps_per_epoch=100,epochs=15,validation_data=test_generator,validation_steps=80)
model.save('AadharClassifier.h5')


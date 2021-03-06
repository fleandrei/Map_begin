#!/usr/bin/python3.7
#-*- coding:Utf-8 -*
import tensorflow as tf 
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *



#fonctions utilisés pour afficher les images 
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

#afficher les probas avec un diagramme en baton
def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')





#Hello world
print("salut")
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


#
fashion=keras.datasets.fashion_mnist #On utilise des jeux de données fournis par Keras appellés "fashion_mnist"

#On charge ces donnnées:
(train_images, train_labels), (test_images, test_labels) = fashion.load_data()


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_labels


#affichage du premier element
#plt.figure()
#plt.imshow(train_images[0])
#plt.colorbar()
#plt.grid(False)



train_images = train_images / 255.0

test_images = test_images / 255.0


#affichage des labels
#plt.figure(figsize=(10,10))
#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(train_images[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[train_labels[i]])
#plt.show()

#Création du modèle
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),   #
    keras.layers.Dense(10, activation=tf.nn.softmax)  #
])

model.compile(optimizer=tf.train.AdamOptimizer(),   #regarder
              loss='sparse_categorical_crossentropy',   #
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=1)  #epochs= nombre de fois où l'ensemble des 60 000 images sont passée dans le réseau de neuronnes pour l'entrainement


test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)
print('test_loss:',test_loss)
predictions = model.predict(test_images)









#test
i=input("quel élément voulez vous tester ?")
i=int(i)
print('le {} élèment est un : {}'.format(i, class_names[np.argmax(predictions[i])]))
#print(np.argmax(predictions[0]))

#Affichage de l'image avec sa légende ainsi que des barplot des probabilités.
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)



# affiche les 15 premiers images et le resultat du test
#num_rows = 5
#num_cols = 3
#num_images = num_rows*num_cols
#plt.figure(figsize=(2*2*num_cols, 2*num_rows))
#for i in range(num_images):
#  plt.subplot(num_rows, 2*num_cols, 2*i+1)
#  plot_image(i, predictions, test_labels, test_images)
#  plt.subplot(num_rows, 2*num_cols, 2*i+2)
#  plot_value_array(i, predictions, test_labels)


plt.show()

img = test_images[0]

print(img.shape)

img = (np.expand_dims(img,0))

print(img.shape)


predictions_single = model.predict(img)

print(predictions_single)


plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)











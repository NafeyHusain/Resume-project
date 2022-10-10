import cv2 as cv;
import numpy as np;
import matplotlib.pyplot as plt;

from tensorflow.teras import datasets,layers,models

(training_image,training_labels),(testing_image,testing_labels)=detasets.cifar10.load_data()

training_image,testing_image=training_image/255,testing_image/255


class_names=['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_image[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i][0]])

plt.show()

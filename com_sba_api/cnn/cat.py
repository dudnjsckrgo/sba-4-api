import tensorflow as tf
import matplotlib.pyplot as plt
from numpy import array, zeros_like
class Cat:
    def show(self):
        image_path  = tf.keras.utils.get_file('cat.jpg', 'http://bit.ly/33U6mH9')
        image = plt.imread(image_path)
        titles = ['RGB Image', "Red channel", 'Green channel', 'Blue channel']
        
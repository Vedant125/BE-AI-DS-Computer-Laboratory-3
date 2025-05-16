''' Practical 6 : Create and Art with Neural style transfer on a given image using 
deep learning. '''
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load and preprocess image
def load_image(path, image_size=(256, 256)):
    img = Image.open(path).convert('RGB')
    img = img.resize(image_size)
    img = np.array(img) / 255.0
    img = img.astype(np.float32)
    return tf.image.convert_image_dtype(img, dtype=tf.float32)[tf.newaxis, ...]

# Load content and style images
content_path = "C:/College Notes/BE SEM 8/Practicals/cl3/6 - NST/content_image.jpg" # put your path 
style_path = "C:/College Notes/BE SEM 8/Practicals/cl3/6 - NST/style_image.jpg"

content_image = load_image(content_path)
style_image = load_image(style_path)

# Load pre-trained NST model from TensorFlow Hub
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Stylize image
stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

# Display all images side-by-side
plt.figure(figsize=(12, 4))

titles = ['Content Image', 'Style Image', 'Stylized Image']
images = [content_image, style_image, stylized_image]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(tf.squeeze(images[i]))
    plt.axis('off')
    plt.title(titles[i])

plt.tight_layout()
plt.show()

import numpy as np
import os
import cv2

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def preprocess_images(images):
    processed_images = []
    for img in images:
        processed_img = cv2.resize(img, (64, 64))
        processed_images.append(processed_img)
    return np.array(processed_images)

def load_data(folder):
    images = load_images_from_folder(folder)
    processed_images = preprocess_images(images)
    return processed_images

def load_labels(folder, label):
    num_images = len(os.listdir(folder))
    labels = np.full((num_images,), label)
    return labels

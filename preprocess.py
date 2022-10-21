import os
import shutil
import tempfile
import matplotlib.pyplot as plt
import PIL
import torch
import numpy as np

root_dir =  os.path.dirname(os.path.realpath(__file__))
#data_dir = os.path.join(root_dir, 'data')
data_dir = os.path.join(root_dir, "data/MedNIST")
def plot_sample(image_files, image_class, class_names, image_files_list):
    plt.subplots(2, 5, figsize=(8, 8))
    for i, k in enumerate(np.random.randint(len(image_class), size=10)):
        im = PIL.Image.open(image_files_list[k])
        arr = np.array(im)
        plt.subplot(2, 5, i + 1)
        plt.xlabel(class_names[image_class[k]])
        plt.imshow(arr, cmap="gray", vmin=0, vmax=255)
    plt.tight_layout()
    plt.show()




def preprocess(if_plot = False):
    """
    reads image and prepares dataloader
    """
    print('Preprocessing data')
    class_names = sorted(x for x in os.listdir(data_dir)
                     if os.path.isdir(os.path.join(data_dir, x)))
    num_class = len(class_names)
    image_files = [
        [
            os.path.join(data_dir, class_names[i], x)
            for x in os.listdir(os.path.join(data_dir, class_names[i]))
        ]
        for i in range(num_class)
        ]
    num_each = [len(image_files[i]) for i in range(num_class)]
    image_files_list = []
    image_class = []


    for i in range(num_class):
        image_files_list.extend(image_files[i])
        image_class.extend([i] * num_each[i])
    num_total = len(image_class)
    image_width, image_height = PIL.Image.open(image_files_list[0]).size

    print(f"Total image count: {num_total}")
    print(f"Image dimensions: {image_width} x {image_height}")
    print(f"Label names: {class_names}")
    print(f"Label counts: {num_each}")
    if if_plot:
        plot_sample(image_files_list, image_class, class_names, image_files_list)



if __name__ == "__main__":
    preprocess(True)

import os
import json

from IPython.display import Image


def load_results(group_id, results_dir_path):
    results_file_name = group_id + ".json"
    results_file_path = os.path.join(results_dir_path, results_file_name)

    with open(results_file_path, "rb") as f:
        results = json.load(f)

    return results



def display_duplicated_images(group_id, images_dir_path, results_dir_path, first_n=5):
    results = load_results(group_id, results_dir_path)
    images_group_dir_path = os.path.join(images_dir_path, group_id)
    results_items = list(results.items())[:first_n]
    
    for base_image, duplicate_images_list in results_items:
        print(f"Base image: {base_image}")
        display(Image(filename=os.path.join(images_group_dir_path, base_image), width=200, height=200))
        
        for index, image in enumerate(duplicate_images_list):
            image_file_path = os.path.join(images_group_dir_path, image[0])
            print(f"Duplicated image {index+1} (similarity: {image[1] * 100:.2f}%): {image[0]}")
            display(Image(filename=image_file_path, width=200, height=200))
            
        print("##########################")
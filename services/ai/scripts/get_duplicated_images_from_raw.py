from src.constants import (
    RAW_DIR_PATH,
    INTERIM_DIR_PATH,
    PROCESSED_DIR_PATH
)

import os

from imagededup.methods import CNN

from src.data.utils import load_json_as_df, create_dir
from src.data.image_utils import download_images_from_group, delete_images_from_group
from src.models.dedup_model import find_duplicates

images_json_file_name = "images.json"
images_json_file_path = os.path.join(RAW_DIR_PATH, images_json_file_name)
images_dir_path = os.path.join(INTERIM_DIR_PATH, "images")
results_dir_path = os.path.join(PROCESSED_DIR_PATH, "dedup_results")


def process_group(encoder, images_df, group_id, images_dir_path, results_dir_path):
    download_images_from_group(images_df, group_id, images_dir_path)
    find_duplicates(encoder, group_id, images_dir_path, results_dir_path)
    delete_images_from_group(group_id, images_dir_path)

if __name__ == '__main__':
    
    images_df = load_json_as_df(images_json_file_path, index_col="image_id")
    
    groups = images_df["group_id"].unique().tolist()

    encoder = CNN()

    # loop over groups with concurrent executor
    for group_id in groups:
        print(f"Processing group {group_id}...")
        process_group(encoder, images_df, group_id, images_dir_path, results_dir_path)





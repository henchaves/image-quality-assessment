import os
import requests
import shutil
import pandas as pd

from tqdm.auto import tqdm

from src.data.utils import create_dir, delete_dir

def download_images_from_group(df: pd.DataFrame, group_id: int, images_dir_path: str) -> None:
    """
    Download all images from a group of images.

    Args:
        df (pandas.DataFrame): DataFrame with the images to download.
        group_id (int): Group ID.
        images_dir_path (str): Path to the directory where the images will be downloaded.
    
    Returns:
        None
    """

    images_group_dir_path = os.path.join(images_dir_path, group_id)
    create_dir(images_group_dir_path)

    images_group_df = df[df["group_id"] == group_id]

    for image_id, row in tqdm(images_group_df.iterrows()):
        image_url = row["image_url"]
        res = requests.get(image_url, stream=True)

        if res.status_code == 200:
            image_file_name = image_id + ".jpg"
            image_file_path = os.path.join(images_group_dir_path, image_file_name)

            with open(image_file_path, "wb") as f:
                res.raw.decode_content = True
                shutil.copyfileobj(res.raw, f)

def delete_images_from_group(group_id: int, images_dir_path: str) -> None:
    images_group_dir_path = os.path.join(images_dir_path, group_id)
    delete_dir(images_group_dir_path)
import os
import pymongo
import pandas as pd
import json
import random
from src.data.utils import load_json_as_df

from src.constants import (
    RAW_DIR_PATH,
)


def conect_mongo():
    DB_USERNAME = os.getenv("MONGO_USERNAME")
    DB_PASSWORD = os.getenv("MONGO_PASSWORD")
    DB_URL = os.getenv("MONGO_URL")
    DB_NAME = os.getenv("MONGO_DB")

    client = pymongo.MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/?retryWrites=true&w=majority")
    return client[DB_NAME]
   


def duplicated_random_images(db):
    collectionDuplicated = db["quality_assessment_results"]
    df = pd.DataFrame(collectionDuplicated.find())
    list_group_id = df.group_id.unique().tolist()
    
    random_group_id = random.randint(0, len(list_group_id)-1)
    list_image_ids = df[df["group_id"]==list_group_id[random_group_id]].image_id.tolist()


    chosed =random.sample(range(0, len(list_image_ids)-1), 2)
    del df['_id']
    return df[((df["image_id"]==list_image_ids[chosed[0]]) | (df["image_id"]==list_image_ids[chosed[1]])) & (df["group_id"] == list_group_id[random_group_id])]


def dataset_images():
    images_json_file_name = "images.json"
    images_json_file_path = os.path.join(RAW_DIR_PATH, images_json_file_name)
    return load_json_as_df(images_json_file_path, index_col="image_id")


















    
    
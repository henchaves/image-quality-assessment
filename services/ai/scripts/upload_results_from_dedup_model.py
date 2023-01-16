from src.constants import (
    RAW_DIR_PATH,
    PROCESSED_DIR_PATH
)

import os
import pymongo
import pandas as pd
from datetime import datetime as dt
from src.features.dedup_model import load_results

results_dir_path = os.path.join(PROCESSED_DIR_PATH, "dedup_results")

DB_USERNAME = os.getenv("MONGO_USERNAME")
DB_PASSWORD = os.getenv("MONGO_PASSWORD")
DB_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("MONGO_DB")

if __name__ == "__main__":
    client = pymongo.MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/?retryWrites=true&w=majority")

    db = client[DB_NAME]

    groups = [group[:-5] for group in os.listdir(results_dir_path) if group.endswith(".json")]

    for group_id in groups:
        print(f"Uploading results for group {group_id} ...")
        results = load_results(group_id)
        duplicate_images_df = pd.DataFrame(columns=["group_id", "base_image_id", "duplicated_image_id", "probability"])
        
        for base_image, duplicated_images in results.items():
            base_image_id = base_image.split(".")[0]
            for duplicated_image in duplicated_images:
              duplicated_image_id = duplicated_image[0].split(".")[0]
              probability = duplicated_image[1]
        
              row = {
                "group_id": group_id,
                "base_image_id": base_image_id,
                "duplicated_image_id": duplicated_image_id,
                "probability": probability
              }
        
              duplicate_images_df = duplicate_images_df.append(row, ignore_index=True)
        
        duplicates_dict = duplicate_images_df.to_dict("index")
        duplicates_array = [{"date": dt.utcnow(), **obj} for obj in duplicates_dict.values()]
        db["duplicated_images_model_results"].insert_many(duplicates_array)
      






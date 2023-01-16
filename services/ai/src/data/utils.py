import os
import json
import pandas as pd
import shutil

def load_json(json_file_path):
    with open(json_file_path, "rb") as f:
        json_ = json.load(f)
    return json_

def load_json_as_df(json_file_path, index_col=None):
    json_ = load_json(json_file_path)
    df = pd.DataFrame(json_)
    if index_col:
        df = df.set_index(index_col)
    return df

def create_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def delete_dir(dir_path):
    shutil.rmtree(dir_path)
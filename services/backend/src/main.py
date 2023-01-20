from fastapi import FastAPI,Response
import src.models as bd
import pandas as pd



app = FastAPI()


@app.get("/")
def home():
    return "Hello, World!"

@app.get("/pair_images")
def pair_images():
    db = bd.conect_mongo()
    duplicateds = bd.duplicated_random_images(db)
    images = bd.dataset_images()

    print(duplicateds.head())

    merged_group = pd.merge(left=images, right=duplicateds, left_on=['group_id','image_id'], right_on=['group_id','image_id'])
    del merged_group['mean_score_prediction']
    del merged_group['date']
    return Response(content = merged_group.to_json(orient="index"),media_type='application/json')
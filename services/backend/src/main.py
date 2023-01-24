from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
import src.models as bd
import src.models.post_result as pr
import pandas as pd
import json as json




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"

@app.get("/pair_images")
def pair_images():
    db = bd.conect_mongo()
    duplicateds = bd.duplicated_random_images(db)
    images = bd.dataset_images()
    score  = bd.get_score_duplicated(db,duplicateds['image_id'].iloc[0], duplicateds['image_id'].iloc[1],duplicateds['group_id'].iloc[1] )
    merged_group = pd.merge(left=images, right=duplicateds, left_on=['group_id','image_id'], right_on=['group_id','image_id'])
    parsedobject=json.loads(merged_group.to_json(orient="index"))
    compoundobject={'score':score,'images':parsedobject}
    return Response(content = json.dumps(compoundobject,indent=4),media_type='application/json')

@app.post("/human_result/")
async def create_item(item: pr.human_result):
    print("teste")
    return item
from fastapi import FastAPI,Response,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import src.models as bd
import pandas as pd
import src.models.post_result as pr
import json as json
import os




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

images = bd.dataset_images()



@app.get("/")
def home():
    return "Hello, World!"

@app.get("/pair_images")
def pair_images():
    try:
        DB_NAME = os.getenv("MONGO_DB")
        client = bd.conect_mongo()
        db = client[DB_NAME]
        duplicateds = bd.get_random_pair(db)
        print(duplicateds)
        quality_1  = bd.get_score_duplicated(db,duplicateds['base_image_id'], duplicateds['group_id'] )
        quality_2  = bd.get_score_duplicated(db,duplicateds['duplicated_image_id'], duplicateds['group_id'])
        union_dfs = pd.concat([quality_1, quality_2])
        merged_group = pd.merge(left=images, right=union_dfs, left_on=['group_id','image_id'], right_on=['group_id','image_id'])
        parsedobject=json.loads(merged_group.to_json(orient="index"))
        compoundobject={'score':duplicateds['probability'],'images':parsedobject}
        client.close()
        return Response(content = json.dumps(compoundobject,indent=4),media_type='application/json')
    except:
        raise HTTPException(status_code=404, detail="Unable to fetch quality")

@app.post("/human_result/")
async def create_item(item: pr.human_result):
    DB_NAME = os.getenv("MONGO_DB")
    client = bd.conect_mongo()
    db = client[DB_NAME] 
    bd.save_human_result(db,item)
    client.close()
    return "Result saved"
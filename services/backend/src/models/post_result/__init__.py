from typing import Union
from pydantic import BaseModel
import json

class human_result(BaseModel):
    image_1: str
    image_2: str
    duplicated : bool
    best_image: Union[str, None] = None
    group_id: str

    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
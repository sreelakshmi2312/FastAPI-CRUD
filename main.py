from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    id:int
    name:str
    price:float


items=[]

@app.get("/items",response_model=List[Item])
async def read_items():
    return items

@app.post("/items",response_model=Item)
async def post_items(item:Item):
    items.append(item)
    return item

@app.put("/items/{item_id}",response_model=Item)
async def update_items(item_id:int,item:Item):
    items[item_id]=item
    return item
@app.delete("/items/{item_id}")
async def delete_item(item_id:int):
    del items[item_id]
    return {"message":"item deleted"}
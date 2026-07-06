from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn 

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug"
)

#Define Item model
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

#Create in memory database to store items
items = {}

#Create an end point for get items
@app.get("/items")
def get_items():
    return list(items.values())

#Get Item filter by id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id)

#Create an end point for create items
@app.post("/items")
def create_item(item: Item):
    items[item.id] = item
    return item

#update item by id
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

#delete item by id
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    else:
        return {"message": "Item not found"}

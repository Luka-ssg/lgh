from fastapi import FastAPI
import uvicorn

# Create an instance of FastAPI
app = FastAPI()

# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Bye, luksuz!"}

# Define another route with a dynamic parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
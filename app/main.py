from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_root():
    # Test Function
    return {"message": "Hello World"}
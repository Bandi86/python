from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def root(request: Request) -> dict:
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    
    
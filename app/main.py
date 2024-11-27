from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello" : "CICD FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello" : "CICD FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)

#@app.post("/files/")
#async def batch_prediction(file: bytes = File(...)):
#    s=str(file,'utf-8')
#    data = StringIO(s)
#    df=pd.read_csv(data)
#    lst = df.values.tolist()
#    inference_request = {
#        "dataframe_records": lst
#    }
#    endpoint = 'http://localhost:1234/invocations'
#    response = requests.post(endpoint, json = inference_request)
#    print(response.text)
#    return response.text


from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"


# initialize fastapi instance
app = FastAPI()


# it initiates /docs which will give you first UI (User interface)
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")
# we want to give two routes.



# ROUTE 1: training the data by running "main.py" file.
@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    


# ROUTE 2: prediction route. Initializing prediction pipeline.
@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text # This will be shown as an output on your UI (User interface).
    except Exception as e:
        raise e
    


# initialize host and port using uvicorn.
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
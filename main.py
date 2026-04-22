from fastapi import FastAPI
from schemas import WicketProbInput, WicketProbOutput
from services import process_wicket_probability

app = FastAPI(title="Wicket Probability Model API V2")


@app.get("/")
def home():
    return {"message": "Wicket Probability API V2 running"}


@app.post("/bowling/wicket-probability", response_model=WicketProbOutput)
def wicket_probability(payload: WicketProbInput):
    return process_wicket_probability(payload)
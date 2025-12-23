from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve processed files
app.mount("/results", StaticFiles(directory="../processing"), name="results")

@app.get("/")
def root():
    return {"status": "Flood simulation ready"}

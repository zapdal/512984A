from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from BACKEND import IMG_PRED

app = FastAPI()
model=IMG_PRED()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/')
def rootpage():
    return 'This Project is made for checking tensorflow operation'


@app.get('/predict/')
async def predict(URL: str = Query(..., title="")):
    try:
        result=model.predict(url=URL)
    except Exception as e:
        result='OPERATION FAILED FOR {}'.format(e)
    return result
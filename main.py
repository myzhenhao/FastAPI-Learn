# uvicorn main:app --reload
# uvicorn main:app --host 0.0.0.0 --port 10000
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse
from routers import home

app = FastAPI()
   
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/home", status_code=status.HTTP_302_FOUND)

app.include_router(home.router)
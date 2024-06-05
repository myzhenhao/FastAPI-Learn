import sys
sys.path.append("..")
from starlette import status
from starlette.responses import RedirectResponse
from typing import Optional, Annotated
from fastapi import Depends, HTTPException, APIRouter, Request, Form
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/home",
    tags=["home"],
    responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/portfolio", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})

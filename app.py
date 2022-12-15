#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Juan Pablo Nahuelpán
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def login(request: Request):
#     stacked_email = "nada"
#     stacked_password = "nada"
#     return templates.TemplateResponse(
#         "login.html",
#         {
#             "request": request,
#             "stacked_email": stacked_email,
#             "stacked_password": stacked_password,
#             })

@app.post("/", response_class=HTMLResponse)
async def login(
    request: Request,
    stacked_email: str = Form(None),
    stacked_password: str = Form(0)):
    print(stacked_email, stacked_password)
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "stacked_email": stacked_email,
            "stacked_password": stacked_password,
            })

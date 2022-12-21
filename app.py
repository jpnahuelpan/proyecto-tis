#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Juan Pablo Nahuelpán
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
# modulos de la aplicación
from proyecto_tis import (
    create_connection,
    Query,
)
# configuración
import config



app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    stacked_email = ""
    stacked_password = ""
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "stacked_email": stacked_email,
            "stacked_password": stacked_password,
            })


@app.post("/", response_class=RedirectResponse)
async def validation(
    request: Request,
    stacked_email: str = Form(None),
    stacked_password: str = Form(0),
        ):

    print(stacked_email, stacked_password)
    con = create_connection(config.USER_DB)
    cursor = con.cursor()
    q = Query(cursor)
    email_registered = q.email_registered(stacked_email)
    if email_registered:
        id_pass = q.get_password_id(stacked_email)
        password = q.get_password(id_pass)
        if password == stacked_password:
            print("Acceso aprovado!")
            redirect_url = request.url_for('entry')
            print(redirect_url)
            return RedirectResponse(redirect_url)
    # else:
    #     return RedirectResponse("login")

    # return templates.TemplateResponse(
    #     "login.html",
    #     {
    #         "request": request,
    #         "stacked_email": stacked_email,
    #         "stacked_password": stacked_password,
    #         })


@app.post('/entry')
async def entry():
    return "Acceso aprovado!"

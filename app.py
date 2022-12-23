#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Juan Pablo Nahuelpán
from fastapi import FastAPI, Request, Form, status
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


@app.get("/login", response_class=HTMLResponse)
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


@app.post("/login", response_class=RedirectResponse)
async def validation(
    request: Request,
    stacked_email: str = Form(None),
    stacked_password: str = Form(0),
        ):

    print(stacked_email, stacked_password)
    con = create_connection(config.USER_DB)
    q = Query(con)
    email_registered = q.email_registered(stacked_email)
    if email_registered:
        id_pass = q.get_password_id_from_email(stacked_email)
        password = q.get_password(id_pass)
        if password == stacked_password:
            redirect_url = request.url_for('entry')
            print(redirect_url)
            return RedirectResponse(
                redirect_url,
                status_code=status.HTTP_303_SEE_OTHER,
                )
        else:
            redirect_url = request.url_for('olvido')
            return RedirectResponse(

            )
    else:
        redirect_url = request.url_for('register')
        return RedirectResponse(
            redirect_url,
            status_code=status.HTTP_303_SEE_OTHER,
            )


@app.get('/entry', response_class=HTMLResponse)
async def entry(request: Request):
    return templates.TemplateResponse(
        "principal.html",
        {
            "request": request,
            })


# @app.post('/ovido', response_class=RedirectResponse)
# async def olvido(request: Request):


@app.get('/register', response_class=HTMLResponse)
async def register_form(request: Request):
    user_name = ""
    a_paterno = ""
    a_materno = ""
    stacked_email = ""
    stacked_password = ""
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "user_name": user_name,
            "a_paterno": a_paterno,
            "a_materno": a_materno,
            "stacked_email": stacked_email,
            "stacked_password": stacked_password,
            })


@app.post("/register", response_class=RedirectResponse)
async def register(
    request: Request,
    user_name: str = Form(),
    a_paterno: str = Form(),
    a_materno: str = Form(),
    stacked_email: str = Form(),
    stacked_password: str = Form(),
        ):
    user_data = {
        "name": user_name,
        "a_paterno": a_paterno,
        "a_materno": a_materno,
        "email": stacked_email,
        "password": stacked_password,
    }
    print(user_data)
    con = create_connection(config.USER_DB)
    q = Query(con)
    q.insert_user(user_data)
    redirect_url = request.url_for('login')
    return RedirectResponse(
        redirect_url,
        status_code=status.HTTP_303_SEE_OTHER,
        )

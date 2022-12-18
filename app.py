#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Juan Pablo Nahuelpán
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
# modulos de la aplicación
from proyecto_tis import create_connection


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
    con = create_connection("db/BaseDeDatos.db")
    cursor = con.cursor()
    response = cursor.execute("select eMail from usuario;")
    response = response.fetchall()[0][0]
    print(f"Response: {response} stacked_email: {stacked_email}")
    if stacked_email == response:
        print("ya paso el fetchall")
        id_pass = cursor.execute(f"select UserId from usuario where eMail='{stacked_email}';")
        id_pass = id_pass.fetchall()[0][0]
        print(f"id pass = {id_pass}")
        password = cursor.execute(f"select password from password where idPass={id_pass};")
        password = password.fetchall()[0][0]
        print(f"id pass: {id_pass}, password: {password}")
        if stacked_password == password:
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

#!/usr/bin/python3
""" user and other random words unicycle, hedgefund, spaghetification"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

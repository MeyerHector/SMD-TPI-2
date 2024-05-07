import pandas as pd
from typing import Any, Dict
from fastapi import FastAPI
from controllers import get_category, get_country, get_rating, get_realese
app = FastAPI()

df = pd.read_csv('netflix.csv')

@app.get("/df_rating")
async def route_get_rating():
    return await get_rating()

@app.get("/df_category")
async def route_get_category():
    return await get_category()


@app.get("/df_country")
async def route_get_country():
    return await get_country()


@app.get("/df_realese")
async def route_get_realese():
    return await get_realese()
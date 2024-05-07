from fastapi import FastAPI
from controllers import get_category, get_country, get_rating, get_realese
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Tus rutas van aquí

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
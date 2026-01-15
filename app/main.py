import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.file_handler import read
from app.json_formatter import to_json
from app.router_daily_fee import router

app = FastAPI(
	title="PF - Financiamento imobiliário com taxas reguladas - Pós-fixado referenciado em TR", 
	description="API que disponibiliza os dados de relatorio do BCB no formato json",
	version="1.0.0"
	)
app.include_router(router=router)
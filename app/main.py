import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from file import read
from formatter import to_json
from router_daily_fee import read_actually

app = FastAPI(
	title="PF - Financiamento imobiliário com taxas reguladas - Pós-fixado referenciado em TR", 
	description="API que disponibiliza os dados de relatorio do BCB no formato json",
	version="1.0.0"
	)
app.include_router(router=read_actually)
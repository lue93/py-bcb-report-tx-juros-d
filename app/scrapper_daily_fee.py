import asyncio 
from pyppeteer import launch
from datetime import date, timedelta

from file_handler import write

async def main():
    """
    Esta funcão efetua o download do conteudo de taxas no formato json, consultando sempre pelo ano anterior no ultimo mes ao dia primeiro
    """

    browser = await launch(headless=True)
    page = await browser.newPage()
    data = f"{date.today().year - 1}-12-01"
    url = "https://www.bcb.gov.br/api/servico/sitebcb/historicotaxajurosdiario/atual?filtro=(codigoSegmento%20eq%20%271%27)%20and%20(codigoModalidade%20eq%20%27905201%27)%20and%20(InicioPeriodo%20eq%20%27"+ data +"%27)"
    await page.goto(url)

    content = await page.content() 
    text = await page.evaluate('document.querySelector("pre").innerText') 
    write(text)
        
    await browser.close()

# Executa o loop assíncrono 
asyncio.get_event_loop().run_until_complete(main())
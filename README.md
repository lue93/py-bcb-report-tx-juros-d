# py-bcb-report-tx-juros-d

Este projeto automatiza a coleta dos relatórios de taxas de juros disponibilizados pelo Banco Central do Brasil (BCB) e os expõe em formato **JSON** através de uma **API** construída com **FastAPI**. Assim, elimina-se a necessidade de acessar manualmente o site do BCB e baixar os dados.

Link do relatório: https://www.bcb.gov.br/estatisticas/reporttxjuros?codigoSegmento=1&codigoModalidade=903201&historicotaxajurosdiario_atual_page=1&tipoModalidade=M&InicioPeriodo=2025-12-01

### Requisição GET via CURL
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/historico-taxa-juros-diario/atual' \
  -H 'accept: application/json'
```

### Resposta
```bash
{
  "conteudo": [
    {
      "Posicao": 1,
      "InstituicaoFinanceira": "CAIXA ECONOMICA FEDERAL",
      "TaxaJurosAoMes": "0,63",
      "TaxaJurosAoAno": "7,86"
    },
    {
      "Posicao": 2,
      "InstituicaoFinanceira": "BCO DO BRASIL S.A.",
      "TaxaJurosAoMes": "0,70",
      "TaxaJurosAoAno": "8,78"
    },
    {
      "Posicao": 3,
      "InstituicaoFinanceira": "APE POUPEX",
      "TaxaJurosAoMes": "0,80",
      "TaxaJurosAoAno": "10,07"
    },
    {
      "Posicao": 4,
      "InstituicaoFinanceira": "BCO COOPERATIVO SICREDI S.A.",
      "TaxaJurosAoMes": "0,81",
      "TaxaJurosAoAno": "10,15"
    },
    {
      "Posicao": 5,
      "InstituicaoFinanceira": "BCO DO EST. DO PA S.A.",
      "TaxaJurosAoMes": "0,83",
      "TaxaJurosAoAno": "10,37"
    },
    {
      "Posicao": 6,
      "InstituicaoFinanceira": "BCO DO ESTADO DO RS S.A.",
      "TaxaJurosAoMes": "0,84",
      "TaxaJurosAoAno": "10,51"
    },
    {
      "Posicao": 7,
      "InstituicaoFinanceira": "BCO DO EST. DE SE S.A.",
      "TaxaJurosAoMes": "0,85",
      "TaxaJurosAoAno": "10,72"
    },
    {
      "Posicao": 8,
      "InstituicaoFinanceira": "BRB - BCO DE BRASILIA S.A.",
      "TaxaJurosAoMes": "0,87",
      "TaxaJurosAoAno": "10,90"
    },
    {
      "Posicao": 9,
      "InstituicaoFinanceira": "BCO BRADESCO S.A.",
      "TaxaJurosAoMes": "0,92",
      "TaxaJurosAoAno": "11,68"
    },
    {
      "Posicao": 10,
      "InstituicaoFinanceira": "ITAÚ UNIBANCO S.A.",
      "TaxaJurosAoMes": "0,94",
      "TaxaJurosAoAno": "11,85"
    },
    {
      "Posicao": 11,
      "InstituicaoFinanceira": "BCO BANESTES S.A.",
      "TaxaJurosAoMes": "0,96",
      "TaxaJurosAoAno": "12,18"
    },
    {
      "Posicao": 12,
      "InstituicaoFinanceira": "BCO SANTANDER (BRASIL) S.A.",
      "TaxaJurosAoMes": "0,97",
      "TaxaJurosAoAno": "12,31"
    }
  ]
}
```


### Acessar documentação
```bash
http://127.0.0.1:8000/docs
```

### Como executar o scrapper 
```bash
python3 app/scrapper_daily_fee.py 
```

### Como executar o servidor
```bash
uvicorn app.main:app --reload
```
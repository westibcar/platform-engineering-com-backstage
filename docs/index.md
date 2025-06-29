# Documentação do Uday App

Esta documentação tem como objetivo auxiliar na utilização do nosso aplicativo integrado ao Backstage.

## Propósito: Cadastro de Empresas

Você pode cadastrar empresas utilizando nossa interface gráfica ou via API.

### Interface Gráfica
Acesse:
[http://uday-app.uday.com.br/](http://uday-app.uday.com.br/)

### API para Cadastro de Empresas (Interface)
Endpoint:
```bash
/api/empresas
```

### API para Cadastro de Empresas (Commandline)
```bash
curl -X POST http://uday-app.uday.com.br/api/empresas \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "12345678000199", "nome": "Empresa Exemplo"}'
```

### Monitoramento dos Serviços
Disponibilizamos um endpoint para monitoramento da saúde dos serviços:
```bash 
/api/healthz
```
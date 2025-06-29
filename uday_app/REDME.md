### Para executar
```
bash python app.py
```

### ✅ Como testar a API

Via `curl` ou Postman:

```bash
curl -X POST http://localhost:5000/api/empresas \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "12345678000199", "nome": "Empresa Exemplo"}'
```

---

Se quiser, posso empacotar isso em um `.zip` ou gerar uma versão com banco de dados SQLite.

Quer seguir assim ou incluir banco de dados e autenticação também?

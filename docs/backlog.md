```markdown
# 📌 Backlog do Projeto (Cronograma de ~45 Dias)

## 🟡 Sprint 1: Setup & Estrutura Base (Dias 1 a 10)
- [x] Criar estrutura de pastas no GitHub (`app/`, `routers/`, etc.)
- [x] Criar e documentar `README.md`, `BACKLOG.md` e `.gitignore`
- [ ] Configurar conexão do SQLite no `database.py`
- [ ] Criar tabelas básicas no `models.py` (Receita e Ingrediente)

## 🔵 Sprint 2: Core de Receitas e Filtros (Dias 11 a 25)
- [ ] Criar endpoint `POST /recipes` (Cadastrar receita com ingredientes e tags)
- [ ] Criar endpoint `GET /recipes` (Listar receitas)
- [ ] Implementar filtro por restrições dietéticas (Query params por tags)

## 🟢 Sprint 3: Lista de Compras e Regras de Negócio (Dias 26 a 35)
- [ ] Criar endpoint `POST /shopping-list` (Recebe IDs de receitas e quantidade de porções)
- [ ] Lógica para somar e agrupar ingredientes duplicados
- [ ] Retornar o JSON consolidado da lista de compras
- [ ] Testes + documentação

## 🔴 Sprint 4: Front-end (Dias 36 a 45)
- [ ] Popular o banco com dados de teste (pelo menos 10 receitas variadas)
- [ ] Testar todos os endpoints pelo Swagger (`/docs`)
- [ ] Refinamentos finais

```markdown
# 📌 Backlog do Projeto (Cronograma 45 dias)

## 🟢 Sprint 1: Core Backend & Regras de Negócio — [CONCLUÍDA]
- [x] Configurar conexão do SQLite no `database.py` e tabelas no `models.py`
- [x] Criar endpoints de Receitas (`POST /recipes`, `GET /recipes`, `GET /recipes/{id}`)
- [x] Implementar filtro por restrições dietéticas (tags via query param)
- [x] Configurar CORS Middleware no `main.py`
- [x] Criar endpoint da Lista de Compras (`POST /shopping-list/`) com agregação de itens

## 🟡 Sprint 2: Carga de Dados Realistas & Interface Front-end (15 dias)
- [ ] Criar e executar o `seed.py` para popular o banco com 15+ receitas reais do cotidiano
- [ ] Criar a interface web (HTML/CSS/JS)
- [ ] Tela de Catalogo: Listagem de receitas com barra de busca e filtros por tags
- [ ] Tela de Detalhes: Exibição completa de ingredientes e modo de preparo
- [ ] Tela de Lista de Compras: Seleção de porções e geração do checklist consolidado

## 🔵 Sprint 3: Integração, Polimento & Finalização (15 dias)
- [ ] Conectar o Front-end à API (requisições via `fetch`)
- [ ] Ajustes visuais, responsividade e correção do `.gitignore`
- [ ] Testes finais de ponta a ponta e atualização do `README.md`

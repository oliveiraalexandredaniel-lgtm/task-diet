```markdown
# 📌 Backlog do Projeto (Cronograma 45 dias)

## 🟢 Sprint 1: Core Backend & Regras de Negócio — [CONCLUÍDA]
- [x] Configurar conexão do SQLite no `database.py` e tabelas no `models.py`
- [x] Criar endpoints de Receitas (`POST /recipes`, `GET /recipes`, `GET /recipes/{id}`)
- [x] Implementar filtro por restrições dietéticas (tags via query param)
- [x] Configurar CORS Middleware no `main.py`
- [x] Criar endpoint da Lista de Compras (`POST /shopping-list/`) com agregação de itens

## 🟡 Sprint 2: Carga de Dados Realistas & Interface Front-end (15 dias)
- [x] Criar e executar o `seed.py` para popular o banco com 15+ receitas reais do cotidiano
- [ ] Criar a interface web (HTML/CSS/JS)
- [ ] Tela de Catalogo: Listagem de receitas com barra de busca e filtros por tags
- [ ] Tela de Detalhes: Exibição completa de ingredientes e modo de preparo
- [ ] Tela de Lista de Compras: Seleção de porções e geração do checklist consolidado

## 🔵 Sprint 3: Integração, Polimento & Finalização (15 dias)
- [ ] Conectar o Front-end à API (requisições via `fetch`)
- [ ] Ajustes visuais, responsividade e correção do `.gitignore`
- [ ] Testes finais de ponta a ponta e atualização do `README.md`


US01 - Busca de Receitas por Tag (Restrição Alimentar)
-------------------------------------------------------------------------------
História:
  Como um usuário com restrição alimentar (ex: intolerante à lactose ou celíaco), 
  quero filtrar as receitas por "marcações" específicas 
  para encontrar apenas pratos seguros para a minha dieta.

Critérios de Aceite:
  - O sistema deve retornar apenas as receitas que contenham a tag selecionada 
    (ex: sem_lactose, sem_gluten, vegano, proteico).
  - Os filtros de tag devem ser acionados facilmente via botões/pílulas de seleção.

-------------------------------------------------------------------------------

US02 - Visualização do Modo de Preparo e Ingredientes
-------------------------------------------------------------------------------
História:
  Como um cozinheiro iniciante, 
  quero visualizar os ingredientes detalhados (quantidade e unidade) e o modo de preparo 
  para conseguir reproduzir a receita sem erros.

Critérios de Aceite:
  - Ao selecionar uma receita, a interface deve exibir a lista completa de ingredientes.
  - O modo de preparo (instruções) deve ser exibido com os passos claros.

-------------------------------------------------------------------------------

US03 - Pesquisa Livre por Nome ou Ingrediente
-------------------------------------------------------------------------------
História:
  Como um usuário buscando inspiração rápida, 
  quero pesquisar receitas digitando o nome do prato na barra de busca 
  para localizar o que desejo em poucos segundos.

Critérios de Aceite:
  - O campo de busca deve aceitar texto livre.
  - A API/Interface deve filtrar dinamicamente a lista de receitas correspondentes.

-------------------------------------------------------------------------------

US04 - Povoamento Automático do Banco de Dados (Seed)
-------------------------------------------------------------------------------
História:
  Como desenvolvedor/administrador da aplicação, 
  quero um script automatizado (seed.py) 
  para popular o banco de dados com receitas pré-definidas e categorizadas.

Critérios de Aceite:
  - O script deve limpar e repopular o banco de dados SQLite com receitas reais e completas.
  - Devem ser inseridas as relações de ingredientes, tags inclusivas e modo de preparo.

===============================================================================

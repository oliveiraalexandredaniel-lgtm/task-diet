# 🥗 Task-Diet - API de Receitas e Planejamento


## 💡 Definição do Problema & Ideação (resumidamente e no modelo do design thinking)

### 1. Definição do Problema
Pessoas com restrições alimentares (como intolerância a lactose, celíacos ou adeptos do veganismo) enfrentam dificuldades frequentes para encontrar receitas adequadas de forma rápida, segura e sem poluição visual. A maioria dos sites de culinária mistura pratos genéricos sem filtros eficientes por restrição, tornando a busca frustrante e demorada.

### 2. Ideação (A Solução)
O **Task Diet** foi idealizado como uma plataforma minimalista e intuitiva focada em:
- **Centralização por Tags:** Filtragem instantânea de receitas por necessidades específicas (Sem Glúten, Sem Lactose, Vegano, etc.).
- **Busca Rápida:** Localização de pratos por nome ou ingredientes em poucos cliques.
- **Experiência Limpa:** Interface direta ao ponto, destacando apenas o que importa (ingredientes e modo de preparo) sem distrações.

Você pode conferir o design e a experiência do usuário do **Task Diet** diretamente no Figma:
👉 [Acessar Protótipo Interativo no Figma](https://www.figma.com/make/Vnd0Xlh4g3PuFkEqVyTnek/Prototipo-aplicativo-receitas?p=f&t=kUcEqMCC9Mktrpkv-0&fullscreen=1)


> **TaskDiet** é uma API RESTful em Python (FastAPI) para planejamento de refeições, gestão de restrições alimentares e geração automatizada de listas de compras.
---

## 💡 Design Thinking

### 1. Definição do Problema
* Pessoas com restrições alimentares (ex: celíacos, intolerantes a lactose, veganos) perdem muito tempo procurando receitas adequadas.
* Dificuldade em planejar refeições semanais e converter receitas em uma lista de compras otimizada, gerando desperdício de alimentos e dinheiro.

### 2. Objetivo do Sistema
* Permitir o cadastro de receitas categorizadas por tags de restrições/dietas.
* Filtrar rapidamente refeições seguras para o perfil do usuário.
* Consolidação automática dos ingredientes de várias receitas em uma única lista de compras.

### 3. Solução Proposta (Backend/API)
* **API REST** para gerenciamento de receitas, usuários e planos de refeição.
* **Filtros por Tags:** Consulta rápida combinando múltiplas restrições.
* **Agregador de Ingredientes:** Lógica que soma quantidades e unifica itens para a lista de compras.

---

# 📋 Backlog do Produto & Registro das Sprints

Documentação das User Stories, prioridades, estimativas (story points) e cronograma das Sprints para o projeto **Task Diet**.

---

## 📌 Backlog do Produto

| Rank | Prioridade | User Story | Estimativa | Sprint |
| :---: | :---: | :--- | :---: | :---: |
| **1** | Alta | **Como desenvolvedor/administrador**, quero um script automatizado (`seed.py`) para popular o banco de dados com receitas pré-definidas e categorizadas. | 3 | 1 |
| **2** | Alta | **Como um usuário com restrição alimentar**, quero filtrar as receitas por tags específicas (ex: sem lactose, sem glúten, vegano) para encontrar apenas pratos seguros para minha dieta. | 5 | 2 |
| **3** | Média | **Como um usuário buscando inspiração rápida**, quero pesquisar receitas digitando o nome do prato ou ingrediente na barra de busca para localizar o que preciso em poucos segundos. | 5 | 2 |
| **4** | Média | **Como um cozinheiro iniciante**, quero visualizar os ingredientes detalhados (quantidade/unidade) e o modo de preparo completo para conseguir reproduzir a receita sem erros. | 5 | 3 |

---

## 📅 Registro das Sprints

| Sprint | Previsão | Status | Histórico / Entregas |
| :---: | :---: | :---: | :--- |
| **01** | 20/08/2026 | **Concluído** | Backend & Banco de Dados (API FastAPI, SQLite, Models, Schemas e Seed de dados) |
| **02** | 30/08/2026 | **Concluído** | Front-end Web & Integração com a API (Interface em HTML/CSS/JS, Busca e Filtros por Tags) |
| **03** | 10/09/2026 | **Concluído** | Detalhes da Receita (Modo de preparo, modal/cards expandidos e polimento visual final) |

---

*Nota: As estimativas utilizam a escala de Story Points baseada em Fibonacci.*

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Framework Web:** FastAPI
* **Banco de Dados:** SQLite (SQLAlchemy ORM)
* **Validação de Dados:** Pydantic

## Arquitetura e Estrutura dos Arquivos

A API segue a separação de responsabilidades para garantir um código limpo e de fácil manutenção:

* **`main.py` (Mapeamento de Rotas):** Ponto de entrada da aplicação onde o FastAPI é inicializado e as rotas (`GET`, `POST`) são definidas.
* **`app/schemas.py` (Validadores de Dados):** Contém as classes Pydantic que definem o formato dos dados de entrada e saída (Inputs/Outputs) exigidos e retornados pela API.
* **`app/models.py` (Mapeamento de Banco de Dados):** Contém as entidades ORM do SQLAlchemy que definem a estrutura física das tabelas no banco de dados SQLite.
* **`app/database.py` (Conexão com Banco):** Gerencia a engine de conexão com o SQLite e provê as sessões (`get_db`) de comunicação com o banco.
* **Uvicorn (Servidor ASGI):** Ferramenta externa responsável por subir o servidor Web e disponibilizar a API e a documentação Swagger na porta local (ex: `:8000`).

---

Para iniciar o servidor localmente, execute no terminal:

python -m app.seed

uvicorn app.main:app --reload

---

## 🚀 Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/oliveiraalexandredaniel-lgtm/task-diet.git
   cd task-diet

   http://127.0.0.1:8000/docs (servidor)

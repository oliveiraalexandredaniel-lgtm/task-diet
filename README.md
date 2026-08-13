# 🥗 Task-Diet - API de Receitas e Planejamento


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

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Framework Web:** FastAPI
* **Banco de Dados:** SQLite (SQLAlchemy ORM)
* **Validação de Dados:** Pydantic

---

## 🚀 Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)](https://github.com/oliveiraalexandredaniel-lgtm/task-diet.git)
   cd seu-repositorio

   http://127.0.0.1:8000/docs (servidor)

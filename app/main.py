# main.py
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Ingredient, Recipe
from app.schemas import RecipeCreate, RecipeResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite requisições vindas do Live Server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Libera acesso para qualquer origem em desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Cria as tabelas do banco no arranque
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Receitas - Projeto")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições do front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Rota para Cadastrar Receita com Ingredientes
@app.post(
    "/recipes/",
    response_model=RecipeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    # Criar a instância da receita
    db_recipe = Recipe(
        title=recipe.title, prep_time=recipe.prep_time, tags=recipe.tags
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # Inserir os ingredientes vinculados ao ID da receita criada
    for ing in recipe.ingredients:
        db_ingredient = Ingredient(
            name=ing.name,
            amount=ing.amount,
            unit=ing.unit,
            recipe_id=db_recipe.id,
        )
        db.add(db_ingredient)

    db.commit()
    db.refresh(db_recipe)
    return db_recipe


# 2. Rota para Listar Receitas com Filtro de Restrições
@app.get("/recipes/", response_model=List[RecipeResponse])
def list_recipes(
    tag: Optional[str] = Query(
        None, description="Filtrar por tag (ex: vegano)"
    ),
    db: Session = Depends(get_db),
):
    query = db.query(Recipe)
    if tag:
        # Busca simples por substring na coluna de tags
        query = query.filter(Recipe.tags.contains(tag))

    return query.all()

from app.schemas import ConsolidatedIngredient, ShoppingListRequest


# 3. Rota para Buscar Receita por ID
@app.get("/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receita não encontrada",
        )
    return recipe


# 4. Rota para Gerar Lista de Compras Consolidada (US04)
@app.post(
    "/shopping-list/", response_model=List[ConsolidatedIngredient]
)
def generate_shopping_list(
    payload: ShoppingListRequest, db: Session = Depends(get_db)
):
    consolidated = {}

    for item in payload.items:
        recipe = db.query(Recipe).filter(Recipe.id == item.recipe_id).first()
        if not recipe:
            continue

        for ing in recipe.ingredients:
            # Chave única para agrupar pelo nome e unidade de medida
            key = (ing.name.strip().lower(), ing.unit.strip().lower())
            total_amount = ing.amount * item.servings

            if key in consolidated:
                consolidated[key]["amount"] += total_amount
            else:
                consolidated[key] = {
                    "name": ing.name,
                    "amount": total_amount,
                    "unit": ing.unit,
                }

    return list(consolidated.values())
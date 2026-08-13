# main.py
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Ingredient, Recipe
from app.schemas import RecipeCreate, RecipeResponse

# Cria as tabelas do banco no arranque
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Receitas - Projeto")


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
# app/schemas.py
from typing import List, Optional
from pydantic import BaseModel


class IngredientCreate(BaseModel):
    name: str
    amount: float
    unit: str


class IngredientResponse(IngredientCreate):
    id: int

    class Config:
        from_attributes = True


class RecipeCreate(BaseModel):
    title: str
    prep_time: int
    tags: Optional[str] = ""  # Ex: "vegano,sem_gluten"
    ingredients: List[IngredientCreate]


class RecipeResponse(BaseModel):
    id: int
    title: str
    prep_time: int
    tags: Optional[str]
    ingredients: List[IngredientResponse]

    class Config:
        from_attributes = True
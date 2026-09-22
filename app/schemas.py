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
    tags: Optional[str] = ""
    instructions: Optional[str] = None
    image_url: Optional[str] = None
    ingredients: List[IngredientCreate]


class RecipeResponse(BaseModel):
    id: int
    title: str
    prep_time: int
    tags: Optional[str]
    instructions: Optional[str] = None
    image_url: Optional[str] = None
    ingredients: List[IngredientResponse]

    class Config:
        from_attributes = True


# Schemas para Lista de Compras
class RecipeItemRequest(BaseModel):
    recipe_id: int
    servings: int = 1


class ShoppingListRequest(BaseModel):
    items: List[RecipeItemRequest]


class ConsolidatedIngredient(BaseModel):
    name: str
    amount: float
    unit: str
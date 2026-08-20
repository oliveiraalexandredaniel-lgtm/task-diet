from app.database import Base, SessionLocal, engine
from app.models import Ingredient, Recipe


def popular_banco():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print("🧹 Limpando dados antigos...")
    db.query(Ingredient).delete()
    db.query(Recipe).delete()
    db.commit()

    receitas_reais = [
        {
            "title": "Strogonoff de Frango Sem Lactose",
            "prep_time": 30,
            "tags": "sem_lactose, sem_gluten, proteico, rapido, sem_oleaginosas",
            "instructions": "1. Sove o frango e doure no azeite com a cebola.\n2. Adicione o molho de tomate, ketchup e mostarda.\n3. Desligue o fogo e misture o creme de leite de aveia/soja.",
            "ingredients": [
                {"name": "Peito de Frango", "amount": 500, "unit": "g"},
                {"name": "Creme de Leite de Aveia (Sem Glúten)", "amount": 200, "unit": "g"},
                {"name": "Molho de Tomate", "amount": 100, "unit": "g"},
                {"name": "Ketchup", "amount": 2, "unit": "colher de sopa"},
                {"name": "Mostarda", "amount": 1, "unit": "colher de sopa"},
                {"name": "Cebola", "amount": 1, "unit": "unidade"},
                {"name": "Azeite", "amount": 15, "unit": "ml"},
            ],
        },
        {
            "title": "Salada Fit de Grão-de-Bico",
            "prep_time": 15,
            "tags": "vegano, sem_lactose, sem_gluten, sem_acucar, baixo_sodio, fit, rapido, kosher, halal",
            "instructions": "1. Misture o grão-de-bico com os legumes picados.\n2. Tempere com azeite, limão e ervas finas.\n3. Sirva frio.",
            "ingredients": [
                {"name": "Grão-de-Bico Cozido", "amount": 300, "unit": "g"},
                {"name": "Tomate Picado", "amount": 2, "unit": "unidade"},
                {"name": "Pepino Picado", "amount": 1, "unit": "unidade"},
                {"name": "Azeite de Oliva", "amount": 20, "unit": "ml"},
                {"name": "Suco de Limão", "amount": 1, "unit": "unidade"},
            ],
        },
        {
            "title": "Omelete de Espinafre e Frango",
            "prep_time": 10,
            "tags": "proteico, rapido, sem_lactose, sem_gluten, sem_acucar, low_fodmap, baixo_sodio",
            "instructions": "1. Bata os ovos com uma pitada leve de sal.\n2. Refogue o espinafre e frango desfiado.\n3. Despeje os ovos na frigideira antiaderente até dourar ambos os lados.",
            "ingredients": [
                {"name": "Ovo", "amount": 3, "unit": "unidade"},
                {"name": "Folhas de Espinafre", "amount": 50, "unit": "g"},
                {"name": "Frango Desfiado", "amount": 60, "unit": "g"},
                {"name": "Azeite", "amount": 5, "unit": "ml"},
            ],
        },
        {
            "title": "Sopa de Legumes com Músculo",
            "prep_time": 40,
            "tags": "sem_lactose, sem_gluten, sem_acucar, baixo_sodio, sem_oleaginosas, marmita",
            "instructions": "1. Cozinhe a carne na pressão por 20 min.\n2. Adicione os legumes picados e cozinhe por mais 15 min.\n3. Ajuste o sal com moderação e sirva quente.",
            "ingredients": [
                {"name": "Músculo Bovino", "amount": 300, "unit": "g"},
                {"name": "Cenoura", "amount": 2, "unit": "unidade"},
                {"name": "Batata", "amount": 2, "unit": "unidade"},
                {"name": "Chuchu", "amount": 1, "unit": "unidade"},
            ],
        },
        {
            "title": "Panqueca de Banana e Aveia",
            "prep_time": 10,
            "tags": "vegetariano, sem_lactose, sem_acucar, fit, rapido, sem_oleaginosas",
            "instructions": "1. Amasse a banana e misture com o ovo e aveia.\n2. Despeje pequenas porções numa frigideira untada.\n3. Dobre e polvilhe canela a gosto.",
            "ingredients": [
                {"name": "Banana Madura", "amount": 1, "unit": "unidade"},
                {"name": "Ovo", "amount": 1, "unit": "unidade"},
                {"name": "Farelo de Aveia", "amount": 30, "unit": "g"},
                {"name": "Canela em Pó", "amount": 2, "unit": "g"},
            ],
        },
        {
            "title": "Frango ao Molho de Mostarda e Ervas",
            "prep_time": 20,
            "tags": "proteico, sem_gluten, sem_lactose, sem_acucar, fit, sem_oleaginosas",
            "instructions": "1. Grelhe os filés de frango temperados.\n2. Em uma panela separada, aqueça a mostarda amarela com ervas e um pouco de água.\n3. Regue o frango e sirva.",
            "ingredients": [
                {"name": "Filé de Peito de Frango", "amount": 400, "unit": "g"},
                {"name": "Mostarda Yellow", "amount": 2, "unit": "colher de sopa"},
                {"name": "Azeite", "amount": 10, "unit": "ml"},
            ],
        },
        {
            "title": "Lasanha de Berinjela Low Carb",
            "prep_time": 45,
            "tags": "vegetariano, sem_gluten, sem_acucar, low_carb, sem_oleaginosas",
            "instructions": "1. Grelhe as fatias de berinjela.\n2. Monte camadas alternando berinjela, molho de tomate e queijo zero lactose.\n3. Leve ao forno a 180°C por 20 minutos.",
            "ingredients": [
                {"name": "Berinjela Fatiada", "amount": 2, "unit": "unidade"},
                {"name": "Molho de Tomate Caseiro", "amount": 300, "unit": "g"},
                {"name": "Queijo Muçarela Zero Lactose", "amount": 200, "unit": "g"},
            ],
        },
        {
            "title": "Tofu Xadrez com Pimentões",
            "prep_time": 25,
            "tags": "vegano, sem_lactose, sem_gluten, sem_acucar, fit, kosher, halal",
            "instructions": "1. Doure o tofu em cubos no azeite de gergelim.\n2. Adicione pimentões e refogue rapidamente para manter a crocância.\n3. Adicione o shoyu e misture bem.",
            "ingredients": [
                {"name": "Tofu em Cubos", "amount": 300, "unit": "g"},
                {"name": "Pimentão Vermelho", "amount": 1, "unit": "unidade"},
                {"name": "Pimentão Amarelo", "amount": 1, "unit": "unidade"},
                {"name": "Molho Shoyu Sem Glúten", "amount": 30, "unit": "ml"},
            ],
        },
        {
            "title": "Tapioca com Frango e Requeijão Zero Lactose",
            "prep_time": 10,
            "tags": "sem_gluten, sem_lactose, rapido, proteico, sem_oleaginosas",
            "instructions": "1. Peneire a tapioca em frigideira bem quente.\n2. Adicione o frango desfiado com requeijão zero lactose.\n3. Dobrar e servir quente.",
            "ingredients": [
                {"name": "Goma de Tapioca", "amount": 80, "unit": "g"},
                {"name": "Frango Desfiado Temperado", "amount": 100, "unit": "g"},
                {"name": "Requeijão Zero Lactose", "amount": 30, "unit": "g"},
            ],
        },
        {
            "title": "Creme de Abóbora e Gengibre",
            "prep_time": 25,
            "tags": "vegano, sem_lactose, sem_gluten, sem_acucar, baixo_sodio, fit, low_fodmap, rapido",
            "instructions": "1. Cozinhe a abóbora até amaciar totalmente.\n2. Bata no liquidificador com o gengibre e azeite.\n3. Aqueça por 3 minutos e sirva com ervas.",
            "ingredients": [
                {"name": "Abóbora Japonesa", "amount": 500, "unit": "g"},
                {"name": "Gengibre Ralado", "amount": 10, "unit": "g"},
                {"name": "Azeite", "amount": 15, "unit": "ml"},
            ],
        },
    ]

    for dados in receitas_reais:
        receita = Recipe(
            title=dados["title"],
            prep_time=dados["prep_time"],
            tags=dados["tags"],
            instructions=dados["instructions"],
        )
        db.add(receita)
        db.commit()
        db.refresh(receita)

        for ing in dados["ingredients"]:
            ingrediente = Ingredient(
                name=ing["name"],
                amount=ing["amount"],
                unit=ing["unit"],
                recipe_id=receita.id,
            )
            db.add(ingrediente)

    db.commit()
    print("✅ Banco atualizado com tags inclusivas e modo de preparo!")
    db.close()


if __name__ == "__main__":
    popular_banco()
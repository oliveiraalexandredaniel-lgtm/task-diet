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
        # --- As 10 Primeiras ---
        {
            "title": "Strogonoff de Frango Sem Lactose",
            "prep_time": 30,
            "tags": "sem_lactose, sem_gluten, proteico, rapido, sem_oleaginosas",
            "instructions": "1. Sove o frango e doure no azeite com a cebola.\n2. Adicione o molho de tomate, ketchup e mostarda.\n3. Desligue o fogo e misture o creme de leite de aveia/soja.",
            "image_url": "https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1510693206972-df098062cb71?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1572449043416-55f4685c9bb7?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=600&q=80",
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
            "image_url": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Abóbora Japonesa", "amount": 500, "unit": "g"},
                {"name": "Gengibre Ralado", "amount": 10, "unit": "g"},
                {"name": "Azeite", "amount": 15, "unit": "ml"},
            ],
        },

        # --- Novos Pratos Adicionados (11 a 20) ---
        {
            "title": "Salmão Grelhado com Salada Verde",
            "prep_time": 20,
            "tags": "proteico, sem_gluten, sem_lactose, low_carb, fit, rapido",
            "instructions": "1. Tempere as postas de salmão com limão e ervas.\n2. Grelhe numa frigideira com azeite por 4 minutos de cada lado.\n3. Sirva acompanhado de mix de folhas verdes.",
            "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Posta de Salmão", "amount": 300, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 10, "unit": "ml"},
                {"name": "Mix de Folhas Verdes", "amount": 100, "unit": "g"},
                {"name": "Limão", "amount": 1, "unit": "unidade"},
            ],
        },
        {
            "title": "Moqueca Vegana de Caju e Palmito",
            "prep_time": 35,
            "tags": "vegano, sem_lactose, sem_gluten, sem_acucar, sem_oleaginosas",
            "instructions": "1. Refogue a cebola, alho, pimentões e tomates.\n2. Adicione o palmito, o caju e o leite de coco.\n3. Cozinhe por 15 minutos em fogo baixo e finalize com coentro.",
            "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Palmito Pupunha em Rodelas", "amount": 300, "unit": "g"},
                {"name": "Caju Fatiado", "amount": 2, "unit": "unidade"},
                {"name": "Leite de Coco", "amount": 200, "unit": "ml"},
                {"name": "Pimentão Vermelho", "amount": 1, "unit": "unidade"},
                {"name": "Azeite de Dendê", "amount": 10, "unit": "ml"},
            ],
        },
        {
            "title": "Poke de Atum Fresco e Abacate",
            "prep_time": 15,
            "tags": "proteico, sem_lactose, sem_gluten, fit, rapido, low_carb",
            "instructions": "1. Corte o atum fresco e o abacate em cubos.\n2. Monte a tigela com base de pepino ou arroz de couve-flor.\n3. Tempere com shoyu sem glúten e gergelim.",
            "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Atum Fresco", "amount": 200, "unit": "g"},
                {"name": "Abacate", "amount": 100, "unit": "g"},
                {"name": "Pepino Japonês", "amount": 1, "unit": "unidade"},
                {"name": "Sementes de Gergelim", "amount": 10, "unit": "g"},
                {"name": "Shoyu Sem Glúten", "amount": 15, "unit": "ml"},
            ],
        },
        {
            "title": "Hambúrguer de Lentilha e Aveia",
            "prep_time": 30,
            "tags": "vegano, vegetariano, sem_lactose, fit, sem_oleaginosas",
            "instructions": "1. Processe a lentilha cozida com temperos e aveia até dar ponto de moldar.\n2. Forme os hambúrgueres e doure na frigideira com azeite por 5 min de cada lado.",
            "image_url": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Lentilha Cozida", "amount": 300, "unit": "g"},
                {"name": "Farelo de Aveia", "amount": 50, "unit": "g"},
                {"name": "Cebola Picada", "amount": 1, "unit": "unidade"},
                {"name": "Alho", "amount": 2, "unit": "dente"},
                {"name": "Azeite de Oliva", "amount": 10, "unit": "ml"},
            ],
        },
        {
            "title": "Risoto Fit de Couve-Flor com Cogumelos",
            "prep_time": 20,
            "tags": "vegetariano, low_carb, sem_gluten, sem_lactose, fit, rapido",
            "instructions": "1. Triture a couve-flor até ficar do tamanho de grãos de arroz.\n2. Refogue os cogumelos no azeite com alho.\n3. Adicione a couve-flor e cozinhe por 5 minutos até amaciar.",
            "image_url": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Couve-Flor Processada", "amount": 400, "unit": "g"},
                {"name": "Cogumelo Shimeji ou Paris", "amount": 200, "unit": "g"},
                {"name": "Alho-Poró Picado", "amount": 50, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
            ],
        },
        {
            "title": "Smoothie Bowl de Açaí sem Açúcar",
            "prep_time": 5,
            "tags": "vegano, sem_lactose, sem_gluten, sem_acucar, rapido, fit",
            "instructions": "1. Bata a polpa de açaí puro com a banana congelada até obter textura cremosa.\n2. Sirva na tigela e decore com morangos e sementes de chia.",
            "image_url": "https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Polpa de Açaí Puro (Sem Açúcar)", "amount": 200, "unit": "g"},
                {"name": "Banana Congelada", "amount": 1, "unit": "unidade"},
                {"name": "Morango Fatiado", "amount": 50, "unit": "g"},
                {"name": "Sementes de Chia", "amount": 10, "unit": "g"},
            ],
        },
        {
            "title": "Escondidinho de Batata-Doce com Frango",
            "prep_time": 35,
            "tags": "proteico, sem_lactose, sem_gluten, fit, marmita, sem_oleaginosas",
            "instructions": "1. Amasse a batata-doce cozida até virar purê.\n2. Monte em um refratário uma camada de frango desfiado temperado e cubra com o purê.\n3. Leve ao forno por 15 minutos para dourar.",
            "image_url": "https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Batata-Doce Cozida", "amount": 400, "unit": "g"},
                {"name": "Frango Desfiado Temperado", "amount": 300, "unit": "g"},
                {"name": "Azeite", "amount": 10, "unit": "ml"},
            ],
        },
        {
            "title": "Wrap Integral de Peito de Peru e Horta",
            "prep_time": 10,
            "tags": "rapido, proteico, sem_lactose, fit",
            "instructions": "1. Abra a massa de wrap integral.\n2. Espalhe alface, tomate, cenoura ralada e peito de peru.\n3. Enrole firmemente e corte ao meio.",
            "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Massa de Wrap Integral", "amount": 1, "unit": "unidade"},
                {"name": "Peito de Peru Fatiado", "amount": 60, "unit": "g"},
                {"name": "Almôndega de Alface", "amount": 30, "unit": "g"},
                {"name": "Cenoura Ralada", "amount": 30, "unit": "g"},
            ],
        },
        {
            "title": "Cuscuz Marroquino com Legumes Grelhados",
            "prep_time": 15,
            "tags": "vegano, vegetariano, sem_lactose, rapido, fit",
            "instructions": "1. Hidrate o cuscuz marroquino com água fervente por 5 minutos.\n2. Grelhe abobrinha, pimentão e berinjela em cubos.\n3. Solte o cuscuz com um garfo e misture os legumes com azeite.",
            "image_url": "https://images.unsplash.com/photo-1541518763669-27fef04b14e8?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Cuscuz Marroquino", "amount": 150, "unit": "g"},
                {"name": "Abobrinha em Cubos", "amount": 100, "unit": "g"},
                {"name": "Pimentão Amarelo", "amount": 50, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
            ],
        },
        {
            "title": "Mingau Proteico de Aveia e Cacau",
            "prep_time": 10,
            "tags": "vegetariano, proteico, sem_lactose, sem_acucar, rapido, fit",
            "instructions": "1. Cozinhe a aveia no leite vegetal até engrossar.\n2. Misture o cacau em pó e a proteína (whey/plant-based).\n3. Sirva morno com rodelas de banana por cima.",
            "image_url": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Aveia em Flocos", "amount": 40, "unit": "g"},
                {"name": "Leite de Amêndoas/Soja", "amount": 200, "unit": "ml"},
                {"name": "Cacau em Pó 100%", "amount": 10, "unit": "g"},
                {"name": "Banana Madura", "amount": 0.5, "unit": "unidade"},
            ],
        },
    ]

    for dados in receitas_reais:
        receita = Recipe(
            title=dados["title"],
            prep_time=dados["prep_time"],
            tags=dados["tags"],
            instructions=dados["instructions"],
            image_url=dados.get("image_url"),
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
    print("✅ Banco atualizado com sucesso! Total de 20 receitas cadastradas.")
    db.close()


if __name__ == "__main__":
    popular_banco()
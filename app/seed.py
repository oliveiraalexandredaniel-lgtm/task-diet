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
        # 1
        {
            "title": "Strogonoff de Frango Sem Lactose",
            "prep_time": 30,
            "tags": "sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, proteico, rapido, sem_oleaginosas",
            "instructions": "1. Selar o frango e dourar no azeite com a cebola.\n2. Adicionar o molho de tomate, ketchup e mostarda.\n3. Misturar o creme de leite vegetal e servir.",
            "image_url": "https://images.unsplash.com/photo-1534939561126-855b8675edd7?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Peito de Frango", "amount": 500, "unit": "g"},
                {"name": "Creme de Leite de Aveia", "amount": 200, "unit": "g"},
                {"name": "Molho de Tomate", "amount": 100, "unit": "g"},
                {"name": "Ketchup", "amount": 2, "unit": "colher de sopa"},
                {"name": "Mostarda", "amount": 1, "unit": "colher de sopa"},
                {"name": "Cebola", "amount": 1, "unit": "unidade"},
                {"name": "Azeite", "amount": 15, "unit": "ml"},
            ],
        },
        # 2
        {
            "title": "Salada Fit de Grão-de-Bico",
            "prep_time": 15,
            "tags": "vegano, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, sem_acucar, sem açúcar, fit, rapido, kosher, halal",
            "instructions": "1. Misturar o grão-de-bico com os legumes picados.\n2. Temperar com azeite, limão e ervas finas.\n3. Servir frio.",
            "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Grão-de-Bico Cozido", "amount": 300, "unit": "g"},
                {"name": "Tomate Picado", "amount": 2, "unit": "unidade"},
                {"name": "Pepino Picado", "amount": 1, "unit": "unidade"},
                {"name": "Azeite de Oliva", "amount": 20, "unit": "ml"},
                {"name": "Suco de Limão", "amount": 1, "unit": "unidade"},
            ],
        },
        # 3
        {
            "title": "Omelete de Espinafre e Frango",
            "prep_time": 10,
            "tags": "proteico, rapido, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, sem_acucar, sem açúcar",
            "instructions": "1. Bater os ovos.\n2. Refogar o espinafre e frango.\n3. Despejar os ovos na frigideira e dourar ambos os lados.",
            "image_url": "https://images.unsplash.com/photo-1510693206972-df098062cb71?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Ovo", "amount": 3, "unit": "unidade"},
                {"name": "Espinafre", "amount": 50, "unit": "g"},
                {"name": "Frango Desfiado", "amount": 60, "unit": "g"},
                {"name": "Azeite", "amount": 5, "unit": "ml"},
            ],
        },
        # 4
        {
            "title": "Sopa de Legumes com Músculo",
            "prep_time": 40,
            "tags": "sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, sem_acucar, sem açúcar, marmita",
            "instructions": "1. Cozinhar a carne na pressão por 20 min.\n2. Adicionar os legumes e cozinhar por mais 15 min.\n3. Ajustar o sal e servir quente.",
            "image_url": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Músculo Bovino", "amount": 300, "unit": "g"},
                {"name": "Cenoura", "amount": 2, "unit": "unidade"},
                {"name": "Batata", "amount": 2, "unit": "unidade"},
                {"name": "Chuchu", "amount": 1, "unit": "unidade"},
            ],
        },
        # 5
        {
            "title": "Panqueca de Banana e Aveia",
            "prep_time": 10,
            "tags": "vegetariano, sem_lactose, sem lactose, sem_acucar, sem açúcar, fit, rapido",
            "instructions": "1. Amassar a banana e misturar com ovo e aveia.\n2. Grelhar porções numa frigideira untada.\n3. Polvilhar canela e servir.",
            "image_url": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Banana Madura", "amount": 1, "unit": "unidade"},
                {"name": "Ovo", "amount": 1, "unit": "unidade"},
                {"name": "Farelo de Aveia", "amount": 30, "unit": "g"},
                {"name": "Canela em Pó", "amount": 2, "unit": "g"},
            ],
        },
        # 6
        {
            "title": "Frango ao Molho de Mostarda e Ervas",
            "prep_time": 20,
            "tags": "proteico, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit",
            "instructions": "1. Grelhar os filés de frango.\n2. Aquecer a mostarda com ervas e um pouco de água.\n3. Regar o frango e servir.",
            "image_url": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Filé de Peito de Frango", "amount": 400, "unit": "g"},
                {"name": "Mostarda Yellow", "amount": 2, "unit": "colher de sopa"},
                {"name": "Azeite", "amount": 10, "unit": "ml"},
            ],
        },
        # 7
        {
            "title": "Lasanha de Berinjela Low Carb",
            "prep_time": 45,
            "tags": "vegetariano, sem_gluten, sem gluten, sem glúten, low_carb, low carb",
            "instructions": "1. Grelhar as fatias de berinjela.\n2. Alternar camadas de berinjela, molho e queijo zero lactose.\n3. Assar a 180°C por 20 min.",
            "image_url": "https://images.unsplash.com/photo-1572449043416-55f4685c9bb7?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Berinjela Fatiada", "amount": 2, "unit": "unidade"},
                {"name": "Molho de Tomate", "amount": 300, "unit": "g"},
                {"name": "Queijo Muçarela Zero Lactose", "amount": 200, "unit": "g"},
            ],
        },
        # 8
        {
            "title": "Tofu Xadrez com Pimentões",
            "prep_time": 25,
            "tags": "vegano, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, fit",
            "instructions": "1. Dourar o tofu em cubos.\n2. Adicionar pimentões e refogar rapidamente.\n3. Misturar o shoyu sem glúten e servir.",
            "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Tofu em Cubos", "amount": 300, "unit": "g"},
                {"name": "Pimentão Vermelho", "amount": 1, "unit": "unidade"},
                {"name": "Pimentão Amarelo", "amount": 1, "unit": "unidade"},
                {"name": "Shoyu Sem Glúten", "amount": 30, "unit": "ml"},
            ],
        },
        # 9
        {
            "title": "Tapioca com Frango e Requeijão Zero Lactose",
            "prep_time": 10,
            "tags": "sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, proteico, rapido",
            "instructions": "1. Peneirar a goma na frigideira quente.\n2. Rechear com frango e requeijão zero lactose.\n3. Dobrar e servir.",
            "image_url": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Goma de Tapioca", "amount": 80, "unit": "g"},
                {"name": "Frango Desfiado", "amount": 100, "unit": "g"},
                {"name": "Requeijão Zero Lactose", "amount": 30, "unit": "g"},
            ],
        },
        # 10
        {
            "title": "Creme de Abóbora e Gengibre",
            "prep_time": 25,
            "tags": "vegano, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, fit, rapido",
            "instructions": "1. Cozinhar a abóbora até amaciar.\n2. Bater com gengibre e azeite.\n3. Aquecer e servir.",
            "image_url": "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Abóbora Japonesa", "amount": 500, "unit": "g"},
                {"name": "Gengibre Ralado", "amount": 10, "unit": "g"},
                {"name": "Azeite", "amount": 15, "unit": "ml"},
            ],
        },
        # 11
        {
            "title": "Salmão Grelhado com Salada Verde",
            "prep_time": 20,
            "tags": "proteico, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, low_carb, low carb, fit, rapido",
            "instructions": "1. Temperar o salmão com limão e sal.\n2. Grelhar por 4 minutos de cada lado.\n3. Servir com o mix de folhas.",
            "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Posta de Salmão", "amount": 300, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 10, "unit": "ml"},
                {"name": "Mix de Folhas Verdes", "amount": 100, "unit": "g"},
                {"name": "Limão", "amount": 1, "unit": "unidade"},
            ],
        },
        # 12
        {
            "title": "Moqueca Vegana de Caju e Palmito",
            "prep_time": 35,
            "tags": "vegano, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten",
            "instructions": "1. Refogar cebola, alho, pimentões e tomates.\n2. Adicionar o palmito, caju e leite de coco.\n3. Cozinhar por 15 min e finalizar com coentro.",
            "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Palmito Pupunha", "amount": 300, "unit": "g"},
                {"name": "Caju Fatiado", "amount": 2, "unit": "unidade"},
                {"name": "Leite de Coco", "amount": 200, "unit": "ml"},
                {"name": "Pimentão Vermelho", "amount": 1, "unit": "unidade"},
            ],
        },
        # 13
        {
            "title": "Poke de Atum Fresco e Abacate",
            "prep_time": 15,
            "tags": "proteico, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, fit, rapido, low_carb, low carb",
            "instructions": "1. Cortar o atum e o abacate em cubos.\n2. Montar a tigela com base de pepino.\n3. Temperar com shoyu sem glúten e gergelim.",
            "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Atum Fresco", "amount": 200, "unit": "g"},
                {"name": "Abacate", "amount": 100, "unit": "g"},
                {"name": "Pepino Japonês", "amount": 1, "unit": "unidade"},
                {"name": "Shoyu Sem Glúten", "amount": 15, "unit": "ml"},
            ],
        },
        # 14
        {
            "title": "Hambúrguer de Lentilha e Aveia",
            "prep_time": 30,
            "tags": "vegano, vegetariano, sem_lactose, sem lactose, fit",
            "instructions": "1. Processar a lentilha com temperos e aveia.\n2. Moldar os hambúrgueres.\n3. Dourar na frigideira com azeite por 5 min de cada lado.",
            "image_url": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Lentilha Cozida", "amount": 300, "unit": "g"},
                {"name": "Farelo de Aveia", "amount": 50, "unit": "g"},
                {"name": "Cebola Picada", "amount": 1, "unit": "unidade"},
                {"name": "Azeite de Oliva", "amount": 10, "unit": "ml"},
            ],
        },
        # 15
        {
            "title": "Risoto Fit de Couve-Flor com Cogumelos",
            "prep_time": 20,
            "tags": "vegetariano, low_carb, low carb, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit, rapido",
            "instructions": "1. Triturar a couve-flor em grãos pequenos.\n2. Refogar os cogumelos no azeite.\n3. Juntar a couve-flor e cozinhar por 5 minutos.",
            "image_url": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Couve-Flor Processada", "amount": 400, "unit": "g"},
                {"name": "Cogumelo Shimeji", "amount": 200, "unit": "g"},
                {"name": "Alho-Poró", "amount": 50, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
            ],
        },
        # 16
        {
            "title": "Smoothie Bowl de Açaí sem Açúcar",
            "prep_time": 5,
            "tags": "vegano, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, sem_acucar, sem açúcar, rapido, fit",
            "instructions": "1. Bater o açaí congelado com a banana.\n2. Despejar na tigela.\n3. Decorar com morangos e sementes de chia.",
            "image_url": "https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Polpa de Açaí Puro", "amount": 200, "unit": "g"},
                {"name": "Banana Congelada", "amount": 1, "unit": "unidade"},
                {"name": "Morango Fatiado", "amount": 50, "unit": "g"},
                {"name": "Chia", "amount": 10, "unit": "g"},
            ],
        },
        # 17
        {
            "title": "Escondidinho de Batata-Doce com Frango",
            "prep_time": 35,
            "tags": "proteico, sem_lactose, sem lactose, sem_gluten, sem gluten, sem glúten, fit, marmita",
            "instructions": "1. Amassar a batata-doce em purê.\n2. Montar camadas de frango desfiado e cobrir com purê.\n3. Assar por 15 minutos.",
            "image_url": "https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Batata-Doce Cozida", "amount": 400, "unit": "g"},
                {"name": "Frango Desfiado", "amount": 300, "unit": "g"},
                {"name": "Azeite", "amount": 10, "unit": "ml"},
            ],
        },
        # 18
        {
            "title": "Wrap Integral de Peito de Peru e Saladinha",
            "prep_time": 10,
            "tags": "rapido, proteico, sem_lactose, sem lactose, fit",
            "instructions": "1. Abrir o wrap integral.\n2. Dispor alface, tomate, cenoura e peito de peru.\n3. Enrolar e cortar ao meio.",
            "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Massa de Wrap Integral", "amount": 1, "unit": "unidade"},
                {"name": "Peito de Peru Fatiado", "amount": 60, "unit": "g"},
                {"name": "Alface Picada", "amount": 30, "unit": "g"},
                {"name": "Cenoura Ralada", "amount": 30, "unit": "g"},
            ],
        },
        # 19
        {
            "title": "Cuscuz Marroquino com Legumes",
            "prep_time": 15,
            "tags": "vegano, vegetariano, sem_lactose, sem lactose, rapido, fit",
            "instructions": "1. Hidratar o cuscuz em água fervente por 5 min.\n2. Grelhar legumes em cubos na frigideira.\n3. Misturar tudo com azeite de oliva.",
            "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Cuscuz Marroquino", "amount": 150, "unit": "g"},
                {"name": "Abobrinha em Cubos", "amount": 100, "unit": "g"},
                {"name": "Pimentão Amarelo", "amount": 50, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
            ],
        },
        # 20
        {
            "title": "Mingau Proteico de Aveia e Cacau",
            "prep_time": 10,
            "tags": "vegetariano, proteico, sem_lactose, sem lactose, sem_acucar, sem açúcar, rapido, fit",
            "instructions": "1. Cozinhar a aveia no leite vegetal até encorpar.\n2. Adicionar cacau e proteína em pó.\n3. Servir morno com fatias de banana.",
            "image_url": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Aveia em Flocos", "amount": 40, "unit": "g"},
                {"name": "Leite de Amêndoas", "amount": 200, "unit": "ml"},
                {"name": "Cacau em Pó 100%", "amount": 10, "unit": "g"},
                {"name": "Banana Madura", "amount": 0.5, "unit": "unidade"},
            ],
        },
        # 21
        {
            "title": "Omelete Fit de Zucchini e Ervas",
            "prep_time": 10,
            "tags": "vegetariano, low_carb, low carb, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, rapido, fit",
            "instructions": "1. Ralar a abobrinha e refogar no azeite.\n2. Bater os ovos com ervas e despejar sobre a abobrinha.\n3. Cozinhar em fogo baixo até firmar.",
            "image_url": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Ovo", "amount": 2, "unit": "unidade"},
                {"name": "Abobrinha Ralada", "amount": 80, "unit": "g"},
                {"name": "Salsa Picada", "amount": 10, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 5, "unit": "ml"},
            ],
        },
        # 22
        {
            "title": "Ceviche Tradicional de Peixe Branco",
            "prep_time": 20,
            "tags": "proteico, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, low_carb, low carb, fit, rapido",
            "instructions": "1. Cortar o peixe fresco em cubos pequenos.\n2. Marinar no suco de limão com cebola roxa por 15 min.\n3. Finalizar com coentro e pimenta.",
            "image_url": "https://images.unsplash.com/photo-1535399831218-d5bd36d1a6b3?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Tilápia ou Peixe Branco", "amount": 300, "unit": "g"},
                {"name": "Suco de Limão", "amount": 100, "unit": "ml"},
                {"name": "Cebola Roxa Fatiada", "amount": 1, "unit": "unidade"},
                {"name": "Coentro Picado", "amount": 10, "unit": "g"},
            ],
        },
        # 23
        {
            "title": "Kibe Assado de Quinoa e Abóbora",
            "prep_time": 40,
            "tags": "vegano, vegetariano, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit",
            "instructions": "1. Misturar a quinoa cozida com purê de abóbora e temperos.\n2. Espalhar em assadeira untada.\n3. Assar por 30 minutos a 200°C até dourar.",
            "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Quinoa Cozida", "amount": 200, "unit": "g"},
                {"name": "Purê de Abóbora Cabotiá", "amount": 200, "unit": "g"},
                {"name": "Hortelã Picada", "amount": 15, "unit": "g"},
                {"name": "Cebola Picada", "amount": 1, "unit": "unidade"},
            ],
        },
        # 24
        {
            "title": "Frango Xadrez com Castanhas",
            "prep_time": 25,
            "tags": "proteico, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit",
            "instructions": "1. Refogar cubos de frango no azeite.\n2. Adicionar pimentões, cebola e pimentão.\n3. Finalizar com shoyu sem glúten e castanhas.",
            "image_url": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Peito de Frango em Cubos", "amount": 400, "unit": "g"},
                {"name": "Pimentão Verde", "amount": 1, "unit": "unidade"},
                {"name": "Castanha-de-Caju", "amount": 30, "unit": "g"},
                {"name": "Shoyu Sem Glúten", "amount": 20, "unit": "ml"},
            ],
        },
        # 25
        {
            "title": "Sopa Fria de Tomate (Gazpacho)",
            "prep_time": 15,
            "tags": "vegano, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, low_carb, low carb, rapido",
            "instructions": "1. Bater tomates maduros, pepino, pimentão e azeite no liquidificador.\n2. Temperar com sal, vinagre e alho.\n3. Servir bem gelado.",
            "image_url": "https://images.unsplash.com/photo-1594998893017-36147cbcae05?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Tomate Maduro", "amount": 4, "unit": "unidade"},
                {"name": "Pepino", "amount": 1, "unit": "unidade"},
                {"name": "Azeite de Oliva Extra Virgem", "amount": 30, "unit": "ml"},
                {"name": "Vinagre de Maçã", "amount": 10, "unit": "ml"},
            ],
        },
        # 26
        {
            "title": "Salada Grega Inclusiva",
            "prep_time": 10,
            "tags": "vegetariano, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, low_carb, low carb, rapido",
            "instructions": "1. Cortar tomates, pepinos e azeitonas pretas.\n2. Misturar com tofu em cubos temperado com orégano.\n3. Regar generosamente com azeite.",
            "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Tomate Sweet Grape", "amount": 150, "unit": "g"},
                {"name": "Pepino Japonês", "amount": 1, "unit": "unidade"},
                {"name": "Azeitona Preta", "amount": 50, "unit": "g"},
                {"name": "Tofu Firme", "amount": 100, "unit": "g"},
            ],
        },
        # 27
        {
            "title": "Bolinho de Grão-de-Bico Assado (Falafel)",
            "prep_time": 30,
            "tags": "vegano, vegetariano, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit",
            "instructions": "1. Processar o grão-de-bico com alho, cebola, cominho e coentro.\n2. Moldar pequenas bolinhas.\n3. Assar a 200°C por 20 minutos até ficar crocante.",
            "image_url": "https://images.unsplash.com/photo-1547058881-aa0ed92a574f?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Grão-de-Bico Demolhado", "amount": 250, "unit": "g"},
                {"name": "Salsa e Coentro", "amount": 30, "unit": "g"},
                {"name": "Alho", "amount": 2, "unit": "dente"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
            ],
        },
        # 28
        {
            "title": "Espagete de Abobrinha à Bolognesa",
            "prep_time": 20,
            "tags": "proteico, low_carb, low carb, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, fit, rapido",
            "instructions": "1. Fazer tiras finas de abobrinha em formato de macarrão.\n2. Cozinhar a carne moída com molho de tomate caseiro.\n3. Refogar a abobrinha por 2 min e cobrir com o molho.",
            "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Abobrinha Itália", "amount": 2, "unit": "unidade"},
                {"name": "Patinho Moído", "amount": 250, "unit": "g"},
                {"name": "Molho de Tomate Caseiro", "amount": 150, "unit": "g"},
                {"name": "Azeite de Oliva", "amount": 10, "unit": "ml"},
            ],
        },
        # 29
        {
            "title": "Overnight Oats de Chia e Frutas Vermelhas",
            "prep_time": 5,
            "tags": "vegetariano, sem_lactose, sem lactose, sem_acucar, sem açúcar, fit, rapido",
            "instructions": "1. Misturar aveia, chia e leite vegetal em um pote de vidro.\n2. Deixar na geladeira durante a noite.\n3. Adicionar frutas vermelhas antes de consumir.",
            "image_url": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Aveia em Flocos", "amount": 40, "unit": "g"},
                {"name": "Semente de Chia", "amount": 15, "unit": "g"},
                {"name": "Leite de Coco Bebida", "amount": 150, "unit": "ml"},
                {"name": "Morangos e Mirtilos", "amount": 50, "unit": "g"},
            ],
        },
        # 30
        {
            "title": "Carne Seca Acebolada com Purê de Mandioquinha",
            "prep_time": 40,
            "tags": "proteico, sem_gluten, sem gluten, sem glúten, sem_lactose, sem lactose, marmita",
            "instructions": "1. Dessalgar e desfiar a carne seca, refogando com bastante cebola.\n2. Cozinhar a mandioquinha e amassar com azeite até formar o purê.\n3. Servir juntos.",
            "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80",
            "ingredients": [
                {"name": "Carne Seca Desfiada", "amount": 250, "unit": "g"},
                {"name": "Mandioquinha", "amount": 300, "unit": "g"},
                {"name": "Cebola Fatiada", "amount": 2, "unit": "unidade"},
                {"name": "Azeite de Oliva", "amount": 15, "unit": "ml"},
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
    print("✅ Banco atualizado! 30 receitas e tags com suporte a acentos/espaços configuradas.")
    db.close()


if __name__ == "__main__":
    popular_banco()
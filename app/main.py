from fastapi import FastAPI

# A variável OBRIGATORIAMENTE precisa se chamar "app"
app = FastAPI(title="TaskDiet API")


@app.get("/")
def home():
    return {"status": "ok", "message": "API TaskDiet rodando!"}
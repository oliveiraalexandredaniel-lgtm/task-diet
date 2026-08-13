from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho onde o arquivo SQLite será criado na raiz do seu projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./recipes.db"

# connect_args={"check_same_thread": False} é necessário apenas no SQLite para trabalhar bem com o FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Função Geradora de Sessão (Injetada com Depends(get_db) nas rotas)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
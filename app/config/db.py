"""db configuration"""
# SQLAlchemy
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base
# Settings
from app.config.settings import settings


SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_session() -> object:
    """Obtiene la sesión de la base de datos

    Yields:
        object: sesión de la base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_db_status(session: object) -> bool:
    """Comprueba el estado de la base de datos

    Args:
        session (object): objeto tipo sesión

    Returns:
        bool: determina si la conexion a la base de datos es exitosa o no
    """
    try:
        result = session.execute(select(1))
        return result.scalar_one_or_none() is not None
    except Exception:
        return False

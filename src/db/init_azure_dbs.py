import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Float,
    Integer,
    DateTime,
    JSON,
    ARRAY,
)
from sqlalchemy.orm import declarative_base
from datetime import datetime
from dotenv import load_dotenv


# ==========================================================
# CONFIG — edit these values
# ==========================================================

load_dotenv()



DATABASES = [
    "recipegraph_dev",
    "recipegraph_test",
    "recipegraph_prod",
]

# Admin connection for creating databases (connect to default "postgres")
ADMIN_CONN_STR = f"""
postgresql://{AZURE_USER}:{AZURE_PASSWORD}@{AZURE_SERVER}:{AZURE_PORT}/postgres?sslmode=require
"""


# ==========================================================
# 1. Create the Databases on Azure
# ==========================================================

def create_databases():
    """Creates dev, test, and prod databases on your Azure Postgres server."""

    print("🔌 Connecting to Azure as admin...")
    conn = psycopg2.connect(ADMIN_CONN_STR)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    for db_name in DATABASES:
        cursor.execute(
            f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';"
        )
        exists = cursor.fetchone()

        if not exists:
            print(f"🟢 Creating database: {db_name}")
            cursor.execute(f"CREATE DATABASE {db_name};")
        else:
            print(f"✔ Database already exists: {db_name}")

    cursor.close()
    conn.close()


# ==========================================================
# 2. SQLAlchemy ORM for the recipes table
# ==========================================================

Base = declarative_base()

class RecipeORM(Base):
    __tablename__ = "recipes"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    average_cost_per_serving = Column(Float, nullable=True)
    estimated_calories_per_serving = Column(Integer, nullable=True)

    # list[Ingredient] → JSON
    ingredients = Column(JSON, nullable=False)

    # list[str]
    instructions = Column(ARRAY(String), nullable=False)

    # timedelta stored as total seconds (int)
    cooking_time_seconds = Column(Integer, nullable=False)

    tags = Column(ARRAY(String), nullable=False)

    image_url = Column(String, nullable=True)

    embedding_vector = Column(ARRAY(Float), nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


# ==========================================================
# 3. Create tables in each Azure database
# ==========================================================

def create_tables():
    for db_name in DATABASES:
        db_url = (
            f"postgresql+psycopg2://{AZURE_USER}:{AZURE_PASSWORD}"
            f"@{AZURE_SERVER}:{AZURE_PORT}/{db_name}?sslmode=require"
        )

        print(f"\n🔗 Connecting to {db_name} at {AZURE_SERVER}...")
        engine = create_engine(db_url, echo=True)

        print(f"📦 Creating tables in {db_name}...")
        Base.metadata.create_all(bind=engine)
        print(f"✔ Tables created in {db_name}")


# ==========================================================
# RUN EVERYTHING
# ==========================================================

if __name__ == "__main__":
    print("🚀 Starting Azure initialization...\n")

    create_databases()
    print("\n🚀 Creating tables...\n")
    create_tables()

    print("\n✨ All Azure databases and tables created successfully!")

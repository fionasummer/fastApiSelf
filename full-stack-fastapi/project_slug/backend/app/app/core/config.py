import os

API_V1_STR = "/api/v1"

PROJECT_NAME = os.getenv("PROJECT_NAME")
# a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000"
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)


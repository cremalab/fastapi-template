from dotenv import load_dotenv

from config.util import Environment

load_dotenv(verbose=True)


class App:
    name = Environment.get_string("APP_NAME", "app_name")
    host = Environment.get_string("HOST", "0.0.0.0")
    port = Environment.get_int("PORT", 3000)
    dev = Environment.get_string("ENVIRONMENT") != "PRODUCTION"


class Celery:
    broker = Environment.get_string("CELERY_BROKER", "redis://redis:6379/14")
    backend = Environment.get_string("CELERY_BACKEND", "redis://redis:6379/15")


class Cors:
    allow_origins = Environment.get_string_list("CORS_ALLOW_ORIGINS", [])
    allow_methods = Environment.get_string_list("CORS_ALLOW_METHODS", ["*"])
    allow_headers = Environment.get_string_list("CORS_ALLOW_HEADERS", ["*"])


class Postgres:
    db_name = Environment.get_string("POSTGRES_DB_NAME", "database_name")
    host = Environment.get_string("POSTGRES_HOST", "localhost")
    port = Environment.get_string("POSTGRES_PORT", "5432")
    user = Environment.get_string("POSTGRES_USER", "root")
    password = Environment.get_string("POSTGRES_PASSWORD", "root")


class Redis:
    host = Environment.get_string("REDIS_HOST", "localhost")
    port = Environment.get_string("REDIS_PORT", "6379")

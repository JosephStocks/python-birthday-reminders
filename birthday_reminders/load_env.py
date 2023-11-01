import logging
import os
from pathlib import Path

from dotenv import load_dotenv


def get_env_var(var_name: str) -> str:
    try:
        return os.environ[var_name]
    except KeyError as e:
        raise ValueError(f"Environment variable {e} not set.") from e


def load_env_variables() -> None:
    ENV = os.environ.get("ENVIRONMENT", default="dev")

    if ENV == "dev":
        dotenv_path = Path.cwd() / ".env.dev"
    elif ENV == "prod":
        dotenv_path = Path.cwd() / ".env.prod"
    else:
        raise ValueError("Invalid environment name")

    print(dotenv_path)
    logging.info(f"Dotenv path: {dotenv_path}")

    load_dotenv(dotenv_path=dotenv_path)
    print(os.environ)

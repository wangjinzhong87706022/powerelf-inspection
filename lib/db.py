import os
import warnings
from typing import Optional


DB_HOST = os.getenv("POWERELF_DB_HOST", "localhost")
DB_PORT = int(os.getenv("POWERELF_DB_PORT", "3306"))
DB_NAME = os.getenv("POWERELF_DB_NAME", "powerelf_srm_yml")
DB_USER = os.getenv("POWERELF_DB_USER", "root")
DB_PASSWORD = os.getenv("POWERELF_DB_PASSWORD", "")

if not DB_PASSWORD:
    warnings.warn(
        "POWERELF_DB_PASSWORD 未设置，将使用空密码连接数据库。"
        "生产环境请设置该环境变量。",
        RuntimeWarning,
    )


def get_sqlalchemy_url(
    host: Optional[str] = None,
    port: Optional[int] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    database: Optional[str] = None,
) -> str:
    return (
        f"mysql+pymysql://{user or DB_USER}:{password or DB_PASSWORD}"
        f"@{host or DB_HOST}:{port or DB_PORT}/{database or DB_NAME}"
    )


def create_engine(url: Optional[str] = None):
    from sqlalchemy import create_engine as _create
    return _create(url or get_sqlalchemy_url())

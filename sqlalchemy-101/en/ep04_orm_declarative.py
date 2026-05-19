"""Sqlalchemy 101 - Episode 4: Orm declarative."""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base."""

    pass


class Article(Base):
    """Article."""

    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))


def run() -> str:
    """Run."""
    return Article.__tablename__

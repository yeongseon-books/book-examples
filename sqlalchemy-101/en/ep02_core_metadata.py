from sqlalchemy import Column, DateTime, Integer, MetaData, Numeric, String, Table


def run() -> list[str]:
    metadata = MetaData()
    Table(
        "products",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(100), nullable=False),
        Column("price", Numeric(10, 2), nullable=False),
        Column("created_at", DateTime),
    )
    return list(metadata.tables.keys())

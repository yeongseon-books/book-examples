# models.py
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    tier: Mapped[str] = mapped_column(String(16), server_default="free")  # ← new

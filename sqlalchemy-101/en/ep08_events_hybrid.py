from common import sync_engine
from sqlalchemy import Integer, String, event, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    @hybrid_property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@event.listens_for(Person, "before_insert")
def normalize_name(_, __, target: Person) -> None:
    target.first_name = target.first_name.strip().title()
    target.last_name = target.last_name.strip().title()


def run() -> str:
    engine = sync_engine()
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(Person(first_name="  alice", last_name="kim  "))
        session.commit()
        person = session.scalar(select(Person))
    return person.full_name

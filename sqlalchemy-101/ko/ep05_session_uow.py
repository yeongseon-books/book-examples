from common import User, create_schema, sync_engine
from sqlalchemy import func, select
from sqlalchemy.orm import Session


def run() -> tuple[int, bool]:
    engine = sync_engine()
    create_schema(engine)
    with Session(engine) as session:
        user = User(name="uow-user")
        session.add(user)
        session.flush()
        first_id = user.id
        same_user = session.get(User, first_id)
        is_identity_same = user is same_user
        session.commit()

    with Session(engine) as session:
        count = session.scalar(select(func.count(User.id)))
    return int(first_id), bool(is_identity_same and count == 1)

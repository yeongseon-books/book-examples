from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload, selectinload

from common import Post, User, create_schema, sync_engine


def run() -> dict[str, int]:
    engine = sync_engine()
    create_schema(engine)
    with Session(engine) as session:
        for i in range(2):
            user = User(name=f"user-{i}")
            user.posts = [Post(title=f"p{i}-1"), Post(title=f"p{i}-2")]
            session.add(user)
        session.commit()

    with Session(engine) as session:
        naive_users = session.execute(select(User)).scalars().all()
        naive_total_posts = sum(len(u.posts) for u in naive_users)
        with_selectin = session.execute(select(User).options(selectinload(User.posts))).scalars().all()
        with_joined = session.execute(select(User).options(joinedload(User.posts))).unique().scalars().all()
        return {
            "naive_posts": naive_total_posts,
            "selectin_users": len(with_selectin),
            "joined_users": len(with_joined),
        }

"""Sqlalchemy 101 - Episode 6: Relationships."""

from common import Post, Tag, User, create_schema, sync_engine
from sqlalchemy.orm import Session


def run() -> tuple[int, int]:
    """Run."""
    engine = sync_engine()
    create_schema(engine)
    with Session(engine) as session:
        user = User(name="rel-user")
        post = Post(title="first", author=user)
        tag = Tag(name="python")
        post.tags.append(tag)
        session.add_all([user, post, tag])
        session.commit()

    with Session(engine) as session:
        saved_user = session.query(User).first()
        saved_post = session.query(Post).first()
        return len(saved_user.posts), len(saved_post.tags)

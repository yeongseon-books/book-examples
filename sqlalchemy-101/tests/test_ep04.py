from ko import ep04_orm_declarative


def test_ep04_orm_declarative() -> None:
    assert ep04_orm_declarative.run() == "articles"

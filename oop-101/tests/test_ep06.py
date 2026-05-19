from ko.ep06_abstraction import InMemoryUserRepository, UserService


def test_ep06_repository_abstraction() -> None:
    repo = InMemoryUserRepository()
    service = UserService(repo)
    service.register("u42", "hana")
    assert repo.get("u42") == "hana"

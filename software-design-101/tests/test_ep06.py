from ko.ep06_layered_architecture import UserController, UserRepository, UserService


def test_ep06_layered_flow() -> None:
    repo = UserRepository()
    service = UserService(repo)
    controller = UserController(service)
    assert controller.create_user({"id": "u1", "name": "Kim"}) == "created"
    assert repo.get("u1") == {"id": "u1", "name": "Kim"}

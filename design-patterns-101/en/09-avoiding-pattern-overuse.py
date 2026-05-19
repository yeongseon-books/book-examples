class AbstractGreeterFactory:
    def create_greeter(self):
        return FormalGreeter()


class FormalGreeter:
    def greet(self, name):
        return f"Hello, {name}"


def over_engineered(name):
    return AbstractGreeterFactory().create_greeter().greet(name)


def simple(name):
    return f"Hello, {name}"

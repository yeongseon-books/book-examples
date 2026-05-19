from dataclasses import dataclass


@dataclass
class Thermostat:
    target: int
    current: int

    def heat_needed(self) -> bool:
        return self.current < self.target


def run_demo() -> str:
    thermostat = Thermostat(target=22, current=19)
    return "heating" if thermostat.heat_needed() else "idle"


if __name__ == "__main__":
    print(run_demo())

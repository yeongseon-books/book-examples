from dataclasses import dataclass


@dataclass
class CardState:
    repetitions: int
    interval: int
    easiness: float


def sm2_step(state: CardState, quality: int) -> CardState:
    quality = max(0, min(5, quality))
    easiness = max(
        1.3, state.easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    )
    if quality < 3:
        return CardState(repetitions=0, interval=1, easiness=easiness)
    if state.repetitions == 0:
        return CardState(repetitions=1, interval=1, easiness=easiness)
    if state.repetitions == 1:
        return CardState(repetitions=2, interval=6, easiness=easiness)
    new_interval = int(round(state.interval * easiness))
    return CardState(
        repetitions=state.repetitions + 1,
        interval=max(1, new_interval),
        easiness=easiness,
    )


if __name__ == "__main__":
    state = CardState(repetitions=0, interval=0, easiness=2.5)
    for q in [5, 5, 4, 2]:
        state = sm2_step(state, q)
        print(state)

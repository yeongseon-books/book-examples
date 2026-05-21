"""Generated from book-content article."""

def is_injective(mapping: dict) -> bool:
    return len(set(mapping.values())) == len(mapping)

def is_surjective(mapping: dict, codomain: set) -> bool:
    return set(mapping.values()) == codomain

m = {"a": 1, "b": 2, "c": 3}
print(is_injective(m), is_surjective(m, {1,2,3}))

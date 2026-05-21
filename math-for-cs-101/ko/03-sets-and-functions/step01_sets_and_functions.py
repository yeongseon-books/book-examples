"""Math For Cs 101 - 3편: sets and functions 예제."""

from common import is_injective


def classify_mapping(mapping, codomain):
    """Classify mapping."""
    injective = is_injective(mapping)
    surjective = set(mapping.values()) == set(codomain)
    return injective, surjective, injective and surjective

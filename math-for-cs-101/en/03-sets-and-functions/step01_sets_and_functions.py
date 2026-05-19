"""Math For Cs 101 - Episode 1: Sets and functions."""

from common import is_injective


def classify_mapping(mapping, codomain):
    """Classify mapping."""
    injective = is_injective(mapping)
    surjective = set(mapping.values()) == set(codomain)
    return injective, surjective, injective and surjective

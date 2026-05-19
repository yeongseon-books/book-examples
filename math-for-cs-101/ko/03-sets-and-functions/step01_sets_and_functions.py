from common import is_injective


def classify_mapping(mapping, codomain):
    injective = is_injective(mapping)
    surjective = set(mapping.values()) == set(codomain)
    return injective, surjective, injective and surjective

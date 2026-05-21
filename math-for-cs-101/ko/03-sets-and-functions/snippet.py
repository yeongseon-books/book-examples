"""Generated from book-content article."""

def can_access(user_scopes: set[str], required_scopes: set[str]) -> bool:
    return required_scopes.issubset(user_scopes)

user = {'read:post', 'read:comment', 'write:comment'}
required = {'read:post'}

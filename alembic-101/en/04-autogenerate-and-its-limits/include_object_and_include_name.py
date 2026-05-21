"""Generated from book-content article."""

def include_object(object, name, type_, reflected, compare_to):
    # Skip audit tables managed by an external system
    if type_ == "table" and name.startswith("legacy_"):
        return False
    return True

context.configure(
    connection=connection,
    target_metadata=target_metadata,
    include_object=include_object,
)

"""Generated from book-content article."""

def include_object(object, name, type_, reflected, compare_to):
    # Skip audit tables managed by an external system
    return not (type_ == "table" and name.startswith("legacy_"))

context.configure(
    connection=connection,
    target_metadata=target_metadata,
    include_object=include_object,
)

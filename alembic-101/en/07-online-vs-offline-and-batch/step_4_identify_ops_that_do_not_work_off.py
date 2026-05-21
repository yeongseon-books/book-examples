"""Generated from book-content article."""

def upgrade() -> None:
    bind = op.get_bind()                  # None in offline mode
    if bind:                              # add a guard
        bind.execute(text("UPDATE ..."))

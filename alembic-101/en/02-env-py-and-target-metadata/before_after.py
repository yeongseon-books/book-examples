# Before: scaffolded defaults (autogenerate produces empty files)
from alembic import context
config = context.config
target_metadata = None  # ← leaving this empty disables autogenerate

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), ...)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

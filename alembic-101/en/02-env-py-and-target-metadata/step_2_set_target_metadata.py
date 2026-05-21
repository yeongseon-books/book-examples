"""Generated from book-content article."""

from sqlalchemy import MetaData
combined = MetaData()
for m in [Base.metadata, OtherBase.metadata]:
    for t in m.tables.values():
        t.tometadata(combined)
target_metadata = combined

# pip install pandera
import pandera as pa
from pandera.typing import Series

class TextSchema(pa.DataFrameModel):
    id: Series[str] = pa.Field(unique=True)
    text: Series[str] = pa.Field(str_length={"min_value": 1})
    source: Series[str]
    ingested_at: Series["datetime64[ns]"]

# 각 단계 진입 시 검증
TextSchema.validate(df)

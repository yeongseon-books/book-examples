"""Generated from book-content article."""

import boto3

textract = boto3.client("textract", region_name="us-east-1")

def extract_tables(img_path: str) -> list:
    with open(img_path, "rb") as f:
        resp = textract.analyze_document(
            Document={"Bytes": f.read()},
            FeatureTypes=["TABLES"],
        )
    tables = [b for b in resp["Blocks"] if b["BlockType"] == "TABLE"]
    return tables

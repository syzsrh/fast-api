from fastapi import FastAPI, UploadFile, File, Query
from typing import Annotated
from validators import validate_csv, validate_file_type
from embedding import embed_text
    
app = FastAPI()

@app.get("/")
async def root():
    return {"ping":"pong"}

@app.post("/csv/")
async def csv_upload(file: UploadFile = File(...), equals: int | None = None):
    """Handle CSV file upload and process it.
    
    This endpoint accepts a CSV file upload and an optional query parameter 'equals'. The CSV file is validated to ensure it meets certain criteria, and if provided, the 'equals' parameter is used for additional processing.

    Args:
        file (UploadFile, required): Uploaded file. Defaults to File(...).
        equals (str | None, optional): Optional query parameter value. Defaults to None.

    Returns:
        dict: A dictionary object containing the processed CSV data.
    """
    
    validate_file_type(file)
    rows = validate_csv(file, equals)
    
    return {
        "file": file.filename,
        "equals": equals,
        "rows": rows
        }

@app.get("/embedding/")
async def embedding(text: Annotated[str, Query(min_length=5)]):
    """Generate and return an embedding for the given text.

    Args:
        text (Annotated[str, Query): A string input from the user. The minimum length of the string is enforced to be 5 characters.

    Returns:
        dict: A dictionary containing the original text and its computed embedding.
    """
    
    embed = embed_text(text)
    return {
        "text":text,
        "embed":embed
        }
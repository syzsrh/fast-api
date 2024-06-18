from fastapi import HTTPException, status
import csv, codecs

def is_int(value):
    """Helper to check if a value can be converted to an integer.

    Args:
        value (Any): The value to be checked.

    Returns:
        bool: True if the value can be converted to an integer, False otherwise.
    """
    
    try:
        int(value)
    except ValueError:
        return False
    return True

def validate_file_type(file, mime = "text/csv"):
    """Validate the file type against the specified MIME type.

    Args:
        file (Any): Uploaded file.
        mime (str, optional): The MIME type to validate against. Defaults to "text/csv".

    Raises:
        HTTPException: Raised when the file type does not match the specified MIME type. 
    """
    
    if file.content_type != mime:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="File type is not supported, please only upload .csv files"
        )
  
def validate_csv(file, equals = None, headers = {"Response", "Value"}):
    """Validate and process a CSV file.

    Args:
        file (UploadFile): The uploaded CSV file.
        equals (int, optional): An optional value to filter rows by. Defaults to None.
        headers (dict, optional): The expected column headers. Defaults to {"Response", "Value"}.

    Raises:
        HTTPException: If the CSV file contains columns other than 'Response' and 'Value'.
        HTTPException: If any row in the 'Response' column contains an empty string.
        HTTPException: If any value in the 'Response' column is not a string.
        HTTPException: If any value in the 'Value' column is not an integer.

    Returns:
        list: A list of dictionaries representing the validated CSV rows.
    """
        
    csv_reader = csv.DictReader(codecs.iterdecode(file.file,'utf-8'))
    columns = csv_reader.fieldnames
    
    if not set(columns) == headers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CSV file must only contain columns 'Response' and 'Value'"
        )
    
    response = []
    
    for row in csv_reader:
        if not row["Response"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="'Response' column must not contain empty strings."
            )
        if not isinstance(row["Response"], str):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="'Response' column must only contain strings."
            )
        if not is_int(row["Value"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="'Value' column must only contain integers."
            )
        row["Response"] = row["Response"].strip()
        if not equals:
            response.append(row)
        else:
            if int(row["Value"]) == equals:
                response.append(row)
    
    return response
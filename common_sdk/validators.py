# common_sdk/validators.py

from fastapi import HTTPException


def validate_non_empty_list(value: list, field_name: str):
    """
    Ensure a list field is not empty.
    Raises 422 if empty.
    """
    if not value:
        raise HTTPException(status_code=422, detail=f"'{field_name}' must be a non-empty list")
    return value

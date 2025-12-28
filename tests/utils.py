# utils.py

import json
from datetime import date
from typing import Dict, List

def load_config(filename: str) -> Dict:
    with open(filename, 'r') as config_file:
        return json.load(config_file)

def get_date_str(date_obj: date) -> str:
    return date_obj.strftime('%Y-%m-%d')

def get_date_obj(date_str: str) -> date:
    return date.fromisoformat(date_str)

def format_error_message(error_type: str, error_message: str, error_details: List[str]) -> str:
    return f"{error_type}: {error_message}\nDetails: {', '.join(error_details)}"

def validate_input(input_value: str, allowed_values: List[str]) -> bool:
    return input_value in allowed_values

def get_pagination_metadata(total_count: int, page_number: int, page_size: int) -> Dict:
    return {
        'total_count': total_count,
        'page_number': page_number,
        'page_size': page_size,
        'has_next_page': page_number * page_size < total_count,
        'has_previous_page': page_number > 1
    }
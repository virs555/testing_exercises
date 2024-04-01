import pytest

from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration

def test__fetch_app_config_field__returns_subfield(config_file_path):
    assert fetch_app_config_field(config_file_path, "extra_fields") == "\nage: int\nemail: str\nsalary: float"

def test__fetch_app_config_field__returns_none_if_havent_found_field(config_file_path):
    assert fetch_app_config_field(config_file_path, "wrong_fields") == None

def test__fetch_extra_fields_configuration__returns_dict_property_type(config_file_path):
    assert fetch_extra_fields_configuration(config_file_path) == {'age': int, 'email': str, 'salary': float}

def test__fetch_extra_fields_configuration__doesnt_return_anything_if_field_empty(config_file_path_without_fields):
    assert fetch_extra_fields_configuration(config_file_path_without_fields) == {}
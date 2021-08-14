from src.utilities import Utilities
from itertools import permutations
from base64 import b16encode
import pytest
from typing import Any, List
from random import sample
from faker import Faker

RGB = permutations(range(255), 3)
HEX_LIST = [b16encode(bytes(c)) for c in RGB]
fake = Faker()

# increase the range of the HEX_LIST below if you need to run more than 10 iterations
@pytest.mark.parametrize("input_value", sample(population=HEX_LIST, k=10))
def test_is_hex(input_value):
    assert Utilities.is_hex_color(colour_input=input_value)


@pytest.mark.parametrize("input_value", sample(population=HEX_LIST, k=10))
def test_is_not_hex(input_value: Any):
    input_value_ = input_value[0:5]
    assert Utilities.is_hex_color(colour_input=input_value_) is False


fake_language_codes: List[str]
fake_language_codes = ["-".join(fake.random_letters(2)) for _ in range(10)]


@pytest.mark.parametrize("language_code", fake_language_codes)
def test_is_invalid_language_code(language_code: str):
    assert Utilities.is_valid_language_code(language_code=language_code) is False

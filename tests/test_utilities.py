from wasp.src.utilities import Utilities
from itertools import permutations
from base64 import b16encode
import pytest

rgb = permutations(range(255), 3)
hex_list = [b'#'+b16encode(bytes(c)) for c in rgb]


@pytest.mark.parametrize("hex_value", hex_list[0:10])
def test_is_hex(hex_value):
    assert Utilities.is_hex_color(colour_input=hex_value)
    breakpoint()

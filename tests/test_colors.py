from wasp.src.domain.colors import Colors
import pytest


@pytest.mark.parametrize(
    "attribute",
    ('BOLD', 'ENDC', 'FAIL', 'HEADER', 'OKBLUE', 'OKGREEN', 'UNDERLINE', 'WARNING')
)
def test_attribute_has_color(attribute):
    colors = Colors()
    attribute_color = getattr(colors, attribute)
    assert attribute_color


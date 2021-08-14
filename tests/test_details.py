from src.details import Details
from argparse import Namespace
from faker import Faker
from typing import Dict, List, Any, Tuple
import pytest
from os.path import isfile
from os import unlink

fake = Faker()

fake_input_values: List[Tuple[Dict[str, Any], Namespace]]
fake_input_values = [
    (
        {
            "name": f"{fake.word()}",
            "description": fake.sentence(),
            "short_name": "",
            "theme_color": fake.color(),
            "background_color":  fake.color(),
            "start_url": fake.url(),
            "display": f"",
            "lang": fake.language_code(),
            "orientation": fake.random_choices(elements=["portrait", "landscape"], length=1)[0],
            "related_applications_check": fake.random_choices(elements=["y", "n"], length=1)[0],
            "dir": fake.file_path(),
            "keywords": fake.words(nb=fake.pyint(min_value=1, max_value=10)),
            "issue_tracker_url": fake.url(),
            "icons_check": fake.random_choices(elements=["y", "n"], length=1)[0],
            "bug_report_email": fake.email()
        },
        Namespace(
            manifest=fake.boolean(),
            package=fake.boolean(),
            task=fake.random_choices(elements=("init", "update", "tag"), length=1))
    ) for _ in range(10)
]


@pytest.mark.parametrize("details, args", fake_input_values)
def test_generate_details(details: Dict[str, Any], args: Namespace):
    package_file_path = "package.json"
    wasp_details = Details(details=details, args=args)
    wasp_details.generate()

    if args.task == "init":
        assert isfile(package_file_path)
        unlink(package_file_path)



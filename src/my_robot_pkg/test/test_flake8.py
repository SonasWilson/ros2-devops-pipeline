import pytest
from ament_flake8.main import main_with_errors


@pytest.mark.flake8
def test_flake8():
    rc, errors = main_with_errors(argv=['src/my_robot_pkg'])

    assert rc == 0, f"Found {len(errors)} code style errors:\n" + "\n".join(errors)

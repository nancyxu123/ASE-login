import pytest
from login import *
from flask import current_app

def test_check():
    with app.app_context():
        assert check_user("abc") == False


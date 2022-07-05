import unittest
from unittest import TestCase

from app.main import get_products, read_root

# sys.path.insert(0, os.path.dirname(__file__))


def test_root():
    message = read_root()
    assert message == {"Hello": "World"}


def test_get_products():
    # idjejkdkf
    products = get_products()
    assert len(products) > 0


if __name__ == "__main__":
    unittest.main()

"""
For now only a import of the ampty moving average class.
"""

from indicators import MA

def test_ma_class_import():
    """
    Test for importing the MA class.

    This test creates an instance of the MA class and asserts its type.

    Assertions:
        - The created instance should be of type MA.
    """
    ma_instance = MA()
    assert isinstance(ma_instance, MA)
    
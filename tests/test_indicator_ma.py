from indicators import MA, Indicator

def test_ma_instance_type():
    """
    Test for the type of the MA instance.

    Assertion:
        - The created instance should be of type MA.
    """
    ma_instance = MA(12)
    assert isinstance(ma_instance, MA)

def test_ma_instance_indicator_type():
    """
    Test for the type of the MA instance as an Indicator.

    Assertion:
        - The created instance should be an instance of the Indicator class.
    """
    ma_instance = MA(12)
    assert isinstance(ma_instance, Indicator)

def test_ma_instance_subclass_of_indicator():
    """
    Test for the MA instance being a subclass of Indicator.

    Assertion:
        - The created instance should be a subclass of the Indicator class.
    """
    ma_instance = MA(12)
    assert issubclass(type(ma_instance), Indicator)


"""
Module: indicators

This module provides a base class for indicators and an indicator registry.
"""

import weakref

class IndicatorRegistry:
    """
    A registry for managing indicator instances and their values.
    """
    def __init__(self):
        self.registry = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        """
        Set the value associated with the indicator instance.
        """
        self.registry[instance] = value

    def __get__(self, instance, owner_class):
        """
        Get either a list of all registered indicator instances 
        or the value associated with a specific instance.
        """
        if instance is None:
            return list(self.registry)
        return self.registry[instance]

class Indicator():
    """
    Base class for indicators.
    """
    _registry = IndicatorRegistry()
    data = []

    def __init__(self, window):
        """
        Initialize an indicator with a specified window size.
        """
        self.window = window
        self._registry = window

    @classmethod
    def calculate_all_registered(cls):
        """
        Calculate the value for all registered indicators.
        """
        for instance in cls._registry:
            instance.calc()

    @classmethod
    def add(cls, data):
        """
        Add data to the indicator's data attribute.
        """
        if cls.get_max_window() > len(cls.data):
            cls.data.insert(0, data)
        else:
            cls.data.pop()
            cls.data.insert(0, data)

    @classmethod
    def get_max_window(cls):
        """
        Get the maximum window size among all registered indicators.
        """
        return max(x.window for x in cls._registry)

    def calc(self):
        """
        Placeholder for the calculation method that should be implemented by subclasses.
        """
        raise NotImplementedError("calc method must be implemented by subclasses")

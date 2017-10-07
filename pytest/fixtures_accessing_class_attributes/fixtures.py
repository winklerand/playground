"""
Simple example on how fixtures can access test class attributes.

Fixtures defined outside of actual test class might require access to
attributes or methods defined inside those classes.
"""

import pytest


# alternative 1:
# define fixtures on module level and access test context via request obj
# https://docs.pytest.org/en/latest/fixture.html#fixtures-can-introspect-the-requesting-test-context
@pytest.fixture
def simple_fixture(request):
    fixture_param_from_class = getattr(request.cls, "_fixture_param")
    return fixture_param_from_class


# alternative 2:
# define a mixin, actual test classes inherit the fixtures
class FixturesMixin:

    _fixture_param = None  # defined in actual test classes

    @pytest.fixture
    def simple_fixture_as_method(self):
        return self._fixture_param

from fixtures import simple_fixture, FixturesMixin
# importing simple_fixture results in flake8 errors:
# F401 'fixtures.simple_fixture' imported but unused
# F811 redefinition of unused 'simple_fixture' from line 1
# solution approach: put fixtures in conftest.py
# https://mail.python.org/pipermail/code-quality/2017-May/000903.html


class TestClassA:

    _fixture_param = 'fixture_param_class_a'

    def test_a(self, simple_fixture):
        print(self.__class__, simple_fixture)
        assert simple_fixture == self._fixture_param


class TestClassB:

    _fixture_param = 'fixture_param_class_b'

    def test_b(self, simple_fixture):
        print(self.__class__, simple_fixture)
        assert simple_fixture == self._fixture_param


class TestClassC(FixturesMixin):

    _fixture_param = 'fixture_param_class_c'

    def test_b(self, simple_fixture_as_method):
        print(self.__class__, simple_fixture_as_method)
        assert simple_fixture_as_method == self._fixture_param

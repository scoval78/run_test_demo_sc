import pytest


@pytest.fixture
def separator():
    print('=' * 10)
    yield 'value'
    print('test finished')

@pytest.fixture(scope='session')
def all_tests():
    print('before all')
    yield True
    print('after all')
import pytest

# Пред условием может быть что браузер запущен


@pytest.mark.regression
def test_one_is_one(separator, all_tests):
    print('Hello world')
    print(separator)

    assert 1 == 1, "Number is not equal to 1"

@pytest.mark.smoke
def test_two_is_two(separator):
    # print('Hello Coval')
    # print(separator)
    assert 2 == 2, "Number is not equal to 2"


@pytest.mark.skip('Bug #2 ')
def test_three_is_three(separator):
    print('Hello Sergei!!!')
    print(separator)
    assert 3 == 2, "Number is not equal to 3"

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert 3 == 3


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
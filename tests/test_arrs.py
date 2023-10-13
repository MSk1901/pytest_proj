import pytest

from utils import arrs
from utils import dicts


@pytest.fixture
def ex_list():
    return [1, 2, 3, 4]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def ex_dict():
    return {1: "bird", 2: "fish", 3: "cat"}


def test_get(ex_list):
    assert arrs.get(ex_list, 1, "test") == 2


def test_get_empty(empty_list):
    assert arrs.get(empty_list, 0, "test") == "test"


def test_slice(ex_list):
    assert arrs.my_slice(ex_list, 1, 3) == [2, 3]
    assert arrs.my_slice(ex_list, 1) == [2, 3, 4]
    assert arrs.my_slice(ex_list, None, 2) == [1, 2]


def test_slice_empty(empty_list):
    assert arrs.my_slice(empty_list) == []


def test_get_val(ex_dict):
    assert dicts.get_val(ex_dict, 1) == "bird"
    assert dicts.get_val(ex_dict, 0) == "git"
    assert dicts.get_val(ex_dict, 0, "not found") == "not found"

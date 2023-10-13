from utils import arrs
from utils import dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], None, 2) == [1, 2]
    assert arrs.my_slice([]) == []


def test_get_val():
    assert dicts.get_val({1: "bird", 2: "fish", 3: "cat"}, 1) == "bird"
    assert dicts.get_val({1: "bird", 2: "fish", 3: "cat"}, 0) == "git"
    assert dicts.get_val({1: "bird", 2: "fish", 3: "cat"}, 0, "not found") == "not found"

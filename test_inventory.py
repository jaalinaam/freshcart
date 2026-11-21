import pytest
from inventory import restock, sell


# ---------- restock ----------

def test_restock_adds_to_existing_item():
    stock = {"apples": 5}
    restock(stock, "apples", 10)
    assert stock["apples"] == 15


def test_restock_rejects_zero_qty():
    with pytest.raises(ValueError):
        restock({}, "apples", 0)


# ---------- sell ----------

def test_sell_reduces_stock():                      # criterion 1
    stock = {"apples": 50}
    sell(stock, "apples", 10)
    assert stock["apples"] == 40


def test_sell_entire_stock_leaves_zero():           # criterion 2
    stock = {"apples": 50}
    sell(stock, "apples", 50)
    assert stock["apples"] == 0


def test_sell_more_than_stock_raises_and_keeps_stock():   # criterion 3
    stock = {"apples": 5}
    with pytest.raises(ValueError):
        sell(stock, "apples", 10)
    assert stock["apples"] == 5          # stock must be UNCHANGED after the failure


def test_sell_unknown_item_raises_keyerror():       # criterion 4
    with pytest.raises(KeyError):
        sell({"apples": 5}, "bananas", 1)


@pytest.mark.parametrize("bad_qty", [0, -3])        # criterion 5
def test_sell_rejects_non_positive_qty(bad_qty):
    with pytest.raises(ValueError):
        sell({"apples": 5}, "apples", bad_qty)
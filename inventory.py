def restock(stock: dict, item: str, qty: int) -> dict:
    """Add qty units of item to the stock."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    stock[item] = stock.get(item, 0) + qty
    return stock


if __name__ == "__main__":
    store = {}
    restock(store, "apples", 50)
    print(store)
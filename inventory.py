def restock(stock: dict, item: str, qty: int) -> dict:
    """Add qty units of item to the stock."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    stock[item] = stock.get(item, 0) + qty
    return stock

def sell(stock: dict, item: str, qty: int) -> dict:
    """Remove qty units of item from the stock."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    if item not in stock:
        raise KeyError(f"{item} is not in stock")
    if qty > stock[item]:
        raise ValueError(f"only {stock[item]} {item} in stock, cannot sell {qty}")
    stock[item] -= qty
    return stock

if __name__ == "__main__":
    store = {}
    restock(store, "apples", 50)
    print(store)


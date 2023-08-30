def num_jewels_in_stones(jewels: str, stones: str) -> int:
    all_jewels = 0
    for jewel in jewels:
        all_jewels += stones.count(jewel)
    return all_jewels


num_jewels_in_stones(jewels="aA", stones="aAAbbbb")
num_jewels_in_stones(jewels="z", stones="ZZ")

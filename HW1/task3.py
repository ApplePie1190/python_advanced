def pack_bag(items, max_weight):
    backpack = []
    current_weight = 0
    for item, weight in items.items():
        if current_weight + weight <= max_weight:
            backpack.append(item)
            current_weight += weight
    return backpack

if __name__ == '__main__':
    items = {"спальник": 1.5, "палатка": 3.0, "термос": 1.0, "котелок": 1.2, "карта": 0.3, "фонарик": 0.5}
    max_weight = 5.0 
    backpack = pack_bag(items, max_weight)
    print(f"В рюкзак поместятся следующие вещи: {backpack}")

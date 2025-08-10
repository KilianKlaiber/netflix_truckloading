def get_truck_items(item_weights: list[int], max_weight: int) -> list[int]:
    """Select items to be placed on one truck

    Args:
        item_weights (list[int]): List of weights to be distributed on trucks
        max_weight (int): maximum weight that the truck can load

    Returns:
        list[int]: List of weights selected from the item_weights
    """

    truck_weights = []

    first_weight = item_weights.pop(0)

    if first_weight > max_weight:
        raise ValueError(
            f"The item weights comprises a weight {first_weight}, which exceeds the maximum admissible weight {max_weight}"
        )

    truck_weights.append(first_weight)

    for index, weight in enumerate(item_weights):
        if sum(truck_weights) + weight <= max_weight:
            next_weight = item_weights.pop(index)
            truck_weights.append(next_weight)

    return truck_weights


def main():
    # Weight of the items to be loaded on trucks
    item_weights = [10, 20, 30, 40, 50]

    # Maximum weight that each truck can carry
    max_weight = 70

    item_weights.sort(reverse=True)

    # List of lists, each list containing the items placed on a single truck.

    trucks = []

    while item_weights:
        truck_weights = get_truck_items(item_weights, max_weight)
        trucks.append(truck_weights)

    print(trucks)


if __name__ == "__main__":
    main()

import math


def get_truck_items(item_weights: list[int], max_weight: int) -> list[int]:
    """Select items to be placed on one truck

    Args:
        item_weights (list[int]): List of weights to be distributed on trucks sorted from heaviest to leightest
        max_weight (int): maximum weight that the truck can load

    Returns:
        list[int]: List of weights selected from the item_weights
    """

    truck_weights = []
    current_weight = 0
    items_to_remove = []

    for weight in item_weights:
        if current_weight + weight <= max_weight:
            truck_weights.append(weight)
            current_weight += weight
            items_to_remove.append(weight)

    for weight in items_to_remove:
        item_weights.remove(weight)
        
    return truck_weights


def main():
    # Weight of the items to be loaded on trucks
    item_weights = [4, 3, 3, 3, 2, 2, 2, 2]

    # Maximum weight that each truck can carry
    max_weight = 6

    item_weights.sort(reverse=True)

    # List of lists, each list containing the items placed on a single truck.

    trucks = []

    while item_weights:
        truck_weights = get_truck_items(item_weights, max_weight)
        trucks.append(truck_weights)

    print(trucks)


if __name__ == "__main__":
    main()

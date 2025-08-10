""" Distribute items among trucks
A list of items with a particular weight must be distributed among truck, which
may only carry a maximum weight such that a minimum number of trucks is used for
carrying the items.
"""


def get_truck_items(item_weights: list[int], max_weight: int) -> list[int]:
    """Select items to be placed on one truck

    Args:
        item_weights (list[int]): List of weights to be distributed on trucks sorted from heaviest to leightest
        max_weight (int): maximum weight that the truck can load

    Returns:
        list[int]: List of weights selected from the item_weights
    """

    if item_weights[0] > max_weight:
        ValueError("First item is heavier than maximum weight")
    
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


def fast_distribution_of_items(item_weights: list[int], max_weight: int) -> list[list[int]]:
    
    item_weights.sort(reverse=True)

    # List of lists, each list containing the items placed on a single truck.

    trucks = []

    while item_weights:
        truck_weights = get_truck_items(item_weights, max_weight)
        trucks.append(truck_weights)

    return trucks


def main():
    
    # Weight of the items to be loaded on trucks
    item_weights = [4, 3, 3, 3, 2, 2, 2, 2]
    total_weight = sum(item_weights)

    # Maximum weight that each truck can carry
    max_weight = 6
    
    trucks = fast_distribution_of_items(item_weights, max_weight)
    
    # Sort the list according to the weight carried by each truck
    trucks.sort(key=sum)
    lowest_weight = sum(trucks[0])
    residual_weight = total_weight - lowest_weight
    total_residual_capacity = (len(trucks)-1) * max_weight
    unused_capacity = total_residual_capacity - residual_weight
    
    if lowest_weight > unused_capacity:
        print(trucks)
        return trucks
    
    else:
        pass
    
    

if __name__ == "__main__":
    main()

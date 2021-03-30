def merge_sort(*args):
    visualizer, left, right = args[0], args[1], args[2]
    mid = (left + right) // 2
    if left < right:
        merge_sort(visualizer, left, mid)
        merge_sort(visualizer, mid + 1, right)
        merge(visualizer, left, right, mid)


def merge(visualizer, left, right, mid):
    left_part = visualizer.array[left:mid+1]
    right_part = visualizer.array[mid+1:right+1]

    left_part_idx = 0
    right_part_idx = 0
    sorted_idx = left

    while left_part_idx < len(left_part) and right_part_idx < len(right_part):
        left_part[left_part_idx].color = visualizer.RED
        right_part[right_part_idx].color = visualizer.RED
        visualizer.refill()
        left_part[left_part_idx].color = visualizer.GREEN
        right_part[right_part_idx].color = visualizer.GREEN
        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_part[left_part_idx].value <= right_part[right_part_idx].value:
            visualizer.array[sorted_idx] = left_part[left_part_idx]
            left_part_idx += 1
        # Opposite from above
        else:
            visualizer.array[sorted_idx] = right_part[right_part_idx]
            right_part_idx += 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_idx += 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_part_idx < len(left_part):
        left_part[left_part_idx].color = visualizer.RED
        visualizer.refill()
        left_part[left_part_idx].color = visualizer.GREEN

        visualizer.array[sorted_idx] = left_part[left_part_idx]
        left_part_idx += 1
        sorted_idx += 1

    while right_part_idx < len(right_part):
        # right_part[right_part_idx].color = visualizer.RED
        # visualizer.refill()
        # right_part[right_part_idx].color = visualizer.GREEN

        visualizer.array[sorted_idx] = right_part[right_part_idx]
        right_part_idx += 1
        sorted_idx += 1

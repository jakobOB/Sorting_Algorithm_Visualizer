def bubble_sort(*args):
    visualizer = args[0]

    for j in range(len(visualizer.array) - 1, 0, -1):

        for i in range(j):
            visualizer.array[i].color, visualizer.array[i+1].color = visualizer.RED, visualizer.RED
            visualizer.refill(delay=5)
            visualizer.array[i].color, visualizer.array[i + 1].color = visualizer.GREEN, visualizer.GREEN

            if visualizer.array[i].value > visualizer.array[i+1].value:
                visualizer.array[i], visualizer.array[i+1] = visualizer.array[i+1], visualizer.array[i]

        visualizer.array[j].color = visualizer.ORANGE

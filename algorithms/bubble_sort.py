def bubble_sort(*args):
    game = args[0]

    for j in range(len(game.array) - 1, 0, -1):

        for i in range(j):
            game.array[i].color, game.array[i+1].color = game.RED, game.RED
            game.refill(delay=5)
            game.array[i].color, game.array[i + 1].color = game.GREEN, game.GREEN

            if game.array[i].value > game.array[i+1].value:
                game.array[i], game.array[i+1] = game.array[i+1], game.array[i]

        game.array[j].color = game.ORANGE

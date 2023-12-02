import os


def check_batches(valid, batches) -> bool:
    for batch in batches:
        batch = batch.split(",")
        for draw in batch:
            color = draw.strip().split(" ")[1]
            amount = int(draw.strip().split(" ")[0])
            if amount > valid[color]:
                return False
    return True


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        config_lines = file.readlines()

    possible = {"red": 12, "green": 13, "blue": 14}

    total = 0

    for line in config_lines:
        game = line.split(":")
        game_id = int(game[0].split(" ")[1])
        game_batches = game[1].split(";")
        game_batches[-1] = game_batches[-1].strip("\n")
        if check_batches(possible, game_batches):
            total += game_id

    print(total)



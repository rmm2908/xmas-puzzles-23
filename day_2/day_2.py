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


def get_line_pwr(batches: list) -> int:
    power = 1
    max_vals = {"red": 0, "blue": 0, "green": 0}
    for batch in batches:
        color = batch.strip().split(" ")[1]
        amount = int(batch.strip().split(" ")[0])
        if amount > max_vals[color]:
            max_vals[color] = amount
    for val in list(max_vals.values()):
        power *= val
    return power



if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), encoding="UTF-8") as file:
        config_lines = file.readlines()

    possible = {"red": 12, "green": 13, "blue": 14}

    total_valid = 0
    power_sum = 0

    for line in config_lines:
        game = line.split(":")
        game_id = int(game[0].split(" ")[1])
        game_batches = game[1].split(";")

        game_batches[-1] = game_batches[-1].strip("\n")
        if check_batches(possible, game_batches):
            total_valid += game_id

        power_batches = game[1].strip("\n").strip().replace(";", ",").split(",")
        line_pwr = get_line_pwr(power_batches)
        power_sum += line_pwr

    print("valid: ", total_valid)
    print("power sum: ", power_sum)

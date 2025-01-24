import random

# Global variable to track the current opponent
current_opponent = None

def player(prev_play, opponent_history=[]):
    global current_opponent

    # Track opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # Default to Rock for the first move
    if not opponent_history:
        return "R"

    # Strategy for Quincy
    if current_opponent == "quincy":
        quincy_sequence = ["R", "R", "P", "P", "S"]
        counter_sequence = ["P", "P", "S", "S", "R"]
        return counter_sequence[len(opponent_history) % len(quincy_sequence)]

    # Strategy for Kris
    if current_opponent == "kris":
        if not prev_play:
            return "R"  # Default to Rock for the first move
        # Kris's counter to your last move
        kris_counter = {"R": "P", "P": "S", "S": "R"}
        # Your counter to Kris's counter
        double_counter = {"P": "S", "S": "R", "R": "P"}
        move = double_counter[kris_counter[prev_play]]

        # Add randomness (50% chance of playing randomly)
        if random.random() < 0.5:
            move = random.choice(["R", "P", "S"])
        return move

    # Strategy for Mrugesh
    if current_opponent == "mrugesh":
        if len(opponent_history) > 10:
            last_ten = opponent_history[-10:]
            move_counts = {"R": last_ten.count("R"), "P": last_ten.count("P"), "S": last_ten.count("S")}
            most_frequent = max(move_counts, key=move_counts.get)
            counters = {"R": "P", "P": "S", "S": "R"}
            move = counters[most_frequent]

            # Add randomness
            if random.random() < 0.4:  # 40% chance to play randomly
                move = random.choice(["R", "P", "S"])
            return move
        return "R"

    # Strategy for Abbey
    if current_opponent == "abbey":
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
        if len(opponent_history) > 1:
            last_two = "".join(opponent_history[-2:])
            if last_two in play_order:
                play_order[last_two] += 1

            # Predict Abbey's next move
            last_move = opponent_history[-1]
            potential_plays = [last_move + "R", last_move + "P", last_move + "S"]
            sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
            if sub_order:
                prediction = max(sub_order, key=sub_order.get)[-1:]
                counters = {"R": "P", "P": "S", "S": "R"}
                move = counters[prediction]

                # Add increased randomness (50% chance to play randomly)
                if random.random() < 0.5:
                    move = random.choice(["R", "P", "S"])
                return move
        return random.choice(["R", "P", "S"])

    # Default fallback
    return random.choice(["R", "P", "S"])

import random

def detect_opponent(opponent_history):
    # Quincy: Fixed sequence ["R", "R", "P", "P", "S"]
    quincy_sequence = ["R", "R", "P", "P", "S"]
    if len(opponent_history) >= 5 and all(
        opponent_history[i] == quincy_sequence[i % len(quincy_sequence)]
        for i in range(5)
    ):
        return "quincy"

    # Kris: Always counters your last move
    if len(opponent_history) >= 3:
        counters = {"R": "P", "P": "S", "S": "R"}
        if all(opponent_history[i] == counters[opponent_history[i - 1]]
               for i in range(1, len(opponent_history))):
            return "kris"

    # Mrugesh: Counters the most frequent move in your last 10 plays
    if len(opponent_history) > 10:
        # Simulate your last 10 moves
        last_ten = opponent_history[-10:]
        move_counts = {"R": last_ten.count("R"), "P": last_ten.count("P"), "S": last_ten.count("S")}
        most_frequent = max(move_counts, key=move_counts.get)

        # Check if the opponent is consistently countering this
        counters = {"R": "P", "P": "S", "S": "R"}
        expected_moves = [counters[most_frequent] for _ in last_ten]
        if all(opponent_history[i] == expected_moves[i % len(expected_moves)]
               for i in range(-len(expected_moves), 0)):
            return "mrugesh"

    # Abbey: Uses a Markov Chain
    # Default to Abbey if no other pattern matches
    return "abbey"


def player(prev_play, opponent_history=[]):
    # Track opponent's moves
    if prev_play:git rebase --continue

        opponent_history.append(prev_play)

    # Default to Rock for the first move
    if not opponent_history:
        return "R"

    # Dynamically detect the opponent
    opponent = detect_opponent(opponent_history)

    # Strategy for Quincy
    if opponent == "quincy":
       
        quincy_sequence = ["R", "R", "P", "P", "S"]
        counter_sequence = ["P", "P", "S", "S", "R"]
        return counter_sequence[len(opponent_history) % len(quincy_sequence)]
    

    # Strategy for Kris
    if opponent == "kris":
        # Kris's predictable responses
        if prev_play == "R":
            return "S"  # Kris will play "P", so play "S" to counter
        elif prev_play == "P":
            return "R"  # Kris will play "S", so play "R" to counter
        elif prev_play == "S":
            return "P"  # Kris will play "R", so play "P" to counter
            # Add randomness (50% chance)
        if random.random() < 0.5:
            move = random.choice(["R", "P", "S"])
            print("this is kris")

        return move

    # Strategy for Mrugesh
    if opponent == "mrugesh":
        print("Testing Quincy logic")

        if len(opponent_history) > 10:
            last_ten = opponent_history[-10:]
            move_counts = {"R": last_ten.count("R"), "P": last_ten.count("P"), "S": last_ten.count("S")}
            most_frequent = max(move_counts, key=move_counts.get)
            counters = {"R": "P", "P": "S", "S": "R"}
            return counters[most_frequent]
        return random.choice(["R", "P", "S"])

    # Strategy for Abbey
    if opponent == "abbey":
        play_order = {}

        # Update play_order based on opponent history
        for i in range(len(opponent_history) - 3):
            sequence = "".join(opponent_history[i:i + 3])  # Get the 3-move sequence
            next_move = opponent_history[i + 3]  # The move that follows the sequence
            if sequence not in play_order:
                play_order[sequence] = {"R": 0, "P": 0, "S": 0}  # Initialize if missing
            play_order[sequence][next_move] += 1  # Increment the count for next_move

        # Use the last 3 moves to predict the next move
        last_three = "".join(opponent_history[-3:])  # Get the last 3 moves
        if last_three in play_order:
            # Predict the most likely next move
            predicted_move = max(play_order[last_three], key=play_order[last_three].get)
        else:
            # Random fallback if there's no data for this sequence
            predicted_move = random.choice(["R", "P", "S"])

        # Counter the predicted move
        counters = {"R": "P", "P": "S", "S": "R"}
        return counters[predicted_move]

    # Default fallback
    return random.choice(["R", "P", "S"])
def main():
    # Scores
    scores = {
        "Gryffindor": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
        "Slytherin": 0
    }

    # Q1
    try:
        q1 = int(input("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
    except ValueError:
        print("Wrong input.")
        return

    if q1 == 1:
        scores["Gryffindor"] += 1
        scores["Ravenclaw"] += 1
    elif q1 == 2:
        scores["Hufflepuff"] += 1
        scores["Slytherin"] += 1
    else:
        print("Wrong input.")
        return

    # Q2
    try:
        q2 = int(input("When I’m dead, I want people to remember me as:\n"
                       "1) The Good\n"
                       "2) The Great\n"
                       "3) The Wise\n"
                       "4) The Bold\n"))
    except ValueError:
        print("Wrong input.")
        return

    if q2 == 1:
        scores["Hufflepuff"] += 2
    elif q2 == 2:
        scores["Slytherin"] += 2
    elif q2 == 3:
        scores["Ravenclaw"] += 2
    elif q2 == 4:
        scores["Gryffindor"] += 2
    else:
        print("Wrong input.")
        return

    # Q3
    try:
        q3 = int(input("Which kind of instrument most pleases your ear?\n"
                       "1) The violin\n"
                       "2) The trumpet\n"
                       "3) The piano\n"
                       "4) The drum\n"))
    except ValueError:
        print("Wrong input.")
        return

    if q3 == 1:
        scores["Slytherin"] += 4
    elif q3 == 2:
        scores["Hufflepuff"] += 4
    elif q3 == 3:
        scores["Ravenclaw"] += 4
    elif q3 == 4:
        scores["Gryffindor"] += 4
    else:
        print("Wrong input.")
        return

    #Winning House
    print("\nScores:")
    for house, score in scores.items():
        print(f"{house}: {score}")

    max_score = max(scores.values())
    winners = [house for house, score in scores.items() if score == max_score]

    if len(winners) == 1:
        print(f"\nThe Sorting Hat assigns you to {winners[0]}!")
    else:
        print(f"\nIt's a tie! You could be in any of: {', '.join(winners)}!")

if __name__ == "__main__":
    main()

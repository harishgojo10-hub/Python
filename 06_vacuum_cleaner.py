rooms = {"A": "Dirty", "B": "Dirty"}
print("Initial state:", rooms)
for room in ["A", "B"]:
    print("Vacuum moves to room", room)
    if rooms[room] == "Dirty":
        rooms[room] = "Clean"
        print("Cleaning room", room)
print("Final state:", rooms)
print("Both rooms are clean.")

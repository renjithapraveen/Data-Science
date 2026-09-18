import random

# Step 1: Create a 5x5 grid (2D array)
grid_size = 5
grid = [["⬜" for _ in range(grid_size)] for _ in range(grid_size)]

# Step 2: Randomly hide the treasure
treasure_row = random.randint(0, grid_size - 1)
treasure_col = random.randint(0, grid_size - 1)

# Step 3: Number of chances
chances = 5

print("Welcome to the Treasure Hunt Game!")
print("Guess where the treasure is hidden in a 5x5 map!")
print("You have", chances, "chances to find it.\n")

def print_grid():
    for row in grid:
        print(" ".join(row))
    print()

# Step 4: Start the game
for attempt in range(1, chances + 1):
    print_grid()
    try:
        row = int(input(f"Attempt {attempt}: Enter row (0-4): "))
        col = int(input("Enter column (0-4): "))
        
        if row == treasure_row and col == treasure_col:
            print("\n🏆 Congratulations! You found the treasure! 🏆")
            grid[row][col] = "💰"
            print_grid()
            break
        else:
            print("❌ No treasure here! Try again.")
            grid[row][col] = "❎"
    except ValueError:
        print("Please enter valid numbers!")
else:
    print("\n Game Over! You couldn't find the treasure.")
    grid[treasure_row][treasure_col] = "💰"
    print("Here was the treasure location:\n")
    print_grid()

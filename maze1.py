maze_temp = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "E", "#"]
]

def maze_disp(maze):
    for row in maze:
        print(" ".join(row))
    print()

while True:
    maze=[row[:] for row in maze_temp]
    player=[1, 1]
    steps= 0

    while True:
        maze_disp(maze)
        move = input("Move (U/L/D/R): ").upper()
        steps += 1

      
        if move=="U":
            new=[player[0]-1, player[1]]
        elif move=="D":
            new=[player[0]+1, player[1]]
        elif move=="L":
            new=[player[0], player[1]-1]
        elif move=="R":
            new=[player[0], player[1]+1]
        else:
            print("Invalid!")
            continue

        x, y = new

        if maze[x][y]== "#":
            print("Wall!")
            continue

        if maze[x][y]== "E":
            print(f"\nCongratulations! You've reached the Exit (E) in {steps} moves!")
            break

        maze[player[0]][player[1]]= " "
        player = new
        maze[player[0]][player[1]]= "S"

    if input("Play again? (Y/N): ").upper() != "Y":
        print("Thank you for playing the Maze Escape Challenge!")
        break
# Example game world setup
game_map = [[' ' for _ in range(10)] for _ in range(10)]


class Player:
    def __init__(self, x, y, degrees):
        self.x = x
        self.y = y
        self.degrees = degrees


def move_player(player, dx, dy):
    player.x += dx
    player.y += dy


def rotate_player(player, degrees):
    player.degrees += degrees


def display_game_map(game_map, player):
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            if x == player.x and y == player.y:
                print('^' if player.degrees == 0 else 'v' if player.degrees ==
                      180 else '<' if player.degrees == 270 else '>', end=' ')
            else:
                print(game_map[y][x], end=' ')
        print()

# Example function to print the game world


def print_game_state(game_map, player):
    display_game_map(game_map, player)


if __name__ == "__main__":
    # Initialize the player at a specific position and direction
    player = Player(5, 5, 0)

while True:
    print_game_state(game_map, player)

    # Get player input
    action = input(
        "Enter a command (e.g., 'w' for up, 'a' for left, 'd' for right, 's' for down, 'r' to rotate): ")

    if action == 'w':
        move_player(player, 0, -1)
    elif action == 'a':
        move_player(player, -1, 0)
    elif action == 'd':
        move_player(player, 1, 0)
    elif action == 's':
        move_player(player, 0, 1)
    elif action == 'r':
        rotate_player(player, 90)

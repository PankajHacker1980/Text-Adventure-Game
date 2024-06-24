import time

class TextAdventure:
    def __init__(self):
        self.current_room = 'foyer'
        self.rooms = {
            'foyer': {
                'description': "You are standing in the foyer of a spooky mansion. "
                               "There are doors to the north and east.",
                'exits': {'north': 'hallway', 'east': 'dining room'}
            },
            'hallway': {
                'description': "You are in a dark hallway. You can see stairs leading up.",
                'exits': {'south': 'foyer', 'up': 'attic'}
            },
            'dining room': {
                'description': "You are in a dusty dining room with a large table.",
                'exits': {'west': 'foyer', 'north': 'kitchen'}
            },
            'kitchen': {
                'description': "You are in a creepy kitchen. There is a door to the south.",
                'exits': {'south': 'dining room'}
            },
            'attic': {
                'description': "You have climbed up to the attic. It's filled with old boxes.",
                'exits': {'down': 'hallway'}
            }
        }
    
    def play_game(self):
        print("Welcome to the Haunted Mansion Adventure!")
        print("Explore the mansion and try to find a way out.")

        while True:
            room = self.rooms[self.current_room]
            print("\n" + room['description'])
            print("Exits:", ", ".join(room['exits'].keys()))

            command = input("Enter your command (e.g., 'go north'): ").lower()
            action, direction = self.parse_command(command)

            if action == 'go':
                if direction in room['exits']:
                    self.current_room = room['exits'][direction]
                else:
                    print("You can't go that way!")
            elif action == 'quit':
                print("Thanks for playing!")
                break
            else:
                print("Invalid command! Try again.")

            time.sleep(1)  # Add a delay for readability
    
    def parse_command(self, command):
        words = command.split()
        if len(words) == 2 and words[0] == 'go':
            return 'go', words[1]
        elif command == 'quit':
            return 'quit', ''
        else:
            return '', ''

if __name__ == "__main__":
    game = TextAdventure()
    game.play_game()

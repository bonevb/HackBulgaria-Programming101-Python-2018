from controller import Controller
import sys



class Menu:
    controller = Controller()

    def start(self):
        while True:
            print('Choose from the following commnads\nshow movies\nmake reservation\nshow movie projections <movie id>\n')
            command = input("Enter command:> ")
            try:
                self.commnads(command)
            except ValueError as error:
                print(str(error) + "\n")
                cont = input("Press Enter to continue...")
                continue

        # name = input('Hello!\nMovie name:\n>>> ')
        # rating = input('\nMovie rating:\n>>> ')
        #
        # self.controller.create_movie(name, rating)
        # self.controller.show_movies()

    def commnads(self, command):
        if command == "show movies":
            self.controller.show_movies()
        elif command == "make reservation":
            self.controller.make_reservation()
        elif command.startswith("show movie projections"):
            arguments = command.split("show movie projections ")[1]
            self.controller.show_movie_projections(arguments)
        elif command == "exit":
            sys.exit()
        elif command == "help":
            pass
            # self.help()
        else:
            raise ValueError("Wrong command.")

# menu = Menu()
# menu.start()

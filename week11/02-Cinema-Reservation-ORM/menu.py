from controller_alchemy import Controller_Alchemy
from reservation import Reservation
import sys



class Menu:
    controller = Controller_Alchemy()

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

    def commnads(self, command):
        if command == "show movies":
            self.controller.list()
        elif command == "make reservation":
            Reservation.make_reservation()
        elif command.startswith("show movie projections"):
            arguments = command.split("show movie projections ")[1]
            self.controller.get_movie_id(arguments)
        elif command == "exit":
            sys.exit()
        elif command == "help":
            pass
            # self.help()
        else:
            raise ValueError("Wrong command.")

menu = Menu()
menu.start()

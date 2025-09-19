from pakudex import Pakudex
from pakuri import Pakuri

def pakudex_menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")
    

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity > 0:
                print(f"The Pakudex can hold {max_capacity} species of Pakuri.\n")
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(max_capacity)

    while True:
        pakudex_menu()
        try:
            action = int(input("What would you like to do? "))
            if action == 1:
                species_array = pakudex.get_species_array()
                if not species_array:
                    print("No Pakuri in Pakudex yet!\n")
                else:
                        print("Pakuri In Pakudex:")
                        for i, species in enumerate(species_array, start=1):
                            print(f"{i}. {species}")
                print()
            elif action == 2:
                display_species = input("Enter the name of the species to display: ")
                stats = pakudex.get_stats(display_species)
                if stats:
                    print(f"Species: {display_species}" )
                    print(f"Attack: {stats[0]} Defense: {stats[1]} Speed: {stats[2]}")
                else:
                    print("Error: No such Pakuri!\n")
            elif action == 3:

                if pakudex.get_size() >= pakudex.get_capacity():
                    print("Error: Pakudex is full!\n")
                else:
                    add_species = input("Enter the name of the species to add: ")

                    if pakudex.add_pakuri(add_species):
                        print(f"Pakuri species {add_species} successfully added!\n")
                    else:
                        print("Error: Pakudex already contains this species!\n")
       
            elif action == 4:
                ev_species = input("Enter the name of the species to evolve: ")
                result = pakudex.evolve_species(ev_species)
                if result:
                    print(f"{ev_species} has evolved!")
                else:
                    print("Error: No such Pakuri!")
                print()
            elif action == 5:
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")
                print()
            elif action == 6:
                print("Thanks for using Pakudex! Bye!")
                break
            else:
                print("Unrecognized menu selection!\n")
        except ValueError:
            print("Unrecognized menu selection!\n")
        except EOFError:
            break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()

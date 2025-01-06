import classes.Orca as o
import classes.Humpback as h

from colorama import Fore, Back, Style

def print_error(e):
    print(f'{Fore.RED}{Back.YELLOW}ERROR IN TESTING --{Style.RESET_ALL} {e}')
    

def main():
    # Create a list of whale objects
    whales = []
    whales.append(o.Orca("Big Momma", 10, 10, "pod302.4"))
    whales.append(o.Orca("Big Momma", 10, 10, "pod302.4"))
    whales.append(h.Humpback("Pete", 30, 30, 16))
    whales.append(o.Orca("Big Pappy", 5, 12, "pod302.4"))
    whales.append(o.Orca("Stripey", 16, 11, "pod302.4"))
    whales.append(h.Humpback("Quicksilver", 16, 30, 9))
    whales.append(h.Humpback("Quicksilver", 16, 30, 9))
    whales.append(h.Humpback("Hanoi", 33, 27, 17))
    whales.append(h.Humpback("Big Boy", 9, 29, 8))

    # display the number of whales created
    try:
        assert o.Orca.count == 9, f"Wrong number of whales created, expected 9 only {o.Orca.count} were"
        print (f'{o.Orca.count} whales have been created')
        print()
    except AssertionError as e:
        print_error(e)

    # loop and print out the whales and what they eat and sing
    for whale in whales:
        print(whale)
        print(f"{whale.name} sings {whale.sing()}")
        if whale.__class__.__name__ == "Orca":
            whale.eat("manta ray")
        else:
            whale.eat("krill")
        print() 

    # # compare some of the whales to see if they are the same or not
    try:
        assert whales[0] == whales[1], "Whales should be the same and are not"
        print("The first two whales are the same")
    except AssertionError as e:
        print_error(e)

    try:
        assert whales[2] != whales[3], "Whales should be the different and are not"
        print("The third and fourth whales are different")
    except AssertionError as e:
        print_error(e)

    try:
        assert whales[-1] != whales[-2], "Whales should be the different and are not"
        print("The last two whales are different")
    except AssertionError as e:
        print_error(e)

    try:
        assert whales[-3] == whales[-4], "Whales should be the same and are not"
        print("The third and fourth last whales are the same")
    except AssertionError as e:
        print_error(e)

# Only run this program if it is the running program
if __name__ == "__main__":
    main()

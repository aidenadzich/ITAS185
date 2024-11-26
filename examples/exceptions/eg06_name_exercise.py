class NameTooShort(ValueError):
    pass

class NameTooLong(ValueError):
    pass

class NameTooCute(ValueError):
    pass


def checkName(name):
    if len(name) < 6:
        raise NameTooShort(name)
    
    if len(name) > 15:
        raise NameTooLong(name)
    
    if name.lower() == 'too cute':
        raise NameTooCute(name)
    
    return('Name is just right')


while True:
    if __name__ == '__main__':
        try:
            the_name = input("Enter a name: ")
            result = checkName(the_name)
            print(result)

        except NameTooShort as e:
            print(f"Name {e} is too short")
        except NameTooLong as e:
            print(f"Name {e} is too long")
        except NameTooCute as e:
            print(f"Name {e} is too cute")
    

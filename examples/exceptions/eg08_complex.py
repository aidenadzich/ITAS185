import os

def read_file():

    while True:
        try:
            file_name = input('Enter your file name: ').strip()

            with open(file_name, 'r') as file:
                print(f'\nContents of {file_name}')
                print('-' * 40)

                while True:
                    try:
                        line = file.readline().strip()
                        if not line:
                            raise EOFError('End of file reached')
                        print(line)
                    except EOFError as e:
                        print('-' * 40)
                        print(e)
                        print('-' * 40)

                        break

        except FileNotFoundError:
            print(f"File {file_name} does not exist")
            print("Please try again")
        
        except PermissionError:
            print(f"No permissions to access {file_name}")

        except IOError as e:
            print(f"An error has occured: {e}")

        except KeyboardInterrupt:
            print("Goodbye!")
            exit(0)

        except:
            print("An unexpeced error has occured")

if __name__ == '__main__':
    read_file()

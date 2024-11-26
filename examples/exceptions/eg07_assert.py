print("Checking asserations")

while True:
    x = input('Enter a number (q to quit): ')
    if x.lower == 'q':
        break
    try:
        x = int(x)
        assert x > 0, "Age must be greater than zero"
        assert x < 120, "Nobody lives that long"
        if x % 2 == 0:
            print('Age is even')
        else:
            print('Age is odd')
    except ValueError as e:
        print(e)
    except AssertionError as e:
        print(e)
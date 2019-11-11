try:
    count = int(input('How many number you want to capture: '))
    numList = []
    for i in range(count):
        msg = 'Enter number #' + str(i+1) + " "
        try:
            num = int(input(msg))
            numList.append(num)
        except ValueError:
            print("Input must be a number!")
    try:
        print('The lowest number in the list:', min(numList))
        print('The highest number in the list:', max(numList))
        print('The total of the number in the list:', sum(numList))
        print('The average of the number in the list:', sum(numList)/len(numList))
    except:
        print("List cannot be empty!")
except ValueError:
    print("Input must be a number!")

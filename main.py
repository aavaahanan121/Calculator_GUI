def find(Input: str):
    Input = [x for x in Input]
    array = []
    for letter in Input:
        try:
            int(letter)
            try:
                int(array[-1])
                array[-1] = str(array[-1]) + letter
            except IndexError:
                array.append(int(letter))

        except ValueError:
            array.append(letter)

    for index in range(len(array)):
        try:
            array[index] = int(array[index])

        except ValueError:
            pass

    index = 0
    while index < len(array):
        if isinstance(array[index], str):

            # if adding
            if array[index] == "+":
                array[index - 1] = array[index - 1] + array[index + 1]
                del array[index]
                try:
                    del array[index]
                except IndexError:
                    pass
                index -= 2

            # if subtracting
            if array[index] == "-":
                array[index - 1] = array[index - 1] - array[index + 1]
                del array[index]
                try:
                    del array[index]
                except IndexError:
                    pass
                index -= 2

            # if dividing
            if array[index] == "/":
                array[index - 1] = array[index - 1] / array[index + 1]
                del array[index]
                try:
                    del array[index]
                except IndexError:
                    pass
                index -= 2

            # if multiplying
            if array[index] == "*":
                array[index - 1] = array[index - 1] * array[index + 1]
                del array[index]
                try:
                    del array[index]
                except IndexError:
                    pass
                index -= 2

        index += 1

    return array

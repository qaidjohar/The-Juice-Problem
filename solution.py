
def readFile(filename):
    fileData = []
    with open(filename) as my_file:
        for line in my_file:
            fileData.append(line[:-1])
    return fileData


def writeFile(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()


def f(calories_list, i, intake_calories, memo):
    if i >= len(calories_list):
        return 1 if intake_calories == 0 else 0
    # <-- Check if value has not been calculated.
    if (i, intake_calories) not in memo:
        count = f(calories_list, i + 1, intake_calories, memo)
        count += f(calories_list, i + 1, intake_calories -
                   calories_list[i], memo)
        memo[(i, intake_calories)] = count  # <-- Memoize calculated result.
        # print(memo[(i, S)])
    return memo[(i, intake_calories)]     # <-- Return memoized value.


def getSumList(calories_list, intake_calories, memo):
    subset = []
    for i, x in enumerate(calories_list):
        # Check if there is still a solution if we include calories_list[i]
        if f(calories_list, i + 1, intake_calories - x, memo) > 0:
            subset.append(x)
            intake_calories -= x
    return subset


def getJuiceChars(calories_sum_list, calories_list, juice_list):
    # print(juice_list)
    final_juice_list = []
    for i in range(len(calories_list)):
        if calories_sum_list[0] == calories_list[i]:
            calories_sum_list.pop(0)
            final_juice_list.append(juice_list[i])
        if(len(calories_sum_list) == 0):
            break
    # print(final_juice_list)
    final_juice_str = ''.join(str(e) for e in final_juice_list)
    # print(final_juice_str)

    return final_juice_str


'''
friends_count = 3
juice_calories [21 1 21 3 3]
unique_juice_count = 5
juice_list = ['a', 'a', 'a', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'e', 'e', 'e', 'e']
unique_juice_list = ['a', 'b', 'c', 'd', 'e']
dict_juice_calories = {'a': '21', 'b': '1', 'c': '21', 'd': '3', 'e': '3'}
'''

if __name__ == "__main__":
    fileData = readFile('sampleinput.txt')
    output = ""
    # print(fileData)
    friends_count = int(fileData.pop(0))
    # print("friends_count ", friends_count)
    for i in range(friends_count):
        juice_calories = fileData.pop(0).split(" ")
        unique_juice_count = juice_calories.pop(0)
        # print(juice_calories, "count=", unique_juice_count)
        juice_list = []
        juice_list[:0] = fileData.pop(0)
        juice_list = sorted(juice_list)
        # print(juice_list)
        unique_juice_list = sorted(list(set(juice_list)))
        # print(unique_juice_list)
        dict_juice_calories = {
            unique_juice_list[i]: juice_calories[i] for i in range(len(unique_juice_list))}
        # print(dict_juice_calories)
        calories_list = [int(dict_juice_calories[val]) for val in juice_list]
        # print(calories_list)
        intake_calories = int(fileData.pop(0))
        # print(intake_calories)
        memo = dict()
        if f(calories_list, 0, intake_calories, memo) == 0:
            print("SORRY, YOU JUST HAVE WATER")
            output += "SORRY, YOU JUST HAVE WATER\n"
        else:
            calories_sum_list = getSumList(
                calories_list, intake_calories, memo)
            final_juices = getJuiceChars(
                calories_sum_list, calories_list, juice_list)
            print(final_juices)
            output += final_juices+"\n"
    writeFile("sampleoutput.txt", output)

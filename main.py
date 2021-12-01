
def main():
    #list = 1 -> TypeError
    list = [7, 3, 0, 1, 5, 2, 1, "怪獣", 3.14, False]
    mean, list = _mean(list)
    print(mean, list)

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def _mean(list):
    try:
        for element in list:
            if not type(element) in (int, float):
                return None, list
        
        while not is_sorted(list):
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    tmp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = tmp
        if len(list) % 2 == 0:
            mean = (list[int(len(list)/2)] + list[int(len(list)/2 - 1)])/2
        else:
            mean = list[int((len(list)-1)/2)]
        return mean, list
    except TypeError:
        print("TypeError: variable 'list' must be list object")

if __name__ == "__main__":
    main()
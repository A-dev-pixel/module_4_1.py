from fake_math import divide as am2
from true_math import divide as am3
if __name__ == '__main__':
    result1 = am2(69, 3)
    result2 = am2(3, 0)
    result3 = am3(49, 7)
    result4 = am3(15, 0)
    print(result1)
    print(result2)
    print(result3)
    print(result4)

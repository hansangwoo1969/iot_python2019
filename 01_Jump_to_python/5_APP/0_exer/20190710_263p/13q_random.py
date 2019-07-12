import random

def random_pop():
    number = random.randint(1, 46)
    return (number)

# def random_pop(data):
#     number = random.choice(data)
#     data.remove(number)
#     return number

if __name__=="__main__":
    for i in range(6):
        print(random_pop())

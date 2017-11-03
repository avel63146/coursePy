guess_me = 7
start = 1
qq_list = []
dictionary = {}

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
elif guess_me == 7:
    print('just right')

while True:
    if guess_me > start:
        print(start, 'too low')
    elif guess_me < start:
        print(start,'oops')
        break
    elif guess_me == start:
        print(start,'found it')
        break
    start += 1

qq_list = list(range(3,-1,-1))
print(qq_list)

for qq in range(1,11):
    if qq%2 == 1:
        qq_list.append(qq)
print(qq_list)

qq_list_two = [qq for qq in range(1,11) if qq%2 == 1]
print(qq_list_two)

del qq_list
qq_list = []
for sqr in range(1,11):
    dictionary = {sqr:sqr*2}
    qq_list.append(dictionary)
print(qq_list)

odd = {num for num in range(0,11,2) }
print(odd)

strin = 'Got'
del qq_list
qq_list = [range(1,10),strin]
generator = (gen for gen in qq_list)
for qq in generator:
    print(qq)

list = ['Harry', 'Ron', 'Hermione']
def good (list):
    return list
print(good(list))

def test(func):
    def spc():
        print('_______________')
        func
        print('_______________')
    return spc()

def get_odds(x):
    for qq in range(0,11,2):
        print(qq)
        if qq == x:
            break
    return x
tester = test(get_odds(6))

class OopsException(Exception):
    pass
try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nunturns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles,plots))
print (movies)
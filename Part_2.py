years_list = [1998, 1999, 2000, 2001, 2002]
print(years_list[3])
print(max(years_list))

things = ['mozzarella', 'cinderella', 'salmonella']
print(things)
cin = things[1].capitalize()
things[1] = cin
moz = things[0].upper()
things[0] = moz
del things[2]
print(things)

surprise = ['Grouch', 'Chico', 'Harpo']
print(surprise[2].lower())
print(surprise[2].title())

e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)
print(e2f['walrus'])
f2e = {'chien':'dog', 'chat':'cat', 'morse':'walrus'}
print(f2e.items())
print(f2e['chien'])
print(set(e2f))

cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats':cats, 'octopi':'', 'emus':''}
plants = {}
other = {}
life = {'animals':animals, 'plants':plants, 'other':other}
print(life)
print(life['animals'])
print(life['animals']['cats'])
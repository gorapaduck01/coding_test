word = input()
count = len(word)


count -= word.count('c=')
count -= word.count('c-')
count -= word.count('dz=')
count -= word.count('d-')
count -= word.count('lj')
count -= word.count('nj')
count -= word.count('s=')
count -= word.count('z=')


print(count)
f = open('myfile.txt', 'w')
f.write('Hello, Dharmik Dodiya!')


f = open('myfile.txt', 'a')
f.write('Hello, world! and Dharmik Dodiya')

f = open('myfile.txt', 'r')
contents = f.read()
print(contents)

f.close()

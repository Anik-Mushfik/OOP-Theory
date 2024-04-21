def my_gen():
    yield 1
    yield 2
    yield 4

for i in my_gen():
    print(i)


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
csv_gen = csv_reader("D:\Python Study\OOP-Theory\Self_study\Generator\some.txt")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#  You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    new_line = line.split(" ")
    output_line = "-".join(new_line)
    return output_line

line = input("enter the space separated string: ")
print(split_and_join(line))
# Name: Jamar Hill
# Date: 5/1/2021
# Description: Project 5A

def file_sum(filename):#file_sum function (followed by parenthesis), filename variable
    total = 0
    with open(filename, 'r') as my_file:#open = syntax for opening a file. r = read
        for line in my_file:
            #numbers = line.split(',')#Takes a string and slips at comma
            #for num in numbers:
            total += float(line)
    with open ('sum.txt','w') as outfile:
        outfile.write(str(total)) #outfile represents a file object in Python (write)
    my_file.close()
    outfile.close()
    return total

file_sum('numbers.txt')


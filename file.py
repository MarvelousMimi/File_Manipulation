# A file is a named location on a secondary storage media where data is permanently stored for later access

# File Manipulation (1)
# Open the file using the function  open()
# It takes in ywo parameters, the text file name and the access mode. Ie Reading, writing, appendinf to the document

# method 1
# openfile = open("./story.txt", "r")
# print(openfile)
# method 2
# with open("./story.txt","r") as openfile:
#     print(openfile)
    
# read the file using the read  keyword:  read()

openfile = open("./story.txt", "r")
read_file = openfile.read()
print(read_file)

# Split each sentence into word using the keyword: split()

# def readfile(filenmae):
#     with open("./story.txt","r") as openfile:
#         read_file = openfile.read()
#     return read_file

# def countwords():
#     text = readfile("./story.txt")
#     split_text = text.split()
#     print(split_text)
    
# countwords()

#  Create a Dictionary that will store the value of each word using    count{}

# def readfile(filenmae):
#     with open("./story.txt","r") as openfile:
#         read_file = openfile.read()
#     return read_file

# def countwords():
#     text = readfile("./story.txt")
#     split_text = text.split()
#     count = {}
    
# countwords()

# Make use of for loop that will go over every word in the list 
# We will store each word and check how many times it occrs

# def readfile(filenmae):
#     with open("./story.txt","r") as openfile:
#         read_file = openfile.read()
#     return read_file

# def countwords():
#     text = readfile("./story.txt")
#     split_text = text.split()
#     count = {}
#     for i in split_text:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     return count
       
# print(countwords())

# To create a new txt file

# new_file = open("zuri.txt","w")
# print(new_file)
# write = "w", read = "r", append ="a"

# To read the file
# new_file = open("zuri.txt","w")
# open_file = new_file.read()
# print(open_file)

# to be able to write, We will use the write function write() to write in a file

# new_file = open("zuri.txt","w")
# write_file= "Hello I am in Zuri Training"
# final_doc = new_file.write(write_file)
# new_file.close()    #we used this .close() to save
# print(final_doc)

# To read the file 
# new_file = open("zuri.txt","r")
# read_file = new_file.read()
# print(read_file)

# # To append
# new_file = open("zuri.txt","a")
# write_file = "Hi there, I am enjoying myself"
# add_file = new_file.write(write_file)
# new_file.close()
# print(add_file)

# # to read
# new_file = open("zuri.txt","r")
# read_file = new_file.read() 
# print(read_file)

# Summation of everything we were learning
def read_file(filename):
    openfile = open("./story.txt","r")
    read_file = openfile.read()
    # print(read_file)
    new = read_file.split()
    # print(new)
    count ={}
    for i in new:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(read_file("./story.txt"))
# f = open("file_example.txt", "r")
# data = f.read()
# print(data)
# f.close()


# with open("sample_file.txt", 'a') as f:
    
#     data = f.write("It might be the 1st paragraph")

# f.close()

## new way to open file

with open("file_example.txt","w" ) as f:
    f.write("Hello world, \n I am learning python")
    f.write("I am using this first time. \n Are you new here? \n You can learn moreparts you have ever imagine")
    
    
# find word line by line

def finding_word_linebyline():
    word = "new"
    data = True
    line_no = 1
    with open("file_example.txt","r" ) as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1

print(finding_word_linebyline())        
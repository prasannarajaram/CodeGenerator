# this file will be used to write functions to learn here and implement in the main code

# import fileinput
# import in_place
# find replace text in a file - working module! 
def file_edit():
    import fileinput
    filename = "write.txt"
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("te", "as"), end='')

def my_func():
    print("Hello")

def find_replace():

    template = open("sample_template.txt","r")
    sample1 = open("sample1.txt","a")
    sample1.write(template.read())
    sample1.close()
    filename = "sample1.txt"
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            line.replace("<<name>>", "Prasanna")
            line.replace("<<profession>>", "Engr") 
    template.close()
    # sample1.close()

def append_template_to_code():
    with open("sample_template.txt","r") as source:
        with open("sample1.txt","a") as dest:
            for line in source:
                dest.write(line)
    with in_place.InPlace('sample1.txt') as file:
        for line in file:
            line = line.replace('<<name>>', 'Prasanna')
            file.write(line)            
            line = line.replace('<<profession>>', 'Engr')
            file.write(line) 
    dest.close()
    source.close()
                
def tag_replace():
#    filename = "sample1.txt"
#    with fileinput.FileInput(filename, inplace=True) as file:
#        for line in file:
#            print(line.replace("<<name>>", "PRASANNA"), end = '')
#            print(line.replace("<<profession>>", "Engr"), end ='')        
    in_file = open('ifd03b.txt','r')
    str1 = in_file.read()
    str2 = str1.replace('<<TagName>>',':PIT82408')
    out_file = open('output.txt','a')
    out_file.write(str2)


           

# append_template_to_code()
tag_replace()
# my_func()
# file_edit()
# find_replace()


def counter():
    num_words = 0       
    num_lines = 0                
    num_charc = 0                
    num_spaces = 0
    my_file = open("musku.txt","r")
    f = my_file.read()
    files=f.split("\n")
    for line in files:
        num_lines += 1        
        for letter in line:            
            if (letter == ' '):
                num_spaces += 1                
            for i in letter:
                if(i !=" " and i !="\n"):
                    num_charc += 1
    print("Number of lines in text file: ", num_lines)
    print('Number of characters in text file: ', num_charc)
    print('Number of spaces in text file: ', num_spaces)
counter()   
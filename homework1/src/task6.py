def task6_read_file():
    file = open('task6_read_me.txt','r')
    content = file.read()
    print(content)
    arr = content.split(' ')
    return(len(arr))
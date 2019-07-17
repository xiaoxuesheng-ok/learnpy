import os


COMMENT_FILE_PATH = 'test.txt'

title = "this is a test sentence"

if os.path.exists(COMMENT_FILE_PATH) :
    os.remove(COMMENT_FILE_PATH)


with open(COMMENT_FILE_PATH,'a+') as file :

    file.write(title+"\n")
    print(title,"\n")
    file.close()



with open(COMMENT_FILE_PATH,'r',encoding='UTF-8') as f :

    result = f.read()
    print(result)

import os

root_child = r'C:\Users\lxr\Desktop\人脸识别项目\aishiguang-emotion\aishiguang-child-emotion'
root_adult = r'C:\Users\lxr\Desktop\人脸识别项目\aishiguang-emotion\aishiguang-adult-emotion'

child_dir = './doc/child'
adult_di = './doc/adult'

cls = ['netrual', 'surprise', 'happy', 'sad', 'fear', 'disgust', 'anger']

# 读取文件中
def getdata(dir):
    data = []
    txts = os.listdir(dir)
    for txt in txts:
        edata = {}
        txt_path = os.path.join(dir, txt)
        f = open(txt_path, 'r')
        line = f.readline().rstrip('\n')
        while line:
            line = f.readline().rstrip('\n')
            if line[0] == '#':
                line.index(line[1])


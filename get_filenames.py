#获取当前文件夹下所有文件名称
import os

def getNameList(path):
    """
    type[path] : str
    rtype: list[str]
    """
    name_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            name_list.append(name)
    return name_list

def saveNameList(name_list):
    with open('name_list.txt', 'ab') as f:
        for name in name_list:
            name = name
            f.write(name.encode('utf-8'))
            f.write(b'\n')
        f.close()

def main():
    r = getNameList('./')
    print(len(r))
    saveNameList(r)

if __name__ == '__main__':
    main()
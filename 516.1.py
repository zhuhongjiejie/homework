with open('attack.csv', 'r') as file:
    content = file.read()
    print(content)
# 文件会在with语句块执行完毕后自动关闭
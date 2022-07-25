list1=['ayaz','wajahat','kashif','amir']
new_list=[(x[-2:].upper(),x[1:3].upper()) for x in list1]
print(new_list)
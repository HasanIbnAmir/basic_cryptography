x=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x']
x1=input("Enter the text:")


i1=0
# print(x.index('o'))
for i in x1:
    index=x.index(f'{i}')
    print(x[index+1],end="")

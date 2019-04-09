def longest_slide_down(pyramid):
    for small_pyramid in pyramid:
        return

def two_slide_down(pyramid):
    new_pyramid=[]
    for i in range(len(pyramid[1])):
        li=[]
        if 0< i<len(pyramid[1])-1:
            li.append(pyramid[0][i-1]+pyramid[1][i])
            li.append(pyramid[0][i]+pyramid[1][i])
            new_pyramid.append(li)
        elif i==0:
            li.append(pyramid[0][i]+pyramid[1][i])
            new_pyramid.append(li)
        elif i==len(pyramid[1])-1:
            li.append(pyramid[0][i-1]+pyramid[1][i])
            new_pyramid.append(li)
    return new_pyramid


def third_slide_down(pyramid):
    for x in range(len(pyramid)):
        if len(pyramid)>1:
            new_pyramid=[]
            if x==0:
                new_pyramid=two_slide_down(pyramid)
            elif x>0:
                for i in range(len(pyramid[1])):
                    li=[]
                    if 0< i < len(pyramid[1]) - 1:
                        for j in pyramid[0][i-1]:
                            li.append(j+pyramid[1][i])
                        for j in pyramid[0][i]:
                            li.append(j+pyramid[1][i])
                    elif i==0:
                        for j in pyramid[0][0]:
                            li.append(j+pyramid[1][i])
                    elif i == len(pyramid[1]) - 1:
                        for j in pyramid[0][-1]:
                            li.append(j+pyramid[1][-1])
                    new_pyramid.append(li)
            del pyramid[0]
            del pyramid[0]
            pyramid.insert(0,new_pyramid)
            print(pyramid)
        else:
            return max([k for i in pyramid for j in i for k in j])


ff=two_slide_down([[1,2,3],[2,3,4,5]])
print(ff)
print(third_slide_down([[1],[1,2],[1,2,3]]))
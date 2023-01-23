#def value(colors):
#    x= color_code(colors[0])
#    y= color_code(colors[1])
#    z=(x*10)+y
#    return z
                  
                  
#def color_code(color):
#    y=(color.lower())
#    if(y=="black"):
#        return 0
#    elif(y=="brown"):
#        return 1
#    elif(y=="red"):
#        return 2
#    elif(y=="orange"):
#        return 3
#    elif(y=="yellow"):
#        return 4
#    elif(y=="green"):
#        return 5
#    elif(y=="blue"):
#        return 6
#    elif(y=="violet"):
#        return 7
#    elif(y=="grey"):
#        return 8
#    elif(y=="white"):
#        return 9
#    else:
#        return "RaiseValueError"

def value(colors):
    x = color_code(colors[0])
    y = color_code(colors[1])
    z = (x*10)+y
    return z

def color_code(color):
    thisdict  = {"black" : 0 , "brown" : 1 , "red" : 2 , "orange" : 3 , "yellow" : 4 , "green" : 5 , "blue" : 6 , "violet" : 7 , "grey" : 8 , "white" : 9}
    return thisdict[color]

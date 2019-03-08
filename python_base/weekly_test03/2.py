def myprint(dict) :
    return dict['height']

def myindex(dict) :
    if 'height' in dict.keys() :
        return True

people = [{'name':'Mary','height':160},{'name':'Isla','height':80},{'name':'Sam'}]
print([j for j in map(myprint,[i for i in filter(myindex,people)])])

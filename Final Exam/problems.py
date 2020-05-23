def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    usInt = int(us_num)

    if (usInt <= 10):
        return trans[us_num]
    elif (usInt <= 19):
        return 'shi ' + trans[us_num[1]]
    else:
        if (us_num[1] != '0'):
            return trans[us_num[0]] + ' shi ' + trans[us_num[1]]
        else:
            return trans[us_num[0]] + ' shi'



class Person(object):
    def __init__(self, name):
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name

        self.age = None

    def getLastName(self):
        return self.lastName

    def setAge(self, age):
        self.age = age

    def getAge(self):
        if (self.age == None):
            raise ValueError

        return self.age

    def __lt__(self, other):
        if (self.lastName == other.lastName):
            return self.name < other.name

        return self.lastName < other.lastName

    def __str__(self):
        return self.name

class USResident(Person):
    '''
    A Person who resides in the US.
    '''
    def __init__(self, name, status):
        '''
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        '''
        stata = ['citizen', 'legal_resident', 'illegal_resident']

        if (status in stata):
            Person.__init__(self, name)
            self.status = status
        else: 
            raise ValueError

    def getStatus(self):
        '''
        Returns the status
        '''
        return self.status




class ASet(Container):
    def remove(self, e):
        '''
        assumes e is hashable
        removes e from self
        '''
        try:
            del self.vals[e]
        except:
            pass

    def is_in(self, e):
        '''
        assumes e is hashable
        returns True if e has been inserted in self and
        not subsequently removed, and False otherwise.
        '''
        try:
           if (self.vals[e] != 0):
            return True
           else:
            return False
        except:
            return False




def largest_odd_times(L):
    '''
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    '''
    newSet = set(L)

    while len(newSet) > 0:
        result = max(newSet)

        if ((L.count(result) % 2) != 0):
            return result
        else:
            newSet.remove(result)


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    temp = {}
    result = []

    for value in aDict.values():
        if (value in temp.keys()):
            temp[value] += 1
        else:
            temp[value] = 1

    for key in aDict.keys():
        if (temp[aDict[key]] == 1):
            result.append(key)

    return sorted(result)

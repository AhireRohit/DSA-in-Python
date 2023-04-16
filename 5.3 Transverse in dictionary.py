myDict = {"Name" : "Rohit", "age" : 20, "college" : "MET"}
# print(myDict)

def transverseDict(dict):
    for key in dict:
        print(key, dict[key])
transverseDict(myDict)
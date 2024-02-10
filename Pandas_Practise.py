import pandas

mydataset = {
    'family_members' : ["Syam","Urmila","Rushanth","Yoswika"],
    'ages' : ["40","30","10","5"]
    }

myvar = pandas.DataFrame(mydataset)
print(myvar)
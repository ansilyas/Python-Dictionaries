#%%
# Dictionaries Method ( {} )::
student={"Alice":25,"Bob":27,"Ans":19,"Ali":20,"Dan":22,}
student["Alice"]
student["Don"]=26
student["Don"]
student.keys()
student.values()
student.items()
# %%
#Create list inside the Dictionaries:
student={
"Alice":["D001",26,"A"],
"Bob":["D002",29,"B"],
"Ans":["D003",19,"A"],
"Ali":["D004",21,"F"],
"Dan":["D005",24,"C"],
}
print(student["Ans"])
print(student["Dan"][:2])
# %%
#Dictionaries with out list:
student={
"Alice":{"Id":"D001","age":26,"Grade":"A"},
"Bob":{"Id":"D002","age":24,"Grade":"B"},
"Ans":{"Id":"D003","age":19,"Grade":"C"},
"Ali":{"Id":"D004","age":20,"Grade":"F"},
"Dan":{"Id":"D005","age":21,"Grade":"A"},
}
print(student["Ali"]["age"])
print(student["Alice"]["Id"],student["Alice"]["Grade"])
# %%

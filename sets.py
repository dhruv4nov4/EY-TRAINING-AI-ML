set_a = {"Rahul","Priya","Amit"}
set_b = {"Amit","Sneha","Priya"}
print(set_a & set_b) # intersection
print(set_a | set_b) #union
print(set_a - set_b) # difference

# list to set to make unique
name = ["rahul","priya","Amit","rahul"]
unique_name = set(name)
print(unique_name)
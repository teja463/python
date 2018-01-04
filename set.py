
list_a = ["pramod", "imran", "chaitu", "seenu", "pramod", "chaitu"]
list_b = ["pramod", "chaitu", "ravi", "thonda", "puli"]
print (list_a, type(list_a))
print (list_b, type(list_b))

set_a = set(list_a)
set_b = set(list_b)

print (set_a, type(set_a))
print (set_b, type(set_b))

print ("Union -> ", set_a.union(set_b))
print ("Intersection -> ", set_a.intersection(set_b))
print ("A - B", set_a.difference(set_b))
print ("B - A", set_b.difference(set_a))
print ("Symmetric Difference", set_a.symmetric_difference(set_b))

print ("Union -> ", set_a | set_b)
print ("Intersection -> ", set_a & set_b)
print ("A - B", set_a - set_b)
print ("B - A", set_b - set_a)
print ("Symmetric Difference", set_a ^ set_b)


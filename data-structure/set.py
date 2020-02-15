
# basic functions of set
# no duplicates allowed in set, elements are unordered

fruit_set = {"apple", "banana", "cherry"}

for x in fruit_set:
    print(x)

print("kiwi" in fruit_set)

fruit_set.add("orange")
print(fruit_set)

fruit_set.add("orange")     # nothing inserted
print(fruit_set)

fruit_set.remove("cherry")
print(fruit_set)

# fruit_set.remove("xxx")   # removing a non-existent element raises an error
fruit_set.discard("xxx")    # discard() does not raise an error
print(fruit_set)


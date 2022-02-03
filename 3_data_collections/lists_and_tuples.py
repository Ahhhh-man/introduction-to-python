# Create Shopping List

shoppping_list = ["alpha", "beta", "gamma", "delta", "epsilon"]
print(shoppping_list)

# checking the data type of this list
print(type(shoppping_list))

# Using indexing for selective entries in the list
print(shoppping_list[1])

# Change entry of an index
shoppping_list[0] = "not alpha"
print(shoppping_list[0])
print(shoppping_list[0:3])

# Adding to the list
shoppping_list.append("omega")
print(shoppping_list)

# Remove from the list
shoppping_list.remove("gamma")
print(shoppping_list)

shoppping_list.pop(3)
print(shoppping_list)


# Mixed list
mixed_list = ["Hello", 10 , 2.5]
print(mixed_list)

## Tuples
essentials = 'apple', 'banana', 'orange',
print(essentials)
print(type(essentials))

# Remark: List are mutable, however tuples are not. Hence you cannot change, add or remove the data for tuples.
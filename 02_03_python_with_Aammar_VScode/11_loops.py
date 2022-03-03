# while and for loops
# while loops

# x=0
# while (x<5):
#     print(x)
#     x=x+1

# for loops

# for x in range(5,10):
#     print(x)

# array
days = ("mon", "tue", "wed", "thus", "fri", "sat", "sun")

for d in days:
    # if (d=="fri"):break
    if (d=="fri"): continue #it skips d (friday excluded)
    print(d)
# Strings
# Concatenation
#   2 or more strings and put them together

firstName = "Will"
lastName = "Walker"
print(firstName + " " + lastName)
name = firstName + " " + lastName
lastFirst = lastName + "," + firstName
print(lastFirst)

# Repitition
#   repetition operator: *
print("Hip"*4 + "Hooray!")
def sailYourBoat():
    print("Row,"*3 + "your boat")
    print("Gently down the stream")
    print("Merrily,"*4)
    print("Life is but a dream")

sailYourBoat()

# Indexing
name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing
print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

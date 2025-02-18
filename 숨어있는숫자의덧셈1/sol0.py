words = "aAb1B2cC34oOp"

vowels = 'aAbBcCoOp'
result = [char for char in words if char not in vowels]
print(result)
print(''.join(result))
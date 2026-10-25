words = ["ai", "python", "data"]

#list of squares

squares = [x * x for x in range(1,11)
 if x % 2==0 ]
print(squares)

#Dict mapping

lengths = {w: len(w) for w in ["ai", "python","data"]} 
print(lengths)

#unique letter
letters=sorted({letters for letters in "banana"})
print(letters)
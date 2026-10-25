numbers = [4, 8, 15, 16, 23, 42]

def stats(nums):
 return min(nums), max(nums),sum(nums)/len(nums)

#unpack the result

lo,hi,avg=stats(numbers)
print(lo,hi,avg)

#for grading

def grade(marks, passing=50):
 return "Pass" if marks >= passing else "Fail"
print(grade(55),grade(55,passing=60))
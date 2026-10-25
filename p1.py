marks = [88, 45, 92, 67, 30, 75]

#for count 50 or more

count=0
for m in marks:
    if  m>=50:
        count+=1
print("Passed:",count)

#for Average

Average=sum(marks)/len(marks)
print(f"Average:{Average:.1f}")

#For highest and lowest 

print("Highest:",max(marks),"Lowest:",min(marks))

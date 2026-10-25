sentence = "the cat and the hat and the bat"

#split the sentence into words 

words=sentence.split()


#count each word in a dict

counts={}
for word in words:counts[word]=counts.get(word,0)+1
print(counts)

#most common words and its count 

print(max(counts,key=counts.get), counts[max(counts,key=counts.get)])
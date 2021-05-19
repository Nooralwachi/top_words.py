from collections import defaultdict
def top_words(filename):
	words_count=defaultdict(int)
	with open(filename, 'r') as f:
		for line in f:
			words= line.strip().split()
			for word in words:
				words_count[word]+=1
	sorted_words=sorted(words_count.items(), key=lambda x:x[1], reverse=True)
	value=c=0
	for (word,count) in sorted_words:
		c+=1
		if c<4 or count==value:	
			print(word, count)
			value=count

top_words('word.txt')
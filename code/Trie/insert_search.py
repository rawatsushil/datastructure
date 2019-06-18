# Python program for insert and search 
# operation in a Trie 

class TrieNode: 
	
	# Trie node class 
	def __init__(self): 
		self.children = {}

		# isEndOfWord is True if node represent the end of the word 
		self.is_end_of_word = False

class Trie: 
	
	# Trie data structure class 
	def __init__(self): 
		self.root = self.get_node() 

	def get_node(self): 
	
		# Returns new trie node (initialized to NULLs) 
		return TrieNode() 

	def insert(self, word): 
		
		# If not present, inserts key into trie 
		# If the key is prefix of trie node, 
		# just marks leaf node 
		root = self.root
		for key in word: 
			child = root.children.get(key) 

			# if current character is not present 
			if not child: 
				root.children[key] = self.get_node() 
			root = root.children[key]

		root.is_end_of_word = True

	def search(self, word):
		root = self.root
		for index in range(len(word)):
			if root.children.get(word[index]) != None:
				if (root.children[word[index]].is_end_of_word == True and 
					index == len(word)- 1):
					return True
				root = root.children[word[index]]
			else:
				return False
		return False


# driver function 
def main(): 

	# Input keys (use only 'a' through 'z' and lower case) 
	keys = ["the","a","there","anaswe","any", 
			"by","their"] 
	output = ["Not present in trie", 
			"Present in trie"] 

	# Trie object 
	t = Trie() 

	# Construct trie 
	for key in keys: 
		t.insert(key)

	print("{} ---- {}".format("the",output[t.search("the")])) 
	print("{} ---- {}".format("these",output[t.search("these")])) 
	print("{} ---- {}".format("their",output[t.search("their")])) 
	print("{} ---- {}".format("thaw",output[t.search("thaw")])) 

if __name__ == '__main__': 
	main() 

# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007) 

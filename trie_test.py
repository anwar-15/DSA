import json
from pprint import pprint

class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()    
        
    def add_word(self, word):

        curr_node = self.root
        for letter in word:
            new_node = curr_node.children.get(letter)

            if new_node is None:
                new_node = TrieNode()
                curr_node = curr_node.children.update({letter: new_node})

            curr_node = new_node
        curr_node.is_word_end = True
        print('Success!!') 

    def search_word(self, word):
        curr_node = self.root
        if curr_node is None:
            return False
        for letter in word:
            if 
        curr_node.children.pop(letter)
            # if new_node is None:
                #print(curr_node.children.pop(letter))
            # print(f" {letter} --->{len(curr_node.children)}")
            


    # def delete_word(self, root, word, index = 0):
    #     char = word[index]
    #     curr_node = root.children.get(char)
    #     while index < len(word) - 2:
    #         curr_node = curr_node.children.get(word[index])
    #         index+=1
        

        

if __name__ == '__main__':

    trie_obj = Trie()
    for word in ['API']:
        trie_obj.add_word(word)
        #print(f"lenght of dict after adding {word} ----> {len(trie_obj.root.children)}")    
        
# pprint(MyJsonEncoder().encode(trie_obj))
# json_data = json.dumps(trie_obj, default = lambda obj: obj.__dict__, indent = 2)
# print(json_data)

for word in ['API']:
    trie_obj.search_word(word)
    print("-------------------------------->")

json_data = json.dumps(trie_obj, default = lambda obj: obj.__dict__, indent = 2)
print(json_data)  




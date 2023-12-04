#This is Trie Data Structure
#TODO: delete an entry from the trie
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
            new_node = curr_node.children.get(letter)
            if new_node is None:
                return False
            curr_node = new_node
            
        if curr_node.is_word_end == True:
            return True
        else:
            return False

    def is_empty(self, curr_node):
        if len(curr_node.children) == 0:
            return True
        return False            

    # def delete_word(self, root, word, index = 0):
    #     # if index > len(word):
    #     #     return False
    #     char = word[index]
    #     can_node_be_deleted = False
    #     try:
    #         curr_node = root.children.get(char)

    #     except KeyError:
    #         print(f" {word} doesn't exist in this trie")
    #         return 
        
    #     else:        
    #         if index < len(word) - 1:
    #             can_node_be_deleted = self.delete_word(curr_node, word, index+1)

    #     json_data = json.dumps(curr_node, default = lambda obj: obj.__dict__, indent = 2)
    #     print(json_data)

    #     print("-----------------------------------------------------------")

    #     if len(curr_node.children) == 0:
    #         curr_node.is_word_end = False
    #         can_node_be_deleted = True

    #     # if len(curr_node.children) == 0:
    #     #     if curr_node.children.is_word_end is True:
    #     #         curr_node.children.is_word_end = False
    #     #     can_node_be_deleted = True

    #     if len(curr_node.children) >= 1:
    #         if can_node_be_deleted is True:
    #             curr_node.children.pop(char)
    #         if curr_node.is_word_end is False:      
    #             can_node_be_deleted = True        

    #     return can_node_be_deleted

    # def delete_word(self, root, key_word, depth = 0):

        
    #     print(root.children.get(key_word[depth]))
    #     if not root:
    #         return None

    #     if depth == len(key_word):

    #         if root.is_word_end == True:
    #             root.is_word_end = False

    #         if self.is_empty(root):
    #             del root
    #             root = None
    #         return root

    #     root.children[key_word[depth]] = self.delete_word(self, root.children[key_word[depth+1]], key_word, depth + 1)

    #     if self.is_empty(root) and root.is_word_end is False:
    #         root = None

    #     return root                 
        



        



if __name__ == '__main__':

    trie_obj = Trie()
    for word in ['API','ANT']:
        trie_obj.add_word(word)
        #print(f"lenght of dict after adding {word} ----> {len(trie_obj.root.children)}")    
        
# pprint(MyJsonEncoder().encode(trie_obj))
# json_data = json.dumps(trie_obj, default = lambda obj: obj.__dict__, indent = 2)
# print(json_data)

# for word in ['API']:
#     print(trie_obj.search_word(word))
    
# print("-------------------------------------")

trie_obj.delete_word(trie_obj.root, 'API')

for word in ['API']:
    print(trie_obj.search_word(word))
    print("-------------------------------->")

# json_data = json.dumps(trie_obj, default = lambda obj: obj.__dict__, indent = 2)
# print(json_data)








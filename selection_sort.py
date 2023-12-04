#Complexity - O(n^2) 

class SelectionSort:
    
    def __init__(self, size):
        self.size = size
        
    def selection_sort(self, custom_list):
        
        for i in range(self.size):
            min_index = i
            
            for j in range(i+1, self.size):
                if custom_list[j] < custom_list[min_index]:
                    min_index = j
            
            custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
        return custom_list    
            
if __name__ == '__main__':
    
    custom_list = [7,8,1,5,3,6]
    selection = SelectionSort(len(custom_list))
    
    print(selection.selection_sort(custom_list))
    
                    
        
#This is modified Bubble_Sort
import time

class BubbleSortModified:
    
    def __init__(self, size):
        self.size = size
        
    def ascending_bubble_sort(self, custom_list):
        
        begin = time.time()
        
        count = 0
        for i in range(self.size - 1):
            swaps = 0
            for j in range(self.size - i - 1):
                
                if custom_list[j] > custom_list[j+1]:
                    custom_list[j] , custom_list[j+1] = custom_list[j+1] , custom_list[j]
                    swaps += 1
            count += 1
            # if swaps < 1:
            #     break        
        
        print(f'Execution steps : {count}')        
        time.sleep(1)            
        end = time.time()
        print(f'time taken for execution : {end - begin:.5f}')
        return custom_list            
    
    def descending_bubble_sort(self, custom_list):
        
        begin = time.time()
        
        count = 0
        for i in range(self.size - 1):
            swaps = 0
            for j in range(self.size - i - 1):
                
                if custom_list[j] < custom_list[j+1]:
                    custom_list[j] , custom_list[j+1] = custom_list[j+1] , custom_list[j]
                    swaps += 1
                
            count += 1        
            if swaps < 1:
                break
        
        print(f'ececution steps: {count}')    
        time.sleep(1)
        end = time.time()
        res = end - begin
        print(f'time taken for execution : {res:.5f}')            
        return custom_list
                    
if __name__ == '__main__':
    
    custom_list = [1,2,3,4,5,6]
    
    bubble = BubbleSortModified(len(custom_list))
    
    print(bubble.ascending_bubble_sort(custom_list))
    print(bubble.descending_bubble_sort(custom_list))
    
                           
    
            
    
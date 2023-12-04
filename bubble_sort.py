#Bubble sort : O(N^2)
import time

class BubbleSort:
    
    def __init__(self, size):
        self.size = size
        
    def ascending_bubble_sort(self, custom_list):
        
        begin = time.time()
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                
                if custom_list[j] > custom_list[j+1]:
                    custom_list[j] , custom_list[j+1] = custom_list[j+1] , custom_list[j]
        time.sleep(1)            
        end = time.time()
        print(f'time taken for execution : {end - begin:.5f}')
        return custom_list            
    
    def descending_bubble_sort(self, custom_list):
        
        begin = time.time()
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                
                if custom_list[j] < custom_list[j+1]:
                    custom_list[j] , custom_list[j+1] = custom_list[j+1] , custom_list[j]
        
        time.sleep(1)
        end = time.time()
        res = end - begin
        print(f'time taken for execution : {res:.5f}')            
        return custom_list
                    
if __name__ == '__main__':
    
    custom_list = [2,6,9,1,3,7]
    bubble = BubbleSort(len(custom_list))
    
    
    
    print(bubble.ascending_bubble_sort(custom_list))
    print(bubble.descending_bubble_sort(custom_list))
    
                           
    
            
    
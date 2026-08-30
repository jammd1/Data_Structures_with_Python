from linear_data_structures.linked_list import Node

def main():
    data1 = 'head_data'
    data2 = 'head.next_data'
    data3 = 'head.next.next_data'
    
    head = Node(data=data1)
    head.next = Node(data=data2)
    head.next.next = Node(data=data3)
    
    
    
    

if __name__ == '__main__':
    main()
    
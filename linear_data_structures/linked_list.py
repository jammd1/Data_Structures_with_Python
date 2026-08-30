
# 기본 노드 정의
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def appendleft(self, data):
        """ 
        Linked List의 맨 처음(왼쪽)에 data를 가진 새 노드를 추가
        
        data (any): Node가 가지는 데이터
        """
        
        if self.head is None: 
            # 만약 Linked List의 head가 None일 시 = Linked List에 아무것도 없을 때
            # head에 맨 새로운 Node를 지정
            self.head = Node(data)
            
        else :
            # 만약 Linked List에 하나 이상의 Node가 있을 시
            # 새로운 노드 생성 후 새로운 노드의 next를 이전의 head로 지정
            # 새 head를 새로운 노드로 지정
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1 # 길이 + 1
    
    def append(self, data):
        """
        Linked List의 맨 마지막(오른쪽)에 data를 가진 새 노드를 추가
        data (any): Node가 가지는 데이터
        """
        if self.head is None:
            self.head = Node(data)
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = Node(data)
        self.length += 1
    
    def popleft(self):
        """
        Linked List의 맨 첫번째(왼쪽)에 있는 Node를 제거한 후 data를 반환한다.
        
        """
        if self.head is None:
            return None
        
        target_node = self.head
        data = target_node.data
        self.head = self.head.next
        self.length -= 1
        
        return data

    def pop(self):
        """
        Linked List의 맨 마지막(오른쪽)에 있는 Node를 제거 후에 data를 반환한다.
        """
        if self.head is None:
            return None
        
        target_node = None
        head = self.head
        while head.next is None:
            head = head.next
        target_node = head
        
        
        
    
    def __str__(self):
        result = ""
        head = self.head
        while head:
            result += str(head.data) + "->"
            head = head.next
        return result

if __name__ == "__main__":
    linked_list = LinkedList()
    
    for i in range(3):
        linked_list.append(i)
    
    linked_list.popleft()
    
    print(linked_list)


        

    
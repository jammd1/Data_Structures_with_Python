
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

    def __contains__(self, item):
        if self.head is None:
            return False
        node = self.head
        
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False
    
    def __str__(self):
        
        if self.head is None:
            return "Linked List is Empty State"
        
        result = "HEAD ->"
        head = self.head
        while head:
            result += str(head.data) + " -> "
            head = head.next
        return result
    
    def insert(self, index: int, data):
        if index <= 0:
            self.appendleft(data)
            
        elif index >= self.length:
            self.append(data)
        
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1
    
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
        
        sudo 
        find last node
        find pre-last node
        disconnect referrence from pre-last one to last one
        """
        if self.head is None:
            return None
        
        node = self.head
        
        while node.next:
            prev = node # prev를 기억
            node = node.next
            
        if node == self.head: # 만약 원소 하나짜리 였으면
            self.head = None
        else:
            prev.next = None # 만약 두개 이상의 원소가 있었으면
            
        self.length -= 1
        return node.data
    
    def remove(self, target):
        """
        target 검색
            ↓
        못 찾음? ── Yes → False
            ↓ No
        첫 번째 노드인가?
            ↓
        Yes → head를 다음 노드로 이동
        No  → 이전 노드와 다음 노드를 직접 연결
            ↓
        length - 1
            ↓
            True    
        """
        node = self.head
        while node and node.data != target: # 노드 검색
            prev = node
            node = node.next
        if node is None: # 검색했는데 아무것도 없을 경우
            return False
        if node == self.head: # 삭제하려는 노드가 head일 경우
            self.head = self.head.next
        else: # 삭제하려는 노드가 첫번째 노드가 아닌 경우
            prev.next = node.next
        self.length -= 1
        return True

        
    
        
      
    

if __name__ == "__main__":
    linked_list = LinkedList()
    
    print(linked_list)
    print(4 in linked_list)
    
    for i in range(10):
        linked_list.append(i)
    
    
    print(linked_list)

    print(9 in linked_list)
    
    for i in range(3): 
        linked_list.pop()
        
    print(linked_list)


        

    
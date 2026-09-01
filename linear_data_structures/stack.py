from node import Node

class Stack:
    
    def __init__(self):
        self.top = None
    
    def push(self, data):
        """
        Stack의 맨 위에 data를 가진 새 노드를 추가
        data (any): Node가 가지는 데이터
        """
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
    
    def pop(self):
        """
        Stack의 맨 위에 있는 노드를 제거하고 그 데이터를 반환
        """
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data
    
    def peek(self):
        """
        Stack의 맨 위에 있는 노드의 데이터를 반환
        """
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        """
        Stack이 비어있는지 확인"""
        
        return self.top is None

    def __str__(self):
        if self.top is None:
            return "Stack is empty"
        result = ""
        node = self.top
        while node:
            result += str(node.data) + " -> "
            node = node.next
        return result[:-4]
        

def reverse_word(word: str):
    """
    문자열 word를 뒤집은 문자열을 반환한다.
    """
    reversed = ""
    stack = Stack()
    for ch in word:
        stack.push(ch)
    while not stack.is_empty():
        reversed += stack.pop()
    return reversed

def check_brackets(word: str):
    """
    문자열 word의 괄호가 올바르게 열고 닫혔는지 확인한다.
    """
    stack = Stack()
    for ch in word:
        if ch == "(":
            stack.push(ch)
        elif ch == ")":
            if not stack.pop():
                return False
    return stack.is_empty()
            
            
if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
   
    print(check_brackets("((a * (b + c)) - d) / e"))
    print(check_brackets("(((a * (b + c)) - d) / e"))
    
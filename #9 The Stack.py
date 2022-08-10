#The Stack

#LIFO Malumot to'plami
#LIFO(Last In First Out)-Oxirgi kirgan birinchi chiqadi
#Malumotlar to'plam ustiga qo'shiladi va to'plam ustidan olinadi.


#The Stack Ustida amallar bajarish

#Push-Stack ustiga element qo'wiw
#Pop-Stack ni ustidan element sug'urib olish
#isEmpty-To'plamni ichi bo'sh ekanligini tekshirish
#isFull-To'plamni ichi to'la ekanligini tekshirish
#Peek-eng yuqoridagi element qiymatini ko'rish
#Peek da elementlarni sug'urib olib bo'lmaydi faqat stack ni ichidagi malumotlarni ko'rishimiz mumkin


class Stack:
    """Stack obyekti"""
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        """Bo'sh ekanligini tekshirish"""
        return len(self.stack)==0
    
    def push(self,data):
        """Element qo'shish"""
        self.stack.append(data)
        return True
    
    def pop(self):
        """Element sug'urib olish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]

if __name__=='__main__':
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print("Top element: ", stack.peek())
    print(stack.peek())
    print(stack.peek())
    print(stack.peek())
    print(stack.peek())


#Stack va Rekursiya

#Rekursiv funksiyalar ham stack asosida ishlaydi
#Dasturlashda bu call stack yoki program stack deb ataladi

#Call Stack
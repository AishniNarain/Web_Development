public class Array_imp {
    int top;
    int size;
    int [] stack;

    Array_imp(){
        top = -1;
        size = 10;
        stack = new int[size];
    }

    boolean isEmpty(){
        if(top == -1){
            System.out.println("Stack is Empty");
        }
        return false;
    }

    boolean isFull(){
        if(top == size-1){
            System.out.println("Stack is Full");
        }
        return false;
    }

    int peek(){
        return stack[top];
    }

    void push(int data){
        if(isFull()){
            System.out.println("Stack Overflow");
        }
        top++;
        stack[top] = data;
    }

    int pop(){
        if(isEmpty()){
            System.out.println("Stack Underflow");
        }
        top--;
        return stack[top];
    }

    void display(){
        for(int i=top;i>=0;i--){
            System.out.println(stack[i]);
        }
    }
    
    public static void main(String args[]){
        Array_imp st = new Array_imp();
        st.push(1);
        st.push(2);
        st.push(3);
        st.push(4);
        st.push(5);
        System.out.println(st.isEmpty());
        System.out.println(st.isFull());
        System.out.println(st.peek());
        System.out.println(st.pop());
        System.out.println(st.pop());
        System.out.println(st.pop());
        System.out.println(st.pop());
        System.out.println(st.isEmpty());
        System.out.println(st.isFull());
    }
}


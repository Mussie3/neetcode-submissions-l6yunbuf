class MinStack {
    // 1. Declare stacks at the CLASS level so all methods can see them
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        // 2. Initialize them in the constructor
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        // If minStack is empty or val is smaller than current min, push to minStack
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        // If we pop the value that was the minimum, pop it from minStack too
        if (stack.peek().equals(minStack.peek())) {
            minStack.pop();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek(); // Must return the value
    }
    
    public int getMin() {
        return minStack.peek(); // The top of minStack is always the current minimum
    }
}
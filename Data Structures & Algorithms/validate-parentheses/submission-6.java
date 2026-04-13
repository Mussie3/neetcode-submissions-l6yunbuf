class Solution {
    public boolean isValid(String s) {
        char[] c = s.toCharArray();
        Stack<Character> stack =  new Stack<>();
        Map<Character, Character> dict = new HashMap<>();
        dict.put(')', '(');
        dict.put(']', '[');
        dict.put('}', '{');
        for(int i = 0; i < c.length; i++){
            if(!stack.isEmpty() && stack.peek() == dict.get(c[i]) ){
                stack.pop();
            } else {
                stack.push(c[i]);
            }
        }

        if(stack.size() == 0) {
            return true;
        } else {
            return false;
        }
    }
}

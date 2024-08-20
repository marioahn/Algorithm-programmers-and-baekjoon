class Solution {
    public boolean solution(int x) {
        int sum = 0;
        
        String[] num = Integer.toString(x).split("");
        for (int i=0; i<num.length; i++) {
            sum += Integer.parseInt(num[i]);
        }
        
        if (x%sum != 0) {
            return false;
        } else return true;
        
    }
}
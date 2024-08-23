class Solution {
    public int solution(int left, int right) {
        int result = 0;
        
        for (int i=left; i<=right; i++) {
            if (i % Math.sqrt(i) == 0) {
                result -= i;
            } else result += i;
        }
        
        
        return result;
    }
}
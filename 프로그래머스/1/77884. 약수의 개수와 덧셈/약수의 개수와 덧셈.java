class Solution {
    public int solution(int left, int right) {
        int result = 0;
        
        for (int i=left; i<right+1; i++) {
            int cnt = 1;
            for (int j=2; j<i+1; j++) {
                if (i%j==0) cnt += 1;
            }
            
            if (cnt%2 == 0) result += i;
            else result -= i;
        }
        
        return result;
    }
}
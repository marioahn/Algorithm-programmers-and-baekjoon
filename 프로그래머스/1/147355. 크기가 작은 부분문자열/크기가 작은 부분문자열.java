class Solution {
    public int solution(String t, String p) {
        int len = p.length();
        long num = Long.parseLong(p); // int아니고, long! - p길이는 최대 10,000니까
        int result = 0;
        
        for (int i=0; i<t.length()-len+1; i++) {
            long diff = Long.parseLong(t.substring(i, i+len));
            if (diff <= num) result ++;
        }
        return result;
    }
}
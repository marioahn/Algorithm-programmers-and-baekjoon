// class Solution {
//     public int solution(String s) {
//         String[] arr = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
//         for (int i=0; i<arr.length; i++) {
//             if (s.contains(arr[i])) {
//                 s = s.replace(arr[i], Integer.toString(i));
//             }
//         }
        
//         return Integer.parseInt(s);
//     }
// }

import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int len = s.length();
        StringBuilder sb = new StringBuilder("");
        String[] digits = {"0","1","2","3","4","5","6","7","8","9"};
        String[] alphabets = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
        for (int i=0; i<10; i++) {
            s = s.replaceAll(alphabets[i], digits[i]);
        }
        
        return Integer.parseInt(s);
    }
}
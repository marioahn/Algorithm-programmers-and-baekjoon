// // way1
// class Solution {
//     public int[] solution(String s) {
//         int[] answer = new int[s.length()];
        
//         for (int i=0; i<s.length(); i++) {
//             if (i != 0) {
//                 // "apple".charAt(4) = 'e';
//                 int idx = s.substring(0,i).lastIndexOf(s.charAt(i));
//                 if (idx != -1) {
//                     answer[i] = i-idx;
//                 } else {
//                     answer[i] = idx;
//                 }
//             } else {
//                 answer[0] = -1;
//             }
//         }
        
//         return answer;
//     }
// }

// way2 - dict사용
import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i); // = s[i] at python
            answer[i] = i-map.getOrDefault(ch,i+1);
            map.put(ch,i);
        }
        
        return answer;
    }
}
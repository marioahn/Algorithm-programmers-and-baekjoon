import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int i=0; i<numbers.length; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                int tmpSum = numbers[i]+numbers[j];
                if (list.indexOf(tmpSum) < 0) {
                    list.add(tmpSum);
                }
            }
        }
        Collections.sort(list);
        
        // 정렬된 list를 배열로 변환
        int[] result = new int[list.size()];
        for (int i=0; i<list.size(); i++) {
            result[i] = list.get(i);
        }
        
        return result;
    }
}
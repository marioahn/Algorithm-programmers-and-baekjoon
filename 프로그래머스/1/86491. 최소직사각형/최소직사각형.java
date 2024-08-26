// class Solution {
//     public int solution(int[][] sizes) {
//         int max_row = 0; // 가로의 최대 길이
//         int max_col = 0; // 세로
        
//         for (int i=0; i<sizes.length; i++) {
//             if (sizes[i][0] < sizes[i][1]) {
//                 int tmp = sizes[i][0];
//                 sizes[i][0] = sizes[i][1];
//                 sizes[i][1] = tmp;
//             }
//             if (max_row<sizes[i][0]) max_row = sizes[i][0];
//             if (max_col<sizes[i][1]) max_col = sizes[i][1];
//         }
        
//         return max_row*max_col;
//     }
// }

class Solution {
    public int solution(int[][] sizes) {
        int length = 0, height = 0; // 아 이렇게 2개 나란히 쓸 수 있구나;
        
        for (int[] card: sizes) {
            length = Math.max(length, Math.max(card[0], card[1]));
            height = Math.max(height, Math.min(card[0], card[1]));
        }

        return length * height;
    }
}
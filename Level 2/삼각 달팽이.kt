class Solution {
    fun solution(n: Int): IntArray {
        var array1 = Array(n, {IntArray(n, {0})})

        var cnt = n
        var num = 0
        var x = 0
        var y = -1
        while (cnt > 0) {
            // 위에서 아래로 채우기
            for (i in 1..cnt) {
                y += 1
                num += 1
                array1[y][x] = num
            }
            cnt -= 1
            // 왼쪽에서 오른쪽으로 채우기
            for (i in 1..cnt) {
                x += 1
                num += 1
                array1[y][x] = num
            }
            cnt -= 1
            // 왼쪽 대각선 방향으로 채우기
            for (i in 1..cnt) {
                x -= 1
                y -= 1
                num += 1
                array1[y][x] = num
            }
            cnt -= 1
        }

        // 정답 배열을 만들어서 반환
        var size: Int = 0
        for (i in 1..n) size += i 
        var answer: IntArray = IntArray(size, {0})

        var idx = 0
        for (y in 0..n - 1) {
            for (x in 0..n - 1) {
                if (array1[y][x] != 0) {
                    answer[idx] = array1[y][x]
                    idx += 1
                }
            }
        }
        return answer
    }
}

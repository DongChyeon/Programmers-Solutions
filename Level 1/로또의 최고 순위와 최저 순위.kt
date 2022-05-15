class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        val unknown_nums = lottos.count{it == 0}
        
        val a = lottos.toSet()
        val b = win_nums.toSet()
        
        // 교집합 연산을 통해 당첨된 번호의 갯수를 구함
        val res = a.intersect(b)
        // 0이 전부 당첨 번호일 경우
        val max = if (res.size + unknown_nums == 0) 1 else res.size + unknown_nums
        // 0이 전부 당첨 번호가 아닐 경우
        val min = if (res.size == 0) 1 else res.size
        
        var answer: IntArray = intArrayOf(7 - max, 7 - min)
        return answer
    }
}

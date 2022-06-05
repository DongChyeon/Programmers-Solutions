class Solution {
    fun solution(s: String): IntArray {
        var (count, del_count) = arrayOf(0, 0)
        var prev: String = s
        var next: String = ""
        
        do {
            // 1. x의 모든 0을 제거합니다.
            next = prev.replace("0", "")
            count += 1
            del_count += prev.length - next.length

            // 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
            prev = next
            next = Integer.toBinaryString(prev.length)
            prev = next
        } while (!next.equals("1")) // 1이 될 때까지 반복
        
        return intArrayOf(count, del_count)
    }
}

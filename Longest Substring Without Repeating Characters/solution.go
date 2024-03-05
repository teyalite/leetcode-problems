func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func lengthOfLongestSubstring(s string) int {
	longest := 0
	current := 0
	i := 0

	occurences := make(map[byte]int)

	for i < len(s) {
		_, ok := occurences[s[i]]

		if ok {
			i = occurences[s[i]] + 1
			occurences = make(map[byte]int)
			longest = max(longest, current)
			current = 0
		} else {
			occurences[s[i]] = i
			current++
			i++
		}
	}

	return max(longest, current)
}
package words

import "strings"

// 统计单词个数
func CountWords(text string) (count int) {
	count = len(strings.Fields(text))
	return count
}

// Package word provides utilities for word games
package word

// 判断一个字符串是否是回文字符串
func IsPalindrome(s string) bool {
	for i := range s {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}



package search

import "log"

// 定义搜索的返回结果
type Result struct {
	Field   string
	Content string
}

// 接口：定义要实现的搜索类型的行为
type Matcher interface {
	Search(feed *Feed, searchTerm string) ([]*Result, error)
}

// matcher为接口类型，实现了该接口中定义的所有的方法的类型即可作为参数传入
// 每种实现了接口的类型，可以定义自己独特的实现方式，从而实现多态
func Match(matcher Matcher, feed *Feed, searchTerm string, results chan<- *Result) {
	searchResults, err := matcher.Search(feed, searchTerm)
	if err != nil {
		log.Println(err)
		return
	}
	for _, result := range searchResults {
		results <- result
	}
}

func Display(results chan *Result) {
	for result := range results {
		log.Printf("%s:\n%s\n\n", result.Field, result.Content)
	}
}

package search

import (
	"log"
	"sync"
)

// 用于搜索的Matcher的映射
var matchers = make(map[string]Matcher)

func Run(searchTerm string) {
	// 获取搜索的数据源列表
	feeds, err := RetrieveFeeds()

	if err != nil {
		log.Fatal(err)
	}
	// 创建一个无缓冲的通道，接收匹配后的结果
	results := make(chan *Result)

	var waitGroup sync.WaitGroup

	// 设置需要等待处理
	// 每个数据源的 goroutine的数量
	waitGroup.Add(len(feeds))

	// 为每个数据源启动一个goroutine来查找结果
	for _, feed := range feeds {
		matcher, exists := matchers[feed.Type]
		if !exists {
			matcher = matchers["default"]
		}

		// 启动一个goroutine来执行搜索
		// matcher为接口类型，故实现了该接口方法的类型都可以作为参数传入
		go func(matcher Matcher, feed *Feed) {
			Match(matcher, feed, searchTerm, results)
			waitGroup.Done()
		}(matcher, feed)
	}

	// 启动一个goroutine来监控是否所有的工作都做完了
	go func() {
		// 等候所有任务完成
		waitGroup.Wait()

		// 用关闭通道的方式，通知Display函数
		close(results)
	}()

	//  启动函数，显示返回的结构，并且在最后一个结果显示完后返回
	Display(results)

}

func Register(feedType string, matcher Matcher) {
	if _, exists := matchers[feedType]; exists {
		log.Fatal(feedType, "Matcher already registered")
	}

	log.Println("Register", feedType, "matcher")

	// 注册一种类型的matcher到matchers映射
	matchers[feedType] = matcher
}

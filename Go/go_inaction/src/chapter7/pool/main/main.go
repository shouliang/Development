// 演示如何使用pool包来共享一组模拟的数据库连接
package main

import (
	"chapter7/pool"
	"io"
	"log"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

const (
	// 要使用的goroutine的数量
	maxGoroutines = 5

	// 池中资源的数量
	pooledResources = 2
)

// dbConncetion 模拟要共享的资源
type dbConncetion struct {
	ID int32
}

// dbConnection实现了io.Closer的接口
// 以便dbConnection可以被池管理
// Close用来完成任意资源的释放管理
func (dbConn *dbConncetion) Close() error {
	log.Println("Closed: Connection", dbConn.ID)
	return nil
}

// 用来给每个连接分配一个独一无二的id
var idCounter int32

// 工厂函数，当需要一个新连接时，资源池会调用这个函数
func createConnection() (io.Closer, error) {
	id := atomic.AddInt32(&idCounter, 1)
	log.Println("Create: New Connection", id)

	return &dbConncetion{id}, nil
}

func main() {
	var wg sync.WaitGroup
	wg.Add(maxGoroutines)

	// 创建用来管理的连接池
	p, err := pool.New(createConnection, pooledResources)
	if err != nil {
		log.Println(err)
	}

	// 使用池里的连接来完成查询
	for query := 0; query < maxGoroutines; query++ {
		// 每个goroutine需要自己复制一份要查询值的副本
		// 不然所有的查询会共享同一个查询变量
		go func(q int) {
			performQueries(q, p)
			wg.Done()
		}(query)
	}

	// 等待所有的goroutine结束
	wg.Wait()

	// 关闭池
	log.Println("Shutdown Program")
	p.Close()
}

// 用来测试连接的资源池
func performQueries(query int, p *pool.Pool) {
	// 从池中获取一个连接
	conn, err := p.Acquire()
	if err != nil {
		log.Println(err)
		return
	}

	// 将该连接释放会池里
	defer p.Release(conn)

	// 用等待来模拟查询响应
	time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	log.Printf("Query: QID[%d] CID[%d]\n", query, conn.(*dbConncetion).ID)
}

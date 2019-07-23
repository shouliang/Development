// 一个简单缓存的设计： 用RWMutex替换Mutex
package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"
)

type Cache struct {
	rw   sync.RWMutex // 新增一个读写锁: 读读不互斥，读写互斥
	data map[interface{}]interface{}
}

func NewCache() *Cache {
	return &Cache{
		data: make(map[interface{}]interface{}),
	}
}

// Get使用读锁
func (c *Cache) Get(key interface{}) (value interface{}, ok bool) {
	c.rw.RLock()
	defer c.rw.RUnlock()
	if c.data != nil {
		v, ok := c.data[key]
		return v, ok
	}
	return nil, false
}

// Set使用写锁
func (c *Cache) Set(key, value interface{}) bool {
	c.rw.Lock()
	defer c.rw.Unlock()
	if c.data != nil {
		c.data[key] = value
		return true
	}
	return false
}

func (c *Cache) Dump() {
	if c.data != nil {
		for k, v := range c.data {
			fmt.Printf("%v %v\n", k, v)
		}
	}
}

func worker(c *Cache, k, v interface{}) {
	c.Set(k, v)
	storedValue, ok := c.Get(k)
	if !ok {
		fmt.Printf("store %v:%v error\n", k, v)
	}
	if storedValue != v {
		fmt.Printf("store %v:%v error, want: %v,got: %v\n", k, v, v, storedValue)
	}
}

func main() {
	cache := NewCache()
	for i := 0; i < 10; i++ {
		k := "key-" + strconv.Itoa(i)
		v := i
		go worker(cache, k, v)
	}
	time.Sleep(1 * time.Second)
	cache.Dump()
}

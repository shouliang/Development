// 一个简单缓存的设计： 基于map的非安全缓存,Go原生的map类型是非线程安全的
package main

import (
	"fmt"
	"strconv"
	"time"
)

type Cache struct {
	data map[interface{}]interface{}
}

func NewCache() *Cache {
	return &Cache{
		data: make(map[interface{}]interface{}),
	}
}

func (c *Cache) Get(key interface{}) (value interface{}, ok bool) {
	if c.data != nil {
		v, ok := c.data[key]
		return v, ok
	}
	return nil, false
}

func (c *Cache) Set(key, value interface{}) bool {
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

/*
func main() {
	cache := NewCache()
	cache.Set("Hello", "World")
	cache.Set(1, 2)
	cache.Set(true, false)
	cache.Dump()
}
*/

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

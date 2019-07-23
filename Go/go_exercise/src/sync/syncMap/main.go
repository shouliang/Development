// Sync.Map 是并发安全的， 有Load、LoadOrStore、Delete、Store、Range等方法
package main

import (
	"fmt"
	"strconv"
	"sync"
)

var wg sync.WaitGroup

func main() {
	var m = sync.Map{}

	// 测试并发读写是否正常
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			key := "key-" + strconv.Itoa(i)
			value := "value-" + strconv.Itoa(i)
			m.Store(key, value)
			v, ok := m.Load(key)
			if !ok {
				fmt.Printf("get %v failed\n", key)
			}
			if v != value {
				fmt.Printf("want: %v, got %v", value, v)
			}
		}(i)
	}

	wg.Wait()

	m.Range(doSomething)

	m.Delete("key-7")

	_, ok := m.Load("key-7")
	if ok != false {
		fmt.Println("deleted failed")
	} else {
		fmt.Println("delete success")
	}

}

func doSomething(k, v interface{}) bool {
	if k != "key-7" {
		fmt.Printf("key: %v, value: %v\n", k, v)
		return true
	}
	return false
}

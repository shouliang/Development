package once_test

import (
	"fmt"
	"sync"
	"testing"
	"unsafe"
)

type Singleton struct {
}

var singleInstance *Singleton
var once sync.Once

func GetSingletonObj() *Singleton {
	once.Do(func() {
		fmt.Println("Create Obj") // 只运行一次
		singleInstance = new(Singleton)
	})

	return singleInstance
}

func TestGetSingletonObj(t *testing.T) {
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func() {
			obj := GetSingletonObj()
			fmt.Printf("%d\n", unsafe.Pointer(obj)) // 会输出同一个地址
			wg.Done()
		}()
	}

	wg.Wait()
}

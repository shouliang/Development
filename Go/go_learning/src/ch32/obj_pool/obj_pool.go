package pool

import (
	"errors"
	"time"
)

// 资源对象
type ReusableObj struct {
}

type ObjPool struct {
	bufChan chan *ReusableObj // 通道：用于缓冲可重用的对象
}

// 生成一个池
func NewObjPool(numOfObj int) *ObjPool {
	objPool := ObjPool{}
	objPool.bufChan = make(chan *ReusableObj, numOfObj)
	for i := 0; i < numOfObj; i++ {
		objPool.bufChan <- &ReusableObj{} // 初始化一定数量的资源
	}

	return &objPool
}

// 从池中获取对象，带有超时控制
func (p *ObjPool) GetObj(timeout time.Duration) (*ReusableObj, error) {
	select {
	case ret := <-p.bufChan:
		return ret, nil
	case <-time.After(timeout): // 超时控制
		return nil, errors.New("Get obj time out")
	}
}

// 将对象放回池中，带有溢出提示
func (p *ObjPool) ReleaseObj(obj *ReusableObj) error {
	select {
	case p.bufChan <- obj:
		return nil
	default:
		return errors.New("overflow")
	}
}

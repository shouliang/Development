package client

import (
	"ch15/service" // 相对于src当前工作区的路径，当前工作区需要设置为GOPATH目录
	"testing"
)

func TestPackage(t *testing.T) {
	t.Log(service.GetFibnacciService(5))
	t.Log(service.Square(4))
}

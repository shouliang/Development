package interface_test

import "testing"

type Programmer interface {
	WriteHelloWorld() string
}

type GoProgrammer struct {
}

// 方法签名和接口中定义的完全一致 duck-type
func (g *GoProgrammer) WriteHelloWorld() string {
	return "fmt.Pritln(\"Hello World\")"
}

func TestClient(t *testing.T) {
	var p Programmer
	p = new(GoProgrammer)
	t.Log(p.WriteHelloWorld())
}

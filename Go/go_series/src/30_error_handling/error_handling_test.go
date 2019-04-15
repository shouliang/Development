/*
在 Go 中，错误一直是很常见的。错误用内建的 error 类型来表示。
就像其他的内建类型（如 int、float64 等），错误值可以存储在变量里、作为函数的返回值等等
*/
package errorhandling

import (
	"net"
	"os"
	"path/filepath"
	"testing"
)

// 简单示例
func TestErrorSimple(t *testing.T) {
	f, err := os.Open("/test.txt")
	if err != nil {
		t.Log(err)
		return
	}
	t.Log(f.Name(), "opened successfully")
}

/* 错误类型的表示
error 是一个接口类型，定义如下：
type error interface {
    Error() string
}
error 有了一个签名为 Error() string 的方法。
所有实现该接口的类型都可以当作一个错误类型。Error() 方法给出了错误的描述。
*/

/* 从错误获取更多信息的不同方法
1. 断言底层结构体类型，使用结构体字段获取更多信息
如果你仔细阅读了 Open 函数的文档，你可以看见它返回的错误类型是 *PathError。
PathError 是结构体类型，它在标准库中的实现如下：
type PathError struct {
    Op   string
    Path string
    Err  error
}
func (e *PathError) Error() string { return e.Op + " " + e.Path + ": " + e.Err.Error() }
*/

// 类型断言（Type Assertion）来获取 error 接口的底层值（Underlying Value）。
// 我们使用 err.Path 来打印该路径
func TestErrorAsserting(t *testing.T) {
	f, err := os.Open("/test.txt")
	if err, ok := err.(*os.PathError); ok {

		t.Log("File at path", err.Path, "failed to open")
		return
	}
	t.Log(f.Name(), "opened successfully")
}

/* 从错误获取更多信息的不同方法
2. 断言底层结构体类型，调用方法获取更多信息
*/
func TestDNSError(t *testing.T) {
	addr, err := net.LookupHost("golangbot123.com")
	if err, ok := err.(*net.DNSError); ok {
		if err.Timeout() {
			t.Log("operation timed out")
		} else if err.Temporary() {
			t.Log("temporary error")
		} else {
			t.Log("generic error:", err)
		}
		return
	}
	t.Log(addr)
}

/* 3. 直接比较
第三种获取错误的更多信息的方式，是与 error 类型的变量直接比较
filepath 包中的 Glob 用于返回满足 glob 模式的所有文件名。如果模式写的不对，该函数会返回一个错误 ErrBadPattern。
filepath 包中的 ErrBadPattern 定义如下：

var ErrBadPattern = errors.New("syntax error in pattern")
errors.New() 用于创建一个新的错误

当模式不正确时，Glob 函数会返回 ErrBadPattern。
*/
func TestErrBadPattern(t *testing.T) {
	files, err := filepath.Glob("[")
	if err != nil && err == filepath.ErrBadPattern {
		t.Log(err)
		return
	}
	t.Log("matched files", files)
}

// 不可忽略错误
// 使用 _ 空白标识符，忽略了 Glob 函数返回的错误。然后简单打印了所有匹配的文件
// 实际上这是因为模式的写法不对。所以绝不要忽略错误。
func TestNotIgnoreError(t *testing.T) {
	files, _ := filepath.Glob("[")
	t.Log("matched files", files)
}

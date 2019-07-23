// Pool 使用：Pool是一个临时对象的集合，可安全地并发访问( Put()、Get())
package main

import (
	"bytes"
	"io"
	"os"
	"sync"
	"time"
)

var bufPool = sync.Pool{
	New: func() interface{} {
		return new(bytes.Buffer)
	},
}

func timeNow() time.Time {
	return time.Unix(1136214245, 0)
}

func log(w io.Writer, key, val string) {
	// 从对象池中获取buffer
	b := bufPool.Get().(*bytes.Buffer)
	b.Reset()

	b.WriteString(timeNow().UTC().Format(time.RFC3339))
	b.WriteByte(' ')
	b.WriteString(key)
	b.WriteByte('=')
	b.WriteString(val)

	w.Write(b.Bytes())

	// 使用完毕，归还buffer
	bufPool.Put(b)
}

func main() {
	log(os.Stdout, "path", "/search?q=flowers")
}

// Clock1 is a TCP servver that periodically writes the time
package main

import (
	"io"
	"log"
	"net"
	"time"
)

func main() {
	listener, err := net.Listen("tcp", "localhost:8000") // 监听本机的tcp 8000端口号
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := listener.Accept() // 一直阻塞直到客户端有请求过来
		if err != nil {
			log.Print(err)
			continue
		}
		handleConn(conn) // 一次处理一个连接
	}
}

func handleConn(c net.Conn) {
	defer c.Close()
	for {
		// 每个1秒向客户端写入当前时间
		_, err := io.WriteString(c, time.Now().Format("15:04:05\n"))
		if err != nil {
			return
		}
		time.Sleep(1 * time.Second)
	}
}
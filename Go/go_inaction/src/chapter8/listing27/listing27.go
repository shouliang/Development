// 展示如何解码JSON字符串
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

// Contact结构体
type Contact struct {
	Name    string `json:"name"`
	Title   string `json:"title"`
	Contact struct {
		Home string `json:"home"`
		Cell string `json:"Cell"`
	} `json:"contact"`
}

// 用于反序列化的演示字符串
var JSON = `{
  "name": "Gopher",
  "title":"programmer",
  "contact": {
    "home": "415.333.3333",
    "cell": "415.555.5555"
  }
}`

func main() {
	var c Contact

	// 使用Unmarshal函数将JSON字符串解析到一个结构体中
	err := json.Unmarshal([]byte(JSON), &c)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}

	fmt.Println(c)
}

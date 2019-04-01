// 演示如何解码JSON字符串到map变量中
// 因为有时候无法为JSON的格式声明一个结构类型
// 故需要使用更加灵活的方式来处理JSON文档
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

// JSON字符串
var JSON = `{
  "name": "Gopher",
  "title":"programmer",
  "contact": {
    "home": "415.333.3333",
    "cell": "415.555.5555"
  }
}`

func main() {
	// 将JSON字符串反序列化到map变量
	// key为string类型，value为interface{}类型
	// 故值可以为任意类型的值
	var c map[string]interface{}
	err := json.Unmarshal([]byte(JSON), &c)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}

	fmt.Println("Name:", c["name"])
	fmt.Println("Title:", c["title"])
	fmt.Println("Contact")
	fmt.Println("H:", c["contact"].(map[string]interface{})["home"])
	fmt.Println("C:", c["contact"].(map[string]interface{})["cell"])
}

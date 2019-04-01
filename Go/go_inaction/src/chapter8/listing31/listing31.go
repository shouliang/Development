// 展示如何序列化JSON字符串
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	c := make(map[string]interface{})
	c["name"] = "Gopher"
	c["title"] = "programmer"
	c["contact"] = map[string]interface{}{
		"home": "415.333.3333",
		"cell": "415.555.5555",
	}

	// 将一个map值转换成JSON字符串，MarshalIndent带缩进
	data, err := json.MarshalIndent(c, "", "    ")

	// Marshal不带缩进
	//data, err := json.Marshal(c)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}

	fmt.Println(string(data))
}

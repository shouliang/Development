// 展示了公开的结构体类型中未公开的字段无法直接访问
package main

import (
	"chapter5/listing71/entities"
	"fmt"
)

func main() {
	u := entities.User{
		Name:  "Bill",
		email: "bill@gmail.com", //unknown field 'email' in struct literal of type entities.User
	}

	fmt.Printf("User: %v\n", u)

}

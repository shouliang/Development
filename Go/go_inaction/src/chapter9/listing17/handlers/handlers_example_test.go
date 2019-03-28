// 展示如何编写合适的文档
// godoc -http=":3000" 然后在浏览器的handlers包里即可找到方法的代码文档说明
package handlers_test

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/http/httptest"
)

// Example开头加上hanlders包中公开的方法名
// 开发人员自己编写的公开方法SendJSON的代码示例说明
func ExampleSendJSON() {
	r, _ := http.NewRequest("GET", "/sendjson", nil)
	w := httptest.NewRecorder()
	http.DefaultServeMux.ServeHTTP(w, r)

	var u struct {
		Name  string
		Email string
	}

	if err := json.NewDecoder(w.Body).Decode(&u); err != nil {
		log.Println("ERROR:", err)
	}

	fmt.Println(u)
}

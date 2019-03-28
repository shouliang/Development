// 展示如何测试内部服务断点
package handlers_test

import (
	"chapter9/listing17/handlers"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func init() {
	handlers.Routes()
}

const checkMark = "\u2713"
const ballotX = "\u2717"

// 测试/sendjson内部服务
func TestSendJSON(t *testing.T) {
	t.Log("Given the need to test the SendJSON endpoint.")
	{
		req, err := http.NewRequest("GET", "/sendjson", nil)

		if err != nil {
			t.Fatal("\tShould be able to create a request.", ballotX, err)
		}
		t.Log("\tShould be able to create a request.", checkMark)

		rw := httptest.NewRecorder()

		// 模拟了外部客户端对/sendjson路由的访问
		http.DefaultServeMux.ServeHTTP(rw, req)

		if rw.Code != 200 {
			t.Fatal("\tShould receive \"200\"", ballotX, rw.Code)
		}
		t.Log("\tShould receive \"200\"", checkMark)

		// 初始化u
		u := struct {
			Name  string
			Email string
		}{}

		// 将相应的文档解析到变量u
		if err := json.NewDecoder(rw.Body).Decode(&u); err != nil {
			t.Fatal("\tShould decode the response.", ballotX)
		}
		t.Log("\tShould decode the response.", checkMark)

		if u.Name == "Bill" {
			t.Log("\tShould have a Name.", checkMark)
		} else {
			t.Error("\tShould have a Name.", ballotX, u.Name)
		}

		if u.Email == "bill@gmail.com" {
			t.Log("\tShould have a Email.", checkMark)
		} else {
			t.Error("\tShould have a Email.", ballotX, u.Email)
		}

	}
}

package jsontest

import (
	"encoding/json"
	"testing"
)

var jsonStr = `{
        "basic_info":{
          "name":"zhangsan",
          "age":43
        },
        "job_info":{
                "skills":["Java","Go","C"]
        }
  }`

func TestEmbeddedJson(t *testing.T) {
	e := new(Employee)
	err := json.Unmarshal([]byte(jsonStr), e)// json.Unmarshal 	将json字符串解析为结构体
	if err != nil {
		t.Error(err)
	}
	t.Log(*e) 

	// json.Marshal 重新将结构体解析为字符串
	if v, err := json.Marshal(e); err == nil {
		t.Log(string(v))
	} else {
		t.Error(err)
	}
}

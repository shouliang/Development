package jsontest

import (
	"encoding/json"
	"testing"
)
// go get -u github.com/mailru/easyjson/...
// ~/go/bin/easyjson -all struct_def.go 就会生成 struct_def_easyjson.go

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
	err := json.Unmarshal([]byte(jsonStr), e)
	if err != nil {
		t.Error(err)
	}
	t.Log(*e) // 输出解析后的结构体

	if v, err := json.Marshal(e); err != nil {
		t.Error(err)
	} else {
		t.Log(string(v)) // 重新将结构体解析为字符串
	}
}

func TestEasyJson(t *testing.T) {
	e := Employee{}
	e.UnmarshalJSON([]byte(jsonStr))
	t.Log(e)
	if v, err := e.MarshalJSON(); err != nil {
		t.Error(err)
	} else {
		t.Log(string(v))
	}
}

func BenchmarkEmbeddedJson(b *testing.B) {
	b.ResetTimer()
	e := new(Employee)
	for i := 0; i < b.N; i++ {
		err := json.Unmarshal([]byte(jsonStr), e)
		if err != nil {
			b.Error(err)
		}

		if _, err := json.Marshal(e); err != nil {
			b.Error(err)
		}
	}
	b.StopTimer()
}

func BenchmarkEasyJson(b *testing.B) {
	b.ResetTimer()
	e := Employee{}
	for i := 0; i < b.N; i++ {
		e.UnmarshalJSON([]byte(jsonStr))
		if _, err := e.MarshalJSON(); err != nil {
			b.Error(err)
		}
	}
	b.StopTimer()
}

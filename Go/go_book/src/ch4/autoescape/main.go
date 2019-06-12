// template.HTML自动转义受信任的HTML数据
package main

import (
	"html/template"
	"log"
	"os"
)

func main() {
	const templ = `<p>A: {{.A}}</p><p>{{.B}}</p>`
	t := template.Must(template.New("escape").Parse(templ))
	var data struct {
		A string        // 不受信任的纯文本
		B template.HTML // 受信任的 HTML ,template.HTML自动将HTML元字符转义
	}
	data.A = "<b>Hello!</b>"
	data.B = "<b>Hello!</b>"
	// 模板.Execute 数据
	if err := t.Execute(os.Stdout, data); err != nil {
		log.Fatal(err)
	}
}

/* 版本管理： 特性在 1.5 版本作为实验特性被添加，1.6 中默认被启用，1.7 移除变量加入标准中。
查找依赖包路径
            1. 当前包下的vendor目录
            2. 向上级目录查找，直到找到src下的vendor目录
            3. 在GOPATH目录下查找
            4. 在GROOT目录下查找

进入当前包目录：glide init 生成glide.yaml配置文件
             glide install 下载依赖包到当前目录的vendor目录
*/
package remote

import (
	"testing"

	cm "github.com/easierway/concurrent_map" // cm 是包别名，方便引用或者防止冲突
)

func TestConcurrentMap(t *testing.T) {
	m := cm.CreateConcurrentMap(99)
	m.Set(cm.StrKey("key"), 10)
	t.Log(m.Get(cm.StrKey("key")))
}

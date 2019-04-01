package search

import (
	"encoding/json"
	"os"
)

const dataFile = "data/data.json"

type Feed struct {
	Name string `json:"site"`
	URI  string `json:"link"`
	Type string `json:"type"`
}

// 读取并反序列化源数据文件
func RetrieveFeeds() ([]*Feed, error) {
	file, err := os.Open(dataFile)

	if err != nil {
		return nil, err
	}

	defer file.Close()

	var feeds []*Feed

	// 将文件解码到一个切片里
	// 这个切片的每一项是一个指向一个Feed类型值的指针
	err = json.NewDecoder(file).Decode(&feeds)

	return feeds, err
}

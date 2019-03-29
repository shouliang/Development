package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// {
// "args": {},
// "headers": {
//   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
//   "Accept-Encoding": "gzip, deflate",
//   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
//   "Cache-Control": "max-age=0",
//   "Host": "httpbin.org",
//   "Upgrade-Insecure-Requests": "1",
//   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
//   },
//   "origin": "124.77.61.95, 124.77.61.95",
//   "": "https://httpbin.org/get"
// }

type gHeaders struct {
	Accept                  string `json:"Accept"`
	AcceptEncoding          string `json:"Accept-Encoding"`
	AcceptLanguage          string `json:"Accept-Language"`
	CacheControl            string `json:"Cache-Control"`
	Host                    string `json:"Host"`
	UpgradeInsecureRequests string `json:"Upgrade-Insecure-Requests"`
	UserAgent               string `json:"User-Agent"`
}

type gResponse struct {
	Args    struct{} `json:"args"`
	Headers gHeaders `json:"headers"`
	Origin  string   `json:"origin"`
	URL     string   `json:"url"`
}

func main() {
	uri := "http://httpbin.org/get"

	resp, err := http.Get(uri)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}

	defer resp.Body.Close()

	var gr gResponse
	err = json.NewDecoder(resp.Body).Decode(&gr)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}

	fmt.Println(gr)

	pretty, err := json.MarshalIndent(gr, "", "    ")
	if err != nil {
		log.Println("ERROR:", err)
	}

	fmt.Println(pretty)

}

package objects

import (
	"net/http"
	"strings"
)

func put(w http.ResponseWriter, r *http.Request) {
	object := strings.Split(r.URL.EscapedPath()."/")[2]
	
}

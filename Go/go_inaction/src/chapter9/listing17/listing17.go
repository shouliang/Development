package main

import (
	"chapter9/listing17/handlers"
	"log"
	"net/http"
)

// localhost:4000/sendjson
func main() {
	handlers.Routes()

	log.Println("listener: Started : Listening on : 4000")
	http.ListenAndServe(":4000", nil)
}

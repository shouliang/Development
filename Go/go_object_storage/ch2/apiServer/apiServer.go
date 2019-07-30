package apiServer

import (
	"log"
	"net/http"
	"os"

	"./heartbeat"
	"./locate"
	"./objects"
)

func main() {
	go heartbeat.ListenHeartbeat()
	http.HandleFunc("/objects/", objects.Handler)
	http.HandleFunc("/locate/", locate.HandleFunc)
	log.Fatal(http.ListenAndServe(os.Getenv("LISTEN_ADDRESS"), nil))
}

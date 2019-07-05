package main

import (
	"log"
	"time"

	"github.com/codemaveric/libra-go/pkg/goclient"
	"github.com/codemaveric/libra-go/pkg/librawallet"
)

func main() {
 	// Instantiate LibraWallet with mnemonic 
	wallet := librawallet.NewWalletLibrary("times good gospel coin social media giant")
	address, _, err := wallet.NewAddress() // Generate a new address
	if err != nil {
		log.Print(err)
	}
	log.Print(address.ToString())
  	
	// Libra Client Configuration
  	config := goclient.LibraClientConfig {
			Host: "ac.testnet.libra.org",
			Port: "80",
			Network: goclient.TestNet,			
		}
	// Instantiate LibraClient with Configuration
	libraClient := goclient.NewLibraClient(config)
  	
	// Mint coins on testnet to reciever address, amount is in microlibra
	libraClient.MintWithFaucetService(address.ToString(), 25000000, true)
  
	accState, err := libraClient.GetAccountState(address.ToString())

	log.Print(accState.Balance)	
}

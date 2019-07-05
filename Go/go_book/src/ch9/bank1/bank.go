// Package bank provides a concurrency-safe bank with one account
package bank

var deposits = make(chan int)
var balances = make(chan int)

func Deposit(amount int) { deposits <- amount } // send amout to deposit
func Banlance() int      { return <-balances }  // receive balance

func teller() {
	var balance int
	for {
		select {
		case amount := <-deposits:
			balance += amount
		case balances <- balance:
		}
	}
}

func init() {
	go teller()
}

package bank_test

import (
	"ch9/bank1"
	"fmt"
	"testing"
)

func TestBank(t *testing.T) {
	done := make(chan struct{})

	go func() {
		bank.Deposit(200)
		fmt.Println("=", bank.Banlance())
		done <- struct{}{}
	}()

	go func() {
		bank.Deposit(100)
		done <- struct{}{}
	}()

	<-done
	<-done

	if got, want := bank.Banlance(), 300; got != want {
		t.Errorf("Balance = %d,want %d", got, want)
	}
}

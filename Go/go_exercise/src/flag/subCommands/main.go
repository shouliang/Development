// 子命令 subCommand go run main.go foo -enable -name='zhangsan'
package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable tip")
	fooName := fooCmd.String("name", "", "tip for name")

	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "just level")

	if len(os.Args) < 2 {
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}

	switch os.Args[1] {
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'foo'")
		fmt.Println("	enable:", *fooEnable)
		fmt.Println("	name:", *fooName)
		fmt.Println("	tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("sumcommand 'bar'")
		fmt.Println("	level:", *barLevel)
		fmt.Println(" 	tail:", barCmd.Args())
	default:
		fmt.Println("expected 'foo' or 'bar' subcommand")
		os.Exit(1)
	}
}

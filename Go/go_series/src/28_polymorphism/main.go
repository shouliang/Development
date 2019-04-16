/* 多态
Go 通过接口来实现多态。我们已经讨论过，在 Go 语言中，我们是隐式地实现接口。
一个类型如果定义了接口所声明的全部方法，那它就实现了该接口

所有实现了接口的类型，都可以把它的值保存在一个接口类型的变量中。
在 Go 中，我们使用接口的这种特性来实现多态。
*/
package main

import "fmt"

// 接口： 收入
type Income interface {
	calculate() int // 计算收入的方法
	source() string // 收入来源
}

// 投标收入 结构体
type FixedBilling struct {
	projectName  string
	biddedAmount int
}

// 时间和材料收入 结构体
type TimeAndMaterial struct {
	projectName string
	noOfHours   int
	hourlyRate  int
}

// FixedBilling 实现了接口中的所有方法
func (fb FixedBilling) calculate() int {
	return fb.biddedAmount
}

func (fb FixedBilling) source() string {
	return fb.projectName
}

// TimeAndMaterial 实现了接口中的所有方法
func (tm TimeAndMaterial) calculate() int {
	return tm.noOfHours * tm.hourlyRate
}

func (tm TimeAndMaterial) source() string {
	return tm.projectName
}

// 新增一个广告收入流：calculateNetIncome 函数进行任何修改。这就是多态的好处。
type Advertisement struct {
	adName     string
	CPC        int
	noOfClicks int
}

// 新增一个广告收入流：calculateNetIncome 实现了接口中的所有方法
func (a Advertisement) calculate() int {
	return a.CPC * a.noOfClicks
}

func (a Advertisement) source() string {
	return a.adName
}

// 所有实现了接口的类型，都可以把它的值保存在一个接口类型的变量中。
// 根据 Income 接口的具体类型，程序会调用不同的 calculate() 和 source() 方法。
// 于是，我们在 calculateNetIncome 函数中就实现了多态。
func calculateNetIncome(ic []Income) {
	var netincome int = 0
	for _, income := range ic {
		fmt.Printf("Income From %s = $%d\n", income.source(), income.calculate())
		netincome += income.calculate()
	}
	fmt.Printf("Net income of organization = $%d\n", netincome)
}

func main() {
	project1 := FixedBilling{projectName: "Project 1", biddedAmount: 5000}
	project2 := FixedBilling{"Project 2", 10000}

	project3 := TimeAndMaterial{projectName: "Project 3", noOfHours: 160, hourlyRate: 25}

	bannerAd := Advertisement{adName: "Banner Ad", CPC: 2, noOfClicks: 500}
	popupAd := Advertisement{"Popup Ad", 5, 750}

	incomeStreams := []Income{project1, project2, project3, bannerAd, popupAd}
	calculateNetIncome(incomeStreams)
}

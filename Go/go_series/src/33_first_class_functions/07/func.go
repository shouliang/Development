// 实现自定义的过滤函数
package main

import "fmt"

type student struct {
	firstName string
	lastName  string
	grade     string
	country   string
}

// 过滤符合函数f的切片student
// 具体的过滤函数f可以有不同的实现
func filter(s []student, f func(student) bool) []student {
	var r []student
	for _, v := range s {
		if f(v) == true {
			r = append(r, v)
		}
	}
	return r
}

func main() {
	s1 := student{
		firstName: "Naveen",
		lastName:  "Ramanathan",
		grade:     "A",
		country:   "India",
	}

	s2 := student{
		firstName: "Samuel",
		lastName:  "Johnson",
		grade:     "B",
		country:   "USA",
	}

	studets := []student{s1, s2}

	// 通过student的grade过滤
	s_filter_grade := filter(studets, func(s student) bool {
		if s.grade == "B" {
			return true
		}
		return false
	})

	fmt.Println(s_filter_grade)

	// 通过student的country过滤
	s_filter_country := filter(studets, func(s student) bool {
		if s.country == "India" {
			return true
		}
		return false
	})

	fmt.Println(s_filter_country)
}

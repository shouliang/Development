package map_test

import "testing"

func TestInitMap(t *testing.T) {
	map1 := map[int]int{1: 1, 2: 4, 3: 9}
	t.Log(map1[2])
	t.Logf("len map1 = %d", len(map1))

	map2 := map[string]int{"one": 1, "two": 2, "three": 3}
	t.Log(map2["two"])
	t.Logf("len map2 = %d", len(map2))

	map3 := map[int]int{}
	map3[4] = 16
	t.Logf("len map3 = %d", len(map3))

	map4 := make(map[int]int, 10) // make初始化map,第二个参数为cap
	t.Logf("len map4 = %d", len(map4))
}

func TestAccessNotExistingKey(t *testing.T) {
	m1 := map[int]int{}
	t.Log(m1[1]) // 不存在的key,默认为零值,也不会报错，但是需要判断key的值是0，还是key不存在

	m1[2] = 0
	t.Log(m1[2])

	// if 语句里面有初始化语句，然后再判断初始化中的变量
	if v, ok := m1[333]; ok {
		t.Logf("key 333's value is %d", v)
	} else {
		t.Log("key 333 is not existing")
	}
}

// for rang
func TestTravelMap(t *testing.T) {
	m1 := map[int]int{2: 7, 4: 9, 5: 6}
	for k, v := range m1 {
		t.Log(k, v)
	}
}

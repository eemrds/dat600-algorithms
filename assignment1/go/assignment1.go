package main

import (
	"fmt"
	"math/rand"
	"reflect"
	"sort"
	"time"
)

func insertionSort(items []int) {
	for i := 1; i < len(items); i++ {
		key := items[i]
		j := i - 1
		for j >= 0 && items[j] > key {
			items[j+1] = items[j]
			j--
		}
		items[j+1] = key
	}

}

func merge(items []int, left int, middle int, right int) {
	n1 := middle - left + 1
	n2 := right - middle
	L := make([]int, n1)
	R := make([]int, n2)
	for i := 0; i < n1; i++ {
		L[i] = items[left+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = items[middle+j+1]
	}
	i, j, k := 0, 0, left
	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			items[k] = L[i]
			i++
		} else {
			items[k] = R[j]
			j++
		}
		k++
	}
	if i < n1 {
		for i < n1 {
			items[k] = L[i]
			i++
			k++
		}
	} else {
		for j < n2 {
			items[k] = R[j]
			j++
			k++
		}
	}
}

func mergeSort(items []int, left int, right int) {
	if left < right {
		middle := (left + right) / 2
		mergeSort(items, left, middle)
		mergeSort(items, middle+1, right)
		merge(items, left, middle, right)
	}

}

func quickSort(items []int, left int, right int) {
	if left < right {
		split := partition(items, left, right)
		quickSort(items, left, split-1)
		quickSort(items, split+1, right)
	}
}
func partition(items []int, left int, right int) int {
	x := items[right]
	i := left - 1
	for j := left; j >= left && j < right; j++ {
		if items[j] <= x {
			i++
			items[i], items[j] = items[j], items[i]
		}
	}
	items[i+1], items[right] = items[right], items[i+1]
	return i + 1
}

func maxHeapify(items []int, heapsize int, i int) {
	left := func(i int) int {
		return 2*i + 1
	}
	right := func(i int) int {
		return 2*i + 2
	}
	largest := i
	if left(i) < heapsize && items[left(i)] > items[i] {
		largest = left(i)
	}
	if right(i) < heapsize && items[right(i)] > items[largest] {
		largest = right(i)
	}
	if largest != i {
		items[i], items[largest] = items[largest], items[i]
		maxHeapify(items, heapsize, largest)
	}
}

func buildMaxHeap(items []int, heapsize int) {
	for i := heapsize / 2; i >= 0; i-- {
		maxHeapify(items, heapsize, i)
	}
}

func heapSort(items []int) {
	buildMaxHeap(items, len(items))
	for i := len(items) - 1; i >= 0; i-- {
		items[i], items[0] = items[0], items[i]
		maxHeapify(items, i, 0)
	}
}

type NamedFunction struct {
	Name string
	Func func([]int) []int
}

func main() {
	var itemsMain []int
	for i := 0; i < 10000; i++ {
		itemsMain = append(itemsMain, rand.Intn(100))
	}
	sortingAlgorithms := []NamedFunction{
		{"insertionSort", func(items []int) []int { insertionSort(items); return items }},
		{"mergeSort", func(items []int) []int { mergeSort(items, 0, len(items)-1); return items }},
		{"quickSort", func(items []int) []int { quickSort(items, 0, len(items)-1); return items }},
		{"heapSort", func(items []int) []int { heapSort(items); return items }},
	}
	for _, namedFunc := range sortingAlgorithms {
		items := make([]int, len(itemsMain))
		copy(items, itemsMain)

		start := time.Now()
		namedFunc.Func(items)
		elapsed := time.Since(start).Microseconds()
		fmt.Printf("Function: %s, Time elapsed: %d us.\n", namedFunc.Name, elapsed)

		sortedItems := make([]int, len(items))
		copy(sortedItems, items)
		sort.Ints(sortedItems)
		// fmt.Printf("Sorted items: %v\n", sortedItems)
		if !reflect.DeepEqual(sortedItems, items) {
			panic("Sorting algorithm is not correct")
		}
	}
}

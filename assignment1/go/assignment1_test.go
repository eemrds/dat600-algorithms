package main

import (
	"reflect"
	"testing"
)

func TestInsertionSort(t *testing.T) {
	cases := []struct {
		in, want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1, 0}, []int{0, 1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		got := c.in
		insertionSort(c.in)
		if !reflect.DeepEqual(got, c.want) {
			t.Errorf("insertionSort(%v) == %v, want %v", c.in, got, c.want)
		}
	}
}

func TestMergeSort(t *testing.T) {
	cases := []struct {
		in, want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1, 0}, []int{0, 1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		got := c.in
		mergeSort(c.in, 0, len(c.in)-1)
		if !reflect.DeepEqual(got, c.want) {
			t.Errorf("insertionSort(%v) == %v, want %v", c.in, got, c.want)
		}
	}
}

func TestQuicksort(t *testing.T) {
	cases := []struct {
		in, want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1, 0}, []int{0, 1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		got := c.in
		quickSort(c.in, 0, len(c.in)-1)
		if !reflect.DeepEqual(got, c.want) {
			t.Errorf("insertionSort(%v) == %v, want %v", c.in, got, c.want)
		}
	}
}

func TestHeapSort(t *testing.T) {
	cases := []struct {
		in, want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{5, 4, 3, 2, 1, 0}, []int{0, 1, 2, 3, 4, 5}},
	}

	for _, c := range cases {
		got := c.in
		heapSort(c.in)
		if !reflect.DeepEqual(got, c.want) {
			t.Errorf("insertionSort(%v) == %v, want %v", c.in, got, c.want)
		}
	}
}

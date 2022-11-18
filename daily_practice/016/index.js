// https://ithelp.ithome.com.tw/articles/10274633
// MaxHeap in JS

// 看不懂

class MaxHeap {
	constructor() {
		this.list = []
	}

	maxHeapify(arr, n, i) {
		let largest = i
		let l = 2 * i + 1
		let r = 2 * i + 2
		if (l < n && arr[l] > arr[largest]) {
			largest = l
		}
		if (r < n && arr[r] > arr[largest]) {
			largest = r
		}
		if (largest != i) {
			;[arr[i], arr[largest]] = [arr[largest], arr[i]]
			this.maxHeapify(arr, n, largest)
		}
	}

	push(num) {
		const size = this.list.length
		if (size === 0) {
			this.list.push(num)
		} else {
			this.list.push(num)
			for (let i = this.list.length / 2 - 1; i >= 0; i--) {
				this.maxHeapify(this.list, this.list.length, i)
			}
		}
	}

	pop(num) {
		const size = this.list.length
		let i
		for (i = 0; i < size; i++) {
			if (num === this.list[i]) {
				break
			}
		}

		;[this.list[i], this.list[size - 1]] = [this.list[size - 1], this.list[i]]

		this.list.splice(size - 1)

		for (let i = parseInt(this.list.length / 2 - 1); i >= 0; i--) {
			this.maxHeapify(this.list, this.list.length, i)
		}
	}

	getRoot() {
		this.list[0]
	}

	popRoot() {
		this.pop(this.list[0])
	}

	printHeap() {
		return this.list
	}
}

let heap = new MaxHeap()
heap.push(20)
heap.push(10)
heap.push(5)
heap.push(80)
heap.push(75)
heap.push(78)
heap.push(72)
heap.push(73)
console.log(heap.printHeap()) //80, 75, 78, 73, 20, 5, 72, 10
heap.popRoot()
console.log(heap.printHeap()) //78, 75, 72, 73, 20, 5, 10

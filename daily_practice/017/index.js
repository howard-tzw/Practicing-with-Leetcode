function maxHeapify(arr, n, i) {
	let largest = i
	let l = 2 * i + 1
	let r = 2 * i + 2

	if (l < n && arr[l] > arr[largest]) {
		largest = l
	}

	if (r < n && arr[r] > arr[largest]) {
		largest = r
	}

	if (largest !== i) {
		;[arr[i], arr[largest]] = [arr[largest], arr[i]]
		maxHeapify(arr, n, largest)
	}
}

function heapSort(arr) {
	const n = arr.length
	for (let i = n / 2 - 1; i >= 0; i--) {
		maxHeapify(arr, n, i)
	}

	for (let i = n - 1; i >= 0; i--) {
		;[arr[0], arr[i]] = [arr[i], arr[0]]
		maxHeapify(arr, i, 0)
	}
}

let data = [30, 20, 15, 1, 10, 5]
heapSort(data)
console.log(data) //[1, 5, 10, 15, 20, 30]

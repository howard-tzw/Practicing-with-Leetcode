// https://ithelp.ithome.com.tw/articles/10279960
// Radix Sort

function radixSort(arr) {
	// 找出最大位數
	let maxDigits = 0
	for (let num of arr) {
		maxDigits = maxDigits < num.toString().length ? num.toString().length : maxDigits
	}
	for (let i = 0; i < maxDigits; i++) {
		let buckets = Array.from({ length: 10 }, () => [])
		for (let j = 0; j < arr.length; j++) {
			let radix = Math.floor(arr[j] / Math.pow(10, i)) % 10
			buckets[radix].push(arr[j])
		}
		// 合併桶子的資料
		arr = [].concat(...buckets)
	}

	return arr
}

let arr = [28, 96, 5, 33, 60, 169, 170, 249, 362, 44, 84, 123]

console.log(radixSort(arr))

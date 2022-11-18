// https://ithelp.ithome.com.tw/articles/10280844
// Binary search

const data = [10, 15, 25, 40, 45, 55, 60, 80, 90]
const target = 55

function binarySort(arr, target) {
	let start = 0
	let end = arr.length - 1
	let mid

	while (start <= end) {
		mid = Math.floor((start + end) / 2)
		if (target > arr[start]) {
			start = mid + 1
		} else if (target < arr[end]) {
			end = mid - 1
		} else {
			return mid
		}
	}

	return null
}

console.log(binarySort(data, target))

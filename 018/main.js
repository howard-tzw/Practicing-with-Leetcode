// https://ithelp.ithome.com.tw/articles/10274995
// Undirected Graph
// Adjacency List

class Graph {
	constructor() {
		this.adjacencyList = {}
	}

	// 新增頂點
	addVertex(vertex) {
		if (!this.adjacencyList[vertex]) {
			this.adjacencyList[vertex] = []
		} else {
			return '頂點已存在'
		}
	}

	addEdge(vertex1, vertex2) {
		if (this.adjacencyList[vertex1]) {
			if (this.adjacencyList[vertex2]) {
				this.adjacencyList[vertex1].push(vertex2)
				this.adjacencyList[vertex2].push(vertex1)
			} else {
				return '第二項頂點不存在'
			}
		} else {
			return '第一項頂點不存在'
		}
	}

	removeVertex(vertex) {
		if (this.adjacencyList[vertex]) {
			this.adjacencyList[vertex].forEach(item => {
				this.removeEdge(vertex, item)
				delete this.adjacencyList[vertex]
			})
		} else {
			return '此頂點已不存在'
		}
	}

	removeEdge(vertex1, vertex2) {
		if (this.adjacencyList[vertex1]) {
			if (this.adjacencyList[vertex2]) {
				this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(vertex => vertex !== vertex2)
				this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(vertex => vertex !== vertex1)
			} else {
				return '第二項頂點已不存在'
			}
		} else {
			return '第一項頂點已不存在'
		}
	}

	printGraph() {
		console.log(this.adjacencyList)
	}
}

let graph = new Graph()
graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')
graph.addVertex('E')
graph.addVertex('F')

graph.addEdge('A', 'B')
graph.addEdge('A', 'D')
graph.addEdge('A', 'E')
graph.addEdge('B', 'C')
graph.addEdge('D', 'E')
graph.addEdge('E', 'F')
graph.addEdge('E', 'C')

graph.printGraph()

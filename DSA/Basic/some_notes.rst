- When you are converting length to index, reduce 1
- When you are converting index to length, add 1

visited = {}
visited[s[left]]-- is same as visited[s[left]] = visited[s[left]] - 1

sorting the array is O(nlog(n))

if (count === s.length) return true
else return false
.. can also be written as below
return (j === s.length) ? true : false
.. but (j === s.length) ? return true : return false is wrong


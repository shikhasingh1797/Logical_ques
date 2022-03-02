let arr = [1, 2, 3, 4, 5, 6, 7];
let n = arr.length-1;
var i=0
while(i<n/2){
  let temp = arr[i];
  arr[i] = arr[n-i];
  arr[n-i] = temp;
  i=i+1
}
console.log(arr);
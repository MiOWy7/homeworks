let arr = [9,8,7,6,5,4,3,2,1];

// Копии двумя способами
let arr2 = arr.slice(); // через slice (копия)
let arr3 = [...arr];    // через spread (копия)

arr2.reverse();        // способ 1: метод reverse (in-place для копии!)
arr3 = arr3.reduce((acc, x) => [x, ...acc], []); // способ 2: reduce

console.log('Исходный массив:', arr);
console.log('Копия 1 (reverse):', arr2);
console.log('Копия 2 (reduce):', arr3);
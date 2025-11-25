function kebabToCamel(str) {
    return str.split('-').map((part, i) => 
        i === 0 ? part : part.at(0).toUpperCase() + part.slice(1)
    ).join('');
}

console.log(kebabToCamel('background-color')); // backgroundColor
console.log(kebabToCamel('font-size'));       // fontSize
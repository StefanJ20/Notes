function reduce(arr, operation, startingValue) {
    let accumulator = startingValue;
    for (let index = 0; index < arr.length; index++) {
        accumulator = operation(accumulator, arr[index]);
    }
    return accumulator;
}

function sum(arr) {
    return reduce(arr, (accum, e) => accum + e, 0);
    //let total = 0;
    // for (let index = 0; index < arr.length; index++) {
        //total = total + arr[index];
    }
}

// return total;

function product(arr) {
    return reduce(arr, (accum, e) => accum * e, 0);
    //let total = 0;
    // for (let index = 0; index < arr.length; index++) {
        //total = total + arr[index];
    }
}

// return total;
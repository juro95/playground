//example of static type system

function add(a: number, b: number) {
  return a + b;
}

let sum = add(2, 3);

//sum = "hello"; // error

// type inference

let mixedArray = [1, "hello", true];

//mixedArray.push({}); // error

// explicit conversion
const number = 2;

const string = number.toString();

// implicit conversion
const num: number = 5;
const str: string = "7";
const result = num + str;
// TypeScript allows this operation and implicitly converts 'num' to a string "5", resulting in the string "57"

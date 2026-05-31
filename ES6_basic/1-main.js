import taskBlock from './1-block-scoped.js';
// the lack of backsticks and ${} is koz we are only passing the code
// there is no extra text.
console.log(taskBlock(true));
console.log(taskBlock(false));
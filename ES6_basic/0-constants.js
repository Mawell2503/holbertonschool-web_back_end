// export is keyword used to import function
export function taskFirst() {
  // const = constant
  // it declares a variable and locks its value
  // (doesnt allow for changes afterwards)
  const task = 'I prefer const when I can.';
  return task;
}
// this function returns the string 'is okay' 
export function getLast() {
  return ' is okay';
}

export function taskNext() {
  // let declares a variable.
  let combination = 'But sometimes let';
  // combination + wtv is in function getLast
  combination += getLast();

  return combination;
}

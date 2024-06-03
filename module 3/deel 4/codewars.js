// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
Examples:

function solution(str, ending) {
  let strIndex = str.length - 1;
  let endingIndex = ending.length - 1;

  while (ending[endingIndex] !== undefined) {
    if (str[strIndex] !== ending[endingIndex]) {
      return false;
    }
    strIndex--;
    endingIndex--;
  }

  return true;
}



console.log(solution('abc', 'abc')) // returns true
console.log(solution('abc', 'ac')) // returns false

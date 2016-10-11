/*
Remove all exclamation marks from the end of words.
Words are separated by spaces in the sentence.
*/
function remove(s){
  return s.split(' ').map((w) => w.replace(/\!+$/, '')).join(' ');
}

console.log(remove('afdsaf!!! !!!foo!'));

// remove("Hi!") === "Hi"
// remove("Hi!!!") === "Hi"
// remove("!Hi") === "!Hi"
// remove("!Hi!") === "!Hi"
// remove("Hi! Hi!") === "Hi Hi"
// remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"

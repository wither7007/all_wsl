a=[...document.getElementsByTagName('*')]
a.length
copy(a)
a.splice(1,2)

a.map((n)=>n.tagName)

const array1 = [1, 2, 3, 4];
a.reduce()
const s=(b)=>b.tagName==='P'
a.filter(n=>s(n))

const array = [15, 16, 17, 18, 19];
debugger
function reducer(previousValue, currentValue, index) {
  const returns = previousValue + currentValue;
  console.log(
    `previousValue: ${previousValue}, currentValue: ${currentValue}, index: ${index}, returns: ${returns}`,
  );
  return returns;
}
for (let item of Window) {  
  console.log(item) 
   /*rest of the code*/ 

}
array.reduce(reducer);


var lazyLoadables = [...document.querySelectorAll('.lazy-load')]
  .filter((element) => element.getAttribute('data-src').trim());

lazyLoadImages(lazyLoadables);
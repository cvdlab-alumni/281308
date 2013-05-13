function pushN(n){
	var numbers = [];
	for (i = 0; i < n; i++) {
		numbers.push(i);
	};
	return numbers;
};


function filterOdd(item, index, array){
	return item % 2 === 0;
};

function doubleF(item, index, array){
	return item *2;
};
function
 filterFourth(item, index, array){
	return item % 4 === 0;
};

function sum(prec, suc, index, array){
	return prec+suc;
};

pushN(20).filter(filterOdd).map(doubleF).filter(filterFourth).reduce(sum);
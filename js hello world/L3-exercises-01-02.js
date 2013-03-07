function identity(n) {
	var line = "";
	for (var i = 1; i <= n; i++) {
		for (var j = 1; j <= n; j++) {
			if (j===n){
				if(j===i)
					line+= "1";
				else line+= "0";
			}
			else if(j===i)
				line+= "1, \t";
			else line+= "0, \t";
		};
		console.log(line);
		if(i!==n)
			line = "";
	};
};

function fibonacci(n) {
	if(!(n in fibonacci))
		fibonacci[n] = fibonacci(n-2) + fibonacci(n-1);
	return fibonacci[n];
}

fibonacci[0] = 1;
fibonacci[1] = 1;
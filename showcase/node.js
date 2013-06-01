!(function (exports){

  var fs = require('fs');

  var plasm_lib = require('plasm.js');
  var obj = plasm_lib.plasm;
  var fun = plasm_lib.plasm_fun;
  var plasm = obj.plasm;
  var Plasm = obj.Plasm;

  var root = this;

  Object.keys(fun).forEach(function (k) { 
    root[k] = fun[k];
  });

  var p = new Plasm();
  fun.PLASM(p);


  var scmodel = (function () {
  /*///////////////////////////////////////////

  PASTE YOUR CODE HERE

  ///////////////////////////////////////////*/
  return model
  })();

  exports.author = 'vfede';
  exports.category = 'vehicles';
  exports.scmodel = scmodel;

  if (!module.parent) {
    fs.writeFile('C:/Users/vfede/Documents/GitHub/281308/showcase/data.json', JSON.stringify(scmodel.toJSON()));
  }

}(this));
// Exercise 1 - Javascript
// Define, with names pillars0, pillars1, pillars2, and pillars3,
// the models of pillars of the 4 house floors, and put them into the STRUCT
// of an initial building model.

// adapt pyplasm code to plasm.js code

T = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
     return object.clone().translate(dims, values);
    };
  };
};
  
R = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });
   
  return function (angle) {
    return function (object) {
      return object.clone().rotate(dims, angle);
    };
  };
};
  
S = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
      return object.clone().scale(dims, values);
    };
  };
};

S3 = S2;
S2 = S1;
S1 = S0;

GRID = SIMPLEX_GRID;
NN = REPLICA;
VIEW = DRAW;

//cilindro non pieno, preferito per alleggerire il carico computazionale
CYLINDER = CYL_SURFACE;
//cilindro pieno
/*CYLINDER = function (params) {
  var R = params[0];
  var h = params[1];
  return function (dims) {
    var domain = DOMAIN([[0,2*PI], [0,R]])([dims, 1]);
    var mapping = function (v) {
      var a = v[0];
      var r = v[1];
      return [r*COS(v[0]),r*SIN(v[0])]
    }
    var circle = MAP(mapping)(domain);
    return EXTRUDE([h])(circle)
  }
}*/

RED = [1,0,0,1];
GREEN = [0,1,0,1];
BLACK = [0,0,0,1];

//dimensioni pilastri
pillarDiameter = 0.25;
pillarRadius = 0.125;

//altezza piani: 2.70, 2.50, 2.50, 2.30 = tot 10 m
pillar0Height = 2.70;
pillar1e2Height = 2.50;
pillar3Height = 2.30;

//pilastro a base circolare, piano terra e primo piano
circularPillar0 = T([1,2])([pillarRadius,pillarRadius])(COLOR(RED)(CYLINDER([pillarRadius, pillar0Height])(24)));
circularPillar1 = T([1,2,3])([pillarRadius, pillarRadius, pillar0Height])(COLOR(RED)(CYLINDER([pillarRadius, pillar1e2Height])(24)));

pillarXdistance = 2.50;
pillarYdistance = 5.00;

//pilastri piano terra interni
pillars0a = COLOR(BLACK)(GRID([[-pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[-pillarDiameter, -pillarYdistance, pillarDiameter],[pillar0Height]]));
//pilastri piano terra circolari prima fila
pillars0b = STRUCT(NN(5)([circularPillar0, T([1])([pillarDiameter + pillarXdistance])]));
//pilastri piano terra circolari seconda fila (primo e ultimo)
pillars0c = T([2])([pillarDiameter + pillarYdistance])(STRUCT(NN(2)([circularPillar0, T([1])([4*pillarDiameter + 4*pillarXdistance])])));
//pilastri piano terra
pillars0 = STRUCT([pillars0a, pillars0b, pillars0c]);

//pilastri primo piano prima fila
pillars1a = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter],[-pillar0Height, pillar1e2Height]]);
//pilastri primo piano seconda fila (con spazio per 4a colonna circolare)
pillars1b = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, -pillarDiameter, -pillarXdistance, pillarDiameter],[-pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, pillar1e2Height]]);
//pilastro circolare primo piano
pillars1c = T([1,2])([3*pillarDiameter+3*pillarXdistance,pillarDiameter+pillarYdistance])(circularPillar1);
//pilastri primo piano
pillars1 = STRUCT([pillars1a, pillars1b, pillars1c]);

//pilastri secondo piano
pillars2 = COLOR(BLACK)(GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, pillar1e2Height]]));

//pilastri terzo dal terzo pilastro in poi
pillars3a = GRID([[-pillarDiameter, -pillarXdistance, -pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]);
//pilastri terzo piano seconda fila piccoli
pillars3b = COLOR(GREEN)(GRID([[pillarRadius, -pillarRadius, -pillarXdistance,  pillarRadius],[-pillarDiameter, -pillarYdistance, -pillarRadius, pillarRadius],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]));
//pilastri terzo piano
pillars3 = STRUCT([pillars3a, pillars3b]);

building = STRUCT([pillars0, pillars1, pillars2, pillars3]);

VIEW(building);
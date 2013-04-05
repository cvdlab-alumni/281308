// Exercise 1 - Python
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

GRID = COMP([INSR(PROD),AA(QUOTE)]);

pillarDiameter = 0.25;
pillarSmallDiameter = 0.125;

//altezza piani: 2.70, 2.50, 2.50, 2.30 = tot 10
pillar0Height = 2.70;
pillar1e2Height = 2.50;
pillar3Height = 2.30;

//pilastro a base circolare, piano terra e primo piano
circularPillar0 = T([1,2])([pillarSmallDiameter,pillarSmallDiameter])(COLOR(RED)(CYLINDER([pillarSmallDiameter, pillar0Height])(24)));
circularPillar1 = T([1,2,3])([pillarSmallDiameter, pillarSmallDiameter, pillar0Height])(COLOR(RED)(CYLINDER([pillarSmallDiameter, pillar1e2Height])(24)));

pillarXdistance = 2.50;
pillarYdistance = 5.50;

//pilastri piano terra interni
pillars0a = COLOR(BLACK)(GRID([[-pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[-pillarDiameter, -pillarYdistance, pillarDiameter],[pillar0Height]]));
//pilastri piano terra circolari prima fila
pillars0b = STRUCT(NN(5)([circularPillar0, T([1])([pillarDiameter + pillarXdistance])]))
//pilastri piano terra circolari seconda fila
pillars0c = T([2])([pillarDiameter + pillarYdistance])(circularPillar0);
//pilastri piano terra
pillars0 = STRUCT([pillars0a, pillars0b, pillars0c])

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
pillars3b = COLOR(GREEN)(GRID([[pillarSmallDiameter, -pillarSmallDiameter, -pillarXdistance,  pillarSmallDiameter],[-pillarDiameter, -pillarYdistance, -pillarSmallDiameter, pillarSmallDiameter],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]));
//pilastri terzo piano
pillars3 = STRUCT([pillars3a, pillars3b])

building = STRUCT([pillars0, pillars1, pillars2, pillars3])

VIEW(building)
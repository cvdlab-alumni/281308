// Exercise 5 - Javascript
// Define with names stair1, stair2, and stair3 (from bottom up to top), 
// and insert within the building model, the 3 stair models of the building.

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

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         PILLARS - begin
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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
pillars2 = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, pillar1e2Height]]);

//pilastri terzo piano dal terzo pilastro in poi
pillars3a = GRID([[-pillarDiameter, -pillarXdistance, -pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]);
//pilastri terzo piano seconda fila piccoli
pillars3b = COLOR(GREEN)(GRID([[pillarRadius, -pillarRadius, -pillarXdistance,  pillarRadius],[-pillarDiameter, -pillarYdistance, -pillarRadius, pillarRadius],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]));
//pilastri terzo piano
pillars3 = STRUCT([pillars3a, pillars3b]);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         PILLARS - end
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         FLOORS - begin
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

groundFloorDepth = 0.10;
floorDepth = 0.20;
floorWidth = 6.70;
floorLenght = 11.25;
floorFull = GRID([[floorLenght],[floorWidth],[floorDepth]]);

//ground floor
floors0 = GRID([[floorLenght],[floorWidth],[groundFloorDepth]]);

//first floor
balconyBase = GRID([[1.20],[1.20],[floorDepth]])
floors1balcony = T([1,2])([-1.10,5.25])(balconyBase);
floors1 = T([3])([pillar0Height])(STRUCT([floorFull, floors1balcony]));

//second floor
floors2a = GRID([[5.50],[-5.25, 1.45],[floorDepth]]);
floors2b = GRID([[-5.50,5.75],[6.70],[floorDepth]]);
triangularBalcony2_point = [[0,0],[1.25,0],[1.25,5.25],[0,5.25]];
triangularBalcony2_cells = [[0,2,3]];
triangularBalcony2d = SIMPLICIAL_COMPLEX(triangularBalcony2_point)(triangularBalcony2_cells);
floors2c = T([1,3])([5.50,0.2])(R([1,3])(PI)(EXTRUDE([floorDepth])(triangularBalcony2d)));
floors2 = T([3])([pillar0Height + pillar1e2Height])(STRUCT([floors2a, floors2b, floors2c]));

//third floor
floors3 = T([3])([pillar0Height + 2*pillar1e2Height])(floorFull);

//third floor ceiling
floors4a = GRID([[5.50],[-5.375, 1.325],[floorDepth]]);
floors4 = T([3])([pillar0Height + 2*pillar1e2Height + pillar3Height])(STRUCT([floors4a, floors2b]));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         FLOORS - end
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         VERTICALS - begin
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//north = ;
//south = ;

//east wall
//east ground floor
east0a = GRID([[9],[-6.45, 0.25],[2]]);
east0b = GRID([[7.2, -0.7, 1.1],[-6.45, 0.25],[-2, 0.7]]);
east0 = STRUCT([east0a, east0b]);
//east first floor
east1a = GRID([[floorLenght],[-6.45, 0.25],[0.8]]);
east1b = GRID([[6.25, -2.50, 2.50],[-6.45, 0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
east1 = T([3])([pillar0Height+floorDepth])(STRUCT([east1a, east1b]));
//east second floor
east2a = GRID([[floorLenght],[-6.45, 0.25],[0.8]]);
east2b = GRID([[9.25, -0.1, 0.35, -0.1, 1.45],[-6.45, 0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
east2 = T([3])([pillar0Height+pillar1e2Height+floorDepth])(STRUCT([east2a, east2b]));
//east third floor
east3a = GRID([[5.50],[-6.60, 0.10],[pillar3Height-0.2]]);
east3b = GRID([[-5.50, 5.75],[-6.45, 0.25],[pillar3Height-0.2]]);
east3 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+floorDepth])(STRUCT([east3a, east3b]));
//east fourth floor
east4 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(GRID([[floorLenght],[-6.60, 0.1],[0.4]]));
//east wall composition
east = STRUCT([east0, east1, east2, east3, east4]);

//west wall
//west ground floor
west0a = GRID([[-2.45, 6.05],[-2.15, 0.25],[0.8]]);
west0b = GRID([[-2.45, -0.25, -0.95, 1.8,-2.50],[-2.15, 0.25],[-0.8, pillar0Height-0.8]]);
west0inizioArco = GRID([[-2.45, -5.80, 0.75],[-3.95, 0.25],[pillar0Height]]);
west0 = STRUCT([west0a, west0b, west0inizioArco]);
//west first floor
west1a = GRID([[floorLenght],[0.25],[0.8]]);
west1b = GRID([[5.75, -2.50, 2.75],[0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
westBaseWall = STRUCT([west1a, west1b]);
west1 = T([2,3])([-0.001,pillar0Height+floorDepth])(westBaseWall);
//west second floor
west2 = T([2,3])([-0.001,pillar0Height+pillar1e2Height+floorDepth])(westBaseWall);
//west third floor
west3a = GRID([[11.25],[0.25],[0.8]]);
west3b = GRID([[-6, -2.50, 2.50],[0.25],[-0.8, pillar3Height-0.8-floorDepth]]);
west3 = T([2,3])([-0.001,pillar0Height+pillar1e2Height+pillar1e2Height+floorDepth])(STRUCT([west3a, west3b]));
//west fourth floor
west4 = T([2,3])([-0.001,pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(GRID([[-5.50, 5.75],[0.1],[0.4]]));
west4a = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(GRID([[5.50],[-(pillarDiameter+pillarYdistance+pillarRadius), 0.1],[0.4]]));
//west wall composition
west = STRUCT([west0, west1, west2, west3, west4, west4a]);

//south wall
//ground floor walls
south0a = GRID([[-2.45, 0.25],[-1.65, 3.85],[0.8]]);
south0b = GRID([[-2.45, 0.25],[-1.65, 0.75, -2.85, 0.25],[-0.8, pillar0Height-0.8]]);
south0a2 = GRID([[-2.45, -0.25, -0.95, 0.25],[-1.65, 0.75],[pillar0Height]]);
south0a3 = GRID([[-2.45, -0.25, -0.95, -0.25, -4.35, 0.25],[-2.15, 1.0],[pillar0Height]]);
south0 = STRUCT([south0a, south0a2, south0a3, south0b]);

south4a = GRID([[-5.50, 0.1],[-0.099, floorWidth-1.325],[0.4]]);
south4b = GRID([[0.1],[-5.375, 1.325],[0.4]]);
south4 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(STRUCT([south4a, south4b]));

//south wall composition
//south = STRUCT([south0, south1, south2, south3, south4]);
south = STRUCT([south0, south4]);
//south wall composition
//south = STRUCT([south0, south1, south2, south3, south4]);
south = STRUCT([south0, south4]);
function arc(alpha, r, R){
  var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);
  var mapping = function (v){
    var a = v[0];
    var r = v[1];
    return [r*COS(a), r*SIN(a)];
  }
  var model = MAP(mapping)(domain);
  return model;
}

//arco1 = PROD([arc(PI,0.75,1), Q(pillar0Height)]);
//arco2 = PROD([arc(PI,2.75,3), Q(pillar0Height)]);

arch1 = T([1,2])([2.45+0.73, 1.65])(R([1,2])(PI)(EXTRUDE([pillar0Height])(arc(PI,0.48,0.73))));
arch2 = T([1,2])([2.45+5.80+0.75,4.70])(R([1,2])(3*PI/2)(EXTRUDE([pillar0Height])(arc(PI,1.75,2))));
arches = STRUCT([arch1,arch2]);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         VERTICALS - end
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         WINDOWS - begin
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

windowVertFrame = COLOR(BLACK)(CUBOID([0.1,0.25,pillar1e2Height-0.25]));
windowHorFrame = COLOR(BLACK)(CUBOID([5.0,0.25,0.1]));
planeFrame = T([1,2,3])([0.25,0.25,pillar0Height+pillar1e2Height])(R([1,2])(PI/2.0)(CUBOID([5.0,0.25,floorDepth])));

windowHframes = STRUCT(NN(3)([windowHorFrame ,T([3])([1.10])]));
windowVframes = STRUCT(NN(5)([windowVertFrame ,T([1])([1.225])]));
windowBig = T([1,2,3])([0.25,0.25,pillar0Height+floorDepth])(R([1,2])(PI/2.0)(STRUCT([windowVframes, windowHframes])));
windowBig2 = T([1,2,3])([0.25,0.25,pillar0Height+pillar1e2Height+floorDepth])(R([1,2])(PI/2.0)(STRUCT([windowVframes, windowHframes])));

windowsFrames = STRUCT([windowBig, windowBig2, planeFrame]);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         WINDOWS - end
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         STAIRS - begin
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

step_depth = floorDepth;
step_raiser0 = pillar0Height/13.0;
step_raiser1 = pillar1e2Height/13.0;

step2d_points = [[0,0],[0,floorDepth+step_raiser0],[step_depth,step_raiser0],[step_depth,floorDepth+step_raiser0]];
step2d_points1 = [[0,0],[0,floorDepth+step_raiser1],[step_depth,step_raiser1],[step_depth,floorDepth+step_raiser1]];
step2d_cells = [[0,2,1],[1,2,3]];
step2d = SIMPLICIAL_COMPLEX(step2d_points)(step2d_cells);
step2d1 = SIMPLICIAL_COMPLEX(step2d_points1)(step2d_cells);
step2d_extruded = EXTRUDE([1.2])(step2d);
step2d_extruded1 = EXTRUDE([1.2])(step2d1);
step3d = MAP([S1,S3,S2])(step2d_extruded);
step3d1 = MAP([S1,S3,S2])(step2d_extruded1);
ramp0 = STRUCT(NN(13)([step3d,T([1,3])([step_depth,step_raiser0])]));
ramp1 = STRUCT(NN(13)([step3d1,T([1,3])([step_depth,step_raiser1])]));

stairs1 = T([1,2])([pillarXdistance, pillarDiameter+pillarYdistance])(ramp0);
stairs2 = T([1,2,3])([1.0, pillarDiameter+pillarYdistance, pillar0Height])(ramp1);
stairs3 = T([1,2,3])([2*pillarXdistance+2*pillarDiameter, pillarDiameter+pillarYdistance, pillar0Height+pillar1e2Height])(ramp1);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                         STAIRS - end
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

building = STRUCT([pillars0, pillars1, pillars2, pillars3, floors0, floors1, floors2, floors3, floors4, east, west, south, windowsFrames, stairs1, stairs2, stairs3, arches]);

VIEW(building)
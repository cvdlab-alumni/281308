# Exercise 2 - Python
# Define, with names north, south, east, and west, the 4 models of vertical enclosures
# (including the hollows), and add them to the STRUCT of the building model.

GRID = COMP([INSR(PROD),AA(QUOTE)]);

#####################################################################
#                         PILLARS - begin
#####################################################################

pillarDiameter = 0.25;
pillarRadius = 0.125;

#altezza piani: 2.70, 2.50, 2.50, 2.30 = tot 10 m
pillar0Height = 2.70;
pillar1e2Height = 2.50;
pillar3Height = 2.30;

#pilastro a base circolare, piano terra e primo piano
circularPillar0 = T([1,2])([pillarRadius,pillarRadius])(COLOR(RED)(CYLINDER([pillarRadius, pillar0Height])(24)));
circularPillar1 = T([1,2,3])([pillarRadius, pillarRadius, pillar0Height])(COLOR(RED)(CYLINDER([pillarRadius, pillar1e2Height])(24)));

pillarXdistance = 2.50;
pillarYdistance = 5.00;

#pilastri piano terra interni
pillars0a = COLOR(BLACK)(GRID([[-pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[-pillarDiameter, -pillarYdistance, pillarDiameter],[pillar0Height]]));
#pilastri piano terra circolari prima fila
pillars0b = STRUCT(NN(5)([circularPillar0, T([1])([pillarDiameter + pillarXdistance])]));
#pilastri piano terra circolari seconda fila (primo e ultimo)
pillars0c = T([2])([pillarDiameter + pillarYdistance])(STRUCT(NN(2)([circularPillar0, T([1])([4*pillarDiameter + 4*pillarXdistance])])));
#pilastri piano terra
pillars0 = STRUCT([pillars0a, pillars0b, pillars0c]);

#pilastri primo piano prima fila
pillars1a = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter],[-pillar0Height, pillar1e2Height]]);
#pilastri primo piano seconda fila (con spazio per 4a colonna circolare)
pillars1b = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, -pillarDiameter, -pillarXdistance, pillarDiameter],[-pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, pillar1e2Height]]);
#pilastro circolare primo piano
pillars1c = T([1,2])([3*pillarDiameter+3*pillarXdistance,pillarDiameter+pillarYdistance])(circularPillar1);
#pilastri primo piano
pillars1 = STRUCT([pillars1a, pillars1b, pillars1c]);

#pilastri secondo piano
pillars2 = GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, pillar1e2Height]]);

#pilastri terzo piano dal terzo pilastro in poi
pillars3a = GRID([[-pillarDiameter, -pillarXdistance, -pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]);
#pilastri terzo piano seconda fila piccoli
pillars3b = COLOR(GREEN)(GRID([[pillarRadius, -pillarRadius, -pillarXdistance,  pillarRadius],[-pillarDiameter, -pillarYdistance, -pillarRadius, pillarRadius],[-pillar0Height, -pillar1e2Height, -pillar1e2Height, pillar3Height]]));
#pilastri terzo piano
pillars3 = STRUCT([pillars3a, pillars3b]);

#####################################################################
#                         PILLARS - end
#####################################################################

#####################################################################
#                         FLOORS - begin
#####################################################################

groundFloorDepth = 0.10;
floorDepth = 0.20;
floorWidth = 6.70;
floorLenght = 11.25;
floorFull = GRID([[floorLenght],[floorWidth],[floorDepth]]);

#ground floor
floors0 = GRID([[floorLenght],[floorWidth],[groundFloorDepth]]);

#first floor
balconyBase = GRID([[1.20],[1.20],[floorDepth]])
floors1balcony = T([1,2])([-1.10,5.25])(balconyBase);
floors1 = T([3])([pillar0Height])(STRUCT([floorFull, floors1balcony]));

#second floor
floors2a = GRID([[5.50],[0.25, -5.0, 1.45],[floorDepth]]);
floors2b = GRID([[-5.50,5.75],[6.70],[floorDepth]]);
triangularBalcony2_point = [[0,0],[1.25,0],[1.25,5.25],[0,5.25]];
triangularBalcony2_cells = [[3,4,5]];
triangularBalcony2d = MKPOL([triangularBalcony2_point, triangularBalcony2_cells, None]);
floors2c = T([1])([5.50])(R([1,3])(PI)(PROD([triangularBalcony2d, Q(-floorDepth)])));
floors2 = T([3])([pillar0Height + pillar1e2Height])(STRUCT([floors2a, floors2b, floors2c]));

#third floor
floors3 = T([3])([pillar0Height + 2*pillar1e2Height])(floorFull);

#third floor ceiling
floors4a = GRID([[5.50],[-5.375, 1.325],[floorDepth]]);
floors4 = T([3])([pillar0Height + 2*pillar1e2Height + pillar3Height])(STRUCT([floors4a, floors2b]));

#####################################################################
#                         FLOORS - end
#####################################################################

#####################################################################
#                         VERTICALS - begin
#####################################################################

#north = ;
#south = ;

#east wall
#east ground floor
east0a = GRID([[9],[-6.45, 0.25],[2]]);
east0b = GRID([[7.2, -0.7, 1.1],[-6.45, 0.25],[-2, 0.7]]);
east0 = STRUCT([east0a, east0b]);
#east first floor
east1a = GRID([[floorLenght],[-6.45, 0.25],[0.8]]);
east1b = GRID([[6.25, -2.50, 2.50],[-6.45, 0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
east1 = T([3])([pillar0Height+floorDepth])(STRUCT([east1a, east1b]));
#east second floor
east2a = GRID([[floorLenght],[-6.45, 0.25],[0.8]]);
east2b = GRID([[9.25, -0.1, 0.35, -0.1, 1.45],[-6.45, 0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
east2 = T([3])([pillar0Height+pillar1e2Height+floorDepth])(STRUCT([east2a, east2b]));
#east third floor
east3a = GRID([[5.50],[-6.60, 0.10],[pillar3Height-0.2]]);
east3b = GRID([[-5.50, 5.75],[-6.45, 0.25],[pillar3Height-0.2]]);
east3 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+floorDepth])(STRUCT([east3a, east3b]));
#east fourth floor
east4 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(GRID([[floorLenght],[-6.60, 0.1],[0.4]]));
#east wall composition
east = STRUCT([east0, east1, east2, east3, east4]);

#west wall
#west ground floor
#west0a = GRID([[9],[0.25],[2]]);
#west1b = GRID([[6.25, -2.50, 2.50],[0.25],[-0.8, pillar1e2Height-0.7-0.30]]);
#west0 = STRUCT([west0a, west0b]);
#west first floor
west1a = GRID([[floorLenght],[0.25],[0.8]]);
west1b = GRID([[5.75, -2.50, 2.75],[0.25],[-0.8, pillar1e2Height-0.8-floorDepth]]);
westBaseWall = STRUCT([west1a, west1b]);
west1 = T([3])([pillar0Height+floorDepth])(westBaseWall);
#west second floor
west2 = T([3])([pillar0Height+pillar1e2Height+floorDepth])(westBaseWall);
#west third floor
west3a = GRID([[11.25],[0.25],[0.8]]);
west3b = GRID([[-6, -2.50, 2.50],[0.25],[-0.8, pillar3Height-0.8-floorDepth]]);
west3 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+floorDepth])(STRUCT([west3a, west3b]));
#west fourth floor
west4 = T([3])([pillar0Height+pillar1e2Height+pillar1e2Height+pillar3Height+floorDepth])(GRID([[-5.50, 5.75],[0.1],[0.4]]));
#west wall composition
west = STRUCT([west1, west2, west3, west4]);

#####################################################################
#                         VERTICALS - end
#####################################################################

building = STRUCT([pillars0, pillars1, pillars2, pillars3, floors0, floors1, floors2, floors3, floors4, east, west]);

VIEW(building)
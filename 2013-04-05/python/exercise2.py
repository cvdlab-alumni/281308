# Exercise 2 - Python
# Define plan by plan, with names floor0, floor1, floor2, floor3, and floor4,
# the 5 models of horizontal partitions, and add them to the STRUCT of the building model.

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
pillars2 = COLOR(BLACK)(GRID([[pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter, -pillarXdistance, pillarDiameter],[pillarDiameter, -pillarYdistance, pillarDiameter],[-pillar0Height, -pillar1e2Height, pillar1e2Height]]));

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

floorDepth = 0.20;
floorWidth = 6.70;
floorLenght = 11.25;
floorFull = GRID([[floorLenght],[floorWidth],[floorDepth]]);

#first floor
balconyBase = GRID([[1.20],[1.20],[floorDepth]])
floors1balcony = T([1,2])([-1.10,5.25])(balconyBase);
floors1 = T([3])([pillar0Height])(STRUCT([floorFull, floors1balcony]));

#second floor
floors2a = GRID([[5.50],[-5.25, 1.45],[floorDepth]]);
floors2b = GRID([[-5.50,5.75],[6.70],[floorDepth]]);
triangularBalcony2_point = [[0,0],[1.25,0],[1.25,5.25],[0,5.25]];
triangularBalcony2_cells = [[3,4,5]];
triangularBalcony2d = MKPOL([triangularBalcony2_point, triangularBalcony2_cells, None]);
floors2c = T([1,2])([5.50,0.2])(R([1,3])(PI)(PROD([triangularBalcony2d, Q(-floorDepth)])));
floors2 = T([3])([pillar0Height + pillar1e2Height])(STRUCT([floors2a, floors2b, floors2c]));

#third floor
floors3 = T([3])([pillar0Height + 2*pillar1e2Height])(floorFull);

#soffitto
floors4a = GRID([[5.50],[-5.375, 1.325],[floorDepth]]);
floors4 = T([3])([pillar0Height + 2*pillar1e2Height + pillar3Height])(STRUCT([floors4a, floors2b]));

floors0 = floors3;

#####################################################################
#                         FLOORS - end
#####################################################################

building = STRUCT([pillars0, pillars1, pillars2, pillars3, floors0, floors1, floors2, floors3, floors4]);

VIEW(building)
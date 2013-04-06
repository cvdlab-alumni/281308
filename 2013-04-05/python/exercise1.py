# Exercise 1 - Python
# Define, with names pillars0, pillars1, pillars2, and pillars3,
# the models of pillars of the 4 house floors, and put them into the STRUCT of an initial building model.

GRID = COMP([INSR(PROD),AA(QUOTE)]);

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

building = STRUCT([pillars0, pillars1, pillars2, pillars3]);

VIEW(building);
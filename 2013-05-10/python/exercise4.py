# Exercise 4 - Python
# Generate the 3D model of a steering wheel specifically designed for Formula and Sport cars 
# (look on the web for common shapes). Mount it the the 2.5D mock-up.

domain=GRID([10])

#profilo XY base
pointsXY = [[30,1085],[30,1085],[30,1085],[40,1220],[83,1300],[83,1300],[225,1330],[440,1330],[455,1320],[455,1320],[737,1320],[900,1360],[1162,1320],[1162,1320],[1162,1320],[1175,1250],[1175,1085],[1175,1085],[1175,1085]];
halfLatoXY = T(2)(-1085)(SPLINE(CUBICUBSPLINE(domain))(pointsXY));
latoXY = T(3)(0)(STRUCT([ R([1,3])(PI)(R([1,2])(PI)(halfLatoXY)), halfLatoXY ]))

#profilo XZ central
pointsXZc = [[25,315],[25,315],[25,315],[1030,315],[1030,315],[1160,270],[1170,270],[1170,220],[1170,220],[1165,220],[1165,220],[1165,215],[1165,215],[1170,215],[1170,215],[1170,200],[1170,200],
[1155,200],[1155,200],[1155,135],[1155,135],[1170,135],[1170,135],[1170,120],[1170,120],
[810,65],[810,65],[620,50],[560,65],[560,65],[355,150],[355,150],[200,170],
[40,245],[40,245],[40,250],[40,250],[45,250],[45,250],[45,255],[45,255],[40,255],[40,265],[40,265],[45,265],[45,300],[40,300],[35,300],[35,310],[35,310],[25,310],[25,310],[25,315],[25,315],[25,315]];
profiloXZ = R([2,3])(-PI/2.0)(T([2])(-315)(SPLINE(CUBICUBSPLINE(domain))(pointsXZc)));

#profilo XZ side
pointsXZs = [[25,315],[25,315],[25,315],
[230,315],[230,315],[230,180],[410,180],[420,315],[420,315],
[810,315],[850,325],[850,190],[940,150],[1020,160],
[1070,290],[1070,290],
[1160,270],[1160,270],[1160,50],[1160,50],[1085,60],[1085,60],
[1060,120],[1060,120],[730,140],[730,140],
[540,155],[540,155],[455,155],[455,155],[355,150],[355,150],[200,170],
[40,245],[40,245],[40,250],[40,250],[45,250],[45,250],[45,255],[45,255],[40,255],[40,265],[40,265],[45,265],[45,300],[40,300],[35,300],[35,310],[35,310],[25,310],[25,310],[25,315],[25,315],[25,315]];
profiloXZsR = R([2,3])(-PI/2.0)(T([2,3])([-315,230])(SPLINE(CUBICUBSPLINE(domain))(pointsXZs)));
profiloXZsL = T([2])([-460])(profiloXZsR);
profiloXZs = STRUCT([profiloXZsL,profiloXZsR])

#profilo YZ front
pointsYZf1 = [[310,705],[310,705],[310,705],[95,705],[95,705],[85,650],[85,650],[310,650],[310,650],[310,650]];
hprofiloYZf1 = T([2])(-705)(SPLINE(CUBICUBSPLINE(domain))(pointsYZf1));
profiloYZf1 = STRUCT([ T([1])(620)(R([1,3])(PI)(hprofiloYZf1)), hprofiloYZf1 ])
pointsYZf2 = [[310,650],[310,650],[310,650],[200,650],[200,650],[170,625],[185,615],[185,615],[310,615],[310,615],[310,615]]; 
hprofiloYZf2 = T([2])(-660)(SPLINE(CUBICUBSPLINE(domain))(pointsYZf2));
profiloYZf2 = STRUCT([ T([1])(620)(R([1,3])(PI)(hprofiloYZf2)), hprofiloYZf2 ])
pointsYZf3 = [[145,650],[145,650],[145,650],[110,650],[110,650],[90,625],[105,615],[105,615],[140,615],[140,615],[140,615],[145,650],[145,650],[145,650]]; 
hprofiloYZf3 = T([2])(-660)(SPLINE(CUBICUBSPLINE(domain))(pointsYZf3));
profiloYZf3 = STRUCT([ T([1])(620)(R([1,3])(PI)(hprofiloYZf3)), hprofiloYZf3 ])

profiloYZf = T([1,2,3])([40,310,5])(R([1,2])(-PI/2.0)(R([2,3])(-PI/2.0)(STRUCT([profiloYZf1,profiloYZf2,profiloYZf3 ]))))

#profilo YZ hood
pointsYZh = [[310,705],[310,705],[310,705],[65,705],[65,705],[65,575],[75,560],[140,550],[310,545],[310,545],[310,545]];
hprofiloYZh = T([2])(-705)(SPLINE(CUBICUBSPLINE(domain))(pointsYZh));
profiloYZhp = STRUCT([ T([1])(620)(R([1,3])(PI)(hprofiloYZh)), hprofiloYZh ])
profiloYZh = T([1,2])([320,310])(R([1,2])(-PI/2.0)(R([2,3])(-PI/2.0)(profiloYZhp)))


#profilo YZ cabin
VIEW(STRUCT([latoXY, profiloXZ, profiloXZs, profiloYZf, profiloYZh]))
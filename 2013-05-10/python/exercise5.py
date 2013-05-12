# Exercise 5 - Python
# Create at least two interesting car surfaces and add them to the mock-up.


########## Exercise 2 ##########

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

########## End Exercise 2 ##########

########## Exercise 3 ##########

def slidePoints(coord):
	x = coord[0]
	y = coord[1]
	z = coord[2]
	def slidePoints0(points):
		p = []
		for a in points:
			c = [0,0,0]
			c[0] = a[0]+x
			c[1] = a[1]+y
			c[2] = a[2]+z
			p.append(c)
		return p
	return slidePoints0

GREY = Color4f(0.2,0.2,0.2,1);
LIGHTGREY = Color4f(0.6,0.6,0.6,1);
GOLD = Color4f(1,0.85,0.40,1);
#VIEW(MAP(tyreProfile)(GRID([20,20])))

wheelDomain2D = GRID([30,40])
wheelDomain = S(2)(2*PI)(MAP([S2,S1])(wheelDomain2D))

tyrePoints = [[0,0,0],[85,0,0],[0,0,50],[85,0,100],[0,0,100]]
tyrePointsS = slidePoints([110,0,0])(tyrePoints)
tyreProfile = BEZIER(S1)(tyrePointsS)
tyre = MAP(ROTATIONALSURFACE(tyreProfile))(wheelDomain)


rim1Points = [[20,0,20],[0,0,20],[20,0,0],[6,0,0]]
rim1PointsS = slidePoints([90,0,0])(rim1Points)
rim1Profile = BEZIER(S1)(rim1PointsS)
rim1L = T([3])(80)(MAP(ROTATIONALSURFACE(rim1Profile))(wheelDomain))
rim1R = T([3])(100)(R([1,3])(PI)(rim1L))

rim2Points = [[10,0,10],[0,0,10],[10,0,0],[-5,0,0]]
rim2PointsS = slidePoints([86,0,0])(rim2Points)
rim2Profile = BEZIER(S1)(rim2PointsS)
rim2L = T([3])(70)(MAP(ROTATIONALSURFACE(rim2Profile))(wheelDomain))
rim2R = T([3])(100)(R([1,3])(PI)(rim2L))

bolt = T([1,3])([86,70])(STRUCT([TUBE([1,3,3])(6), TUBE([0,1.5,4])(15)]))

# ho provato a fare la funzione che le ruota ma ho usato troppo tempo e son dovuto ritornare a questa.
bolts = STRUCT ([
	R([1,2])(PI)(bolt),R([1,2])(0)(bolt),
	R([1,2])(PI*0.9)(bolt),R([1,2])(PI*0.8)(bolt),R([1,2])(PI*0.7)(bolt),
	R([1,2])(PI*0.6)(bolt),R([1,2])(PI*0.5)(bolt),R([1,2])(PI*0.4)(bolt),
	R([1,2])(PI*0.3)(bolt),R([1,2])(PI*0.2)(bolt),R([1,2])(PI*0.1)(bolt),
	R([1,2])(-PI*0.9)(bolt),R([1,2])(-PI*0.8)(bolt),R([1,2])(-PI*0.7)(bolt),
	R([1,2])(-PI*0.6)(bolt),R([1,2])(-PI*0.5)(bolt),R([1,2])(-PI*0.4)(bolt),
	R([1,2])(-PI*0.3)(bolt),R([1,2])(-PI*0.2)(bolt),R([1,2])(-PI*0.1)(bolt)])

star = COLOR(GOLD)(T([3])([70])(S([1,2,3])([50,50,50])(STAR(5))));
mozzo = T([3])([71])(STRUCT([
	TUBE([35,40,5])(30),
	TUBE([15,20,10])(6),
	TUBE([1,15,5])(30)
	])  );

wheelR = T([1,2,3])([190,-320,40])(S([1,2,3])([0.55,0.55,0.55])(
		R([1,2])(PI/2.0)(R([1,3])(-PI/2.0)(
	STRUCT([
	COLOR(GREY)(tyre),
	rim1L, rim1R,
	rim2L, rim2R,
	COLOR(LIGHTGREY)(bolts),
	star, mozzo])))))

wheelL = T([1,2,3])([190,-320,40])(S([1,2,3])([0.55,0.55,0.55])(
		R([1,2])(-PI/2.0)(R([1,3])(-PI/2.0)(
	STRUCT([
	COLOR(GREY)(tyre),
	rim1L, rim1R,
	rim2L, rim2R,
	COLOR(LIGHTGREY)(bolts),
	star, mozzo])))))

FRwheel = T([1,2])([130,500])(wheelR)
RRwheel = T([1])([600])(S([1,2,3])([1.1,1.1,1.1])(FRwheel))

FLwheel = T([1,2])([130,140])(wheelL)
RLwheel = T([1])([600])(S([1,2,3])([1.1,1.1,1.1])(FLwheel))


########## End Exercise 3 ##########

domain= GRID([10,10])

steerTorus = COLOR(BLACK)(S([1,2,3])([1.57,1.57,1.57])(TORUS([27.5,33])([30,30])));

razze = STRUCT([
COLOR(GREY)(T([3])([-0.1])(CYLINDER([17,2.1])(20))),
COLOR(BLACK)(TUBE([8,12,3])(20)),
COLOR(YELLOW)(CYLINDER([8,3])(20)),
COLOR(GREY)(T([1,2])([-10,-50])(CUBOID([10,100,2]))),
COLOR(GREY)(T([1,2])([0,-5])(CUBOID([50,10,2]))),
])

steeringWheel = T([1,2,3])([500,-100,130])(R([1,3])(-PI/2.0)(STRUCT([razze, steerTorus])))

#car
car = COLOR(RED)(STRUCT([latoXY, profiloXZ, profiloXZs, profiloYZf, profiloYZh]))

########## End Exercise 2 ##########

########## Exercise 5 ##########

wingDomain=MAP([S2,S1])(GRID([20,20]))
wingBordo = BEZIER(S1)([[1,0,0],[0.6,0,230],[1,0,460]])
wingSection = BEZIER(S2)([[0, 0], [100, 0], [100, 28], [0,0]])

wing = T([1,2,3])([1158,230,262])(
	R([1,3])(PI)(R([2,3])(PI/2.0)(
		MAP(PROFILEPRODSURFACE([wingBordo,wingSection]))(wingDomain)
		)))

########## End Exercise 5 ##########

########## Cofano ##########

domain = GRID([30,30])

#i nove valori numerici usati da tutti i punti
x1 = 0
x2 = 25
x3 = 0
y1 = 500
y2 = 0
y3 = 85
z1 = 500
z2 = 500
w1 = 0

#i quattro vertici della patch
p1 = [x1,x2,x3]
p2 = [y1,y2,y3]
p3 = [z1,(z2-y2),y3]
p4 = [w1,(z2-x2),x3]

#manici delle curve dei profili presi direttamente dal blueprint:
c4mp1 = [x1-110, x2+10, x3]
c4mp4 = [w1-110, (z2-x2)-10, x3]
c1mp1 = [x1+140,x2,x3+120]
c3mp4 = [w1+140,(z2-x2),x3+120]
c1mp2 = [y1-40,y2,y3+50]
c3mp3 = [z1-40,(z2-y2),y3+50]
c2mp2 = [y1-220, y2+100, y3+110]
c2mp3 = [z1-220, (z2-x2)-100, y3+110]
c1 = BEZIER(S1)([p2, c1mp2, c1mp1, p1])
bcurve1 = MAP(c1)(domain)
c2 = BEZIER(S2)([p3, c2mp3, c2mp2,  p2])
bcurve2 = MAP(c2)(domain)
c3 = BEZIER(S1)([p3, c3mp3, c3mp4, p4])
bcurve3 = MAP(c3)(domain)
c4 = BEZIER(S2)([p4, c4mp4, c4mp1, p1])
bcurve4 = MAP(c4)(domain)

# i manici della patch modificati per far combaciare l'approssimazione effettuata da COONSPATCH
# alle curve prese dal blueprint.
c4mp1 = [x1-110-60, x2+10+80, x3]
c4mp4 = [w1-110-60, (z2-x2)-10-80, x3]
c1mp1 = [x1+140+280,x2+40,x3+120+240]
c3mp4 = [w1+140+280,(z2-x2)-40,x3+120+240]
c1mp2 = [y1-80,y2,y3+100]
c3mp3 = [z1-80,(z2-y2),y3+100]

c2mp2 = [y1-220, y2+100, y3+110]
c2mp3 = [z1-220, (z2-x2)-100, y3+110]

c1 = BEZIER(S1)([p2, c1mp2, c1mp1, p1])
curve1 = MAP(c1)(domain)

c2 = BEZIER(S2)([p3, c2mp3, c2mp2,  p2])
curve2 = MAP(c2)(domain)

c3 = BEZIER(S1)([p3, c3mp3, c3mp4, p4])
curve3 = MAP(c3)(domain)

c4 = BEZIER(S2)([p4, c4mp4, c4mp1, p1])
curve4 = MAP(c4)(domain)

hoodPatch = COONSPATCH([c1,c3,c2,c4])
#in posizione sulle curve
#hood = T([2,3])([-500,-10])(S([1,3])([1/3.0,1/3.0])(MAP(hoodPatch)(domain)))

#in posizione nell'auto
hood = T([1,2,3])([80,-710,80])(
	S([1,2,3])([0.70,0.95,0.70])(
		S([1,3])([1/3.0,1/3.0])(MAP(hoodPatch)(domain))
		)
	)

#VIEW(STRUCT([
#	COLOR(RED)(curve1),
#	COLOR(GREEN)(curve2),
#	COLOR(BLUE)(curve3),
#	curve4,
#	COLOR(RED)(bcurve1),
#	COLOR(GREEN)(bcurve2),
#	COLOR(BLUE)(bcurve3),
#	bcurve4,
#	hood]))

########## End Cofano ##########

#completo con ruote
#VIEW(STRUCT ([car, FRwheel, FLwheel, RRwheel, RLwheel, steeringWheel, COLOR(RED)(wing), COLOR(RED)(hood)]));

#Con cofano
VIEW(STRUCT ([car, steeringWheel, COLOR(RED)(wing), COLOR(RED)(hood)]));
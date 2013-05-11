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
#con bezier fa pena.
#razza1 = BEZIER(S1)([[3.1, 2.5], [3.1, 5.5], [4.2, 4.2], [4.8, 4.6]])
#razza1 = MAP(razza1)(domain)
#razza2 = BEZIER(S1)([[2.65, 2.35], [3, 5.4], [1.7, 4.5], [1.2, 4.8]])
#razza2 = MAP(razza2)(domain)
#razza3 = BEZIER(S1)([[3.2, 5.2], [2.35, 5.4], [3.1, 4.8], [1.2, 5.1]])
#razza3 = MAP(razza3)(domain)
#razza4 = BEZIER(S1)([[2.8, 5.2], [3.5, 5.35], [3.1, 4.8], [4.7, 4.9]])
#razza4 = MAP(razza4)(domain)
#VIEW(STRUCT([razza1, razza2, razza3, razza4]))

#così invece non posso fare la superfice
#pointsRazze = [[310,705],[310,705],[310,705],[95,705],[95,705],[85,650],[85,650],[310,650],[310,650],[310,650]];
#profiloRazze = T([2])(-705)(SPLINE(CUBICUBSPLINE(domain))(pointsRazze));
#profiloYZf1 = STRUCT([ T([1])(620)(R([1,3])(PI)(profiloRazze)), profiloRazze ])

#purtroppo sono le 18... :)

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
VIEW(STRUCT ([car, FRwheel, FLwheel, RRwheel, RLwheel, steeringWheel]));

########## End Exercise 2 ##########

########## Exercise 5 ##########


domain = GRID([25,25])

Pu0 = [(0,0,0),(0,0,1),(1,0,1),(1,0,0)]
Pu1 = [(0,1,0),(0,1,1),(1,1,1),(1,1,0)]
P0v = [(0,0,0),(0,0,1),(0,1,1),(0,1,0)]
P1v = [(1,0,0),(0,0,1),(1,1,1),(1,1,0)]
Dom1D = INTERVALS(1)(24)

cu0 = MAP(BEZIER(S1)(Pu0))(Dom1D)
cu1 = MAP(BEZIER(S1)(Pu1))(Dom1D)
c0v = MAP(BEZIER(S1)(P0v))(Dom1D)
c1v = MAP(BEZIER(S1)(P1v))(Dom1D)

C0v = BEZIER(S1)([Pu0])
C1v = BEZIER(S1)([Pu1])

Cu0 = BEZIER(S1)([Pu0])
Cu1 = BEZIER(S1)([Pu1])
Cua = [[0,0,1],[0,0,2],[1,0,2],[1,0,1]]
Cub = [[0,1,1],[0,1,2],[1,1,2],[1,1,1]]
mapping = BEZIER(S2)([Cu0, Cua,  Cub, Cu1])

tettinoWIP = MAP(mapping)(domain)


Su0 = BEZIER(S1)([[0,0,0],[10,0,20],[5,0,20]])
Su1 = BEZIER(S1)([[0,10,0],[10,10,20],[5,0,20]])
S0v = BEZIER(S2)([[0,0,0],[0,0,3],[0,10,3],[0,10,0]])
S1v = BEZIER(S2)([[0,0,0],[0,0,3],[0,10,3],[0,10,0]])
VIEW(MAP(COONSPATCH([Su0,Su1,S0v,S1v]))(GRID([20,20])))

domain = GRID([10,10])

cu0 = BEZIER(S1)([[0,2,4],[1,2.5,4],[2,2.5,5],[3,2.5,4.5]])
curve01 = MAP(cu0)(domain)
cu1 = BEZIER(S1)([[0.69,5.2, 4.05], [0.9,5.2, 4.14], [1.72,5.2, 4.92], [3.19,5.2, 4.55]])
curve02 = MAP(cu1)(domain)
c0v = BEZIER(S2)([[3.19, 5.2,4.55], [1.67, 4.91,4.55], [1.99, 2.49,4.55], [3.22, 2.43,4.55]])
curve03 = MAP(c0v)(domain)
c1v = BEZIER(S2)([[0.69, 5.2,4.05], [0.17, 3.92,4.05], [0.6, 2.71,4.05], [0.66, 2.43,4.05]])
curve04 = MAP(c1v)(domain)
VIEW(STRUCT([curve01,curve02,curve03,curve04]))

#s= BEZIER(S2)([cu0,cu1,c0v,c1v])
surface = COONSPATCH([cu1,cu0,c1v,c0v])
surf = MAP(surface)(domain)
VIEW(COLOR(RED)(surf))

#senza ruote
#VIEW(STRUCT ([car, steeringWheel]));
#completa di ruote
#VIEW(STRUCT ([car, FRwheel, FLwheel, RRwheel, RLwheel, steeringWheel]));
 def translatePoints(values):
x = values[0]
y = values[1]
z = values[2]
def translatePoints0(points):
p = []
for a in points:
c = [0,0,0]
c[0] = a[0]+x
c[1] = a[1]+y
c[2] = a[2]+z
p.append(c)
return p
return translatePoints0

p0 = [[0,0,0],[0.5,0,0]]
v0 = BEZIER(S1)(p0)
p1 = translatePoints([0,6,2.5])([[0.5,0,0],[1,0,0]])
v1 = BEZIER(S1)(p1)
p2 = [[0,0,0],[0.2,2,0],[0.3,3.5,0],[0.5,6,2.5]]
v2 = BEZIER(S2)(p2)
p3 = translatePoints([0.5,0,0])(p2)
v3 = BEZIER(S2)(p3)

first = MAP(COONSPATCH([v0,v1,v2,v3]))(GRID([20,20]))

p4 = [[1,0,0],[1.5,0,0]]
v4 = BEZIER(S1)(p4)
p5 = translatePoints([0,6,2.5])([[0.8,0,0],[1.3,0,0]])
v5 = BEZIER(S1)(p5)
p6 = [[1,0,0],[1.1,2,0],[1,3.5,0],[0.8,6,2.5]]
v6 = BEZIER(S2)(p6)
p7 = translatePoints([0.5,0,0])(p6)
v7 = BEZIER(S2)(p7)

second = MAP(COONSPATCH([v4,v5,v6,v7]))(GRID([20,20]))

VIEW(STRUCT([
MAP(v0)(GRID([10,10])),
MAP(v1)(GRID([10,10])),
MAP(v2)(GRID([10,10])),
MAP(v3)(GRID([10,10])),
first, second]))
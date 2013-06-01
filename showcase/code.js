//Showcase - Code.js - Federico Violante - 281308

//****FUNZIONI DI SUPPORTO****//

//scala tutte le dims del valore scale
Sk = function(scale) {
	return function (object) {
		return object.clone().scale([0,1,2], [scale,scale,scale]);
	};
};

//colori in RGB da 1 a 255
COLOR255 = function(args){
	return COLOR([args[0]/255.0, args[1]/255.0, args[2]/255.0, args[3]]);
};

//sfera
var SPHERE = function (arg){
	var a = arg[0];
	var b = arg[1];
	var u = SIN(a) * COS(b);
	var v = SIN(a) * SIN(b);
	var w = COS(a);
	return [u,v,w];
};

//settori dei domini 
var sect = 36;
var framesect = 12;
var doorsect = 36;

//Colori
var BLACK = [0,0,0,1];

//****MODELLO****//

//Scena

universe = function(){
	var universeDom = DOMAIN([[0,PI],[0,2*PI]])([3,4]);
	var universe = Sk(10000)(MAP(SPHERE)(universeDom));
	return COLOR([0,0,0,1])(universe);
};
//DRAW(universe());

earth = function(){
	var earthDom = DOMAIN([[0,PI/2.0],[0,2*PI]])([72,172]);
	var earth = T([2])([-12000])(Sk(10000)(MAP(SPHERE)(earthDom)));
	return COLOR255([10,110,200,1])(earth);
};
//DRAW(earth());

//Bubbleship

tetrahedralCore = function(){
	var core_faceX = TRIANGLE_DOMAIN(1, [[1,0,0],[2,0,SQRT(2)],[0,0,SQRT(2)]]);
	var core_faceYL = TRIANGLE_DOMAIN(1, [[1,0,0],[1,SQRT(2),SQRT(2)],[2,0,SQRT(2)]]);
	var core_faceYR = TRIANGLE_DOMAIN(1, [[1,0,0],[1,SQRT(2),SQRT(2)],[0,0,SQRT(2)]]);
	var core_faceZ = TRIANGLE_DOMAIN(1, [[2,0,SQRT(2)],[1,SQRT(2),SQRT(2)],[0,0,SQRT(2)]]);
	var core = STRUCT([core_faceX, core_faceYL, core_faceYR, core_faceZ]);
	return COLOR([1,1,1,1])(core);
};
DRAW(tetrahedralCore());

cockpit = function(){

	//Glass
	var cockpitBubbleDom = DOMAIN([[0,3*PI/4.0],[0,2*PI]])([2*sect,sect]);
	var cockpitBubble = MAP(SPHERE)(cockpitBubbleDom);

	var cockpitDoorDom = DOMAIN([[3*PI/4.0,PI],[0,2*PI]])([doorsect,sect]);
	var cockpitDoor = T([0,1,2])([-0.3,0,-PI/4.5])(R([0,2])(-PI/4.0)(MAP(SPHERE)(cockpitDoorDom)));

	var cockpitGlass = COLOR255([160,210,255,0.5])(STRUCT([cockpitBubble, cockpitDoor]));

	//Frame
	var cockpitDoorFrameDom = DOMAIN([[3*PI/4.0,(3*PI+0.4)/4.0],[0,2*PI]])([framesect,sect]);
	var cockpitDoorFrame = T([0,1,2])([-0.3,0,-PI/4.5])(R([0,2])(-PI/4.0)(MAP(SPHERE)(cockpitDoorFrameDom)));

	var cockpitClosedDoorFrameDom = DOMAIN([[(PI-0.4)/4.0, PI/4.0],[0,2*PI]])([framesect,sect]);
	var cockpitClosedDoorFrame = MAP(SPHERE)(cockpitClosedDoorFrameDom);

	var cockpitFrames = COLOR([1,1,1,1])(STRUCT([cockpitDoorFrame, cockpitClosedDoorFrame]));

	var IncockpitDoorFrameDom = DOMAIN([[(3*PI-0.1)/4.0,(3*PI+0.5)/4.0],[0,2*PI]])([framesect,sect]);
	var IncockpitDoorFrame = T([0,1,2])([-0.3,0,-PI/4.5])(R([0,2])(-PI/4.0)(MAP(SPHERE)(IncockpitDoorFrameDom)));

	var IncockpitClosedDoorFrameDom = DOMAIN([[(PI-0.5)/4.0, (PI+0.1)/4.0],[0,2*PI]])([framesect,sect]);
	var IncockpitClosedDoorFrame = MAP(SPHERE)(IncockpitClosedDoorFrameDom);

	var IncockpitBackDom = DOMAIN([[3*PI/4,PI],[0,2*PI]])([doorsect,sect]);
	var IncockpitBack = R([0,2])(-PI/2.0)(MAP(SPHERE)(IncockpitBackDom));

	var IncockpitFloorDom = DOMAIN([[3*PI/4,PI],[0,2*PI]])([doorsect,sect]);
	var IncockpitFloor = R([1,2])(-PI/2.0)(MAP(SPHERE)(IncockpitFloorDom));

	var IncockpitUpDom = DOMAIN([[(PI-0.25)/2.0,(PI+0.25)/2.0],[PI/4,3*PI/4]])([framesect,sect]);
	var IncockpitUp = R([0,2])(-PI/2.0)(MAP(SPHERE)(IncockpitUpDom));

	var IncockpitUpBackDom = DOMAIN([[(PI-0.5)/2.0,(PI+0.5)/2.0],[0,PI]])([framesect,sect]);
	var IncockpitUpBack = R([0,1])(-PI/2.0)(MAP(SPHERE)(IncockpitUpBackDom));

	var IncockpitCircleUpDom = DOMAIN([[(PI-0.4),PI],[0,2*PI]])([framesect,sect]);
	var IncockpitCircleUp = R([1,2])(PI/2.0)(MAP(SPHERE)(IncockpitCircleUpDom));

	var IncockpitTop = STRUCT([IncockpitUp, IncockpitUpBack, IncockpitCircleUp]);

	var IncockpitFrames = COLOR(BLACK)(Sk(0.999)(STRUCT([IncockpitDoorFrame, IncockpitClosedDoorFrame, IncockpitBack, IncockpitFloor, IncockpitTop])));

	var allCockpitFrames = STRUCT([cockpitFrames, IncockpitFrames]);

	var cockpitObj = T([0,1,2])([1,-1,1])(R([0,2])(PI/2.0)(R([0,1])(PI/2.0)(STRUCT([cockpitGlass, allCockpitFrames]))));

	return cockpitObj;
};

DRAW(cockpit());

var points = [[0,0], [1,1], [2,0]];
var polypoint = POLYPOINT(points);
DRAW(polypoint);
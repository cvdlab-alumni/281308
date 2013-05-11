# Exercise 4 - Python
# Generate the 3D model of a steering wheel specifically designed for Formula and Sport cars 
# (look on the web for common shapes). Mount it the the 2.5D mock-up.


pointsRazze = [[310,705],[310,705],[310,705],[95,705],[95,705],[85,650],[85,650],[310,650],[310,650],[310,650]];
hprofiloYZf1 = T([2])(-705)(SPLINE(CUBICUBSPLINE(domain))(pointsRazze));
profiloYZf1 = STRUCT([ T([1])(620)(R([1,3])(PI)(hprofiloYZf1)), hprofiloYZf1 ])



steerTorus = TORUS([27.5,33])([30,30]);
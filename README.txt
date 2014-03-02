User Manual:

To launch the program, run routed.py, you will be presented with a text prompt, there are several commands:
	-add rt <routers>
		This command adds routers to the routing table, where <routers> is a comma separated list of (positive) integers and integer ranges. That is, routers can be 6,9,10-13,4,8 which would include routers rt4,rt6,rt8,rt9,rt10,rt11,rt12,rt13
	-del rt<routers>
		This command deletes routers from the routing table, where <routers> is a comma separated list of (positive) integers and integer ranges. That is, routers can be 6,9,10-13,4,8 which would include routers rt4,rt6,rt8,rt9,rt10,rt11,rt12,rt13.
	-add nt<networks>
		This command adds networks to the routing table, where <networks> is a comma separated list of (positive) integers and integer ranges. That is, networks can be 6,9,10-13,4,8 which would include networks rt4,rt6,rt8,rt9,rt10,rt11,rt12,rt13
	-del nt<networks>
		This command deletes networks from the routing table, where <networks> is a comma separated list of (positive) integers and integer ranges. That is, networks can be 6,9,10-13,4,8 which would include networks rt4,rt6,rt8,rt9,rt10,rt11,rt12,rt13.
	-con x y z
		This command connects node x and node y, where node x and y are existing nodes in the routing table (for example, x = rt8, y =rt15 would be valid values for x and y if they were previously added) and z is the cost of the connection. Note that these connections are one directional, “con rt1 rt2 5” is not the same as “con rt2 rt1 5”. Also, note that if a connection already exists between two nodes, this command will override any previous connection.
	-display
		This command prints out the routing table you are currently working on, for example, entering “add rt 1-2” and “add nt 7” and then entering “display” would generate
		Rt1 Rt2 Nt7
		Rt1 0 0 0
		Rt2 0 0 0
		Nt7 0 0 0
		This shows that there are no connections between any nodes, as you have not connected anything yet.
	-tree x
		This command computes the tree of shortest paths, with x as its root. In other words, it displays every node x 	can connect too, the path it took to get there, and the cost of the connection. For example, if you were to enter “add rt 1-3”, “add nt 7”, “con rt1 rt2 1” “con rt2 rt3 1” and then enter “tree rt1”, you would get
		0: rt1 : to get to rt1
		1: rt1, rt2: to get to rt2
		2: rt1, rt2, rt3: to get to rt3
		No path to nt7
	-quit
		This command exits the program.
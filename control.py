import addNode
import delNode
import conModule
import displayModule
import bellman


def start():
        command = "placeholder"

        while command != "quit":
                command = raw_input('---->')

                if command[:6] == "add rt":
                        addNode.add_rt(command[6:])
                elif command[:6] == "del rt":
                        delNode.del_rt(command[6:])
                elif command[:6] == "add nt":
                        addNode.add_nt(command[6:])
                elif command[:6] == "del nt":
                        delNode.del_nt(command[6:])
                elif command[:3] == "con":
                        conModule.con(command[4:])
                elif command[:7] == "display":
                        displayModule.display()
                elif command[:4] == "tree":
                        bellman.tree(command[5:])
                elif command == "quit":
                        print "killing the daemon"
                else:
                        print "Invalid input"

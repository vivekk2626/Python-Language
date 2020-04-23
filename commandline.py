import sys

print("\n*********** Application For Command Line Arguments***************");

print("\n Application name is : "+sys.argv[0]);

x=int(sys.argv[1]);
y=int(sys.argv[2]);

z=x+y;

print("\n Addition is {}".format(z));



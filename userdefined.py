
def add(a):
	print("\nAccept One Return One >:",a);
	return a+1;

add(1);


def Addsub(a):
	print("\nAccept one return Multiple >")
	return a+1,a-1;

add,sub=Addsub(6);	

print("\nAddition is :",add);
print("\nSubstraction is :",sub);


def fun(ino):
	print("\nInside Fun :" ,ino)
	return 1;

def another(ino):
	print("\nFunction inside another function call :");
	fun(ino);

another(1);	


def defineunderadcall():
	def inner():
		print("Inner function inside define :");

	inner();

defineunderadcall();		
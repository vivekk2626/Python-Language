import sys

def main():
	print("\nHello krishna");

	app=list();

	j=int(input('\nEnter want to pushed : '));

	isum=0;
	for i in range(j):

		x=int(input());
		isum=isum+(x);
		app.append(x);

	print("\nElemets in list are :");	
			
	for i in range(j):
		
		print(app[i]);

	print("\nSum of List is :{}".format(isum));

	print(len(app)); #gives the length

if __name__ == '__main__':
	

	print("\n *******Application For List Iteration ************");

	print("\n Application name is : "+sys.argv[0]);

	main()
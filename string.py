import sys

def main():
	app=list();

	print("Enter the number want to Enter :");
	x=int(input()); #make it into integer bcoz when we take the input from the console it is basically str.

	for i in range(x):
		x=input()
		app.append(x);

	i=0;
	j=len(app);
	j=j-1;

	while(i<j):
		temp=app[i];
		app[i]=app[j];
		app[j]=temp;
		i=i+1;
		j=j-1;

	print("\nAfter reversing the array");

	for i in app:
		print(i);		






if __name__ == '__main__':
	main()

	print("\n*********** Application For String ***************");

	print("\n Application name is : "+sys.argv[0]);
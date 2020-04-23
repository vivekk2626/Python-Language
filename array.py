import array as arr;

def main():
	a=arr.array('i',[]);


	x=int(input("\nEnter How many Want to Pushed :"));

	for i in range(x):
		x=int(input());
		a.append(x);

	print("\nValues of Array is :")	
	for i in range(len(a)):
		print(a[i]);		
	


if __name__ == '__main__':
	print("\n********Application For Array ************")
	main()
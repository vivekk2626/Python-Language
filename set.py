def main():
	s={'vivek','aai'};

	l=int(input("Enter The Number That You Want To Pushed :"));

	print(s);	
	
	for i in range(l):
		x=input();
		s.add(x)

	print(s);	

	#s.remove('vive');  #raises key error
	s.discard('vive'); # not raised 










if __name__ == '__main__':
	main()
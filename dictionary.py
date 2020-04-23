import sys

def main():
	key=[];
	value=[];
	lang={'language':'c++','ide':'eclipse','framework':'angular'};

	print("\nHow Many key And Value Want To Enter :");
	x=int(input());

	for i in range(x):
		k=input("\nEnter the key :");
		v=input("\nEnter the value :");

		key.append(k);
		value.append(v);
	
	data=dict(zip(key,value));
	list=['vivek','aai','tai','mai'];

	print("\nDictionary :")

	print("\nBefore Adding into Dictionary");
	print(data);
	
	data['4']=lang;  #assigning the dictionary to the  new key
	data['3']=list;

	print("\nAfter Adding into Dictionary");
	print(data);	

	print("\nDeleted The Records Into Dictionary");
	del data['1'];   #deleting the 1th recored from the dictionary
	print(data);
	
	print("\nPrinting the data Of record 3 of list")
	print(data['3'][2]);  ## printing the value of containing the key as 4 int that list print 2 item; 

	print("\nPrinting the data Of record 4 of Dictionary") 	
	print(data['4']['ide']);  #printing the value of dictionary.	



if __name__ == '__main__':
	print("\n********* Application for Dictionary Creation **********");
	main()
	



















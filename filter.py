
def add(a,b):
	return a+b;
app=list();

x=input("Enetr the number That u want to pushed :")

for i in range(int(x)):
	y=int(input());

	app.append(y);


print("\n ******** This is Lambda-Filter function **********")
add=list(filter(lambda no:(no%2==0),app))

print("List of Even number is :",add);

print("\n ******** This is Lambda-Map function **********");

map=list(map(lambda no1:no1+1,app));
print(map);

print("\n ******** This is Lambda-Reduce function **********");

question = ["snehalaya kahape hai?","snehalaya ke project manager kon hai?","snehalaya mai kitne student hai?","snehalaya ke sachiv kon hai?","snehalaya mai kitne staff hai?" ]
first_options = ["Ahmednagar","sanjay gujale",450,"vishnu ambekar",34]
second_options = ["pune","vaijnath lohar",240,"sachin dormule",29]
third_options = ["mumbai","sunil more",350,"nick",45]
forth_options = ["delhi","joes",300,"rajiv gujar",30]
five_options = ["parner","sunil pawar",340,"anil gawade",40]

all_option = ["first_option","second_option","third_option","first_option","five_option"]
ans_key = [0,1,2,4,3]

i = 0
while i < 5:
	print question [i]
	print first_options [i]
	print second_options [i]
	print third_options [i]
	print forth_options [i]
	print five_options [i]
	user_input =int(raw_input("enter your answer"))
	if ans_key [i] == user_input:
		print "your answer right hai"
	else:
		print "try again"	
	i = i + 1		

index = question.index("snehalaya ke project manager kon hai?")

Abhi ke liye iss list ko use kar ke code likh sakte ho:


question.pop(2)
print(question)


print(len(question))


question.append("snehalaya ke head kon hai?")
print(question)


first_options.append("anil gawde")
print (first_options)
second_options.append("girish kulkarni")
print(second_options)
third_options.append("ramesh yadav")
print(third_options)
forth_options.append("kishor kaware")
print(forth_options)
five_options.append("kiran kaware")
print(five_options)


option2 = [ ]
option2.append("vaijnath lohar")
print option2


if "vaijnath lohar" in third_options:
	print "hai"
else: 
	print "nahi hai"	

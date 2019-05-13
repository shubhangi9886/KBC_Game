question = ["navgurukul kaha pe hai","navgurukul mai kitne student hai","navgurukul ke co-fawnder kon hai","navgurukul ki facility incharg kon hai","navgurukul mai study konsi hoti hai"]
first_options = ["banglore",30,"Ganesh pawar","anuradha didi","ITI"]
second_options = ["delhi",56,"amar singh","mayuri","software"]
third_options = ["mumbai",53,"rushbh varma","anjali","electronic"]
forth_options = ["pune",49,"shivam","vandana pandey","networking"]
five_options = ["parner",78,"abhisek gupta","komal","software engineering"]

all_option = ["first_options","second_options","third_options","forth_options","five_options"]
ans_key = [0,1,2,3,4]

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
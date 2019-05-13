question_list = ["who is the snehalaya","How many student of snehalaya","who is the project manager of snehalaya","who is the secetary of snehalaya"]
first_option = ["amhednagar",300,"Anil gawade","Girish kulkarni"]
secound_option = ["pune",500,"sunil more","Bharat kulkarni"]
third_option = ["Baglore",450,"vaijnath lohar","vishnu ambekar"]
forth_option = ["mumbai",400,"amol gore","rajiv gujar"]
all_option = ["first_option","secound_option","third_option","forth_option"]
ans_key = [0,1,2,3] 
i = 0
while i < len(question_list):
    print question_list[i]
    print first_option[i]
    print secound_option[i]
    print third_option[i]
    print forth_option[i]
    user = input("Enter your answer")
    if ans_key[i] == user:
        print "your answer right"
    elif 5050 == user:
        print first_option[i]
        print secound_option[i]
        
                
        user_input = input("Enter your answer")
        if ans_key == user:
            print "right answer"
        else:
            print "wrong answer"
    if user == -1:
            print "game se bahar ho"              
    break
i = i + 1
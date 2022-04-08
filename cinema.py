#Making a list for the movies 
from cgitb import text


movies = ['1. Jujutsu Kaisen Zero', '2. One Piece Film Red', '3. Kimetsu no Yaiba Mugen Train']

#Greeting the customer
print('----------------------------------------')
print('Hello!!! Welcome to Enguun Anime Cinema!')
print('----------------------------------------')

#Ask for name and phone number
def booking():
    name = input('Please enter your name: ')
    phone_number = input('Please enter your phone number: ')
#The seats for each movie and sessions
    seats = (([], [], []), ([], [], []), ([], [], []))

    if phone_number.isnumeric() == True:
        #Letting customer choose movie
        print('Todays screenings are')
        for movie in movies:
            print(movie)

        choice = None
        
        while choice not in ('1', '2', '3'):
            choice = input('Please select a movie 1/2/3): ')

        match choice:
            case '1':
                choice = int(choice)-1
                print ('You chose', movies[choice])
            case '2':
                choice = int(choice)-1
                print ('You chose', movies[choice])
            case '3':
                choice = int(choice)-1
                print ('You chose', movies[choice])
            case _:
                choice = int(choice)-1
                print ('You chose', movies[choice])
        #Its time for session choices, morning, afternoon, and evening
        session_choice = ''
        session_list = ['1. morning', '2. afternoon', '3. evening']
        for session in session_list:
            print(session)

        while session_choice not in ('1', '2', '3', ):
            session_choice = input("Choose your session (1, 2, 3): ")

        match session_choice:
            case '1':
                session_choice = int(session_choice)-1
                print ('You have chosen', session_list[session_choice])
            case '2':
                session_choice = int(session_choice)-1
                print ('You have chosen', session_list[session_choice])
            case '3':
                session_choice = int(session_choice)-1
                print ('You have chosen', session_list[session_choice])
            case _:
                print ('Wrong choice.')

        #Booking the seats

        seats_text = ''
        print()
        print('Pick your seats')
        for seat in range(1, 6):
            if seat in seats[choice][session_choice]:
                seats_text = seats_text + ' X'
            else:
                seats_text = seats_text + f'{seat}'
        print (seats_text)
        
        seat_choice = None

        while seat_choice not in range(1, 11):
            try:
                seat_choice = int(input("Please choose the seat you want: "))
            except:
                #if they fail to enter a seat thats valid
                print("Please enter a valid movie code")
                continue
                
            if seat_choice not in range(1, 6) or seat_choice in seats[choice][session_choice]:
                print("Seat not available, choose a different seat")
                seat_choice = None
            else:
                seats[choice][session_choice].append(seat_choice)
                print(f"Seat {seat_choice} booked")

            #Confirming cinema booking
            print('You are', name, 'and your phone number is', phone_number, 'and you are watching', {movies[int(choice)-1]}, 'in the', {session_list[int(session_choice)-1]},'in seat number', {seat_choice})
    #if customer fails to enter any numerals to phone number question
    else:
        print('Please enter numbers.')

book_again = 'Yes'
while book_again=='Yes':
    #calling booking()
    booking()
    #asking if the info is correct
    confirmation = None
    while confirmation not in ('Yes', "No"):
        confirmation = input ('Is this what you want? Yes or No?: ')
        
    if confirmation == 'Yes':
        book_again = 'No'
        print ("Thank you kind customer for choosing Enguun Anime Cinema")
    else:
         book_again = None
         while book_again not in ('Yes', "No"):
            book_again = input ('Are you sure you want to book again? Yes of No: ')

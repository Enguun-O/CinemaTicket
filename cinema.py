#1. Making a list for the movies 
movies = ['1. Jujutsu Kaisen Zero', '2. One Piece Film Red', '3. Kimetsu no Yaiba Mugen Train']

#2. Greeting the customer
print('----------------------------------------')
print('Hello!!! Welcome to Enguun Anime Cinema!')
print('----------------------------------------')

#3. Ask for name and phone number
def booking():
    name = input('Please enter your name: ')
    phone_number = input('Please enter your phone number: ')
    if phone_number.isnumeric() == True:
        #4. Letting customer choose movie
        print('Todays screenings are')
        for movie in movies:
            print(movie)

        choice = None
        
        while choice not in ('1', '2', '3'):
            choice = input('Please select a movie 1/2/3): ')

            match choice:
                case '1':
                    print ('You chose', movies[int(choice)-1])
                case '2':
                    print ('You chose', movies[int(choice)-1])
                case '3':
                    print ('You chose', movies[int(choice)-1])
                case _:
                    print ('Invalid. Sorry') 
        #5. Its time for session choices
        session_choice = ''
        session_list = ['1. morning', '2. afternoon', '3. evening']
        for session in session_list:
            print(session)

        while session_choice not in ('1', '2', '3', ):
            session_choice = input("Choose your session (1, 2, 3): ")

            match session_choice:
                case '1':
                    print ('You have chosen', session_list[int(session_choice)-1])
                case '2':
                    print ('You have chosen', session_list[int(session_choice)-1])
                case '3':
                    print ('You have chosen', session_list[int(session_choice)-1])
                case _:
                    print ('Wrong choice.')
            
            #6. Confirmation
            print('You are', name, 'and your phone number is', phone_number, 'and you are watching', choice, 'in the', session_choice,)


    else:
        print('Please enter numbers.')

booking()   

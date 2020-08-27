import random

print('Welcome to Guessing Game');
print('You will be guessing numbers, if your guess is right, you win');
print('Choose a Level');
print('Enter below, easy or medium or hard')
level = input('Enter a Level: ');
if(level == 'easy'):
guess = 6
        print('You are in easy mode: Only 6 guesses available');
        for i in range(1,guess+1):
                guesses = int(input('Enter your guess: '));
                num = random.randint(1,10);
                print('You have', guess-i, 'guesses left');
                if(guesses == num):
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('You got it right!');
                else:
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('That was wrong');
        print('Game over!');
        
elif(level == 'medium'):
        guess = 4
        print('You are in medium mode: Only 4 guesses available');
        for i in range(1,guess+1):
                guesses = int(input('Enter your guess: '));
                num = random.randint(1,20);
                print('You have', guess-i, 'guesses left');
                if(guesses == num):
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('You got it right!');
                else:
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('That was wrong');
        print('Game over!');
        
else:
        guess = 3
        print('You are in hard mode: Only 3 guesses available');
        for i in range(1,guess+1):
                guesses = int(input('Enter your guess: '));
                num = random.randint(1,50);
                print('You have', guess-i, 'guesses left');
                if(guesses == num):
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('You got it right!');
                else:
                        print('Our number is', num);
                        print('Your number is', guesses);
                        print('That was wrong');
        print('Game over!');

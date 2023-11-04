import random 
from colorama import Fore 
import time 
import sys 
run_condition='True'
title='rock paper scissors'
color_txt=Fore.RED,Fore.GREEN,Fore.BLUE
for n in title:
  sys.stdout.flush()
  time.sleep(0.2)
  sys.stdout.write(f'\t{random.choice(color_txt)}{n.upper()}')
else:
  reset_to_default_color=Fore.RESET 
  print(f'{reset_to_default_color}')
  time.sleep(0.2)
  print(f'{1}:1 player,\n2:2 players\n')
  while bool(run_condition):
     play=str(input('1 player or 2 players? or q to exit program:'))
     if play=='1':
      time.sleep(0.2)
      rock='rock'
      paper='paper'
      scissors='scissors'
      options=['rock','paper','scissors']
      for n in options:
          if n==options[0]:
              print(f'{options[0][0]}:{n}')
          elif n==options[1]:
              print(f'{options[1][0]}:{n}')
          elif n==options[-1]:
              print(f'{options[-1][0]}:{n}')
      else:
          option_input=input('r,p or s:')
          time.sleep(0.2)
          computer_options=[options[0][0],options[1][0],options[-1][0]]
          random_option=random.choice(computer_options)
          computer_won_msg='The computer won!'
          player_won_msg='The player won!'
          tie_msg='Its a tie!'
          print('Computer generating random option.....')
          time.sleep(0.2)
          print(random_option)
          time.sleep(0.2)
          def win_condition():
            if play=='1':
             if random_option==computer_options[0]:
                print(f'The computer chose {rock}')
             elif random_option==computer_options[1]:
                print(f'The computer chose {paper}')
             elif random_option==computer_options[-1]:
                print(f'The computer chose {scissors}')
             if option_input==computer_options[0] and random_option==computer_options[0]:
              print(tie_msg)
             elif option_input==computer_options[0] and random_option==computer_options[1]:
              print(computer_won_msg)
             elif option_input==computer_options[0] and random_option==computer_options[-1]:
              print(player_won_msg)
             elif option_input==computer_options[1] and random_option==computer_options[0]:
              print(player_won_msg)
             elif option_input==computer_options[1] and random_option==computer_options[1]:
              print(tie_msg)
             elif option_input==computer_options[1] and random_option==computer_options[-1]:
              print(computer_won_msg)
             elif option_input==computer_options[-1] and random_option==computer_options[-1]:
              print(tie_msg)
             elif option_input==computer_options[-1] and random_option==computer_options[0]:
              print(computer_won_msg)
             elif option_input==computer_options[-1] and random_option==computer_options[1]:
              print(computer_won_msg)
              
      win_condition()
            #if user wants to exit program
     elif play=='q':
         break
     elif play=='2':
                 your_turn='You"re going first'
                 second_player_turn='Now it"s the second player"s turn'
                 print(your_turn)
                 time.sleep(0.2)
                 options=['rock','paper','scissors']
                 moves=[options[0][0],options[1][0],options[-1][0]]
                 def choice_input():
                     for n in moves:
                         if n==moves[0]:
                             print(f'rock:{n}')
                         elif n==moves[1]:
                             print(f'paper:{n}')
                         elif n==moves[2]:
                             print(f'scissors:{n}')
                     else:
                         global input_move_player_1
                         input_move_player_1=str(input('r or p or s:'))
                         if input_move_player_1:
                             global input_move_player_2 
                             print(second_player_turn)
                             time.sleep(0.2)
                             input_move_player_2=str(input('r or p or s:'))
                             
                 choice_input()
                 def win_condition_1():
                     player_one_won='player 1 won!'
                     player_two_won='player 2 won!'
                     tie_msg='It"s a tie'
                     if input_move_player_1==moves[0] and input_move_player_2==moves[0]:
                         print(f'Since you and the second player both chose {input_move_player_1} {tie_msg}')
                     elif input_move_player_1==moves[1] and input_move_player_2==moves[1]:
                         print(f'Since you and the second player both chose  {input_move_player_1} {tie_msg}')
                     elif input_move_player_1==moves[2] and input_move_player_2==moves[2]:
                         print(f'Since you and the second player both chose {input_move_player_1} {tie_msg}')
                     elif input_move_player_1==moves[0] and input_move_player_2==moves[1]:
                         print(f'Since paper beats rock  {player_two_won}')
                     elif input_move_player_1==moves[0] and input_move_player_2==moves[2]:
                         print(f'Since rock beats scissors{player_one_won}')
                     elif input_move_player_1==moves[1] and input_move_player_2==moves[2]:
                         print(f'Since scissors beats paper {player_two_won}')
                     elif input_move_player_1==moves[1] and input_move_player_2==moves[0]:
                         print(f'Since paper beats rock {player_one_won}')
                     elif input_move_player_1==moves[2] and input_move_player_2==moves[1]:
                         print(f'Since scissors beats paper {player_one_won}')
                     elif input_move_player_1==moves[2] and input_move_player_2==moves[0]:
                         print(f'Since rock beats scissors {player_two_won}')
                       
                 win_condition_1()
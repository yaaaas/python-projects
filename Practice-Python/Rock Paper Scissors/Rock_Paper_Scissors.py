while True:
  while True:
    play1 = input("Player 1, please choose Rock, Paper or Scissors: ")
    if play1 in ["Rock", "Paper", "Scissors"]:
      break;
    
  while True:
    play2 = input("Player 2, please choose Rock, Paper or Scissors: ")
    if play2 in ["Rock", "Paper", "Scissors"]:
      break;
    
  if play1 == play2:
    print("It's a draw!")
    
  if play1 == "Rock":
    if play2 == "Scissors":
      print("Player 1 Wins!")
    if play2 == "Paper":
      print("Player 2 win!")
  
  if play1 == "Paper":
    if play2 == "Scissors":
      print("Player 2 Wins!")
    if play2 == "Rock":
      print("Player 1 wins!")
      
  if play1 == "Scissors":
    if play2 == "Rock":
      print("Player 2 Wins!")
    if play2 == "Paper":
      print("Player 1 wins!")
  
  cont = input("Do you wish to continue?(Y/N)")
  if cont != "Y":
    break;

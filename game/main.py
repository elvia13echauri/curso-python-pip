import random

def chooseOpcions():
  options = ('piedra','papel','tijera')
  userOption = input('piedra, papel o tijera? ')
  userOption = userOption.lower()
  computerOption = random.choice(options)

  if not userOption in options:
    print('esa opcion no es valida')
    return None, None
  
  print('User option => ', userOption)
  print('Computer option =>' , computerOption)
  return userOption,computerOption

def checkRules(userOption,computerOption,winsUser,winsComputer):
  if userOption == computerOption:
    print('empate')
  elif userOption == 'piedra':
    if computerOption == 'tijera':
      print('piedra gana a tijera')
      print('User gano')
      winsUser += 1
    else:
      print('papel gana a piedra')
      print('computer gana')
      winsComputer += 1
  elif userOption == 'papel':
    if computerOption == 'piedra':
      print('papel gana a piedra')
      print('user gana')
      winsUser += 1
    else:
      print('tijera gana a papel')
      print('computer gana')
      winsComputer += 1
  elif userOption == 'tijera':
    if computerOption == 'papel':
      print('tijera gana a papel')
      print('user gana')
      winsUser += 1
    else:
      print('piedra gana a tijera')
      print('computer gana')
      winsComputer += 1
  return winsComputer,winsComputer

def runGame():
  round = 1
  band = True
  winsComputer = 0
  winsUser = 0
  while band == True:
    print('*' * 50)
    print('ROUND ', round)
    print('Computer: ',winsComputer)
    print('User: ',winsUser)
    round += 1
  
    userOption,computerOption = chooseOpcions()
    winsUser,winsComputer = checkRules(userOption,computerOption,winsUser,winsComputer)
    
    if winsComputer == 2:
      print('El ganador es COMPUTER')
      band = False
    elif winsUser == 2:
      print('El ganador es USER')
      band = False

runGame()

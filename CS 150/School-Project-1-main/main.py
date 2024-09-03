def choiceSelect():
  storageChoice = input('ENTER CHOICE OF STORAGE: ')
  gpuChoice = input('ENTER CHOICE OF GPU: ')
  ramChoice = input('ENTER CHOICE OF RAM: ')
  choices = (storageChoice, gpuChoice, ramChoice)
  return choices
  
def costCalculation(choices):
  if choices[0] == '1':
      storageCost = 59.99
  elif choices[0] == '2':
      storageCost = 100
  elif choices[0] == '3':
      storageCost = 119.99
  else:
    print('INVALID CHOICE. PLEASE TRY AGAIN.')
    exit()
  if choices[1] == '1':
      gpuCost = 499.99
  elif choices[1] == '2':
      gpuCost = 1499.99
  elif choices[1] == '3':
      gpuCost = 3499.99
  else:
    print('INVALID CHOICE. PLEASE TRY AGAIN.')
    exit()
  if choices[2] == '1':
      ramCost = 49.99
  elif choices[2] == '2':
      ramCost = 89.99
  elif choices[2] == '3':
      ramCost = 129.99
  else:
    print('INVALID CHOICE. PLEASE TRY AGAIN.')
    exit()
  totalCost = storageCost + gpuCost + ramCost
  totalCost = round(totalCost, 2)
  print('TOTAL COST: $', totalCost)
  
def display():
  print('COMPUTER BUILDER\n\n')
  print('TYPE IN THE CORRESPONDING NUMBER OF THE ITEM TO ADD TO CART.\n\nSTORAGE: \n1. 1TB SSD - $59.99\n2. 2TB SDD - $100\n3. 5TB SSD - $119.99\n\n')
  print('GPU: \n1. NVIDIA GeForce GTX 1080 - $499.99\n2. NVIDIA GeForce RTX 2080 - $1,499.99\n3. NVIDIA GeForce RTX 3090 - $3,499.99\n\n')
  print('RAM: \n1. 8GB DDR4 - $49.99\n2. 16GB DDR4 - $89.99\n3. 32GB DDR4 - $129.99\n\n')

def main():
  display()
  choices = choiceSelect()
  costCalculation(choices)
  
main()
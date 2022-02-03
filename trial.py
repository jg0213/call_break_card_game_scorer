def main(): #defines the area in indents that will be triggered with main()#
  print('hi')
  yn = input('Wanna loop back to the start? ')
  if yn == 'yes':
    main() #loops back to where we defined main#
    
main() #This starts the main loop, without this, main would just be defined but not run#
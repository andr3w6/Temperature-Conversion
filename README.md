# Temperature-Conversion
##  This is a program that will calculate temperatures in Celcius or Fahrenheit and display the boiling and freezing points of water towards the end of the program. This program ##was used as a test question in my Python class. 
                                              The top of the program has comments that do not affect the program. Comments are used to explain a program and how it functions when someone is examining the code. Multiline comments are within three sets of quotation marks at the beginning and end of the enclosed text. However, multiline comments are not the only type of comments. Comments that only affect a single line are started with a pound sign. These comments only last for the remainder of the line and are in red colored text             The variable named toContinue will be used to test a condition that will let the program know whether to move past the loop or to keep going. The variable is assigned a character string containing the letter y. String literals are enclosed in single or double quotation marks. The text for these is green which is the same as the multiline comments in terms of color. Many would assume that the single equal sign means that to continue equals y, but a single equal sign means it is assigned this character string. A traditional equal sign requires two equal signs. 
                                              A while loop executes a series of instructions as long as the condition is met. For this program, the while loop executes as long as the toContinue variable is not assigned the character string n. The symbol ! means not, therefore combined with a single equal sign it means toContinue is not n. A nested if statement is used in the while loop to reevaluate what toContinue is set to when the loop is ran multiple times. A variable temperature is then assigned an integer input by the user once prompted to enter a temperature value. That temperature is used by conversion variables that convert the temperature to the correct type. The conversion_f is used when a celcius value needs to be converted to fahrenheit, and conversion_c is used when converting the opposite fahrenheit to celcius. Be mindful of the various sets of parentheses when working with conversions because it can alter the answer if done incorrectly. This is especially important to programs that use fractions in multiplication like this program. We need to know which conversion variables to use so the user is asked to type a C or an F for the temperature. 
                                                                                                                                      An if statement decides which decision should be taken based on what input the user typed for the temperature type. This if statement is different as it tests more options in a somewhat different way than the first if statement. Depending on which statement is true, the program will out put a different message to the user. The elif line of the statement works like an if line as it tests a condition since the first condition was false. The else line is used to catch invalid input. Python allows you to prompt the user to enter a C or an F when neither were selected. This else line is able to execute since the single quotation marks with nothing inside them covers the infinite amount of incorrect possibilities with a simple equals statement. Print statements show the user a message. To improve readability, messages often contain an extra space at the end of the message regardless of it being an assignment statement or a print statement. However, a print statement does not retrieve a value like the temperature assignment statement. Inside the print statements, the green text that is inside quotation marks is displayed as it appears in the code. A comma separates the different strings and variables being displayed, but any space not within the quotation marks will not be displayed as blankspace when the user interacts with the program. The temperature and conversions will display their values instead of the words themselves like the strings. The last part of the loop asks the user to enter in a y or n to denote whether they want to continue or not. If a user selects y the loop restarts where users can test a many different temperatures. This is why there is an if statement at the beginning of the while loop. If a user selects n the loop ends and proceeds to the next part of the program. Selecting n ends the while loop since the condition of not n is no longer true. 
                                                                                                                                      The program then displays the Boiling and Freezing point of water to remind users using the program for science experiments because the scenario for using the program was for a class. Note that \n is inside the quotation marks, but is not displayed as \n. This is because \n is an example of an escape sequence that displays the print statement a line below the last line form the while loop. The strange looking text containing letters, numbers, and percent signs is not displayed as it appears on the program either. This text is called a format string specifying where the strings are justified. The percent sign is the format operator that is followed by the strings that will be formatted. The s denoted that a string is being formatted. The first statement has "%20s" which translates to right justify a string a field width of 20 Like other kinds of spacing, text format vastly improves the readability of what is being displayed where lines of text are lined up. The last line thanks the user for using this program. 

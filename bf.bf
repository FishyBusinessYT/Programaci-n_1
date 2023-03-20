#Store the phrase "Input a number:\n" in memory:

>>++++++++++[<+++++++>-]<+++            #"I" 73
>>+++++++++++[<++++++++++>-]            #"n" 110
>+++++++++++[<++++++++++>-]<++          #"p" 112
>>+++++++++++[<++++++++++>-]<+++++++    #"u" 117
>>+++++++++++[<++++++++++>-]<++++++     #"t" 116
>>+++[<++++++++++>-]<++                 #" " 32
>>++++++++++[<++++++++++>-]<---         #"a" 97
>>+++[<++++++++++>-]<++                 #" " 32
>>+++++++++++[<++++++++++>-]            #"n" 110
>+++++++++++[<++++++++++>-]<+++++++     #"u" 117
>>+++++++++++[<++++++++++>-]<-          #"m" 109
>>++++++++++[<++++++++++>-]<--          #"b" 98
>>++++++++++[<++++++++++>-]<+           #"e" 101
>>+++++++++++[<++++++++++>-]<++++       #"r" 114
>>++++++[<++++++++++>-]<--              #":" 58
>++++++++++                             "\n" 10

#Print everything and get both numbers:

[<]>[.>]                                #Print message
>>,>                                    #Get num
>++++[<++++++++++++>-]< [<->-] <<<<[<]  #Process input

>[.>]                                   #Print message
>>>,>                                   #Get num
>++++[<++++++++++++>-]< [<->-] <<<<<    #Process input

[[-]<]                                  #Delete message

>>+++++++[<++++++++++>-]<+++            #"I" 73
>>++++++++++[<+++++++++++>-]            #"n" 110
>++++++++++++++++[<+++++++>-]           #"p" 112
>+++++++++[<+++++++++++++>-]            #"u" 117
>++++++++[<+++++++++++++++>-]<----      #"t" 116
>>++++[<++++++++>-]                     #" " 32
>++++++++++[<+++++++++++>-]<+           #"o" 111
>>++++++++++++++++[<+++++++>-]          #"p" 112
>++++++++++[<++++++++++>-]<+            #"e" 101
>>++++++[<+++++++++++++++++++>-]        #"r" 114
>++++++++++[<++++++++++>-]<---          #"a" 97
>>++++++++[<+++++++++++++++>-]<----     #"t" 116
>>+++++++++++++++[<+++++++>-]           #"i" 105
>++++++++++[<+++++++++++>-]<+           #"o" 111
>>++++++++++[<+++++++++++>-]            #"n" 110
>++++++[<++++++++++>-]<--               #":" 58
>>++[<+++++>-]                          #"\n" 10

<[<]>[.>]                               #Print message
>>>>,>                                  #Get symbol
>++++[<++++++++++>-]< [<->-] <<<<<<     #Process input

[<]>[[-]>]                              #Delete message

#Take numbers to memory cell 1:

>>>                                     #Get to the right of the cell train

>>+++[<<++++++>>-]<                     #Create the step counter

[
    [<]>                                #Go to the first number of the train
    [[<+>-]>]                           #Move every number over one slot to the left
    <<<-                                #Go back to the step counter and remove 1
]


#Check operation:

>>+++                                   #Set the comparison value
>+                                      #Set the next cell to 1 (will land here if the values coincide)
<[<-<+>>-]                              #Go back to the comparison value and take 1 from both IV and CV until CV depletes
<[[-]>]>>                               #If IV isn't depleted (unequal value) we clear the cell and move forward thrice

[                                       #6  #If it's a plus symbol we enter this loop
    -<<<[-]                             #3  #Remove the input value
    <[<+>-]                             #2  #Add the values
    <[<+>->>>+<<<]<[>+<-]>>>>           #3  #Copy the result over to cell 3
    >>+++[<+++>-]>+<<                   #2  #If statement setup
    ?[]                  #4/5#If #2 is bigger than 9 we end up on #5
]

#Set up comparison values:


>+++++                                  #Minus
>++                                     #Times
>+++++++                                #"/"
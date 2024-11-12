# goit-cs-hw-01
Computer Systems and Their Fundamentals Home Work.
Assembler calculator Description:
    Data initialization:
        The program defines three variables: a, b and c:
        a = 5
        b = 3
        c = 2
        The variable resultMsg contains the string 'Result: $' which will be displayed before the result.
    The main logic of the program:
        The program uses the AL register to store intermediate results.
        First, the value of the variable b is loaded into the AL register.
        Then c is subtracted from this value.
        After that, the value of a is added to the result.
        Since we are working with numbers from 0 to 9, the result is converted to an ASCII character by adding the value 30h to the result.
    Output of the result:
        First, the message "Result: " is displayed.
        Then the result itself is displayed as an ASCII character.
        Completion of the program:

        The program terminates by calling the DOS function to exit.
        Program execution steps
        The program loads the values ​​of variables b, c and a.
        An arithmetic operation is performed: b - c + a.
        The result is converted into an ASCII character.
        The program displays the line "Result: " and the result itself.
            Completes execution.
    DOS functions used:
        Function 09h (int 21h): Print a line on the screen.
        Function 02h (int 21h): Display one character on the screen.
        Function 4Ch (int 21h): Program termination.
        Execution example:
        If you run the program, it will output:

        makefile
        Copy the code
        Result: 6
        where the calculation result (b - c + a) = (3 - 2 + 5) = 6.
    Program execution:
        Compile this code using an assembler such as TASM or MASM.
        Load the generated .COM file into a DOS environment or DOS emulator.
        Run the program and observe the result.
        Important points:
        The program works only in a DOS environment or in emulators that support calling DOS interrupts (for example, DOSBox).
        To work with larger numbers or other characters, you will need to change the way the result is converted to ASCII and adjust the output logic.

Interpreter Description: 
    Parser: 
        factor: compiles the numbers and expressions in the arms.
        term: summarizes the operations of multiplication and division. This method has higher priority and must be used before the method for processing addition/removal.
        expr: summarizes the operations added and published.
    Interpreter: 
        Shows all the basic operations: addition, subtraction, multiplication and division.
    Priorities: 
        Multiplication and division operations come first through their processing in the term method.
        The added value is added after the multiplication/division in the expr method.

How does the code work: 
    User introduce a mathematical expression.
    The lexer breaks the text into tokens.
    The parser build an abstract syntax tree (AST) with prioritized operations.
    The interpreter calculates the result using similar methods for the skin type of AST nodes.
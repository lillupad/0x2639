# 0x2639
an esolang or something idk

0x2639 is a stack-based esoteric programing language designed by lillupad (me), based on hexadecimal bytes

### commands
| command  | function |
| ------------- | ------------- |
| :: [comment] | marks [comment] as a comment  |
| 7075 [number]  | pushes [number] to the stack  |
| 706f | reads the top value off the stack |
| 7063 | reads the top value off the stack as a character, based on it's ascii value |
| 726d | pops the top value off the stack |
| 696e | takes user input as a number and pushes it to the stack |
| 6164 | pushes the sum of the top 2 numbers on the stack to the stack |
| 7375 | pushes the difference between the 2nd number on the stack and the top number on the stack to the stack |
| 6d75 | pushes the product of the top 2 numbers on the stack to the stack |
| 6469 | pushes the quotient of the 2nd number on the stack and the top number on the stack to the stack |

### example programs

#### hello world
<pre>
:: the most verbose hello world
7075 72
7063
7075 101
7063
7075 108
7063
7063
7075 111
7063
7075 44
7063
7075 32
7063
7075 87
7063
7075 111
7063
7075 114
7063
7075 108
7063
7075 100
7063
7075 33
7063
</pre>

### cat
<pre>
:: note - this only works with numbers
696e
706f
</pre>

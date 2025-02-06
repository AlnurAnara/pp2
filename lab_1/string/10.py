'''
Escape Characters
Code	Result	
\'	    Single Quote	

\\	    Backslash	



\n	    New Line换行	 txt = "Hello\nWorld!"
                         print(txt) # Hello
                                      World!

\r	    Carriage Return回车	   txt = "Hello\rWorld!"
                               print(txt) #Hello
                                           World!


\t	    Tab	                     txt = "Hello\tWorld!"
移动到下一组第四个空格的开始处      print(txt)  #Hello   World!

\b	    Backspace(回退一个字符）#This example erases one character (backspace):
                                txt = "Hello \bWorld!"
                                print(txt) # HelloWorld!

\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#output We are the so-called "Vikings" from the north.

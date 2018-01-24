#Create a window with required number of buttons

from tkinter import*
import math

root=Tk()
root.geometry("275x330")
root.title('Calculator')

display =None

class Calc():

    def __init__(self):

        self.current_value = 0
        self.operation_pending = True
        self.total_value =0
        self.new_num=True
        self.op = 0
        self.equal_operation =False
    
    
    def num_Button(self,num):

        temp1 = display.get()
        temp2 = str(num)        
        if self.new_num:

            self.current_value = temp2
            self.new_num = False
            
        else:

            self.current_value = temp1 + temp2
            
        self.display(self.current_value)          
            
                
        
    def op_Button(self,operator):
        
        self.op = operator
        if self.operation_pending:
            
            self.result(self.current_value)
            
        else:
            self.total_value =float(self.current_value)
            
            self.operation_pending =True           
            
        self.new_num =True




    
    def result(self, value):
        
        value = float(value)

        if (self.op == '+'):
            
            self.total_value = self.total_value + value
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '-'):
            
            self.total_value = self.total_value - value
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '*'):
            
            self.total_value = self.total_value * value
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '/'):
            if (value == 0):
                print("cannot be divided by zero")
            else:
                self.total_value = self.total_value / value
                print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))
            
        elif (self.op == 's'):
            
            self.total_value = math.sqrt(self.total_value)
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '!'):
            
            self.total_value = math.factorial(round(abs(value)))
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '^'):
            
            self.total_value = self.total_value ** value
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == 'e'):
            
            self.total_value = round(math.exp(self.total_value),3)
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '%'):
            
            self.total_value = (self.total_value)% (value)
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))
            

        elif (self.op == 'ln'):
            
            self.total_value = round(math.log(float(self.current_value),3))
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))
        
        elif (self.op == 'log'):
        
            self.total_value = round(math.log(float(self.current_value),10),3)
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))

        elif (self.op == '+/-'):
            self.current_value = -value
            self.display(self.current_value)
            self.total_value  = self.current_value
            self.operation_pending = False
            print("current value is  :%f, total value is  %f"%(float(self.current_value),self.total_value))
            
        self.current_value =self.total_value 
           

    def equal_Button(self):

        if self.equal_operation:
            temp = self.total_value
            
        else:
            temp = self.current_value
            self.equal_operation = False
            

        self.result(temp)
        self.display(str(self.total_value))
        self.operation_pending = False


    def ans_Button(self):

        self.total_value = self.current_value


    def clearall_Button(self):

        self.display(0)

    def clear_Button(self):
        
        display.delete(0,END)
    

    def display(self,value):
        
        display.delete(0,END)
        display.insert(0,value)
    


calc = Calc()    
    
#-------Creating Two frames -----------------
    #-----------------Frame1 ----------------
frame1 =Frame(root)
frame1.pack(side =TOP)
display = Entry(frame1,justify =RIGHT, width =50,  font ="Times 24 bold")
display.insert(0,"")
display.pack()
    #-------------- Frame2-------------------
frame2 = Frame(root)
frame2.pack()
Button(frame2,text = "7" ,width =8,  height=2, command = lambda :calc.num_Button(7)).grid(row = 4,column =0)
Button(frame2,text = "8" ,width =8,  height=2, command = lambda :calc.num_Button(8)).grid(row = 4,column =1)
Button(frame2,text = "9" ,width =8,  height=2, command = lambda :calc.num_Button(9)).grid(row = 4,column =2)
Button(frame2,text = "4" ,width =8,  height=2, command = lambda :calc.num_Button(4)).grid(row = 5,column =0)
Button(frame2,text = "5" ,width =8,  height=2, command = lambda :calc.num_Button(5)).grid(row = 5,column =1)
Button(frame2,text = "6" ,width =8,  height=2, command = lambda :calc.num_Button(6)).grid(row = 5,column =2)
Button(frame2,text = "1" ,width =8,  height=2, command = lambda :calc.num_Button(1)).grid(row = 6,column =0)
Button(frame2,text = "2" ,width =8,  height=2, command = lambda :calc.num_Button(2)).grid(row = 6,column =1)
Button(frame2,text = "3" ,width =8,  height=2, command = lambda :calc.num_Button(3)).grid(row = 6,column =2)
Button(frame2,text = "1/x" ,width =8,  height=2, command = lambda :calc.op_Button("1/x")).grid(row = 2,column =0)
Button(frame2,text = "ANS" ,width =8,  height=2, command = lambda :calc.ans_Button()).grid(row = 7,column =2)
Button(frame2,text = "log" ,width =8,  height=2, command = lambda :calc.op_Button("log")).grid(row = 2,column =2)
Button(frame2,text = "+/-" ,width =8,  height=2, command = lambda :calc.op_Button("+/-")).grid(row = 2,column =3)
Button(frame2,text = "0" ,width =8,  height=2, command = lambda :calc.num_Button(0)).grid(row = 7,column =1)
Button(frame2,text = "." ,width =8,  height=2, command = lambda :calc.num_Button('.')).grid(row = 7,column =0)
Button(frame2,text = "=" ,width =8,  height=2, command = lambda :calc.equal_Button()).grid(row = 7,column =3)
Button(frame2,text = "+" ,width =8,  height=2, command = lambda :calc.op_Button('+')).grid(row = 6,column =3)
Button(frame2,text = "-" ,width =8,  height=2, command = lambda :calc.op_Button('-')).grid(row = 5,column =3)
Button(frame2,text = "*" ,width =8,  height=2, command = lambda :calc.op_Button('*')).grid(row = 4,column =3)
Button(frame2,text = "/" ,width =8,  height=2, command = lambda :calc.op_Button('/')).grid(row = 3,column =3)
Button(frame2,text = "mod" ,width =8,  height=2, command = lambda :calc.op_Button('%')).grid(row = 2,column =1)
Button(frame2,text = "sqrt" ,width =8,  height=2, command = lambda :calc.op_Button('s')).grid(row = 3,column =0)
Button(frame2,text = "!" ,width =8,  height=2, command = lambda :calc.op_Button('!')).grid(row = 3,column =1)
Button(frame2,text = "e" ,width =8,  height=2, command = lambda :calc.op_Button('e')).grid(row = 3,column =2)
Button(frame2,text = "C" ,width =8,  height=2, command = lambda :calc.clear_Button()).grid(row = 1,column =3)
Button(frame2,text = "ln" ,width =8,  height=2, command = lambda :calc.op_Button('log')).grid(row = 1,column =0)
Button(frame2,text = "x^y" ,width =8,  height=2, command = lambda :calc.op_Button('^')).grid(row = 1,column =1)
Button(frame2,text = "AC" ,width =8,  height=2, command = lambda :calc.clearall_Button()).grid(row = 1,column =2)







root.mainloop()




from tkinter import *
from math import *

root=Tk()
root.title('Calculator')

x=StringVar()
op= ""
flag=0

def btnclick(n):
    global op
    global flag
    if(n=='**'):
        flag=1
        op = op + '^'
        x.set(op)
    elif(n=='√'):
        flag=2
        op = op +'√'
        x.set(op)
    elif(n=='!'):
        flag=3
        op=op+'!'
        x.set(op)
    elif(n=='1/'):
        if(op==''):
            op = op+str(n)
            x.set(op)
        else:
            op='ERROR'
            x.set(op)
            op=''
    elif(n=='.'):
        list1=list(op)
        if(n in list1):
            pass
        else:
            op = op +str(n)
            x.set(op)
    elif(n=='sin '):
        flag=4
        op=op+str(n)
        x.set(op)
    elif(n=='cos '):
        flag=5
        op=op+str(n)
        x.set(op)
    elif(n=='tan '):
        flag=6
        op=op+str(n)
        x.set(op)
    else:
        op = op + str(n)
        x.set(op)

def btnclr():
    global op
    op = ""
    x.set(" ")

def equal():
    global op
    global flag
    if(flag==1):
        op = op.replace('^','**')
        cal = str(eval(op))
        flag=0
    elif(flag==2):
        list1=list(op)
        op=''
        i=0
        while(list1[i]!='√'):
            if(list1[i]!='√' and list1[i+1]=='√'):
                op=op+list1[i]+'*'
            elif(list1[i]!='√'):
                op=op+list1[i]
            i=i+1
        i=i+1
        op1=''
        while(i<len(list1) and list1[i].isdigit()):
            op1=op1+list1[i]
            i=i+1
        s = str(sqrt(int(op1)))
        op=op+s
        while(i<len(list1)):
            op=op+list1[i]
            i=i+1
        cal=str(eval(op))
        flag=0
    elif(flag==3):
        list1=list(op)
        op=''
        op1=''
        i=0
        while(i<len(list1)):
            op=''
            while(list1[i]!='!' and list1[i].isdigit()):
                op=op+list1[i]
                i=i+1
            if(list1[i]=='!'):
                cal1=str(factorial(int(op)))
                i=i+1
                op=cal1
                while(i<len(list1)):
                    op=op+list1[i]
                    i=i+1
            else:
                op1=op
                op1=op1+list1[i]
                op=''
            op=op1+op
            i=i+1
        cal=str(eval(op))
        flag=0
    elif(flag==4):
        list1=op.split()
        cal = str(sin(int(list1[1])))
        flag=0
    elif(flag==5):
        list1=op.split()
        cal = str(cos(int(list1[1])))
        flag=0
    elif(flag==6):
        list1=op.split()
        cal = str(tan(int(list1[1])))
        flag=0
    else:
        try:
            cal = str(eval(op))
        except ZeroDivisionError:
           cal = "Can't divide by zero"

    x.set(cal)
    op=cal
    
def delete():
    global op
    n=len(op)
    op = op[0:n-1]
    x.set(op)

frametop=Frame(root,width=1600,height=50)
frametop.pack(side=TOP)

f1=Frame(root,width=800,height=700)
f1.pack(side=LEFT)

labelhead=Label(frametop,font=('arial',30,'bold'),text='CALCULATOR',fg='blue')
labelhead.grid(row=0,column=0)

t_disp = Entry(f1,font=('verdana',25,'bold'),textvariable = x,bd=30,bg='light blue',justify='right')
t_disp.grid(columnspan=5)

btnpow=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='^',fg='black',bg='light blue',command= lambda: btnclick('**'))
btnpow.grid(row=1,column=0)

btnsin=Button(f1,padx=22,pady=12,bd=8,font=('verdana',14),text='sin',fg='black',bg='light blue',command= lambda: btnclick('sin '))
btnsin.grid(row=1,column=1)

btncos=Button(f1,padx=22,pady=12,bd=8,font=('verdana',14),text='cos',fg='black',bg='light blue',command= lambda: btnclick('cos '))
btncos.grid(row=1,column=2)

btntan=Button(f1,padx=22,pady=12,bd=8,font=('verdana',14),text='tan',fg='black',bg='light blue',command= lambda: btnclick('tan '))
btntan.grid(row=1,column=3)

btndel=Button(f1,padx=22,pady=12,bd=8,font=('verdana',14),text='del',fg='black',bg='light blue',command= lambda: delete())
btndel.grid(row=1,column=4)

btnsqrt=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='√',fg='black',bg='light blue',command= lambda: btnclick('√'))
btnsqrt.grid(row=2,column=0)

btn7=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='7',fg='black',bg='light blue',command= lambda: btnclick(7))
btn7.grid(row=2,column=1)

btn8=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='8',fg='black',bg='light blue',command= lambda: btnclick(8))
btn8.grid(row=2,column=2)

btn9=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='9',fg='black',bg='light blue',command= lambda: btnclick(9))
btn9.grid(row=2,column=3)

btnadd=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='+',fg='black',bg='light blue',command= lambda: btnclick('+'))
btnadd.grid(row=2,column=4)

btnfact=Button(f1,padx=24,pady=12,bd=8,font=('verdana',18,'bold'),text='!',fg='black',bg='light blue',command= lambda: btnclick('!'))
btnfact.grid(row=3,column=0)

btn4=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='4',fg='black',bg='light blue',command= lambda: btnclick(4))
btn4.grid(row=3,column=1)

btn5=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='5',fg='black',bg='light blue',command= lambda: btnclick(5))
btn5.grid(row=3,column=2)

btn6=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='6',fg='black',bg='light blue',command= lambda: btnclick(6))
btn6.grid(row=3,column=3)

btnsub=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='-',fg='black',bg='light blue',command= lambda: btnclick('-'))
btnsub.grid(row=3,column=4)

btninv=Button(f1,padx=22,pady=14,bd=8,font=('verdana',13),text='1/x',fg='black',bg='light blue',command= lambda: btnclick('1/'))
btninv.grid(row=4,column=0)

btn1=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='1',fg='black',bg='light blue',command= lambda: btnclick(1))
btn1.grid(row=4,column=1)

btn2=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='2',fg='black',bg='light blue',command= lambda: btnclick(2))
btn2.grid(row=4,column=2)

btn3=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='3',fg='black',bg='light blue',command= lambda: btnclick(3))
btn3.grid(row=4,column=3)

btnmul=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='*',fg='black',bg='light blue',command= lambda: btnclick('*'))
btnmul.grid(row=4,column=4)

btndot=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='.',fg='black',bg='light blue',command= lambda: btnclick('.'))
btndot.grid(row=5,column=0)

btnc=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='C',fg='black',bg='light blue',command= lambda: btnclr())
btnc.grid(row=5,column=1)

btnzero=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='0',fg='black',bg='light blue',command= lambda: btnclick('0'))
btnzero.grid(row=5,column=2)

btnequal=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='=',fg='black',bg='light blue',command= lambda: equal())
btnequal.grid(row=5,column=3)

btndiv=Button(f1,padx=22,pady=12,bd=8,font=('verdana',18,'bold'),text='/',fg='black',bg='light blue',command= lambda: btnclick('/'))
btndiv.grid(row=5,column=4)



root.mainloop()

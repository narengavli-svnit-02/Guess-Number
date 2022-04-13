from tkinter import *
import random
import time
root=Tk()
root.title("Game")
root.geometry("800x500")
root.minsize(800,500)
root.maxsize(800,500)

# create function
def sub_btn():
    global user_input,x,output_label_val,won_sum,lose_sum,total_game_status,random_num
    if user_input.get()=="":
        output_label_val.set("Please enter a valid value")
        user_input.focus_set()

    else:
        usr_input = int(user_input.get())
        if usr_input==random_num:
            output_label_val.set("You are Won this game. Play again.")
            won_sum+=1
            x=6
            total_game_status.set(F"Total Win games : {won_sum}\t\t\t\t\tTotal Lose games : {lose_sum} ")
            random_num=random.randint(0,30)
        elif usr_input>random_num:
            x-=1
            output_label_val.set(F"Get Up you are near to win, Now you have only {x} chance remaining.\nEnter the value less then {usr_input}.")
        elif usr_input<random_num:
            x-=1
            output_label_val.set(F"Get Up you are near to win, Now you have only {x} chance remaining.\nEnter the value greter then {usr_input}.")
    if x==0:
            output_label_val.set("You are lose this game, Don't worry play again.")
            x=6
            lose_sum+=1
            total_game_status.set(F"Total Win games : {won_sum}\t\t\t\t\tTotal Lose games : {lose_sum} ")
            random_num=random.randint(0,30)

# Create Frame 
top_frame=Frame(root)
top_frame.pack(fill=BOTH,pady=5)
body_frame=Frame(root)
body_frame.pack(fill=BOTH,pady=5)
bottom_frame=Frame(root)
bottom_frame.pack(fill=BOTH,pady=5)

# Create Variable
output_label_val=IntVar()
output_label_val.set("Enter Value Between 0 to 30")
random_num=random.randint(0,30)
x=6
won_sum=0
lose_sum=0
total_game_status=IntVar()
total_game_status.set(F"Total Win games : {won_sum}\t\t\t\t\tTotal Lose games : {lose_sum} ")

# top_frame 
Label(top_frame,text="Guess Number",font=("Cambria 20 bold"),fg="blue").pack(padx=10,pady=5)

Label(top_frame,text="-------------------------------------------------------------------------------------------------------------------------------------",font=("Times 14 bold")).pack(anchor="nw")

Label(top_frame,textvariable=total_game_status,font=("Times 14 bold"),fg="green").pack(anchor="nw",padx=10,pady=2)

Label(top_frame,text="-------------------------------------------------------------------------------------------------------------------------------------",font=("Times 14 bold")).pack(anchor="nw")

output_label=Label(top_frame,textvariable=output_label_val,font=("Times 14 bold"))
output_label.pack(padx=10,pady=5)

# Body Frame
Label(body_frame,text="Enter number hear  >>",font=("Times 14 bold")).grid(row=0,column=0,pady=5,padx=10)
user_input=Entry(body_frame,font=("Times 14 bold"))
user_input.focus_set()
user_input.grid(row=0,column=1,pady=5)

# Bottom Frame 
submit_btn=Button(bottom_frame,text="submit",font=("Hacked 14 bold"),bg="blue",fg="white",padx=10,pady=2,command=sub_btn)
submit_btn.pack(pady=20)
Label(bottom_frame,text="Thank You for playing this game.",font=("Times 17 bold")).pack(side=BOTTOM,pady=50)

root.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from .bl import *

gender_values = {
                "Male" : "Male",
                "Female" : "Female",
                "Other" : "Other"
                }    

def add_course(main_form, course_grid):
    
    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()

    def add_btn_onclick():
        code = old_code_var.get().strip()
        title = old_title_var.get().strip()
        price = old_price_var.get().strip()
        time = old_time_var.get().strip()
        teacher = old_teacher_var.get().strip()

        status, output = save_course_bl(
            code=code,
            title=title,
            price=price,
            time=time,
            teacher=teacher
        )
        
        if status=="ERROR":
            if output.get("code"):
                old_code_var.set("")
                title_entry.focus() 

            if output.get("title"):
                old_title_var.set("")
                title_entry.focus()

            if output.get("price"):
                old_price_var.set("")
                price_entry.focus()

            if output.get("time"):
                old_time_var.set("")
                price_entry.focus()

            if output.get("teacher"):
                old_teacher_var.set("")
                price_entry.focus()

            messagebox.showerror("Error!", "\n".join(output.values()))

        elif status=="SUCCESS":
            old_code_var.set("")
            old_title_var.set("")
            old_price_var.set("")
            old_time_var.set("")
            old_teacher_var.set("")
            code_entry.focus()

            course_grid.insert("", 'end',  values =(code, title, price, time, teacher))
            messagebox.showinfo("Success", output)
            form.destroy()
            main_form.deiconify()

    form = Toplevel()

    #region form confug
    form.title("Add course")

    window_width = 1080
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    form.resizable(width=False,height=False)
    form.configure(bg="white")
    form.overrideredirect(True)
    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = LabelFrame(master=form, text="Contact info", height=80, bg="white")
    body.pack(fill=BOTH, expand=True, padx=20, pady=20)
    body.propagate(False)


    code_frame = Frame(master=body, height=40, bg="white")
    code_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    code_frame.propagate(False)

    title_frame = Frame(master=body, height=40, bg="white")
    title_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    title_frame.propagate(False)


    price_frame = Frame(master=body, height=40, bg="white")
    price_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    price_frame.propagate(False)

    time_frame = Frame(master=body, height=40, bg="white")
    time_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    time_frame.propagate(False)

    teacher_frame = Frame(master=body, height=40, bg="white")
    teacher_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    teacher_frame.propagate(False)
    
    
    #endregion

    #region form hedaer

    Label(
        master=header, 
        text=" Add Contact", 
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        compound=LEFT
    ).pack(side=LEFT, padx=20)
    #endregion

    #region old_code
    old_code_var = StringVar()
    Label(
        master=code_frame, 
        text="code :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    code_entry = Entry(
        master=code_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_code_var,
    )
    code_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_title
    old_title_var = StringVar()

    Label(
        master=title_frame, 
        text="Title :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    title_entry = Entry(
        master=title_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_title_var
    )
    title_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_price
    old_price_var = StringVar()

    Label(
        master=price_frame, 
        text="price :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    price_entry = Entry(
        master=price_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_price_var,
    )
    price_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_time
    old_time_var = StringVar()

    Label(
        master=time_frame, 
        text="time :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    time_entry = Entry(
        master=time_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_time_var,
    )
    time_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_teacher
    old_teacher_var = StringVar()

    Label(
        master=teacher_frame, 
        text="teacher :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    teacher_entry = Entry(
        master=teacher_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_teacher_var,
    )
    teacher_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region Button

    Button(
        master=footer,
        text="Add",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        command=add_btn_onclick
    ).pack(side=RIGHT, padx=20)

    Button(
        master=footer,
        text="Back",
        bg="#dc3545",
        fg="white",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=20)

    #endregion

    form.mainloop()

def edit_course(main_form, course_grid, old_code, old_title, old_price, old_time, old_teacher):
    
    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()

    def edit_btn_onclick():
        code = old_code_var.get().strip()
        title = old_title_var.get().strip()
        price = old_price_var.get().strip()
        time = old_time_var.get().strip()
        teacher = old_teacher_var.get().strip()

        status, output = edit_course_bl(
            code=code,
            title=title,
            price=price,
            time=time,
            teacher=teacher
        )
        
        if status=="ERROR":
        
            if output.get("title"):
                old_title_var.set("")
                title_entry.focus()

            if output.get("price"):
                old_price_var.set("")
                price_entry.focus()

            if output.get("time"):
                old_time_var.set("")
                price_entry.focus()

            if output.get("teacher"):
                old_teacher_var.set("")
                price_entry.focus()

            messagebox.showerror("Error!", "\n".join(output.values()))

        elif status=="SUCCESS":
            selected_id = course_grid.selection()
            course_grid.item(selected_id[0],  values =(code, title, price, time, teacher))
            messagebox.showinfo("Success", output)
            form.destroy()
            main_form.deiconify()

    form = Toplevel()

    #region form confug
    form.title("Edit course")

    window_width = 1080
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    form.resizable(width=False,height=False)
    form.configure(bg="white")
    form.overrideredirect(True)
    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = LabelFrame(master=form, text="Contact info", height=80, bg="white")
    body.pack(fill=BOTH, expand=True, padx=20, pady=20)
    body.propagate(False)


    code_frame = Frame(master=body, height=40, bg="white")
    code_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    code_frame.propagate(False)

    title_frame = Frame(master=body, height=40, bg="white")
    title_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    title_frame.propagate(False)


    price_frame = Frame(master=body, height=40, bg="white")
    price_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    price_frame.propagate(False)

    time_frame = Frame(master=body, height=40, bg="white")
    time_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    time_frame.propagate(False)

    teacher_frame = Frame(master=body, height=40, bg="white")
    teacher_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    teacher_frame.propagate(False)
    
    
    #endregion

    #region form hedaer

    Label(
        master=header, 
        text=" Edit Contact", 
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        compound=LEFT
    ).pack(side=LEFT, padx=20)
    #endregion

    #region old_code
    old_code_var = StringVar(value=old_code)
    Label(
        master=code_frame, 
        text="code :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    code_entry = Entry(
        master=code_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_code_var,
        state=DISABLED
    )
    code_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_title
    old_title_var = StringVar(value=old_title)

    Label(
        master=title_frame, 
        text="Title :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    title_entry = Entry(
        master=title_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_title_var
    )
    title_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_price
    old_price_var = StringVar(value=old_price)

    Label(
        master=price_frame, 
        text="price :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    price_entry = Entry(
        master=price_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_price_var,
    )
    price_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_time
    old_time_var = StringVar(value=old_time)

    Label(
        master=time_frame, 
        text="time :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    time_entry = Entry(
        master=time_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_time_var,
    )
    time_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_teacher
    old_teacher_var = StringVar(value=old_teacher)

    Label(
        master=teacher_frame, 
        text="teacher :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    teacher_entry = Entry(
        master=teacher_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_teacher_var,
    )
    teacher_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region Button

    Button(
        master=footer,
        text="Edit",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        command=edit_btn_onclick
    ).pack(side=RIGHT, padx=20)

    Button(
        master=footer,
        text="Back",
        bg="#dc3545",
        fg="white",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=20)

    #endregion

    form.mainloop()

def add_student(main_form, student_grid):
    
    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()

    def add_btn_onclick():
        name = old_name_var.get().strip()
        family = old_family_var.get().strip()
        gender = old_gender_var.get().strip()
        std_code = old_std_code_var.get().strip()
        age = old_age_var.get().strip()
        phone = old_phone_var.get().strip()

        status, output = save_student_bl(
            name=name,
            family=family,
            gender=gender,
            std_code=std_code,
            age=age,
            phone=phone
        )
        
        if status=="ERROR":
            if output.get("name"):
                old_name_var.set("")
                name_entry.focus() 

            if output.get("family"):
                old_family_var.set("")
                family_entry.focus()

            if output.get("gender"):
                old_gender_var.set("")

            if output.get("std_code"):
                old_std_code_var.set("")
                std_code_entry.focus()

            if output.get("age"):
                old_age_var.set("")
                age_entry.focus()

            if output.get("phone"):
                old_phone_var.set("")
                phone_entry.focus()

            messagebox.showerror("Error!", "\n".join(output.values()))

        elif status=="SUCCESS":
            old_name_var.set("")
            old_family_var.set("")
            old_gender_var.set("")
            old_std_code_var.set("")
            old_age_var.set("")
            old_phone_var.set("")
            name_entry.focus()

            student_grid.insert("", 'end',  values =(name, family, gender, std_code, age, phone))
            messagebox.showinfo("Success", output)
            form.destroy()
            main_form.deiconify()

    form = Toplevel()

    #region form confug
    form.title("Add course")

    window_width = 1080
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    form.resizable(width=False,height=False)
    form.configure(bg="white")
    form.overrideredirect(True)
    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = LabelFrame(master=form, text="Contact info", height=80, bg="white")
    body.pack(fill=BOTH, expand=True, padx=20, pady=20)
    body.propagate(False)


    name_frame = Frame(master=body, height=40, bg="white")
    name_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    name_frame.propagate(False)

    family_frame = Frame(master=body, height=40, bg="white")
    family_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    family_frame.propagate(False)


    gender_frame = Frame(master=body, height=40, bg="white")
    gender_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    gender_frame.propagate(False)

    std_code_frame = Frame(master=body, height=40, bg="white")
    std_code_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    std_code_frame.propagate(False)

    age_frame = Frame(master=body, height=40, bg="white")
    age_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    age_frame.propagate(False)

    phone_frame = Frame(master=body, height=40, bg="white")
    phone_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    phone_frame.propagate(False)
    
    
    #endregion

    #region form hedaer

    Label(
        master=header, 
        text=" Add student", 
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        compound=LEFT
    ).pack(side=LEFT, padx=20)
    #endregion

    #region old_name
    old_name_var = StringVar()
    Label(
        master=name_frame, 
        text="Name :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    name_entry = Entry(
        master=name_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_name_var,
    )
    name_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_family
    old_family_var = StringVar()

    Label(
        master=family_frame, 
        text="Family :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    family_entry = Entry(
        master=family_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_family_var
    )
    family_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_gender
    old_gender_var = StringVar()
    for text, values in gender_values.items():
        Radiobutton(
        master=gender_frame, 
        text=values, 
        variable=old_gender_var,
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W,
        value=text
        ).pack(side=LEFT, fill=Y)


    #endregion

    #region old_std_code
    old_std_code_var = StringVar()

    Label(
        master=std_code_frame, 
        text="Student code :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    std_code_entry = Entry(
        master=std_code_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_std_code_var,
    )
    std_code_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_age
    old_age_var = StringVar()

    Label(
        master=age_frame, 
        text="Age :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    age_entry = Entry(
        master=age_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_age_var,
    )
    age_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_phone
    old_phone_var = StringVar()

    Label(
        master=phone_frame, 
        text="Phone :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    phone_entry = Entry(
        master=phone_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_phone_var,
    )
    phone_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region Button

    Button(
        master=footer,
        text="Add",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        command=add_btn_onclick
    ).pack(side=RIGHT, padx=20)

    Button(
        master=footer,
        text="Back",
        bg="#dc3545",
        fg="white",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=20)

    #endregion

    form.mainloop()

def edit_student(main_form, student_grid, old_name, old_family, old_gender, old_std_code, old_age, old_phone):
    
    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()

    def edit_btn_on_click():
        name = old_name_var.get().strip()
        family = old_family_var.get().strip()
        gender = old_gender_var.get().strip()
        std_code = old_std_code_var.get().strip()
        age = old_age_var.get().strip()
        phone = old_phone_var.get().strip()

        status, output = edit_student_bl(
            name=name,
            family=family,
            gender=gender,
            std_code=std_code,
            age=age,
            phone=phone
        )
        
        if status=="ERROR":
        
            if output.get("name"):
                old_name_var.set("")
                name_entry.focus()

            if output.get("family"):
                old_family_var.set("")
                family_entry.focus()

            if output.get("gender"):
                old_gender_var.set("")

            if output.get("age"):
                old_age_var.set("")
                age_entry.focus()

            if output.get("phone"):
                old_phone_var.set("")
                phone_entry.focus()

            messagebox.showerror("Error!", "\n".join(output.values()))

        elif status=="SUCCESS":
            selected_id = student_grid.selection()
            student_grid.item(selected_id[0],  values =(name, family, gender, std_code, age, phone))
            messagebox.showinfo("Success", output)
            form.destroy()
            main_form.deiconify()

    form = Toplevel()

    #region form confug
    form.title("Edit student")

    window_width = 1080
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    form.resizable(width=False,height=False)
    form.configure(bg="white")
    form.overrideredirect(True)
    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = LabelFrame(master=form, text="Contact info", height=80, bg="white")
    body.pack(fill=BOTH, expand=True, padx=20, pady=20)
    body.propagate(False)


    name_frame = Frame(master=body, height=40, bg="white")
    name_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    name_frame.propagate(False)

    family_frame = Frame(master=body, height=40, bg="white")
    family_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    family_frame.propagate(False)


    gender_frame = Frame(master=body, height=40, bg="white")
    gender_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    gender_frame.propagate(False)

    std_code_frame = Frame(master=body, height=40, bg="white")
    std_code_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    std_code_frame.propagate(False)

    age_frame = Frame(master=body, height=40, bg="white")
    age_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    age_frame.propagate(False)

    phone_frame = Frame(master=body, height=40, bg="white")
    phone_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    phone_frame.propagate(False)
    
    
    #endregion

    #region form hedaer

    Label(
        master=header, 
        text=" Edit Contact", 
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        compound=LEFT
    ).pack(side=LEFT, padx=20)
    #endregion

    #region old_name
    old_name_var = StringVar(value=old_name)
    Label(
        master=name_frame, 
        text="Name :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    name_entry = Entry(
        master=name_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_name_var,
    )
    name_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_family
    old_family_var = StringVar(value=old_family)

    Label(
        master=family_frame, 
        text="Family :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    family_entry = Entry(
        master=family_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_family_var
    )
    family_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_gender
    
    
    old_gender_var = StringVar(value=old_gender)
    for text, values in gender_values.items():
        Radiobutton(
        master=gender_frame, 
        text=values, 
        variable=old_gender_var,
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W,
        value=text
        ).pack(side=LEFT, fill=Y)

    
    #endregion

    #region old_std_code
    old_std_code_var = StringVar(value=old_std_code)

    Label(
        master=std_code_frame, 
        text="Student code :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    std_code_entry = Entry(
        master=std_code_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_std_code_var,
        state=DISABLED
    )
    std_code_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_age
    old_age_var = StringVar(value=old_age)

    Label(
        master=age_frame, 
        text="Age :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    age_entry = Entry(
        master=age_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_age_var,
    )
    age_entry.pack(fill=BOTH, expand=TRUE)

    #endregion

    #region old_phone
    old_phone_var = StringVar(value=old_phone)

    Label(
        master=phone_frame, 
        text="Phone :", 
        bg="white",
        fg="#06172a", 
        font=("tahoma", 9, "normal"),
        width=10,
        anchor=W
    ).pack(side=LEFT)

    phone_entry = Entry(
        master=phone_frame,
        font=("tahoma", 12, "normal"),
        bg="#f5f5f5",
        bd=1,
        borderwidth=15, 
        relief=FLAT,
        textvariable=old_phone_var,
    )
    phone_entry.pack(fill=BOTH, expand=TRUE)

    #endregion
  
    #region Button

    Button(
        master=footer,
        text="Edit",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        command=edit_btn_on_click
    ).pack(side=RIGHT, padx=20)

    Button(
        master=footer,
        text="Back",
        bg="#dc3545",
        fg="white",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=20)

    #endregion

    form.mainloop()

def show_course(main_form):
    
    def delete_btn_on_click():
        selected_id = course_grid.selection()

        if not selected_id:
            messagebox.showerror("Error", "select error")
        else:
            code, title, price, time, teacher = course_grid.item(selected_id[0], "values")


            answer = messagebox.askyesno(title='confirmation',
                    message=f'Do you want to delete {teacher} class with the price of {price} and the time of {time}, code : {code} ?')
            
            if answer:
                status, output = remove_course_bl(code=code)
                    
                if status=="ERROR":
                    messagebox.showerror("Error!!!", "\n".join(output.values()))

                elif status=="SUCCESS":
                    course_grid.delete(selected_id[0])
                    messagebox.showinfo("Success!!!", "Success message")

    def add_btn_on_click():
        form.withdraw()
        add_course(form, course_grid)

    def edit_btn_on_click():
        selected_id = course_grid.selection()

        if not selected_id:
            messagebox.showerror("Error", "select error")
        
        else:
            form.withdraw()
            old_code, old_title, old_price, old_time, old_teacher = course_grid.item(selected_id[0], "values")
            edit_course(form, course_grid, old_code, old_title, old_price, old_time, old_teacher)

    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()
 
    def form_load():
        status, output = read_courses_bl()
                
        if status=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output.values()))
            return []

        elif status=="SUCCESS":
            return output
    
    course_data = form_load()

    form = Toplevel()

    #region form confug
    form.title("course management")

    window_width = 600
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    form.overrideredirect(True)

    form.configure(bg="white")
    

    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body_course = LabelFrame(master=form, height=80, bg="white")
    body_course.pack(fill=BOTH, expand=True, padx=20, pady=20, side=LEFT)
    body_course.propagate(False)
   
    #endregion

    #region form header
    course_image = PhotoImage(file=r"images/course.png")

    Label(
        master=header,
        text="courses",
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        image=course_image,
        compound=LEFT
        ).pack(side=LEFT,padx=10)
    #endregion

    #region scrollbar
    grid_scrollbar_course= ttk.Scrollbar(master=body_course, orient=VERTICAL)
    grid_scrollbar_course.pack(side=RIGHT,fill=Y, pady=20, padx=(0,20))

    #endregion

    #region grid

    columns = ('code', 'title', 'price', 'time', 'teacher')  
    course_grid = ttk.Treeview(master=body_course, columns = columns, show = 'headings', selectmode=BROWSE)  
    col_width = course_grid.winfo_width() 

    course_grid.column("code", anchor=CENTER, width=col_width)
    course_grid.column("title", anchor=CENTER, width=col_width)
    course_grid.column("price", anchor=CENTER, width=col_width)
    course_grid.column("time", anchor=CENTER, width=col_width)
    course_grid.column("teacher", anchor=CENTER, width=col_width)


    course_grid.heading("code", text="code", anchor=CENTER)
    course_grid.heading("title", text="title", anchor=CENTER)
    course_grid.heading("price", text="price", anchor=CENTER)
    course_grid.heading("time", text="time", anchor=CENTER)
    course_grid.heading("teacher", text="teacher", anchor=CENTER)



    for course in course_data:
        course_grid.insert("", 'end',  values =(course["code"], course["title"], course["price"], course["time"], course["teacher"]))


    course_grid.pack(fill=BOTH, expand=True,pady=20,padx=(20,5))
    course_grid.configure(yscrollcommand=grid_scrollbar_course.set)
    grid_scrollbar_course["command"]=course_grid.yview

    #endregion

    #region button

    back_image = PhotoImage(file=r"images/return.png")
    
    Button(
        master=footer,
        text="Back",
        bg="#6c757d",
        fg="white",
        font=("tahoma", 10, "bold"),
        image=back_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#5c636a",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=10)

    delete_image = PhotoImage(file=r"images/delete.png")

    Button(
        master=footer,
        text="Delete",
        fg="black",
        bg="#dc3545",
        font=("tahoma", 10, "bold"),
        image=delete_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="black",
        command=delete_btn_on_click
    ).pack(side=RIGHT, padx=(0,10))

    edit_image = PhotoImage(file=r"images/edit.png")

    Button(
        master=footer,
        text="Edit",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        image=edit_image,
        compound=LEFT,
        padx=7, pady=7,
        command=edit_btn_on_click
    ).pack(side=RIGHT, padx=(0,10))

    add_image = PhotoImage(file=r"images/add.png")

    Button(
        master=footer,
        text="Add",
        bg="#00c853",
        fg="Black",
        font=("tahoma", 10, "bold"),
        image=add_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#14872f",
        activeforeground="Black",
        command=add_btn_on_click

    ).pack(side=RIGHT, padx=10)

    #endregion

    form.mainloop()

def show_student(main_form):

    def delete_btn_on_click():
        selected_id = student_grid.selection()

        if not selected_id:
            messagebox.showerror("Error", "select error")
        else:
            name, family, gender, std_code, age, phone = student_grid.item(selected_id[0], "values")


            answer = messagebox.askyesno(title='confirmation',
                    message=f'Do you want to delete {name, family, gender} with the student code of {std_code} and the age of {age} ?')
            
            if answer:
                status, output = remove_student_bl(std_code=std_code)
                    
                if status=="ERROR":
                    messagebox.showerror("Error!!!", "\n".join(output.values()))

                elif status=="SUCCESS":
                    student_grid.delete(selected_id[0])
                    messagebox.showinfo("Success!!!", "Success message")

    def add_btn_on_click():
        form.withdraw()
        add_student(form, student_grid)

    def edit_btn_on_click():
        selected_id = student_grid.selection()

        if not selected_id:
            messagebox.showerror("Error", "select error")
        
        else:
            form.withdraw()
            old_name, old_family, old_gender, old_std_code, old_age, old_phone = student_grid.item(selected_id[0], "values")
            edit_student(form, student_grid, old_name, old_family, old_gender, old_std_code, old_age, old_phone)

    def back_btn_onclick():
        form.destroy()
        main_form.deiconify()
 
    def form_load():
        status, output = read_students_bl()
                
        if status=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output.values()))
            return []

        elif status=="SUCCESS":
            return output
    
    students_data = form_load()

    form = Toplevel()
    
    #region form confug
    form.title("student management")

    window_width = 600
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    form.overrideredirect(True)

    form.configure(bg="white")

    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body_student = LabelFrame(master=form, height=80, bg="white")
    body_student.pack(fill=BOTH, expand=True, padx=20, pady=20, side=LEFT)
    body_student.propagate(False)
   
    #endregion

    #region form header
    student_image = PhotoImage(file=r"images/student.png")
    
    Label(
        master=header,
        text="students",
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        image=student_image,
        compound=LEFT
        ).pack(side=LEFT,padx=10)
    #endregion

    #region scrollbar
    grid_scrollbar_course= ttk.Scrollbar(master=body_student, orient=VERTICAL)
    grid_scrollbar_course.pack(side=RIGHT,fill=Y, pady=20, padx=(0,20))

    #endregion

    #region grid

    columns = ('Name', 'Family', 'Gender', 'Student code', 'Age', 'Phone')  
    student_grid = ttk.Treeview(master=body_student, columns = columns, show = 'headings', selectmode=BROWSE)  
    col_width = student_grid.winfo_width() 

    student_grid.column("Name", anchor=CENTER, width=col_width)
    student_grid.column("Family", anchor=CENTER, width=col_width)
    student_grid.column("Gender", anchor=CENTER, width=col_width)
    student_grid.column("Student code", anchor=CENTER, width=col_width)
    student_grid.column("Age", anchor=CENTER, width=col_width)
    student_grid.column("Phone", anchor=CENTER, width=col_width)



    student_grid.heading("Name", text="Name", anchor=CENTER)
    student_grid.heading("Family", text="Family", anchor=CENTER)
    student_grid.heading("Gender", text="Gender", anchor=CENTER)
    student_grid.heading("Student code", text="Student code", anchor=CENTER)
    student_grid.heading("Age", text="Age", anchor=CENTER)
    student_grid.heading("Phone", text="Phone", anchor=CENTER)



    for student in students_data:
        student_grid.insert("", 'end',  values =(student["name"], student["family"], student["gender"], student["std_code"], student["age"], student["phone"]))


    student_grid.pack(fill=BOTH, expand=True,pady=20,padx=(20,5))
    student_grid.configure(yscrollcommand=grid_scrollbar_course.set)
    grid_scrollbar_course["command"]=student_grid.yview

    #endregion

    #region button

    back_image = PhotoImage(file=r"images/return.png")

    Button(
        master=footer,
        text="Back",
        bg="#6c757d",
        fg="white",
        font=("tahoma", 10, "bold"),
        image=back_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#5c636a",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=10)

    delete_image = PhotoImage(file=r"images/delete.png")

    Button(
        master=footer,
        text="Delete",
        fg="black",
        bg="#dc3545",
        font=("tahoma", 10, "bold"),
        image=delete_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#bb2d3b",
        activeforeground="black",
        command=delete_btn_on_click
    ).pack(side=RIGHT, padx=(0,10))

    edit_image = PhotoImage(file=r"images/edit.png")

    Button(
        master=footer,
        text="Edit",
        bg="#ffc107",
        fg="black",
        activebackground="#ffca2c",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        image=edit_image,
        compound=LEFT,
        padx=7, pady=7,
        command=edit_btn_on_click
    ).pack(side=RIGHT, padx=(0,10))

    add_image = PhotoImage(file=r"images/add.png")

    Button(
        master=footer,
        text="Add",
        bg="#00c853",
        fg="black",
        font=("tahoma", 10, "bold"),
        image=add_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#14872f",
        activeforeground="black",
        command=add_btn_on_click
    ).pack(side=RIGHT, padx=10)

    #endregion

    form.mainloop()

def show_student_cource(old_form): 

    def back_btn_onclick():
        form.destroy()
        old_form.destroy()
        main_form()

    def form_load_std():
        status_std, output_std = read_students_bl()
        if status_std=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output_std.values()))
            return []

        elif status_std=="SUCCESS":
            return output_std
        
    def form_load_course():
        status_cource, output_course = read_courses_bl()
        if status_cource=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output_course.values()))
            return []

        elif status_cource=="SUCCESS":
            return output_course

    def Assign_std_on_click():
        selected_id_std = student_grid.selection()
        selected_id_course = course_grid.selection()

        if not selected_id_course or not selected_id_std:
            messagebox.showerror("EEROR", "select error")
        
        status, output = assign_student_bl(student_grid=student_grid, course_grid=course_grid, selected_id_course=selected_id_course, selected_id_std=selected_id_std)

        if status=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output.values()))

        elif status=="SUCCESS":
                messagebox.showinfo("Success!!!", "Success message")

    cource_data = form_load_course()
    std_data = form_load_std()

    form = Toplevel()

    #region form confug
    form.title("Course Assignment")

    window_width = 1080
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    form.overrideredirect(True)

    form.configure(bg="white")

    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body_std = LabelFrame(master=form, height=80, bg="white")
    body_std.pack(fill=BOTH, expand=True, padx=20, pady=20, side=LEFT)
    body_std.propagate(False)

    body_course = LabelFrame(master=form, height=80, bg="white")
    body_course.pack(fill=BOTH, expand=True, padx=20, pady=20, side=RIGHT)
    body_course.propagate(False)
   
    #endregion

    #region form header
    assign_image = PhotoImage(file=r"images/assign.png")
    
    Label(
        master=header,
        text="Course Assignment",
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        image=assign_image,
        compound=LEFT
        ).pack(side=LEFT,padx=10)
    #endregion

    #region scrollbar
    grid_scrollbar_course= ttk.Scrollbar(master=body_course, orient=VERTICAL)
    grid_scrollbar_course.pack(side=RIGHT,fill=Y, pady=20, padx=(0,20))

    grid_scrollbar_std= ttk.Scrollbar(master=body_std, orient=VERTICAL)
    grid_scrollbar_std.pack(side=RIGHT,fill=Y, pady=20, padx=(0,20))

    #endregion

    #region grid

    columns = ('code', 'title', 'price', 'time', 'teacher')  
    course_grid = ttk.Treeview(master=body_course, columns = columns, show = 'headings', selectmode=EXTENDED)  
    col_width_course = course_grid.winfo_width() 

    course_grid.column("code", anchor=CENTER, width=col_width_course)
    course_grid.column("title", anchor=CENTER, width=col_width_course)
    course_grid.column("price", anchor=CENTER, width=col_width_course)
    course_grid.column("time", anchor=CENTER, width=col_width_course)
    course_grid.column("teacher", anchor=CENTER, width=col_width_course)

    course_grid.heading("code", text="code", anchor=CENTER)
    course_grid.heading("title", text="title", anchor=CENTER)
    course_grid.heading("price", text="price", anchor=CENTER)
    course_grid.heading("time", text="time", anchor=CENTER)
    course_grid.heading("teacher", text="teacher", anchor=CENTER)

    for course in cource_data:
        course_grid.insert("", 'end',  values =(course["code"], course["title"], course["price"], course["time"], course["teacher"]))


    course_grid.pack(fill=BOTH, expand=True,pady=20,padx=(20,5))
    course_grid.configure(yscrollcommand=grid_scrollbar_course.set)
    grid_scrollbar_course["command"]=course_grid.yview

    columns = ('Name', 'Family', 'Gender', 'Student code', 'Age')  
    student_grid = ttk.Treeview(master=body_std, columns = columns, show = 'headings', selectmode=BROWSE)  
    col_width_std = student_grid.winfo_width() 

    student_grid.column("Name", anchor=CENTER, width=col_width_std)
    student_grid.column("Family", anchor=CENTER, width=col_width_std)
    student_grid.column("Gender", anchor=CENTER, width=col_width_std)
    student_grid.column("Student code", anchor=CENTER, width=col_width_std)
    student_grid.column("Age", anchor=CENTER, width=col_width_std)


    student_grid.heading("Name", text="Name", anchor=CENTER)
    student_grid.heading("Family", text="Family", anchor=CENTER)
    student_grid.heading("Gender", text="Gender", anchor=CENTER)
    student_grid.heading("Student code", text="Student code", anchor=CENTER)
    student_grid.heading("Age", text="Age", anchor=CENTER)



    for student in std_data:
        student_grid.insert("", 'end',  values =(student["name"], student["family"], student["gender"], student["std_code"], student["age"]))


    student_grid.pack(fill=BOTH, expand=True,pady=20,padx=(20,5))
    student_grid.configure(yscrollcommand=grid_scrollbar_course.set)
    grid_scrollbar_course["command"]=student_grid.yview
    #endregion

    #region button

    back_image = PhotoImage(file=r"images/return.png")

    Button(
        master=footer,
        text="Back",
        bg="#6c757d",
        fg="white",
        font=("tahoma", 10, "bold"),
        image=back_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#5c636a",
        activeforeground="white",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=10)

    assigning_image = PhotoImage(file=r"images/assigning.png")

    Button(
        master=footer,
        text="Assign",
        fg="black",
        bg="#00c853",
        font=("tahoma", 10, "bold"),
        image=assigning_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#14872f",
        activeforeground="black",
        command=Assign_std_on_click
    ).pack(side=RIGHT, padx=(0,10))

    #endregion

    form.mainloop()

def main_form():

    def assign_course_on_click():
        form.iconify()
        show_student_cource(form)

    def show_student_on_click():
        form.iconify()
        show_student(form)

    def exit_btn_on_click():
        form.destroy()

    def show_course_on_click():
        form.iconify()
        show_course(form)

    def form_load():
        status, output = read_student_course_bl()
                
        if status=="ERROR":
            messagebox.showerror("Error!!!", "\n".join(output.values()))
            return []

        elif status=="SUCCESS":
            return output
        
    students_data = form_load()
        
    form = Tk()
    
    #region form confug
 
    form.title("Student Management System")

    window_width = 1000
    window_height = 600
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    form.configure(bg="white")
    form_image = PhotoImage(file=r"images/menu.png")
    form.iconphoto(False, form_image)

    #endregion

    #region frame
    header = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=80, bg="#f3f6f9", highlightbackground="#e7e7e7", highlightthickness=1)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body_student = LabelFrame(master=form, height=80, bg="white")
    body_student.pack(fill=BOTH, expand=True, padx=20, pady=20, side=LEFT)
    body_student.propagate(False)

   
    #endregion

    #region form header

    Label(
        master=header,
        text="Student Management System",
        bg="#f3f6f9",
        fg="#06172a", 
        font=("tahoma", 11, "bold"),
        compound=LEFT,
        ).pack(side=LEFT,padx=10)
    #endregion

    #region scrollbar
    grid_scrollbar_student= ttk.Scrollbar(master=body_student, orient=VERTICAL)
    grid_scrollbar_student.pack(side=RIGHT,fill=Y, pady=20, padx=(0,20))

    #endregion

    #region grid

    columns = ("name", "family", "gender", "age", "stdcode", "course code", "tittle", "teacher", "time", "price")  
    students_grid = ttk.Treeview(master=body_student, columns = columns, show = "headings")  
    col_width_student = students_grid.winfo_width() 

    students_grid.column("name", anchor=CENTER, width=col_width_student)
    students_grid.column("family", anchor=CENTER, width=col_width_student)
    students_grid.column("gender", anchor=CENTER, width=col_width_student)
    students_grid.column("age", anchor=CENTER, width=col_width_student)
    students_grid.column("stdcode", anchor=CENTER, width=col_width_student)
    students_grid.column("course code", anchor=CENTER, width=col_width_student)
    students_grid.column("tittle", anchor=CENTER, width=col_width_student)
    students_grid.column("teacher", anchor=CENTER, width=col_width_student)
    students_grid.column("time", anchor=CENTER, width=col_width_student)
    students_grid.column("price", anchor=CENTER, width=col_width_student)



    students_grid.heading("name", text="First Name", anchor=CENTER)
    students_grid.heading("family", text="Last Name", anchor=CENTER)
    students_grid.heading("gender", text="gender", anchor=CENTER)
    students_grid.heading("age", text="age", anchor=CENTER)
    students_grid.heading("stdcode", text="stdcode", anchor=CENTER)
    students_grid.heading("course code", text="course code", anchor=CENTER)
    students_grid.heading("tittle", text="tittle", anchor=CENTER)
    students_grid.heading("teacher", text="teacher", anchor=CENTER)
    students_grid.heading("time", text="time", anchor=CENTER)
    students_grid.heading("price", text="price", anchor=CENTER)



    for student in students_data:
        for course in student["course"]:
            students_grid.insert("", "end", 
                    values =(
                        student["name"], 
                        student["family"], 
                        student["gender"], 
                        student["age"], 
                        student["stdcode"],
                        course["code"],
                        course["title"],
                        course["teacher"],
                        course["time"],
                        course["price"],

                        ))
    


    students_grid.pack(fill=BOTH, expand=True,pady=20,padx=(20,5))
    students_grid.configure(yscrollcommand=grid_scrollbar_student.set)
    grid_scrollbar_student["command"]=students_grid.yview



    #endregion

    #region bottun

    course_image = PhotoImage(file=r"images/course.png")

    Button(
        master=footer,
        text="Course",
        bg="#00c853",
        fg="black",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#14872f",
        activeforeground="black",
        image=course_image,
        command=show_course_on_click
    ).pack(side=LEFT, padx=10)

    student_image = PhotoImage(file=r"images/student.png")

    Button(
        master=footer,
        text="Students",
        fg="black",
        bg="#626FFF",
        font=("tahoma", 10, "bold"),
        image=student_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#3441CA",
        activeforeground="black",
        command=show_student_on_click
    ).pack(side=LEFT, padx=(0,10))

    assign_image = PhotoImage(file=r"images/assign.png")

    Button(
        master=footer,
        text="Course Assignment",
        bg="#ffc107",
        fg="black",
        activebackground="#ffc107",
        activeforeground="black",
        font=("tahoma", 10, "bold"),
        image=assign_image,
        compound=LEFT,
        padx=7, pady=7,
        command=assign_course_on_click
    ).pack(side=LEFT, padx=(0,10))

    exit_image = PhotoImage(file=r"images/exit.png")

    Button(
        master=footer,
        text="Exit",
        bg="#6c757d",
        fg="white",
        font=("tahoma", 10, "bold"),
        image=exit_image,
        compound=LEFT,
        padx=7, pady=7,
        activebackground="#5c636a",
        activeforeground="white",
        command=exit_btn_on_click

    ).pack(side=RIGHT, padx=20)


    #endregion
   
    form.mainloop()
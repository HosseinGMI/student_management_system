from .dal import *
from typing import Iterable

project_file_path = r"file\student_project.txt"
student_file_path = r"file\students.txt"
course_file_path = r"file\courses.txt"

def listofstr_to_listofdict(data):
    return list(map(lambda std: eval(std.strip()), data))

def listofdict_to_listofstr(data):
    return list(map(lambda cnt: f"{cnt}\n", data))

def read_student_course_bl():

    err_message = {}
     
    status, output = read_content(
        file_path=project_file_path
        )

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    student_list = listofstr_to_listofdict(output)
    return ("SUCCESS", student_list)

def read_courses_bl():

    err_message = {}
     
    status, output = read_content(
        file_path=course_file_path
        )

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    student_list = listofstr_to_listofdict(output)
    return ("SUCCESS", student_list)

def read_students_bl():

    err_message = {}
     
    status, output = read_content(
        file_path=student_file_path
        )

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    student_list = listofstr_to_listofdict(output)
    return ("SUCCESS", student_list)

def validation_field(val: any, field: str, is_empty: bool = True, range_val: Iterable = [], int_only: bool = False) -> list[str]:
    
    err_message = []

    if (not is_empty) and val=="":
        err_message.append(f"{field} is empty")
    
    elif int_only:
            try:
                int(val)
            except:
                err_message.append(f"Please enter only digits for {field}")

    if range_val and val not in range_val:
        err_message.append(f"{field} not in range")

    
    return "\n".join(err_message)

def save_course_bl(code: str, title: str, price: str, time : str, teacher : str):
    
    code = code.strip()
    title = title.strip()
    price = price.strip()
    time = time.strip()
    teacher = teacher.strip()

    err_message = {}

    #region field validation
    error = validation_field(val=code, field="code", is_empty=False, int_only=True)
    if error :
        err_message["code"] = error

    error = validation_field(val=title, field="title", is_empty=False, int_only=False)
    if error :
        err_message["title"] = error

    error = validation_field(val=price, field="price", is_empty=False, int_only=True)
    if error :
        err_message["price"] = error

    error = validation_field(val=time, field="time", is_empty=False, int_only=False)
    if error :
        err_message["time"] = error

    error = validation_field(val=teacher, field="teacher", is_empty=False, int_only=False)
    if error :
        err_message["teacher"] = error

    if err_message:
        return ("ERROR", err_message)
    #endregion
    


    status, output = read_content(
        file_path=course_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    course_list = listofstr_to_listofdict(output)

    for course in course_list:
        if course["code"] == code:
            err_message["code"] = f"{code} exists"
            return ("ERROR", err_message)




    course = {
        "code" : code,
        "title" : title,
        "price" : price,
        "time" : time,
        "teacher" : teacher
    }

    status, output = save_content(
        file_path=course_file_path,
        content=f"{course}\n"
        )
    
    if status=="SUCCESS":
        return ("SUCCESS", "Success message")

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)

def edit_course_bl(code: str, title: str, price: str, time : str, teacher : str):
    code = code.strip()
    title = title.strip()
    price = price.strip()
    time = time.strip()
    teacher = teacher.strip()

    err_message = {}

    
    #region field validation
    error = validation_field(val=code, field="code", is_empty=False, int_only=True)
    if error :
        err_message["code"] = error

    error = validation_field(val=title, field="title", is_empty=False, int_only=False)
    if error :
        err_message["title"] = error

    error = validation_field(val=price, field="price", is_empty=False, int_only=True)
    if error :
        err_message["price"] = error

    error = validation_field(val=time, field="time", is_empty=False, int_only=False)
    if error :
        err_message["time"] = error

    error = validation_field(val=teacher, field="teacher", is_empty=False, int_only=False)
    if error :
        err_message["teacher"] = error

    if err_message:
        return ("ERROR", err_message)
    #endregion
    


    status, output = read_content(
        file_path=course_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    course_list = listofstr_to_listofdict(output)

    for course in course_list:
        if course["code"] == code:
            course["title"] = title
            course["price"] = price
            course["time"] = time
            course["teacher"] = teacher
            break
    else:
        err_message["code"] = f"{code} does not exists"
        return ("ERROR", err_message)

    str_course_list = listofdict_to_listofstr(course_list)

    status, output = save_content(
        file_path=course_file_path,
        content=str_course_list,
        mode="w",
        write_state="wl"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Success message")
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
def remove_course_bl(code: str):
    code = code.strip()

    err_message = {}

    error = validation_field(val=code, field="code", is_empty=False)
    if error:
        err_message["code"] = error
    
    if err_message:
        return("ERROR", err_message)
    
    status, output = read_content(
        file_path=course_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)


    course_list = listofstr_to_listofdict(output)

    for course in course_list:
        if course["code"] == code:
            course_list.remove(course)
            break
    else:
        err_message["code"] = f"{code} does not  exists"
        return ("ERROR", err_message)
    

    str_course_list = listofdict_to_listofstr(course_list)

    status, output = save_content(
        file_path=course_file_path,
        content=str_course_list,
        mode="w",
        write_state="wl"
    )
    
    if status=="SUCCESS":
        return ("SUCCESS", "Success message")

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)

def save_student_bl(name: str, family: str, gender: str, std_code : str, age : str, phone : str):
    
    name = name.strip()
    family = family.strip()
    gender = gender.strip()
    std_code = std_code.strip()
    age = age.strip()
    phone = phone.strip()

    err_message = {}

    #region field validation
    error = validation_field(val=name, field="name", is_empty=False, int_only=False)
    if error :
        err_message["name"] = error

    error = validation_field(val=family, field="family", is_empty=False, int_only=False)
    if error :
        err_message["family"] = error

    error = validation_field(val=gender, field="gender", is_empty=False)
    if error :
        err_message["gender"] = error

    error = validation_field(val=std_code, field="std_code", is_empty=False, int_only=True)
    if error :
        err_message["std_code"] = error

    error = validation_field(val=age, field="age", is_empty=False, int_only=True)
    if error :
        err_message["age"] = error
    
    error = validation_field(val=phone, field="phone", is_empty=False, int_only=True)
    if error :
        err_message["phone"] = error

    if err_message:
        return ("ERROR", err_message)


    status, output = read_content(
        file_path=student_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    student_list = listofstr_to_listofdict(output)

    for student in student_list:
        if student["std_code"] == std_code:
            err_message["std_code"] = f"{std_code} exists"
            return ("ERROR", err_message)
        
    for student in student_list:
        if student["phone"] == phone:
            err_message["phone"] = f"{phone} exists"
            return ("ERROR", err_message)

    #endregion



    student = {
        "name" : name,
        "family" : family,
        "gender" : gender,
        "std_code" : std_code,
        "age" : age,
        "phone" : phone
    }

    status, output = save_content(
        file_path=student_file_path,
        content=f"{student}\n"
        )
    
    if status=="SUCCESS":
        return ("SUCCESS", "Success message")

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)

def edit_student_bl(name: str, family: str, gender: str, std_code : str, age : str, phone : str):
    name = name.strip()
    family = family.strip()
    gender = gender.strip()
    std_code = std_code.strip()
    age = age.strip()
    phone = phone.strip()

    err_message = {}

    
    #region field validation
    error = validation_field(val=name, field="name", is_empty=False, int_only=False)
    if error :
        err_message["name"] = error

    error = validation_field(val=family, field="family", is_empty=False, int_only=False)
    if error :
        err_message["family"] = error

    error = validation_field(val=gender, field="gender", is_empty=False)
    if error :
        err_message["gender"] = error

    error = validation_field(val=std_code, field="std_code", is_empty=False, int_only=True)
    if error :
        err_message["std_code"] = error

    error = validation_field(val=age, field="age", is_empty=False, int_only=True)
    if error :
        err_message["age"] = error
    
    error = validation_field(val=phone, field="aphonege", is_empty=False, int_only=True)
    if error :
        err_message["phone"] = error

    if err_message:
        return ("ERROR", err_message)
    #endregion
    


    status, output = read_content(
        file_path=student_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
    student_list = listofstr_to_listofdict(output)

    for student in student_list:
        if student["std_code"] == std_code:
            student["name"] = name
            student["family"] = family
            student["gender"] = gender
            student["age"] = age
            student["phone"] = phone
            break
    else:
        err_message["std_code"] = f"{std_code} does not exists"
        return ("ERROR", err_message)

    str_student_list = listofdict_to_listofstr(student_list)

    status, output = save_content(
        file_path=student_file_path,
        content=str_student_list,
        mode="w",
        write_state="wl"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Success message")
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)
    
def remove_student_bl(std_code: str):
    std_code = std_code.strip()

    err_message = {}

    error = validation_field(val=std_code, field="std_code", is_empty=False)
    if error:
        err_message["std_code"] = error
    
    if err_message:
        return("ERROR", err_message)
    
    status, output = read_content(
        file_path=student_file_path
        )
    
    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)


    student_list = listofstr_to_listofdict(output)

    for student in student_list:
        if student["std_code"] == std_code:
            student_list.remove(student)
            break
    else:
        err_message["std_code"] = f"{std_code} does not  exists"
        return ("ERROR", err_message)
    

    str_student_list = listofdict_to_listofstr(student_list)

    status, output = save_content(
        file_path=student_file_path,
        content=str_student_list,
        mode="w",
        write_state="wl"
    )
    
    if status=="SUCCESS":
        return ("SUCCESS", "Success message")

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)

def assign_student_bl( student_grid: str, course_grid: str, selected_id_course: str, selected_id_std: str):

    name, family, gender, std_code, age = student_grid.item(selected_id_std[0], "values")

    
    err_message = {}

    course = []

    student = {
            "name" : name,
            "family" : family,
            "gender" : gender,
            "stdcode" : std_code,
            "age" : age,
            
            }
    
    for items in range(len(selected_id_course)):
        code, title, price, time, teacher = course_grid.item(selected_id_course[items], "values") 
        course_add = {"code" : code, "title" : title, "price" : price, "time" : time, "teacher" : teacher}
        course.append(course_add)
    
    student["course"] = course


    status, output = save_content(
        file_path=project_file_path,
        content=f"{student}\n"
        )
    
    if status=="SUCCESS":
        return ("SUCCESS", "Success message")

    if status=="ERROR":
        err_message["filerror"] = "Fileerror message"
        return ("ERROR", err_message)

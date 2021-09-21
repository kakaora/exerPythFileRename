import os

os.chdir('/Users/TheKing/Dropbox/Academics/University of Utah/Clinical Informatics/Fall 2021/BMI 6017-090 Computer Science Fundamentals/myProject/exerPythFileRename/Videos/')

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    file_name, file_ext = os.path.splitext(f)
    ##print(file_name.split('-'))
    f_title, f_course, f_num = file_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)

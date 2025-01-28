from fastapi import FastAPI, Body

app = FastAPI()

courses_db = [
    {'id': 1, 'instructor': 'Atıl', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Ahmet', 'title': 'Java', 'category': 'Development'},
    {'id': 3, 'instructor': 'Atıl', 'title': 'Jenkins', 'category': 'Devops'},
    {'id': 4, 'instructor': 'Zeynep', 'title': 'Kubernetes', 'category': 'Devops'},
    {'id': 5, 'instructor': 'Fatma', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 6, 'instructor': 'Atlas', 'title': 'Deep Learning', 'category': 'AI'}
]

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/courses")
async def get_all_courses():
    return courses_db

#Path Parameter
@app.get("/courses/{course_title}")
async def get_courses(course_title: str):
    for course in courses_db:
        if course.get("title").casefold() == course_title.casefold():
            return course
    
@app.get("/courses/byid/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get("id") == course_id:
            return course

#Query parameter
@app.get("/courses/?")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get("category").casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

#Path and Query Parameters
@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold()
           and course.get('category').casefold() == category.casefold()):
           courses_to_return.append(course)
    return courses_to_return

@app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)
    return new_course

@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == updated_course.get("id"):
            courses_db[index] = updated_course

@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break
    return



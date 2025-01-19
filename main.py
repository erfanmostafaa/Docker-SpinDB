from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title' : 'Title One ' , 'author' : 'Author one' , 'category' : 'sience'},
    {'title' : 'Title Two ' , 'author' : 'Author Two' , 'category' : 'math'},
    {'title' : 'Title Three ' , 'author' : 'Author Three' , 'category' : 'history'},
    {'title' : 'Title Four ' , 'author' : 'Author Four' , 'category' : 'sience'},
    {'title' : 'Title Five ' , 'author' : 'Author Five' , 'category' : 'math'},
    {'title' : 'Title Six ' , 'author' : 'Author  Six' , 'category' : 'history'},

]

@app.get('/books')
def read_all_books():
    return BOOKS


@app.get("/books/{dynamic_params/}")

def read_alls_books(dynamic_param):
    return {'dynamic_param' : dynamic_param}



@app.get("/books/mybook")

def read_all_book():
    return {'book_titile' : 'My favorite book!'}
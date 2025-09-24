# List of books for task5_books function
books = [
    ['The Hunger Games','Suzanne Collins'],
    ['Charlie and the Chocolate Factory','Roald Dahl'],
    ['Summer of \'49','David Halberstam'],
    ['Catcher in the Wry','Bob Uecker']]

#"Database" for task5_getID function
studentDB={
    'Lucas Estevez':42,
    'Jackson Seales':420,
    'Michal Lustig':505,
    'Daniel Barbotko':69
}

#Returns books 0-2
def task5_books():
    return(books[0:3])

#Returns student ID for given name
def task5_getID(student):
    return(studentDB[student])
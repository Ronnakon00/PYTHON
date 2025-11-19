books = []
def add_book(To,isbn,name,namefbook,amout):
    if len(To) == 0:
            return To.append(
                            { 
                            'isbn': isbn,
                            'title': name,
                            'author': namefbook,
                            'total_copies': amout,
                            }
                            )   
    for i in To :
        if isbn != i.get('isbn') :
            return To.append(
                            { 
                            'isbn': isbn,
                            'title': name,
                            'author': namefbook,
                            'total_copies': amout,
                            }
                            )                    
        else : return print("Cant add")

def search_books(name):
    for i in books:
        if i.get('title') == name or i.get('author') == name :
            for j in range(len(i)):
                return print(i)
    return print("Dont have this book")
            
add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
add_book(books, '002', 'Clean Code', 'Robert Martin', 2)
add_book(books, '003', 'The Pragmatic Programmer', 'Hunt & Thomas', 2)
add_book(books, '004', 'Design Patterns', 'Gang of Four', 1)
add_book(books, '005', 'Introduction to Algorithms', 'Cormen et al.', 2)
add_book(books, '006', 'Code Complete', 'Steve McConnell', 3)
add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)

search_books('Clean Code')

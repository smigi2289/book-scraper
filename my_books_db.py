import csv;

books_db_path = "book_details.csv"
def get_known_sellers_list(sellersColumn):
    known_sellers = sellersColumn.split('@')
    
    return known_sellers


def get_data():
    booksData = []
    with open(books_db_path) as book_details_file:
        data = csv.reader(book_details_file)
        for row in data:
            bookData = {"basic_search_text":row[0],"full_book_name":row[1],"known_sellers":get_known_sellers_list(row[2])}
            booksData.append(bookData)
            
    return booksData
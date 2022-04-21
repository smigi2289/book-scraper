from pydoc import text
import simania_scraper;
import my_email_helper
import my_books_db

booksData = my_books_db.get_data()

isUnix =False

for bookData in booksData:
    unknown_sellers = simania_scraper.get_unknown_sellers_for_book(bookData["basic_search_text"],bookData["full_book_name"],bookData["known_sellers"],isUnix)
    if(len(unknown_sellers)>0):
        print("found unknown sellers")
        subject =f" נמצאו מוכרים לא מוכרים לספר {bookData['full_book_name']}"
        message = ""
        i=1
        for seller in unknown_sellers:
            message=message +f"\n{i}:{seller['seller_name']}"
            i = i+1
        my_email_helper.send_email_from_me("roy2289@gmail.com",message=message,subject=subject)
    else:
        print("no new sellers")



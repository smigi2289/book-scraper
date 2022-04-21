from pydoc import text
import simania_scraper;
import my_email_helper
import my_books_db

booksData = my_books_db.get_data()

for bookData in booksData:
    unknown_sellers = simania_scraper.get_unknown_sellers_for_book(bookData["basic_search_text"],bookData["full_book_name"],bookData["known_sellers"])
    if(len(unknown_sellers)>0):
        print("found unknown sellers")
        message ="found unknown sellers: \n\n"
        for seller in unknown_sellers:
            message+= seller["seller_name"]+","
        my_email_helper.send_email_from_me("found unknown sellers",unknown_sellers[0]["seller_name"])
    else:
        print("no new sellers")
#my_email_helper.send_email_from_me("roy2289@gmail.com","hi","subject")
#get_unknown_sellers_by_file("book_details.csv")



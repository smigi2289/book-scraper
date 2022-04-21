from selenium import webdriver;

def login(driver,user_text,password_text):
    login=driver.find_element_by_css_selector("#topTop > div:nth-child(5) > a:nth-child(1)");
    login.click()
    user = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    perform_login_button = driver.find_element_by_css_selector("#gaia_table > tbody > tr:nth-child(7) > td:nth-child(2) > input")
    user.send_keys(user_text)
    password.send_keys(password_text)
    perform_login_button.click()


def find_book_after_login(driver,writer,partial_name):
    search_input = driver.find_element_by_id('query')
    search_input.send_keys(writer)
    submit_search_button = driver.find_element_by_css_selector("#topLogo > table > tbody > tr > td:nth-child(3) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input")
    submit_search_button.click()
    
    book_links = driver.find_elements_by_class_name("searchResult")
    
    for i in range(1,len(book_links)+1):
        specific_book_link = driver.find_element_by_css_selector(f"#the_books > table:nth-child({i}) > tbody > tr > td:nth-child(3) > div > div.title.clickable > a:nth-child(1)")
        if partial_name in specific_book_link.text:
            specific_book_link.click()
            break
        
def get_sellers_data(driver):
    sellers_data = []
    sellers = driver.find_elements_by_css_selector('#priceComparison > book-private-sellers > div > div.description > table > tbody > tr')
    i=0;
    for seller in sellers:
        i=i+1
        if(i==1):
            continue
        seller_data =driver.find_elements_by_css_selector(f"#priceComparison > book-private-sellers > div > div.description > table > tbody > tr:nth-child({i}) > td")
        seller_data_object = {}
        seller_data_object["seller_name"]= seller_data[0].text
        seller_data_object["seller_location"] = seller_data[1].text
        seller_data_object["book_state"]= seller_data[2].text
        seller_data_object["book_price"]= seller_data[3].text
        sellers_data.append(seller_data_object)   
    
    return sellers_data

def getUnkownSellers(all_sellers_data,known_sellers):
    unknown_sellers = []
    for seller in all_sellers_data:
        seller_is_known = False
        for known_seller in known_sellers:
            if(known_seller == ''):
                continue
            if known_seller in seller["seller_name"]:
                seller_is_known = True
        if not seller_is_known:
            unknown_sellers.append(seller)
    return unknown_sellers

def get_unknown_sellers_for_book(basic_search_text,full_book_name,known_sellers,isLinux=False):
    
    win_driver_path = "chromedriver.exe"
    unix_driver_path = "chromedriver"
    if(isLinux):
        driver_path =unix_driver_path
    else:
       driver_path = win_driver_path 
    driver = webdriver.Chrome(executable_path=driver_path);

    driver.get("https://simania.co.il/")

    login(driver,"roy2289@gmail.com","22753737")

    #find_book_after_login(driver,"אסימוב","כתבי אייזק אסימוב (כרך 1")
    find_book_after_login(driver,basic_search_text,full_book_name)

    data = get_sellers_data(driver)

    unknown_sellers = getUnkownSellers(data,known_sellers)
    driver.quit()
    
    return unknown_sellers

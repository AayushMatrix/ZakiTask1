def apply_discount(price,discount_percentage):
    return price * (1-discount_percentage/100)

class Library:
    def __init__ (self,title,author,publish_year,publication,bundle=50):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.publication = publication
        self.bundle = bundle
        self.book_name = ['Curious','Cloudy','Watching']
        self.book_price = {'Hurston':20,'Devil':43,'Eyes':55}
        self.book_color = {'Red'}
        self.available = True

    def add_book_price(self,book,price):
        self.book_price[book]=price  
        print("Book price are",self.book_price)
    
    def add_book_name(self,book):
        self.book_name.append(book)
        print("Book name are",self.book_name)

    def add_color(self,color):
        self.book_color.add(color)
        print("Book color are",self.book_color)
    
    def calculate_price(self,price,discount_percentage=10):
        discount = apply_discount(price,discount_percentage)
        total = discount * 2
        print(total)
    
    def set_availability(self, status):
        self.available = status

    def buy_book(self, book_name, quantity=1):
        if book_name not in self.book_price:
            print(f"Book not found: {book_name}")
            print(f"Availability: {self.available}") 
            return False
        
        if quantity >= self.bundle:
            self.set_availability(False)
            print("Status: Item sold out")
        else:
            self.set_availability(True)
        print(f"Availability: {self.available}")        
        return self.set_availability 

lib = Library("Sample Book", "Author", 2023, "Pub Co")
lib.add_book_price("Red",20)
lib.add_book_name("Munamadan")
lib.add_color("Yellow")
lib.calculate_price(200)
lib.buy_book("Devil",200) 


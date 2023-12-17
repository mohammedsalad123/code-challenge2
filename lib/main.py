from customer import Customer
from resturant import Restaurant
from review import Review

# Create instances and test instance methods
customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

print(customer1.full_name())  # Test instance method full_name()

# Create instances and test class methods
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

print(Restaurant.all())  



review1 = Review(customer1, restaurant1, 4)
print(review1.get_rating())

print(Review.all()) 
review1.get_customer()

review1.get_restaurant()


restaurant = Restaurant("Food Haven")
print(restaurant.name)  
restaurant.get_name()

review1 = Review("John Doe", restaurant, 4)
restaurant.reviews()
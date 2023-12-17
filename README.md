# Yelp-Style Domain Management

This project implements a Yelp-style domain with three main classes: `Customer`, `Restaurant`, and `Review`. It allows management of restaurants, customers, and their reviews.

## Author

- **Author:** Mohammed Salad

## License

This project is licensed under the MIT License 

## Classes and Functionality

### Customer

Represents a customer with attributes such as given name, family name, and associated reviews.

#### Methods:

- `given_name()`: Returns the customer's given name.
- `family_name()`: Returns the customer's family name.
- `full_name()`: Returns the full name of the customer.
- `all()`: Returns a list of all customer instances.
- `restaurants()`: Returns a list of unique restaurants reviewed by the customer.
- `add_review(restaurant, rating)`: Adds a review associated with the customer and a given restaurant.

### Restaurant

Represents a restaurant with a name and associated reviews.

#### Methods:

- `name()`: Returns the restaurant's name.
- `reviews()`: Returns a list of reviews for the restaurant.
- `customers()`: Returns a list of unique customers who reviewed the restaurant.
- `all()`: Returns a list of all restaurant instances.
- `average_star_rating()`: Calculates the average star rating based on its reviews.

### Review

Represents a review given by a customer for a specific restaurant.

#### Methods:

- `rating()`: Returns the rating given in the review.
- `all()`: Returns a list of all review instances.
- `customer()`: Returns the customer object associated with the review.
- `restaurant()`: Returns the restaurant object associated with the review.


# phase-3-code-2

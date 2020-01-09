from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Menu for Pizza Palace
myFirstRestaurant = Restaurant(name = "Pizza Palace")

session.add(myFirstRestaurant)
session.commit()

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzerella",
course = "Entree", price = "$8.99", restaurant = myFirstRestaurant) #Create Foreign Key relationship

session.add(cheesepizza)
session.commit()


# Menu for UrbanBurger
restaurant1 = Restaurant(name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="$4.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(name="Auntie Ann\'s Diner ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(name="State Bird Provisions")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print ("added menu items!")

#Create
#1. Specify Name variable to make new entry in database
#2. Create Foreign key relationship between the MenuItem and the MyFirstRestaurant Variable
#myFirstRestaurant = Restaurant(name = "Pizza Palace")

#session.add(myFirstRestaurant)
#session.commit()

#cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzerella",
#course = "Entree", price = "$8.99", restaurant = myFirstRestaurant) #Create Foreign Key relationship

#session.add(cheesepizza)
#session.commit()

#Read
#1. Use session.query() method to read data from database. Use python for loop to return data that you want to see
#session.query(MenuItem).all
#output: <bound method Query.all of <sqlalchemy.orm.query.Query object at 0x7f4b967d6dd0>>
#firstResult = session.query(Restaurant).first() #Create a variable called first result, set it to equal to Restaurant Table, and use .first() method to correspond to a single row in my database. Single row references allow me to extract column entries as method names. 
#firstResult.name #Give the name of the restaurant object as it is stored in the database.
# output: u'Pizza Palace'

#2. Create a python script that will populate data from the database and make it readable
#When we use a query by itself it lists the objects in the database that are referenced in memory but it is not readable.
#items = session.query(MenuItem).all() #Make a variable called items and set it equal to a query that retrieves all of my menu items.
#for item in items: #declare item as the variable that to iterate through
#print item.name #prints out every menu item in the database.

#Update
#1. Find Entry
#2. Reset Values
#3. add to session
#4. session.commit()

#1. Use the filter_by function to find all the veggie burgers in our Restaurant Menu Database
#veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
#- filter_by function always returns a collection of objects
#- write a for loop to display the data.
#for veggieBurger in veggieBurgers:
#   print veggieBurger.id
#   print veggieBurger.price
#   print veggieBurger.restaurant.name
#   print "\n"

#The output displays a list of all the veggie burgers in my database
# the first one is UrbanBurger with an ID of 2

# Now create a query where we only return the menu item with the ID of 2
#UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 2).one()
#store it to the variable Uraban VeggieBurger
#appending the  .one() fucntion to the end of the query tells sql alchemy to only return one object.

#Check its price to make sure you have the right burger.
#print UrbanVeggieBurger.price
#output: $7.50

#Let's reset the price of the Urban Veggie Burger to $2.99.
#add the UrbanVeggieBurger object to our session and commit it to the database

#UrbanVeggieBurger.price = '2.99'
#session.add(UrbanVeggieBurger)
#session.commit()

#Now execute the query to see all the veggie burgers in the database
#You will see the price has now changed.

#Use the same for loop and modify it a bit to change all the veggie burger prices to $2.99
#for veggieBurger in veggieBurgers:
#   if veggieBurger.price != '$2.99':
#           veggieBurger.price = '$2.99'
#           session.add(veggieBurger)
#           session.commit()

#Output:
#2
#$2.99
#Urban Burger


#10
#$2.99
#Urban Burger


#21
#$2.99
#Panda Garden


#27
#$2.99
#Thyme for That Vegetarian Cuisine


#37
#$2.99
#Andala's


#43
#$2.99
#Auntie Ann's Diner


#Delete
#1. Find Entry
#2. session.delete(entry)
#3. session.commit()

#spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream).one()
#print spinach.restaurant.name
#session.delete(spinach)
#session.commit()

#Now when you query spinach it is not found
#Output:
#>>> spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/usr/local/lib/python2.7/dist-packages/sqlalchemy/orm/query.py", line 3332, in one
#    raise orm_exc.NoResultFound("No row was found for one()")
#sqlalchemy.orm.exc.NoResultFound: No row was found for one()
#>>>

#Congratulations! You've learned how to use an ORM to create a database and execute CRUD operations on it. 
#In Lession 2 we'll build a web server that will be able to perform these crud operations bases on requests from the user.

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

app = Flask(__name__) #create an instance of this class with the name of the running application.

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Making an API Endpoint (GET Request)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

#Add JSON Endpoint Here
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)
# The route decorator is used to bind a function to a URL. The examples below are static
# We can also make certain paths of the URL dynamic and attach multiple rules to a function
@app.route('/') #This is a decorator. The decorator wraps our function inside the app.route function
@app.route('/restaurants/<int:restaurant_id>') #The function below is executed if either of theese routes are sent from the browser
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items = items)
    
    #output = ''
    #for i in items:
        #output += i.name
        #output += '</br>'
        #output += i.price
        #output += '</br>'
        #output += i.description
        #output += '</br>'
        #output += '</br>'
    #return output

# Task 1: Create route for newMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
        'description'], price=request.form['price'], course=request.form['course'],
        restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST']) # By Default, a route in Flask only answers to get requests but that can be changed by providing the methods argument inside the "route decorator"
def editMenuItem(restauraunt_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("Menu Item Edited!")
        return redirect(url_for('resturantMenu', restaurant_id = restauraunt_id))
    else:
        return render_template(
            'editmenuitem.html', restauraunt_id=restauraunt_id, menu_id=menu_id, item = editedItem,)

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete',
            methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu Item has been deleted")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deletemenuitem.html', item = itemToDelete)
    
if __name__ == '__main__': #The if statement makes sure the server only runs if the script is run directly from the python interpreter and not used as an imported module.
    app.secret_key = 'super_secret_key' #Used to create sessions for users. Normally this should be a really secure password.
    app.debug = True #Enables Debug support #Server will reload itself anytime it notices a code change
    app.run(host = '0.0.0.0', port = 5000) #By default, the server is only accessible from the host machine
 #host 0.0.0.0 tells the web server on my vagrant machine to listen on all public ip addresses.   
 #with Flask, we don't have to explicitly write out response codes.
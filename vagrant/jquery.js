//jquery notes

/* 
JQuery is a JavaScript Library used to directly manipulate the DOM (Document Object Model)
It exists so we can focus on UX, and not browser compatibility.

$ => jQuery Collection
$ references the JQuery Javascript Object and  returns an array-like Function/Object. (like an array but with additional methods)
We can pass strings, functions, or methods to the jQuery Function
Ex.
$(string)
$(function)
$(DOM Element)
$(Dom Element)

You can also call methods directly on the jQuery Object like ajax.
$.ajax() - simplifies ajax into a jQuery Method call.

$('tag'); => argument passed into function is callaed a SELECTOR
$('.class'); => JQuery uses CSS selectors so you can call classes and IDs
$('#id');

DOM Tree
                            body
                             |
                            div
                             |  
                            div
                          /     \
                      form       ul
                       |        /   \
                     input     li    li
Traversal Methods
Used to Navigate around the DOM

Examples:
.parent() Div is the parent of another Div.
.parents()
.children() - elements that are nested inside each other in the DOM. Ex. Ul or Form could be ca chile of div.
.find()
.siblings() - elements at the same level are siblings. Such as a UL and a Form, li and li, or li and input.

For this quiz, use a jQuery tag selector to grab all of the <li>s on the page!
Start with this variable! (don't delete it!)
var listElements;

listElements = $('li');

console.log(listElements);

For this quiz, use a jQuery class selector to grab all of the elements of class 'article-item' on the page!
// don't change this variable!

var articleItems;

articleItems = $('.article-item');

console.log(articleItems);

For this quiz, use a jQuery class selector to grab all the element with id 'nav' on the page!
don't change this variable!

var nav;

nav = $('#nav');

console.log(nave);

For this quiz, use articleList and DOM navigation methods to collect articleList's
sibling <h1> (var h1), children (var kids), and parent <div>s (var parents).
You must use articleList to navigate to the element(s)!

var articleList, h1, kids, parents;

articleList = $('.article-list');

h1 = articleList.siblings('h1');

kids = articleList.find('*');

parents = articleList.parents('div');

console.log(h1, kids, parents);


Hosting jQuery -
You can add jQuery to any website using script tags

Host on your own server 
.local
.jQuery official

It is recomended to use a CDN
.Content Delivery Netowrk (like google)

*****DOM MANIPULATION*****

.addClass - adds the specified classes to each of the set of matched elements.
$('#item').addClass('blue') add the blue class to the element witht he ID of 'item'
var featured;
featured = $('.featured');
featured.toggleClass('featured')

For this quiz, remove the class 'featured' from Article #2 and add it to Article #3!
You must use jQuery's toggleClass method!
var article2, article3;
article2 = $('.featured');
article3 = article2.next();
article2 = toggleClass('featured')
article3 = toggleClass('featured')

***CHANGING CSS CLASSES***
.attr()

For this quiz, set the href of the <a> in the first nav item to "#1".
You must use jQuery's attr() method!

var navlist, firstItem, link;
navlist = $('.nav-list'); select navlist by passing in the class .nav-list
firstItem = navlist.children().first(); select children of navlis and use first() to return first one
link = firstItem.find('a'); pass the 'a' tag into the find() of first item to select the a tag.
link.attr('href', '#1'); Use the .attr method to change the jref attribut and set it to #1

***Modifying CSS***

For this quiz, change the font-size of all the article-items to 20px!
You must use jQuery's css() method!

var articleItems;
articleItems = $('.article-item'); select the article items class
articleItems.css('font-size', '20px'); use .css method to change font size.

***PULLING HTML AND TEXT***
For this quiz, use jQuery's val method to make live changes to the 'Cool Articles' <h1>!
The starter code below creates an event listener that will run any time the input changes.
For more on events, check the instructor notes.

$('#input').on('change', function() {
    var val;
    val = $('#input').val();  Collect the value of 'input' using .val()
    h1 = $('.article').children('h1'); Collect the h1 that we want to change
    h1.text(val); Set h1 to Value
});

*****REMOVING DOM ELEMENTS*****
For this quiz, remove the <ul> from the first article item!
You must use jQuery's remove() method.
var articleItems;
articleItems = $('.article.item'); create a jQuery collection of all the elements of class article item
ul = articleItems.find('ul); call find on the article items to find all the instances of unordered list
ul.remove() remove the unordered list.

if i only wanted to remove elements with class bold i could use a selector.
ul.children().remove('bold');

***ADDING DOM ELEMENT***
Its hard to add elements to the DOM with VANILLA JS because.

1.Have to create a DOM node
var div = document.createNote('div');

2. Add Data to it
div.innerHTML = "Hello Udacity";

3. Find a Parent for it.
var parent = document.querySelector('#parent');

4. Add that node as a 'child' to that 'parent'
parent.append(Child(div);)

JQUERY makes the process easier becuase you can create DOM noes and simultaneously add them to the document
with one simple method.

***Appending Child Elements***
Add Children to the element

var firstArticleItem;
firstArticleItem = $('.article-item').first(); select the first element of the .article-item class
firstArticleItem.append('<img src="http://placepuppy.it/200/300">'); adds a new element as the last child of the selected item
firstArticleItem.prepend(<img src="http://placepuppy.it/200/300">'); adds a new element as the first child of the selected item.



Documentation on .append()
Documentation on .prepend()
Documentation on .insertBefore()
Documentation on .insertAfter()

***BUILD A DOM (FAMILY) TREE***
For this quiz, you'll need to add to the DOM tree that already exists.
'#family2' should be a sibling of and come after '#family1'. '#bruce' should be the only immediate child
of '#family2'. '#bruce' should have two <div>s as children, '#madison' and '#hunter'.

var family1, family2, bruce, madison, hunter;

family1 = $('#family1');
family2 = $('<div id="family2"><h1>Family 2</h1></div>'); passing in a string to the jQuery Object creates a new DOM Element.
bruce = $('<div id="bruce"><h2>Bruce</h2></div>');
madison = $('<div id="madison"><h3>Madison</h2></div>');
hunter = $('<div id="hunter"<h3>Hunter</h3></div>');

family2.insertAfter(family1); insert family 2 after family 1
family2.append(bruce); add bruce to family 2 
bruce.append(madison); add madison and hunter to bruce.
bruce.append(hunter);

***Iterating with Each Quiz***
Documentation on .each() similiar to a for loop
Documentation on $(this) 'this' keyword references the object that created it.

For this quiz, use jQuery's each() method to iterate through the <p>s,
calculate the length of each one, and add each length to the end of each <p>.
Also, make sure you don't change the text inside each <p> except to add the length, otherwise your
length numbers won't be correct!

function numberAdder() {
    var text, number;
    text = $(this).text(); finds the text referenced within the object
    number = text.length; calculates its length
    $(this).text(text + " " + number); Changes the text on each element to the same text plus a space plus a number.
}

$('p').each(numberAdder); iterate through all the 'p' tags using the .each(), numberAdder()


Want faster page loads? Use a CDN!
It's also worth noting that because so many websites use jQuery, there's a very good chance 
that your users' browsers have already cached the same copy of jQuery that you want to use.

If you use a CDN, your users' browsers will recognize that they already have a cached copy of 
jQuery from the same CDN when your site loads, which means that they don't need to download it again. 
So those extra KBs from jquery.min.js won't be downloaded and your site will load faster!

jQuery is popular because it allows 'Fast Selection' , 'Cross-Browser Compatibility', and 'Easy DOM Manipulation'.

***PASSING A FUNCTION(CALLBACK) TO THE JQUERY OBJECT***
See Documentation.
*/


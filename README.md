# INLS620_FinalProject
The Game Review Service for INLS 620 Fall 2017 class by Stevia Tedjawiguna and Ga Kay Gao

Machine-readable access through HTML+Microdata.

##Class Attributes:

navbar
	Indicates parent tag for the navigation bar

navbar-list
	Indicates parent tag for the navigation elements. May appear in navbar. Describes the elements in the navigation bar

homepage
	May appear in navbar-list. Describes the home page element

game-list
	May appear in navbar-list. Describes the game list element

game-data
	Indicates parent tag for game information

user-data
	Indicates parent tag for user information

review-data
	Indicates parent tag for review information

page-title
	May appear in game-data, user-data, and review-data. Describes the title for every page in the service

user-photo
	May appear in user-data. Describes the image for the user page

biodata
	May appear in user-data. Indicates parent tag for user data

about
	May appear in user-data, and biodata. Describes information about the user. Includes name and bio

user-review
	Describes the list of reviews written by a user

all-accounts
	Describes all user accounts in the service

all-users
	Describes all users

banned-users
	Describes all banned users

all-games
	Describes the list of all games in the service

game-search
	Describes the search function for games

description
	Describes the description for a specific game

reviews
	May appear in game-data. Describes the reviews for a specific game

game-review
	Describes the list of reviews for a specific game

post-review
	Describes the post functionality for creating a new review for a game

ind-review
	May appear in review-data. Indicates the parent game for individual reviews

review-text
	May appear in the ind-review, and review-data. Describes the text for the review

update-review
	Describes the update functionality for an individual review

game-review
	Describes the link to go back to the review list for a game

users
	Describes the list of users in the service

post-game
	Describes the post functionality for a new game

update-game-desc
    Describes the update functionality for game description on individual game page

update
    Describes the functionality of the submit button of update game description

## Link Relations

index
	Indicates that the page is part of hierarchal structure and the hyperlink leads to the top level resource of that structure (MDN)

next
	Indicates that the hyperlink leads to the next resource of the sequence the current page is in (MDN)

prev
	Indicates that the hyperlink leads to the preceding resource of the sequence the current page is in (MDN)

collection
	Points to a resource which represents the collection resource (IANA)

item
	Points to a resource that represents the member of the collection resource (IANA)

related
	Identifies a related resource (IANA).

##Microdata Types:

http://schema.org/WebPage
    Denotes a web page

http://schema.org/ProfilePage
    A type of web page: Profile page

http://schema.org/ItemList
    Denotes a list of items

http://schema.org/ListItem
    Any list item

http://schema.org/VideoGame
    Indicates the properties of an electronic game that involves human interaction with user interface

http://schema.org/Review
    A review of an item

##Microdata Properties:

URL
    The URL of the item

headline
    Headline of an article

image
    An image of the item

name
    The name of the item

description
    The description of the item

itemListElement
    To list the unordered items

position
    Indicates the position in the list

review
    A review of the item

author
    The author of the review

dateCreated
    Indicates the date of when the review is created

comment
    A comment on the review




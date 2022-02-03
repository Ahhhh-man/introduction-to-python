# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
## universal -> everyone can watch
## pg --> General viewing, but some scenes may be unsuitable for young children
## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
## 15 --> No one younger than 15 may see a 15 film in a cinema.
## 18 --> No one younger than 18 may see an 18 film in a cinema.

# Request user age
age = int(input('What\'s your age? '))
# Assume movie rating is given
movie_rating = '15'

if movie_rating == '18' and age >= 18:
    print('You can watch this "Suitable only for adults 18+" film')
elif movie_rating == '15' and age >= 15:
    print('You can watch this "Suitable only for 15 years and over" film')
elif movie_rating == '12' and age >= 12:
    print('You can watch this "Suitable for 12 years and over" film')
elif movie_rating == 'pg':
    print('You can watch this "PG Parental Guidance" film')
elif movie_rating == 'U':
    print('You can watch this "U Universal - Suitable for all')
else:
    print('Sorry you can\'t watch this {} film'.format(movie_rating))
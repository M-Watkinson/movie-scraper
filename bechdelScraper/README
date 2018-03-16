# Bechdel Test Movie List scraper

With this project, I wanted to scrape the IMDb links for every passing movie on the Bechdel Test Movie List. Then I wanted to use those links to get the movie title and rating off of IMDb. Finally, I wanted to write all of that information into a csv file with separated rows for the movie titles and ratings.

## The Process

I began by opening the url to all the movies on the Bechdel Test Movie List and getting the IMDb links from their listing. I did this by targeting the div with a class of movie. However, I also wanted to narrow my results by only getting movies that passed the test. This was a lot trickier, and I had to look around on Google for awhile to see if others tried to do the same thing. I eventually created a for loop that went through the movies and listed any image with the "src" of "/static/pass.png". However, I had to also put that into an if/else statement in the for loop so that it didn't get all of the movies or throw an error.

Next, I wanted to get the title and rating of each of the passing movies from IMDb. For this, I had to open the url's I got from the previous scraping, then target the H1s on the page, because the only H1s were those with the titles of the movie. This made it very easy, which I was thankful for. The ratings were also very easy, because they all had a span with "itemprop" as "ratingValue". Then, in order to easily put them into two rows in a csv file, I put them into a list called output. Because title and rating are separated by a comma without a space, Python thinks it is one thing, but csv recognizes the comma and separates it into two. Then I wrote the results of output into a csv file.

One problem that came out of this is that it kept returning an HTTPError. To fix this, I put a time.sleep() function into the except portion of my code. I also had to use try/except to help with the error I kept getting due to the fact that not every movie had a ratingValue.

## Final Thoughts

This project was really tough and very frustrating. I spent a lot of time on things that felt simple, like only getting the passing movies to be listed. However, I felt like I learned a lot from this project, and it helped me plan more before I started scraping. I also did more pseudo code in a notebook to predict how I thought things would work (even though they typically did not end up working that way). Overall, I am thankful for the experience but happy that the project is finished.

## WARNING

This file spits out 4,372 movies and takes about an hour and a half to run. 

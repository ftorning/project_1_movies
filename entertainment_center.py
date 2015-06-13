import media
import fresh_tomatoes_v2

zoolander = media.Movie("Zoolander",
                        "At the end of his career, a clueless fashion model is brainwashed to kill the Prime Minister of Malaysia.",
                        "http://upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg",
                        "https://youtu.be/YtQq0T3ExLs"
                        )
dumb_and_dumber = media.Movie("Dumber and Dumber",
                              "The cross-country adventures of two good-hearted but incredibly stupid friends.",
                              "https://d12vb6dvkz909q.cloudfront.net/uploads/galleries/2202/dd-poster.jpg",
                              "https://youtu.be/l13yPhimE3o"                              
                              )
bridesmaids = media.Movie("Bridesmaids",
                          "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
                          "http://www.mattsmoviereviews.net/Images/bridesmaidsposter09.jpg",
                          "https://youtu.be/FNppLrmdyug"                          
                          )
redviolin = media.Movie("The Red Violin",
                        "A perfect violin inspires passion, making its way through three centuries of owners.",
                        "http://www.impawards.com/1999/posters/red_violin_ver2.jpg",
                        "https://youtu.be/3feDUcDRNAg"                       
                        )
flawless = media.Movie("Flawless",
                       "An police officer suffers a stroke and is prescribed singing lessons - with the drag queen next door",
                       "http://www.impawards.com/1999/posters/flawless.jpg",
                       "https://youtu.be/ObrdmtHZsvw"                       
                       )
hollandsopus = media.Movie("Mr. Holland's Opus",
                           "A professional musician and composer finds fulfillment as a high school music teacher, husband, and father.",
                           "http://www.impawards.com/1995/posters/mr_hollands_opus_ver1.jpg",
                           "https://youtu.be/CB1-ASsrNQI"                           
                           )
thering = media.Movie("The Ring",
                      "A journalist must investigate a mysterious videotape which seems to cause the death of anyone in a week of viewing it.",
                      "https://biffbampop.files.wordpress.com/2014/10/the-ring-movie-poster-2002-1020234266.jpg",
                      "https://youtu.be/ymPUAsPsTwg"                      
                      )
conjuring = media.Movie("The Conjuring",
                        "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
                        "http://i.movie.as/p/600/126276.jpg",
                        "https://youtu.be/k10ETZ41q5o"                        
                        )
orphan = media.Movie("Orphan",
                     "A husband and wife who recently lost their baby adopt a 9-year-old girl who is not nearly as innocent as she claims to be.",
                     "http://www.impawards.com/2009/posters/orphan.jpg",
                     "https://youtu.be/e-L0eOjvSM4"                     
                     )
                                          
                     
#Create list of class instances
movies = [zoolander, dumb_and_dumber, bridesmaids, redviolin, flawless, hollandsopus, thering, conjuring, orphan]
#Calls fresh tomatoes v2 that includes storyline
fresh_tomatoes_v2.open_movies_page(movies)


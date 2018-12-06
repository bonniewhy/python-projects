# 3. MAD LIBS GENERATOR ---
#       TODO: Inspired by "Summer Son's Mad Libs project" with Javascript. The program
#       will first prompt the user for a series of inputs a la Mad Libs. For example, a
#       singular noun, an adjective, etc. Then, once all of the information has been
#       inputted, the program will take that data and place them into a premade story
#       template. You'll need prompts for user input, and to then print out the full story
#       at the end with the input included.
#
#       Concepts to keep in mind --
#           -- Strings
#           -- Variables
#           -- Concatenation
#           -- Print
#
#       A pretty fun beginning project that gets you thinking about how to manipulate user
#       inputted data. Comared to the prior projects, this project focuses far more on
#       strings and concatenating. Have some fun coming up with some wacky stories for this!
import time

# Write a menu function to prompt the player to choose a story.
def menu():
    # Each story should have a different subject, and depending on what "word" is chosen, that is what story they will play through."
    choices = "melodramatic", "offensive", "mistake"
    
    # There is also a way to exit during this menu if the player is sick of playing.

    # If the user inputs an invalid answer, you should tell them they're wrong and prompt them for a correct answer to the menu.

    # If the user types a valid input, the menu function should call the corresponding story function.
    return choice

def melodramatic():
    # Write a story with that keyword.
    
    # Remove major parts of the story.

    # Make a list to hold each of the word types and replace each word with {wordtype} in the story string.

    '''Tonight, I witnessed (four) (little) (girls) get ran over by a (Jeep) on (Yanceyville road) near (Peach Orchard Drive). Everybody (kept going), but naturally, I (stopped) in the middle of the road and turned my (hazards) on to call 911. The driver gets out of the (car) and starts (approaching) the (girls), but surprisingly they (get up) and start heading home. I (yell) to them and tell them not to leave -- the (police) were on their way. The driver gets in the (car) and starts (driving off) through the mud and (construction). I ride alongside him in the (street), honking my (horn). He gets to the end of the (hill) and sits there because he didn't want me to run his (tags). Therefore, I sit in the (middle) of the (street) until he finally (pulls out) in (front) of me onto the side of the (road). As I'm (reading) his (tag) to the (emergency responder), he walks up to my (car) and I speed off. When I came back on the way back (home), I (spoke) to a (relative) who told me the driver (lied) to the (police) and told them that the (girls') (parents) sent him to pick them up. Turns out he was trying to (kidnap) the (girls). If I didn't stop, those (babies) may not have ever seen their (families) again! Yes, it was (dangers), and I had (somewhere to be), but I stopped long enough to make a (difference). Why don't we (stop) when we see stuff like this? Maybe that's why so many (kids) are (going missing). Sometimes things are (bigger) than (us). It's not always about you! I believe (God) placed me there tonight for a reason and all I can do is thank (him). Those (girls) will be able to go (home) to their (families).'''

def offensive():

    # Jerri Blank's drug monologue? Something from SWC.
    '''Hello. I'm (Jerri Blank), and I'm a (forty-six year-old) high school freshman. For (thirty-two) years I was a (teenage) runaway. I was a (boozer), a (user) and a (loser). My friends were (dealers), (cons) and (eighteen-karat pimps). Stoney and I would go over to (Buckle’s) and (Puff) would turn us on to a hot load of (mescaline) crumbled into a tumbler of (ether) with a float of (Percocet) jimmies. I’d (wake up) with blood on my (ass), and then we’d get high. Those were some good times. Look, I rode that (brown tiger) for (twenty) years. It took me through a (carnival) of hell. I became the plaything of (Indonesian) (businessmen). By the end, I was barely (human). But now, I'm out of jail, picking up my life exactly where I left off. I'm back in (high school), living at (home) and (discovering) all sorts of things about my (body). I'm finding out that though the faces have changed, the (hassles) are just the same. '''

def mistake():
    # Dropping your phone, in excrutiating detail and anger, sadness, hoplessness.
    '''This has to be the absolute most (horrifying) thing that has ever happened to me. As I was walking home from the (bus stop), I thought the day was pretty (normal) -- (boring) even. The (wind) was (blowing) and the (sky) was (getting darker) by the minute. I had just gotten off work and it had been a very busy day, filled with (gossip) and (tension). Needless to say, I was (exhausted) and (happy) to be on the last leg of my journey home. If only I could have the power of (premontion), cause then I wouldn't have done what I was about to do next. Sigh, I really am such a (dumb ass). As the elation of getting off of my (awful) job hit me at the same time as a kick ass song on my Spotify playlist, I started to (shake it) on the walk home. Getting more and more into my (dancing) and (dance moves), I really started to (vigorously) shake my (arms) and (twirl around). Well, I should've remembered that I was wearing the awful pair of (jeans), the ones with the girl pockets so (small) I can barely fit a (penny) inside. My final turn left me with my (eyes) wide open as I saw my (phone) fly out of my pocket, almost like it had (wings), and arc through the (sky) to land, face-first, on a (huge) (rock) in the middle of the (road). I felt my heart stop, a (tear) stinged the corner of my (eye), and I rushed to pick up (my baby) only to be (dissapointed) when I found the (screen) shattered to bits. The only thing left to do was to utter, "I've made a huge mistake..." and (cry) on the rest of my walk home.'''


def main():
    # Increase run time so that the program goes for as long as it should.

    # Greeting complete with menu print out.

    # Once user selects a story, for loop looping through the parts of speech list.
    # for word in parts of speech: input("Enter a" + word) or however you can do this.
    # Store inputs in a new list to call when returning the story.
    # Return the story with the user's inputs (something indicating where they are, parentheses or quotations or something) in a way that seems like the computer is reading it to you and they are actually a human.


if __name__ == "__main__":
    main()
# Ibrose.github.io
NUGU pokemon recommendation program for kids
Members: 
JungJunHo, Department of Information Systems, wryyyyy0525@naver.com
KyuSubHwang, Information department, kyusubhwang@hanyang.ac.kr
Millet Clemence, Electronic engineering, clemence.millet@edu.devinci.fr

I. Introduction
- Motivation: Why are you doing this?
1. Kids like someone else agreeing their opinions. Also, SKT made nugu limited pokemon version, so there will be many pokemon fans who bought NUGU. Besides, those who bought NUGU and use service for kids usually will be a pokemon fan, because many kids like pokemon.
2. While listening to SKT lectures, there were mentions that NUGU services kid content(pink-pong & pokemon) and my younger cousin mentioned that ‘there is a pokemon popularity vote and you should apply it’. So I made this suggestion.
- What do you want to see at the end?
NUGU uses previous reply data and groups pokemon according to its data, and answer based on this data.

II. Datasets
- Describing your dataset
The recommendation algorithm will use Pokémon data which has dexnum, name, poppoint, wellknown, legendary, recent, sets, gen, prime, destype values. Each column is as follows:

Dex: pokedex number of pokemon

Name: name of pokemon(in Korean), the part where NUGU will actually speak.

Poppoint: the popularity point, which will be used in decision. This value can be incremented, by user’s reply.

Wellknown: is the pokemon well known or not. 1: Well-known, 0: Not well-known. Wellknown cases are those which are popular: Pikachu. Eevee, Snorlax, Charizard or so on, which even non-fans know.

Legendary: is the pokemon legendary or not. 1: yes, 0: No.

Recent: Is the pokemon appeared in recent games, for 4 years? 1: yes, 0: no.

Sets: The evolving tree of pokemon. Same number, same group(ex: set 2 파이리-리자드-리자몽)

Gen: pokemon generation, 1 to 8.

Prime: The well known pokemon in its evolution tree. 1: Those pokemon will be used in the reply. 0: not used in reply, Only when there is a name in the previous replies. If there was a name in the reply, the value becomes 1.

Destype: Type of design, total 17, which is:
Long: Long shape, similar as a snake.
Ghost: ghost like pokemon
Mineral: Rock/Steel like pokemon, motive from minerals.
Dragon: Dragon motive pokemon.
Bug: Bug like pokemon.
Bird: bird like pokemon
Fish: Fish like pokemon, or whales. 
Marine: Marine objects, invertebrate animal motives.
Water: Water-related pokemon, excluding fish and marine cases below.
Cute: Cute and adorable pokemon, such as Pikachu.
Humanoid: Somewhat similar to human.
Monster: Designed somewhat like unrealistic monster.
Grass: Grass, tree, fruit motive pokemon.
Catlike: Cat like pokemon, or Felidae animals(tiger, lion, etc) pokemon
Doglike: Dog like pokemon, or canine animals(wolf, fox, etc) pokemon
Animal: Animal(in real life) pokemon, excluding catlike, doglike.
Amorph: Something like mud, liquid like, which does not have fixed shape.

Value of Poppoint: we will use 2 data, one is the popularity vote done by Pokémon Korea, which chooses top 10 of each generation. The other is the popularity vote to choose POTY, done by Pokémon Company. Both of which are official vote. For each top 10 of Pokémon Korea vote, we put scores per each rate: top 1 gets 10 points, top 2 gets 9 points, till top 10 gets 1 point. There are several pokemon who has multiple forms and get multiple ranks, in this case, we decreases the point to half except its highest rank. For example, if one got top 3, top 5, and top 7, it gets 8 +6(/2) +4(/2) =13. For the POTY vote result, similar to the before the score will be divided according to the score, but the POTY point will be decreased to half, round up under 0. For example, top 1 and top 2 gets 15 points, top 3 and 4 gets 14 points, till top 29 and 30 gets 1 point. I will add two data and divide by half(round up under 0) For example, if one got top 3, top 5, and top 7, it gets 8 +6(/2) +4(/2) =13, and got top 1 in POTY, the final score is (13 + (30/2)) /2 = 14.

III. Methodology
- Explaining your choice of algorithms (methods)
What we will use: collaborative filtering algorithm, decision tree algorithm.
- Explaining features or code (if any)
Nugu replies by answering questions below, as a decision tree.
1) Which design type does user likes most(using destype)?
2) Which generation does the user likes most? (1,2,3,4,5,6,7,8)
 Unlike the others, the recommendation algorithm recommends those that are in different generation, because kids are likely to know about their most-like generations. Priority: 2-4-5-6-3-7-1-8
3) Does the user like well-known pokemon?
4) Does the user like legendary pokemon?
5) Does the user like recent pokemon?
After all those questions, it makes suggestions that matches those and with highest poppoint values, by decision tree algorithm. 
By talking with user, NUGU changes the popularity list by giving points to the answered pokemon.
There is a list, which saves user’s reply, up to 20 and erases the oldest if it is over 20. If the user reply is over 3, NUGU starts reply with pokemon that is similar to the user’s reply. This is to increase the correctness of collaborative filtering algorithm, to prevent cold start problems.

IV. Evaluation & Analysis
- Graphs, tables, any statistics (if any)

V. Related Work (e.g., existing studies)
- Tools, libraries, blogs, or any documentation that you have used to do this project.

VI. Conclusion: Discussion
according to those.

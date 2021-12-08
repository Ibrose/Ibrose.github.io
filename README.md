# Ibrose.github.io
**NUGU Pokemon Recommender for kids**   

[Result video](https://youtu.be/byCFJoSztUE)

Collaborators:

Junho Jung, Department of Information Systems, <wryyyyy0525@naver.com>

Kyusub Hwang, Department of Information Systems, <kyusubhwang@hanyang.ac.kr>

Millet Clemence, Department of Electronic engineering, <clemence.millet@edu.devinci.fr>


# CONTENTS
I. Introduction	 

>1.	Motivation: Why are you doing this?

>2.	Goal: What do you want to see at the end?	 

II. Datasets	

>1.	Dataset description	

III. Methodology	

>1.	Algorithm explanation	

>2.	Code Explanation	 

>3.	NUGU play builder	

IV. Evaluation & Analysis	 

>1.	Data Analysis	 

>2.	Prediction Model	

>3.	Accuracy Estimation	

V. Related Work	 

VI. Conclusion	 



# I. Introduction
## 1. Motivation: Why are you doing this?
>1. Kids like someone else agreeing their opinions. Also, SKT made nugu limited pokemon version, so there will be many pokemon fans who bought NUGU. Besides, those who bought NUGU and use service for kids usually will be a pokemon fan, because many kids like pokemon.

>2. While listening to SKT lectures, there were mentions that NUGU services kid content(pink-pong & pokemon) and my younger cousin mentioned that ‘there is a pokemon popularity vote and you should apply it’. So I made this suggestion.

## 2. Goal: What do you want to see at the end?
>NUGU uses previously sorted data and checks cosine similarity of pokemon according to its data, and answer based on this data.



# II. Datasets
## 1. Dataset description
The recommendation algorithm will use Pokémon data which has dexnum, name, poppoint, wellknown, legendary, recent, sets, gen, prime, destype values. All of those are the data which is used in official pokemon site. Each column is as follows:

- Dex: pokedex number of pokemon
- Name: name of pokemon(in Korean), the part where NUGU will actually speak.
- Poppoint: the popularity point, which will be used in decision. This value can be incremented, by user’s reply.
    - Value of Poppoint: we will use 2 data, one is the popularity vote done by Pokémon Korea, which chooses top 10 of each generation. The other is the popularity vote to choose POTY, done by Pokémon Company. Both of which are official vote. For each top 10 of Pokémon Korea vote, we put scores per each rate: top 1 gets 10 points, top 2 gets 9 points, till top 10 gets 1 point. There are several pokemon who has multiple forms and get multiple ranks, in this case, we decreases the point to half except its highest rank. For example, if one got top 3, top 5, and top 7, it gets 8 +6(/2) +4(/2) =13. For the POTY vote result, similar to the before the score will be divided according to the score, but the POTY point will be decreased to half, round up under 0. For example, top 1 and top 2 gets 15 points, top 3 and 4 gets 14 points, till top 29 and 30 gets 1 point. I will add two data and divide by half(round up under 0) For example, if one got top 3, top 5, and top 7, it gets 8 +6(/2) +4(/2) =13, and got top 1 in POTY, the final score is (13 + (30/2)) /2 = 14. 
- Wellknown: is the pokemon well known or not. 1: Well-known, 0: Not well-known. Wellknown cases are those which are popular: Pikachu. Eevee, Snorlax, Charizard or so on, which even non-fans know.
- Legendary: is the pokemon legendary or not. 1: yes, 0: No.
- Recent: Is the pokemon appeared in recent games, for 4 years? 1: yes, 0: no.
- Sets: The evolving tree of pokemon. Same number, same group(ex: set 2 파이리-리자드-리자몽)
- Gen: pokemon generation, 1 to 8.
- Prime: The well known pokemon in its evolution group. 1: It is well known. 0: It isn’t. To be exact, I set those which are the lowest of each evolution group and below top 500 of POTY popularity vote.
- Destype: Type of design, total 17, all from pokemon data files in pokemon game, which is:
    1. Long: Long shape, similar as a snake.
    2. Ghost: ghost like pokemon
    3. Mineral: Rock/Steel like pokemon, motive from minerals.
    4. Dragon: Dragon motive pokemon.
    5. Bug: Bug like pokemon.
    6. Bird: bird like pokemon
    7. Fish: Fish like pokemon, or whales. 
    8. Marine: Marine objects, invertebrate animal motives.
    9. Water: Water-related pokemon, excluding fish and marine cases below.
    10. Cute: Cute and adorable pokemon, such as Pikachu.
    11. Humanoid: Somewhat similar to human.
    12. Monster: Designed somewhat like unrealistic monster.
    13. Grass: Grass, tree, fruit motive pokemon.
    14. Catlike: Cat like pokemon, or Felidae animals(tiger, lion, etc) pokemon
    15. Doglike: Dog like pokemon, or canine animals(wolf, fox, etc) pokemon
    16. Animal: Animal(in real life) pokemon, excluding catlike, doglike.
    17. Amorph: Something like mud, liquid like, which does not have fixed shape.

We originally saved data as string, but since it didn’t fit in to cosine similarity easily, so we changed it to int value, to calculate easier. The number is a number in front of each design type (ex: Amorph: saved it as 17)







# III. Methodology
## 1. Algorithm explanation
We made pokedata.csv file, where we save all those pokemon data. We will use those data to get similar pokemon and reply back.

What we will use to calculate similarity: Cosine Similarity

Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. It is often used to measure document similarity in text analysis. (Jiawei Han, Jian Pei, in Data Mining, 2012)
<img src="https://user-images.githubusercontent.com/81448385/144530339-aa475a48-9455-499c-b8ab-be6bc496cae7.png"/>
<img src="https://user-images.githubusercontent.com/81448385/144530541-df45fbe3-42b3-422e-a3fc-2494f7e20e3c.png"/>

Nugu uses all those data above, to check pokemon with similar data as input pokemon. It gets pokemon data in csv file and save it as data. And it gets the ‘name’ column of data, where the name of every pokemon is saved. In the poke\_recommend function, it calculates cosine similarity of the input and 898 pokemon’s data, from third column to the last (poppoint, wellknown, legendary, recent, sets, gen, prime, destype) by using cos\_sim function and save it into list poke\_sim. In the poke\_sim[0], it saves names of pokemon, and in poke\_sim[1], it saves cosine similarities. After it is done, we sort it according to poke\_sim[1], by using ‘key = lambda x: x[1]’. Also, we want the bigger similarities to come first so we set reverse = True. To get three pokemon that has highest similarity, we save pokelist[pokesim[1][0]], pokelist[pokesim[2][0]], pokelist[pokesim[3][0]], and save it as poke\_out. We do not get pokelist[pokesim[0][0]] since it will be the input pokemon itself. So we save those three in poke\_ret[0] and cosine similarities (poke\_sim) in poke\_ret[1] and return poke\_ret.

<img src="https://user-images.githubusercontent.com/81448385/144530631-cdcbed2f-28e3-4871-a419-67312b624c40.png"/>
For example, this is the result of similar pokemon of Bulbasaur(이상해씨), we got 6 pokemon names and made it as graph. We will get top 3 most similar pokemon and return to NUGU and say it. 

## 2. Code Explanation
<img src="https://user-images.githubusercontent.com/81448385/144530776-710ed075-6c46-40c5-9788-65271a6a4384.PNG"/>
In this part, we get pokedata.csv file and save it as data. Also, we get the name values in data and make it as pokelist.

<img src="https://user-images.githubusercontent.com/81448385/144530869-2b70618b-26b8-4a57-8cea-ab299720bfe4.PNG"/>
In this class arceus, we get json request, get what we want, and reply back as json. The def \_\_init\_\_ is used like that since it is needed. The get method is the actual function. It gets the request from NUGU. It gets body of request, encoding it to utf-8(to read Korean languages) and save it as pokemob. To get the actual value of requested pokemon name, we get pokemob[‘action’][‘parameters’][‘pokemonname’(this part value is named as pokemonname in play Builder, so we use so’)][‘value’] and save it to pokemonname. We input this value to poke\_reommend and get recommendation and save it to pokereply. By using response\_builder, we make the reply and JsonResponse it, to make it as json and reply back to NUGU.





## 3. NUGU play builder 

<img src="https://user-images.githubusercontent.com/81448385/144530967-19bf3eb9-995c-4fd4-9e9c-24ba97231100.PNG"/>
This is the total structure of our tree. By pokestart, NUGU starts the program. Using answer.pokemon NUGU asks the user to say the pokemon one likes, and according to reply, if it is correct input it goes to pokeinput and reply back, but if it is wrong, it goes to errorcase.

<img src="https://user-images.githubusercontent.com/81448385/144531061-06b7fa7a-ad26-4799-8212-9bcd904a6f65.PNG"/>
<img src="https://user-images.githubusercontent.com/81448385/144531069-76e3d823-adec-4574-b1fa-1ff22b715d48.PNG"/>
In pokestart, it gets user comment like ‘start the pokemon recommender’ and similar sentences, which has the poketalk entity, which is pokemon. And for user’s pokemon name input, I set pokename and Nameopoke, both are the 898 names of pokemon.

<img src="https://user-images.githubusercontent.com/81448385/144531291-f06c2b50-b8ac-460a-bea3-611dcfa588c1.PNG"/>
In the pokeinput, I set the sending data as pokemonname, which is the user’s input nameopoke. 

<img src="https://user-images.githubusercontent.com/81448385/144531297-8a09b96e-8c85-4d0c-9ca2-787d5b005d15.PNG"/>
For reply, we used backend proxy, and set backend parameters pokereply1, pokereply2, pokereply3, all of those are reply from backend server.

For this part, we made responding sentence using backend parameters to reply, so our reply example are like following:

<img src="https://user-images.githubusercontent.com/81448385/144531469-1f7e97b2-df86-490e-897b-72d8d90793c0.PNG"/>
<img src="https://user-images.githubusercontent.com/81448385/144531462-6257df01-4622-486d-8621-bfdc498034c4.PNG"/>



# IV. Evaluation & Analysis
## 1. Data Analysis
<img src="https://user-images.githubusercontent.com/81448385/144531652-9576dc7a-6afa-4c14-8bf0-18cac2e285fd.png"/>
Scatter plot was used to observe relationships between input pokemon(x-axis) and output pokemon(y-axis) which had the second largest cosine similarity values (Since the first was the input pokemon itself, it was not considered). 
## 2. Prediction Model
<img src="https://user-images.githubusercontent.com/81448385/144531667-d693b9c5-0de2-4102-9be2-da4bfd0926a9.png"/>
As the raw scatter plot seemed to have linear correlation, we created linear regression neuron based on gradient descent to create a prediction model. The neuron tries to find out the optimum linear function that could explain the linear correlation between pokemons. By passing index of input pokemon and output pokemon, the neuron works as follows:

<img src="https://user-images.githubusercontent.com/81448385/144531869-1caab20a-e7c0-476f-99ce-7b9525e1eef8.png"/>

1. Init(): initiation of weight and bias to 1.0
1. Forpass(): For all samples, calculate y\_hat(prediction value) which is derived from w\*x+b
1. Backprop(): To reduce the error between actual y value and predicted y\_hat value, backpropagation with a loss function which updates gradients of weight and bias is used. 

 Loss function used:    
<img src="https://user-images.githubusercontent.com/81448385/144532004-894bf6ed-37c9-4cb8-b5d9-460fbf31feb4.png"/>


1. Fit(): first calls forpass() to calculate y\_hat and error, then calls backprop() to get gradients of weights and bias. Finally update neuron’s weight and bias. This is an iteration process over arbitrarily set epochs.


## 3. Accuracy Estimation

We made a reference to Precision model to calculate accuracy of our recommendation system. The precision model is one of the models to evaluate efficiency of recommendation systems   
<img src="https://user-images.githubusercontent.com/81448385/145175492-2a337ceb-45ee-42da-95ee-10d5906a931b.png"/>   

Based on the Linear Equation derived from the Linear Regression using gradient descent, we assign ‘True’ if the y hat value of the equation is inside a set which consists of 3 pokemon with highest cosine similarities and ‘False’ otherwise. Therefore, accuracy can be measured by True divided by Total case. 
<img src="https://user-images.githubusercontent.com/81448385/145175824-f9c6f560-108f-4310-98b1-be1390fe7a9b.png"/>   
In each epoch, forpass() and backpropagation() repeatedly updates weight and bias and recalculates the accuracy accordingly. Based on updated linear regression model, the accuracy started off 10% but somehow decreased to 5%. It seems that linear regression model shows its limits to properly reflect our dataset.   



# V. Related Work
\- Tools, libraries, blogs, or any documentation that you have used to do this project.

Place where I get Pokémon data:

<https://pokemon2020.pokemon.com/en-us/>

<https://pokemonkorea.co.kr/pokemon_25th/menu118>

Data analysis, Prediction, Accuracy estimation learned from:    
Data Mining, 2012 Jiawei Han, Jian Pei

# VI. Conclusion
데모 동영상   
[Result video](https://youtu.be/byCFJoSztUE)


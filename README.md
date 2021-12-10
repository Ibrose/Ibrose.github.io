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

>3.	NUGU backend server	

IV. Evaluation & Analysis	 

>1.	Data Analysis	 

>2.	Prediction Model	

>3.	Accuracy Estimation	

V. Related Work	 

VI. Conclusion	 



# I. Introduction
## 1. Motivation: Why are you doing this?
>1. Kids like giving their opinions on what they like, and we thought it could be fun to make them exchange with the NUGU speaker about a topic they like. Also, SKT made a limited edition of a Pokémon NUGU speaker, so obviously Pokémon fans who buy this NUGU speaker edition would be interested in our product. Besides, because many kids like Pokémon, parents who would buy NUGU would be much likely to use our service for their kids.

>2. While listening to SKT lectures, there was a mention about NUGU services for kids, for example ping-pong and Pokémon. Jung Jun Ho also said that his little cousin mentioned a Pokémon popularity vote and said it would be fun to use it in our AI project. So, this is how the idea came.

## 2. Goal: What do you want to see at the end?
>We would like NUGU speaker to be able to recommend to the user a Pokémon that he could like based on its preferences.



# II. Datasets
## 1. Dataset description
The recommendation algorithm will use Pokémon data which has dexnum, name, poppoint, wellknown, legendary, recent, sets, gen, prime, destype values. All of those are the data which is used in official pokemon game data. Here is the explanation of each parameter:

- dexnum: pokedex number of pokemon
- name: name of pokemon(in Korean), the part where NUGU will actually speak.
- poppoint: the popularity point, which will be used in decision. 
    - Value of Poppoint: we will use 2 data, one is the popularity vote done by Pokémon Korea, which chooses top 10 of each generation. The other is the popularity vote to choose POTY, done by Pokémon Company. Both are official vote. For each top 10 of Pokémon Korea vote, we give a certain score that corresponds to the rating of each Pokémon: the 1st gets 10 points, the 2nd gets 9 points, till the 10th gets 1 point. The rest gets 0 points. There are several Pokémons that can be found in multiple forms and multiple ranks, in these cases, we reduce the number of points by half for these different forms and ranks. For the POTY vote result, the 1st and 2nd get 15 points, the 3rd and 4th get 14 points … and the 29th and 30th get 1 point. Finally, the total score of a Pokémon is the average of the 2 scores given by each vote. 
- wellknown: is the pokemon well known or not. 1: Well-known, 0: Not well-known. Well-known Pokémons are the most popular ones Pikachu. Eevee, Snorlax, Charizard... Those that even non-fans know.
- legendary: the Pokémon gets 1 point if it is a legendary Pokémon, otherwise it gets 0 points.
- recent: the Pokémon gets 1 point if it appeared for the first time in games during the last 4 years, otherwise it gets 0 points.
- sets: Pokémons can be part of an evolving tree. If Pokémons are in the same group, they get the same number (ex: set 2 파이리-리자드-리자몽)
- gen: the Pokémon’s generation, goes from 1 to 8
- prime: in one same evolution group the well-known Pokémons get 1 point, those are the ones that are in the top 500 of the POTY popularity vote.
- destype: type of design, there are 17 in total :
    1. Long: Long shape, similar as a snake.
    2. Ghost: ghost like pokemon
    3. Mineral: Rock/Steel like pokemon, motive from minerals.
    4. Dragon: Dragon motive pokemon.
    5. Bug: Bug like pokemon.
    6. Bird: bird like pokemon
    7. Fish: Fish like pokemon, or whales. 
    8. Marine: Marine objects, invertebrate animal motives.
    9. Water: Water-related pokemon, excluding fish and marine cases above.
    10. Cute: Cute and adorable pokemon, such as Pikachu.
    11. Humanoid: Somewhat similar to human.
    12. Monster: Designed somewhat like an unrealistic monster.
    13. Grass: Grass, tree, fruit motive pokemon.
    14. Catlike: Cat like pokemon, or Felidae animals(tiger, lion, etc) pokemon
    15. Doglike: Dog like pokemon, or canine animals(wolf, fox, etc) pokemon
    16. Animal: Animal(in real life) pokemon, excluding catlike, doglike.
    17. Amorph: Something like mud, liquid like, which does not have fixed shape.
    
We originally saved data as string, but we changed it to int values because it is easier to work with when using cosine similarity. The number each number corresponds to a design type (ex: Amorph: saved it as 17)







# III. Methodology
## 1. Algorithm explanation
We made pokedata.csv file, where we save all those pokemon data. We will use this data to look for a Pokémon similar to the one given by the user.

What we will use to calculate similarity: Cosine Similarity

Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. It is often used to measure document similarity in text analysis. (Jiawei Han, Jian Pei, in Data Mining, 2012)
<img src="https://user-images.githubusercontent.com/81448385/144530339-aa475a48-9455-499c-b8ab-be6bc496cae7.png"/>
<img src="https://user-images.githubusercontent.com/81448385/144530541-df45fbe3-42b3-422e-a3fc-2494f7e20e3c.png"/>

Nugu uses all those data above, to check pokemon with similar data as input pokemon. In the poke_recommend function, it calculates cosine similarity of every Pokémon’s data, but it uses only the data from the third column to the last one (poppoint, wellknown, legendary, recent, sets, gen, prime, destype), using cos_sim function and saving it into a list, poke_sim. In the poke_sim[0], it saves names of Pokémon, and in poke_sim[1], it saves cosine similarity values. After this is done, we sort the list according to poke_sim[1], by using ‘key = lambda x: x[1]’. Also, we want the bigger similarities to come first, so we set reverse = True. To get the three Pokémon that has the highest similarity, we save pokelist[pokesim[1][0]], pokelist[pokesim[2][0]], pokelist[pokesim[3][0]], and save it as poke_out. We do not save pokelist[pokesim[0][0]] since it will be the input Pokémon itself. So we save those three in poke_ret[0] and their cosine similarities (poke_sim) in poke_ret[1] and return poke_ret.

<img src="https://user-images.githubusercontent.com/81448385/144530631-cdcbed2f-28e3-4871-a419-67312b624c40.png"/>
For example, this is the result of similar pokemon of Bulbasaur(이상해씨), we got 6 pokemon names and made it as graph. We will get top 3 most similar pokemon and return to NUGU and say it. 

## 2. Code Explanation
<img src="https://user-images.githubusercontent.com/81448385/144530776-710ed075-6c46-40c5-9788-65271a6a4384.PNG"/>
In this part, we get pokedata.csv file and save it as data. Also, we get the name values in data and make it as pokelist.

<img src="https://user-images.githubusercontent.com/81448385/144530869-2b70618b-26b8-4a57-8cea-ab299720bfe4.PNG"/>
In this class arceus, we get json request, get what we want, and reply back as json. The def \_\_init\_\_ is used like that since it is needed. The get method is the actual function. It gets the request from NUGU. It gets body of request, encoding it to utf-8(to read Korean languages) and save it as pokemob. To get the actual value of requested pokemon name, we get pokemob[‘action’][‘parameters’][‘pokemonname’][‘value’] and save it to pokemonname. We input this value to poke\_reommend and get recommendation and save it to pokereply. By using response\_builder, we make the reply and JsonResponse it, to make it as json and reply back to NUGU.





## 3. NUGU backend server 

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
   2. Forpass(): For all samples, calculate y\_hat(prediction value) which is derived from w\*x+b
   3. Backprop(): To reduce the error between actual y value and predicted y\_hat value, backpropagation with a loss function which updates gradients of weight and bias is used.   
 Loss function used:    
<img src="https://user-images.githubusercontent.com/81448385/144532004-894bf6ed-37c9-4cb8-b5d9-460fbf31feb4.png"/>
   4. Fit(): first calls forpass() to calculate y\_hat and error, then calls backprop() to get gradients of weights and bias. Finally update neuron’s weight and bias. This is an iteration process over arbitrarily set epochs.


## 3. Accuracy Estimation

We made a reference to Precision model to calculate accuracy of our recommendation system. The precision model is one of the models to evaluate efficiency of recommendation systems   
<img src="https://user-images.githubusercontent.com/81448385/145175492-2a337ceb-45ee-42da-95ee-10d5906a931b.png"/>   

Based on the Linear Equation derived from the Linear Regression using gradient descent, we assign ‘True’ if the y hat value of the equation is inside a set which consists of 3 pokemon with highest cosine similarities and ‘False’ otherwise. Therefore, accuracy can be measured by True divided by Total case. 
<img src="https://user-images.githubusercontent.com/81448385/145533562-462a728b-c082-40a1-86fe-6890dbcd8986.PNG"/>   
In each epoch, forpass()and backpropagation() repeatedly updates weight and bias, recalculating prediction and accuracy. The accuracy started as 1% and grows to 16% after 10 epochs



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


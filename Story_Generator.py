import random as r


sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time', 'Long ago', 'In']
  
character = [' there lived a king.', ' there was a man named Jack.', ' there lived a farmer.']
  
time = [' One day', ' One full-moon night', 'In the first day of the second week from the last of four weeks of Autumn,']
  
story_plot = [' he was passing by', ' he was going for a picnic to', ' he was going to a nearby market', ' he was sleeping under the longest of the apple tree in', 'in his dream about ']
  
place = [' the mountains', ' the garden', ' the village', ' near the long flowing river']
  
second_character = [' he saw a man', ' he saw a young lady', 'he saw a purple ox', 'he saw a Holy cow', 'he brown pursian rabbit']
  
age = [' who seemed to be in late 20s', ' who seemed very old and feeble', ' who seems to be immortal']
  
work = [' searching something.', ' digging a well on roadside.', 'digging the grave for her late goat.', ' plucking grasses among the flowers.', ' finding the meaning of the life']

sentence_ending =[' Therefore, he ran away.', ' So, he started eating rocks.', ' So, He started dancing.', ' So, he started solving the multi-dimentional vector product of the derivates of the logarithmic inverse function of the pi over the modulo of 93!.' ]

if __name__ == "__main__":

    s = r.choice(sentence_starter)+r.choice(character)+\
        r.choice(time)+r.choice(story_plot)+\
     r.choice(place)+r.choice(second_character)+\
    r.choice(age)+r.choice(work)+r.choice(sentence_ending)

    print(s)


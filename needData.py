import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def timefunc(interval_col):#translate time string to int
    h = []
    for hours in interval_col:
        if(hours == "0-1 hours"):
            h.append(0)
        elif(hours == "1-2 hours"):
            h.append(1)
        elif(hours == "2-3 hours"):
            h.append(2)
        elif(hours == "3-4 hours"):
            h.append(3)
        elif(hours == "4-5 hours"):
            h.append(4)
        elif(hours == "5-6 hours"):
            h.append(5)
        elif(hours == "6+ hours"):
            h.append(6)
        else:
            h.append(0)
    return h

def timefunc2(interval_col):
    h=[]
    for hours in interval_col:
        if hours == "0 hours":
            h.append(0)
        elif hours == "1 hours" or hours == "1 hour":
            h.append(1)
        elif hours == "2 hours":
            h.append(2)
        elif hours == "3 hours":
            h.append(3)
        elif hours == "4 hours":
            h.append(4)
        elif hours == "5 hours":
            h.append(5)
        elif hours == "6+ hours":
            h.append(6)
        else:
            h.append(0)
    return h


def childRankFunc(interval_col): #translates string(ex."not much like my child") to a number
    h = []
    for answer in interval_col:
        if answer == "Very much like my child":
            h.append(1)
        elif(answer == "Mostly like my child"):
            h.append(2)
        elif(answer == "Somewhat like my child"):
            h.append(3)
        elif(answer == "Not much like my child"):
            h.append(4)
        elif answer == "Not like my child":
            h.append(5)
        else:
            h.append(0)
    return h

def yesNoFunc(interval_col):
    h=[]
    for answer in interval_col:
        if answer == "No":
            h.append(1)
        elif answer == "Yes":
            h.append(2)
        else:
            h.append(0)
    return h

df = pd.read_csv("curiosity.csv")#read/load data
#print(df)


df["ExperiencesInt"]=childRankFunc(df["Everywhere my child goes, he/she is out looking for new things or experiences."])
df["ImitationInt"]=yesNoFunc(df["My child tries to be like the people around him/her."])
df["AttentionInt"]=childRankFunc(df["Most of the time, my child does not pay attention to what he/she is doing."])
df["CasualityInt"]=childRankFunc(df["My child does not notice the effects of his/her actions until it’s too late."])
df["MistakesInt"]=childRankFunc(df["My child learns from his/her mistakes."])
df["SeekInfoInt"]=childRankFunc(df["My child actively seeks as much information as he/she can in new situations."])
df["FrighteningInt"]=childRankFunc(df["My child likes to do things that are a little frightening."])
df["UnpredictableInt"]=childRankFunc(df["My child prefers activities that are excitingly unpredictable."])
df["CarefulInt"]=childRankFunc(df["My child thinks a lot about how he/she is doing."])
df["ExploringInt"]=childRankFunc(df["My child is always looking for experiences that challenge how he/she thinks about themselves and the world."])
df["PeerSimilarityInt"]=childRankFunc(df["My child’s behavior is similar to that of his/her friends."])
df["ChallengeInt"]=childRankFunc(df["My child views challenging situations as an opportunity to grow and learn."])
df["ConsequenceInt"]=childRankFunc(df["My child usually judges what he/she is doing by the consequences of his/her actions."])
df["UnfamiliarInt"]=childRankFunc(df["My child is the kind of person who embraces unfamiliar people, events, and places."])
df["GrowUpInt"]=childRankFunc(df["My child knows who he/she wants to be."])
df["PunishmentInt"]=childRankFunc(df["My child does not learn well from punishment."])
df["ComplexInt"]=childRankFunc(df["My child is at his/her best when doing something that is complex or challenging."])
df["ObvliousInt"]=childRankFunc(df["Often my child does not notice what he/she is doing until someone calls it to his/her attention."])
df["UncertaintyInt"]=childRankFunc(df["My child is the type of person who really enjoys the uncertainty of everyday life."])
df["StandardsInt"]=childRankFunc(df["My child has personal standards, and tries to live up to them."])
df["SweetsInt"]=childRankFunc(df["It’s hard for my child to notice when he/she has had enough (food or sweets)."])
df["ProgressInt"]=childRankFunc(df["My child usually keeps track of his/her progress toward his/her goals."])
df["NotOvereatInt"]=childRankFunc(df["My child is usually careful not to overdo it when working, eating, drinking."])
df["SelfConciousInt"]=childRankFunc(df["My child thinks a lot about what other people think of him/her."])
df["ComparingInt"]=childRankFunc(df["My child tends to compare himself/herself with other people."])
df["SimiliarBehaviorInt"]=childRankFunc(df["My child’s behavior is not that different from other people’s."])
df["IndifferentInt"]=childRankFunc(df["My child does not care if he/she is different from most people."])
df["SeekChallengeInt"]=childRankFunc(df["My child frequently seeks out opportunities or situations to challenge themselves and grow as a person."])
df["ElectronicsInt"]=timefunc2(df["On average, how much time per day does your child spend using electronics (such as television, computers, etc.)?"])
df["HomeworkInt"]=timefunc2(df["On average, how much time per day does your child spend on his/her schoolwork?"])


print(df)
plt.show()


"""plt.hist(df["Siblings"])
nsib = df["Siblings"].values
print(np.mean(nsib))
print(np.median(nsib))
print(np.std(nsib))

df["QualityTimeInt"]=timefunc(df["QualityTime"])
df["SchoolWorkTimeInt"]=timefunc(df["SchoolWorkTime"])
df["ElectronicInt"]=timefunc(df["Unnamed: 14"])
plt.scatter(df["QualityTimeInt"], df["SchoolWorkTimeInt"])"""


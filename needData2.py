import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import csv

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
        elif hours == "1 hour" or hours == "1 hours":
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
            h.append(2)
        elif(answer == "Mostly like my child"):
            h.append(1)
        elif(answer == "Somewhat like my child"):
            h.append(0)
        elif(answer == "Not much like my child"):
            h.append(-1)
        elif answer == "Not like my child":
            h.append(-2)
        else:
            h.append(0)
    return h

def yesNoFunc(interval_col):
    h=[]
    for answer in interval_col:
        if answer == "No":
            h.append(-1)
        elif answer == "Yes":
            h.append(1)
        else:
            h.append(0)
    return h


df = pd.read_csv("hopeLutheranChurchSurvey.csv")#read/load data

df["Grade"]=df["Grade"]
df["SiblingsInt"]=df['How many siblings does your child have that live at home?']
df["GetAlongInt"]=df["If your child has siblings, how well do they get along?"]
df["FriendlinessInt"]=df["How well does your child get along with other children of their age, whether at camp or at school?"]
df["One-OneInt"]=timefunc2(df["On average, how much time per day do you spend with your child for one-on-one activities?"])
df["TimeSchoolworkInt"]=timefunc2(df["On average, how much time per day does your child spend on his/her schoolwork?"])
df["ElectronicTimeInt"]=timefunc2(df["On average, how much time per day does your child spend using electronics (such as television, computers, etc.)?"])
df["HardWorkerInt"]=childRankFunc(df["My child is a hard worker."])
df["HappyInt"]=childRankFunc(df["My child remains unaffected when someone close to him/her is happy."])
df["MoodsInt"]=childRankFunc(df["My child is “in tune” with other people’s moods."])
df["FocusInt"]=childRankFunc(df["My child has difficulty maintaining his/her focus on projects that take more than a few months to complete."])
df["ExcitementInt"]=childRankFunc(df["When someone else is feeling excited, my child tends to get excited too."])
df["SetbacksInt"]=childRankFunc(df["Setbacks don’t discourage my child. He/She does not give up easily."])
df["CompletionInt"]=childRankFunc(df["My child finishes whatever he/she begins."])
df["DodgingInt"]=childRankFunc(df["When a friend starts to talk about his/her problems, my child tries to steer the conversation towards something else."])
df["DistractedInt"]=childRankFunc(df["New ideas and projects sometimes distract my child from previous ones."])
df["InterestsInt"]=childRankFunc(df["My child's interests change from year to year."])
df["DifferentGoalsInt"]=childRankFunc(df["My child often sets a goal but later chooses to pursue a different one."])
df["ApatheticInt"]=childRankFunc(df["My child does not feel sympathy for people who cause their own serious illnesses."])
df["OvercomeSetbacksInt"]=childRankFunc(df["My child has overcome setbacks to conquer an important challenge."])
df["EmpathyInt"]=childRankFunc(df["My child can tell when others are sad even when they do not say anything."])
df["DiligenceInt"]=childRankFunc(df["My child is diligent. He/She never gives up."])
df["LostFocusInt"]=childRankFunc(df["My child has been obsessed with a certain idea or project for a short time but later lost interest."])
df["KindnessInt"]=childRankFunc(df["My child enjoys making other people feel better."])
df["ConcernInt"]=childRankFunc(df["My child has tender, concerned feelings for people less fortunate than him/her."])
df["RespectInt"]=childRankFunc(df["It upsets my child to see someone being treated disrespectfully."])
df["MisfortunteInt"]=childRankFunc(df["Other people’s misfortunes do not disturb my child a great deal."])


df2=pd.read_csv("curiosity.csv")
df2["Grade"]=df2["Grade"]
df2["ExperiencesInt"]=childRankFunc(df2["Everywhere my child goes, he/she is out looking for new things or experiences."])
df2["ImitationInt"]=yesNoFunc(df2["My child tries to be like the people around him/her."])
df2["AttentionInt"]=childRankFunc(df2["Most of the time, my child does not pay attention to what he/she is doing."])
df2["CasualityInt"]=childRankFunc(df2["My child does not notice the effects of his/her actions until it’s too late."])
df2["MistakesInt"]=childRankFunc(df2["My child learns from his/her mistakes."])
df2["SeekInfoInt"]=childRankFunc(df2["My child actively seeks as much information as he/she can in new situations."])
df2["FrighteningInt"]=childRankFunc(df2["My child likes to do things that are a little frightening."])
df2["UnpredictableInt"]=childRankFunc(df2["My child prefers activities that are excitingly unpredictable."])
df2["CarefulInt"]=childRankFunc(df2["My child thinks a lot about how he/she is doing."])
df2["ExploringInt"]=childRankFunc(df2["My child is always looking for experiences that challenge how he/she thinks about themselves and the world."])
df2["PeerSimilarityInt"]=childRankFunc(df2["My child’s behavior is similar to that of his/her friends."])
df2["ChallengeInt"]=childRankFunc(df2["My child views challenging situations as an opportunity to grow and learn."])
df2["ConsequenceInt"]=childRankFunc(df2["My child usually judges what he/she is doing by the consequences of his/her actions."])
df2["UnfamiliarInt"]=childRankFunc(df2["My child is the kind of person who embraces unfamiliar people, events, and places."])
df2["GrowUpInt"]=childRankFunc(df2["My child knows who he/she wants to be."])
df2["PunishmentInt"]=childRankFunc(df2["My child does not learn well from punishment."])
df2["ComplexInt"]=childRankFunc(df2["My child is at his/her best when doing something that is complex or challenging."])
df2["ObvliousInt"]=childRankFunc(df2["Often my child does not notice what he/she is doing until someone calls it to his/her attention."])
df2["UncertaintyInt"]=childRankFunc(df2["My child is the type of person who really enjoys the uncertainty of everyday life."])
df2["StandardsInt"]=childRankFunc(df2["My child has personal standards, and tries to live up to them."])
df2["SweetsInt"]=childRankFunc(df2["It’s hard for my child to notice when he/she has had enough (food or sweets)."])
df2["ProgressInt"]=childRankFunc(df2["My child usually keeps track of his/her progress toward his/her goals."])
df2["NotOvereatInt"]=childRankFunc(df2["My child is usually careful not to overdo it when working, eating, drinking."])
df2["SelfConciousInt"]=childRankFunc(df2["My child thinks a lot about what other people think of him/her."])
df2["ComparingInt"]=childRankFunc(df2["My child tends to compare himself/herself with other people."])
df2["SimiliarBehaviorInt"]=childRankFunc(df2["My child’s behavior is not that different from other people’s."])
df2["IndifferentInt"]=childRankFunc(df2["My child does not care if he/she is different from most people."])
df2["SeekChallengeInt"]=childRankFunc(df2["My child frequently seeks out opportunities or situations to challenge themselves and grow as a person."])
df2["ElectronicsInt"]=timefunc2(df2["On average, how much time per day does your child spend using electronics (such as television, computers, etc.)?"])
df2["HomeworkInt"]=timefunc2(df2["On average, how much time per day does your child spend on his/her schoolwork?"])
df2["SiblingRelationshipInt"]=df2["If your child has siblings, how well do they get along?"]
df2["SiblingsInt"]=df2["How many siblings does your child have that live at home?"]
df2["PeerRelationshipInt"]=  df2["How well does your child get along with other children of their age, whether at camp or at school?"]


df["GritScore"]= df["HardWorkerInt"] - df["FocusInt"] + df["SetbacksInt"] + df["CompletionInt"] - df["DistractedInt"] - df["InterestsInt"] - df["DifferentGoalsInt"] + df["OvercomeSetbacksInt"] + df["DiligenceInt"] - df["LostFocusInt"]


df["EmpathyScore"]= df["MoodsInt"] - df["HappyInt"] + df["ExcitementInt"] - df["DodgingInt"] - df["ApatheticInt"] + df["EmpathyInt"] + df["KindnessInt"] + df["ConcernInt"] + df["RespectInt"] - df["MisfortunteInt"]
    

df2["CuriosityScore"]= df2["ExperiencesInt"] + df2["SeekInfoInt"] + df2["FrighteningInt"] + df2["UnpredictableInt"] + df2["ExploringInt"] + df2["ChallengeInt"] + df2["UnfamiliarInt"] + df2["ComplexInt"] + df2["UncertaintyInt"] + df2["SeekChallengeInt"]


df2["SelfRegulationScore"]= 0 - df2["ImitationInt"] - df2["AttentionInt"] - df2["CasualityInt"] + df2["MistakesInt"] + df2["CarefulInt"] - df2["PeerSimilarityInt"] + df2["ConsequenceInt"] + df2["GrowUpInt"] - df2["PunishmentInt"] - df2["ObvliousInt"] + df2["StandardsInt"] - df2["SweetsInt"] + df2["ProgressInt"] + df2["NotOvereatInt"] -  df2["SelfConciousInt"] - df2["ComparingInt"] - df2["SimiliarBehaviorInt"] + df2["IndifferentInt"]


vGrit = df["GritScore"].values
vEmpathy = df["EmpathyScore"].values
vCuriosity = df2["CuriosityScore"].values
vSelfRegulation = df2["SelfRegulationScore"].values

gritMean = np.mean(vGrit)
empathyMean = np.mean(vEmpathy)
curiosityMean = np.mean(vCuriosity)
selfRegulationMean = np.mean(vSelfRegulation)

gritMedian = np.median(vGrit)
empathyMedian = np.median(vEmpathy)
curiosityMedian = np.median(vCuriosity)
selfRegulationMedian = np.median(vSelfRegulation)

gritSTD = np.std(vGrit)
empathySTD = np.std(vEmpathy)
curiositySTD = np.std(vCuriosity)
selfRegulationSTD = np.std(vSelfRegulation)

print(df2["Zipcode"])

#print("gritMean =" + gritMean)

"""print("gritMean= %s" %gritMean)
print("gritMedian= %s" %gritMedian)
print("gritSTD= %s" %gritSTD)
print("empathyMean= %s" %empathyMean)
print("empathyMedian= %s" %empathyMedian)
print("empathySTD= %s" %empathySTD)
print("curiosityMean= %s" %curiosityMean)
print("curiosityMedian= %s" %curiosityMedian)   
print("curiositySTD= %s" %curiositySTD)
print("selfRegulationMean= %s" %selfRegulationMean)
print("selfRegulationMedian= %s" %selfRegulationMedian)
print("selfRegulationSTD= %s" %selfRegulationSTD)"""


#print(df.shape)
#print(df2.shape)
#np.corr
#print(df)
#print(df2)
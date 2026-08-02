# Your name:
# Your age:
# Your school:
# Your favorite subject:
# How many hours did you study today?
# Three topics you want to learn:

name = input("your name: ")
age = input("your age: ")
school = input("your school: ")
fav_subject = input("your favorite subject:")
study_hour = input("your study hour today: ")
topic_1 = input("what is the first topic you want to learn: ")
topic_2 = input("what is the second topic you want to learn: ")
topic_3 = input("what is the third topic you want to learn: ")


name = name.strip().title()
age = int(age)
school = school.strip().upper()
fav_subject = fav_subject.lower()
study_hour = float(study_hour)
topics = [topic_1, topic_2, topic_3]
topics = sorted(topics)
weekly_study = study_hour * 7

print(f"your name: {name}")
print(f"you are: {age} years old")
print(f"your school: {school}")
print(f"your favorite subject: {fav_subject}")
print(f"your weekly study hours: {weekly_study}")
print(f"your want-to-learn topics: {topics}")
import pandas as pd

# Load the CSV file
file_path = '/home/najiya/queen_puzzle/mental-health-analysis-using-BERT/data conversion/depression survey(Responses) - Form responses 1 (1).csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Define mappings for converting options to numerical values
mappings = {
    "How often do you feel sad?": {
        "I do not feel sad.": 0,
        "I feel sad.": 1,
        "I am sad all the time and I can't snap out of it.": 2,
        "I am so sad and unhappy that I can't stand it.": 3,
    },
    "How do you feel about the future?": {
        "I am not particularly discouraged about the future.": 0,
        "I feel discouraged about the future.": 1,
        "I feel I have nothing to look forward to.": 2,
        "I feel the future is hopeless and that things cannot improve.": 3,
    },
    "How do you perceive your accomplishments?": {
        "I do not feel like a failure.": 0,
        "I feel I have failed more than the average person.": 1,
        "As I look back on my life, all I can see is a lot of failures.": 2,
        "I feel I am a complete failure as a person.": 3,
    },
    "Do you enjoy activities as much as you used to?":{
        "I get as much satisfaction out of things as I used to.": 0,
        "I don't enjoy things the way I used to.": 1,
        "I don't get real satisfaction out of anything anymore.": 2,
        "I am dissatisfied or bored with everything.": 3,
    },
    "Do you feel guilty?": {
        "I don't feel particularly guilty.": 0,
        "I feel guilty a good part of the time.": 1,
        "I feel quite guilty most of the time.": 2,
        "I feel guilty all the time.": 3,
    },
    "Do you feel like you're being punished?": {
        "I don't feel I am being punished.": 0,
        "I feel I may be punished.": 1,
        "I expect to be punished.": 2,
        "I feel I am being punished.": 3,
    },
    "How do you feel about yourself?": {
        "I don't feel disappointed in myself.": 0,
        "I am disappointed in myself.": 1,
        "I am disgusted with myself.": 2,
        "I hate myself.": 3,
    },
    "Do you blame yourself for problems?": {
        "I don't feel I am any worse than anybody else.": 0,
        "I am critical of myself for my weaknesses or mistakes.": 1,
        "I blame myself all the time for my faults.": 2,
        "I blame myself for everything bad that happens.": 3,
    },
    "Do you have thoughts of self-harm?": {
        "I don't have any thoughts of killing myself.": 0,
        "I have thoughts of killing myself, but I would not carry them out.": 1,
        "I would like to kill myself.": 2,
        "I would kill myself if I had the chance.": 3,
    },
    "How often do you cry?": {
        "I don't cry any more than usual.": 0,
        "I cry more now than I used to.": 1,
        "I cry all the time now.": 2,
        "I used to be able to cry, but now I can't cry even though I want to.": 3,
    },
    "Do you feel irritated?": {
        "I am no more irritated by things than I ever was.": 0,
        "I am slightly more irritated now than usual.": 1,
        "I am quite annoyed or irritated a good deal of the time.": 2,
        "I feel irritated all the time.": 3,
    },
    "Have you lost interest in others?": {
        "I have not lost interest in other people.": 0,
        "I am less interested in other people than I used to be.": 1,
        "I have lost most of my interest in other people.": 2,
        "I have lost all of my interest in other people.": 3,
    },
    "How well do you make decisions?": {
        "I make decisions about as well as I ever could.": 0,
        "I put off making decisions more than I used to.": 1,
        "I have greater difficulty in making decisions than before.": 2,
        "I can't make decisions at all anymore.": 3,
    },
    "How do you feel about your appearance?": {
        "I don't feel that I look any worse than I used to.": 0,
        "I am worried that I am looking old or unattractive.": 1,
        "I feel there are permanent changes in my appearance that make me look unattractive.": 2,
        "I believe that I look ugly.": 3,
    },
    "How well do you work?": {
        "I can work about as well as before.": 0,
        "It takes an extra effort to get started doing something.": 1,
        "I have to push myself very hard to do anything.": 2,
        "I can't do any work at all.": 3,
    },
    "How well do you sleep?": {
        "I can sleep as well as usual.": 0,
        "I don't sleep as well as I used to.": 1,
        "I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.": 2,
        "I wake up several hours earlier than I used to and cannot get back to sleep.": 3,
    },
    "How often do you feel tired?": {
        "I don't get more tired than usual.": 0,
        "I get tired more easily than I used to.": 1,
        "I get tired from doing almost anything.": 2,
        "I am too tired to do anything": 3,
    },
    "How is your appetite?": {
        "My appetite is no worse than usual.": 0,
        "My appetite is not as good as it used to be.": 1,
        "My appetite is much worse now.": 2,
        "I have no appetite at all anymore.": 3,
    },
    "Have you lost weight?": {
        "I haven't lost much weight, if any, lately.": 0,
        "I have lost more than five pounds.": 1,
        "I have lost more than ten pounds.": 2,
        "I have lost more than fifteen pounds.": 3,
    },
    "Are you worried about your health?": {
        "I am no more worried about my health than usual.": 0,
        "I am worried about physical problems like aches, pains, or constipation.": 1,
        "I am very worried about physical problems and it's hard to think of much else.": 2,
        "I am so worried about my physical problems that I cannot think of anything else.": 3,
    },
    "Have you noticed any changes in your interest in forming close personal connections?": {
        "I have not noticed any changes.": 0,
        "I am somewhat less interested than before.": 1,
        "I have very little interest now.": 2,
        "I have completely lost interest.": 3,
        "I have not noticed any recent change in my interest in sex.": 0,
        "I have almost no interest in sex.": 2,
    },

    
    # Repeat for all questions in your dataset
}

# Apply the mappings to convert text to numerical values
for question, mapping in mappings.items():
    if question in data.columns:
        data[question] = data[question].map(mapping)

# Save the converted data to a new CSV file
output_path = '/home/najiya/queen_puzzle/mental-health-analysis-using-BERT/data conversion/depression survey(numerical_stResponses).csv'  # Replace with desired output file path
data.to_csv(output_path, index=False)

print(f"Numerical data saved successfully to {output_path}")

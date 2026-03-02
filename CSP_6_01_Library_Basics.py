import analytics
#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices:list):
    for i in range(len(rawPrices)):
        y = round(analytics.apply_markup(rawPrices[i],0.15))
        rawPrices[i] = y
    return(rawPrices)

# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
#these are my grades, YOU guess ¯\_(ツ)_/¯
def analyze_scores(scores:list):
    n=len(scores)
    x=analytics.get_highest(scores)
    y=analytics.get_average(scores)
    z = int(y)
    return(x,z)
analyze_scores([77,81,86,87,90,94,95])

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(stuff:list):

    analytics.clean_text(stuff)
    return analytics.clean_text(stuff)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(numbers:list):
    analytics.filter_threshold(numbers,100)
    return analytics.filter_threshold(numbers,100)


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case words with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(words,target):
    location = -1
    for i in range(len(words)):
        if words[i] == target:
            break
        else:
            location+=1
            continue
    analytics.clean_text(words)
    return analytics.clean_text(words), location
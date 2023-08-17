def word():
    article= input("Enter your article: ")
    replacement= input(" write your replacement words here: ")
    new_word= input("write your new word here: ")
    new_article= article.replace(replacement,new_word)
    print(new_article)
word()
Good evening sir..
I have developed a REST API using python and FAST APIthat accepts a small piece of text adn analyzes it. It returns word count, character count, unique words, sentenfce count, average word length and upper and lower cases of the given text.

The flow is:
user sends a text--_>POST ANALYZE-->PYDANTIC validates the input-->py analyzes the etxt--> results are stored in return dict as py returns JSON.

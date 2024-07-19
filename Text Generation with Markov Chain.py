import random


def train_markov_chain(text, n=2):
    """Train a Markov chain on the given text."""
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain


def generate_text(markov_chain, start_words, num_words=100):
    """Generate text from the trained Markov chain."""
    current_words = list(start_words)
    generated_text = list(current_words)

    for _ in range(num_words):
        current_key = tuple(current_words)
        if current_key in markov_chain:
            next_word = random.choice(markov_chain[current_key])
            generated_text.append(next_word)
            current_words = current_words[1:] + [next_word]
        else:
            break

    return ' '.join(generated_text)


# Sample love story text
sample_text = """
Once upon a time in a small village, there was a beautiful girl named Lily. She had a kind heart and a bright smile. One day, a young man named Jack moved into the village. He was charming and had a gentle demeanor. From the moment they met, Lily and Jack felt an instant connection. They spent their days talking and laughing, sharing their dreams and secrets. As the days passed, their bond grew stronger, and they fell deeply in love. They promised to support each other through thick and thin, and their love story became a legend in the village.
"""

# Train Markov chain and generate text
if __name__ == "__main__":
    n = 2  # Number of words to use in the state
    markov_chain = train_markov_chain(sample_text, n)
    start_words = ("Once", "upon")  # Starting words for the generation
    generated_text = generate_text(markov_chain, start_words, num_words=100)
    print(generated_text)

import emoji


def show_emoji():
    text = emoji.emojize(
        "Hello :smile: :rocket:",
        language="alias"
    )
    print(text)
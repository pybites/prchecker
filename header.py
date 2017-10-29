feedback_messages = [
    "It's not too late to start!",
    "Off to a great start, keep going!",
    "Half way there, keep it up!",
    "So close!",
    "Way to go!",
    "Now you're just showing off!"
]


def get_header(prs):
    if prs is None:
        return feedback_messages[0]

    if prs.totalCount > 4:
        return feedback_messages[-1]

    return feedback_messages[prs.totalCount]

feedback_messages = [
    "It's not too late to start!",
    "Off to a great start, keep going!",
    "Half way there, keep it up!",
    "So close!",
    "Way to go!",
    "Now you're just showing off!"
]


def get_header(prs):
    num_prs = len(prs)

    if num_prs > 4:
        return feedback_messages[-1]

    return feedback_messages[num_prs]

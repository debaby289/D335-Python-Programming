'''
A user is asked to type a caption for a photo in a web form's text field. If the caption didn't end with a punctuation mark (. ! ?), a period should automatically be added. A common error is to end with a comma, which should be replaced by a period. Another common error is to end with two periods, which should be changed to one period (however, ending with three periods (or more) indicates ellipses so should be kept as is). The corrected caption is output.

If the input is "I like pie", the output is "I like pie." If the input is "I like pie!", the output remains "I like pie!" If the input is "Coming soon…", the output remains "Coming soon…"

Hints:
    Start by checking for ! or ? which don't require any action.
    Then check for , which requires the simple action of replacing by a period. In Python, this requires using replace() on the string.
    Then check for two ending periods (making sure the caption is at least 2 characters long). If found, check for three ending periods (making sure caption is at least 3 characters long), in which case no action required. Otherwise, remove the last period.
'''
user_caption = input()

# No action needed for ! or ?
if user_caption[-1] in '!?':
    pass

# Replace comma with period
elif user_caption[-1] == ',':
    user_caption = user_caption[:-1] + '.'

# Handle double period (but not ellipses)
elif user_caption.endswith('..') and not user_caption.endswith('...'):
    user_caption = user_caption[:-1]

# Add period if no punctuation
elif user_caption[-1] not in '.!?,':
    user_caption += '.'

print(user_caption)
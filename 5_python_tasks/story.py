story = {
    'start': 'Once upon a time...',
    'middle': '...and...',
    'end': '... the end.',
}

print(story)
print(type(story))
print(story.keys())
print(story.values())

for story in story.values():
    print(story)

story['hero'] = 'Batman'
print(story)
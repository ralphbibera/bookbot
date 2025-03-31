def get_num_words(content):
    return len(content.split())


def get_character_count(content):
    character_count = {}
    lower_case = content.lower()
    words = lower_case.split()
    for word in words:
        for char in word:
            if character_count.get(char):
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def character_counts(text):
    text_lower = text.lower()
    character_dict = {}
    for char in text_lower:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_on(item):
    return item["num"]

def get_sorted_character_list(text):

    character_dict = character_counts(text)
    character_list = []
    for character in character_dict:
        if character.isalpha():
            character_list.append(
                {"char": character, "num": character_dict[character]}
                )
    character_list.sort(reverse=True, key=sort_on)

    return character_list

def get_word_count(text):
    return len(text.split())

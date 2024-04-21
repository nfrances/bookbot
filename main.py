def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    character_dict = get_characters(file_contents)
    chars_sorted_list = chars_dict_sorted(character_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' was found {item['num']} times")
    print ("--- End Report ---")


def get_book_text(book_path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_characters(file_contents):
    lowered_file_contents = file_contents.lower()
    letters = []
    for letter in lowered_file_contents:
        letters.append(letter)
    character_dict = {}
    for character in letters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(d):
    return d["num"]

def chars_dict_sorted(character_dict):
    sorted_list=[]
    for ch in character_dict:
        sorted_list.append({"char": ch, "num": character_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

        
main()
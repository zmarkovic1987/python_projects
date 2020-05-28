# my_price = 78.55
# my_tip = 20
#
# def calculate_total(price, percent):
#     tip = price*percent/100
#     new_number = price + tip
#     return new_number
#
#
# print(calculate_total(my_price, my_tip))


def read_file(my_file):
    odd_lines = []
    even_lines = []
    line_count = 0

    for e in my_file:
        line_count += 1
        stripped_line = e.replace('\n', '')
        if line_count % 2 == 0:
            even_lines.append(stripped_line)
        elif line_count % 2 != 0:
            odd_lines.append(stripped_line)
    return odd_lines, even_lines

def sanitize(sanitize_list):
    clean_string = []

    for st in sanitize_list:
        st = st.replace('/', '')
        st = st.replace(':', '')
        st = st.replace('-', '')
        st = st.replace('+', '')
        st = st.replace('(', '')
        st = st.replace(')', '')
        st = st.replace(' ', '')
        clean_string.append(st)

    return clean_string



def analyze_friends(names, clean_phones, area_codes, states):

    def get_unique_area_codes():
        unique_area_codes = []
        for ar in area_codes:
            if ar[0:3] not in unique_area_codes:
                unique_area_codes.append(ar)
        return unique_area_codes

    unique_area_codes_list = get_unique_area_codes()
    print('You have ' + str(len(names)) + ' friends in a list')
    print('They live in ' + str(states))
    print('Their area codes are ' + str(unique_area_codes_list))


friends_file = open('data_file')
[names, phones] = read_file(friends_file)
map_file = open('map_areacodes_states.txt')
[area_codes, states] = read_file(map_file)

clean_phones = sanitize(phones)
analyze_friends(names, phones, area_codes, states)

friends_file.close()
map_file.close()

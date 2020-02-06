############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    Muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    Muskmelon.add_pairing(["mint"])

    Casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    Casaba.add_pairing(["strawberries", "mint"])

    Crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    Crenshaw.add_pairing(["proscuitto"])

    Yellow_Watermelon = MelonType("yw", 2013, "yellow", False, True,
                                  "Yellow Watermelon")
    Yellow_Watermelon.add_pairing(["ice cream"])

    all_melon_types.extend([Muskmelon, Casaba, Crenshaw, Yellow_Watermelon])

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    dict_melons = {}

    for melon in melon_types:
        dict_melons[melon.code] = melon

    return dict_melons

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


    def __init__(self, shape_rating, color_rating, field_number, melon_type, harvester):
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_number = field_number
        self.melon_type = melon_type
        self.harvester = harvester

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field_number != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_type_dict = make_melon_type_lookup(melon_types)
    melon_1 = Melon(8, 7, 2, melon_type_dict['yw'], 'Sheila')
    melon_2 = Melon(3, 4, 2, melon_type_dict['yw'], 'Sheila')
    melon_3 = Melon(9, 8, 3, melon_type_dict['yw'], 'Sheila')
    melon_4 = Melon(10, 6, 35, melon_type_dict['cas'], 'Sheila')
    melon_5 = Melon(8, 9, 35, melon_type_dict['cren'], 'Michael')
    melon_6 = Melon(8, 2, 35, melon_type_dict['cren'], 'Michael')
    melon_7 = Melon(2, 3, 4, melon_type_dict['cren'], 'Michael')
    melon_8 = Melon(6, 7, 4, melon_type_dict['musk'], 'Michael')
    melon_9 = Melon(7, 10, 3, melon_type_dict['yw'], 'Sheila')

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
            melon_8, melon_9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    sellable = None
    for melon in melons:
        if melon.is_sellable():
            sellable = 'CAN BE SOLD'
        else:
            sellable = 'NOT SELLABLE'
        print(f'Harvested by {melon.harvester} from Field {melon.field_number} {sellable}')

# further study


def make_melons_from_log(filepath, melon_types):
    file = open(filepath)

    melon_type_dict = make_melon_type_lookup(melon_types)
    melons = []

    for line in file:
        words = line.split()
        melon = Melon(words[1], words[3], words[11],
                      melon_type_dict[words[5]], words[8])
        melons.append(melon)

    return melons

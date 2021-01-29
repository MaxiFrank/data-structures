"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    open_file = open(filename)

    for line in open_file:
      house = line.split('|')[2]
      if house:
        houses.add(house)
    return houses

def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    open_file = open(filename)
    if cohort == 'All':
      students = []
      for line in open_file:
        clean_line = line.rstrip().split('|')
        if clean_line[4] != 'I' and clean_line[4] != 'G':
          students.append(clean_line[0] + ' ' + clean_line[1])

    if cohort != 'All':
      students = []
      for line in open_file:
        clean_line = line.rstrip().split('|')
        if clean_line[4] == cohort:
          students.append(clean_line[0] + ' ' + clean_line[1])

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = all_names_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    open_file = open(filename)
    for line in open_file:
      first, last, house, _, i_g = line.rstrip().split('|')
      if house.lower() == "dumbledore's army": # why does lower(house) not work??
        dumbledores_army.append(first + ' ' + last)
      if house.lower() == 'gryffindor':
        gryffindor.append(first + ' ' + last)
      if house.lower() == 'hufflepuff':
        hufflepuff.append(first + ' ' + last)
      if house.lower() == 'ravenclaw':
        ravenclaw.append(first + ' ' + last)
      if house.lower() == 'slytherin':
        slytherin.append(first + ' ' + last)
      if i_g == 'G':
        ghosts.append(first + ' ' + last)
      if i_g == 'I':
        instructors.append(first + ' ' + last)
    return [sorted(ls) for ls in [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts,instructors]]

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file = open(filename)

    for line in file:
      first, last, house, advisor, cohort = line.rstrip().split('|')
      all_data.append((first + ' ' + last, house, advisor, cohort))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    file = open(filename)

    for line in file:
      first, last, house, advisor, cohort = line.rstrip().split('|')
      if first + ' ' + last == name:
        return cohort
      


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_duped_last_names(('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    file = open(filename)

    all_names = []
    repeated_names = set()
    for line in file:
      first, last, house, advisor, cohort = line.rstrip().split('|')
      all_names.append(last)

    for idx in range(len(all_names) - 1):
      if all_names[idx] in all_names[idx+1:]:
        repeated_names.add(all_names[idx])
    return list(repeated_names)

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    dumbledores_army = [] #list of list of tuples
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []

    open_file = open(filename)
    for line in open_file:
      first, last, house, advisor, cohort = line.rstrip().split('|')
      if house.lower() == "dumbledore's army":
        dumbledores_army.append((first + ' ' + last, cohort))
      if house.lower() == 'gryffindor':
        gryffindor.append((first + ' ' + last, cohort))
      if house.lower() == 'hufflepuff':
        hufflepuff.append((first + ' ' + last, cohort))
      if house.lower() == 'ravenclaw':
        ravenclaw.append((first + ' ' + last, cohort))
      if house.lower() == 'slytherin':
        slytherin.append((first + ' ' + last, cohort))
      
    current_cohort = None
    current_ls = None

    for ls in [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin]:
      for tuple_ in ls:
        if tuple_[0] == name:
          current_cohort = tuple_[1] # variables are only available at their current indent
          current_ls = ls
          break # break only breaks out of the current loop
    
    classmate_set = set()
    for tuple_ in current_ls:
      if tuple_[1] == current_cohort:
        classmate_set.add(tuple_[0])
    classmate_set.remove(name)
    
    return classmate_set

# ##############################################################################
# # END OF MAIN EXERCISE.  Yay!  You did it! You Rock!


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')


from naber import constant


color = constant.BColors()


def multiline_content(number):
    """ EOF """
    if not zero_checker(number):
        number = 3
        print(f"Default lines 3")
        print(f'You have "3" lines')
    else:
        print(f'You have "{number}" '
              + is_plural(number,'line'))

    print(color_green_info('Write your content.\n'))
    counter = number
    lines = ""
    for i in range(number):
        lines += input('('+str(counter)+')'+" >> ")+"\n"
        counter = counter-1

    title = input(color_green_info('Write your title.')+'\n >> ')
    return title, lines


def minimalize_string(string):
    if len(string) > 11:
        return string[:7]+'..'
    return string
                   
    


def zero_checker(number):
    if number < 1:
        return False
    return True


def is_plural(number,string):
    """ check the number """
    if number > 1:
        return do_plural(string)
    return string


def do_plural(string):
    """ add to 's' end of string """
    return string+'s'
    

def color_green_info(string):
    """ switch string color to green """
    return f'{color.OKGREEN}{string}\
    {color.ENDC}'


def color_blue_status(string):
    """ switch string color to blue """
    return f'{color.OKBLUE}{string}\
    {constant.BColors.ENDC}'


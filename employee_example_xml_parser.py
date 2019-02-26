import xml.etree.ElementTree as etree


def get_namespaces(path):
    """
    Grabs the various namesspaces in the xml document
    """
    nsmap = {}
    for event, elem in etree.iterparse(
            path,
            events=('start', 'end', 'start-ns', 'end-ns')):
        if event == 'start-ns':
            ns, url = elem
            nsmap[ns] = url #this eats a lot of memory i think
        elif event == 'end-ns':
            pass
        if event == 'start' and elem.tag == 'Employee':
            print('Employee id: ', elem.get('id')) # for this particular xml file grabs the employee id
            print('Employee id: ', elem.find('age').text) # gets the name of the employee
            print('Employee name: ', elem.find('name').text)
            print('Employee gender: ', elem.find('gender').text)
            print('Employee role: ', elem.find('role').text)
            print('<<-------------------------------------------->>')
        else: # this is an element
            #print(elem.tag) # printing the of the lement
            elem.clear() # clearing the node from memory

    # if the dictionary is empty dont print/return
    if nsmap:
        print(nsmap)

def parse_xml(path):
    nsmap = {}
    for event, elem in etree.iterparse(
            path,
            events=('start', 'end', 'start-ns', 'end-ns')):
        print(elem)


def parse_xml2(path):
    parser = etree.XMLPullParser(events=('start','end'))
    parser.feed(path)
    print(list(parser.read_events()))

def main():
    path = '/home/apluser/Data/xml_data/employees.xml'
    #path = '/home/apluser/uniprot_test_small_2_entry.xml'
    #path = '/home/apluser/uniprot_sprot.xml'
    #path = '/home/mcdansl1/Data/uniprot_sprot.xml'
    #parse_xml2(path)
    get_namespaces(path)
    #parse_xml(path)

if (__name__ == "__main__"):
    main()

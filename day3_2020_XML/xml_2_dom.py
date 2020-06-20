from xml.dom.minidom import parse
import xml.dom.minidom

# DOMTree = xml.dom.minidom.parse("Student.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#     print ("Root element : %s " %collection.getAttribute("shelf"))
tai_lieu = parse('files_xml/student.xml')
node_root = tai_lieu.documentElement
students = node_root.getElementsByTagName ("student")

for student in students:
    print (student.getAttribute('id'))
    print (student.getElementsByTagName("name")[0].childNodes[0].data)
    print (student.getElementsByTagName("date")[0].childNodes[0].data)
    print()
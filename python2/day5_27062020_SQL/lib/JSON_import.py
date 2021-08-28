import json
def read_json_local(directory):
    f = open (directory,encoding="utf-8")
    content = json.load(f)
    f.close()
    return content
def write_json_local(directory,content):
    f  =open(directory,"w",encoding="utf-8")
    json.dump(content,f,ensure_ascii=False,indent = 4)
    f.close()
    return True
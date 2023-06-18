#json package to work on JSON file
import json

#This class has methods to convert json to text
class ReadJson:

    """
    This method is used to take json file read it and 
    convert it into text
    """
    def read_json(self,filename):
        file=open(filename,'r')
        js=file.read()
        texts=json.loads(js)
        single_text=""
        for i in range(0,len(texts)):
            single_text+=texts[i]+" "
        return single_text
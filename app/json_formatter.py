
import json

def to_json(from_json_string):
    """ Função utilitaria que devolve o json com indentação e sem caracteres de escape """
    return json.dumps(json.loads(from_json_string), indent=4, ensure_ascii=False)
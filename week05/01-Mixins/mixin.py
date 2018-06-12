import json

import xml.etree.ElementTree as ET


class Jsonable:
    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )

    def prepare_for_serialization(self):
        class_name = self.__class__.__name__
        dict_ = {}

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                dict_[k] = v
            elif isinstance(v, Jsonable):
                dict_[k] = v.prepare_for_serialization()
            else:
                raise ValueError()

        return {'class_name': class_name, 'dict': dict_}

    def to_json(self):
        return json.dumps(self.prepare_for_serialization(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        result = json.loads(json_str)
        if cls.__name__ != result['class_name']:
            raise ValueError('The classes are different')
        return cls(**result['dict'])


class Xmlable:

    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )

    def prepare_for_serialization(self):
        class_name = self.__class__.__name__
        dict_ = {}

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                dict_[k] = v
            elif isinstance(v, Jsonable):
                dict_[k] = v.prepare_for_serialization()
            else:
                raise ValueError()

        return {'class_name': class_name, 'dict': dict_}

    def to_xml(self):
        dict_ = self.prepare_for_serialization()['dict']
        elem = ET.Element(self.__class__.__name__)
        for key, value in dict_.items():
            if isinstance(value, dict):
                child_elem = ET.Element(key)
                for k, v in value.items():
                    child = ET.Element(k)
                    child.text = str(v)
                    child_elem.append(child)
                elem.append(child_elem)
            else:
                child = ET.Element(key)
                child.text = str(value)
                elem.append(child)
        return ET.tostring(elem)

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        # print(root.tag)
        dict_ = {}
        my_dict = dict()
        result = root.getchildren()
#        print('Result', result)
        for child in result:
            if child.text is None:
                for children in child:
#                   print(children.tag, children.text)
                    my_dict[children.tag] = children.text
#                   print('Children', children)
#                   print(child.tag)
                dict_.update(my_dict)
#               print(my_dict)
            else:
                if child.text is not None:
                    try:
                        int(child.text)
                        dict_[child.tag] = int(child.text)
                    except ValueError:
                        dict_[child.tag] = child.text
        if cls.__name__ != root.tag:
            raise ValueError('The classes are different')
        return cls(**dict_)


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Person(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__